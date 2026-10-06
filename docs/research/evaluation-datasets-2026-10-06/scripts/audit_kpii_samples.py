"""Audit already downloaded Dataset Viewer samples without running dataset code."""
import argparse
import hashlib
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--samples', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
results, templates = [], {}
for split in ['train', 'dev', 'test_track_a']:
    path = args.samples / f'k-pii-{split}-firstrows.json'
    raw = path.read_bytes()
    data = json.loads(raw)
    rows = [entry['row'] for entry in data['rows']]
    bad_spans, bad_lengths, entities = [], [], 0
    for row in rows:
        for entity in row['entities']:
            entities += 1
            start, end = entity['start'], entity['end']
            if not (0 <= start < end <= len(row['text']) and row['text'][start:end] == entity['surface']):
                bad_spans.append(row['doc_id'])
        if not len(row['tokens']) == len(row['bio_tags']) == len(row['token_offsets']):
            bad_lengths.append(row['doc_id'])
    templates[split] = {row['template_id'] for row in rows}
    results.append({'split': split, 'rows_checked': len(rows), 'entities_checked': entities,
                    'bad_span_documents': sorted(set(bad_spans)), 'bad_token_label_length_documents': bad_lengths,
                    'no_pii_documents_in_sample': sum(not row['entities'] for row in rows),
                    'truncated_rows': sum(bool(row.get('truncated_cells')) for row in data['rows']),
                    'raw_sha256': hashlib.sha256(raw).hexdigest()})
overlap = {}
for i, a in enumerate(templates):
    for b in list(templates)[i+1:]:
        overlap[f'{a} vs {b}'] = sorted(templates[a] & templates[b])
report = {'scope': 'convenience first-rows sample; NOT model evaluation, semantic label validation, or full split audit',
          'dataset': 'woohyun212/k-pii-bench', 'api_config': 'default', 'captured_date': '2026-10-06',
          'download_note': '/rows offset=0 length=100 returned HTTP 500; used /first-rows instead',
          'sample_count': sum(x['rows_checked'] for x in results),
          'entity_count': sum(x['entities_checked'] for x in results), 'results': results,
          'template_id_overlap_in_sample': overlap}
args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
