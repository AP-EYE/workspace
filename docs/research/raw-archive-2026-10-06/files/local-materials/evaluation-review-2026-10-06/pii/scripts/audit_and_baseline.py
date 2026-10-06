"""Read-only synthetic-data audit and offline Korean rule baseline.
Does not contact services or use models. Source data is never modified.
"""
import json,pathlib,sys,collections,re,hashlib,subprocess,difflib,time
ROOT=pathlib.Path(__file__).resolve().parents[1]; E=ROOT/'evidence'
PREV=ROOT.parents[1]/'evaluation-datasets-2026-10-06'/'evidence'
REPO=ROOT/'sources'/'ko-pii'
sys.path.insert(0,str(REPO/'src'))
from ko_pii.detect import detect_all
from ko_pii.eval.kdpii import KdpiiDocument,evaluate_kdpii,match_forms_overlap
def dump(name,obj):(E/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def prf(tp,fp,fn):
 p=tp/(tp+fp) if tp+fp else 0;r=tp/(tp+fn) if tp+fn else 0
 return dict(tp=tp,fp=fp,fn=fn,precision=p,recall=r,f1=2*p*r/(p+r) if p+r else 0)
def norm(s):return re.sub(r'\s+',' ',s).strip()

# Existing fixed convenience samples, not randomly sampled population estimates.
krows=[]
for split in ['train','dev','test_track_a']:
 f=PREV/f'k-pii-{split}-firstrows.json'
 for a in json.loads(f.read_text(encoding='utf-8'))['rows']:krows.append((split,a['row_idx'],a['row']))
kt=collections.Counter(); kd=collections.Counter(); errors=[]; contexts=[]; josa=[]
for split,idx,r in krows:
 kd[r['domain']]+=1; t=r['text']; es=r['entities']
 for e in es:
  kt[e['type']]+=1
  if not(0<=e['start']<e['end']<=len(t)) or t[e['start']:e['end']]!=e['surface']:errors.append([split,idx,e['type'],'offset'])
  contexts.append({'split':split,'row_idx':idx,'doc_id':r['doc_id'],'type':e['type'],'template':r['template_text'],'context':t[max(0,e['start']-20):min(len(t),e['end']+20)]})
 if len(r['tokens'])!=len(r['bio_tags']) or len(r['tokens'])!=len(r['token_offsets']):errors.append([split,idx,'token_lengths'])
 # Independent expected token BIO from character gold; catches scorer/adapter mismatch.
 expected=[]
 for a,b in r['token_offsets']:
  hits=[e for e in es if a<e['end'] and b>e['start']]
  expected.append(('B-' if a<=hits[0]['start'] else 'I-')+hits[0]['type'] if hits else 'O')
 if expected!=r['bio_tags']:errors.append([split,idx,'bio_vs_character_gold',sum(a!=b for a,b in zip(expected,r['bio_tags']))])
cleaned=[(sp,idx,r['doc_id'],norm(re.sub(r':\d+>>','>>',r['template_text']))) for sp,idx,r in krows]
exact_cross=[];near_cross=[]
for i,a in enumerate(cleaned):
 for b in cleaned[i+1:]:
  if a[0]==b[0]:continue
  if a[3]==b[3]:exact_cross.append({'a':a[:3],'b':b[:3],'template':a[3]})
  elif abs(len(a[3])-len(b[3]))<max(len(a[3]),len(b[3]))*.15:
   ratio=difflib.SequenceMatcher(None,a[3],b[3],autojunk=False).ratio()
   if ratio>=.9:near_cross.append({'a':a[:3],'b':b[:3],'ratio':ratio,'a_template':a[3],'b_template':b[3]})
dump('kpii-deep-sample-audit.json',{'scope':'126 existing first-rows convenience samples; not full dataset','rows':len(krows),'entities':sum(kt.values()),'labels':dict(kt),'domains':dict(kd),'negative_docs':sum(not r['entities'] for _,_,r in krows),'errors':errors,'cross_split_exact_normalized_templates':exact_cross,'cross_split_near_templates_ratio_ge_0_90':near_cross,'duplicate_texts':len(krows)-len({r['text'] for _,_,r in krows})})
dump('kpii-context-review-input.json',contexts)

# Full, openly released 540-document synthetic corpus, including negative docs.
f=REPO/'data'/'generated_eval.jsonl'; records=[json.loads(x) for x in f.read_text(encoding='utf-8').splitlines() if x.strip()]
labs=collections.Counter();bad=[];ambiguous=[];short=0;uniqueg=0;goldsets=[];docs=[];preds=[];st=time.perf_counter()
for i,r in enumerate(records):
 g=collections.defaultdict(set)
 for p in r['pii']:
  labs[p['type']]+=1;g[p['type']].add(p['text'])
  positions=[m.start() for m in re.finditer(re.escape(p['text']),r['text'])]
  if not positions:bad.append({'row_idx':i,'label':p['type'],'reason':'gold_surface_absent'})
  elif len(positions)>1:ambiguous.append({'row_idx':i,'label':p['type'],'occurrences':len(positions)})
  else:uniqueg+=1
  if p['type']=='PERSON' and len(p['text'])<3:short+=1
 docs.append(KdpiiDocument(query=r['text'],gold=dict(g))); goldsets.append(g);preds.append(detect_all(r['text']))
elapsed=time.perf_counter()-st
cache={r['text']:p for r,p in zip(records,preds)}
report=evaluate_kdpii(docs,detector=lambda s:cache[s],person_min_length=3)
strictforms=collections.defaultdict(lambda:[0,0,0]); negpred=[]
for i,(r,g,preds_i) in enumerate(zip(records,goldsets,preds)):
 pb=collections.defaultdict(set)
 for p in preds_i:
  if p.label=='PERSON' and len(p.text)<3:continue
  pb[p.label].add(p.text)
 if not r['pii'] and preds_i:negpred.append({'row_idx':i,'predicted_labels':dict(collections.Counter(p.label for p in preds_i))})
 for lab in set(g)|set(pb):
  gs={s for s in g.get(lab,[]) if lab!='PERSON' or len(s)>=3};ps=pb.get(lab,set())
  counts=[len(gs&ps),len(ps-gs),len(gs-ps)]
  strictforms[lab]=[a+b for a,b in zip(strictforms[lab],counts)]
tot=[sum(x[i] for x in strictforms.values()) for i in range(3)]
counter=[]
for case,p,g in [('partial_name',{'홍길'},{'홍길동'}),('one_prediction_covers_two_gold',{'김민지와 김민수'},{'김민지','김민수'}),('repeated_text_is_deduplicated',{'홍길동'},{'홍길동'})]:
 mp,mg=match_forms_overlap(p,g);counter.append({'case':case,'matched_pred_count':len(mp),'matched_gold_count':len(mg),'scorer_counts':prf(len(mp),len(p-mp),len(g-mg))})
sha=subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip()
core_labels={'PERSON','PHONE','EMAIL','ADDRESS','RRN','ACCOUNT'}
core_neg_docs=sum(bool(set(x['predicted_labels'])&core_labels) for x in negpred)
dump('ko-pii-full-audit-and-baseline.json',{'source_commit':sha,'dataset_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'docs':len(records),'gold_entries':sum(labs.values()),'labels':dict(labs),'label_count':len(labs),'negative_docs':sum(not r['pii'] for r in records),'duplicate_exact_texts':len(records)-len({r['text'] for r in records}),'gold_surface_absent':bad,'gold_with_multiple_text_occurrences':len(ambiguous),'affected_docs_multiple_occurrences':len({x['row_idx'] for x in ambiguous}),'unique_occurrence_gold_entries':uniqueg,'person_gold_shorter_than_3':short,'canonical_scorer_person_min_length_3':{'all':prf(report.micro_tp,report.micro_fp,report.micro_fn),'per_label':{k:prf(v.tp,v.fp,v.fn) for k,v in report.per_label.items()}},'exact_surface_set_scorer_person_min_length_3_NOT_character_span_metric':{'all':prf(*tot),'per_label':{k:prf(*v) for k,v in strictforms.items()}},'negative_docs_with_any_prediction':len(negpred),'negative_prediction_details':negpred,'elapsed_all_documents_seconds_includes_python_loop':elapsed,'synthetic_scorer_counterexamples':counter,'interpretation':'Offline rule detection only. Dataset gold is author LLM-validated, not independently human verified; repeated forms lack occurrence offsets. Exact-surface-set is not strict character-span F1. These are development audit results, not a locked holdout or global accuracy.'})
details=json.loads((E/'ko-pii-full-audit-and-baseline.json').read_text(encoding='utf-8'))
details['python_version']=sys.version
details['core_labels']=sorted(core_labels)
details['negative_docs_with_core_label_prediction']=core_neg_docs
dump('ko-pii-full-audit-and-baseline.json',details)
print(json.dumps({'kpii_docs':len(krows),'kpii_entities':sum(kt.values()),'kpii_errors':errors,'kpii_negatives':sum(not r['entities'] for _,_,r in krows),'ko_docs':len(records),'ko_gold':sum(labs.values()),'ko_canonical':prf(report.micro_tp,report.micro_fp,report.micro_fn),'ko_exact_surface':prf(*tot),'ko_negative_docs_flagged':len(negpred),'ko_negative_docs_flagged_core_labels':core_neg_docs},ensure_ascii=False,indent=2))
