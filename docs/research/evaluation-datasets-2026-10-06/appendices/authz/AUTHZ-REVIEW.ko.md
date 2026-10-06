# 인가 외부 기준선 독립 재검토

조사일 2026-10-06. 기존 태스크 2·4를 보강하기 위한 원문·공개 코드 감사다. **새 서비스 취약점 탐색이나 외부 스캔은 실행하지 않았다.** 로컬에 있던 원문 6편을 먼저 1차 읽기한 뒤, 채택 후보의 평가 절과 공개 자산을 2차 확인했다. 감사 후속 작업으로 [wger 공식 이미지 2.4/2.5의 취약·수정 GET 재현](real-app/WGER-PAIRED-REPRO.ko.md)과 [2.7의 공개 정상 원본 테스트](real-app/public-normal/README.ko.md)를 추가했다. `p.`는 로컬 PDF의 1부터 시작하는 페이지 번호다.

## 먼저 바꿀 결론

AuthProbe와 VAmPI는 유용한 기능 점검 대상이지만, 둘만으로 프로젝트의 일반화나 논문 기여를 평가하기에는 약하다. 다음 구성이 더 강하다.

- **비교 도구:** Akto 고정판을 주 비교군, RESTler의 NameSpaceRuleChecker를 추가 비교군, AuthProbe를 작은 외부 회귀 기준선으로 둔다. 도구와 평가 대상 API를 별도 표로 관리한다.
- **실제 읽기 대상:** BACScan의 Memos/Lunary 후보에 더해, **wger의 공개 CVE 2개·GET 경로 5개와 비소유자 공개 조회 정상 사례**를 확보했다. 공지→취약 source→수정 diff를 연결하고, 이 중 영양 계획 1경로와 목록 2경로는 공식 이미지의 취약·수정 응답까지 확인했다. 공개 정상 template은 다른 2.7 snapshot의 원본 maintainer 테스트를 8/8 통과시켰다.
- **넓은 후보:** BolaZ의 SELECT 8개 사례는 후속 후보지만, 정확한 대상 commit/정답 데이터 패키지 확보가 부족하므로 현재 실험 목록에 8개를 곧바로 더하지 않는다.
- **정답의 독립성:** 판정에 쓰는 추정 소유권/목록과 정답 생성에 쓰는 근거를 분리한다. 권한 정책·maintainer test·수정 diff·실제 반환 객체를 이용해 정답을 고정해야 한다.
- **독립 사례 수:** AuthProbe에서 객체 6개를 발견한 것은 독립적인 취약점 6개를 발견한 것과 다르다. 요청/객체 단위 지표와 endpoint·CVE family·애플리케이션 단위 지표를 함께 낸다.

## A. RESTler — 추가해야 할 공개 비교 도구

**Vaggelis Atlidakis, Patrice Godefroid, Marina Polishchuk. Checking Security Properties of Cloud Service REST APIs. ICST 2020.** [저자 PDF](https://patricegodefroid.github.io/public_psfiles/icst2020.pdf) · [공식 출판 소개](https://www.microsoft.com/en-us/research/?p=568212) · [코드](https://github.com/microsoft/restler-fuzzer)

- 읽기 수준: **2차**, §I·III.A/B·IV.A–C·V·VII, 특히 PDF pp.3–4,7–10. 추출기가 결론 경계를 놓쳐 p.10 전체를 별도 읽었다.
- 한 것: OpenAPI 기반 stateful fuzzing에 namespace·resource hierarchy 등 4가지 보안 규칙을 추가했다. 사용자를 교체하거나 부모 객체를 바꾸어 자원 접근 경계를 검사한다.
- 안 한 것: 정상 공유·공개 자원에 맞춘 보편적 권한 추론이나 공개 정상/BOLA 분류 데이터셋 제공은 아니다. §IV.A p.7은 서비스 이름을 “whose names are anonymized”라고 설명한다. 한국어: 대상 서비스 이름은 익명화되어 있다.
- 실제 대상: Azure A 13개 request type, Azure B 19개, Office365 C 18개. 각 1시간, BFS/BFS-Cheap/BFS-Fast 및 checker 최적화 비교. 공개 Swagger를 썼지만 대상 이름과 취약 시점 재현 배포는 제공하지 않는다.
- 정답/결과: §IV/Table II의 측정 단위는 bug bucket. 세 서비스의 NameSpace 열은 0이며, 전체 7개 bug 중 namespace 위반 발견 수로 오해하면 안 된다. 정상/BOLA의 완전한 TP/FP/FN/TN 데이터가 아니다.
- 판정: **도구는 살림, 논문 서비스 데이터셋 재현은 보류.** AuthProbe만 비교하는 것보다 공개되고 오래 사용된 동일 계열 기술을 포함할 수 있다.

현재 공식 [Checkers.md](https://github.com/microsoft/restler-fuzzer/blob/6d984deedbc54aad957fa3da0c7e9e5df23a2aee/docs/user-guide/Checkers.md)는 NameSpaceRuleChecker가 **기본 OFF**이며 별도 사용자로 replay한다고 명시한다. 객체 소비 dependency 외에 `trigger_objects` 문자열로 추가 요청을 지정할 수 있다. 이를 켜지 않고 결과가 없다고 평가하면 잘못된 비교다. ResourceHierarchyChecker는 부모/자식 객체 두 개 이상을 소비하는 요청에 적용된다. 우리 범위에서는 평가 대상 operation을 읽기로 제한하고 준비 단계의 생성/reset 비용은 별도 기록해야 한다.

### 이번 코드 실행: 10개 구성요소 입력

고정 commit `6d984deedbc54aad957fa3da0c7e9e5df23a2aee`의 `_rule_violation`과 `_false_alarm` 메서드를 AST로 그대로 추출하여, 실제 네트워크 없이 합성 응답에 실행했다. 메서드를 다시 구현한 것이 아니다. 스크립트 `restler-oracle-probe.py`, 결과 `evidence/restler-oracle-component-probe.json`.

| 합성 GET 응답 | 메서드 결과 | 해석 |
|---|---|---|
| 200 + 정확히 `[]` | violation 아님 | 별도 예외 처리 |
| 200 + `[ ]`, 줄바꿈 빈 배열, `{"results":[],"count":0}` | violation | JSON 의미보다 문자열 표현에 의존 |
| 200 + 정상 자기 객체 목록 / 공개 객체 목록 | violation | 원본 가정 밖 정상 접근의 구별 근거가 부족 |
| 200 + 비인가 비공개 객체 | violation | 준비한 양성 입력 |
| 403, 404 | violation 아님 | 정상 차단 입력 |
| 500 | violation | 일반 서버 오류도 bug 경로에 포함되므로 BOLA TP로 집계 금지 |

**범위:** 이 결과는 RESTler 전체 스캔, 도구 전체 정확도, 실제 서비스 FPR이 아니다. 해당 checker가 실제로 그 요청에서 trigger되는지도 E2E에서 검증해야 한다. 다만 JSON 구조·객체 관계 기반 판정이 필요한 이유를 공개 원본 코드로 보인다. [namespace 원본](https://github.com/microsoft/restler-fuzzer/blob/6d984deedbc54aad957fa3da0c7e9e5df23a2aee/restler/checkers/namespace_rule_checker.py#L227) · [공통 판정](https://github.com/microsoft/restler-fuzzer/blob/6d984deedbc54aad957fa3da0c7e9e5df23a2aee/restler/checkers/checker_base.py#L153)

## B. wger — 실제 읽기와 정상 공유를 함께 갖춘 강한 추가 후보

wger는 운동·영양 관리 애플리케이션이다. 인가 정보 유출의 대상이 반드시 이메일/주민번호일 필요는 없다. 영양 섭취와 운동 구성도 특정 사용자에 속한 비공개 객체일 수 있으므로, **PII가 검출되지 않았다는 이유로 BOLA를 정상으로 만들면 안 된다.**

| 사례 family | 외부 근거와 정확한 버전 | 읽기 경로 / 기대 정답 | 확보 상태 |
|---|---|---|---|
| CVE-2026-27839: raw ORM 우회 | [공식 GHSA](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86), 취약 parent `a912c313b8fec21469ff47e6f51a1040d03c92e8`, [fix `29876a1`](https://github.com/wger-project/wger/commit/29876a1954fe959e4b58ef070170e81703dab60e) | `GET /api/v2/nutritionplan/{pk}/nutritional_values/`, `meal/{pk}/nutritional_values/`, `mealitem/{pk}/nutritional_values/`. 자기 객체는 허용, 타인 비공개 객체는 반환 금지 | 공식 공지·취약 원본 3개 lookup·수정 diff 확인. **공식 2.4/2.5 이미지에서 nutritionplan 자기/교차 8요청 실행**. 나머지 2경로 미실행 |
| CVE-2026-27835: 목록 범위 누락 | [공식 GHSA](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm), 취약 parent `0aae00b8db0e6611e5c641dcdf6daee30bb8043b`, [실제 fix `035a661`](https://github.com/wger-project/wger/commit/035a66161dcbdbac8bbd03adbc1bdb071f233274) | `GET /api/v2/repetitions-config/`, `GET /api/v2/max-repetitions-config/`. 자기 객체만 목록에 포함, 타인 객체 섞임은 BOLA | 두 `.all()`을 `slot_entry__slot__day__routine__user` 조건으로 고친 diff 확인. **공식 2.4/2.5 이미지에서 두 경로·두 계정 8요청 실행** |
| 비소유자의 공개 routine template 조회 | [정상 동작 수정 및 테스트 `3515e61`](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9), 2026-08-26 | `public-templates-list`에서 발견한 비소유자 template의 detail GET은 200, 같은 ID 유지. `templates-detail` 자기 template도 200 | maintainer 추가 테스트가 비소유자임을 assert한 뒤 200을 확인. 공식 **2.7 이미지에서 해당 원본 테스트 포함 8/8 실행·통과**. [로그·digest](real-app/public-normal/README.ko.md) |

첫 CVE는 세 endpoint를 갖지만 **1개의 CVE/공통 원인 family**다. 두 번째는 두 endpoint지만 1 family다. 따라서 ‘5개 독립 취약점’으로 수를 부풀리지 않는다. 공개 template 정상 사례는 더 나중 시점의 별도 snapshot이며, 취약 버전과 같은 commit에서 동시에 검증했다고 말하면 안 된다.

### 공개 자산 검증 중 발견한 불일치

1. CVE-2026-27835의 GitHub global advisory JSON references에는 `1fda5690b35706bb137850c8a084ec6a13317b64`가 연결되어 있다. 실제 diff는 measurement category 저장의 소유권 및 Routine 관계 이름 변경이며, 두 repetition 목록의 `.all()` 수정이 아니다. 저장소 history에서 **실제 fix `035a661...`를 추가 확인**했다. 공지 링크가 있다고 diff 확인을 생략하면 잘못된 기준선을 만들 수 있다.
2. IDOR-GUARD 공개 저장소는 wger를 `a912c313...`로 고정하면서 `WGER_REPETITIONS_CONFIG_LEAK` 실험을 제공한다. 그런데 그 upstream snapshot의 repetition 두 queryset은 이미 사용자별 `.filter(...)`다. 이번에 원본 파일을 내려받아 확인했다. 따라서 해당 자산의 목록 시나리오를 그대로 실행하여 ‘취약 원본’을 재현했다고 선언하면 안 된다. 해당 코드의 wrapper/patch 전체 효과를 실제 실행으로 더 확인해야 한다.
3. CVE-2026-27839의 parent `a912c313...`에서 nutritionplan·meal·mealitem의 raw `.get(pk=pk)`는 확인했고, 바로 다음 fix에서 `self.get_object()`로 바뀐다. **nutrition 사례의 source/fix 연결은 일치한다.**

증거는 `wger-27835-advisory.json`, `wger-27835-fix.json`, `wger-27835-actual-fix.json`, `wger-27839-advisory.json`, `wger-27839-fix.json`, `wger-public-template-normal.json` 및 source `.py`에 보존했다.

## C. BolaZ — 읽기 사례는 유용하나 바로 재현 가능한 벤치마크로 과장 금지

**Anbin Wu et al. Rethinking Broken Object Level Authorization Attacks Under Zero Trust Principle. arXiv:2507.02309v2, 2025.** [원문](https://arxiv.org/pdf/2507.02309v2) · [작성자 코드](https://github.com/wuanbin/bolaz)

- 읽기 수준: **2차**, 제목·초록·서론 pp.1–3·§6.2–6.7 pp.17–24·§7·§9. 로컬 PDF는 v2이며 DOI placeholder가 있는 submitted manuscript다. 출판 확정 학회 논문이라고 쓰지 않는다.
- 한 것: Java SpringBoot의 front/back source에서 resource ID 생산/소비와 전달 관계를 분석하고 허용 ID 범위를 생성한다.
- 안 한 것: 모든 프레임워크 지원·완전 자동 설정·실제 모든 정상 요청의 검증. §7.1 p.25: “BolaZ is currently implemented on the SpringBoot framework.” 한국어: 구현은 현재 SpringBoot에 한정된다.
- 같은 점: 어떤 객체가 어느 사용자·기능에 전달될 수 있는지 판정에 활용. 다른 점: client/server source와 CodeQL, DB 관계 수동 설정을 쓰므로 black-box Akto보다 많은 입력을 받는다.
- 판정: **조건부 살림.** 대상 선정과 소유자 가정의 반례에는 중요하지만, 동등 입력의 주 비교 도구로 바로 채택하지 않는다.

### 대상·정답·평가 실제 내용

Table 3 p.17은 Blog, BookStore, Mall, NewbeeMall, IceCms, MusicWebsite, OnlineExam, UniversityForum, InformationSystem, OnlineMall **10개 GitHub project/526 API**다. 표는 `-master` 명칭을 쓰며 여기서 정확한 commit은 확보하지 못했다.

RQ1·2는 이 중 5개를 수동 실행·Fiddler traffic capture·front/back source 분석으로 주석했다. 두 그룹이 독립 분석 후 교차 검증했으며 정답은 **P-API 40, C-API 54, API 관계 98**이다. 이 값은 정상/취약 BOLA 요청의 개수가 아니다. §6.4.1은 API 분류 오류를 수동 교정하고 관계 분석을 평가하므로 87% 관계 recall을 완전 자동 파이프라인 성능으로 사용하면 안 된다.

Table 8 p.22의 발견된 35 TP 가운데 SELECT는 **8**이다. Table 9 p.23의 읽기 subset은 다음과 같다.

| 앱 | 보고된 읽기 결함 |
|---|---|
| Mall | orderId로 다른 사용자의 주문 정보 조회 1 |
| MusicWebsite | userId로 다른 사용자의 collection detail/status/rank 조회 3 |
| IceCMS | userId로 다른 사용자 정보 조회 1 |
| BookStore | account로 타인 cart/order 조회 2 |
| OnlineExam | studentId로 다른 학생 성적 조회 1 |

이것은 저자가 수동 확인한 발견 사례이며, 전체 hidden positive/negative 모집단은 아니다. TN·전체 FN이 없으므로 이 표로 FPR 또는 전체 BOLA recall을 계산할 수 없다. 특히 '35/36 정밀도'를 '읽기 97% 재현율'로 바꾸면 잘못이다.

§6.7 비교는 PHP용 BolaRay를 SpringBoot에 맞추어 적용하고 authorization model을 수동 표시한 실험이다. 공개 원본 BolaRay를 아무 수정 없이 같은 조건으로 실행한 비교라고 소개하면 안 된다.

### 공개 코드 감사

`wuanbin/bolaz` commit `f89fe0d86f10b3d353efad26822bd3a04bebe8c7`을 내려받았다. Python3.9/JDK11/CodeQL 및 front AST가 필요하고 README에 DB primary/foreign key, table columns, 제외 API, 절대 경로를 직접 설정하도록 되어 있다. 파일 목록에서 10앱의 pinned deploy+seed+normal/attack labels 통합 패키지는 확인하지 못했다. `bolaray/api_config.json`은 3개 요청 예시이며 35개 정답 패키지가 아니다. 샘플 자격정보는 보고서에 복사하지 않았다. 도구 실행 NOT_RUN.

## D. IDORacle — 좋은 평가 방식과 공개 재현 자산, 판본을 분리해야 함

**Yuewantong Song et al. IDORacle: Template-Guided SQL-Sink Mediation for Object-Level Authorization in Java Applications. arXiv:2609.12426v1, 2026-09-11.** [원문](https://arxiv.org/pdf/2609.12426v1)

- 읽기 수준: **2차**, §1·§5 pp.7–9·§6–7 pp.9–11·§8·§10/Data availability. 원문은 Java SQL 런타임 예방 연구다.
- 한 것: 같은 subject·endpoint에서 자기/타인 객체를 바꾼 paired trace, DB 결과와 HTTP 응답의 독립 기록, direct/derived ownership·public/admin 예외·batch를 평가한다.
- 안 한 것: source/DB 없는 black-box scanner 평가가 아니다. §8은 외부 opaque API와 DB에 표현되지 않은 일시적 업무 상태를 범위 한계로 밝힌다. 마지막 Data availability: “Data will be made available on request.”
- 같은 점: 상태 코드가 같아도 실제 객체 반환이 달라질 수 있어 object-level evidence를 보존. 다른 점: 보호 도구에 선언된 metadata가 제공되므로 black-box 추정과 정보 조건이 다르다.
- 판정: **평가 프로토콜 참고로 살림, detector 성능 비교에서 분리.**

원문 §5.2의 두 low-privilege 사용자+administrator, §5.3의 정상/공격 짝, §5.5의 DB-level/response-level 분리는 AP-EYE에 직접 도움이 된다. 다만 CVE에서 파생한 합성 schema와 실제 앱에 붙인 agent 평가를 구별해야 하며, create_by가 있다는 이유만으로 그 앱의 원래 정책이 creator-only라는 독립 증거가 되지는 않는다.

### 현재 공개 자산은 별도로 확인

[IDOR-GUARD](https://github.com/GuanhangShiFDU/IDOR-GUARD) main `b1fbe699e56b930cca0c75e4558354bcd66db553`을 확보했다. README는 XXL-Job/RuoYi/BootDo/wger/Gitea/Krayin/Langflow를 열거하고, `original/no-cache/cache` 모드를 제공한다. fetch script에는 upstream commit/tag가 있다. Java17·Maven·Python3.12·Go1.24+·PHP8.1+·Node20+·Docker Compose가 필요하다. POSIX `.venv-*/bin/python` 경로를 사용하므로 Windows PowerShell에서 README를 그대로 실행하는 재현성은 확인되지 않았다. 전체 설치·서버 실행 NOT_RUN.

중요한 차이:

- README의 clone 명령은 `gshi` branch인데 읽은 GitHub 기본 브랜치는 `main`이다. 조사 시 `gshi=2d502872fa3a9da5bc3ffe5922a96f40fd6c0ec1`, `main=b1fbe699...`로 달랐다.
- `RealCaseController` 일부는 외부 앱을 부르는 대신 로컬 `RealCaseMapper`를 직접 호출한다. 별도 `RealCasePerfService`는 실제 앱 URL 호출 경로를 갖는다. UI의 Real case 이름만으로 외부 앱 원본 실행을 단정하면 안 된다.
- wger 목록 pin 불일치는 앞 절에 기록했다.
- arXiv v1의 fail-closed 서술과 공개 Django adapter README의 `FAIL_OPEN=True` 예시는 같지 않다. 전체 논문/현재 구현이 동등하다고 전제할 수 없다.

출판사 [별도 항목](https://www.sciencedirect.com/science/article/pii/S0167404826003196)은 제목을 data-access mediation으로 표시하고 January 2027, 22 paired cases/8 apps의 설명을 검색 결과로 노출했다. **전체 원문 접근은 403으로 실패했으므로 그 판본은 원문 미확인**이다. 해당 숫자를 본 검토의 검증된 데이터셋 개수에 합산하지 않았다.

## E. AuthScope — 정상 공개 조회를 먼저 제거해야 한다는 오래된 직접 근거

**Chaoshun Zuo, Qingchuan Zhao, Zhiqiang Lin. AuthScope: Towards Automatic Discovery of Vulnerable Authorizations in Online Services. CCS 2017, pp.799–813.** [학회 원문](https://acmccs.github.io/papers/p799-zuoA.pdf)

- 읽기 수준: **2차**, §1·§4.2.3–4.3·§5·§7·§9, PDF pp.1–2,9–11,13–14.
- 한 것: Android app 두 계정의 traffic 차분, 요청 식별자 대체, 사용자별 응답 차분으로 정보 노출을 탐지했다. §7이 대상 공격을 “unauthorized read”라고 한정한다.
- 안 한 것: 쓰기 인가의 자동 추론, 모든 로그인 방식, 유지되는 공개 API benchmark. Android4.4·Facebook 로그인·2017년 원격 서비스라는 환경이다.
- 실제 데이터: 2017년 3월 Google Play 인기 무료 앱 중 Facebook 로그인 조건을 만족하는 4,838앱. Table 2는 2,976 suspicious interfaces에서 **공개 자원 2,379개를 제거**하여 597개 vulnerable interface를 보고한다.
- 정답 방법: 사용자 특이 필드 비교 후 로그인 없이 다시 실행하여 public resource를 걸러낸다. 우리도 이를 단순 복사해서 'anonymous denied→private'라고 만들면 안 된다. 로그인한 모든 회원에게 공개되는 객체와 명시적 공유는 별도다.
- 판정: **방법/오탐 근거로 살림, 로컬 재현 데이터셋으로는 제외.** 597개를 내려받을 수 있는 정상/취약 API 패키지로 확보하지 못했다. 전체 FN/TN을 모르는 발견 연구다.

이 논문 때문에 '공개 자원 오탐을 줄인다' 자체를 새롭다고 주장하기는 어렵다. AP-EYE의 차이는 Akto의 구체적인 판정 경로에서 어떤 공유/혼합 목록/부족한 근거를 구별하고, 외부 고정 사례에서 어떤 지표가 나아졌는지로 좁혀야 한다.

## F. BACFuzz — 읽기 주 비교군에서 제외

**I Putu Arya Dharmaadi et al. BACFuzz: Exposing the Silence on Broken Access Control Vulnerabilities in Web Applications. arXiv:2507.15984v1, 2025.** [원문](https://arxiv.org/pdf/2507.15984v1)

- 읽기 수준: **1차**, 제목·초록·서론·§7·§9 결론/향후 과제 전체. 세부 benchmark 표를 2차 검증한 것으로 쓰지 않는다.
- 한 것: PHP runtime/SQL 관측과 mutation을 결합한 gray-box BAC fuzzer. 초록은 20개 앱, known 17개 중 16개를 보고한다.
- 안 한 것: §9 PDF p.11의 “both context-dependent and passive BAC remain open challenges”가 핵심이다. SELECT-only 정보 열람은 향후 과제로 남긴다.
- 판정: **읽기 주 비교군 제외.** 쓸 수 있는 원리는 HTTP 성공을 실제 보안 효과와 분리하는 것이지만, DML oracle을 읽기 oracle로 그대로 대체할 수 없다. arXiv에 현재 artifacts will be publicly released라고 되어 있고, 이번에 바로 실행할 저자 공식 데이터 패키지는 확보하지 못했다.

## G. TrafficAuthzRisk — 높은 점수의 외부 기준선으로 사용 금지

**Siqi Lin et al. A Non-Intrusive Traffic Analysis Framework for Authorization Risk Detection and Coordinated Response in Web Applications. arXiv:2607.16754v1.** [원문](https://arxiv.org/pdf/2607.16754v1)

- 읽기 수준: **2차**, 영어 제목·초록·§1·§5.1–5.2·§6·§7. PDF에 뒤따르는 중국어 번역은 수치 근거로 사용하지 않았다.
- 한 것: traffic-side evidence/risk fusion을 제안하고 저자 통제 환경에서 정상 1,000 + object-risk 600 + permission/context-risk 400을 생성한다.
- 안 한 것: 외부 실서비스 일반화, 강한 최신 도구 비교, 자연 발생 비율 평가. §6.2가 “generated by local testbed scripts”라고 명시한다.
- 평가: 양성 1,000개 전부가 읽기 BOLA가 아니다. 비교는 URL keyword·빈도·그 합집합이다. 초록의 99.9%를 우리 목표치나 Akto 대비 우수 근거로 쓰지 않는다.
- 판정: **보류.** 좋은 결과를 보이는 자체 예제를 반복하는 위험을 설명하는 문헌이며, 바로 가져올 공개 외부 정답 데이터는 확보하지 못했다.

## 이번 조사에서 직접 한 일과 남은 검증

실행한 것은 원문 추출·전체 지정절 읽기, 공개 3저장소 clone과 코드 감사, GitHub 공식 advisory/commit/source 대조, RESTler의 두 원본 메서드에 대한 10개 입력 구성요소 실행이다. 후속 작업에서 wger 2.4/2.5의 영양 계획 GET과 반복 설정 두 목록 GET을 **실제 원본 앱 경로로 재현**했고, 2.7의 원본 공개 template 테스트 **8/8**도 통과시켰다. 서비스 외부 스캔·RESTler 전체 실행·BolaZ 분석·IDOR-GUARD 전체 서버 실행은 **NOT_RUN**이다.

다음 검증에서 가장 우선할 항목은 **wger 영양 공지의 나머지 두 경로, 명시적 공유 정상 사례, 다른 실제 앱·원인 family**다. 현재 공식 이미지 2.4/2.5에서 두 CVE family의 일부/전체 GET 경로 정답을 확보했고, 2.7에서 공개 정상 테스트를 실행했다. 정확한 advisory parent/fix commit의 단일 변경 A/B 실험은 아니며 Akto 탐지 결과도 없다. 결과의 순서는 원문/공지 확인 → 코드 정답 확인 → 실제 endpoint 재현 → 고정 Akto/RESTler/AuthProbe 입력 가능성 확인 → scanner 성능 비교다.

평가 결과표는 `도구`, `snapshot`, `operation`, `principal`, `target object(s)`, `정책 근거`, `예상 허용 객체 집합`, `실제 반환 객체 집합`, `detector verdict`, `미판정 사유`를 최소 필드로 가진다. list에서는 금지된 객체가 하나 섞였는지도 검사한다. normal/공유 정책을 몰라 보류한 요청을 성공적인 정상 판정으로 세지 않는다.
