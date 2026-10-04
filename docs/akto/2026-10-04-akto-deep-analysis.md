# Akto 심층 분석: 기존 기능과 AP-EYE 기여 후보

확인일: 2026-10-04. 담당: 심재훈. 관련 작업: [AP-EYE #5](https://github.com/AP-EYE/workspace/issues/5).

**결정: Akto 기여를 우선한다. URL 공개·비공개 컨텍스트의 결함 후보를 서버에서 재현한 뒤 작은 수정 PR을 검토한다. 한국어 개인정보는 기존 사용자 정의 유형 설정부터 평가한다. fork는 필요한 변경의 수용이 어려울 때 검토한다.**

## 확인 범위와 증거 수준

- Akto 소스: [302dad92e1549b7a84ce73eded447ad5d18124f0](https://github.com/akto-api-security/akto/commit/302dad92e1549b7a84ce73eded447ad5d18124f0).
- 별도 tests-library: [ce2267da7e28927876b41d944e63bdde10e41e00](https://github.com/akto-api-security/tests-library/commit/ce2267da7e28927876b41d944e63bdde10e41e00).
- 조사 흐름: 대시보드 설정, 트래픽 기반 API·필드 생성, 인증 교체 테스트, 응답 검증, 민감정보·보고서 표시.
- 직접 실행: 원본 Java 메서드 6개를 분리해 JDK 8에서 입력 20개 실행, 핵심 기대 결과 8개 검사 통과. [전체 결과와 해시](evidence/2026-10-04-component-results.json), [재현 방법](reproduction/README.md).
- 미실행: Akto 서버, MongoDB가 포함된 URL 컨텍스트, 실제 YAML 엔진, 대시보드 등록과 수집, 전체 Maven 테스트. Docker 엔진은 중지 상태였고 Maven은 설치되어 있지 않았다.
- 합성 입력은 메서드 동작을 설명하는 진단 자료다. 제품 전체의 오탐률이나 최종 평가 데이터셋으로 사용하지 않는다.

## 기존 기능부터 확인한 결과

| 영역 | 이미 제공하는 기능 | 설정으로 먼저 확인할 부분 | 보완 가능성과 제한 |
|---|---|---|---|
| 인가 | 사용자·역할별 인증정보, 인증 헤더 교체, 역할·접근 유형 컨텍스트 | 다른 사용자 토큰, 공개 API 설정, 계정별 충분한 트래픽 | 트래픽에서 추정한 공유 여부와 실제 접근 권한은 다를 수 있음 |
| BOLA | 토큰·사용자 ID 변경 템플릿, 코드·길이·유사도 검증 | 오류 본문 제외, API 선택, 사용자 정의 본문 조건 | 혼합 목록과 객체별 연결 관계 검증 필요 |
| 개인정보 | 기본 유형, 키·값 및 AND/OR 사용자 정의 조건 | 한국어 키·형식 정규식, 민감 여부·우선순위 | 국내 전화번호 기본값과 문장 문맥은 별도 평가 |
| 집계·마스킹 | API별 민감 필드·통계·샘플, 유형·컬렉션 마스킹 | 필드·응답·고유값 집계 단위와 마스킹 수준 | 관측 통계가 피해 정보주체 수는 아님 |
| 보고서 | PDF, 영향 API, 설명·심각도, 요청·응답 증거 | 기존 보고서·이슈 상세 활용 | 실제 침해 시점·전체 피해 범위·대응 내역은 별도 |
| AI | AktoGPT 정규식 생성, agentic 코드·템플릿 속성 | 배포판·설정별 제공 범위 | AI 존재가 한국어 법적 분류 성능을 증명하지 않음 |

설정 근거: [역할별 테스트](https://docs.akto.io/api-security-testing/how-to/conduct-role-based-testing), [User config](https://docs.akto.io/api-security-testing/concepts/user-config), [컨텍스트](https://docs.akto.io/test-editor/concepts/test-yaml-syntax-detailed/contexts), [사용자 정의 유형](https://docs.akto.io/api-inventory/how-to/create-a-custom-data-type), [마스킹](https://docs.akto.io/api-inventory/how-to/redact-sensitive-data).

## 인가·BOLA 판정 흐름

토큰 교체 템플릿은 원본 2xx와 private variable 컨텍스트가 있는 API를 고른 뒤 다른 인증정보로 요청한다. 바뀐 응답의 2xx, 본문 길이, 원본과 90% 이상 일치 조건을 확인한다.

현재 외부 템플릿에는 OPTIONS 제외와 오류 문자열 제외도 있다. 서버 포함 템플릿과 외부 버전이 달라 실제 설치에서 로드한 버전을 기록해야 한다. [외부 템플릿](https://github.com/akto-api-security/tests-library/blob/ce2267da7e28927876b41d944e63bdde10e41e00/Broken-Object-Level-Authorization/BOLAByChangingAuthToken.yaml), [서버 포함 템플릿](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/dashboard/src/main/resources/inbuilt_test_yaml_files/BOLAByChangingAuthToken.yaml).

private 컨텍스트는 트래픽과 사용자 정보를 이용한다. 공식 문서도 단일 계정·부족한 트래픽에서 정확도가 떨어질 수 있다고 설명한다. 기존 역할·공개 접근 설정을 적용한 비교가 먼저다. [컨텍스트 구현](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java#L94).

### 응답 비교 분리 실행

길이 구현은 JSON 원소 수가 아니라 `trim().length() - 2`다. 비교기는 배열 인덱스를 버리고 필드 경로별 값 집합을 비교한다. [길이](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java#L478), [비교기](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/utils/src/main/java/com/akto/testing/Utils.java#L381), [값 추출](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/utils/src/main/java/com/akto/runtime/RuntimeUtil.java#L113).

| 원본 → 바뀐 응답 | 유사도 | 길이+90% 조건 | 해석 |
|---|---:|---|---|
| 빈 배열 → 빈 배열, 빈 객체 → 빈 객체 | 100% | 미통과 | 빈 200이면 모두 취약하다는 주장은 틀림 |
| 동일한 data:빈 배열 래퍼 | 100% | 통과 | 감싼 빈 목록은 구조 조건 필요 |
| 동일한 허용 공유 객체 | 100% | 통과 | 공개 설정·독립 권한 증거 필요 |
| 동일한 금지 비공개 객체 | 100% | 통과 | 실제 금지 권한을 확인했을 때 증거 후보 |
| 비공개 객체 → 빈 목록 | 0% | 미통과 | 정상 필터링 사례 |
| 비공개 객체 → 다른 허용 객체 | 0% | 미통과 | 다른 응답 자체는 BOLA 증거가 아님 |
| 비공개 객체 → 해당 객체+다른 허용 객체 | 0% | 미통과 | 금지 객체가 남아도 놓칠 수 있는 비교기 사례 |
| 두 객체의 값 연결만 서로 교환 | 100% | 통과 | 객체별 ID·본문 연결이 손실됨 |

**통과는 API 선택·2xx를 가정한 길이·유사도 조건의 재구성 결과다. 실제 Akto의 최종 취약점 결과가 아니다.** 오류 문자열·역할 등 전체 경로는 실행하지 않았다. 공유·금지 여부는 입력에 부여한 정답 설명이다.

고정된 실험 객체는 기존 본문 조건으로 금지 ID·표식의 포함 여부를 검사하는 설정도 먼저 시도할 수 있다. 실제 YAML 실행은 미확인이다. 개선 근거는 본문 검사 기능의 부재가 아니라 객체 구조·권한 증거의 일반화에서 기존 설정으로 해결되지 않는 범위다.

### 우선 기여 후보: URL private 컨텍스트 정보 손실

[FilterAction.getPrivateResourceCount](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java#L1464)는 URL 변수의 `querySti(...)` 결과를 바로 `new SingleTypeInfo()`로 덮어쓴다. [getIsPrivate](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/type/SingleTypeInfo.java#L956)는 관측 수가 0이면 true를 반환한다.

분리 실행에서 공개 관측 10/10인 객체는 private=false였지만 새 객체로 교체하면 true가 됐다. 조회된 공개 여부·값을 잃는 동작은 확인했다. 실제 DB 입력에서 BOLA 대상 선택에 미치는 영향은 미확인이다.

**한 줄 삭제만으로 해결된다고 단정하지 않는다.** 이후 fallback도 null·공개·빈 값 상태를 함께 처리하면서 privateCnt를 증가시킨다. 공개로 확인된 값, 정보 없는 값, 비공개 값을 구분하고 중복 증가 여부까지 전체 분기를 검증해야 한다.

## 한국어 개인정보: 기존 설정을 먼저 평가

[KeyTypes](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/type/KeyTypes.java#L253)는 사용자 정의 유형을 분류 흐름에 적용한다. [CustomDataType](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/CustomDataType.java)는 키·값 조건을 결합한다. [RegexPredicate](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/data_types/RegexPredicate.java)는 Java 정규식의 전체 문자열 일치를 사용한다.

직접 확인한 입력:

- 기본 전화번호 메서드: `+821012345678`, `+82 10 1234 5678`은 true. `010-1234-5678`, `01012345678`은 false. 기본 파싱 지역이 KR로 지정되어 있지 않다. [구현](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/type/KeyTypes.java#L393).
- 키 `^(?:주민등록번호|resident_registration_number|rrn)$`, 값 `^[0-9]{6}-?[0-9]{7}$`의 AND: 한국어 키와 합성 13자리 형식을 처리했다.
- 같은 13자리 order_id는 키 조건으로 제외했다. 값 조건만으로는 구분할 수 없다.
- `.*진단.*`은 개인 진단 문장과 일반 서비스 안내를 모두 통과했다. 키워드 일치를 문맥 분류 성능으로 해석하면 안 된다.

주민번호 예시는 `000000-0000000` 같은 합성 형식이다. 번호 유효성·실제 개인정보·법적 분류의 정답을 입증하지 않는다. UI 등록·전체 runtime 적용은 미실행이다.

조사한 pii-types, DAO, 주요 runtime·dashboard 코드에서 한국 식별자 전용 정의를 찾지 못했다. 기본 SSN은 미국 형식이고 [fintech 목록](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/pii-types/fintech.json)은 다른 국가의 예시를 제공한다. 플러그인·상용 기능까지 없다는 결론은 아니다.

우선 사용자 정의 설정으로 기준선을 만들고 주문번호·일반 문장·마스킹 값 등 음성 사례를 포함한다. 설정으로 해결되지 않는 범위만 코드 개선 후보로 남긴다.

## 집계와 사후 신고 정보

[SingleTypeInfo](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/type/SingleTypeInfo.java)는 API·필드·유형별 count, userIds, 값 집합, uniqueCount/publicCount를 저장한다. [SensitiveParamInfo](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/SensitiveParamInfo.java)는 민감 필드를, [SensitiveSampleData](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/libs/dao/src/main/java/com/akto/dto/SensitiveSampleData.java#L16)는 최대 10개 샘플을 다룬다. 인증 사용자 수, 응답 속 정보주체 수, 필드 발생 수, 고유값 수를 구분해야 한다.

[카탈로그 생성](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/api-runtime/src/main/java/com/akto/runtime/APICatalogSync.java), [민감 필드 조회](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/dashboard/src/main/java/com/akto/action/SensitiveFieldAction.java), [마스킹](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/api-runtime/src/main/java/com/akto/utils/RedactSampleData.java)을 확인했다. 마스킹은 저장 노출을 줄이지만 재현·증거 비교에 영향을 준다.

Akto에는 [PDF 생성](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/dashboard/src/main/java/com/akto/action/ReportAction.java)과 [취약점 보고서](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/dashboard/web/polaris_web/web/src/apps/dashboard/pages/testing/vulnerability_report/ReportFindings.jsx)가 있다. 보고서 기능이 없다는 결론은 부정확하다.

| 신고 항목 예 | 활용할 수 있는 Akto 정보 | 추가로 필요한 정보 |
|---|---|---|
| 기관·담당자·연락처 | 보고서 조직명 등의 입력 | 실제 담당자·책임자 확인 |
| 개인정보 항목·규모 | API·필드·유형·샘플 | 전체 범위, 정보주체 중복 제거, 집계 기준 |
| 발생 시점·경위 | 테스트 시점, 요청·응답, 취약점 설명 | 실제 침해 시점, 공격·감사 로그 |
| 피해 최소화 방법 | 영향 설명·권고 | 실제 통지·차단·피해 지원 |
| 대응 조치·구제 절차 | 개선 권고 | 수행한 조치와 담당자 검증 |

대조한 자료: [국가법령정보센터 게시 개인정보 유출등 신고서](https://www.law.go.kr/flDownload.do?bylClsCd=200203&flNm=%5B%EB%B3%84%EC%A7%80+1%5D+%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4+%EC%9C%A0%EC%B6%9C%EB%93%B1+%EC%8B%A0%EA%B3%A0%EC%84%9C&flSeq=151185997). 기관 서식의 항목 비교이며 모든 기관의 최신 공통 서식이나 신고 의무·기한 판단은 아니다.

신고 지원은 확인한 증거와 미확인 항목을 채우는 보조 기능으로 본다. 취약점 발견을 실제 유출로 간주해 자동 신고하는 기능으로 정의하지 않는다. 이번 본체는 읽기 BOLA 평가로 좁히고 신고 지원은 후속 범위로 둔다.

## 테스트·이슈·기존 PR

읽은 기존 테스트는 [FilterValidationTests](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/testing/src/test/java/com/akto/testing/FilterValidationTests.java)의 본문 조건·값 추출 테스트와 [TestRedactSampleData](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/apps/api-runtime/src/test/java/com/akto/utils/TestRedactSampleData.java)의 마스킹 테스트다. 실행하지 않았으며 이번 목록·한국어 입력을 모두 보장하는지 확인하지 못했다.

| 근거 | 확인 내용 | 해석 |
|---|---|---|
| [PR #1359](https://github.com/akto-api-security/akto/pull/1359) | BOLA 인증 헤더 upsert, 2024-08-15 머지 | 토큰 교체의 기존 유지보수 |
| [PR #798](https://github.com/akto-api-security/akto/pull/798) | 유형·컬렉션 마스킹, 2024-02-10 머지 | 기존 설정 활용 근거 |
| [PR #213](https://github.com/akto-api-security/akto/pull/213), [이슈 #212](https://github.com/akto-api-security/akto/issues/212) | 커뮤니티 참여자의 Discord 작업 머지 | 과거 기여 수용 사례 |
| [이슈 #141](https://github.com/akto-api-security/akto/issues/141) | BOLA 블로그 기여 | 탐지 결함 근거가 아님 |
| [#166](https://github.com/akto-api-security/akto/issues/166), [#14](https://github.com/akto-api-security/akto/issues/14) | 템플릿·OWASP 관련 작업 | 목록 오탐을 입증하지 않음 |

회의에서 언급된 2023~2024 BOLA 이슈의 정확한 링크는 이번 검색에서 찾지 못했다. 회의 당사자에게 확인해야 한다. 다른 이슈로 대체하지 않았고, 검색 결과 부재를 이슈가 없다는 증명으로 해석하지 않았다.

## 최근 관리 상태와 기여 절차

[GitHub 스냅샷](evidence/2026-10-04-github-snapshot.json), 2026-10-04 조회 기준:

- master 최신 확인 커밋: 2026-10-04 07:11 UTC.
- 최신 core [v2.36.9](https://github.com/akto-api-security/akto/releases/tag/v2.36.9): 10-04 07:28 UTC. v2.36.8 같은 날, v2.36.7 10-03, v2.36.6 10-01, v2.36.5 09-30. 다른 제품 태그와 구분했다.
- 스타 1,525, fork 294, 기여자 API에서 55개 계정 관측. 봇 포함이라 사람 55명이 아니다.
- open_issues_count 350은 PR을 포함한 값이다.
- 2023년 행사 당시 #212의 작업 요청은 약 9분 뒤 배정 응답, #213은 생성 약 4일 뒤 머지됐다. 단일 과거 사례이며 현재 평균 응답·머지 기간이나 SLA가 아니다.
- 최근 활동은 확인했지만 우리 제안 수용 여부·배포판 기능 동등성은 미확인이다.

[CONTRIBUTING](https://github.com/akto-api-security/akto/blob/302dad92e1549b7a84ce73eded447ad5d18124f0/CONTRIBUTING.md)은 fork, 작업 브랜치, 테스트 통과, 이유를 설명한 PR을 요구한다. 이슈에는 제품 버전과 재현 정보를 포함하며 MIT 라이선스다. 이번 조사는 업스트림 이슈·PR을 게시하지 않았다. AP-EYE 산출물은 develop 대상 PR과 팀 리뷰를 거친다.

## 심재훈의 다음 액션과 선행 조건

| 우선순위 | 액션 | 관련 위치 | 선행 조건·완료 기준 |
|---|---|---|---|
| P0 | URL 정보 손실과 fallback을 서버에서 재현하고 기존 설정 적용 결과 비교 | FilterAction.getPrivateResourceCount, SingleTypeInfo.getIsPrivate, apps/testing | 실행 환경, 공개·비공개·정보 없음 DB fixture. 값·카운트·대상 선택까지 확인 |
| P0 | 공개 STI와 관측 부족 상태를 분리하는 최소 수정안 검토 | URL 분기·회귀 테스트 | 덮어쓰기, fallback, 중복 카운트 검증. 새 코드 작업의 이슈 먼저 생성 |
| P1 | 한국어 사용자 정의 유형 등록 후 기본 설정과 비교 | CustomDataTypeAction, KeyTypes, RegexPredicate | UI·runtime 적용, 국내 번호·음성 사례 결과 저장 |
| P1 | 외부 읽기 BOLA 평가 대상 선정 | AP-EYE #6, docs/dataset/ | 논문 원문에서 정상·BOLA 권한 정답과 공개 코드 확인 |
| P2 | 기본 템플릿·기존 설정 보강·개선 판정 비교 | tests-library, Utils, RuntimeUtil | 독립 권한 증거, 빈·허용·공유·혼합 목록, 정상·보류·BOLA 정답 |
| P2 | 아키텍처·한 줄 정의 확정 | AP-EYE #7, arch/architecture.md | #5·#6 근거를 연결하고 직접 평가할 본체 하나 선택 |

후보 순서: URL 컨텍스트 결함 검증 → 기존 설정의 한국어 지원 검증 → 목록 객체 단위 판정 개선 검토. 이번 조사만으로 새 게이트웨이나 한국어 AI 분류기 개발을 결정하지 않는다.

한 줄 정의 초안: “기존 Akto는 트래픽 기반 API·개인정보 식별과 토큰 교체·응답 비교 테스트를 제공한다. 우리는 읽기 BOLA의 공개·비공개 구분과 목록 판정 근거를 보강하고, 외부 평가 대상 TBD에서 오탐률·재현율·보류율로 평가한다.”

최종 범위·데이터셋·목표 수치는 미정이다. 외부 데이터셋과 권한 정답을 확인한 뒤 정한다. 한국어 개인정보를 본체로 고르면 유형별 정밀도·재현율과 음성 사례 오류를 별도 평가한다.
