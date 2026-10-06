# Akto 수정 이력 검토표

기준: 2026-10-06 KST. 공개 GitHub API 수집본을 사용한다. 이 문서는 보안 감사의 완료 증명서가 아니다.

## 읽는 방법

- **핵심 patch 검토**: 본문·관련 변경 부분을 읽고 의미를 요약한 항목이다. 모든 호출 경로를 동적으로 검증한 것은 아니다.
- **상세 확보**: 본문·파일 목록·GitHub가 제공한 patch를 확보했으나 개별 수정 의미를 충분히 검증하지 않은 항목이다.
- **목록 분류**: 제목·본문 키워드에 따른 자동 분류다. 보안 취약점 판정이 아니다.
- merged는 특정 base branch에 병합됐다는 의미다. master·상용 배포·실제 사용 이미지 적용과 구별한다.
- 원시 이슈에는 외부 사용자의 주장·스팸이 섞인다. 사실의 근거는 코드·재현·관리자 설명과 함께 판단한다.

본체 목록은 이슈 179 + PR 6,402 = 6,581건이다. 본체 PR 상세 164건, tests-library 관련 PR 상세 24건을 확보했다. 번호는 저장소마다 독립적이다. 공개 advisory API 0건은 취약점 부재를 의미하지 않는다.

## 1. 본체 핵심 변경

| PR·종류 | 상태·병합일(UTC)·대상 | 실제 변경과 남는 한계 |
|---|---|---|
| [#527](https://github.com/akto-api-security/akto/pull/527) · 분류 | 병합 2023-09-04 · `develop` | key 조건에 value 규칙을 잘못 넣던 매핑 수정. key/value 의미를 구분해야 한다. |
| [#883](https://github.com/akto-api-security/akto/pull/883) · 검사 오탐 | 병합 2024-02-17 · `develop` | cookie MaxAge 대소문자·날짜 처리, URL 정규식 escaping·wordlist 처리 등의 patch. 모든 BOLA 오탐이 해결됐다는 뜻은 아니다. |
| [#1121](https://github.com/akto-api-security/akto/pull/1121) · 분류 | 병합 2024-05-18 · `master` | AWS secret custom type을 비활성화하고 일반 타입으로 재분류하는 처리. 변경 이유나 전후 정확도는 이 patch만으로 확정하지 않는다. |
| [#1231](https://github.com/akto-api-security/akto/pull/1231) · 마스킹 | 병합 2024-07-05 · `develop` | cookie와 GraphQL의 redaction 처리 확대. 적용되는 입력 경로·설정 조건은 별도 확인해야 한다. |
| [#1248](https://github.com/akto-api-security/akto/pull/1248) · 마스킹 | 병합 2024-07-05 · `develop` | mini-runtime query parameter redaction 보완. redactAll 조건이 있으므로 무조건 적용으로 해석하지 않는다. |
| [#1249](https://github.com/akto-api-security/akto/pull/1249) · 마스킹 | 병합 2024-07-05 · `develop` | api-runtime query parameter redaction 보완. mini-runtime의 동명 변경과 대상 모듈을 구분한다. |
| [#1359](https://github.com/akto-api-security/akto/pull/1359) · BOLA | 병합 2024-08-15 · `master` | 인증 헤더 변경 경로에서 upsert를 사용하도록 수정. 없는 헤더의 추가도 다룬다. |
| [#1363](https://github.com/akto-api-security/akto/pull/1363) · BOLA | 병합 2024-08-17 · `master` | private_variable_context의 설명 작성용 StringBuilder 초기화로 null 오류 방지. 의미 판정의 정확도 개선과는 구별한다. |
| [#1491](https://github.com/akto-api-security/akto/pull/1491) · 마스킹 | 병합 2024-09-14 · `feature/mini-runtime-release` | 민감 key 샘플의 redaction 및 타입 mapper의 redacted 설정 전달 보완. mini-runtime-release 대상. |
| [#1492](https://github.com/akto-api-security/akto/pull/1492) · 마스킹 | 병합 2024-09-14 · `feature/cyborg-release` | cyborg 타입 mapper에 redacted 상태 반영. master 병합으로 표기하지 않는다. |
| [#1619](https://github.com/akto-api-security/akto/pull/1619) · 의존성 | 병합 2024-10-15 · `feature_data_ingestion_service` | Struts 및 Spring 관련 의존성 버전 변경. CVE 영향은 사용 경로·배포 버전을 따로 분석해야 한다. |
| [#1965](https://github.com/akto-api-security/akto/pull/1965) · 의존성 | 병합 2025-01-11 · `feature/mini-runtime-release` | 오래된 Jetty·SnakeYAML 직접 의존성 제거. shaded/transitive dependency까지 모두 제거됐다는 증거는 아니다. |
| [#2418](https://github.com/akto-api-security/akto/pull/2418) · 정규식 | 병합 2025-04-24 · `master` | test-editor helper의 전체 일치 matches를 부분 일치 find로 변경. 현재 PII RegexPredicate의 matches와 다른 코드다. |
| [#2674](https://github.com/akto-api-security/akto/pull/2674) · 플랫폼 보안 제보 | open·미병합 · `master` | 로그인 JSP에 사용자 이름을 JavaScript 문자열로 직접 삽입하는 XSS 제보의 수정안. open·미병합이며 현재 코드 형태와 일치. 전체 입력/실행 경로 재현은 NOT_RUN. |
| [#2908](https://github.com/akto-api-security/akto/pull/2908) · 마스킹 예외 | 병합 2025-08-01 · `master` | BURP 수집 소스를 global redaction 처리에서 제외하는 변경. 예외의 존재와 실제 계정별 redaction 결과를 구분한다. |
| [#3055](https://github.com/akto-api-security/akto/pull/3055) · 마스킹 예외 | 병합 2025-08-28 · `master` | global redaction을 MIRRORING 소스에 적용하는 조건 변경. 제품의 모든 입력 경로가 같은 정책을 쓰지 않는다. |
| [#3497](https://github.com/akto-api-security/akto/pull/3497) · 마스킹 | 병합 2025-11-07 · `master` | sample data redaction 및 기존 데이터/타입 갱신 경로의 보완. 과거 저장된 모든 원문이 제거됐다는 운영 검증은 하지 않았다. |
| [#5498](https://github.com/akto-api-security/akto/pull/5498) · 검사 근거 | 병합 2026-06-24 · `master` | 검출 근거가 원문에 있는지 검증하고 호출자 credential을 누출 근거에서 제외하며 결정적 검출 결과와 LLM 결과를 결합. 문자열 존재가 권한 위반 증거를 대신하지는 않는다. |
| [#5519](https://github.com/akto-api-security/akto/pull/5519) · 마스킹 UI | 병합 2026-06-24 · `master` | cookie/샘플 표시에서 마스킹 placeholder 처리를 개선. UI가 가려졌다는 사실만으로 DB 원문 제거를 주장할 수 없다. |
| [#5682](https://github.com/akto-api-security/akto/pull/5682) · 성능 제안 | open·미병합 · `master` | Hyperscan을 다루는 미병합 제안. 현재 기본 Akto의 엔진이나 속도로 소개하지 않는다. 제목·구성 수준 확인. |
| [#5863](https://github.com/akto-api-security/akto/pull/5863) · 문장 PII | 병합 2026-07-22 · `master` | 기본 Presidio 결과에서 DATE_TIME·NRP·LOCATION 제외. entities를 지정한 경우와 다르며 오탐 감소와 탐지 범위 감소가 함께 있다. |
| [#5881](https://github.com/akto-api-security/akto/pull/5881) · 인증정보 취급 | 병합 2026-07-23 · `master` | session identifier 후보에서 Authorization header를 제거. 실제 외부 유출 사건을 입증한 자료는 아니다. |
| [#5902](https://github.com/akto-api-security/akto/pull/5902) · 문장 PII | 병합 2026-07-27 · `master` | anonymizer score threshold 0.4와 목록 marker·이메일 등의 회귀 테스트 추가. threshold는 정확도 백분율이 아니다. 테스트 코드는 확인했으나 서비스 테스트 실행은 NOT_RUN. |
| [#5915](https://github.com/akto-api-security/akto/pull/5915) · 의존성 | 병합 2026-07-28 · `master` | Go 의존성 버전 보완. 프로젝트 전체 CVE 제거 또는 악용 가능성의 확정을 뜻하지 않는다. |
| [#6112](https://github.com/akto-api-security/akto/pull/6112) · OSS 사용성 제보 | open·미병합 · `master` | local_deploy의 plan gate 때문에 Access Restricted가 나타나는 문제를 다루는 미병합 수정안. 현재 UI 분기 확인, 실제 Docker 배포 NOT_RUN. |
| [#6121](https://github.com/akto-api-security/akto/pull/6121) · LLM 마스킹 | 병합 2026-08-19 · `master` | redaction 설정 UI·DTO·Go 모듈 연결 추가. 내부 모델의 한국어 성능은 이 변경으로 확인할 수 없다. |
| [#6150](https://github.com/akto-api-security/akto/pull/6150) · 외부 검사 모듈 | 병합 2026-08-19 · `master` | PII block 우선순위라는 제목이나 본체의 핵심 patch는 모듈 버전 변경. 실제 내부 알고리즘의 수정 내용을 확보한 것으로 간주하지 않는다. |
| [#6240](https://github.com/akto-api-security/akto/pull/6240) · 외부 검사 모듈 | 병합 2026-08-27 · `master` | 이메일 PII 탐지 수정이라는 제목이나 본체에서 확인되는 것은 주로 모듈 버전 변경. 전후 precision/recall 수치는 없다. |
| [#6278](https://github.com/akto-api-security/akto/pull/6278) · 분류 확장 | 병합 2026-09-01 · `feature/cyborg-release` | cyborg의 외부 datatype corrector 관련 HTTP·후보·캐시 등의 확장. 조사한 master에 동일 구현이 있다는 주장은 하지 않는다. |
| [#6279](https://github.com/akto-api-security/akto/pull/6279) · 분류 확장 | 병합 2026-09-01 · `feature/mini-runtime-release` | mini-runtime-release의 외부 datatype corrector 연계. branch-specific 구현이며 배포 이미지 채택 여부는 별도 확인. |
| [#6309](https://github.com/akto-api-security/akto/pull/6309) · 플랫폼 접근통제 | 병합 2026-09-10 · `master` | RBAC 요금제 검사 전에 product-level NO_ACCESS를 처리하도록 이동. 기존 early return이 접근 제한을 건너뛸 수 있다는 문제. master 현재 순서도 확인. |
| [#6402](https://github.com/akto-api-security/akto/pull/6402) · 데이터 최소화 | 병합 2026-09-15 · `master` | 사용자명 lookup map을 브라우저 payload로 보내던 구조를 서버 조회로 이동. 모든 PII 전송·저장 경로 제거를 의미하지 않는다. |
| [#6487](https://github.com/akto-api-security/akto/pull/6487) · LLM 출력 | 병합 2026-09-22 · `master` | 탐지 이유에 PII/비밀값을 다시 인용하지 않도록 prompt 보완. 별도의 출력 검증 없이 완전한 누출 방지를 증명할 수 없다. |
| [#6513](https://github.com/akto-api-security/akto/pull/6513) · LLM 출력 | 병합 2026-09-24 · `feat/async-reason` | 추가 설명 경로도 값 대신 종류·개수로 설명하도록 보완. feat/async-reason 병합이며 관련 문구는 조사한 master에서도 확인. |
| [#6569](https://github.com/akto-api-security/akto/pull/6569) · 플랫폼 보안 제보 | open·미병합 · `master` | 역할 변경·비밀번호 초기화 대상의 account 범위와 호출자 권한 확인을 보완하는 미병합 수정안. 다른 interceptor를 포함한 실제 공격 가능성은 NOT_RUN. |

## 2. 이슈의 해결 상태를 보수적으로 읽기

| 이슈 | 확인한 근거 | 조사 결론 |
|---|---|---|
| [#2673](https://github.com/akto-api-security/akto/issues/2673) | 사용자 이름의 로그인 JSP 삽입 및 #2674 수정안 | 소스와 일치하는 open 제보. 실제 공격 재현은 미실행 |
| [#5512](https://github.com/akto-api-security/akto/issues/5512) / [#4235](https://github.com/akto-api-security/akto/issues/4235) | OSS 로컬 설치의 접근 제한 관련 글 | 로컬 사용 가능 범위를 직접 검증해야 함. 댓글의 우회를 공식 정책으로 간주하지 않음 |
| [#6043](https://github.com/akto-api-security/akto/issues/6043) | shaded dependency와 SBOM 사각지대 제보 | 패키지 탐지와 악용 가능성을 구분. 제보도 exploitability는 조사하지 않았다고 명시 |
| [#5473](https://github.com/akto-api-security/akto/issues/5473) | Mongo 버전/driver 호환성 관련 closed 글 | 현재 Compose는 7.0.4. 과거 제보의 환경과 현재 코드를 섞지 않음 |
| [#5480](https://github.com/akto-api-security/akto/issues/5480) | OpenAPI 3.1에서 endpoint 0건이라는 제보와 해결 댓글 | closed·해결 주장 존재. 원인 patch 연결과 여러 3.1 schema에 대한 검증은 미확인 |

## 3. 검사 템플릿 저장소의 변경

| tests-library PR | 상태·병합일(UTC)·대상 | 검토 결과 |
|---|---|---|
| [#80](https://github.com/akto-api-security/tests-library/pull/80) | closed·미병합 · `master` | 응답 일치 threshold를 90에서 80으로 낮추는 수정안. closed지만 merged_at이 없으므로 적용됐다고 기록하지 않는다. |
| [#81](https://github.com/akto-api-security/tests-library/pull/81) | 병합 2024-05-09 · `master` | 28개 BOLA 템플릿에 오류 문구 제외를 추가. HTTP 200 업무 오류의 오탐을 줄이려는 변경이며 영어 문자열 목록에 의존한다. |
| [#85](https://github.com/akto-api-security/tests-library/pull/85) | 병합 2024-05-10 · `master` | 잠긴/차단된 계정과 반복 실패 문구, 비어 있지 않은 응답 조건을 보완. 여전히 언어·문구 변형과 정상 본문의 단어 충돌 평가가 필요하다. |
| [#86](https://github.com/akto-api-security/tests-library/pull/86) | 병합 2024-05-10 · `master` | BOLAJSONBodyParamArray의 length 아래 gt: 0 누락으로 생긴 parsing 문제 보완. 탐지 의미보다 템플릿 유효성 문제다. |
| [#167](https://github.com/akto-api-security/tests-library/pull/167) | 병합 2024-12-02 · `master` | 12개 BOLA 파일에 HTML tag 제외를 추가. 로그인/오류 HTML 응답의 오탐을 줄이는 휴리스틱; HTML 응답 전체의 의미 판정은 아니다. |
| [#208](https://github.com/akto-api-security/tests-library/pull/208) | 병합 2025-07-27 · `master` | 응답 정규식으로 카드·SSN·인도 번호 후보를 찾는 PIIDataLeak threat 템플릿 추가. 권한/소유권을 직접 판단하는 규칙은 아니다. |
| [#214](https://github.com/akto-api-security/tests-library/pull/214) | 병합 2025-07-30 · `master` | 앞서 추가한 PIIDataLeak.yml 삭제. 이유는 빈 본문에서 확인되지 않으므로 오탐 때문에 삭제됐다고 단정하지 않는다. |
| [#216](https://github.com/akto-api-security/tests-library/pull/216) | 병합 2025-08-04 · `master` | 제목은 PII threat 제거지만 실제 diff는 SecurityMisconfig의 host 조건 제거와 stack trace regex 조정. #214의 삭제와 구별한다. |
| [#227](https://github.com/akto-api-security/tests-library/pull/227) | closed·미병합 · `master` | closed·미병합. API가 887개 파일 변경을 반환한 큰 제안이며 제목만으로 범위를 알 수 없다. 파일 목록·상태만 확인, 전체 patch 감사는 하지 않았다. |
| [#228](https://github.com/akto-api-security/tests-library/pull/228) | 병합 2025-09-12 · `pro` | pro 브랜치에 병합. 28개 BOLA 템플릿의 duration FAST→SLOW 메타데이터 변경. 탐지 정확도 향상 PR로 소개하면 부정확하다. |
| [#297](https://github.com/akto-api-security/tests-library/pull/297) | open·미병합 · `master` | agentic BOLA 테스트 추가안, open·미병합. 367개 파일 변경의 목록/대표 patch만 확인. 현재 기본 템플릿으로 평가하지 않는다. |

검사 템플릿에 달린 CVE는 보통 검사 대상 취약점의 참고 자료다. 그 번호를 Akto 자체의 CVE 목록으로 옮기면 안 된다. 일부 템플릿은 INTRUSIVE로 표시돼 있으므로 실습 서버와 명시적인 검사 범위가 필요하다.

## 4. 이번에 확인한 원인 패턴

1. 데이터 취급의 누락: body뿐 아니라 query, cookie, GraphQL, 로그·설명문·export까지 관리해야 한다.
2. 분류의 단순화: key와 value, 전체 일치와 부분 일치, locale, checksum, 관측 부족을 별개로 다뤄야 한다.
3. 휴리스틱의 한계: 같은 2xx 응답·유사한 payload·영어 오류 제외는 객체 소유권의 정답이 아니다.
4. 제품 접근통제: 결제/라이선스 분기와 보안 권한 분기를 섞으면 의도한 제한을 건너뛸 수 있다.
5. 의존성 가시성: 직접 의존성만 갱신해서 shaded·transitive dependency까지 모두 해결했다고 할 수 없다.
6. 운영과 소스의 차이: feature/release branch의 fix, master, Docker image, 외부 검사 모듈은 서로 다른 증거다.

AP-EYE 회귀 사례로는 여러 수집 소스의 PII 잔존 여부, 한국어 200 오류, 다른 소유자의 배열 객체, 인증 헤더의 유무, NO_ACCESS와 요금제 조합을 우선한다. 이 목록은 구현·배포 성공을 주장하는 것이 아니라 조사에서 도출한 시험 제안이다.

## 5. 확보한 본체 PR 상세 전체 목록

아래 표는 상세 확보 범위를 공개하기 위한 것이다. 164건 전체를 완전한 보안 감사로 표시하지 않는다. GitHub patch 필드가 없거나 잘릴 수 있고 PR 본문의 전후 성능 주장도 독립 재현하지 않았다.

| PR | 제목 | 상태 / base | 검토 수준 |
|---|---|---|---|
| [#42](https://github.com/akto-api-security/akto/pull/42) | Add prompt for user to go to user config, when auth token is not set | merged / `develop` | 상세 확보 |
| [#61](https://github.com/akto-api-security/akto/pull/61) | replace auth token in cookie | merged / `develop` | 상세 확보 |
| [#180](https://github.com/akto-api-security/akto/pull/180) | add fintech types source | merged / `develop` | 상세 확보 |
| [#225](https://github.com/akto-api-security/akto/pull/225) | Add sensitive data types US addresses #97 | merged / `master` | 상세 확보 |
| [#238](https://github.com/akto-api-security/akto/pull/238) | Added Regex for Insurance | merged / `master` | 상세 확보 |
| [#251](https://github.com/akto-api-security/akto/pull/251) | Update fintech.json | closed / unmerged / `master` | 상세 확보 |
| [#252](https://github.com/akto-api-security/akto/pull/252) | Update TestFintechTypes.java | closed / unmerged / `master` | 상세 확보 |
| [#254](https://github.com/akto-api-security/akto/pull/254) | Added sensitive data types - Europe specific | merged / `master` | 상세 확보 |
| [#275](https://github.com/akto-api-security/akto/pull/275) | BFLA Matrix | closed / unmerged / `develop` | 상세 확보 |
| [#278](https://github.com/akto-api-security/akto/pull/278) | BFLA matrix | closed / unmerged / `develop` | 상세 확보 |
| [#350](https://github.com/akto-api-security/akto/pull/350) | dry run to invalidate sensitive data | merged / `develop` | 상세 확보 |
| [#352](https://github.com/akto-api-security/akto/pull/352) | Hotfix/match sensitive data | merged / `master` | 상세 확보 |
| [#353](https://github.com/akto-api-security/akto/pull/353) | added 4 new xss tests | merged / `develop` | 상세 확보 |
| [#382](https://github.com/akto-api-security/akto/pull/382) | added whitelist to pii cleaner | merged / `develop` | 상세 확보 |
| [#384](https://github.com/akto-api-security/akto/pull/384) | remove custom auth in replace auth header test and remove all custom auth instead of removing only one | merged / `develop` | 상세 확보 |
| [#441](https://github.com/akto-api-security/akto/pull/441) | Polaris/data types | merged / `polaris_develop` | 상세 확보 |
| [#502](https://github.com/akto-api-security/akto/pull/502) | Sensitive Data fixes done | merged / `polaris_develop` | 상세 확보 |
| [#526](https://github.com/akto-api-security/akto/pull/526) | fix key condition in custom data types | closed / unmerged / `feature/auth0_integration` | 상세 확보 |
| [#527](https://github.com/akto-api-security/akto/pull/527) | fix key condition in custom data types | merged / `develop` | 핵심 patch 검토 |
| [#529](https://github.com/akto-api-security/akto/pull/529) | fix redundant data type updates | merged / `develop` | 상세 확보 |
| [#546](https://github.com/akto-api-security/akto/pull/546) | fix(fintech.json): trailing comma | merged / `master` | 상세 확보 |
| [#593](https://github.com/akto-api-security/akto/pull/593) | reset sensitive data | merged / `develop` | 상세 확보 |
| [#681](https://github.com/akto-api-security/akto/pull/681) | Feature/tag CVE | merged / `develop` | 상세 확보 |
| [#682](https://github.com/akto-api-security/akto/pull/682) | Add sensitive data Cookie types | merged / `hacktoberfest` | 상세 확보 |
| [#683](https://github.com/akto-api-security/akto/pull/683) | Adds sensitive data types for Database URL patterns | merged / `hacktoberfest` | 상세 확보 |
| [#798](https://github.com/akto-api-security/akto/pull/798) | Support for redacting api collections and data types | merged / `master` | 상세 확보 |
| [#883](https://github.com/akto-api-security/akto/pull/883) | False positive fixes | merged / `develop` | 핵심 patch 검토 |
| [#997](https://github.com/akto-api-security/akto/pull/997) | show request headers only on vulnerableapis collection and add remove_auth_headers tests | merged / `feature_req_header_vuln_col` | 상세 확보 |
| [#1110](https://github.com/akto-api-security/akto/pull/1110) | modify multiple auth tokens | merged / `master` | 상세 확보 |
| [#1121](https://github.com/akto-api-security/akto/pull/1121) | disable aws secret pii | merged / `master` | 핵심 patch 검토 |
| [#1163](https://github.com/akto-api-security/akto/pull/1163) | Hotfix/sample data regex and cidr | merged / `master` | 상세 확보 |
| [#1202](https://github.com/akto-api-security/akto/pull/1202) | Added changes to create api groups using regex | merged / `master` | 상세 확보 |
| [#1229](https://github.com/akto-api-security/akto/pull/1229) | Update Automated API groups regex | merged / `develop` | 상세 확보 |
| [#1231](https://github.com/akto-api-security/akto/pull/1231) | Support redact for cookies and graphql | merged / `develop` | 핵심 patch 검토 |
| [#1248](https://github.com/akto-api-security/akto/pull/1248) | redact query params | merged / `develop` | 핵심 patch 검토 |
| [#1249](https://github.com/akto-api-security/akto/pull/1249) | query redact in runtime | merged / `develop` | 핵심 patch 검토 |
| [#1254](https://github.com/akto-api-security/akto/pull/1254) | fix filter for sensitive data | merged / `master` | 상세 확보 |
| [#1358](https://github.com/akto-api-security/akto/pull/1358) | Custom auth header auth check | merged / `master` | 상세 확보 |
| [#1359](https://github.com/akto-api-security/akto/pull/1359) | always upsert auth header in case of bola | merged / `master` | 핵심 patch 검토 |
| [#1363](https://github.com/akto-api-security/akto/pull/1363) | handling npe while skipping-reason-stringbuilder for private_variable_context/regex  | merged / `master` | 핵심 patch 검토 |
| [#1378](https://github.com/akto-api-security/akto/pull/1378) | remove api collection check redact | merged / `feature/cyborg-release` | 상세 확보 |
| [#1382](https://github.com/akto-api-security/akto/pull/1382) | support custom auth header check | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#1491](https://github.com/akto-api-security/akto/pull/1491) | Sensitive key redaction | merged / `feature/mini-runtime-release` | 핵심 patch 검토 |
| [#1492](https://github.com/akto-api-security/akto/pull/1492) | Handle redacted field | merged / `feature/cyborg-release` | 핵심 patch 검토 |
| [#1565](https://github.com/akto-api-security/akto/pull/1565) | show non-sensitive data | merged / `master` | 상세 확보 |
| [#1572](https://github.com/akto-api-security/akto/pull/1572) | add reset job for data types | merged / `master` | 상세 확보 |
| [#1579](https://github.com/akto-api-security/akto/pull/1579) | pii-types | merged / `master` | 상세 확보 |
| [#1583](https://github.com/akto-api-security/akto/pull/1583) | Feature/datatype to test | merged / `master` | 상세 확보 |
| [#1600](https://github.com/akto-api-security/akto/pull/1600) | sensitive data count fix | merged / `master` | 상세 확보 |
| [#1610](https://github.com/akto-api-security/akto/pull/1610) | modify data type | merged / `master` | 상세 확보 |
| [#1611](https://github.com/akto-api-security/akto/pull/1611) | Initial regex text fixed | merged / `master` | 상세 확보 |
| [#1619](https://github.com/akto-api-security/akto/pull/1619) | update versions for CVE fixes in data ingestion service | merged / `feature_data_ingestion_service` | 핵심 patch 검토 |
| [#1620](https://github.com/akto-api-security/akto/pull/1620) | upgrade versions to fix CVEs in database abstractor service | merged / `feature/cyborg-release` | 상세 확보 |
| [#1621](https://github.com/akto-api-security/akto/pull/1621) | use corretto instead of openjdk to fix cve | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#1628](https://github.com/akto-api-security/akto/pull/1628) | Feature/remove false positive from testing | merged / `master` | 상세 확보 |
| [#1639](https://github.com/akto-api-security/akto/pull/1639) | Fixing host regex condition | merged / `master` | 상세 확보 |
| [#1722](https://github.com/akto-api-security/akto/pull/1722) | fixing regex error | merged / `master` | 상세 확보 |
| [#1752](https://github.com/akto-api-security/akto/pull/1752) | allow users to modify akto data types | merged / `master` | 상세 확보 |
| [#1760](https://github.com/akto-api-security/akto/pull/1760) | Feature/edit akto data type cyborg | closed / unmerged / `feature/cyborg-release` | 상세 확보 |
| [#1761](https://github.com/akto-api-security/akto/pull/1761) | Feature/edit akto data type mini runtime | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#1762](https://github.com/akto-api-security/akto/pull/1762) | Feature/edit akto data type cyborg | merged / `feature/cyborg-release` | 상세 확보 |
| [#1764](https://github.com/akto-api-security/akto/pull/1764) | allow users to edit akto custom data type | merged / `master` | 상세 확보 |
| [#1771](https://github.com/akto-api-security/akto/pull/1771) | fixing regex split check | merged / `master` | 상세 확보 |
| [#1879](https://github.com/akto-api-security/akto/pull/1879) | add inactive field to akto data types | merged / `master` | 상세 확보 |
| [#1949](https://github.com/akto-api-security/akto/pull/1949) | cve version upgrades for modules | merged / `master` | 상세 확보 |
| [#1955](https://github.com/akto-api-security/akto/pull/1955) | update cve versions | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#1965](https://github.com/akto-api-security/akto/pull/1965) | fix cve packages | merged / `feature/mini-runtime-release` | 핵심 patch 검토 |
| [#1966](https://github.com/akto-api-security/akto/pull/1966) | Feature/CVE fixes | open / unmerged / `master` | 상세 확보 |
| [#1992](https://github.com/akto-api-security/akto/pull/1992) | handle regex replace for wordlist | merged / `master` | 상세 확보 |
| [#2068](https://github.com/akto-api-security/akto/pull/2068) | Fixing token datatype operator | merged / `master` | 상세 확보 |
| [#2069](https://github.com/akto-api-security/akto/pull/2069) | Hotfix/fix reset data types | merged / `master` | 상세 확보 |
| [#2083](https://github.com/akto-api-security/akto/pull/2083) | add fill data type button | merged / `master` | 상세 확보 |
| [#2197](https://github.com/akto-api-security/akto/pull/2197) | working e2e for sensitive data type | merged / `temp/temp_ai_agents_backend` | 상세 확보 |
| [#2267](https://github.com/akto-api-security/akto/pull/2267) | Refactor search filters and update ID generation in Sensitive Data Ex… | merged / `master` | 상세 확보 |
| [#2316](https://github.com/akto-api-security/akto/pull/2316) | New detect tab in sensitive data page | merged / `master` | 상세 확보 |
| [#2418](https://github.com/akto-api-security/akto/pull/2418) | Use find for regex validation | merged / `master` | 핵심 patch 검토 |
| [#2630](https://github.com/akto-api-security/akto/pull/2630) | redact pii data in postgres sample | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#2674](https://github.com/akto-api-security/akto/pull/2674) | Fix XSS vulnerability in login.jsp by escaping JavaScript strings | open / unmerged / `master` | 핵심 patch 검토 |
| [#2908](https://github.com/akto-api-security/akto/pull/2908) | Not redacting apis from source BURP | merged / `master` | 핵심 patch 검토 |
| [#2914](https://github.com/akto-api-security/akto/pull/2914) | remove false positive prone payloads | merged / `master` | 상세 확보 |
| [#2958](https://github.com/akto-api-security/akto/pull/2958) | fixed query param and auth headers missing in sse request | merged / `master` | 상세 확보 |
| [#3030](https://github.com/akto-api-security/akto/pull/3030) | fix cves | merged / `master` | 상세 확보 |
| [#3042](https://github.com/akto-api-security/akto/pull/3042) | remove cves | merged / `master` | 상세 확보 |
| [#3045](https://github.com/akto-api-security/akto/pull/3045) | Hotfix/fix cves dbabs | merged / `feature/cyborg-release` | 상세 확보 |
| [#3055](https://github.com/akto-api-security/akto/pull/3055) | redact only on mirroring source | merged / `master` | 핵심 patch 검토 |
| [#3131](https://github.com/akto-api-security/akto/pull/3131) | Feature/testing visibility updated regex  | merged / `feature/testing_visibility` | 상세 확보 |
| [#3136](https://github.com/akto-api-security/akto/pull/3136) | updated regex to pass unit tests | merged / `feature/testing_visibility` | 상세 확보 |
| [#3178](https://github.com/akto-api-security/akto/pull/3178) | updated regex | merged / `feature/testing_visibility` | 상세 확보 |
| [#3194](https://github.com/akto-api-security/akto/pull/3194) | updated regex with response.body flagging | merged / `feature/testing_visibility` | 상세 확보 |
| [#3497](https://github.com/akto-api-security/akto/pull/3497) | Feature/keep sample data redaction | merged / `master` | 핵심 patch 검토 |
| [#3528](https://github.com/akto-api-security/akto/pull/3528) | added regex feature in threat-activity page | merged / `master` | 상세 확보 |
| [#3574](https://github.com/akto-api-security/akto/pull/3574) | add VIN data type | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#3596](https://github.com/akto-api-security/akto/pull/3596) | Feature/vin data type support | merged / `master` | 상세 확보 |
| [#3614](https://github.com/akto-api-security/akto/pull/3614) | added support for vin support data type | merged / `master` | 상세 확보 |
| [#3630](https://github.com/akto-api-security/akto/pull/3630) | Adding support for akto data type in reset retro | merged / `master` | 상세 확보 |
| [#3649](https://github.com/akto-api-security/akto/pull/3649) | Feature/regex extract | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#3652](https://github.com/akto-api-security/akto/pull/3652) | regex extract | merged / `master` | 상세 확보 |
| [#3711](https://github.com/akto-api-security/akto/pull/3711) | add support for regex extract in url | open / unmerged / `master` | 상세 확보 |
| [#3808](https://github.com/akto-api-security/akto/pull/3808) | fix reset data types w.r.t. query params | merged / `master` | 상세 확보 |
| [#3832](https://github.com/akto-api-security/akto/pull/3832) | fix: handle regex errors in API collection creation and updates | merged / `hotfix/regex_errors` | 상세 확보 |
| [#3843](https://github.com/akto-api-security/akto/pull/3843) | Hotfix/regex errors | merged / `master` | 상세 확보 |
| [#4090](https://github.com/akto-api-security/akto/pull/4090) | Update learn more links and add fallback logic for sensitive data types | merged / `master` | 상세 확보 |
| [#4095](https://github.com/akto-api-security/akto/pull/4095) | fixed cookies data type | merged / `master` | 상세 확보 |
| [#4097](https://github.com/akto-api-security/akto/pull/4097) | fixed cookies data type | merged / `master` | 상세 확보 |
| [#4098](https://github.com/akto-api-security/akto/pull/4098) | fixed cookies datatype for dast | merged / `feature/cyborg-release` | 상세 확보 |
| [#4134](https://github.com/akto-api-security/akto/pull/4134) | fix: update regex to allow negative numbers in inventory id | merged / `master` | 상세 확보 |
| [#4252](https://github.com/akto-api-security/akto/pull/4252) | add support for url regex in test auth conditions | merged / `master` | 상세 확보 |
| [#4256](https://github.com/akto-api-security/akto/pull/4256) | add url regex support | merged / `feature/cyborg-release` | 상세 확보 |
| [#4270](https://github.com/akto-api-security/akto/pull/4270) | url regex support for roles in mini-testing | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#4607](https://github.com/akto-api-security/akto/pull/4607) | added screenshot support in automated auth token | merged / `master` | 상세 확보 |
| [#4708](https://github.com/akto-api-security/akto/pull/4708) | False Positive Stop Ingestion At Backend | merged / `master` | 상세 확보 |
| [#4774](https://github.com/akto-api-security/akto/pull/4774) | Adding fallbacks to remove false positives of blocking user | merged / `master` | 상세 확보 |
| [#4784](https://github.com/akto-api-security/akto/pull/4784) | fix: add database url fintech patterns (#90) | open / unmerged / `master` | 상세 확보 |
| [#4823](https://github.com/akto-api-security/akto/pull/4823) | Redact auth headers | merged / `master` | 상세 확보 |
| [#4877](https://github.com/akto-api-security/akto/pull/4877) | Feature/pii data count guardrail | merged / `master` | 상세 확보 |
| [#4878](https://github.com/akto-api-security/akto/pull/4878) | update pii data type in guardrails | merged / `feature/cyborg-release` | 상세 확보 |
| [#4951](https://github.com/akto-api-security/akto/pull/4951) | update claude hooks for masking tool input | merged / `master` | 상세 확보 |
| [#5317](https://github.com/akto-api-security/akto/pull/5317) | add auth token to scripts and code | merged / `master` | 상세 확보 |
| [#5330](https://github.com/akto-api-security/akto/pull/5330) | added passing of auth token from data ingestion service to guardrails service | merged / `master` | 상세 확보 |
| [#5394](https://github.com/akto-api-security/akto/pull/5394) | remove false positive | open / unmerged / `master` | 상세 확보 |
| [#5415](https://github.com/akto-api-security/akto/pull/5415) | support regex_replace in mdoify header operation | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#5487](https://github.com/akto-api-security/akto/pull/5487) | Make RAG detection robust to reduce false positives | merged / `feature/mini-runtime-release` | 상세 확보 |
| [#5498](https://github.com/akto-api-security/akto/pull/5498) | Add accurate, verified vulnerability evidence for test results | merged / `master` | 핵심 patch 검토 |
| [#5510](https://github.com/akto-api-security/akto/pull/5510) | Add cookie redact support | open / unmerged / `feature/mini-runtime-release` | 상세 확보 |
| [#5519](https://github.com/akto-api-security/akto/pull/5519) | add cookie redact | merged / `master` | 핵심 patch 검토 |
| [#5542](https://github.com/akto-api-security/akto/pull/5542) | added bearer for auth token | merged / `feature/cyborg-release` | 상세 확보 |
| [#5630](https://github.com/akto-api-security/akto/pull/5630) | remove regex for api key header detection | merged / `temp/new_activate_traffic_jobs` | 상세 확보 |
| [#5682](https://github.com/akto-api-security/akto/pull/5682) | hyperscan for PII redaction | open / unmerged / `master` | 제안 구성 확인 |
| [#5718](https://github.com/akto-api-security/akto/pull/5718) | refactor: simplify ignore phrase redaction logic by removing placehol… | merged / `master` | 상세 확보 |
| [#5720](https://github.com/akto-api-security/akto/pull/5720) | test: enhance ignore phrase matcher tests for redaction logic, JSON v… | merged / `master` | 상세 확보 |
| [#5769](https://github.com/akto-api-security/akto/pull/5769) | change prompt to have context of regex prefilter | merged / `master` | 상세 확보 |
| [#5801](https://github.com/akto-api-security/akto/pull/5801) | remove sensitive data and audit data from argus product | merged / `master` | 상세 확보 |
| [#5833](https://github.com/akto-api-security/akto/pull/5833) | update system prompt to fix the false positives | merged / `feature/cyborg-release` | 상세 확보 |
| [#5836](https://github.com/akto-api-security/akto/pull/5836) | update system prompt to fix the false positives | merged / `feature/cyborg-release` | 상세 확보 |
| [#5841](https://github.com/akto-api-security/akto/pull/5841) | update system prompt to fix the false positives | merged / `feature/cyborg-release` | 상세 확보 |
| [#5863](https://github.com/akto-api-security/akto/pull/5863) | prevent redaction of common types like datetime, location | merged / `master` | 핵심 patch 검토 |
| [#5881](https://github.com/akto-api-security/akto/pull/5881) | chore: remove auth header as session id | merged / `master` | 핵심 patch 검토 |
| [#5902](https://github.com/akto-api-security/akto/pull/5902) | fix the redaction bug of agent-guard | merged / `master` | 핵심 patch 검토 |
| [#5909](https://github.com/akto-api-security/akto/pull/5909) | point the pii password to call azure foundry | merged / `master` | 상세 확보 |
| [#5910](https://github.com/akto-api-security/akto/pull/5910) | Hotfix/sensitive data fix mini runtime | closed / unmerged / `master` | 상세 확보 |
| [#5915](https://github.com/akto-api-security/akto/pull/5915) | fix : patch vulnerabilities | merged / `master` | 핵심 patch 검토 |
| [#5961](https://github.com/akto-api-security/akto/pull/5961) | added regex handling | merged / `master` | 상세 확보 |
| [#5983](https://github.com/akto-api-security/akto/pull/5983) | updated prompts to reduce false positives and improved message logging | merged / `feature/cyborg-release` | 상세 확보 |
| [#6112](https://github.com/akto-api-security/akto/pull/6112) | Fix &quot;Access Restricted&quot; gate blocking open-source local_deploy dashboards | open / unmerged / `master` | 핵심 patch 검토 |
| [#6121](https://github.com/akto-api-security/akto/pull/6121) | feat: add support for llm based redaction | merged / `master` | 핵심 patch 검토 |
| [#6122](https://github.com/akto-api-security/akto/pull/6122) | feat: add custom redaction support in cyborg | merged / `feature/cyborg-release` | 상세 확보 |
| [#6149](https://github.com/akto-api-security/akto/pull/6149) | fix: PII block precedence over policy precedence | merged / `master` | 상세 확보 |
| [#6150](https://github.com/akto-api-security/akto/pull/6150) | fix: PII block precedence over policy precedence | merged / `master` | 핵심 patch 검토 |
| [#6153](https://github.com/akto-api-security/akto/pull/6153) | chore: add banner for custom redaction support | merged / `master` | 상세 확보 |
| [#6183](https://github.com/akto-api-security/akto/pull/6183) | update llm redaction based banner | merged / `master` | 상세 확보 |
| [#6205](https://github.com/akto-api-security/akto/pull/6205) | fix: redaction payload threat reporting | merged / `master` | 상세 확보 |
| [#6240](https://github.com/akto-api-security/akto/pull/6240) | fix: PII email detection logic | merged / `master` | 핵심 patch 검토 |
| [#6278](https://github.com/akto-api-security/akto/pull/6278) | Feature/external data type resolver cyborg | merged / `feature/cyborg-release` | 핵심 patch 검토 |
| [#6279](https://github.com/akto-api-security/akto/pull/6279) | Feature/external data type resolver | merged / `feature/mini-runtime-release` | 핵심 patch 검토 |
| [#6309](https://github.com/akto-api-security/akto/pull/6309) | fix: enforce product-scope NO_ACCESS check regardless of RBAC billing tier | merged / `master` | 핵심 patch 검토 |
| [#6359](https://github.com/akto-api-security/akto/pull/6359) | added a hard black list for hooks field (handling false positives) | merged / `feature/cyborg-release` | 상세 확보 |
| [#6402](https://github.com/akto-api-security/akto/pull/6402) | fix pii data being sent in the api request payload | merged / `master` | 핵심 patch 검토 |
| [#6406](https://github.com/akto-api-security/akto/pull/6406) | Feature/guardrail violations redaction | open / unmerged / `master` | 상세 확보 |
| [#6463](https://github.com/akto-api-security/akto/pull/6463) | Feature/guardail claude org id with pii llm | open / unmerged / `master` | 상세 확보 |
| [#6487](https://github.com/akto-api-security/akto/pull/6487) | fix: update reason field in prompts to prevent quoting PII and sensit… | merged / `master` | 핵심 patch 검토 |
| [#6513](https://github.com/akto-api-security/akto/pull/6513) | fix: stop reason-enrichment prompt from quoting PII | merged / `feat/async-reason` | 핵심 patch 검토 |
| [#6530](https://github.com/akto-api-security/akto/pull/6530) | add response regex extract | merged / `master` | 상세 확보 |
| [#6569](https://github.com/akto-api-security/akto/pull/6569) | Fix role escalation in updateUserScopeRoleMapping and cross-account p… | open / unmerged / `master` | 핵심 patch 검토 |
| [#6571](https://github.com/akto-api-security/akto/pull/6571) | Extract login-flow values from non-JSON responses via step regex | merged / `feature/mini-runtime-release` | 상세 확보 |

## 6. 확보한 tests-library PR 상세 전체 목록

| PR | 제목 | 상태 / base | 검토 수준 |
|---|---|---|---|
| [#13](https://github.com/akto-api-security/tests-library/pull/13) | Nuclei templates for port scanning and fetch sensitive files via SSRF | closed / unmerged / `master` | 상세 확보 |
| [#43](https://github.com/akto-api-security/tests-library/pull/43) | BOLA and BUA templates added (10) | closed / unmerged / `master` | 상세 확보 |
| [#44](https://github.com/akto-api-security/tests-library/pull/44) | false positives modifications | merged / `master` | 상세 확보 |
| [#45](https://github.com/akto-api-security/tests-library/pull/45) | BOLA new templates | closed / unmerged / `master` | 상세 확보 |
| [#47](https://github.com/akto-api-security/tests-library/pull/47) | BOLA templates x 4 [Prod Ready] | merged / `master` | 상세 확보 |
| [#48](https://github.com/akto-api-security/tests-library/pull/48) | 7 BOLA templates | merged / `master` | 상세 확보 |
| [#62](https://github.com/akto-api-security/tests-library/pull/62) | 7 BFLA templates added | merged / `master` | 상세 확보 |
| [#80](https://github.com/akto-api-security/tests-library/pull/80) | Update BOLAByChangingAuthToken.yaml | closed / unmerged / `master` | 관련 patch 검토 |
| [#81](https://github.com/akto-api-security/tests-library/pull/81) | API Error Handling &lt;-&gt; BOLA | merged / `master` | 관련 patch 검토 |
| [#85](https://github.com/akto-api-security/tests-library/pull/85) | BOLA fix v2 | merged / `master` | 관련 patch 검토 |
| [#86](https://github.com/akto-api-security/tests-library/pull/86) | BOLA hot fix | merged / `master` | 관련 patch 검토 |
| [#104](https://github.com/akto-api-security/tests-library/pull/104) | false positive fix | merged / `master` | 상세 확보 |
| [#121](https://github.com/akto-api-security/tests-library/pull/121) | Command Injection False positives | merged / `master` | 상세 확보 |
| [#162](https://github.com/akto-api-security/tests-library/pull/162) | BOLA | closed / unmerged / `master` | 상세 확보 |
| [#167](https://github.com/akto-api-security/tests-library/pull/167) | html fix for bola | merged / `master` | 관련 patch 검토 |
| [#203](https://github.com/akto-api-security/tests-library/pull/203) | fix false positives | merged / `master` | 상세 확보 |
| [#208](https://github.com/akto-api-security/tests-library/pull/208) | PII Data Leak and security config | merged / `master` | 관련 patch 검토 |
| [#214](https://github.com/akto-api-security/tests-library/pull/214) | remove pii data leak template | merged / `master` | 관련 patch 검토 |
| [#216](https://github.com/akto-api-security/tests-library/pull/216) | Remove pii data threat template | merged / `master` | 관련 patch 검토 |
| [#227](https://github.com/akto-api-security/tests-library/pull/227) | Bola templates updated | closed / unmerged / `master` | 목록/대표 변경 확인 |
| [#228](https://github.com/akto-api-security/tests-library/pull/228) | Bola templates updated | merged / `pro` | 관련 patch 검토 |
| [#284](https://github.com/akto-api-security/tests-library/pull/284) | updated regex to handle CMD false positive | merged / `master` | 상세 확보 |
| [#296](https://github.com/akto-api-security/tests-library/pull/296) | add: new agentic tests for Broken Object Level Authorization (BOLA) v… | open / unmerged / `master` | 상세 확보 |
| [#297](https://github.com/akto-api-security/tests-library/pull/297) | add: new agentic tests for Broken Object Level Authorization (BOLA) v… | open / unmerged / `master` | 목록/대표 변경 확인 |
