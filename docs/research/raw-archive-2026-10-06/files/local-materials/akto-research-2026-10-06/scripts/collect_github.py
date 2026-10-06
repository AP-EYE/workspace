import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'evidence' / 'github'
OUT.mkdir(parents=True, exist_ok=True)

def fetch(name, endpoint, paginate=True):
    path = OUT / (name + '.json')
    if path.exists():
        data = json.loads(path.read_text(encoding='utf-8'))
        return {'name':name, 'cached':True, 'items':len(data), 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    cmd=['gh','api',endpoint]
    if paginate: cmd += ['--paginate','--slurp']
    r=subprocess.run(cmd,capture_output=True,encoding='utf-8')
    if r.returncode:
        return {'name':name,'error':r.stderr[:700]}
    data=json.loads(r.stdout)
    if paginate: data=[x for page in data for x in page]
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    return {'name':name,'items':len(data),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

jobs=[('repo','repos/akto-api-security/akto',False),
      ('all_issues_and_prs','repos/akto-api-security/akto/issues?state=all&per_page=100',True),
      ('closed_pulls','repos/akto-api-security/akto/pulls?state=closed&per_page=100',True),
      ('releases','repos/akto-api-security/akto/releases?per_page=100',True),
      ('advisories','repos/akto-api-security/akto/security-advisories?per_page=100',True),
      ('contributors','repos/akto-api-security/akto/contributors?per_page=100',True),
      ('templates_repo','repos/akto-api-security/tests-library',False),
      ('templates_issues','repos/akto-api-security/tests-library/issues?state=all&per_page=100',True)]
if __name__ == '__main__':
    manifest={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requests':[]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures=[pool.submit(fetch,*j) for j in jobs]
        for f in concurrent.futures.as_completed(futures):
            result=f.result(); manifest['requests'].append(result); print(json.dumps(result,ensure_ascii=False),flush=True)
    manifest['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT/'collection_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
