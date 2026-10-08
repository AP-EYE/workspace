"""Run pinned upstream Java methods in isolation, not the Akto server or YAML engine."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.request

AKTO_COMMIT = "302dad92e1549b7a84ce73eded447ad5d18124f0"
TEMPLATE_COMMIT = "ce2267da7e28927876b41d944e63bdde10e41e00"
METHODS = [
    ("libs/utils/src/main/java/com/akto/testing/Utils.java", "public static double compareWithOriginalResponse("),
    ("libs/utils/src/main/java/com/akto/runtime/RuntimeUtil.java", "public static void extractAllValuesFromPayload(String"),
    ("libs/utils/src/main/java/com/akto/runtime/RuntimeUtil.java", "public static void extractAllValuesFromPayload(JsonNode"),
    ("libs/dao/src/main/java/com/akto/dto/type/KeyTypes.java", "public static boolean isPhoneNumber("),
    ("libs/dao/src/main/java/com/akto/dto/type/SingleTypeInfo.java", "public boolean getIsPrivate("),
    ("libs/dao/src/main/java/com/akto/dto/data_types/RegexPredicate.java", "public boolean validate("),
]
DEPENDENCIES = [
    ("com/fasterxml/jackson/core", "jackson-core", "2.16.1"),
    ("com/fasterxml/jackson/core", "jackson-databind", "2.16.1"),
    ("com/fasterxml/jackson/core", "jackson-annotations", "2.16.1"),
    ("com/googlecode/libphonenumber", "libphonenumber", "8.12.41"),
]


def method(text: str, signature: str) -> tuple[str, int]:
    start = text.index(signature)
    opening = text.index("{", start)
    # Lex strings and comments so braces inside them do not alter depth.
    token = re.compile(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|//[^\n]*|/\*[\s\S]*?\*/|[{}]')
    depth = 0
    for item in token.finditer(text, opening):
        if item.group() == "{":
            depth += 1
        elif item.group() == "}":
            depth -= 1
            if depth == 0:
                return text[start:item.end()], text[:start].count("\n") + 1
    raise ValueError(f"Unclosed method: {signature}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--templates", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for path, expected in ((args.source, AKTO_COMMIT), (args.templates, TEMPLATE_COMMIT)):
        actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip()
        if actual != expected:
            raise SystemExit(f"Pinned source required: {expected}, got {actual}")
    args.work.mkdir(parents=True, exist_ok=True)
    jar_dir = args.work / "jars"
    jar_dir.mkdir(exist_ok=True)
    dependencies = []
    for group, artifact, version in DEPENDENCIES:
        filename = f"{artifact}-{version}.jar"
        url = f"https://repo.maven.apache.org/maven2/{group}/{artifact}/{version}/{filename}"
        target = jar_dir / filename
        if not target.exists():
            urllib.request.urlretrieve(url, target)
        with urllib.request.urlopen(url + ".sha1", timeout=30) as response:
            expected = response.read().decode().strip().split()[0]
        data = target.read_bytes()
        if hashlib.sha1(data).hexdigest() != expected:
            raise SystemExit(f"Dependency checksum mismatch: {filename}")
        dependencies.append({"name": filename, "url": url, "sha256": hashlib.sha256(data).hexdigest()})
    blocks, provenance = [], []
    for path, signature in METHODS:
        raw = (args.source / path).read_bytes()
        block, line = method(raw.decode("utf-8"), signature)
        blocks.append(block)
        provenance.append({"path": path, "line": line, "signature": signature,
                           "file_sha256": hashlib.sha256(raw).hexdigest(),
                           "method_sha256": hashlib.sha256(block.encode()).hexdigest()})
    # Original method bodies are inserted unchanged. Fields, input cases, and
    # template gate below are experiment scaffolding, not upstream engine code.
    source = r'''import java.util.*;
import java.util.regex.Pattern;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.google.i18n.phonenumbers.PhoneNumberUtil;
import com.google.i18n.phonenumbers.Phonenumber;
public class Audit {
static ObjectMapper mapper = new ObjectMapper();
static JsonFactory factory = mapper.getFactory();
__COMPARE__
__EXTRACT_STRING__
__EXTRACT_NODE__
__PHONE__
static class SingleTypeInfo {
  public long uniqueCount, publicCount;
  public static final double THRESHOLD = 0.1;
  __PRIVATE__
}
static class RegexPredicate {
  private String value;
  RegexPredicate(String value) { this.value = value; }
  __REGEX__
}
static Map<String,Object> row(String id) {
  Map<String,Object> r=new LinkedHashMap<>(); r.put("id",id); return r;
}
public static void main(String[] args) throws Exception {
  List<Map<String,Object>> rows=new ArrayList<>();
  String[][] pairs={
    {"empty_array","[]","[]"},
    {"empty_object","{}","{}"},
    {"empty_wrapped_array","{\"data\":[]}","{\"data\":[]}"},
    {"identical_shared","[{\"id\":\"shared-a\",\"text\":\"permitted\"}]","[{\"id\":\"shared-a\",\"text\":\"permitted\"}]"},
    {"identical_forbidden","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]"},
    {"foreign_private_to_empty","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[]"},
    {"different_allowed_object","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"public-b\",\"text\":\"allowed\"}]"},
    {"mixed_forbidden_and_allowed","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"public-b\",\"text\":\"allowed\"},{\"id\":\"private-a\",\"text\":\"protected-marker\"}]"},
    {"same_values_reordered_between_objects","[{\"id\":\"a\",\"text\":\"x\"},{\"id\":\"b\",\"text\":\"y\"}]","[{\"id\":\"a\",\"text\":\"y\"},{\"id\":\"b\",\"text\":\"x\"}]"}
  };
  for(String[] p:pairs) {
    Map<String,Object> r=row(p[0]);
    double pct=compareWithOriginalResponse(p[1],p[2],new HashMap<String,Boolean>());
    int len=p[2].trim().length()-2;
    r.put("original",p[1]);r.put("current",p[2]);r.put("percentage_match",pct);
    r.put("length_operand",len);
    r.put("validation_gate_if_selected",len>0&&pct>=90);
    r.put("scope","upstream comparator; reconstructed length/90-percent gate; assumes selection and 200; YAML engine not executed");
    rows.add(r);
  }
  for(String phone: new String[]{"+821012345678","010-1234-5678","01012345678","+82 10 1234 5678"}) {
    Map<String,Object> r=row("phone");r.put("input",phone);r.put("builtin_phone",isPhoneNumber(phone));rows.add(r);
  }
  RegexPredicate key=new RegexPredicate("^(?:주민등록번호|resident_registration_number|rrn)$");
  RegexPredicate value=new RegexPredicate("^[0-9]{6}-?[0-9]{7}$");
  String[][] pii={{"주민등록번호","000000-0000000"},{"rrn","0000000000000"},{"order_id","0000000000000"},{"주민등록번호","[REDACTED]"}};
  for(String[] p:pii){Map<String,Object> r=row("custom_korean_pattern");r.put("key",p[0]);r.put("value",p[1]);r.put("key_match",key.validate(p[0]));r.put("value_match",value.validate(p[1]));r.put("and_match",key.validate(p[0])&&value.validate(p[1]));r.put("notice","synthetic format only; validity and legal classification not established");rows.add(r);}
  RegexPredicate health=new RegexPredicate(".*진단.*");
  for(String text:new String[]{"우울증 진단을 받았습니다.","진단 서비스 운영시간 안내입니다."}){Map<String,Object> r=row("health_keyword");r.put("input",text);r.put("keyword_match",health.validate(text));rows.add(r);}
  SingleTypeInfo observed=new SingleTypeInfo();observed.uniqueCount=10;observed.publicCount=10;
  Map<String,Object> r=row("url_sti_overwrite");r.put("before_private",observed.getIsPrivate());
  observed=new SingleTypeInfo();
  r.put("after_private",observed.getIsPrivate());r.put("scope","original getIsPrivate method plus the same new-object assignment; DB/URL branch not executed");rows.add(r);
  System.out.println(mapper.writeValueAsString(rows));
}
}'''
    for marker, block in zip(("COMPARE", "EXTRACT_STRING", "EXTRACT_NODE", "PHONE", "PRIVATE", "REGEX"), blocks):
        source = source.replace(f"__{marker}__", block)
    java_file = args.work / "Audit.java"
    java_file.write_text(source, encoding="utf-8")
    classes = args.work / "classes"
    classes.mkdir(exist_ok=True)
    import os
    classpath = os.pathsep.join(str(jar_dir / item["name"]) for item in dependencies)
    subprocess.run(["javac", "-encoding", "UTF-8", "-cp", classpath, "-d", str(classes), str(java_file)], check=True)
    execution = subprocess.check_output(["java", "-Dfile.encoding=UTF-8", "-cp", str(classes) + os.pathsep + classpath, "Audit"], text=True, encoding="utf-8")
    rows = json.loads(execution)
    by_id = {r["id"]: r for r in rows}
    assert by_id["empty_array"]["validation_gate_if_selected"] is False
    assert by_id["empty_wrapped_array"]["validation_gate_if_selected"] is True
    assert by_id["identical_forbidden"]["validation_gate_if_selected"] is True
    assert by_id["foreign_private_to_empty"]["validation_gate_if_selected"] is False
    assert by_id["mixed_forbidden_and_allowed"]["validation_gate_if_selected"] is False
    assert by_id["url_sti_overwrite"]["before_private"] is False
    assert by_id["url_sti_overwrite"]["after_private"] is True
    filter_text = (args.source / "libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java").read_text(encoding="utf-8")
    assert "singleTypeInfo = new SingleTypeInfo();" in filter_text
    template = args.templates / "Broken-Object-Level-Authorization/BOLAByChangingAuthToken.yaml"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = {"date": "2026-10-04", "scope": "isolated upstream Java methods, not end-to-end Akto",
              "akto_commit": AKTO_COMMIT, "template_commit": TEMPLATE_COMMIT,
              "java_version": subprocess.run(["java", "-version"], text=True, capture_output=True).stderr.strip(),
              "template_sha256": hashlib.sha256(template.read_bytes()).hexdigest(),
              "method_provenance": provenance, "dependencies": dependencies,
              "cases": rows, "assertions_passed": 8}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cases": len(rows), "assertions_passed": 8, "results": rows}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
