"""Run full upstream URL/DAO method variants against an isolated MongoDB."""
import argparse, difflib, hashlib, json, os, subprocess, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from urllib.parse import quote

p=argparse.ArgumentParser()
p.add_argument("--source",type=Path,required=True)
p.add_argument("--report",type=Path,required=True)
p.add_argument("--work",type=Path,required=True)
p.add_argument("--output",type=Path,required=True)
a=p.parse_args()
expected="302dad92e1549b7a84ce73eded447ad5d18124f0"
assert subprocess.check_output(["git","rev-parse","HEAD"],cwd=a.source,text=True).strip()==expected,"Pinned source required"
a.work.mkdir(parents=True,exist_ok=True);a.output.mkdir(parents=True,exist_ok=True)
tree=ET.parse(a.report)
assert tree.getroot().get("tests")=="1" and tree.getroot().get("failures")=="0" and tree.getroot().get("errors")=="0", "Baseline must actually execute and pass"
props={x.get("name"):x.get("value") for x in tree.findall("./properties/property")}
cp=props.get("surefire.test.class.path",props["java.class.path"])
# A manifest classpath avoids Windows command length limits.
uris=[]
for entry in cp.split(os.pathsep):
    path=Path(entry).resolve()
    uris.append(quote(os.path.relpath(path,a.work.resolve()).replace(os.sep,"/"))+ ("/" if path.is_dir() else ""))
manifest="Manifest-Version: 1.0\r\n"
line="Class-Path: "+" ".join(uris)
while len(line)>70:
    manifest+=line[:70]+"\r\n";line=" "+line[70:]
manifest+=line+"\r\n\r\n"
launcher=a.work/"classpath.jar"
with zipfile.ZipFile(launcher,"w") as z:z.writestr("META-INF/MANIFEST.MF",manifest)
runner=a.work/"AuditRunner.java"
runner.write_text('public class AuditRunner { public static void main(String[] args) { try { new com.akto.test_editor.filter.UrlPrivateContextAuditTest().auditDatabaseUrlBranch(); System.exit(0); } catch(Throwable e) { e.printStackTrace(); System.exit(1); } } }',encoding="utf-8")
classes=a.work/"runner";classes.mkdir(exist_ok=True)
subprocess.run(["javac","-encoding","UTF-8","-cp",str(launcher),"-d",str(classes),str(runner)],check=True)
path=a.source/"libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java"
raw=path.read_bytes();original=raw.decode("utf-8").replace("\r\n","\n")
committed=subprocess.check_output(["git","show","HEAD:libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java"],cwd=a.source).decode("utf-8").replace("\r\n","\n")
assert original==committed,"Production source must match pinned commit"
needle="                    singleTypeInfo = new SingleTypeInfo();\n"
assert original.count(needle)==1
removed=original.replace(needle,"")
candidate=removed.replace(
"                    BasicDBObject obj = new BasicDBObject();\n                    if (singleTypeInfo != null && singleTypeInfo.getIsPrivate())",
"                    BasicDBObject obj = new BasicDBObject();\n                    if (singleTypeInfo != null && !singleTypeInfo.getIsPrivate()) {\n                        continue;\n                    }\n                    if (singleTypeInfo != null && singleTypeInfo.getIsPrivate())",1)
start=candidate.index("public BasicDBObject getPrivateResourceCount")
fallback=candidate.index("                            privateCnt++;",start)
candidate=candidate[:fallback]+candidate[fallback:].replace("                            privateCnt++;","                            if (singleTypeInfo == null) {\n                                privateCnt++;\n                            }",1)
assert candidate!=removed
patch="".join(difflib.unified_diff(original.splitlines(True),candidate.splitlines(True),fromfile="a/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java",tofile="b/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java"))
(a.output.parent/"reproduction/url-private-context-candidate.patch").write_text(patch,encoding="utf-8")
runs=[]
for variant,text in [("baseline",original),("remove_overwrite_only",removed),("candidate",candidate)]:
    overlay=a.work/variant;overlay.mkdir(exist_ok=True)
    java=overlay/"FilterAction.java";java.write_text(text,encoding="utf-8")
    subprocess.run(["javac","-encoding","UTF-8","-cp",str(launcher),"-d",str(overlay),str(java)],check=True)
    result=a.output/f"2026-10-05-url-{variant}.json"
    command=["java","-Dfile.encoding=UTF-8",f"-Daudit.variant={variant}",f"-Daudit.output={result}","-cp",os.pathsep.join([str(overlay),str(classes),str(launcher)]),"AuditRunner"]
    with (a.work/f"{variant}.log").open("w",encoding="utf-8") as log:subprocess.run(command,stdout=log,stderr=log,check=True)
    data=json.loads(result.read_text(encoding="utf-8"))
    assert len(data["cases"])==8
    runs.append({"variant":variant,"source_sha256":hashlib.sha256(text.encode()).hexdigest(),"cases":8,"checks":"count expectations, public values exclusion, private observed value preservation"})
    print(json.dumps({"variant":variant,"cases":[{"case":r["case"],"count":r["result"]["privateCount"],"values":r["result"]["values"]} for r in data["cases"]]},ensure_ascii=False))
assert path.read_bytes()==raw,"Original production source must remain untouched"
(a.output/"2026-10-05-url-provenance.json").write_text(json.dumps({"akto_commit":subprocess.check_output(["git","rev-parse","HEAD"],cwd=a.source,text=True).strip(),"runs":runs,"scope":"Full original FilterAction and MongoDB DAO; shadow classes for variants; no product UI or HTTP replay"},indent=2)+"\n",encoding="utf-8")
