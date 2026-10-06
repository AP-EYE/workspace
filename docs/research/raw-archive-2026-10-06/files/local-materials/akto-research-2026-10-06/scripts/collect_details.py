import concurrent.futures,json,pathlib,re,subprocess,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence/github/details';OUT.mkdir(exist_ok=True)
rows=json.loads((ROOT/'evidence/github/indexed_items.json').read_text(encoding='utf-8'))
rx=r'\bpii\b|sensitive data|data.?type|redact|masking|phone.number|credit.card|fintech|regex|\bbola\b|\bbfla\b|private.resource|response.compar|auth.token|auth.header|false.positive|false.negative|cve|xss|role.escalation|cross.account|patch.*vulnerab'
numbers={x['number'] for x in rows if x['kind']=='PR' and re.search(rx,x['title'],re.I)}
numbers.update([527,883,1359,1363,1619,1965,2674,5915,6569])
jobs=[]
for n in sorted(numbers):
 jobs.extend([(f'pr-{n}',f'repos/akto-api-security/akto/pulls/{n}',False),(f'files-{n}',f'repos/akto-api-security/akto/pulls/{n}/files?per_page=100',True)])
for x in rows:
 if x['kind']=='ISSUE' and x['comments']>0 and (x['tags'] or x['number'] in [4235,5512]):
  jobs.append((f'comments-{x["number"]}',f'repos/akto-api-security/akto/issues/{x["number"]}/comments?per_page=100',True))
def run(j):
 name,endpoint,paged=j; p=OUT/(name+'.json')
 if p.exists():return {'name':name,'cached':True}
 cmd=['gh','api',endpoint]+(['--paginate','--slurp'] if paged else [])
 r=subprocess.run(cmd,capture_output=True,encoding='utf-8')
 if r.returncode:return {'name':name,'error':r.stderr[:300]}
 data=json.loads(r.stdout)
 if paged:data=[i for page in data for i in page]
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 return {'name':name,'items':len(data)}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for i,result in enumerate(pool.map(run,jobs)):
  results.append(result)
  if 'error' in result or i%50==0:print(i,len(jobs),result,flush=True)
manifest={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selected_prs':sorted(numbers),'jobs':results}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('Done',len(numbers),'PRs;',len(jobs),'requests;',sum('error' in r for r in results),'errors',flush=True)
