# 원문 읽기 기록

2026-10-06. 저장소 `paper-reading` 스킬에 따라 제목·초록·서론·결론/한계를 먼저 읽고, 채택 후보의 데이터·방법·평가 절을 추가 확인했다. 추출기가 대문자 절 제목이나 2단 편집을 놓친 부분은 PDF의 해당 페이지 전체 텍스트로 보완했다. 아래 `p.`는 **로컬 원본 PDF의 1부터 시작하는 페이지 번호**다. 출판면 번호가 다른 경우 함께 적었다. 자동 변환 Markdown은 검색 보조이며 표 수치는 PDF를 따른다.

## A. AuthProbe

**Jay Barach. AuthProbe: Specification-Driven, Multi-Identity Detection of Broken Object-Level Authorization in Recruitment APIs. arXiv:2607.20574, 2026.** [원문](https://arxiv.org/pdf/2607.20574) · [공개 코드](https://github.com/jbarach2012/AuthProbe)

- 읽기 수준: **2차**, §I·§VII·§VIII·결론 중심. 동료 심사를 거친 학회 논문으로 표기하지 않는다.
- 한 것: OpenAPI와 여러 사용자 세션으로 객체를 발견하고 다른 사용자로 읽기를 시도한다. 저자가 만든 취약/수정 ATS를 이용하여 반복 가능한 검사를 보인다.
- 안 한 것: 임의 실제 서비스 전반에서의 일반화, 복잡한 역할 정책, 쓰기 취약점 검증. §VIII.A p.8: “the two targets are synthetic and were authored to exhibit and to fix the studied flaw”. 번역: 두 대상은 연구한 결함을 넣고 고치도록 만든 합성 대상이다.
- 같은 점: 읽기 BOLA·여러 계정·증거 기반 결과. 다른 점: AP-EYE는 혼합 목록·공유 정책·한국어 개인정보가 있는 응답을 추가로 다루려 한다. 아직 새롭거나 더 정확하다고 입증하지 않았다.
- 판정: **살림 — 실행 가능한 외부 기능 기준선.** 실서비스 대표 벤치마크로는 쓰지 않는다.

2차 확인: §VII.A p.6의 두 FastAPI 인메모리 대상에 Alice/Bob 두 사용자, 각 3개 지원서가 존재한다. 동일 계정 조회는 허용되고 타인 조회는 금지되어야 한다. 취약 버전은 순차 ID와 누락된 소유권 검사, 수정 버전은 UUID·소유권 검사·균일한 404를 사용한다. 따라서 수정 버전은 세 요소가 함께 바뀌며, 소유권 검사 하나의 효과만 분리한 실험은 아니다.

Table III p.6의 취약 대상은 High 7, Medium 1이며 BOLA는 6건이다. 나머지는 ID 열거 관련 결과다. 주요 카운트를 이번 공개 commit에서 재현했고 저자 pytest 11개가 통과했다. 논문의 전체 시간 실험(m=1…50), 모든 알고리즘 단계의 논문/코드 일치성은 재현하지 않았다. 현재 `scanner.py`/`probes/bola.py`는 목록으로 ID를 수집하고 타 계정 응답의 해당 ID를 확인한다. 논문의 소유자 응답 비교 설명을 현재 코드에 그대로 투영하지 않는다.

재사용: 원본 대상·회귀 테스트·API fixture. 개선 검증에는 별도 실서비스 사례와 공개/공유 정상 사례가 더 필요하다.

## B. BACScan

**Fengyu Liu et al. BACScan: Automatic Black-Box Detection of Broken-Access-Control Vulnerabilities in Web Applications. ACM CCS 2025, pp.1320–1333.** [저자 원문](https://yuanxzhang.github.io/paper/bacscan-ccs25.pdf) · [코드](https://github.com/LFYSec/BACScan)

- 읽기 수준: **2차**, §1·§4.2.2·§5.1–5.4·§6·§8. 인가가 없는 상태 변화와 읽기를 분리한다.
- 한 것: 앱 탐색·요청 관계 분석·여러 권한의 요청 재생으로 읽기/수정 BAC를 검사했다. 실서비스와 공개 PoC 기반 평가가 있어 외부 데이터 후보를 찾는 데 유용하다.
- 안 한 것/한계: 전체 정상 요청 모집단을 제공하는 분류 벤치마크가 아니며, 크롤링 누락과 읽기 응답 유사성 판단에 오류가 남는다. 현재 공개판의 재현 한계는 논문 주장과 별개로 [README](https://github.com/LFYSec/BACScan/blob/456cb5195b77d9e52c57c6f1d17abfc7dc13ff74/README.md)의 “the crawler currently used in BACScan is a simplified version”에서 확인된다. 번역: 현재 공개된 crawler는 단순화 버전이다.
- 같은 점: 인증만 바꾸어 읽을 수 있다는 이유로 판단할 때 생기는 오탐 문제. 다른 점: BACScan은 상태 변경 BAC와 웹 UI 탐색까지 포함한다.
- 판정: **살림 — 실서비스 대상과 평가 설계 참고.** 전체 도구를 당장 실행 가능한 주 기준선으로 확정하지 않는다.

2차 확인: §5.1/Table 1 p.9. 14개 시험 앱과 6개 정답 앱. 알려진 정답은 PoC가 존재하는 Huntr·ExploitDB·기존 연구 사례를 수집하여 구성했으며 44개 중 읽기 20개/수정 24개다. 6개 앱의 정확한 버전과 유형별 개수는 본문 보고서에 옮겼다. 피해자 일반계정·피해자 관리자·공격자 일반계정으로 수평/수직 인가를 시험하므로 읽기 사례를 전부 BOLA로 분류해서는 안 된다.

§4.2.2 p.8은 공개 페이지를 걸러낸 뒤 GET 재생과 응답 유사성 임계값 0.7을 사용한다. 이것은 성능 70%가 아니다. Table 2 p.10의 알려진 읽기 취약점은 TP=15, FP=3, FN=5, precision=83.33%, recall=75%. 새로 발견한 읽기는 TP=21, FP=5이며 전체 FN은 모른다. Table 3 p.11에서는 알려진 20개에 새로 발견한 21개를 더한 41개를 읽기 정답으로 삼아 36/41=87.80% recall을 보고한다. 발견된 사례를 정답에 추가한 평가와 독립된 숨김 시험을 구분해야 한다.

원문 내부에도 Table 1의 신규 합계 `34+22`와 본문/Table 2의 `33+21`이 다르다. 이번 과제의 핵심 값은 일관된 알려진 정답 44개와 Table 2를 기준으로 삼았고, 신규 총수를 임의로 통일하지 않았다.

공개판은 Python·Playwright·Elasticsearch·앱별 세션 설정이 필요하다. README의 원격 예제 주소에는 요청하지 않았다. 대상 앱·PoC·fix·normal fixture를 묶은 재현 패키지는 아직 만들지 않았다.

## C. EvoMaster의 보안 검사 확장

**Omur Sahin, Man Zhang, Andrea Arcuri. Enhancing REST API Fuzzing with Access Policy Violation Checks and Injection Attacks. arXiv:2604.00702, 2026.** [원문](https://arxiv.org/pdf/2604.00702) · [EvoMaster](https://github.com/WebFuzzing/EvoMaster) · [WFD](https://github.com/WebFuzzing/Dataset)

- 읽기 수준: **2차**, §1·§5.1–5.5·§6–7·Data Availability. 읽은 판본은 저장소 PDF이며 버전·해시는 manifest에 남겼다.
- 한 것: API fuzzer에 여러 접근 정책/주입 오류 판정기를 결합하고 toy·취약 실습 API·WFD를 평가했다.
- 안 한 것: 전체 API의 모든 인가 오류에 대한 수작업 완전 정답 구성. §5.4 p.21: “We have not manually reviewed the whole code and documentation of those 8 APIs”. 번역: 8개 API의 전체 코드·문서를 수작업으로 검토한 것은 아니다.
- 같은 점: 인가 검사와 여러 사용자 상태. 다른 점: 다양한 보안 오류를 찾는 fuzzer 연구이며 BOLA 정상/비정상 분류만을 위한 평가가 아니다.
- 판정: **살림 — 외부 대상 API 목록의 근거.** 검출 건수를 우리 FPR/recall로 변환하지 않는다.

2차 확인: Table 1 p.18의 8개 대상은 capital(21 endpoints), crAPI(44), Damn-Vulnerable-RESTaurant-API-Game(21), DVAPI(16), dvws-node(31), VAmPI(14), vulnerable-rest-api(19), WebGoat(201)다. 9 toy + 8 vulnerable-by-design + 36 WFD에서 WebGoat가 중복되어 총 52개다.

§5.2에서는 취약 API와 WFD에 각각 1시간 예산, 10회 반복을 쓴다. 단순 합산으로 8×10+36×10=440시간의 탐색 예산이며 toy와 부가 비용은 별도다. 이것을 우리 Windows 환경의 예상 완료 시간으로 제시하지 않는다. 일부는 white-box 계측과 DB reset을 사용하므로 black-box Akto와 입력 조건이 다르다.

§5.4–5.5 p.21에서 취약 API와 WFD에서 F206을 찾지 못했다고 밝힌다. black-box fuzzing 중 로그인 정보를 바꿀 수 있는 endpoint가 초기 인증을 무효화하는 문제도 설명한다. 따라서 우리 읽기 평가에서는 fixture와 인증 상태를 복구하고, 인증 실패를 안전한 인가 차단으로 잘못 세지 않아야 한다.

이번에는 이 논문을 근거로 VAmPI를 선택하고 원본 책 조회 코드만 직접 검증했다. 논문 실험이 사용한 VAmPI와 이번에 받은 commit이 동일하다고 증명한 것은 아니며, 현재 확인한 commit을 별도 고정했다.

## D. BolaRay — 주 비교에서 제외한 근거

**Yongheng Huang et al. Detecting Broken Object-Level Authorization Vulnerabilities in Database-Backed Applications. ACM CCS 2024.** [저자 원문](https://leehaofeng.github.io/papers/2024-BolaRay.pdf) · [코드](https://github.com/BolaRay-d/BolaRay)

- 읽기 수준: **1차**, 제목·초록·서론·결론과 §5.5 Limitations(p.14). 평가 본문 전체를 2차 정독한 것으로 표시하지 않는다.
- 한 것: 데이터베이스 테이블 관계에서 객체 인가 모델을 추론하는 정적 분석을 제시했다.
- 안 한 것: §5.5는 “BolaRay does not consider SELECT statements as sensitive operations”라고 명시한다. 번역: SELECT를 민감 연산으로 취급하지 않는다. 이어 정보 유출 BOLA를 탐지할 수 없다고 밝힌다. PHP 지원과 수동 DAL 명세도 제약이다.
- 같은 점: 객체·소유권·연관 관계를 인가 판정에 이용. 다른 점: 우리가 우선 다루는 읽기 정보 유출이 저자 명시 범위 밖이다.
- 판정: **보류 — 개념 참고용으로 유지, 읽기 BOLA의 주 성능 비교군 제외.** 제목에 BOLA가 있다고 그대로 비교군으로 삼지 않는다.

## E. SPY

**Maksim Savkin, Timur Ionov, Vasily Konovalov. SPY: Enhancing Privacy with Synthetic PII Detection Dataset. NAACL 2025 Student Research Workshop, pp.236–246.** [원문](https://aclanthology.org/2025.naacl-srw.23.pdf) · [코드·데이터](https://github.com/LogicZMaksimka/SPY_Dataset)

- 읽기 수준: **2차**, §1·§3–7·Limitations. 생성 흐름 Figure 1, 성능 Table 3 확인.
- 한 것: 영어 법률/의료 문맥에 작성자의 개인정보와 방해 개체를 넣는 합성 데이터 및 도메인 전이 실험.
- 안 한 것: 한국어 평가, 실제 데이터 일반화 입증. Limitations p.6(출판 p.241): “we were unable to fully assess the pipeline’s transferability to real-world data.” 번역: 실제 데이터로의 전이성을 충분히 평가하지 못했다.
- 같은 점: 실제 개인정보를 모으지 않는 평가. 다른 점: SPY의 작성자 중심 정답 정책은 모든 관련자의 개인정보를 다룰 AP-EYE보다 좁다.
- 판정: **살림 — 생성·라벨 생성·외부 도메인 평가 설계 참고.** 한국어 정확도 근거로 사용하지 않는다.

§3 pp.3–4(238–239): Llama-3-70B로 문맥 생성, PII placeholder 반복 추가, Faker 값으로 치환, 작성자와 무관한 개체를 추가한다. 순서가 바뀌거나 후처리되면서 기존 placeholder가 사라질 수 있다는 한계도 Table 2에 나타난다. 생성한 문장을 마지막으로 다시 검사해야 하는 이유다.

§5 p.5(240): DeBERTaV3-base를 한 도메인에서 학습하고 다른 도메인에 시험한다. Presidio, zero-shot Llama-3-70B와 비교한다. 논문은 precision/recall/F1을 토큰 분류 지표로 설명한다. 이를 K-LegalDeID의 strict 문자-span F1과 같다고 가정하지 않는다. 코드를 실행하여 scorer 일치성을 확인한 것은 아니다.

Table 3에서 예를 들어 법률 이름의 F1은 Presidio 29.2, DeBERTa 90.2다. 이는 해당 정답 정책과 도메인 전이 설정의 값이며 ‘Presidio 일반 정확도 29.2%’가 아니다. 한국어 값만 영어 문맥에 치환해도 한국어 문맥 벤치마크가 되지는 않는다. 저장소는 Faker seed로 동적 생성을 재현하는 구조를 안내하지만 이번 생성/훈련은 실행하지 않았다.

## F. K-LegalDeID

**Wooseok Choi, Hyungbin Kim, Yon Dohn Chung. K-LegalDeID: A Benchmark Dataset and KLUEBERT-CRF for De-identification in Korean Court Judgments. EACL 2026, pp.2308–2325.** [원문](https://aclanthology.org/2026.eacl-long.103.pdf) · [저자 기관 소개](https://pure.korea.ac.kr/en/publications/k-legaldeid-a-benchmark-dataset-and-kluebert-crf-for-de-identific/)

- 읽기 수준: **2차**, §1·§4.1–5.4·§6–7·Limitations. Tables 1–3 확인.
- 한 것: 한국어 법률/SNS 문맥의 PII 데이터 구성과 KLUEBERT-CRF의 경계·유형 평가.
- 안 한 것: 비식별 전의 원본 판결문으로 실제 환경 성능을 검증하는 것. 데이터 간 주석 불일치도 한계다. §5.3 p.7(2314): “our approach employs a different annotation scheme and data processing methodology.” 번역: 다른 주석 체계와 데이터 처리 방법을 사용한다.
- 같은 점: 한국어 합성 대체값·정확한 개인정보 경계가 중요. 다른 점: 법률 비식별화와 API 사용자별 인가는 목적·정답 정책이 다르다.
- 판정: **살림 — 한국어 생성·라벨·평가 방법의 주요 논문.** 데이터 즉시 사용 가능 여부는 미확인.

§4.1 pp.3–5: 법률 39분야의 판결문 2,000건에서 46,973개 주석 문장을 만들고 대체값을 넣은 문장 인스턴스 138,576개를 구성한다. SNS 908,422개와 Thunder-DeID 45,000개(4,500×10)를 결합하여 총 1,091,998개다. 원문 수·문장 수·증강 수를 혼동하지 않는다. 11개 유형은 name/address/number/bank name/account number/security code/school/company/URL/email/ID다. 자동 생성만으로 모든 의미 라벨이 정해진 것이 아니며, 8명 주석자의 일치도 κ=0.7352를 보고한다.

§5.1–5.4 pp.6–8: 증강 Thunder 원문 문장 단위로 70/20/10 분리하는 설명을 확인했다. 이를 모든 데이터가 판결문 사건 단위로 완전히 분리되었다는 보장으로 확대하지 않는다. strict entity F1은 **경계와 유형 모두 일치**를 요구한다. Table 1 결합 평가 0.9923, Table 2 Court+SNS → Thunder 전이 0.3658, Table 3 Thunder를 학습에 포함한 뒤 Thunder 시험 0.9928이다. 마지막 값을 독립된 미지 도메인 일반화 성능이라고 쓰면 안 된다.

원문·기관 페이지·[Responsible NLP Checklist](https://aclanthology.org/attachments/2026.eacl-long.103.checklist.pdf)를 확인했지만 이번 조사에서는 바로 다운로드할 저자 데이터/코드 링크를 확보하지 못했다. ‘논문 공개’와 ‘재현 자산 확보’를 구분한다.

## G. Thunder-DeID

**Sungeun Hahm et al. Thunder-DeID: Accurate and Efficient De-identification Framework for Korean Court Judgments.** [읽은 원문: arXiv:2506.15266v3](https://arxiv.org/pdf/2506.15266v3), 2025-10-16 · [학회 출판 기록: Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.682/)

- 읽기 수준: **2차**, v3 §1·§3.1–3.8·§4.1–4.2·§5·Limitations. 쪽 번호와 수치는 **arXiv v3**를 기준으로 한다. 학회 최종 PDF와 전체 내용이 동일하다고 확인한 것은 아니다.
- 한 것: 가림표지가 있는 법률 문서를 사람이 유형별로 주석하고 실제 형식에 맞는 대체 목록을 넣어 학습·평가. 형태소+BPE로 조사와 개체 경계 분리.
- 안 한 것: 비식별 전의 실제 판결문 성능. Limitations p.10: “This limitation prevents us from evaluating our model’s performance in real-world settings.” 번역: 이 제약으로 실제 환경의 모델 성능을 평가할 수 없다.
- 같은 점: 한국어 값과 조사의 경계, 합성 대체값 평가. 다른 점: 법률 문맥의 매우 세분화된 729라벨은 우리 API용 최소 유형과 일치하지 않는다.
- 판정: **살림 — 생성/주석 방법 참고, 접근 가능한 배포본 확인 전 실험 데이터 채택 보류.**

§3 pp.3–7: v3는 중복을 제거한 민사 3,000/형사 3,000/행정 700문서, 총 48,306개 entity를 17명이 주석했다고 설명한다. 729라벨의 대체 목록 중 691개는 공개 자료를 선별 수집하고 구조화된 식별자는 규칙으로 생성한다. 따라서 대체 목록의 모든 고유명이 무작위로 합성된 것은 아니다. 우리 합성 평가에는 실인물·실기관과 결합되지 않는 대체값을 사용한다.

§4 pp.7–9: 문서 단위 80/10/10, 3 seeds(1200/1203/1205), single replacement와 per-epoch replacement 비교. Table 2의 최고 이진 token F1 0.9808과 유형 token micro F1 0.9105는 서로 다른 모델 크기의 값이며 exact entity F1이 아니다. 공식 소개 페이지의 예전 점수/크기와 혼합하지 않는다.

접근성 점검: [공식 데이터 페이지](https://champ.snu.ac.kr/datasets-deid)의 소개는 4,500문서·595유형이다. 연결된 [판결문 자산](https://huggingface.co/datasets/thunder-research-group/SNU_Thunder-DeID-annotated_court_judgments), [대체 목록](https://huggingface.co/datasets/thunder-research-group/SNU_Thunder-DeID-list_of_entity_mentions)은 이번 비인증 도구 요청에서 401, [코드](https://github.com/mcrl/SNU_Thunder-DeID)는 404가 반환됐다. 삭제·비공개·권한 제한 중 원인은 확정하지 않았다. v3의 6,700/729와 이 소개의 4,500/595를 동일한 배포본으로 취급하지 않는다.

## H. K-PII-Bench — 논문과 분리한 공개 자산 점검

[작성자 저장소](https://github.com/woohyun212/k-pii-bench) · [데이터 카드](https://huggingface.co/datasets/woohyun212/k-pii-bench)

- 읽기 수준: **원문 미확인**. README, 평가 프로토콜, 공개 Dataset Viewer 표본을 확인했다. 읽지 못한 논문의 방법/성능을 추정하지 않는다.
- 카드/README의 주장: 한국어 합성 300,000문서, 18유형·12도메인, train 243,711/dev 28,147/test 28,142, template skeleton 분리. 데이터 CC BY 4.0, 코드 Apache 2.0 표시.
- 직접 확인: 비인증 API로 split 목록과 첫 표본 126문서 접근. 541개 span의 문자열 일치 확인. 모델 성능·전수 분할 중복·문맥 품질을 검증한 것은 아니다. 표본 안에서는 토큰/태그 길이 불일치와 split 간 template ID 교집합이 없었다. 편의 표본이므로 전체 보장은 아니다.
- 중요한 한계: README는 DOI를 추후 넣겠다고 명시한다. 실제 표본에는 문맥과 대체값의 의미가 맞지 않는 사례도 있다. 기술적으로 내려받을 수 있다는 이유만으로 논문 수준의 정답 품질이 보장되지 않는다.
- 판정: **조건부 살림 — 외부 한국어 합성 시험 후보.** 논문 근거는 F/G/E에서 가져오고, 이 자산은 독립 품질 점검 이후 사용한다.

## 채택 관계

AuthProbe와 VAmPI는 외부 기능 재현, BACScan은 실서비스 후보 확보, SPY는 완전 합성 생성 흐름, K-LegalDeID/Thunder-DeID는 한국어 주석·평가, K-PII-Bench는 접근 가능한 외부 합성 문맥 후보로 역할을 나눈다. 이 조합은 AP-EYE의 새로움이나 우수성을 증명한 결과가 아니라 **그 주장을 시험할 수 있게 만드는 외부 기준 제안**이다.
