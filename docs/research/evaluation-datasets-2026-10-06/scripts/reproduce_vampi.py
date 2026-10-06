"""Verify upstream read BOLA and legitimate public list, in a temporary app copy."""
import argparse
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import sys
import tempfile

p = argparse.ArgumentParser()
p.add_argument('--source', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
source, output = args.source.resolve(), args.output.resolve()
commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
old_cwd = Path.cwd()
cases = []
with tempfile.TemporaryDirectory(prefix='apeye-vampi-') as temp:
    appdir = Path(temp) / 'app'
    shutil.copytree(source, appdir, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    sys.path.insert(0, str(appdir))
    os.chdir(appdir)
    try:
        import config
        from models.user_model import User
        from models.books_model import Book
        from api_views import books
        client = config.vuln_app.app.test_client()
        with config.vuln_app.app.app_context():
            assert Path(config.db.engine.url.database).resolve().is_relative_to(appdir)
            config.db.create_all()
            headers = {}
            for name in ['alice', 'bob']:
                user = User(name, secrets.token_urlsafe(20), f'{name}@example.invalid')
                user.books = [Book(book_title=f'{name}-book', secret_content=f'synthetic-private-{name}')]
                config.db.session.add(user)
                headers[name] = {'Authorization': 'Bearer ' + user.encode_auth_token(name)}
            config.db.session.commit()
        # Only the upstream book handler's existing mode flag is toggled. Its
        # implementation, auth check, response projection, and query are unchanged.
        for mode in [1, 0]:
            books.vuln = mode
            for requester in ['alice', 'bob']:
                for owner in ['alice', 'bob']:
                    response = client.get(f'/books/v1/{owner}-book', headers=headers[requester])
                    expected = 200 if mode or requester == owner else 404
                    assert response.status_code == expected
                    body = response.get_json()
                    exposes_secret = body.get('secret') == f'synthetic-private-{owner}'
                    assert exposes_secret == (expected == 200)
                    cases.append({'mode': mode, 'requester': requester, 'owner': owner,
                                  'operation': 'GET /books/v1/{book}', 'http_status': response.status_code,
                                  'gold_bola': requester != owner and exposes_secret,
                                  'exposes_private_field': exposes_secret})
            response = client.get('/books/v1')
            body = response.get_json()
            assert response.status_code == 200 and len(body['Books']) == 2
            assert all('secret' not in book for book in body['Books'])
            cases.append({'mode': mode, 'requester': 'anonymous', 'operation': 'GET /books/v1',
                          'http_status': 200, 'gold_bola': False, 'case_kind': 'public projection'})
    finally:
        if 'config' in sys.modules:
            with config.vuln_app.app.app_context():
                config.db.session.remove()
                config.db.engine.dispose()
        os.chdir(old_cwd)
result = {'scope': 'Flask/Connexion in-process test client; no listening service or scanner',
          'source_commit': commit, 'mode_switch': 'api_views.books.vuln: upstream existing flag',
          'cases': cases, 'case_count': len(cases), 'gold_bola_count': sum(c['gold_bola'] for c in cases)}
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'cases'}, indent=2))
