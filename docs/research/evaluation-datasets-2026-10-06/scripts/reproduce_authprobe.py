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
          'oracle_revision': 'v2-exact-object-and-fixture-content',
          'independent_vulnerability_families': 1,
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
                fixture_name = f"synthetic-{identity['name']}-{i}"
                response = requests.post(base + '/applications', headers=identity['headers'],
                                         json={'name': fixture_name}, timeout=5)
                response.raise_for_status()
                created = response.json()
                fixture = {'id': created['id'], 'owner': identity['name'],
                           'name': fixture_name, 'note': None}
                assert created == fixture
                objects.append(fixture)
        for identity in config.identities:
            name = identity['name']
            for object_index, fixture in enumerate(objects, start=1):
                obj_id, owner = fixture['id'], fixture['owner']
                response = requests.get(f'{base}/applications/{obj_id}', headers=identity['headers'], timeout=5)
                own = name == owner
                expected_status = 200 if own or label == 'vulnerable' else 404
                assert response.status_code == expected_status
                body = response.json()
                returned_target_object = response.status_code == 200 and body.get('id') == obj_id
                fixture_content_matches = body == fixture
                if expected_status == 200:
                    assert returned_target_object and fixture_content_matches
                else:
                    assert body == {'detail': 'not found'}
                    assert not returned_target_object and not fixture_content_matches
                leaked = returned_target_object and fixture_content_matches
                cases.append({'requester': name, 'owner': owner, 'object_alias': f'object-{object_index}', 'operation': 'GET item',
                              'policy_allows': own, 'http_status': response.status_code,
                              'returned_target_object': returned_target_object,
                              'fixture_content_matches': fixture_content_matches,
                              'gold_bola': not own and leaked, 'case_kind': 'own' if own else 'cross'})
            response = requests.get(base + '/applications', headers=identity['headers'], timeout=5)
            assert response.status_code == 200
            expected_collection = {str(f['id']): f for f in objects if f['owner'] == name}
            returned_collection = response.json()
            assert len(returned_collection) == len(expected_collection) == 3
            assert {str(row['id']): row for row in returned_collection} == expected_collection
            cases.append({'requester': name, 'operation': 'GET collection', 'http_status': 200,
                          'exact_owned_fixture_set_matches': True,
                          'gold_bola': False, 'case_kind': 'scoped collection'})
        scanned = scan(config)
        aliases = {str(fixture['id']): f'object-{i}' for i, fixture in enumerate(objects, start=1)}
        findings = [{'probe': f.probe, 'severity': f.severity, 'title': f.title,
                     'requester': f.evidence.get('attacker'), 'owner': f.evidence.get('victim'),
                     'object_alias': aliases.get(str(f.evidence.get('object_id')))} for f in scanned.findings]
        finding_keys = [(f['requester'], f['owner'], f['object_alias']) for f in findings if f['probe'] == 'bola']
        gold_keys = {(c['requester'], c['owner'], c['object_alias']) for c in cases if c['gold_bola']}
        assert len(finding_keys) == len(set(finding_keys))
        assert set(finding_keys) == gold_keys
    result['targets'].append({'target': label, 'cases': cases,
                              'bola_finding_case_join_verified': True,
                              'findings_by_probe': dict(collections.Counter(f['probe'] for f in findings)),
                              'findings_by_severity': dict(collections.Counter(f['severity'] for f in findings)),
                              'findings': findings})
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps([{k:v for k,v in t.items() if k not in ('cases','findings')} |
                  {'case_count': len(t['cases']), 'gold_bola_count': sum(c['gold_bola'] for c in t['cases'])}
                 for t in result['targets']], indent=2))
