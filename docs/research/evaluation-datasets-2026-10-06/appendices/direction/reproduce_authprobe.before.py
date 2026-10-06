"""Reproduce the published m=3 localhost targets; save no auth headers/bodies."""
import argparse
import collections
import json
import subprocess
import sys
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--source', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
sys.path.insert(0, str(args.source.resolve()))
import requests
from authprobe._serve import serve
from authprobe.demo import _config
from authprobe.scanner import scan
from targets import vulnerable_ats, secure_ats

result = {'scope': 'localhost HTTP, author targets, two identities, three objects each',
          'source_commit': subprocess.check_output(['git', '-C', str(args.source), 'rev-parse', 'HEAD'], text=True).strip(),
          'targets': []}
for label, module in [('vulnerable', vulnerable_ats), ('secure', secure_ats)]:
    module._APPS.clear()
    if hasattr(module, '_COUNTER'):
        module._COUNTER['n'] = 0
    cases = []
    with serve(module.app) as base:
        assert base.startswith('http://127.0.0.1:')
        config = _config(base)
        objects = []
        for identity in config.identities:
            for i in range(3):
                response = requests.post(base + '/applications', headers=identity['headers'],
                                         json={'name': f"synthetic-{identity['name']}-{i}"}, timeout=5)
                response.raise_for_status()
                objects.append((response.json()['id'], identity['name']))
        for identity in config.identities:
            name = identity['name']
            for object_index, (obj_id, owner) in enumerate(objects, start=1):
                response = requests.get(f'{base}/applications/{obj_id}', headers=identity['headers'], timeout=5)
                own = name == owner
                leaked = response.status_code == 200 and response.json().get('owner') == owner
                expected_status = 200 if own or label == 'vulnerable' else 404
                assert response.status_code == expected_status
                cases.append({'requester': name, 'owner': owner, 'object_alias': f'object-{object_index}', 'operation': 'GET item',
                              'policy_allows': own, 'http_status': response.status_code,
                              'gold_bola': not own and leaked, 'case_kind': 'own' if own else 'cross'})
            response = requests.get(base + '/applications', headers=identity['headers'], timeout=5)
            assert response.status_code == 200
            assert len(response.json()) == 3
            assert all(row['owner'] == name for row in response.json())
            cases.append({'requester': name, 'operation': 'GET collection', 'http_status': 200,
                          'gold_bola': False, 'case_kind': 'scoped collection'})
        scanned = scan(config)
        aliases = {str(oid): f'object-{i}' for i, (oid, _) in enumerate(objects, start=1)}
        findings = [{'probe': f.probe, 'severity': f.severity, 'title': f.title,
                     'requester': f.evidence.get('attacker'), 'owner': f.evidence.get('victim'),
                     'object_alias': aliases.get(str(f.evidence.get('object_id')))} for f in scanned.findings]
    result['targets'].append({'target': label, 'cases': cases,
                              'findings_by_probe': dict(collections.Counter(f['probe'] for f in findings)),
                              'findings_by_severity': dict(collections.Counter(f['severity'] for f in findings)),
                              'findings': findings})
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps([{k:v for k,v in t.items() if k not in ('cases','findings')} |
                  {'case_count': len(t['cases']), 'gold_bola_count': sum(c['gold_bola'] for c in t['cases'])}
                 for t in result['targets']], indent=2))
