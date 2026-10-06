import json,pathlib,subprocess,urllib.request,hashlib
R=pathlib.Path(__file__).resolve().parents[1];A=R/'sources/akto';O=R/'evidence/probes';O.mkdir(exist_ok=True)
java=pathlib.Path(r'C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot\bin')
def method(src,needle):
 start=src.index(needle);br=src.index('{',start);end=br+1;n=1
 while n:n+=(src[end]=='{')-(src[end]=='}');end+=1
 return src[start:end]
s=(A/'libs/utils/src/main/java/com/akto/runtime/RuntimeUtil.java').read_text(encoding='utf-8')
t=(A/'libs/utils/src/main/java/com/akto/testing/Utils.java').read_text(encoding='utf-8')
methods=[method(s,'public static void extractAllValuesFromPayload(String'),method(s,'public static void extractAllValuesFromPayload(JsonNode'),method(t,'public static double compareWithOriginalResponse(')]
deps=[]
for artifact in ['jackson-core','jackson-databind','jackson-annotations']:
 jar=O/(artifact+'-2.16.1.jar');url=f'https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/{artifact}/2.16.1/{jar.name}'
 if not jar.exists():urllib.request.urlretrieve(url,jar)
 deps.append({'url':url,'path':str(jar),'sha256':hashlib.sha256(jar.read_bytes()).hexdigest()})
cases=[
 ('same_object',{'id':1,'label':'alpha'},{'id':1,'label':'alpha'},100),
 ('different_private_value',{'id':1,'label':'alpha'},{'id':2,'label':'alpha'},50),
 ('array_association_lost',[{'id':1,'label':'alpha'},{'id':2,'label':'beta'}],[{'id':1,'label':'beta'},{'id':2,'label':'alpha'}],100),
 ('extra_object_preserves_original_leak',[{'id':1,'label':'alpha'}],[{'id':1,'label':'alpha'},{'id':2,'label':'beta'}],0),
 ('number_vs_string',{'id':1},{'id':'1'},100),
 ('90pct_common_metadata',dict(id=1,**{f'm{i}':'shared' for i in range(9)}),dict(id=2,**{f'm{i}':'shared' for i in range(9)}),90),
]
lines=['import java.util.*;','import com.fasterxml.jackson.core.*;','import com.fasterxml.jackson.databind.*;','import com.fasterxml.jackson.databind.node.*;','public class BolaProbe {','static ObjectMapper mapper=new ObjectMapper(); static JsonFactory factory=mapper.getFactory();',*methods,'public static void main(String[] args) {']
for name,left,right,expected in cases:
 a=json.dumps(json.dumps(left,separators=(',',':')));b=json.dumps(json.dumps(right,separators=(',',':')))
 lines.append(f'System.out.println("{name}\\t"+compareWithOriginalResponse({a},{b},new HashMap<>()));')
lines+=['}}'];(O/'BolaProbe.java').write_text('\n'.join(lines),encoding='utf-8')
cp=';'.join([str(O)]+[d['path'] for d in deps])
subprocess.run([str(java/'javac.exe'),'-encoding','UTF-8','-cp',cp,str(O/'BolaProbe.java')],capture_output=True,check=True)
x=subprocess.run([str(java/'java.exe'),'-cp',cp,'BolaProbe'],capture_output=True,encoding='utf-8',check=True)
got={k:float(v) for k,v in (line.split('\t') for line in x.stdout.splitlines())}
results=[dict(case=n,original=l,current=r,expected_component_score=e,actual_score=got[n],pass_observed_semantics=got[n]==e) for n,l,r,e in cases]
assert all(x['pass_observed_semantics'] for x in results)
(O/'bola-results.json').write_text(json.dumps({'scope':'isolated exact comparator and extraction methods, NOT BOLA end-to-end','dependencies':deps,'results':results},indent=2),encoding='utf-8')
print(x.stdout);print('6 component assertions passed; no deployed BOLA verdict tested')
