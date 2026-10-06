# Akto 심층 조사와 AP-EYE 한국어 PII 설계 판단

조사 기준: 2026-10-06 KST. 대상은 공개 소스·문서·이슈·PR이며, 상용 서비스 내부 구현 전체를 열람한 감사는 아니다.

## 먼저 알아야 할 결론

Akto는 API 요청·응답을 모아 API 목록과 데이터 구조를 만들고, 요청을 변형해 보안 문제를 검사하는 플랫폼이다. 최근 제품은 AI 에이전트·MCP·LLM 보안까지 확장됐다. AP-EYE에서는 **API 수집·재실행·결과 관리 기반으로 활용하면서, 객체 권한 판단과 한국어 PII 검증을 별도 근거로 강화하는 방향**이 적합하다.

한국어 PII를 붙일 때 가장 중요한 발견은 다음과 같다.

1. 기존 API 필드 분류는 정규식·필드 이름·개별 검증 함수가 중심이다. 국가별 규칙이 있다는 사실만으로 그 나라의 개인정보를 잘 찾는다고 볼 수 없다.
2. 최신 Akto에는 **Presidio를 이용하는 별도 anonymizer 서비스**도 있다. 다만 조사한 설정은 `en_core_web_sm`, `supported_languages=["en"]`, 임계값 `0.4`다. “Akto는 정규식만 쓴다”도, “이미 한국어가 된다”도 부정확하다.
3. 최신 Presidio에는 한국 식별번호 탐지기가 이미 존재하고, Google·Azure도 한국 관련 기능을 제공한다. 한국어 정규식 추가 자체를 새로운 연구 성과로 내세우기 어렵다.
4. Akto의 국가별 PII precision/recall/F1을 입증하는 공개 평가표는 이번 조사에서 확인하지 못했다. 제품의 지원 개수나 개별 결과의 confidence를 정확도 백분율로 읽으면 안 된다.
5. 원본 Java 로직으로 **PII 진단 입력 63개와 BOLA 비교 입력 6개**를 실행했다. 국제번호/국내번호 차이, 과도하게 느슨한 식별번호 규칙, 배열 객체 연결을 잃는 응답 비교를 확인했다. 전체 Akto 배포나 실제 고객 트래픽에 대한 성능 측정은 아니다.

## 1. 조사 범위와 증거 수준

| 조사 항목 | 확보·확인 범위 | 해석의 한계 |
|---|---|---|
| Akto 본체 공개 이슈·PR | 6,581건: 이슈 179, PR 6,402 | 전체 목록·본문·상태를 수집하고 키워드 분류. 전 PR의 모든 코드를 사람이 감사한 것은 아님 |
| PR 병합 메타데이터 | 본체 목록에 대응하는 병합 PR 5,658건 | 병합 대상은 master 외 여러 브랜치 포함. 배포 완료와 다름 |
| 관련 PR 상세 | PII·BOLA·인증·보안 키워드 선별 161건 + 추가 3건의 본문·변경파일·제공된 patch | 상세 확보 164건. 핵심 변경은 별도 검토표에 설명, 나머지는 상세 확보 단계로 명시 |
| tests-library | 공개 이슈·PR 347건, 관련 PR 상세 24건 확보 | 본체 저장소와 번호 체계가 다름 |
| 보안 advisory | 본체 GitHub API에서 공개 advisory 0건 반환 | 취약점이 없다는 증거가 아님. 비공개 제보·미등록 취약점 제외 |
| 소스 실험 | 원본 전화번호 함수/정규식 63입력, 응답 추출/비교 함수 6입력 | 컴포넌트 진단. 서비스 기동·DB·UI·실제 API 재실행은 NOT_RUN |
| 비교 제품 | Presidio 소스, Google/Azure/AWS 공식 문서, 한국어 도구 공개 평가 | 외부 제품을 같은 데이터로 직접 실행한 비교는 NOT_RUN |
| 논문 | SPY, GLiNER2-PII 원문 확보·평가절 확인 | 저자 보고 성능. 우리 재현 성능으로 표시하지 않음 |

목록은 여러 API 요청에 걸쳐 수집했으므로 원자적 스냅샷이 아니다. 별도 closed-pulls 응답과 전체 이슈 응답의 닫힌 PR 수가 1건 차이 난다. 이 보고서의 총계는 `all_issues_and_prs.json`의 6,581건을 기준으로 고정했다. 삭제된 글, 비공개 저장소, 다른 제품 저장소의 모든 변경은 포함되지 않는다.

증거 표기는 **소스 확인 / 병합 확인 / 제보·미병합 / 컴포넌트 실행 / 미실행 / 제안**을 구별한다. `closed`만으로 해결 완료라고 부르지 않는다.

## 2. Akto를 구체적인 예로 이해하기

쇼핑몰에서 Alice가 자기 주문을 조회한다고 하자.

```text
GET /orders/123 + Alice의 인증 정보
  → 응답: 주문 123, 소유자 Alice, 배송지·전화번호
```

Akto가 하는 일은 크게 네 단계다.

1. 이 트래픽을 받아 `/orders/{id}`라는 API, 요청 파라미터, 응답 필드를 목록으로 만든다.
2. 응답의 전화번호·이메일·토큰 같은 필드를 분류하고, 설정에 따라 저장 샘플을 마스킹한다.
3. 같은 요청을 Bob의 인증 정보로 보내거나 객체 번호를 바꿔 접근제어를 검사한다.
4. 원래 응답과 변형 요청의 응답을 비교해 의심 결과·실행 증거를 보여준다.

여기에는 서로 다른 질문이 있다. “전화번호가 있다”는 **데이터 분류**, “Bob에게 Alice의 전화번호가 반환됐다”는 **권한 위반**, “Akto의 DB·로그·보고서에 원문이 남았나”는 **보안 도구 자신의 데이터 보호**다. AP-EYE는 이 세 가지를 각각 검증해야 한다.

핵심 흐름은 다음과 같다. 실제 모듈 구성은 배포 방식에 따라 달라진다.

```text
미러링·HAR·Burp·Postman·명세 등 입력
          ↓
수집/파싱 → URL 정규화·필드 타입 추론 → API 인벤토리·샘플 저장
                                            ↓
                      계정·역할·인증 문맥 + YAML 검사 규칙
                                            ↓
                            요청 변형·재전송 → 응답 검증 → 결과/증거

AI 경로: 에이전트·MCP·LLM 입력/출력 → 정책·탐지기 → 허용/차단/마스킹·이벤트
```

API 플랫폼의 설명은 [공개 README][A1]와 [공식 문서][A2]에, 현재 AI 제품의 범위는 [현행 제품 페이지][A3]에 근거한다. 수집하지 못한 API는 트래픽 기반 인벤토리에서 빠질 수 있고, 명세로 가져온 API라도 유효한 인증·실행 샘플이 없으면 권한 검증 품질이 제한된다.

## 3. 제품, 코드, 배포를 구분해야 한다

| 구분 | 확인한 내용 | AP-EYE에서의 의미 |
|---|---|---|
| 기존 API 플랫폼 | 인벤토리, 민감정보 분류, YAML 검사, 역할·인증 기반 검사, 실행 결과 | 재사용 가치가 큰 중심 기반 |
| 최신 제품 포지션 | Akto Atlas/Argus, 에이전트·MCP·LLM 탐지와 가드레일 | 오래된 API 소개만 읽으면 현재 개발 방향을 놓침 |
| 공개 소스 | Java 백엔드/검사기, React UI, Python anonymizer/LLM scanner, Go guardrails wrapper 등 | 한 가지 언어나 하나의 검사기로 구성된 제품이 아님 |
| 저장소 라이선스 | 본체 MIT | 별도 의존성·모델·상용 서비스 권한까지 동일하다는 뜻은 아님 |
| SaaS/상용 self-hosted | 현재 가격 페이지는 사용량 기반·영업 문의 중심 | 임의의 월 비용이나 무료 범위를 추정하지 않음 |
| OSS self-hosted | `local_deploy`에서 Access Restricted 제보와 미병합 수정안 존재 | 연구 시작 전에 선택한 이미지로 실제 진입·검사 가능 여부 확인 필요 |

특히 [이슈 #5512][I5512]와 [PR #6112][P6112]는 plan 값이 비어 있는 로컬 설치가 UI에서 차단되는 문제를 다룬다. 조사 시점 #6112는 **open·미병합**이다. 현재 master의 `apps/main/index.js`에서도 plan 중심 분기와 local-deploy 우회 부재를 확인했다. 댓글의 임시 우회 제안을 공식 지원 정책으로 간주하지 않는다. [가격 페이지][A4]와 [라이선스][A5]를 함께 봐야 한다.

현재 루트 Compose는 MongoDB `7.0.4`, dashboard/testing의 가변 `local` 태그, puppeteer의 `latest` 태그를 사용한다. 연구 재현에는 이미지 digest·소스 commit·템플릿 commit을 따로 기록해야 한다. Compose가 Mongo 포트를 호스트에 노출한다는 것도 배포 검토사항이다. 이것만으로 특정 사용자의 서버가 외부에 노출됐다고 단정하지 않는다.

## 4. 유지보수와 커뮤니티 상태

수집 당시 본체는 stars 1,527, forks 294, contributor API 55개 계정(사용자 계정 54, bot 1)이었다. 최근 약 30일 구간인 2026-09-06 이후 생성된 목록에는 PR 267개가 있었다. 2026-10-05의 master commit과 `v2.37.0` 릴리스도 확인했다. **개발 활동은 활발하다.**

다만 PR 양은 버그 해결률이나 외부 기여 친화성의 직접 지표가 아니다. 런타임·위협 탐지·dashboard 등의 릴리스가 한 저장소에 섞여 있고, 1,900개 release 응답은 본체의 1,900개 주요 버전을 뜻하지 않는다. 장기 open 제보, 기능 브랜치 병합, 의존성 자동 PR도 함께 있다. 기여할 때는 담당자가 실제로 받아들이는 대상 브랜치와 재현 환경부터 맞춰야 한다. [저장소][A1], [기여 가이드][A6]

## 5. 과거에 무엇이 약했고 어떻게 바뀌었나

아래는 본문·patch·현재 코드에서 의미를 확인한 대표 사례다. 날짜·브랜치·추가 사례는 `HISTORY-REVIEW.ko.md`, 전체 목록은 `ISSUE-PR-INDEX.csv`에 있다.

| 사례 | 이전 문제/약점 | 수정과 상태 | 과장하면 안 되는 부분 |
|---|---|---|---|
| [#527][P527] | 값에 적용할 규칙이 key 조건에도 들어가는 매핑 문제 | key/value 조건 분리, develop 병합 | 한국어 전체 탐지 개선을 뜻하지 않음 |
| [#1359][P1359] | BOLA 검사 시 필요한 인증 헤더가 없으면 제대로 교체·추가되지 않을 수 있음 | 인증 교체 경로에 upsert 적용, master 병합 | 권한 판단의 전체 정확도는 별도 |
| [#1363][P1363] | private context 검사 이유를 만드는 StringBuilder가 null | 초기화로 NPE 방지, master 병합 | 크래시 수정이며 BOLA 의미 판정 완성은 아님 |
| [#1231][P1231], [#1248][P1248], [#1249][P1249] | cookie/GraphQL/query 파라미터 마스킹 범위 부족 | 해당 처리 추가, 당시 develop 병합 | 이후 설정·입력 소스별 적용 차이 있음 |
| [#1491][P1491], [#1492][P1492] | redacted 설정 전달 및 민감 샘플 처리 문제 | mapper와 동기화 경로 보완, 배포 브랜치 병합 | master 병합으로 기록하면 부정확 |
| [#2418][P2418] | 검사기의 정규식이 문자열 전체 일치를 요구 | 특정 test-editor helper를 `matches`→`find`로 변경 | PII `RegexPredicate`는 현재도 `matches`; 서로 다른 경로 |
| [#5863][P5863] | 평범한 날짜·위치 등 과잉 마스킹 | 기본 제외 타입에 DATE_TIME/NRP/LOCATION, master 병합 | 오탐 감소와 탐지 범위 축소의 교환 |
| [#5902][P5902] | 낮은 점수의 탐지가 목록 번호·텍스트를 훼손 | anonymizer 임계값 0.4와 회귀 테스트, master 병합 | 0.4는 정확도 40%라는 뜻이 아님 |
| [#5881][P5881] | Authorization 값이 session ID 후보로 쓰임 | 해당 후보 제거, master 병합 | 실제 외부 유출 사고를 확인한 것은 아님 |
| [#5498][P5498] | LLM이 만든 부정확한 근거·자기 인증정보를 누출 근거로 제시할 위험 | 원문 위치 확인·credential 제외·결정적 검출기와 병합, master 병합 | 근거가 원문에 존재함과 실제 취약함은 다른 검증 |
| [#6309][P6309] | RBAC 요금제 분기가 제품별 NO_ACCESS 검사까지 건너뜀 | 제품 접근 차단을 과금 분기보다 먼저 검사, master 병합·현재 순서 확인 | 과거 제보의 실제 고객 피해는 미확인 |
| [#6402][P6402] | 사용자명 등의 lookup map을 브라우저가 API payload로 반복 전달 | 서버에서 조회하도록 이동, master 병합 | 모든 PII 저장/전송을 없앤 수정은 아님 |
| [#6487][P6487], [#6513][P6513] | LLM의 설명문이 PII·비밀값을 재인용할 위험 | 종류·개수만 설명하도록 prompt 보완; 현재 master에도 문구 확인 | prompt 지시만으로 완전한 누출 차단이 증명되지는 않음 |
| [#1619][P1619], [#1965][P1965], [#5915][P5915] | 낡거나 취약점 관련 의존성 | 버전 갱신/불필요 의존성 제거 | dependency CVE가 곧 Akto에서 악용 가능하다는 의미는 아님 |

두 가지 **미해결 공개 제보**는 특히 별도로 봐야 한다.

- [이슈 #2673][I2673] / [PR #2674][P2674]: 로그인 JSP에 사용자 이름을 JavaScript 문자열로 삽입하는 XSS 가능성. 수정 PR은 open이고, 현재 master에도 직접 삽입 형태가 남아 있다. 입력 통제·실행 경로·정책까지 포함한 실제 공격 재현은 하지 않았으므로 “확정된 현재 운영 취약점”이 아닌 **소스와 일치하는 미해결 제보**로 기록한다.
- [PR #6569][P6569]: 역할 변경과 비밀번호 초기화 대상 조회에 account 범위·호출자 역할 제한 등을 보완하는 수정안. 조사 시점 open·미병합. patch가 제시한 위험은 중요하지만, 다른 interceptor까지 포함한 end-to-end 악용 가능성은 미검증이다.

[이슈 #6043][I6043]은 shaded/재포장된 의존성 때문에 일반 SBOM 검사에서 취약 라이브러리를 놓칠 수 있다는 연구자 제보다. 제보자도 exploitability는 조사하지 않았다고 명시한다. 별도 감사 없이 “Akto가 나열된 CVE에 모두 취약하다”고 옮기면 안 된다.

`#5473` Mongo 버전 문제와 `#5480` OpenAPI 3.1 import 문제는 closed 상태이지만, 닫힘과 재현 검증은 다르다. 특히 #5480의 짧은 해결 댓글만으로 모든 3.1 명세가 정상 동작한다고 결론내리지 않았다.

검사 규칙 저장소도 따로 확인했다. [tests-library #81](https://github.com/akto-api-security/tests-library/pull/81)과 [#85](https://github.com/akto-api-security/tests-library/pull/85)는 BOLA 오탐을 줄이기 위해 오류·계정 잠김 등의 영어 문구를 제외했고, [#86](https://github.com/akto-api-security/tests-library/pull/86)은 누락된 YAML 조건을 고쳤다. [#167](https://github.com/akto-api-security/tests-library/pull/167)은 일부 HTML 응답을 제외했다. 한편 [#208](https://github.com/akto-api-security/tests-library/pull/208)에서 추가한 PIIDataLeak 규칙은 [#214](https://github.com/akto-api-security/tests-library/pull/214)에서 삭제됐다. 삭제 이유는 확인되지 않았다. [#228](https://github.com/akto-api-security/tests-library/pull/228)은 ‘Bola templates updated’라는 제목이지만 실제로는 pro 브랜치의 실행시간 분류 변경이다. 제목만 보고 탐지 성능 개선이나 현재 사용 가능 기능으로 세면 안 된다.

## 6. BOLA 판정에서 남는 구조적 한계

현재 tests-library의 `BOLAByChangingAuthToken.yaml`은 대략 다음을 검사한다.

- 정상 샘플은 2xx, 비어 있지 않은 응답, private context가 있어야 한다.
- 인증 헤더를 바꾸어 재실행한다.
- 새 응답도 2xx이고 원래 응답과 90% 이상 일치하며, 특정 오류 문구를 포함하지 않으면 의심한다.

이는 실용적인 휴리스틱이지만 객체 소유권의 정답을 직접 아는 것은 아니다. 오류 문구 목록도 주로 영어이므로 “권한이 없습니다” 같은 한국어 업무 오류를 별도 시험해야 한다. [고정된 검사 템플릿][T1]

원본 `extractAllValuesFromPayload`와 `compareWithOriginalResponse`를 추출해 실행한 결과:

| 합성 입력 관계 | 비교 점수 | 의미 |
|---|---:|---|
| 같은 객체 | 100 | 기본 동작 |
| 2개 필드 중 id만 다름 | 50 | 필드별 동일 값 집합 비율 |
| 배열의 id와 label 연결만 서로 바뀜 | 100 | 배열 인덱스 대신 공통 경로와 값 집합을 쓰므로 객체 간 연결을 잃음 |
| 원래 객체가 그대로 있고 다른 객체가 추가됨 | 0 | 원래 데이터가 포함돼도 각 경로의 값 집합이 바뀌면 점수가 낮아질 수 있음 |
| 숫자 1과 문자열 "1" | 100 | 텍스트 값 변환으로 타입 차이를 보존하지 않음 |
| 공통 메타데이터 9개 + 서로 다른 id 1개 | 90 | 공개 메타데이터 비중이 판정을 지배할 수 있음 |

이 결과는 **해당 비교 함수의 실행 결과**다. 전후 API 선택, private context, 인증 성공 여부, 다른 검사 규칙을 합친 최종 Akto 결과는 실행하지 않았다.

또한 현재 `FilterAction.getPrivateResourceCount()`의 URL 경로에서 DB 조회 결과를 `new SingleTypeInfo()`로 덮어쓰는 코드가 있고, `getIsPrivate()`는 관측 수 0을 true로 취급한다. fallback과 privateCount 증가도 이어지므로 한 줄 삭제를 완전한 해결책으로 제시할 수 없다. **미관측·공개·비공개를 구분할 수 있는지 검증할 후보**다. [비교 함수][C1], [private context][C2], [관측 판정][C3]

AP-EYE에는 최소한 `요청자 → 요청 객체 → 응답 객체 → 소유자/권한 정책`을 연결하는 결과가 필요하다. 목록 API의 혼합 소유권, 공개 필드만 반환하는 정상 응답, 공유 객체, 관리자 권한, 인증 실패, 200을 반환하는 업무 오류, 캐시·페이지네이션도 정상/보류/BOLA 정답에 넣어야 한다.

## 7. Akto의 PII 탐지 경로를 정확히 나누기

### 7.1 기존 API 필드 분류

`KeyTypes.getSubtype`의 확인된 흐름은 활성 custom type 검사 → 카드번호 검증 → 숫자 타입 처리 → 내장 문자열 패턴 → JWT/전화번호/IP/VIN 등의 개별 검사다. 먼저 일치하는 custom type을 반환하므로 범용 규칙을 추가하면 다른 타입과 충돌할 수 있다. [타입 분류 코드][C4]

`RegexPredicate.validate`는 String 입력만 받고 Java 정규식의 `matches()`를 사용한다. 따라서 이메일 하나인 필드와 문장 속 이메일은 다르고, JSON 숫자 타입 값과 문자열 숫자도 다르다. `onKey`, `onKeyAndPayload`는 각각 필드 이름만 검사하거나 이름과 값을 함께 검사하는 데 사용된다. 타입, 민감 여부, 활성 여부, redacted 여부는 서로 별개다. [정규식 코드][C5], [타입 생성 코드][C6]

수집한 소스에는 외부 `pii-types/general.json` 규칙 81개, 본체 `fintech.json` 10개가 있다. general에는 비밀번호·계정명·토큰·주소 관련 영문 key와 서비스별 secret/URL 패턴이 많다. 이 숫자는 독립적인 개인정보 종류 91개나 활성 탐지기 91개를 의미하지 않는다. 중복·설정·내장 검증기가 섞여 있다. fintech의 10개 항목은 모두 JSON에 `active:false`, `sensitive:false`로 기재돼 있다. 생성 코드도 전달된 활성 상태를 사용하므로 실제 계정 설정을 확인해야 한다. [일반 규칙][D1], [국가별 규칙][D2]

### 7.2 Agent Guard의 Presidio anonymizer

현재 소스에서 별도 Python 서비스가 Presidio 2.2.364, spaCy 3.8.7을 사용한다. 기본 모델은 영어 `en_core_web_sm`, 분석기의 지원 언어도 영어만 등록한다. 입력에 language 필드가 있다는 사실만으로 한국어 처리가 활성화되지는 않는다.

검출 결과는 문자 시작/끝 위치와 score를 갖고 `[REDACTED]`로 치환한다. 임계값은 0.4이고, entities를 명시하지 않으면 DATE_TIME·NRP·LOCATION을 제외한다. 따라서 API 필드 분류와 문장 마스킹을 동일 성능으로 묶어 평가하면 안 된다. [서비스 코드][C7]

### 7.3 LLM·외부 검사기 경로

LLM scanner에는 prompt injection, 금지 주제, 유해성, 비밀번호 등의 경로가 있으며, 설명문 재인용 방지 수정이 있었다. 일부 risk/confidence는 A/B/C/D 판정에 대응하는 상수로 할당된다. 이는 경험적으로 보정된 정확도와 구별해야 한다. [LLM scanner][C8]

`#6121`은 LLM redaction 설정 UI·DTO와 외부 모듈 연결을 추가한다. `#6150` PII block 우선순위, `#6240` 이메일 탐지 수정의 본체 patch는 주로 Go 모듈 버전 변경이다. 따라서 해당 PR 제목만 보고 내부 알고리즘·전후 성능을 설명할 수 없다.

`#6278/#6279`의 외부 datatype corrector는 후보·HTTP 검사기·캐시·Kafka 등의 확장 지점을 제공하지만 feature 배포 브랜치 병합이다. 조사한 master의 기존 분류기에 그 구현이 있다고 가정하지 않는다. 한국어 확장의 후보 경로로 검토할 가치는 있다.

## 8. 다른 나라 PII는 실제로 어떻게 찾나

국가별 식별번호는 대체로 **형태 후보 찾기 → 정규화 → 유효 구조/검증 숫자 → 주변 문맥 → 정책 결정**의 조합이다. 이름·주소는 형식만으로 구별하기 어려워 언어별 NER, 사전, 모델이 추가된다. 검증 숫자를 통과해도 실제 발급·소유·허용된 공개를 증명하지는 않는다.

| 국가/유형 | 조사한 Akto 기존 규칙 | 비교 가능한 더 풍부한 방법 | AP-EYE에 주는 의미 |
|---|---|---|---|
| 미국 SSN | `3-2-4` 숫자 형태 | Presidio의 형식·문맥·invalid pattern 처리 | 하이픈 없는 값, 임의 숫자, field 의미를 구분 |
| 미국 Medicare | 오래된 HICN 형태 | 현재 MBI는 다른 11자리 영숫자 체계 | 규칙 이름이 있다고 최신 제도까지 지원하는 것은 아님 |
| 캐나다 SIN | 9자리 숫자 | Presidio의 문맥·형식·Luhn | 숫자 길이만 맞는 주문번호와 충돌 가능 |
| 영국 NINO | prefix 제한 + 숫자·문자 | 문맥 및 구분자 정규화 | 정상 공백 표기도 시험 |
| 핀란드 개인번호 | 날짜 모양 + 구분자 + 끝 문자 | 실제 날짜·세기 문자·검증 문자 | 제도 변경으로 새 문자가 추가되면 오래된 regex는 미탐 |
| 독일 보험번호 | 날짜 모양·문자·숫자 | 번호 종류별 checksum/문맥 검증 | 세금·보험·신분증을 한 숫자 규칙으로 합치면 안 됨 |
| 인도 PAN/UHID | 정해진 영숫자/숫자 길이 | PAN의 문맥, Aadhaar는 별도 checksum 등 | 서로 다른 식별체계를 같은 범주로 혼동 금지 |
| 일본 | ‘Japanese Social Insurance Number’라는 12자리 패턴 | Google의 JAPAN_INDIVIDUAL_NUMBER 등 별도 infoType | Akto 명칭을 법적 My Number 지원과 자동 등치하지 않음 |
| 유럽 IBAN | 제한적인 문자+숫자 형태 | 국가별 길이·알파벳 계좌 부분·mod-97 | checksum과 국가별 구조가 필요 |
| 한국 | 조사한 general/fintech에 전용 국가 규칙 없음 | Presidio 한국 recognizer, Google 한국 infoType, Azure ko | 기존 구현을 비교군으로 삼아 API 문맥에 맞게 평가 |

위 비교는 Akto [규칙 파일][D2], Presidio [지원 목록][R1] 및 [국가별 소스][R2], Google [infoType 목록][R3]에 근거한다. Presidio 문서의 설명에도 오기 가능성이 있어, 식별번호 법적 정의는 해당 국가의 공식 규격을 우선해야 한다. 예컨대 Medicare HICN→MBI 변화는 [CMS][R4], 핀란드 세기 문자 확대는 [핀란드 정부][R5]로 교차 확인했다.

### 직접 실행한 규칙 진단 결과

국가별 전화번호는 libphonenumber 8.12.41이 제공하는 예시 번호로 만들었다. 미국·영국·프랑스·독일·핀란드·인도·일본·캐나다·한국 각 1개 예시를 네 형식으로 표현했다.

| 표현 형식 | 원본 Akto isPhoneNumber가 인식한 예시 |
|---|---:|
| E.164 국제번호 (`+국가코드…`) | 9 / 9 |
| 해당 국가 국내 형식 | 0 / 9 |
| 공백을 포함한 국제 표시 형식 | 8 / 9 |
| 국내 형식에서 숫자만 남김 | 0 / 9 |

원인은 기본 region으로 실제 국가 코드 대신 `UNSPECIFIED` 이름을 전달하고, 입력 길이도 8~16자로 제한하는 로직과 관련된다. 한국만의 문제가 아니다. **이 표는 36개 선택 입력의 결과이며 “국내번호 recall 0%”라는 모집단 성능 주장이 아니다.**

정규식 27개 입력에서는 다음을 확인했다.

- 기본 이메일 규칙은 긴 TLD `.technology`와 문장 속 이메일을 인식하지 못했다.
- 미국 SSN의 전부 0 형태, 캐나다 SIN의 전부 0/잘못된 Luhn 형태가 정규식을 통과했다.
- 핀란드·독일 번호의 존재할 수 없는 2월 날짜가 형태 검사를 통과했다.
- 영국 NINO의 공백 표기, 일본 12자리 번호의 하이픈 표기는 해당 규칙에 일치하지 않았다.
- 영문 bank code를 가진 공개 IBAN 예시는 미탐했고, 독일 예시의 검증 숫자를 틀리게 바꾼 값은 통과했다.
- 핀란드 새 세기 문자 B를 사용한 형태는 거절됐다. 이 입력 자체의 checksum 유효성까지 주장하지 않는다.

국가 규칙의 active/sensitive 상태와 전체 classifier의 우선순위를 적용하지 않은 **규칙 단독 결과**다. 전체 Akto에서 같은 입력이 어떤 최종 타입으로 저장되는지는 별도 실행 대상이다. 공유 가능한 입력·결과는 [PII 컴포넌트 결과](probe-evidence/results.json)에 있고, 원본 함수 추출 스크립트·JAR·의존성은 아래 §14에 명시한 로컬 조사 폴더에만 있다.

## 9. 제품별 한국어 지원 비교

| 제품/경로 | 방법 | 한국 관련 지원 근거 | 정확도 근거/한계 |
|---|---|---|---|
| Akto 기존 인벤토리 | key/value regex, libphonenumber·카드 등 전용 검사 | 커스텀 규칙으로 확장 가능 | 국가별 공개 P/R/F1 표 미확인 |
| Akto Agent Guard anonymizer | Presidio + spaCy | 현재 코드 설정은 en만 | 한국어 배포·측정 NOT_RUN |
| 최신 Presidio | regex + 문맥 + checksum + 교체 가능한 NER | KR_RRN/FRN/PASSPORT/DRIVER_LICENSE/BRN 소스 존재 | 지원 언어·recognizer 등록·NER 모델을 맞춰야 함. 하나의 보편 정확도 없음 |
| Google Sensitive Data Protection | infoType별 신호·검증·문맥, custom regex/사전/규칙 | RRN, ARN, 여권, 면허, NHI, BRN 등 | 한국 번호 지원과 한국어 모든 이름·주소 성능은 별개. 국가별 공통 평가표 미확인 |
| Azure Language Text PII | 학습 기반 엔터티 추출·분류·마스킹 | Text PII 언어표에 ko | Conversation PII의 언어 범위와 혼동 금지. ko 지원은 모든 엔터티의 동일 품질 보장 아님 |
| AWS Comprehend PII | 관리형 모델, span·타입·score·마스킹 | 공식 PII 문서는 영어·스페인어 | 일반 Comprehend의 언어 지원을 한국어 PII 지원으로 확대 해석 금지 |
| ko-pii | 한국 규칙·사전·checksum | 국내 식별번호와 일부 속성 | 개발자 자체 benchmark. 조건·지표·최신 비교군 구성을 확인해야 함 |
| GLiNER 계열 등 | label 조건부 span 모델 | 다국어 모델마다 학습 언어가 다름 | ‘multilingual’ 이름만으로 한국어 검증을 대체할 수 없음 |

근거: [Presidio][R1], [Google][R3], [Azure 언어표][R6], [AWS PII][R7], [ko-pii benchmark][R8]. 클라우드 비교 실행은 하지 않았고 비용도 발생시키지 않았다.

## 10. 정확도는 어느 정도인가: 숫자를 읽는 방법

PII가 없는 글자가 훨씬 많기 때문에 전체 문자 accuracy는 거의 아무것도 찾지 않아도 높아질 수 있다. 최소한 다음을 함께 보고해야 한다.

- precision: PII라고 표시한 것 중 정답 비율.
- recall: 실제 PII 중 찾아낸 비율. 마스킹의 누락과 직접 관련된다.
- F1: 둘의 조화평균. 엔터티 유형별 결과와 함께 봐야 한다.
- span 기준: 문자의 정확한 시작/끝까지 맞춰야 하는지, 일부 겹쳐도 맞다고 하는지.
- 서비스 기준: DB·로그·보고서·내보내기까지 원문이 남지 않았는지.

`score=0.95`, `VERY_LIKELY`, BOLA 일치율 90, severity CRITICAL은 서로 다른 의미다. 어느 것도 곧바로 “검사기 정확도 95%/90%”가 아니다. [Google likelihood][R9], [Presidio 평가 설명][R10], [AWS service card][R11]

### 비교 가능한 공개 수치와 비교하면 안 되는 수치

아래 각 표 **내부**의 조건만 비교해야 한다. 표들 사이의 점수를 합쳐 제품 순위를 만들면 안 된다.

**SPY 원 논문, 표 3, 인쇄 p.240 — 저자 보고, 우리 재실행 아님.** 합성 의료/법률 문서에서 Presidio와 Llama-3-70B zero-shot, 반대 도메인으로 학습·평가한 DeBERTa를 비교했다.

| 의료 문서의 엔터티 F1 | Presidio | Llama-3-70B | DeBERTa |
|---|---:|---:|---:|
| 이름 | 28.2 | 67.6 | 87.8 |
| 이메일 | 53.4 | 91.8 | 98.5 |
| 전화번호 | 47.6 | 89.9 | 95.0 |

이는 국가별 식별번호의 정확도표가 아니다. 공개 인물·공공 연락처 등 비민감 문맥과 PII를 구분하는 정의가 성능에 영향을 준다. 학습 조건도 다르다. 저자들은 실제 데이터 전이 검증이 부족하고 연구 외 사용을 권하지 않는 한계를 적었다. [SPY 원문][B1] — 읽기 수준: 2차, §1·3·5·6·7 및 Limitations.

**GLiNER2-PII, 표 2 — 저자 보고 exact type+span F1.** SPY 법률 100문서, 의료 100문서에 대한 별도 설정이다.

| 모델 | 법률 F1 | 의료 F1 | 평균 F1 |
|---|---:|---:|---:|
| NVIDIA GLiNER-PII | 0.401 | 0.381 | 0.391 |
| urchade/gliner_multi_pii-v1 | 0.388 | 0.381 | 0.384 |
| OpenAI privacy-filter | 0.360 | 0.386 | 0.373 |
| knowledgator/gliner-pii-base-v1.0 | 0.385 | 0.350 | 0.368 |
| fastino/gliner2-PII | 0.475 | 0.467 | 0.471 |

학습용 4,910개 문서는 합성이며 영어·프랑스어·스페인어·독일어·이탈리아어·포르투갈어·네덜란드어 등이 명시돼 있다. 한국어 성능 증거가 아니다. 논문이 SPY를 자연 문서처럼 설명하는 부분은 원 SPY의 합성 데이터 설명과 구분해서 읽어야 한다. [원문][B2] — 읽기 수준: 2차, §1–6. 두 SPY 표는 샘플·학습·채점이 달라 직접 순위 비교하지 않는다.

**ko-pii 개발자 공개 평가 — 독립 검증 아님.**

| 해당 평가 설정 | ko-pii | Presidio kr_adapt | privacy-filter |
|---|---:|---:|---:|
| KDPII v1.1, 대화 4,891문서, F1 | 0.660 | 0.273 | 0.264 |
| 자체 합성 행정/서식 540문서, F1 | 0.790 | 0.483 | 0.451 |

이 평가는 위치를 무시하는 substring 집합 매칭이며 1~2글자 PERSON을 제외한다. 최신 Presidio 기본 recognizer 전체와 동일한 구성이라고 확인되지 않았다. KDPII 표의 TP+FN도 ko-pii/privacy-filter는 1,302, Presidio는 1,305로 차이가 있어 gold mapping을 재확인해야 한다. 보고된 ko-pii의 PERSON F1 0.135, ADDRESS 0.241은 자유로운 이름·주소가 여전히 어렵다는 신호다. **0.660을 “한국어 개인정보 66% 정확도”라고 일반화하지 않는다.** [benchmark][R8]

추가 발견한 cross-lingual arXiv 평가는 HTML v1의 42-benchmark 설명과 수집한 최신 PDF의 32-benchmark 설명을 먼저 대조해야 하므로 핵심 순위 근거에서 제외했다. 자세한 읽기 기록은 `PAPER-NOTES.ko.md`에 있다.

## 11. 한국어 PII에는 무엇을 구현해야 하나

### 11.1 식별번호와 자유 문장을 나눈다

| 영역 | 우선 구현할 내용 | 대표 실패 입력 |
|---|---|---|
| 국내 전화번호 | KR locale, +82/010/02 등 형식, 구분자 정규화 | 숫자만 있음, 공백/괄호, JSON 숫자형, 다른 나라 번호와 혼합 |
| 주민/외국인 등록번호 | 형태·생년월일·문맥, 구형/신형 규칙 구분 | 주문번호와 같은 자릿수, 부분 마스킹, 오래된 checksum 강제 |
| 여권/면허 | 현행·구형 형식 및 명칭 문맥 | 띄어쓰기, 영문/숫자 혼동, 다른 ID와 충돌 |
| 카드/계좌 | 카드 검증과 은행별 계좌 후보·문맥 | 주문번호, 상품코드, 테스트 카드, 은행명 없는 숫자 |
| 이름/주소 | 한국어 NER + 조사/경계 처리 + 문맥 | ‘김…님’, 두 글자 이름, 외국인 이름, 도로명·지번·상세주소 |
| 일반 PII/secret | 이메일/IP/토큰과 한국어 key 동의어 | `연락처`, `수령인`, `주소`, 영문 camelCase, 문장 속 값 |

주민번호의 오래된 checksum만으로 실패 값을 무조건 제외하면 안 된다. 현행 Presidio KR_RRN도 과거 구조·checksum이 맞으면 true를 주지만, 그 검증이 실패한 경우에는 새 번호 체계를 고려해 None을 반환한다. 그 설계와 [행정안전부의 부여체계 변경 설명][R12]을 참고하되, 실제 구현은 공식 규격을 버전별로 고정한다. checksum은 실재 인물 조회나 신원 확인 기능이 아니다.

사업자등록번호·법인 정보·건강 관련 문구도 탐지 후보가 될 수 있지만, 개인정보/민감정보 여부는 주체와 맥락에 따라 다르다. `type`, `sensitive`, `redact`, `authorization_violation`을 각각 표현해야 한다.

### 11.2 추천 구조

```text
원본 HTTP/JSON
 → 파싱·위치 기록
 → locale/필드 이름 문맥
 → 구조화 식별번호 규칙 + 유효성 검사
 → 자유문장 NER 보완
 → 중첩·충돌 정리 + 근거·신뢰도
 → 정책: 탐지만 / 마스킹 / 검토
 → 원문 위치 기준 치환
 → 저장·로그·보고서·export 재검사
```

정규화 과정에서 원문의 byte/문자 위치가 달라지므로 offset mapping을 보존해야 한다. Python의 문자 인덱스와 JavaScript UTF-16 인덱스 차이, 한글 조합형, emoji를 회귀 사례에 넣는다. 마스킹 후 JSON이 깨지거나 문자열 숫자의 앞자리 0이 사라지는지도 검사한다.

구현 선택은 두 갈래다. 기존 인벤토리의 한국어 구조화 필드는 custom type/Java 검증기로 확장하고, 문장형 PII는 Akto anonymizer 또는 별도 Presidio adapter에 한국어 recognizer·NER를 등록한다. 처음부터 대형 LLM 호출을 필수 경로로 만들 필요는 없다. 입력을 외부 모델로 보낼 경우에는 탐지 전에 원문이 나간다는 데이터 흐름과 비용·지연도 설계에 포함해야 한다.

## 12. 공정한 AP-EYE 비교 실험 설계

이 절은 **제안이며 아직 실행하지 않은 계획**이다.

**비교군**은 ① 고정 commit Akto 기본, ② Akto+한국 규칙, ③ 현재 한국 recognizer를 실제 등록한 Presidio, ④ Presidio+한국어 NER, ⑤ 필요 시 한국어 지원을 확인한 span 모델이다. 클라우드 비교군은 같은 합성 입력과 같은 엔터티 범위를 사용한다.

**데이터**는 다음 세 층을 사용한다.

1. 규격 경계 테스트: 정상/비정상 날짜, 체크값, 구분자, 언어 혼합, 부분 마스킹. 이번 63개는 시작점이지 충분한 평가셋이 아니다.
2. 한국어 문장 benchmark: [K-PII-Bench][B3]의 공개 카드에는 30만 합성 문서·18유형·12도메인, template skeleton이 겹치지 않는 split이 명시된다. test_track_a 28,142건, dev 28,147건, train 243,711건. 카드·schema만 확인했으며 데이터 전수 검증이나 논문 성능 재현은 하지 않았다. KDPII도 라이선스와 실제 annotation을 확인한 뒤 활용한다.
3. API 전용 benchmark: path/query/header/cookie/body, 중첩 JSON·배열·GraphQL·한글 오류, 목록 API, 여러 소유자가 섞인 응답. 합성 또는 사용 권한이 확보된 데이터로 만들고 두 명의 판정과 불일치 조정 기록을 남긴다.

**데이터 누수 방지**는 문자열만 다르게 바꾼 같은 문장을 train/test에 섞지 않는 것이다. template, API endpoint, 문서 계열, 인물·조직별로 나누고 test를 본 뒤 정규식·threshold를 조정하지 않는다. 한국어 두 글자 이름이나 띄어쓰기 오류를 임의로 빼면 안 된다.

**채점표**에는 다음이 필요하다.

| 축 | 반드시 기록할 결과 |
|---|---|
| 엔터티 | 타입별 TP/FP/FN·P/R/F1, 표본 수, bootstrap CI |
| 경계 | exact span을 주 지표로, overlap은 별도 보조 지표 |
| 지원 범위 | 모든 요구 타입 점수와 비교군 공통 타입 점수를 분리 |
| 불균형 | micro/macro 결과 및 고위험 식별번호의 recall |
| 위치 | query/header/cookie/body별 오류, 문자열/숫자 타입별 오류 |
| 실제 마스킹 | 남은 원문 PII, 과잉 마스킹, JSON 파손, export/log 누출 |
| 성능/비용 | 동일 하드웨어·입력 길이·batch에서 p50/p95 latency, 처리량, 비용 |
| 판정 설명 | regex/검증/문맥/모델 중 어떤 근거로 잡았는지 |
| BOLA 연계 | 민감정보 존재와 비인가 타인 정보 노출을 분리한 confusion matrix |

성능 목표값은 baseline과 실패 비용을 본 후 정한다. 문헌의 98%를 우리 시스템의 목표 달성 증거로 쓰지 않는다.

## 13. AP-EYE에서 지금 할 일을 우선순위로 바꾸면

아래 순서는 이 보고서의 Akto·PII 탐색을 [최신 프로젝트 방향·평가 결정](../../research/evaluation-datasets-2026-10-06/README.md)에 맞춰 재배열한 것이다. **읽기 BOLA가 연구 본체이며 한국어 PII는 별도 확장**이다. PII 성공 여부를 인가 위반 판정의 필요조건으로 두지 않는다.

| 순서 | 구체적 작업 | 완료라고 부를 수 있는 산출물 |
|---|---|---|
| 1 | 읽기 BOLA의 외부 정답과 정상 정책을 고정 | AuthProbe·VAmPI 기능 회귀, wger 취약·수정 및 공개 정상 실행 패키지와 정책 gold |
| 2 | 실제 사용할 Akto branch·image digest·검사 템플릿 버전을 고정하고 원본 전체 검사를 실행 | 수집→선택→실행→응답→판정/skip이 연결된 기준선 |
| 3 | Test Role/YAML 설정 보정판과 같은 권한 근거를 받는 단순 규칙을 비교 | 기존 설정만으로 해결되는지, 제안 판정 자체의 이득인지 분리 |
| 4 | 확인된 읽기 BOLA 실패가 있으면 객체별 권한 근거와 반환 내용을 대응시키는 작은 개선을 검증 | 외부 사례의 재현 시험, 정상 오탐·보류·입력 비용 및 기존 동작 회귀 |
| 5 | **별도 확장:** 한국어 PII 유형·필드/문자 위치·마스킹 정책과 외부 자료를 고정 | ko-pii/K-PII-Bench 품질 감사, 정상 문서·반복 출현을 포함한 라벨 계약 |
| 6 | 한국어 규칙·Presidio recognizer·필요한 NER를 동일 자료에서 비교 | 유형별 P/R/F1, exact 문자 span F1, 빈 문서 오탐·과잉 마스킹 |
| 7 | 재현 가능한 작은 upstream 기여를 준비 | 읽기 BOLA 수정 또는 한국어 locale 개선 각각의 문제·원인·변경·회귀 시험 |

upstream 기여는 국내 전화번호 locale, 한국 규칙·회귀 fixture, 마스킹 적용 범위 문서, 비교기의 객체 연결 검증처럼 작고 검증 가능한 단위가 적합하다. 장기 fork는 UI 접근성·상용 모듈 의존·수정 수용 여부를 확인한 다음 판단한다. 급하게 전체 제품을 fork하면 릴리스 브랜치·동기화·모델·정책 변경을 팀이 계속 따라가야 한다.

## 14. 남은 불확실성과 재현 방법

이번 조사로 확인한 것은 공개 소스와 이력, 그리고 격리된 컴포넌트 동작이다. 다음은 아직 확인되지 않았다.

- 선택한 OSS Docker 이미지에서의 실제 UI 접근·전체 검사·한국어 데이터 저장/마스킹.
- 공개 제보 #2673/#6569의 전체 권한 경로와 실제 공격 가능성.
- Akto의 상용 PII 모델과 외부 Go 모듈 내부의 모든 변경 및 성능.
- 비교 제품을 동일 한국 API 데이터셋으로 실행한 precision/recall/F1.
- 운영 데이터의 분포·라벨 품질·성능 및 비용.
- 6,402개 PR 전체에 대한 줄 단위 보안 감사. 전체 목록 확보와 핵심 변경 검토를 구별한다.

원래 조사 PC의 **`C:\Users\andyw\Desktop\AP-EYE` 루트**에서 다음 명령으로 컴포넌트를 재현했다. Python 3.12, JDK 21이 사용됐고 전화번호 라이브러리는 Akto가 고정한 8.12.41을 사용했다. 스크립트는 이 Git 공유 폴더가 아닌 `local-materials/akto-research-2026-10-06/scripts/`에 있고, 고정 Akto 소스 checkout과 JAR도 그 로컬 폴더에만 있다. 스크립트는 JDK 경로를 당시 Windows 설치 경로로 지정하므로 다른 PC에서는 경로 수정이 필요하다. 공용 Maven artifact를 필요할 때 다운로드하며 실제 API나 개인정보 서비스로 시험 데이터를 보내지 않는다.

```powershell
python 'local-materials/akto-research-2026-10-06/scripts/component_probe.py'
python 'local-materials/akto-research-2026-10-06/scripts/bola_probe.py'
```

원본 source commit과 최초 조사 파일 hash는 [원래 조사 manifest](EVIDENCE-MANIFEST.json)에, 현재 공유본 파일 hash는 [공유본 manifest](SHARED-COPY-MANIFEST.json)에 있다. 이 Git 공유본의 실험별 입력·결과는 [PII 컴포넌트 결과](probe-evidence/results.json)와 [BOLA 비교 결과](probe-evidence/bola-results.json)에 있다. 스크립트·원본 소스·JAR가 없는 Git 공유본만으로는 재실행할 수 없으며 위 로컬 조사 폴더 또는 같은 commit의 새 checkout이 필요하다. 상세 이력은 [수정 이력](HISTORY-REVIEW.ko.md), 문헌 검토는 [문헌 기록](PAPER-NOTES.ko.md), 검색 가능한 전체 목록은 [이슈·PR 검색](ISSUE-EXPLORER.html)에서 읽을 수 있다.

## 출처

[A1]: https://github.com/akto-api-security/akto/tree/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d
[A2]: https://docs.akto.io/
[A3]: https://www.akto.io/
[A4]: https://www.akto.io/pricing
[A5]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/LICENSE.md
[A6]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/CONTRIBUTING.md
[C1]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/libs/utils/src/main/java/com/akto/testing/Utils.java#L381
[C2]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/libs/utils/src/main/java/com/akto/test_editor/filter/FilterAction.java#L1464
[C3]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/libs/dao/src/main/java/com/akto/dto/type/SingleTypeInfo.java#L956
[C4]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/libs/dao/src/main/java/com/akto/dto/type/KeyTypes.java
[C5]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/libs/dao/src/main/java/com/akto/dto/data_types/RegexPredicate.java
[C6]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/apps/dashboard/src/main/java/com/akto/listener/InitializerListener.java#L766
[C7]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/apps/agent-guard/python-service/anonymizer-container/src/anonymizer_service.py
[C8]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/apps/agent-guard/python-service/worker-py/src/llm_scanner.py
[D1]: https://github.com/akto-api-security/pii-types/blob/830439223637a1d3a2756b2a4dfe7ff7fd8101d8/general.json
[D2]: https://github.com/akto-api-security/akto/blob/42e88a247fb2a0532ec8d7a8ba6261b794ee3f8d/pii-types/fintech.json
[T1]: https://github.com/akto-api-security/tests-library/blob/ce2267da7e28927876b41d944e63bdde10e41e00/Broken-Object-Level-Authorization/BOLAByChangingAuthToken.yaml
[R1]: https://presidio.dataprivacystack.org/supported_entities/
[R2]: https://github.com/data-privacy-stack/presidio/tree/d8847904621733f4eaad4f9bd977b96a11325c90/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific
[R3]: https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
[R4]: https://bluebutton.cms.gov/data-dictionary/bene-mbi-id/
[R5]: https://valtioneuvosto.fi/-/10623/henkilotunnusten-riittavyys-varmistetaan-uusilla-valimerkeilla?languageId=en_US
[R6]: https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/language-support
[R7]: https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html
[R8]: https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/docs/BENCHMARK.md
[R9]: https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
[R10]: https://presidio.dataprivacystack.org/evaluation/
[R11]: https://docs.aws.amazon.com/ai/responsible-ai/comprehend-detectpii/overview.html
[R12]: https://mois.go.kr/plan2020/download/2020plan.pdf
[B1]: https://aclanthology.org/2025.naacl-srw.23.pdf
[B2]: https://arxiv.org/pdf/2605.09973v1
[B3]: https://huggingface.co/datasets/woohyun212/k-pii-bench
[I2673]: https://github.com/akto-api-security/akto/issues/2673
[I5512]: https://github.com/akto-api-security/akto/issues/5512
[I6043]: https://github.com/akto-api-security/akto/issues/6043
[P527]: https://github.com/akto-api-security/akto/pull/527
[P883]: https://github.com/akto-api-security/akto/pull/883
[P1121]: https://github.com/akto-api-security/akto/pull/1121
[P1231]: https://github.com/akto-api-security/akto/pull/1231
[P1248]: https://github.com/akto-api-security/akto/pull/1248
[P1249]: https://github.com/akto-api-security/akto/pull/1249
[P1359]: https://github.com/akto-api-security/akto/pull/1359
[P1363]: https://github.com/akto-api-security/akto/pull/1363
[P1491]: https://github.com/akto-api-security/akto/pull/1491
[P1492]: https://github.com/akto-api-security/akto/pull/1492
[P1619]: https://github.com/akto-api-security/akto/pull/1619
[P1965]: https://github.com/akto-api-security/akto/pull/1965
[P2418]: https://github.com/akto-api-security/akto/pull/2418
[P2674]: https://github.com/akto-api-security/akto/pull/2674
[P2908]: https://github.com/akto-api-security/akto/pull/2908
[P3055]: https://github.com/akto-api-security/akto/pull/3055
[P3497]: https://github.com/akto-api-security/akto/pull/3497
[P5498]: https://github.com/akto-api-security/akto/pull/5498
[P5519]: https://github.com/akto-api-security/akto/pull/5519
[P5863]: https://github.com/akto-api-security/akto/pull/5863
[P5881]: https://github.com/akto-api-security/akto/pull/5881
[P5902]: https://github.com/akto-api-security/akto/pull/5902
[P5915]: https://github.com/akto-api-security/akto/pull/5915
[P6112]: https://github.com/akto-api-security/akto/pull/6112
[P6121]: https://github.com/akto-api-security/akto/pull/6121
[P6150]: https://github.com/akto-api-security/akto/pull/6150
[P6240]: https://github.com/akto-api-security/akto/pull/6240
[P6309]: https://github.com/akto-api-security/akto/pull/6309
[P6402]: https://github.com/akto-api-security/akto/pull/6402
[P6487]: https://github.com/akto-api-security/akto/pull/6487
[P6513]: https://github.com/akto-api-security/akto/pull/6513
[P6569]: https://github.com/akto-api-security/akto/pull/6569
