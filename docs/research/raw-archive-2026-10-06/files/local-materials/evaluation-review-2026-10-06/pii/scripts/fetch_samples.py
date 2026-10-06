import pathlib,json,urllib.request,urllib.parse,concurrent.futures,hashlib
R=pathlib.Path(__file__).resolve().parents[1]; E=R/'evidence'
base='https://datasets-server.huggingface.co/'
jobs=[]
for split in ('train','validation'):
 q={'dataset':'ai4privacy/pii-masking-openpii-1.5m','config':'default','split':split}
 jobs.append((f'openpii-{split}-firstrows.json',base+'first-rows?'+urllib.parse.urlencode(q)))
 jobs.append((f'openpii-{split}-ko100.json',base+'filter?'+urllib.parse.urlencode(dict(q,where='"language"=\'ko\'',offset=0,length=100))))
jobs.append(('gretel-train-firstrows.json',base+'first-rows?'+urllib.parse.urlencode({'dataset':'gretelai/synthetic_pii_finance_multilingual','config':'default','split':'train'})))
def fetch(job):
 name,url=job
 try:
  with urllib.request.urlopen(url,timeout=60) as res: data=res.read();status=res.status
  (E/name).write_bytes(data)
  return {'file':name,'url':url,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 except Exception as exc:return {'file':name,'url':url,'error':str(exc)}
out=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,jobs))
(E/'sample-fetch-manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
