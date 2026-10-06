# AP-EYE 팀 공유용 조사: 방향 재검토와 평가 데이터셋·목표

조사·재검토일: 2026-10-06. 이 문서는 태스크 2·4의 **현재 제안**이다. 논문의 보고값, 공개 코드에서 확인한 사실, 이번에 직접 실행한 결과를 구분한다. 우리 개선판의 성능이나 실제 Akto 전체 실행 성능은 아직 측정되지 않았다. 팀 회의에는 [1쪽 결정 요약](TEAM-BRIEF.ko.md)을 먼저 공유할 수 있다.

## 팀에 먼저 전달할 판단

보고서의 원본 수집 자료, 초기·추가 조사 스크립트, 실행 로그와 외부 저장소 버전은 [조사 원자료 전체 보존](../raw-archive-2026-10-06/README.md)에 있다. 3개 로컬 조사 폴더의 648개 연구 파일과 외부 소스 사본 16개를 목록·해시로 대조했다.

**읽기·조회 BOLA 판정을 연구 본체로 유지하는 방향은 맞다.** [9월 30일 질의응답](../../../review/2026-09-30%20조재현%20교수님%20질의응답.md)의 “한 단계만 본체”와 [10월 2일 검토](../../../review/2026-10-02-최한림-조재현.md)의 Akto 기여 우선·읽기 BOLA·외부 기준 확보 요구에 맞는다. 한국어 PII 탐지는 필요한 제품 기능이지만, 인가 정답을 결정하는 필수 조건으로 묶으면 연구 질문과 평가 단위가 섞인다. **BOLA 판정과 노출된 한국어 정보의 분류를 따로 검증**한다. API의 비공개 정보는 PII가 없어도 보호 대상일 수 있다.

현재 자료로는 “Akto보다 정확하다”거나 “한국어 PII 정확도가 몇 %다”라고 말할 수 없다. 앞선 조사는 원문과 작은 실행 사례를 확보한 출발점이었다. 이번 재검토에서 **실제 서비스 wger의 취약 2.4·수정 2.5 GET 응답, 공개 정상 template의 2.7 원본 테스트, 공개 한국어 합성 데이터의 실제 규칙 기준선**을 보탰다. Akto 전체 실행과 같은 조건의 도구 비교는 남아 있다. [wger 취약·수정 실행](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md) · [공개 정상 테스트](appendices/authz/real-app/public-normal/README.ko.md) · [독립 방향 검토](appendices/direction/DIRECTION-REVIEW.ko.md)

팀 발표용 한 문장:

> 기존 Akto는 트래픽 기반 API 식별과 인증 교체형 BOLA 테스트를 제공한다. 우리는 공개·공유 객체와 금지 객체가 섞인 **읽기 응답에서 객체별 권한 근거와 실제 반환 내용을 대응시키는 판정**을 보강하고, **AuthProbe·VAmPI의 기능 회귀 사례와 wger 2.4/2.5 취약·수정 및 2.7 공개 정상 사례**에서 **종단 재현율, 정상 유형별 오탐률, 판정 커버리지, 근거 입력 비용**으로 평가한다.

별도 확장 문장:

> 한국어 개인정보 탐지는 노출된 응답을 설명하는 별도 모듈로 평가하고, 외부 한국어 합성 자료와 독립 API 문맥 세트에서 유형·경계별 정밀도와 재현율을 측정한다.

‘보강’은 **검증할 가설**이다. 원본 Akto의 전체 실패나 개선판의 우월성이 이미 확인됐다는 뜻은 아니다. Akto에 [Test Role](https://docs.akto.io/api-security-testing/how-to/create-a-test-role)과 [인증 교체 BOLA 템플릿](https://github.com/akto-api-security/tests-library/blob/ce2267da7e28927876b41d944e63bdde10e41e00/Broken-Object-Level-Authorization/BOLAByChangingAuthToken.yaml)이 이미 있으므로 기존 기능을 무시하지 않는다.

## 태스크 2: 인가 외부 기준을 무엇으로 잡을까

**도구 비교군**과 **평가 대상 API·정답 데이터**를 분리한다. 논문이 도구를 공개했다고 그 논문의 실제 서비스 정답 데이터까지 공개된 것은 아니다. 후보별 원문 절·페이지·코드 감사는 [인가 심층 검토](appendices/authz/AUTHZ-REVIEW.ko.md)와 [기존 원문 읽기 기록](paper-reading-notes.md)에 있다.

| 자료·원문 | 논문이 실제 평가한 대상과 정답 | 공개·이번 확인 | 채택 판단 |
|---|---|---|---|
| [AuthProbe, arXiv 2026](https://arxiv.org/abs/2607.20574), §VII–VIII, 2차 읽기 | 저자 합성 FastAPI 채용 API의 취약·수정 버전. 두 계정·객체 셋으로 허용/금지 명시 | [원본 코드](https://github.com/jbarach2012/AuthProbe)와 테스트 공개; 로컬 HTTP 재현 **완료** | 작은 기능 회귀 기준. 타 앱 성능의 근거가 아님 |
| [VAmPI](https://github.com/erev0s/VAmPI), [EvoMaster 보안 확장](https://arxiv.org/abs/2604.00702) §5.1–5.5, 2차 읽기 | 실제 실행 대상 목록 중 취약 훈련 API. 공개 책 목록은 정상, 타인 책의 비공개 내용은 차단되어야 함 | 원본 handler `vuln` 토글과 test client로 10건 **실행** | 공개 데이터와 보호 필드를 구분하는 두 번째 기능 점검 |
| [wger 공식 GHSA: 27839](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)·[수정](https://github.com/wger-project/wger/commit/29876a1954fe959e4b58ef070170e81703dab60e) | 실제 앱의 영양 계획·식사·식사항목 `nutritional_values` GET 3경로. 공지상 영향 `<=2.4`, 수정 `>=2.5`. 타인 비공개 자원 반환이 금지 | 취약 raw `.get(pk=pk)`와 수정 `self.get_object()` 코드 대조. **공식 2.4/2.5 이미지에서 nutritionplan 1경로의 자기/교차 8요청 실행 완료** | 실제 서비스 외부 양성군 확보. 나머지 meal·mealitem 2경로는 **NOT_RUN**. 3경로는 같은 CVE family |
| [wger 공식 GHSA: 27835](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm)·[실제 목록 수정](https://github.com/wger-project/wger/commit/035a66161dcbdbac8bbd03adbc1bdb071f233274) | `repetitions-config`·`max-repetitions-config` GET 목록 2경로에서 타인 객체 유출. 공지상 영향 `<=2.4`, 수정 `>=2.5` | 두 `.all()`과 소유자 filter diff 코드 대조. **공식 2.4/2.5 이미지에서 두 목록·두 계정, 총 8요청 실행 완료** | 혼합 목록/객체별 판정 외부 양성군 확보. 2경로는 같은 CVE family |
| [wger 정상 공개 template 수정·테스트](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9) | maintainer가 비소유자의 **공개** routine template 상세 GET 200을 정상으로 명시 | 공식 **2.7 이미지에서 원본 테스트 8/8 통과**, 비소유자 공개 detail 200·동일 ID assert 포함. [실행 패키지](appendices/authz/real-app/public-normal/README.ko.md). 수정 커밋보다 36커밋 뒤 snapshot | 정상 공개를 BOLA로 오인하는지 시험할 외부 oracle. 2.4/2.5 CVE와 다른 버전 |
| [BACScan, CCS 2025](https://yuanxzhang.github.io/paper/bacscan-ccs25.pdf) §4.2.2·§5 Tables 1–3, 2차 읽기 | 실제 앱 20개, 그중 알려진 결함이 있는 6개 앱의 44건 중 읽기 20·수정 24 | [코드](https://github.com/LFYSec/BACScan) 공개이나 crawler 간소화·수동 절차 존재. 원문과 앱 이름·버전 확인, 재현 **NOT_RUN** | 실제 앱 pool. 읽기 20개를 BOLA로 자동 간주하지 말고 사례별로 분류 |
| [BolaZ, arXiv v2](https://arxiv.org/pdf/2507.02309v2) §6.2–6.7 Tables 3·8·9, 2차 읽기 | SpringBoot 10개 프로젝트/526 API; 저자가 확인한 SELECT 읽기 결함 8건(5개 앱) | [코드](https://github.com/wuanbin/bolaz) 공개. 앱 pin·정상/공격 전체 라벨 패키지 부족; **NOT_RUN** | 후속 실제 읽기 후보·소유관계 참고. 8건을 완전한 분류 벤치마크로 계산하지 않음 |
| [RESTler ICST 2020](https://patricegodefroid.github.io/public_psfiles/icst2020.pdf) §III–V, 2차 읽기 | 익명 Azure A/B·Office365 C. 정상/BOLA request-level 정답 데이터는 없음 | [NameSpaceRuleChecker](https://github.com/microsoft/restler-fuzzer/blob/6d984deedbc54aad957fa3da0c7e9e5df23a2aee/docs/user-guide/Checkers.md)는 공개, 기본 OFF. 원본 판정 메서드 10입력 구성요소 실행; E2E **NOT_RUN** | 별도 인가 비교 **도구**. 논문의 익명 앱은 재현 데이터셋으로 채택 불가 |
| [IDORacle arXiv v1](https://arxiv.org/pdf/2609.12426v1) §5–8, 2차 읽기 | 주체·endpoint 고정, 자기/타인 객체 paired trace와 DB/HTTP 이중 oracle | 원문은 data on request. 별도 [IDOR-GUARD](https://github.com/GuanhangShiFDU/IDOR-GUARD) 공개 자산 감사 완료, 전체 실행 **NOT_RUN** | 짝지은 정답·DB/응답 검증 방식 참고. black-box 동등 비교군 아님 |

BACScan Table 1의 실제 알려진 읽기 사례는 Memos 0.9.0 **5**, WordPress_SPM 4.57 **1**, Snipe-it 5.0.3 **3**, Lunary 1.2.7 **6**, Collabtive 2.1 **5**이고 MyBloggie 2.1.4는 **0**이다. 논문의 `RBAC`는 **Read-based Broken Access Control**을 뜻한다. 전체 20개에서 TP 15·FP 3·FN 5이므로 알려진 읽기 사례에 대한 재현율은 75%, 해당 발견의 정밀도는 83.33%다. **정상 전체/TN이 없어 FPR은 계산할 수 없다.** 새 발견을 합친 Table 3의 36/41=87.80%는 다른 모집단이다. [BACScan 원문 pp.9–11](https://yuanxzhang.github.io/paper/bacscan-ccs25.pdf)

정답 재현의 함정도 확인했다. CVE-2026-27835의 공식 advisory가 연결한 한 commit은 실제 두 목록의 `.all()` 수정이 아니다. 별도로 `035a661…`을 추적했다. [IDOR-GUARD](https://github.com/GuanhangShiFDU/IDOR-GUARD)의 wger pin에서는 해당 **목록 결함이 이미 수정된 소스**가 관측됐다. 패키지 이름만 보고 취약·수정 짝이라고 채택하면 정답이 틀린다. nutrition 27839의 parent/fix 연결은 일치했다. [대조 기록](appendices/authz/AUTHZ-REVIEW.ko.md)

**비교 도구는** 고정판 Akto 원본, 기존 Test Role/YAML을 적절히 설정한 Akto, 같은 근거를 받는 단순 객체 일치 규칙, RESTler NameSpaceRuleChecker, 제안 방식으로 잡는다. AuthProbe는 해당 공개 합성 앱의 회귀 기준으로만 둔다. [AuthScope CCS 2017](https://acmccs.github.io/papers/p799-zuoA.pdf)는 비인가 읽기 후보 중 공개 자원 2,379개를 제거했다. 그러므로 “공개 자원을 걸러낸다” 자체는 새로운 연구 주장이 아니다. [BolaRay CCS 2024](https://leehaofeng.github.io/papers/2024-BolaRay.pdf)는 SELECT를 민감 연산으로 취급하지 않는다고 한계에 명시했고, [BACFuzz arXiv v1](https://arxiv.org/pdf/2507.15984v1)은 passive/SELECT 읽기를 남은 과제로 적어 이번 읽기 주 비교군에서 제외한다. [인가 심층 검토](appendices/authz/AUTHZ-REVIEW.ko.md)

### 이번에 직접 실행한 인가 증거

| 실행 | 확인 결과 | 의미와 한계 |
|---|---|---|
| AuthProbe 원본 pytest | **11 passed** | [원본 테스트 로그](evidence/authprobe-pytest.log). 논문 저자 target의 자체 테스트 |
| AuthProbe localhost HTTP | 취약 BOLA **6개 요청**, 기타 finding 2; 수정 finding 0; 별도 정답 응답 28개 | [fixture 전체·요청 ID·반환 ID·본문 및 finding/gold 일대일 대조](evidence/authprobe-reproduction.json). **BOLA 결함은 1개 로직**이며 6독립 취약점이 아님 |
| VAmPI 원본 handler | 취약 비공개 책 교차조회 2, 정상 조회·차단·공개 목록 8 | [10개 test-client 결과](evidence/vampi-reproduction.json). 네트워크 scanner 성능 아님 |
| **wger 공식 2.4/2.5 이미지** | 영양 GET: 2.4 교차조회 2개 **200/타인 고유값**, 2.5 같은 정책 2개 **404**. 반복 설정 2목록: 2.4 타인 ID 혼입 4요청, 2.5 자기 ID만 4요청 | [16개 실제 Django API 경로 응답과 고정 image digest](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md). synthetic fixture/force_authenticate 사용, Akto scanner 결과 아님 |
| **wger 공식 2.7 이미지** | 원본 template 테스트 **8/8 통과**; 비소유자의 공개 detail GET 200·동일 ID, 자기 template GET 200·동일 ID | [원본 테스트 로그·image digest·재실행 명령](appendices/authz/real-app/public-normal/README.ko.md). 2.4/2.5와 다른 snapshot·정상 정책 정답, Akto scanner 결과 아님 |
| RESTler namespace 판정 원본 메서드 | 합성 응답 10입력에서 `[]`는 예외, `[ ]`·줄바꿈 빈 배열·공개/자기목록도 violation 가능 | [구성요소 결과](appendices/authz/evidence/restler-oracle-component-probe.json). E2E/FPR 성능 아님 |

이 네 실행으로 **Akto의 실제 전체 재현율·오탐률은 아직 산출되지 않는다.** [Akto 배포·seed·Test Role·CLI 검사 조건](appendices/direction/DIRECTION-REVIEW.ko.md#8-akto-전체-기준선의-로컬-실행-사전조건)을 먼저 맞춰야 한다. 공식 [CLI](https://docs.akto.io/api-security-testing/how-to/run-tests-in-cli-using-akto)는 context 테스트를 건너뛸 수 있다고 명시하므로 CLI의 빈 결과를 정상 판정으로 세지 않는다. 실행 단계는 `전체 gold → 수집/선택 → 재생 실행 → 유효 응답 → 판정 가능 → 정확한 확정`으로 기록한다.

## 태스크 2: 한국어 PII 자료와 다른 언어 방식 비교

PII 분류에는 서로 다른 두 과제가 있다. Akto의 JSON **필드 유형 분류**와 자유서술 문장 속 정확한 **문자 구간(span) 탐지**다. 필드 전체를 찾은 결과를 span exact F1처럼 채점하지 않는다. 공개된 이름·전화번호라도 보는 주체와 목적에 따라 인가 판단은 달라지므로, PII 탐지 결과를 BOLA 정답으로 쓰지 않는다.

| 자료·원문 | 실제 생성·라벨·보고 지표 | 공개·이번 확인 | 채택 판단 |
|---|---|---|---|
| [SPY, NAACL SRW 2025](https://aclanthology.org/2025.naacl-srw.23/) §3–6·Limitations, 2차 읽기 | 의료 4,491·법률 4,197 **영어** 문서. Llama-3-70B 문맥/placeholder, Faker로 6개국 값 채움, 방해 개체 추가. 7유형 | [코드·생성 자료](https://github.com/LogicZMaksimka/SPY_Dataset) 공개. 생성/학습 **NOT_RUN** | 문맥 원형 분리·국가별 형식·도메인 이동 참고. 저자 정보만 gold인 기준은 채택 불가 |
| [K-LegalDeID, EACL 2026](https://aclanthology.org/2026.eacl-long.103/) §4–5, 2차 읽기 | 비식별 실제 판결문 2,000건의 가림 부분 치환과 SNS·Thunder 결합. 11유형, 8명 주석·κ=.7352. 문장 인스턴스 1,091,998 | 완전 합성 문맥 아님. 즉시 받을 저자 데이터/코드 **미확인** | 한국어 라벨·경계 기준. 내부 typed entity F1 .9923과 다른 Thunder 도메인 .3658은 분포 이동 주의 사례 |
| [Thunder-DeID, EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.682/) 및 [arXiv v3](https://arxiv.org/pdf/2506.15266v3) §3–4, 2차 읽기 | v3: 비식별 판결문 6,700건·48,306 entity·729 label, 목록/규칙 치환. 80/10/10 문서 분할 | [공식 소개](https://champ.snu.ac.kr/datasets-deid)는 **다른 공개판 4,500건/595유형**. 연결 HF 접근 401, 코드 링크 404 확인 | 법률 형태·분할 원칙. v3의 이진 token F1 .9808·유형 token F1 .9105는 entity F1과 직접 비교 불가 |
| [K-PII-Bench 공개 카드](https://huggingface.co/datasets/woohyun212/k-pii-bench)·[코드](https://github.com/woohyun212/k-pii-bench), 원문 **미확인** | 공개 자산은 한국어 합성 300,000문서/18유형/12도메인·문자 offset/BIO 제공 | API에서 train/dev/test 앞부분 **126문서·541 span 형식 일치**. 의미 불일치와 음성 문서 0개 발견; 전체 모델 성능 **NOT_RUN** | 큰 외부 문맥 후보. 원고와 수정 공개판의 차이·골드 의미를 검증한 뒤 사용 |
| [Marker Korea ko-pii](https://github.com/Marker-Inc-Korea/ko-pii), 공개 자산 감사 | 한국어 합성 540문서·3,635 문자열 gold·26유형. 문자 offset 없는 set 평가 | 규칙 도구를 전체 540문서에 **직접 실행**; 아래 지표 확인 | 바로 실행 가능한 외부 한국어 기준선. strict span 평가에는 gold 보강 필요 |
| [OpenPII 1.5M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m), 카드·표본 | 카드상 30언어·19유형, 한국어 포함. 혼합 첫 표본 126건 중 한국어 **16문서·113 span** | 한국어 표본의 offset 일치 확인. 불자연스러운 국내 이름·번호/문맥 후보, 한국어 음성 0개; 한국어 전체 규모 미확인 | 다국가·다른 생성기 스트레스 후보. 품질 검수 후 작은 독립 시험군으로만 고려 |
| [Gretel 합성 금융 문서](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual), 카드·metadata | 영어·스페인어·스웨덴어·독일어·이탈리아어·네덜란드어·프랑스어 7언어. 한국어 원본 없음 | 생성·NER 주석·검토 절차 확인. 카드의 split 수와 metadata split 수 불일치 | 다국어 생성 방식 참고. 한국어 주평가군에서 제외 |
| [PII-Bench, ACL 2026](https://aclanthology.org/2026.acl-long.227.pdf) §3–5, 2차 읽기 | 질문과 **정보 주체**의 관계를 span/유형과 구별해 평가. synthetic single 1,214, multi 1,228, hard/distract 각 200 | 원문 방법 확인. 즉시 내려받을 저자 dataset/code 경로 미확인, **NOT_RUN** | 주체별 gold 설계 참고. 질문 관련성을 API 조회 권한으로 대체하지 않음 |

다른 나라의 방법을 한국어로 가져올 때는 **언어 지원, 라벨, gold 단위, 도메인, 수집 방식**이 같아야 점수를 비교할 수 있다. SPY의 6개국 Faker 형식은 문맥 다양화 방법이지 한국어 정확도의 증거가 아니다. K-LegalDeID의 내부 .9923 entity F1과 Thunder의 .9808 binary token F1은 단위가 다르다. 같은 K-LegalDeID에서도 보지 못한 Thunder 문맥의 entity F1은 .3658로 떨어졌다. 원인을 하나로 단정할 수 없지만 내부 split 점수를 API JSON에 그대로 적용할 수 없다는 직접 경고다. [K-LegalDeID 원문 Tables 1–2](https://aclanthology.org/2026.eacl-long.103.pdf) · [Thunder v3 Table 2](https://arxiv.org/pdf/2506.15266v3)

국가별 정형 번호는 대개 **형식 후보 → 정규화 → 검증 숫자·구조 → 주변 문맥**을 결합하고, 이름·주소는 언어별 NER나 사전을 더한다. [Presidio 지원 유형](https://presidio.dataprivacystack.org/supported_entities/)은 영국 NHS, 스페인 NIF, 인도 Aadhaar, 한국 식별번호 같은 국가별 규칙을 나누어 제공한다. 조사한 Akto 컴포넌트의 9개 국가 **예시 전화번호**에서는 국제 E.164 입력 9/9, 국내 형식 0/9 인식이었지만 표본 36개 형식 진단일 뿐 국가별 recall을 나타내지 않는다. [원본 규칙·실행 절차](../../akto/research-2026-10-06/AKTO-DEEP-RESEARCH.ko.md#8-다른-나라-pii는-실제로-어떻게-찾나)

| 같은 원문 안에서만 해석할 보고 수치 | 조건과 정확한 의미 | 이번 사용 판단 |
|---|---|---|
| [SPY Table 3](https://aclanthology.org/2025.naacl-srw.23.pdf)의 의료 문서 이름 F1: Presidio **28.2**, Llama-3-70B **67.6**, 반대 도메인 학습 DeBERTa **87.8** | 영어 합성 의료 문맥·저자 정책 라벨·각기 다른 학습 방식 | 문맥/모델이 이름 인식에 미치는 영향 참고. 한국어 순위가 아님 |
| [GLiNER2-PII Table 2](https://arxiv.org/pdf/2605.09973)의 SPY 법률/의료 평균 F1: **0.471** | 7개 유럽 언어 학습의 별도 모델/평가 설정. SPY 원문은 합성인데 GLiNER2 서술과 차이 있음 | 한국어 성능으로 인용하지 않음. 위 SPY Table 3과도 직접 순위 비교 불가 |
| [K-LegalDeID Tables 1–2](https://aclanthology.org/2026.eacl-long.103.pdf): 내부 typed entity **0.9923**, Court+SNS→Thunder **0.3658** | 한국어 법률 문맥의 서로 다른 분포. 정확한 entity 경계+유형 채점 | 도메인 이동 실험의 필요성. API 일반화 점수가 아님 |
| [ko-pii 저자 방식의 이번 실행](appendices/pii/PII-REVIEW.ko.md#2-직접-실행한-한국어-규칙-기준선): **0.79018** | 한국어 합성 540문서, 부분문자열 허용 set scorer | 오프라인 규칙 개발 기준선. strict span·국가별 공통 F1 아님 |

**국가별 정확도를 공정하게 순위 매길 공개 공통 시험은 이번에 확보하지 못했다.** 제품의 지원 언어 목록, 개별 confidence 점수, 논문의 서로 다른 F1을 정확도 순위표로 합치지 않는다. [제품별 한국어 기능·공식 출처](../../akto/research-2026-10-06/AKTO-DEEP-RESEARCH.ko.md#9-제품별-한국어-지원-비교)

### 한국어 공개 자산을 직접 돌려 보니

[ko-pii 고정 commit](https://github.com/Marker-Inc-Korea/ko-pii/commit/9516cabd6f582935cae1536ccbd8c5448afae679)의 540문서·3,635 원시 문자열 gold에 **저자 공개 규칙 탐지기**를 실행했다. 저자 방식의 부분 문자열·set scorer에서는 TP 2,832, FP 733, FN 771, **F1 0.79018**이었다. 이 scorer의 TP는 매칭된 **예측** 수이고 PERSON 길이 필터와 다대다 부분문자열 매칭을 쓰므로 `TP+FN`을 원시 gold 수로 해석하지 않는다. 같은 예측을 정확한 표면 문자열 set으로 채점하면 **F1 0.66481**이다. 둘 다 위치와 반복 출현을 세는 **strict 문자 span F1이 아니다.** 같은 문자열이 여러 번 등장하는 gold가 220개이고, 실제 빈-gold 문서는 README의 18이 아닌 **19**였으며 그중 **15문서에서 탐지**가 나왔다. 숫자 하나만 보고 한국어 PII 탐지가 끝났다고 말할 수 없다. [실행·채점 증거](appendices/pii/evidence/ko-pii-full-audit-and-baseline.json) · [scorer 원본](https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/src/ko_pii/eval/kdpii.py)

K-PII-Bench의 126개 편의 표본은 `text[start:end] == surface`와 제공 BIO의 재계산 결과가 모두 맞는다. 그러나 **음성 문서 0개**여서 오탐률 확인이 안 된다. ‘강사 등록 번호는 원불교’처럼 형식이 맞는 entity가 의미상 잘못된 문맥에 놓인 사례도 있다. [DATASHEET](https://github.com/woohyun212/k-pii-bench/blob/1b480c515cc8425ea5c5675079bd7cf17b951554/DATASHEET.md)는 원고 snapshot의 약 35,483 span/label 불일치와 약 4,182 잔존 placeholder를 공개판에서 수정했다고 적는다. 이는 **작성자 수정 내역**이며 이번에 원본 오류 전부를 재실행한 것은 아니다. 원고 점수와 현재 파일을 같은 실험으로 합치지 않는다. 또한 공식 BIO CLI와 별도 `span_metrics.py`의 `strict` 함수는 다르다. 후자는 반복된 같은 표면형을 set으로 합쳐 한 번만 찾아도 F1 1.0을 돌려주는 반례를 확인했다. 재현 시 **평가 함수와 문서·문자 위치 단위**를 고정해야 한다. [표본 감사](appendices/pii/evidence/kpii-deep-sample-audit.json) · [scorer probe](appendices/pii/evidence/kpii-scorer-probe.json)

**추가 비교 후보**는 한국어 인식기를 켠 [Presidio 공식 recognizer](https://presidio.dataprivacystack.org/supported_entities/), 독립 ko-pii 규칙, Akto 원본 필드 분류, 한국어 NER다. Presidio에 KR 주민번호·외국인등록번호·여권·운전면허·사업자번호 recognizer가 있으므로 “Presidio 한국어 미지원”이라고 단정하면 안 된다. 기본 영어 구성과 한국어 인식기를 활성화한 구성을 분리한다. [GLiNER2-PII 원문](https://arxiv.org/pdf/2605.09973)은 7개 유럽 언어를 학습 대상으로 적어 한국어 성능 근거가 아니다. 모델/규칙의 지표는 **같은 시험 자료·라벨·평가 코드에서 새로 측정**한다. [다국어 근거·수치 해석](appendices/pii/PII-REVIEW.ko.md#4-다국가-pii는-어떻게-하는가--방법과-수치-해석)

### 한국어 합성 평가 세트의 정답 계약

외부 ko-pii와 K-PII-Bench는 각각 독립 결과표로 먼저 평가하고, 우리 **API 응답 문맥**의 합성 stress set은 별도 보완 자료로 만든다. 템플릿·원문 문서·생성기별로 train/dev/test를 나누고, 값을 채우기 전에 문맥 원형을 분할한다. 생성 시 `(문서 ID, JSON path, 시작·끝 문자 offset, 표면형, 유형)`을 저장한다. `홍길동에게`의 gold는 `홍길동`만으로 고정하고 조사·공백·하이픈·Unicode 정규화 차이를 검증한다. 반복된 동일 문자열도 출현마다 따로 표시한다. 정상 주문번호·가격·공개 대표번호·빈 문서·PII와 비PII가 섞인 목록을 넣어 오탐과 과도한 마스킹을 측정한다. 형식 자동검사와 의미상 라벨 검토를 분리하고, 일부는 독립 이중 주석·불일치 조정을 한다. 문서·템플릿 단위 분할과 라벨 매핑표는 시험 실행 전에 고정한다. 이 API stress set은 **아직 생성·독립 검수 NOT_RUN**이며 외부 자료의 성능을 대체하지 않는다.

## 태스크 4: 평가 계약과 목표 수치 결정 순서

인가 gold 한 건은 `(앱·고정 버전, 요청자, 대상 객체, GET 연산, 시점의 허용 정책)`이다. 평가자는 서버 fixture/공식 정책/취약·수정 코드로 gold를 만들고, 도구에는 사전 허용한 증거만 준다. 소유자 조회·익명 공개·로그인 사용자 공개·명시적 공유·미공유·빈 목록·허용 객체만 있는 목록·허용/금지 혼합 목록을 구분한다. 목록 응답에는 **예상 허용 객체 집합과 실제 반환 객체 집합**을 기록한다. 200이라는 상태만으로 BOLA를 확정하지 않는다.

도구의 `보류`는 실제 보안 상태의 세 번째 정답이 아니라 **판정 근거의 부족**을 뜻한다. 금지/허용 gold가 있는 사례에서도 도구는 보류할 수 있다. `수집 안 됨`, `검사 선택 안 됨`, `실행 실패`, `응답은 받았으나 보류`, `정상 확인`, `BOLA 확인`을 분리한다. 모든 경고가 없다는 이유로 정상으로 바꾸지 않는다. [평가 설계 독립 검토](appendices/direction/DIRECTION-REVIEW.ko.md#6-정답보류표본-수를-고정하는-방법)

| 개선할 문제 | 주 지표 | 함께 보고할 지표·주의 |
|---|---|---|
| 비인가 조회 미탐 | **종단 재현율 = 정확히 확정한 BOLA / 전체 gold BOLA** | 미발견·skip·실패·보류인 양성도 분모에 포함. 요청별·endpoint/CVE family별·앱별로 따로 보고 |
| 공개/공유 정상 오탐 | **FPR = BOLA라고 잘못 확정한 정상 / 전체 gold 정상** | 공개·공유·자기 객체·목록 유형별 FP/분모. Precision과 혼동 금지 |
| 전부 보류하는 회피 | **판정 커버리지 = 확정 판정 수 / 전체 gold 수** | 양성·정상별 보류율, 동일 커버리지에서 오류율 비교 |
| 정보 입력량 | 객체·정책 라벨 수, 계정/시드 생성과 사람 검수 시간 | 동일 요청/객체/정책 정보 실험과 도구별 정상 워크플로 실험을 분리 |
| 한국어 필드/유형 | 유형별 precision·recall·macro F1 | Akto 필드 전체 예측은 별도 계산, 라벨 지원 범위와 negative 비율 함께 공개 |
| 한국어 문장 경계 | **유형+시작·끝 문자 위치의 exact entity F1** | 반복 출현·조사·공백, 별도 zero-PII 문서 FPR과 비마스킹 누출률. ko-pii 저자 F1과 직접 비교 금지 |

동일한 소유권 버그에 요청을 수십 개 보내 독립 취약점 수를 부풀리지 않는다. **AuthProbe의 교차 조회 6건은 한 결함**, wger의 nutrition 3경로는 CVE family 하나, 목록 2경로도 family 하나다. 앱/원인으로 묶어 불확실성과 일반화 범위를 보고한다. 0/30 독립 정상 요청에서 오탐 0이어도 이항 가정의 단측 95% 상한은 약 9.5%이고, 같은 앱에서 반복한 요청은 그 독립 가정도 충족하지 않는다. 따라서 초기 0건을 ‘FPR 0% 입증’이라고 발표하지 않는다.

목표 수치는 **외부 앱·정답·negative 구성 → 개발 세트 고정 → Akto/RESTler/단순규칙/PII 규칙 기준선 실행 → 최소 개선 폭과 허용 저하·threshold 사전 동결 → 독립 시험 세트 한 번 평가** 순서로 정한다. 현재 숫자로 고정할 수 있는 것은 **평가 fixture의 기대 결과와 향후 탐지기 회귀 조건**이다. AuthProbe에는 BOLA gold 6요청과 수정판 정상 응답을, wger에는 2.4의 영양 교차 노출 2요청·혼합 목록 4요청과 2.5의 동일 정책상 차단·필터링 응답을 보존했다. 향후 탐지기에는 이 양성을 놓치지 않고 정상·수정 응답을 오경고하지 않는지를 요구하되, **아직 어느 도구도 이 fixture에서 전부 6/6을 검출했다고 주장하지 않는다.** 이것은 연구 목표의 통계적 증거가 아니다. Akto 전체 FPR·recall, 한국어 필드/span 성능의 숫자 목표는 **NOT_MEASURED/TBD**로 남긴다. baseline 없이 “95% 정확도”를 정하면 근거가 없다.

## 비교를 공정하게 만드는 두 실험

1. **판정 비교:** 같은 고정 요청/응답, 계정·객체 및 허용한 정책 단서를 제안 방식과 단순 객체 일치 규칙에 똑같이 제공한다. Akto의 원래 입력/설정과 설정 보정판도 함께 기록한다. 추가된 정책 정답 정보 때문에 좋아진 것과 판정 방법 때문에 좋아진 것을 나누어 해석한다. 기존 설정 또는 단순 규칙이 똑같이 해결하면 기여를 회귀 시험·구성·설명 가능성으로 정직하게 좁힌다.
2. **도구 워크플로:** 같은 대상 snapshot에서 Akto의 traffic seed/Test Role, RESTler의 spec/두 번째 자격, AuthProbe의 OpenAPI/객체 발견 등 도구가 실제 요구하는 절차로 실행한다. 준비·reset·설정·사람 시간과 요청 예산, skip을 기록한다. 지원 입력이 달라 판정 자체의 우열과 운영 비용을 한 점수로 섞지 않는다.

Akto 전체 기준선은 아직 **NOT_RUN**이다. 현재 소스 `42e88a2…`, tests-library `ce2267d…`의 템플릿/비교 함수 **구성요소 조사만** 완료했다. 실제 실행 때는 이미지 digest, 테스트 정의 SHA, 앱 commit, fixture·정책, 원본 정상 요청 seed, 재생 요청 수, 선택/skip 사유, 반환 객체와 판정을 보존한다. Docker는 준비됐지만 기존 다른 컨테이너가 있어 별도 프로젝트명·loopback 포트·볼륨을 사용해야 한다. [Akto 사전조건](appendices/direction/DIRECTION-REVIEW.ko.md#8-akto-전체-기준선의-로컬-실행-사전조건)

## 팀이 결정하거나 다음 검증에서 채울 부분

| 우선 | 구체적인 결정·검증 | 완료로 볼 증거 |
|---|---|---|
| P0 | **연구 본체/구조:** 읽기 BOLA를 한 단계로 확정하고 한국어 PII는 별도 확장. 내부 게이트웨이/외부 스캐너의 데이터 수집 관점은 현 아키텍처에서 여전히 TBD | [현 아키텍처](../../../arch/architecture.md)에 합의된 입력·출력·인가 판정 경계가 기록됨 |
| P0 | **실제 서비스 정답 확장:** wger 2.4/2.5의 영양 1경로·반복 목록 2경로와 2.7의 공개 template 정상 테스트는 확보. 명시적 공유와 더 다양한 앱·원인 family를 추가 | [취약·수정 패키지](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md) 및 [공개 정상 패키지](appendices/authz/real-app/public-normal/README.ko.md)와 같은 수준으로 추가 앱의 GET 응답/정책/버전을 고정 |
| P0 | **Akto 원본 기준선:** 동일 API에 traffic seed·Test Role·GET BOLA template를 적용, 원본/기존 설정 보정/단순 규칙을 비교 | 모든 gold 요청의 `선택→실행→응답→판정/skip` 증거와 image digest |
| P0 | **한국어 기준선:** 외부 ko-pii 전체 규칙 결과와 K-PII 공개판 품질 감사를 바탕으로 필드/span 과제를 분리; 한국어 Presidio 등 동일 라벨 비교 | 모델/규칙 버전·라벨 매핑·gold offset·negative/중복출현 규칙·실제 TP/FP/FN |
| P1 | **목표 숫자:** 개발군 baseline과 통제된 입력 비용을 측정한 뒤 효과 크기·허용 저하·검정 단위 결정 | 봉인된 시험군을 보기 전의 실험 등록/평가 스크립트 고정 |

완료한 작업은 논문 제목 수집이 아니라 **원문 평가 절·표·한계 확인, 취약 수정 소스 대조, 실제 wger의 취약·수정 GET과 공개 정상 테스트 재현, 한국어 규칙 기준선·채점 감사**다. Akto/RESTler 전체 도구 비교와 한국어 새 모델 성능은 아직 결과로 보고하지 않는다. 상세 실행 명령·환경은 [재현 기록](reproduction.md), [wger 취약·수정 실행](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md), [공개 정상 실행](appendices/authz/real-app/public-normal/README.ko.md), [인가 검토](appendices/authz/AUTHZ-REVIEW.ko.md), [PII 검토](appendices/pii/PII-REVIEW.ko.md), [방향 검토](appendices/direction/DIRECTION-REVIEW.ko.md)에 둔다.
