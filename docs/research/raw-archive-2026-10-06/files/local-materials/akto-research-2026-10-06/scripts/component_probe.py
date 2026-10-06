"""Runs exact Akto phone method and original Java regexes on synthetic diagnostics.
This is NOT an Akto deployment test or a population accuracy benchmark.
"""
import base64,hashlib,json,pathlib,subprocess,urllib.request
R=pathlib.Path(__file__).resolve().parents[1]; A=R/'sources/akto'; O=R/'evidence/probes';O.mkdir(exist_ok=True)
java=pathlib.Path(r'C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot\bin')
jar=O/'libphonenumber-8.12.41.jar'
url='https://repo.maven.apache.org/maven2/com/googlecode/libphonenumber/libphonenumber/8.12.41/libphonenumber-8.12.41.jar'
if not jar.exists():urllib.request.urlretrieve(url,jar)
src=(A/'libs/dao/src/main/java/com/akto/dto/type/KeyTypes.java').read_text(encoding='utf-8')
start=src.index('public static boolean isPhoneNumber('); br=src.index('{',start); level=1;end=br+1
while level:
 level+=(src[end]=='{')-(src[end]=='}');end+=1
method=src[start:end]
types=json.loads((A/'pii-types/fintech.json').read_text(encoding='utf-8'))['types'];rx={x['name']:x['regexPattern'] for x in types}
cases=[]
def add(name,value,note):cases.append({'detector':name,'value':value,'note':note,'regex':rx[name]})
add('PAN CARD','ABCDE1234F','shape example; issuance not asserted')
add('PAN CARD','PAN: ABCDE1234F','same shape inside sentence')
add('US Medicare Health Insurance Claim Number','123456789A','legacy HICN shape')
add('US Medicare Health Insurance Claim Number','1EG4TE5MK73','CMS example of newer MBI; different identifier')
add('Indian Unique Health Identification','00000000000000','all-zero number; no validity evidence')
add('United Kingdom National Insurance Number','QQ123456C','forbidden Q prefix')
add('United Kingdom National Insurance Number','AB123456C','shape example')
add('United Kingdom National Insurance Number','AB 12 34 56 C','formatted variant')
add('Finnish Personal Identity Number','310299-123A','impossible February day; shape only')
add('Finnish Personal Identity Number','010101B123A','new century separator B; checksum not asserted')
add('Canadian Social Insurance Number','000000000','invalid reserved all-zero shape')
add('Canadian Social Insurance Number','123456789','Luhn-invalid synthetic shape')
add('Canadian Social Insurance Number','123 456 789','spaced variant')
add('German Insurance Identity Number','12310299A123','impossible February day; shape only')
add('Japanese Social Insurance Number','000000000000','all-zero shape; not proof of assigned number')
add('Japanese Social Insurance Number','1234-5678-9012','hyphenated variant')
add('IBAN EUROPE','GB82WEST12345698765432','public IBAN example with alpha bank code')
add('IBAN EUROPE','DE89370400440532013000','public IBAN example')
add('IBAN EUROPE','DE00370400440532013000','same example with invalid check digits')
add('US ADDRESS','123 Example St, CA 90210','synthetic shape')
add('US ADDRESS','서울특별시 종로구 예시로 123','Korean synthetic address')
rx['EMAIL']=r'^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,7})+$'
# Extract the original literal and let Java compile it verbatim; avoid escape translation drift.
email_line=next(x.strip() for x in src.splitlines() if 'patternToSubType.put' in x and 'EMAIL' in x)
ssn_line=next(x.strip() for x in src.splitlines() if 'patternToSubType.put' in x and 'SSN' in x)
for value,note in [('alice@example.com','reserved-domain example'),('alice@example.technology','long ASCII TLD'),('문의: alice@example.com','embedded email'),('이름@example.com','Korean local part; EAI policy needed')]:
 cases.append({'detector':'EMAIL','value':value,'note':note,'regex':'EXTRACTED_JAVA_LITERAL'})
for value,note in [('000-00-0000','invalid SSN all zero'),('123456789','no-hyphen variant')]:cases.append({'detector':'SSN','value':value,'note':note,'regex':'EXTRACTED_JAVA_LITERAL'})
def j(s):return json.dumps(s,ensure_ascii=False)
lines=['import com.google.i18n.phonenumbers.*;','import java.util.regex.*;','public class Probe {',method,'public static void main(String[] args) {','PhoneNumberUtil u=PhoneNumberUtil.getInstance();']
lines+=['for(String region:new String[]{"US","GB","FR","DE","FI","IN","JP","CA","KR"}) {','var p=u.getExampleNumberForType(region,PhoneNumberUtil.PhoneNumberType.MOBILE);','for(var f: new PhoneNumberUtil.PhoneNumberFormat[]{PhoneNumberUtil.PhoneNumberFormat.E164,PhoneNumberUtil.PhoneNumberFormat.NATIONAL,PhoneNumberUtil.PhoneNumberFormat.INTERNATIONAL}) {','String s=u.format(p,f); System.out.println("PHONE\\t"+region+"\\t"+f+"\\t"+isPhoneNumber(s)+"\\t"+s);','}','String s=u.format(p,PhoneNumberUtil.PhoneNumberFormat.NATIONAL).replaceAll("[^0-9]","");','System.out.println("PHONE\\t"+region+"\\tDIGITS\\t"+isPhoneNumber(s)+"\\t"+s);','}']
for i,c in enumerate(cases):
 if c['detector'] in ['EMAIL','SSN']:
  literal=(email_line if c['detector']=='EMAIL' else ssn_line).split('Pattern.compile(',1)[1].rsplit(')',2)[0]
  # Original source statement: put(subtype, Pattern.compile(literal));
  expr='Pattern.compile('+literal+')'
 else:expr='Pattern.compile('+j(c['regex'])+')'
 lines.append('System.out.println("REGEX\\t'+str(i)+'\\t"+'+expr+'.matcher('+j(c['value'])+').matches());')
lines+=['}}']; code='\n'.join(lines);(O/'Probe.java').write_text(code,encoding='utf-8')
subprocess.run([str(java/'javac.exe'),'-encoding','UTF-8','-cp',str(jar),str(O/'Probe.java')],check=True,capture_output=True)
r=subprocess.run([str(java/'java.exe'),'-Dfile.encoding=UTF-8','-cp',str(O)+';'+str(jar),'Probe'],check=True,capture_output=True,encoding='utf-8')
(O/'stdout.tsv').write_text(r.stdout,encoding='utf-8')
phones=[]
for line in r.stdout.splitlines():
 x=line.split('\t')
 if x[0]=='PHONE':phones.append(dict(region=x[1],format=x[2],matched=x[3]=='true',synthetic_example=x[4]))
 else:cases[int(x[1])]['matched']=x[2]=='true'
result={'scope':'isolated original phone method and original Java regexes; not runtime or accuracy benchmark','akto_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=A,text=True).strip(),'java_version':subprocess.run([str(java/'java.exe'),'-version'],capture_output=True,text=True).stderr.strip(),'dependency':{'url':url,'sha256':hashlib.sha256(jar.read_bytes()).hexdigest()},'phone_results':phones,'regex_results':cases,'source_sha256':hashlib.sha256((O/'Probe.java').read_bytes()).hexdigest()}
(O/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('Phone',len(phones),'regex',len(cases),'total',len(phones)+len(cases))
for c in cases:print(c['detector'],c['note'],c['matched'])
for f in ['E164','NATIONAL','INTERNATIONAL','DIGITS']:print(f,sum(x['matched'] for x in phones if x['format']==f),'/9')
