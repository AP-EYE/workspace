import concurrent.futures,hashlib,json,pathlib,urllib.request,datetime
R=pathlib.Path(__file__).resolve().parents[1];D=R/'sources/references';D.mkdir(exist_ok=True)
urls={
 'SPY_2025.naacl-srw.23.pdf':'https://aclanthology.org/2025.naacl-srw.23.pdf',
 'GLiNER2_PII_2605.09973.pdf':'https://arxiv.org/pdf/2605.09973',
 'CrossLingual_2608.02616.pdf':'https://arxiv.org/pdf/2608.02616',
 'k_pii_bench_README.md':'https://huggingface.co/datasets/woohyun212/k-pii-bench/raw/main/README.md',
 'akto_redact.md':'https://docs.akto.io/api-inventory/how-to/redact-sensitive-data',
 'akto_custom_type.md':'https://docs.akto.io/api-inventory/how-to/create-a-custom-data-type',
 'akto_datatypes.md':'https://docs.akto.io/api-inventory/concepts/data-types',
 'google_infotypes.html':'https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference',
 'azure_languages.html':'https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/language-support',
 'aws_pii.html':'https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html',
}
def dl(it):
 name,url=it;p=D/name
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'AP-EYE research source archive'})
   with urllib.request.urlopen(req,timeout=40) as r:p.write_bytes(r.read())
  return {'name':name,'url':url,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(dl,urls.items()))
(D/'manifest.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':results},indent=2),encoding='utf-8')
for r in results:print(r['name'],r.get('bytes',r.get('error')))
