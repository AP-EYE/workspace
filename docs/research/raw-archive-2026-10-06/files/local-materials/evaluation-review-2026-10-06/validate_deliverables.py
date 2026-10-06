import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

repo = Path(__file__).resolve().parents[2] / "team_hub"
docs = repo / "docs"
bundle = docs / "research/evaluation-datasets-2026-10-06"
paths = [docs / "dataset/README.md", docs / "akto/README.md"]
paths += sorted(bundle.rglob("*.md"))
paths += sorted((docs / "akto/research-2026-10-06").rglob("*.md"))
errors = []
for path in paths:
    assert path.is_file(), path
    body = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", body):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local = path.parent / unquote(target.split("#", 1)[0])
        if not local.exists():
            errors.append((str(path.relative_to(repo)), target))

manifest = json.loads((bundle / "evidence/manifest.json").read_text(encoding="utf-8"))
for item in manifest["evidence_files"]:
    path = bundle / "evidence" / item["file"]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != item["sha256"]:
        errors.append(("manifest", str(path.relative_to(repo))))
for path in (bundle / "appendices/pii/evidence").glob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))
for path in (bundle / "appendices/authz/evidence").glob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))
normal = bundle / "appendices/authz/real-app/public-normal"
normal_manifest = json.loads((normal / "evidence/manifest.json").read_text(encoding="utf-8"))
for key, rel in {
    "evidence_wger_2_7_template_tests_log": "evidence/wger-2.7-template-tests.log",
    "scripts_run_public_template_test_ps1": "scripts/run_public_template_test.ps1",
}.items():
    actual = hashlib.sha256((normal / rel).read_bytes()).hexdigest()
    if actual != normal_manifest["sha256"][key]:
        errors.append(("wger-public-normal-manifest", rel))
akto = docs / "akto/research-2026-10-06"
akto_manifest = json.loads((akto / "SHARED-COPY-MANIFEST.json").read_text(encoding="utf-8"))
for item in akto_manifest["files"]:
    path = akto / item["path"]
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
        errors.append(("akto-shared-manifest", item["path"]))
result = {"checked_markdown": len(paths), "broken_local_links_or_hashes": errors}
print(json.dumps(result, ensure_ascii=False, indent=2))
if errors:
    raise SystemExit(1)
