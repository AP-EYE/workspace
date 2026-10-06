"""Execute the original wger 2.4 nutrition GET route using Django's API client.

Run in a disposable official wger/server:2.4 container with a fresh SQLite DB.
Authentication is supplied by APIClient.force_authenticate; view/ORM policy is
unmodified. Fixtures are synthetic and contain no external credentials.
"""

import json
import os
import secrets

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.main")

import django

django.setup()

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from wger.core.models import Language, License
from wger.nutrition.models import Ingredient, Meal, MealItem, NutritionPlan


def ingredient(language, name, energy):
    return Ingredient.objects.create(
        language=language,
        name=name,
        energy=energy,
        protein=energy / 10,
        carbohydrates=energy / 10,
        fat=energy / 10,
        license_title="synthetic evaluation fixture",
        license_object_url="",
        license_author_url="",
        license_derivative_source_url="",
    )


lang, _ = Language.objects.get_or_create(
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
run_token = secrets.token_hex(4)
users = {
    "alice": User.objects.create(username=f"apeye_alice_{run_token}"),
    "bob": User.objects.create(username=f"apeye_bob_{run_token}"),
}
plans = {}
for i, (name, user) in enumerate(users.items()):
    plan = NutritionPlan.objects.create(user=user, description=f"{name} private plan")
    meal = Meal.objects.create(plan=plan, order=1, name=f"{name} private meal")
    item = ingredient(lang, f"{name} synthetic food", 111 + i * 111)
    MealItem.objects.create(meal=meal, ingredient=item, order=1, amount=100)
    plans[name] = plan

rows = []
for requester, user in users.items():
    client = APIClient()
    client.force_authenticate(user=user)
    for owner, plan in plans.items():
        response = client.get(f"/api/v2/nutritionplan/{plan.pk}/nutritional_values/")
        try:
            data = response.json()
        except Exception:
            data = None
        rows.append(
            {
                "requester": requester,
                "owner": owner,
                "target_id": plan.pk,
                "status": response.status_code,
                "response": data,
            }
        )

assert len(rows) == 4
for row in rows:
    assert row["status"] in (200, 404)
    if row["requester"] == row["owner"]:
        assert row["status"] == 200
    if row["status"] == 200:
        expected_energy = 111.0 if row["owner"] == "alice" else 222.0
        assert row["response"]["energy"] == expected_energy
    else:
        assert row["response"] is None or "energy" not in row["response"]
print(json.dumps({"test_type": "official_image_django_api_client", "rows": rows}, ensure_ascii=False, indent=2, default=str))
