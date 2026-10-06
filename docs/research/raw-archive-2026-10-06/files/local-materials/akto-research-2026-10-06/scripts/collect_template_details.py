import concurrent.futures,json,pathlib,re,subprocess
R=pathlib.Path(__file__).resolve().parents[1];D=R/'evidence/github/template-details';D.mkdir(exist_ok=True)
rows=json.loads((R/'evidence/github/templates_issues.json').read_text(encoding='utf-8'))
nums=[x['number'] for x in rows if 'pull_request' in x and re.search(r'bola|bfla|false.positive|sensitive|pii',x['title'],re.I)]
def run(n):
 for kind,suffix in [('pr',''),('files','/files?per_page=100')]:
  p=D/(f'{kind}-{n}.json')
  if p.exists():continue
  cmd=['gh','api',f'repos/akto-api-security/tests-library/pulls/{n}'+suffix]
  if kind=='files':cmd+=['--paginate','--slurp']
  r=subprocess.run(cmd,capture_output=True,encoding='utf-8',check=True);data=json.loads(r.stdout)
  if kind=='files':data=[f for page in data for f in page]
  p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 return n
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:print('Collected template PRs',list(pool.map(run,nums)))
