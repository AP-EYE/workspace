import pathlib,json,collections
E=pathlib.Path(__file__).resolve().parents[1]/'evidence'
by_split={};ko=[];errors=[];labels=collections.Counter();all_lang=collections.Counter()
for split in ['train','validation']:
 rows=json.loads((E/f'openpii-{split}-firstrows.json').read_text(encoding='utf-8'))['rows']
 by_split[split]={'all_rows':len(rows),'korean_rows':sum(r['row']['language']=='ko' for r in rows)}
 for wrapper in rows:
  r=wrapper['row'];all_lang[r['language']]+=1
  if r['language']!='ko':continue
  spans=r['privacy_mask'];t=r['source_text'];entry={'split':split,'row_idx':wrapper['row_idx'],'uid':r['uid'],'text':t,'annotations':[]}
  for a in spans:
   labels[a['label']]+=1
   if t[a['start']:a['end']]!=a['value']:errors.append({'split':split,'row_idx':wrapper['row_idx'],'type':a['label']})
   entry['annotations'].append({'label':a['label'],'value':a['value'],'context':t[max(0,a['start']-15):min(len(t),a['end']+15)]})
  ko.append(entry)
out={'source_revision':json.loads((E/'openpii-meta.json').read_text(encoding='utf-8'))['sha'],'sampling':'first-rows cached API convenience samples; rows/filter API returned HTTP 500; no population inference','by_split':by_split,'all_sample_language_counts':dict(all_lang),'korean_docs':len(ko),'korean_entities':sum(labels.values()),'korean_label_counts':dict(labels),'offset_errors':errors,'negative_korean_docs':sum(not r['annotations'] for r in ko),'total_korean_population_NOT_VERIFIED':True}
(E/'openpii-korean-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(E/'openpii-korean-review-input.json').write_text(json.dumps(ko,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
