"""Verify report references/counts and hash frozen evidence. No network calls."""
import collections, csv, datetime, hashlib, json, pathlib, re, subprocess
R=pathlib.Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
allitems=read(R/'evidence/github/all_issues_and_prs.json')
assert len(allitems)==6581
assert sum('pull_request' in x for x in allitems)==6402
assert len(read(R/'evidence/github/templates_issues.json'))==347
assert len(list((R/'evidence/github/details').glob('pr-*.json')))==164
assert len(list((R/'evidence/github/template-details').glob('pr-*.json')))==24
public=read(R/'evidence/github/public_index.json');assert len(public)==6928
with (R/'ISSUE-PR-INDEX.csv').open(encoding='utf-8-sig',newline='') as f:
    csvrows=list(csv.DictReader(f));assert len(csvrows)==6928
    assert all('body' not in x for x in csvrows)
    assert all(not str(v).startswith(('=','+','-','@','\t','\r')) for x in csvrows for v in x.values())
md=(R/'AKTO-DEEP-RESEARCH.ko.md').read_text(encoding='utf-8')
defs=dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)',md,re.M))
used=re.findall(r'\[[^\]\n]+\]\[([^\]]+)\]',md)
assert all(x in defs for x in used)
repos=[]
for n in ['akto','pii-types','tests-library','Documentation','presidio','ko-pii']:
    def git(*args):return subprocess.check_output(['git','-C',str(R/'sources'/n),*args],text=True,encoding='utf-8').strip()
    repos.append({'directory':'sources/'+n,'commit':git('rev-parse','HEAD'),'origin':git('remote','get-url','origin'),'commit_date':git('show','-s','--format=%cI','HEAD'),'tracked_changes':git('status','--porcelain','--untracked-files=no')})
    assert not repos[-1]['tracked_changes'], n+' snapshot changed'
for repo,commit,p in re.findall(r'https://github.com/(?:akto-api-security|data-privacy-stack|Marker-Inc-Korea)/([^/]+)/blob/([0-9a-f]+)/([^\s#]+)',md):
    subprocess.run(['git','-C',str(R/'sources'/repo),'cat-file','-e',commit+':'+p],capture_output=True,check=True)
probe=read(R/'evidence/probes/results.json')
phone=probe['phone_results'];regex=probe['regex_results']
assert len(phone)==36 and len(regex)==27
bola=read(R/'evidence/probes/bola-results.json')['results']
assert len(bola)==6 and all(x['pass_observed_semantics'] for x in bola)
for name in ['AKTO-DEEP-RESEARCH.html','HISTORY-REVIEW.html','PAPER-NOTES.html','ISSUE-EXPLORER.html','HISTORY-REVIEW.ko.md','PAPER-NOTES.ko.md']:
    assert (R/name).is_file()
validation={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_reference_links':len(used),'all_used_reference_definitions_exist':True,'pinned_github_blob_paths_exist':True,'index_rows':len(public),'core_PR_details':164,'template_PR_details':24,'PII_component_inputs':63,'BOLA_component_inputs':6,'all_snapshot_tracked_files_clean':True,'scope':'Artifact consistency; not deployed Akto, not PII population benchmark'}
(R/'evidence/consistency-validation.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
paths=[]
for d in ['scripts','evidence','sources/references']:
    paths.extend(p for p in (R/d).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
paths.extend(p for p in R.iterdir() if p.is_file() and p.name!='EVIDENCE-MANIFEST.json')
entries=[]
for p in sorted(set(paths)):
    entries.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'as_of':'2026-10-06 Asia/Seoul','collection_notes':['GitHub calls were paginated and non-atomic; counts use all_issues_and_prs.json.','Collection scripts reuse cached JSON. A collection-run timestamp is not a claim that every cached response was refreshed at that time.','Raw public GitHub bodies are untrusted evidence; displayed index omits bodies and long numeric title strings.','Repository snapshots are identified by commit; their complete Git object stores are not duplicated in this per-file hash list.'],'source_repositories':repos,'scope':validation,'files':entries}
(R/'EVIDENCE-MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'validation':validation,'hashed_files':len(entries),'bytes_hashed':sum(x['bytes'] for x in entries)},ensure_ascii=False))
