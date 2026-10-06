import pathlib,json,urllib.request,urllib.parse,concurrent.futures,hashlib
E=pathlib.Path(__file__).resolve().parents[1]/'evidence'
def fetch(job):
 split,offset=job
 params=dict(dataset='ai4privacy/pii-masking-openpii-1.5m',config='default',split=split,offset=offset,length=100)
 url='https://datasets-server.huggingface.co/rows?'+urllib.parse.urlencode(params)
 name=f'openpii-{split}-rows-{offset}.json'
 try:
  with urllib.request.urlopen(url,timeout=60) as res:data=res.read();status=res.status
  (E/name).write_bytes(data)
  return dict(file=name,url=url,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as ex:return dict(file=name,url=url,error=str(ex))
jobs=[(s,o) for s in ['train','validation'] for o in range(0,500,100)]
out=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,jobs))
(E/'openpii-pages-manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
