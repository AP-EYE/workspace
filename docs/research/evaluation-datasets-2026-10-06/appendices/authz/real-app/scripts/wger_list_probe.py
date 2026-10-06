"""Original wger 2.4/2.5 GET list routes for repetition configs.

Uses synthetic records and Django APIClient.force_authenticate in a disposable,
network-isolated official image. No application source or permission logic patch.
"""

import datetime
import json
import os
import secrets

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.main")

import django

django.setup()

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from wger.core.models import Language, License
from wger.exercises.models import Exercise, ExerciseCategory
from wger.manager.models import (
    Day,
    MaxRepetitionsConfig,
    RepetitionsConfig,
    Routine,
    Slot,
    SlotEntry,
)


Language.objects.get_or_create(
    id=1,
    defaults={"short_name": "en", "full_name": "English", "full_name_en": "English"},
)
Language.objects.get_or_create(
    id=2,
    defaults={"short_name": "de", "full_name": "Deutsch", "full_name_en": "German"},
)
License.objects.get_or_create(
    id=2,
    defaults={"full_name": "Synthetic fixture license", "short_name": "synthetic"},
)
category, _ = ExerciseCategory.objects.get_or_create(name="Synthetic evaluation category")
exercise = Exercise.objects.create(
    category=category,
    license_title="synthetic evaluation fixture",
    license_object_url="",
    license_author_url="",
    license_derivative_source_url="",
)

run_token = secrets.token_hex(4)
users = {}
gold = {}
for i, name in enumerate(("alice", "bob")):
    user = User.objects.create(username=f"apeye_list_{name}_{run_token}")
    users[name] = user
    routine = Routine.objects.create(
        user=user,
        name=f"{name} private routine",
        start=datetime.date(2026, 1, 1),
        end=datetime.date(2026, 1, 8),
    )
    day = Day.objects.create(routine=routine, order=1, name="day")
    slot = Slot.objects.create(day=day, order=1)
    entry = SlotEntry.objects.create(
        slot=slot, exercise=exercise, order=1, repetition_unit=None, weight_unit=None
    )
    repetitions = RepetitionsConfig.objects.create(slot_entry=entry, iteration=1, value=10 + i)
    maximum = MaxRepetitionsConfig.objects.create(slot_entry=entry, iteration=1, value=20 + i)
    gold[name] = {"repetitions-config": repetitions.pk, "max-repetitions-config": maximum.pk}

rows = []
for requester, user in users.items():
    client = APIClient()
    client.force_authenticate(user=user)
    for endpoint in ("repetitions-config", "max-repetitions-config"):
        response = client.get(f"/api/v2/{endpoint}/")
        data = response.json()
        items = data["results"] if isinstance(data, dict) and "results" in data else data
        ids = [item["id"] for item in items]
        rows.append(
            {
                "requester": requester,
                "endpoint": endpoint,
                "status": response.status_code,
                "expected_own_id": gold[requester][endpoint],
                "other_user_id": gold["bob" if requester == "alice" else "alice"][endpoint],
                "returned_ids": ids,
            }
        )

assert len(rows) == 4
for row in rows:
    assert row["status"] == 200
    assert row["expected_own_id"] in row["returned_ids"]
print(json.dumps({"test_type": "official_image_django_api_client", "rows": rows}, ensure_ascii=False, indent=2))
