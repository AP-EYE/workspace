"""Verify the saved paired wger GET responses and evidence file hashes."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
evidence = root / "evidence"
manifest = json.loads((evidence / "manifest.json").read_text(encoding="utf-8"))

for item in manifest["files"]:
    path = root / item["file"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], path

for version in ("2.4", "2.5"):
    nutrition = json.loads((evidence / f"wger-{version}-nutrition.json").read_text(encoding="utf-8"))
    assert nutrition["test_type"] == "official_image_django_api_client"
    assert len(nutrition["rows"]) == 4
    for row in nutrition["rows"]:
        same_owner = row["requester"] == row["owner"]
        assert row["status"] == (200 if same_owner or version == "2.4" else 404)
        if row["status"] == 200:
            assert row["response"]["energy"] == (111 if row["owner"] == "alice" else 222)
        else:
            assert not row["response"] or "energy" not in row["response"]

    listing = json.loads((evidence / f"wger-{version}-list.json").read_text(encoding="utf-8"))
    assert listing["test_type"] == "official_image_django_api_client"
    assert len(listing["rows"]) == 4
    for row in listing["rows"]:
        assert row["status"] == 200
        expected = {row["expected_own_id"]}
        if version == "2.4":
            expected.add(row["other_user_id"])
        assert set(row["returned_ids"]) == expected

print("wger paired evidence verified: 2 images, 8 nutrition GETs, 8 list GETs, all hashes match")
