import collections,csv,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
G=ROOT/'evidence/github'
allitems=json.loads((G/'all_issues_and_prs.json').read_text(encoding='utf-8'))
pulls={p['number']:p for p in json.loads((G/'closed_pulls.json').read_text(encoding='utf-8'))}
patterns={
 'pii':r'\bpii\b|sensitive data|data.?type|redact|masking|phone.number|credit.card|social.security|fintech|regex|personal.*information',
 'bola':r'\bbola\b|\bbfla\b|\bidor\b|private.resource|response.compar|auth.token|auth.header|false.positive|false.negative',
 'platform_security':r'\bcve[- ]|\bxss\b|\bssrf\b|\bcsrf\b|injection|vulnerabilit|auth.*bypass|cross.account|cross.tenant|permission|access.control|path.travers|security.fix|security.patch|secret.leak',
 'bug':r'\bbug\b|\bfix(?:ed|es)?\b|incorrect|exception|crash|wrong|failure',
 'ai':r'\bllm\b|\bai\b|akto.?gpt|\bner\b|model.accuracy',
}
rows=[]
for x in allitems:
 p=pulls.get(x['number'],{})
 body=x.get('body') or ''
 tags=[k for k,v in patterns.items() if re.search(v,x['title']+' '+body,re.I)]
 rows.append({'number':x['number'],'kind':'PR' if 'pull_request' in x else 'ISSUE','title':x['title'],'state':x['state'],'merged':bool(p.get('merged_at')),'created':x['created_at'],'closed':x['closed_at'],'tags':','.join(tags),'url':x['html_url'],'body':body,'comments':x['comments']})
(G/'indexed_items.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (ROOT/'ISSUE-PR-INDEX.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'total':len(rows),'kinds':dict(collections.Counter(x['kind'] for x in rows)),'states':dict(collections.Counter(x['kind']+':'+x['state'] for x in rows)),'merged_prs':sum(x['merged'] for x in rows),'keyword_tags':dict(collections.Counter(t for x in rows for t in x['tags'].split(',') if t))}
(G/'index_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
for cat in ['ISSUES','PII/BOLA TITLE','SECURITY FIX TITLE']:
 print('\n'+cat)
 for x in sorted(rows,key=lambda x:x['number']):
  if cat=='ISSUES': yes=x['kind']=='ISSUE'
  elif cat=='PII/BOLA TITLE': yes=bool(re.search(patterns['pii']+'|'+patterns['bola'],x['title'],re.I))
  else: yes=bool(re.search(patterns['platform_security'],x['title'],re.I)) and bool(re.search(patterns['bug'],x['title'],re.I))
  if yes: print(x['number'],x['kind'],x['state'],'MERGED' if x['merged'] else '',x['title'])
