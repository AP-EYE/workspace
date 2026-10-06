# wger 실제 앱의 읽기 BOLA 취약·수정 버전 재현

실행일: 2026-10-06. [wger 공식 취약점 공지: 영양 단건 조회](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)와 [반복 설정 목록 조회](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm)는 모두 `<=2.4` 영향, `>=2.5` 수정을 표기한다. **공식 이미지 `wger/server:2.4`와 `:2.5`를 실제 실행**하여 합성 계정 두 개와 계정별 비공개 객체를 만든 뒤 원본 Django GET API 경로를 호출했다. [이미지 digest·소스 라벨·스크립트/결과 해시](evidence/manifest.json)

## 결과

| 검사한 원본 GET 경로 | 취약 `2.4` | 수정 `2.5` | 정답 근거 |
|---|---|---|---|
| `/api/v2/nutritionplan/{pk}/nutritional_values/`: 자기 계획 2요청 | 각 **200**, 자기 고유 영양값 111/222 | 각 **200**, 자기 고유 영양값 111/222 | 계획의 `user`와 반환 `energy` 표식 |
| 같은 경로: 타인 계획 2요청 | 각 **200**, 타인 고유값 222/111 노출 | 각 **404**, 고유 영양값 없음 | [공식 공지](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)·원본 raw ORM 조회와 수정 `self.get_object()` |
| `/api/v2/repetitions-config/`, `/api/v2/max-repetitions-config/`: 양쪽 계정, 총 4요청 | 모두 **200**, 각 목록에 자기와 타인 ID **2개** | 모두 **200**, 각 목록에 자기 ID **1개** | [공식 공지](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm)·원본 `.all()`과 사용자 필터 수정 |

16개 정책 관측 중 취약 2.4의 위반 요청은 **영양 교차조회 2 + 목록 혼합 4 = 6요청**이다. 이는 **2개 CVE family**이며 독립 취약점 6개라는 뜻이 아니다. 2.5에서는 교차 영양 조회가 차단되고 목록에서 타인 객체가 제거됐다. [2.4 영양 응답](evidence/wger-2.4-nutrition.json) · [2.5 영양 응답](evidence/wger-2.5-nutrition.json) · [2.4 목록](evidence/wger-2.4-list.json) · [2.5 목록](evidence/wger-2.5-list.json) · [해시/정답 자동 검증기](scripts/verify_wger_results.py)

## 실행 조건과 재현

- 공식 Docker Hub 이미지 digest는 2.4 `sha256:fd2302524d6fd7c2ddd647d1aa90d6848b98fe1e712906d49feab5ec88f3aaa9`, 2.5 `sha256:1cac2c62b8d85b54dab16291df802a1cdbf66828201b8df6104db0400320f0df`다. 이미지 OCI source revision은 각각 `9f76bde20c69b686242f81f49a958603c382cdc9`, `f270e5781e912de52cf008fdfa8be89b7de8149e`다. 이는 공지의 parent/fix commit과 **동일하다고 주장하지 않는다**.
- 각 이미지를 별도 `--network none` 컨테이너에 `--rm`으로 기동했다. 다른 실행 컨테이너/데이터에는 접근하지 않았다. `/tmp/`의 빈 SQLite DB에 원본 migration을 적용했다.
- [영양 fixture·GET 스크립트](scripts/wger_nutrition_probe.py)는 두 사용자/계획/식사/식사 항목에 합성 영양값 111·222를 만든다. [목록 fixture·GET 스크립트](scripts/wger_list_probe.py)는 사용자별 routine→day→slot→entry→config 관계와 서로 다른 ID를 만든다. 원본 application view·queryset·인가 코드는 바꾸지 않았다.
- 두 스크립트는 Django REST Framework의 `APIClient.force_authenticate(user=...)`로 요청자를 지정한다. **HTTP 라우터·원본 view·ORM·serializer는 실제 실행**하지만 로그인·토큰 발급/검증과 외부 네트워크 배포는 시험하지 않는다. 결과 JSON에는 자격정보나 실제 개인정보를 저장하지 않았다.

저장소 `team_hub`에서 재실행할 때 다음 순서로 각 image digest와 새 빈 SQLite 경로를 사용한다. 아래는 2.4 예시이며 2.5에는 image digest·컨테이너명·DB 파일 경로만 바꾼다.

```powershell
$img = 'wger/server@sha256:fd2302524d6fd7c2ddd647d1aa90d6848b98fe1e712906d49feab5ec88f3aaa9'
$name = 'ap-eye-wger-repro-24'
$folder = 'docs/research/evaluation-datasets-2026-10-06/appendices/authz/real-app'
docker run -d --rm --name $name --network none --entrypoint tail $img -f /dev/null
docker exec -e DJANGO_DB_DATABASE=/tmp/ap-eye-repro.sqlite3 $name python3 manage.py migrate --noinput --verbosity 0
Get-Content -Raw "$folder/scripts/wger_nutrition_probe.py" | docker exec -i -e DJANGO_DB_DATABASE=/tmp/ap-eye-repro.sqlite3 -e DJANGO_DEBUG=True $name python3 -
Get-Content -Raw "$folder/scripts/wger_list_probe.py" | docker exec -i -e DJANGO_DB_DATABASE=/tmp/ap-eye-repro.sqlite3 -e DJANGO_DEBUG=True $name python3 -
docker stop $name
```

고정 JSON은 실행 순서의 자동 증가 ID와 관계를 보존한다. 출력의 개인정보처럼 보일 수 있는 값은 모두 합성 fixture다. 이번 결과는 **wger 자체의 인가 동작을 확인한 외부 정답 재현**이며 Akto·RESTler·AP-EYE의 탐지 성능 실험이 아니다. 2.5 이미지의 수정은 영양·목록 이외의 전체 인가 안전성을 보증하지 않는다. [wger 원본 source·공지 diff 대조](../AUTHZ-REVIEW.ko.md#b-wger--실제-읽기와-정상-공유를-함께-갖춘-강한-추가-후보)
