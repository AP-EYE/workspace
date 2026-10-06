# wger 공개 루틴 템플릿 정상 조회: 원본 테스트 실제 실행

실행일: 2026-10-06. 공식 [수정 커밋 `3515e61d8a246c7dccaf5453da3efd1d0d4937f9`](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9)은 `UserRoutineTemplateViewSet`과 `PublicRoutineTemplateViewSet`에 `RoutinePermission`을 추가하고, 조회 정상 사례 두 개를 추가했다. 그 커밋에서 추가된 **원본 maintainer 테스트를 포함한** `wger.manager.tests.test_templates` 8개를 공식 Docker 이미지 `wger/server:2.7`에서 실행하여 **8/8 통과**했다. [실행 로그](evidence/wger-2.7-template-tests.log) · [이미지·소스·로그 해시](evidence/manifest.json) · [재실행 스크립트](scripts/run_public_template_test.ps1)

| 정책 사례 | 원본 테스트의 정답과 관측 | 이 패키지에서 확인한 범위 |
|---|---|---|
| 비소유자의 공개 템플릿 | `GET /api/v2/public-templates/` 결과 첫 객체가 로그인 사용자 소유가 아님을 assert한 뒤, 동일 객체 `GET /api/v2/public-templates/{id}/`는 **200**이고 응답 ID가 목록 ID와 같음을 assert | `test_public_template_detail_api` 실행·통과 |
| 소유자의 자기 템플릿 | `GET /api/v2/templates/`에서 찾은 자기 객체에 `GET /api/v2/templates/{id}/`는 **200**·동일 ID | `test_private_template_detail_api` 실행·통과 |

경로는 이미지의 원본 `wger/urls.py`에서 `api/v2/` prefix와 `public-templates`·`templates` router 등록을 확인했다. 테스트 본문은 [이미지 revision의 원본 테스트](https://github.com/wger-project/wger/blob/83005f7d487c814833f3943784370bb0149fbaa8/wger/manager/tests/test_templates.py#L68-L90)와 [수정 커밋 diff](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9)를 함께 확인했다. 두 테스트는 로그인 사용자와 객체 소유권을 확인하고 실제 Django test client로 목록·detail 라우트를 실행한다. 이 사례를 BOLA 양성으로 잘못 알리면 정상 공개 접근에 대한 오탐이다.

## 버전과 방법의 경계

- 사용한 이미지의 고정 digest는 `sha256:1c5789b93bfe5eed0b7287255782d9177027b255de2b22b59f511a693a48db04`, OCI source revision은 `83005f7d487c814833f3943784370bb0149fbaa8`이다. [GitHub commit 비교](https://github.com/wger-project/wger/compare/3515e61d8a246c7dccaf5453da3efd1d0d4937f9...83005f7d487c814833f3943784370bb0149fbaa8)에서 이 revision은 수정 커밋보다 **36커밋 후속**이다. **`3515e61` 자체를 빌드해 실행한 것은 아니다.** 두 테스트 내용이 이미지에 들어 있음을 확인하고 해당 이미지의 원본 테스트를 실행했다.
- `docker run --rm --network none`로 독립 컨테이너를 만들었고, Django test runner의 **메모리 SQLite** DB가 종료 시 파기됐다. 나머지 Docker 컨테이너를 건드리지 않았다.
- test runner가 `axes.W001` 캐시 설정 경고를 냈다. 이 경고는 격리된 테스트 환경의 로그인 실패 추적 설정과 관련되며, 위 두 인가 요청의 `200` 및 동일 ID assert가 통과했다는 사실을 바꾸지 않는다. **실제 로그인·토큰 보안은 평가하지 않았다.**
- 이 결과는 `wger:2.7`의 정상 정책 근거이자 비소유자 허용 사례다. 취약 `wger:2.4`/수정 `:2.5`의 영양·반복 설정 CVE 재현과는 다른 snapshot이다. **Akto, RESTler, AP-EYE의 탐지 성능은 여기서 실행하지 않았다.**

재실행: 이 디렉터리에서 PowerShell로 `./scripts/run_public_template_test.ps1`을 실행한다. Docker가 필요하며 공식 이미지는 digest로 고정되어 있다.
