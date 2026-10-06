# 한국어 PII 평가 설계 독립 보강

조사·실행: 2026-10-06. 대상: AP-EYE 태스크 2·4. 기존 보고서를 고치지 않고 추가 근거와 감사 결과를 분리했다. 논문 원문, 저자 데이터 카드, 공개 소스와 실제 로컬 실행을 구분한다.

## 결론

기존 방향에서 **한국어 합성 평가와 외부 데이터 우선 원칙은 유지**하되, K-PII-Bench 하나에 기대는 설계는 보완해야 한다. 공개 외부 규칙 기준선 `ko-pii`와 그 합성 평가 자료를 확보했고, 540문서를 직접 실행하여 저자 점수를 재현했다. 동시에 점수가 채점 방식에 크게 의존하며, 정상 음성 사례와 반복 개체의 평가가 부족하다는 사실도 확인했다.

AP-EYE의 기여를 ‘한국어 PII를 처음 지원한다’로 잡으면 안 된다. Presidio에는 이미 한국 식별자 인식기가 있고, ko-pii에는 한국어 규칙·사전·형식 검사가 있다. 더 설득력 있는 질문은 **API의 키와 값, 한국어 자유서술, 비인가 객체의 반환을 함께 볼 때 기존 구성의 어떤 오탐·미탐이 줄어드는가**다. PII 분류와 인가 위반은 별도 정답으로 두고, 한국어 PII가 없는 BOLA도 놓치지 않아야 한다.

## 1. 바로 사용 가능한 외부 자산과 채택 판단

| 자산 | 실제 공개 상태·생성/라벨 | 이번 판단 |
|---|---|---|
| [ko-pii generated_eval](https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/data/generated_eval.README.md) | 원본 JSONL 540문서·3,635 gold 항목·26유형 확보. LLM 합성 문맥/값, 자동 형식 검사와 LLM 검토. 사람 검수 정답은 아님. 저장소 MIT 표시 | **채택: 외부 개발·회귀 자료와 한국어 규칙 기준선.** 반복 문자열의 위치 gold를 추가 검수하기 전 strict span 시험의 정답으로 바로 사용하지 않음 |
| [K-PII-Bench](https://huggingface.co/datasets/woohyun212/k-pii-bench) | 300,000문서, 18유형, 12도메인이라는 작성자 카드. 공개 수정판의 문자 span·BIO 제공. 기존 126문서/541개체 표본 재감사 | **조건부 채택: 원형 분리/강건성 설계 참고, 독립 품질 검수 후 시험군.** 현 표본에는 PII가 없는 문서가 없고 의미 불일치가 있음 |
| [OpenPII 1.5M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m) | 작성자 카드 1,636,375문서·30언어·19라벨, 한국어 포함, CC BY 4.0. 직접 확보한 126개 혼합 언어 표본 중 한국어 16문서/113개체 확인 | **보류: 다국가 형식·다른 생성기 스트레스 자료 후보.** 한국어 표본의 부자연스러운 이름·전화 형식·문맥 오류, 전체 한국어 수/독립 split 미확인 |
| [Gretel synthetic finance](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual) | 55,940문서, 원본은 영어·스페인어·스웨덴어·독일어·이탈리아어·네덜란드어·프랑스어. LLM 생성→NER 주석/검사→LLM 평가·일부 사람 점검 | **한국어 주평가에서 제외.** 원본에 한국어 없음. 제3자의 `-kr` 번역본은 번역/재주석 자산으로 별도 심사해야 함 |
| [KDPII revised](https://zenodo.org/records/16759166) | 공식 기관 배포 v2는 원본 train/dev/test를 합친 revised 자산이며 split이 없다고 명시 | **합성 주평가 보류.** 이번에 완전 합성임을 원문으로 확인하지 못함. 원래 test와 revised를 혼동하지 않으며 라벨 체계 참고용 |
| K-LegalDeID / Thunder-DeID | 기존 원문 기록대로 비식별 법률 문맥의 가림 부분 대체. 배포본 접근·논문 판본 일치가 해결되지 않음 | **생성·주석 방법 채택, 즉시 실행할 외부 데이터 확정은 보류** |

자료가 외부에서 왔다는 것과 독립된 최종 시험군이라는 것은 다르다. 이미 열어 보고 오류 분석한 표본은 개발·감사 표본으로 기록하고, 개선 도구를 만들기 전에 보지 않은 문서/원형을 별도 동결해야 한다. ko-pii 작성자 자신의 합성 자료는 AP-EYE에는 외부 자료지만 ko-pii의 독립 제3자 성능 평가라고 부르지 않는다.

## 2. 직접 실행한 한국어 규칙 기준선

원본 [ko-pii commit](https://github.com/Marker-Inc-Korea/ko-pii/tree/9516cabd6f582935cae1536ccbd8c5448afae679)을 별도 디렉터리에 고정했다. Python 표준 라이브러리 기반 `detect_all`만 오프라인 실행했다. 외부 모델/API·GPU·유료 호출은 사용하지 않았다.

| 같은 540문서·같은 예측, person_min_length=3 | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| 저자 canonical substring-set scorer | 2,832 | 733 | 771 | 0.79439 | 0.78601 | **0.79018** |
| 더 엄격한 exact-surface-set 진단 채점 | 2,382 | 1,183 | 1,219 | 0.66816 | 0.66148 | **0.66481** |

첫 행은 저자 보고 0.790을 재현한다. 두 번째 행은 우리가 추가한 진단이다. **둘 다 문자 위치를 포함하는 strict entity-span F1이 아니다.** 같은 문자열이 여러 번 나오면 set으로 합쳐지며, 첫 행은 부분 문자열도 맞았다고 처리한다. 원본 scorer는 `TP`를 *매칭된 예측 문자열 수*, `FN`을 *매칭되지 않은 gold 문자열 수*로 계산하고 한 예측↔여러 gold 또는 여러 예측↔한 gold 매칭을 허용한다. PERSON 길이 필터도 적용하므로 원시 gold **3,635항목**과 첫 행의 `TP+FN=3,603`을 같은 gold 분모로 해석하면 안 된다. 정확한 경계를 평가하면 결과가 크게 달라질 수 있다는 증거다. [scorer 원본](https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/src/ko_pii/eval/kdpii.py)

| 유형 | substring-set F1 | exact-surface-set F1 | 해석 |
|---|---:|---:|---|
| 이메일 | 0.99756 | 0.99756 | 표면 문자열 경계 차이가 작음 |
| 전화 | 0.98925 | 0.98925 | 이 자료의 정형 전화에서 강한 규칙 기준선 |
| 주민번호 | 0.95739 | 0.95739 | 형식·문맥·버전별 유효성 기준은 별도 검토 필요 |
| 이름 | 0.59938 | 0.59454 | 문맥형 인명의 오탐·미탐 개선 여지 |
| 계좌 | 0.95890 | 0.65753 | 부분 문자열 매칭과 전체 값 경계 차이 |
| 주소 | 0.96552 | 0.16561 | 부분 주소만 찾아도 인정하는 점수와 전체 값 일치가 크게 다름 |

주소 값은 주소 전체/행정구역/상세주소를 어떤 단위로 보호할지에 따라 gold가 달라진다. 0.16561을 다른 논문의 strict span 점수와 같은 지표로 순위 매기면 안 된다. 이번 진단은 **채점 계약을 먼저 고정해야 한다는 근거**다.

### 데이터 자체 감사

- 540문서 모두 읽음. 실제 gold 항목 3,635개, 26유형. gold 문자열이 본문에 없는 항목 0개, 문서 완전 중복 0개.
- **빈 gold 문서는 실제 19개**다. README의 18개와 다르므로 고정 파일의 실행값을 사용한다.
- 220개 gold 항목은 본문에 같은 문자열이 두 번 이상 나오며, 해당 문서는 160개다. 위치를 자동으로 첫 번째 출현에만 붙이면 정답을 손상시킨다.
- 19개 빈-gold 문서 중 원본 도구가 하나 이상의 결과를 낸 문서는 **15개**다. 제안한 핵심 6유형(PERSON/PHONE/EMAIL/ADDRESS/RRN/ACCOUNT)만 남겨도 **12개**다. 이는 해당 소규모 자료의 문서 경고율이며 전체 한국어 FPR 추정값이 아니다.
- 오류 예: 행 번호 504의 `주문번호`를 PERSON, 510의 수강 시작 날짜를 DT_BIRTH, 512의 환불 ‘수단’을 NATIONALITY로 잡음. 반면 479·519의 IP 탐지는 ‘PII 형태 인식’과 ‘이 문맥에서 개인의 보호 대상임’의 정책 차이도 포함하므로 전부 형식 탐지 오류라고 부르면 안 된다.
- 3자 미만 PERSON을 제외하는 저자 설정도 정책 선택이다. AP-EYE는 두 글자 이름을 무조건 배제하지 말고 전체 gold 평가와 비교 재현 설정을 별도로 보고해야 한다.

**실행 증거:** [전체 감사·유형별 confusion count](evidence/ko-pii-full-audit-and-baseline.json), [실행 스크립트](scripts/audit_and_baseline.py), [실행 로그](evidence/audit-and-baseline.log), [재현 절차와 입력 의존성](REPRODUCTION.md). 시간 값은 단발 로컬 감사 측정이며 성능·처리량 벤치마크로 제시하지 않는다. 독립 사람 검수·Akto 동시 비교·NER 비교는 `NOT_RUN`.

## 3. K-PII-Bench에서 기존 형식 검사를 넘어 확인한 것

고정 코드 commit: `1b480c515cc8425ea5c5675079bd7cf17b951554`.

### 공개 수정판과 원고 수치를 섞지 말 것

[DATASHEET Corrected Release](https://github.com/woohyun212/k-pii-bench/blob/1b480c515cc8425ea5c5675079bd7cf17b951554/DATASHEET.md)에 따르면 원고 실험에 사용한 내부 snapshot에는 약 35,483개 span/label 불일치, 약 4,182개 미치환 placeholder, 원형 분할 문제가 있었고 공개판에서 수정했다. 이는 **작성자의 수정 내역**이며 우리가 원래 오류 전부를 재현한 것은 아니다. gold와 split이 달라진 공개판에 과거 원고의 점수를 붙일 수 없다. 원고 DOI/원문은 기존 조사처럼 미확인이다.

### 직접 재감사한 범위

기존 HF first-rows 표본 126문서/541개체에서 다음을 실행했다.

- 문자 offset/표면 문자열 일치와 token/BIO/offset 길이 검사 통과.
- 문자 gold로 토큰 BIO를 독립 재계산하여 제공 BIO와 비교: 불일치 0.
- 표본 내 완전 문서 중복 0, split 사이 정규화 template 동일 0, SequenceMatcher 0.90 이상 near-template pair 0. 전체 300,000문서 무누수를 증명하지 않는다.
- PII 없는 문서 **0개**, 18유형 중 **17유형만 관찰**. 이 표본으로 전체 negative 오탐률이나 모든 유형 성능을 측정할 수 없다.

내용의 의미는 별개다. 다음은 표본을 읽어 찾은 구체적 오류 후보이며, 독립 사람 이중 주석의 오류율로 제시하지 않는다.

| 위치 | 확인한 내용 | 왜 문제가 되는가 |
|---|---|---|
| train row 2, D6374abd2f | ‘강사 등록 번호’ 위치에 NRP의 종교명이 들어감 | 번호 문맥과 민감 속성 라벨의 의미 불일치 |
| dev row 22, D18da97db6 | 예정된 ‘미팅 날짜’ placeholder가 DATE_OF_BIRTH | 일반 일정과 생년월일 구분을 학습·평가할 때 오답 gold가 됨 |
| train row 22, D047b39470 | 세금 납부 번호 placeholder가 KR_NHIS | 납부 번호와 건강보험 식별자의 문맥 충돌 |
| train row 0 및 여러 문서 | 명사 뒤 기존 조사와 자동 추가 조사가 어색하게 결합 | 조사 경계가 형식적으로 맞아도 자연스러운 한국어 분포를 보증하지 않음 |

근거: [정량 감사 JSON](evidence/kpii-deep-sample-audit.json), [고정 표본의 문맥 검토 입력](evidence/kpii-context-review-input.json). 외부 test 표본을 검토했으므로 그 표본은 이후 개선판의 숨김 최종 시험에서 제외하거나 감사에 사용했음을 공개해야 한다.

### scorer 이름만 믿으면 안 됨

공식 `k-pii-bench-eval`은 [evaluate.py](https://github.com/woohyun212/k-pii-bench/blob/1b480c515cc8425ea5c5675079bd7cf17b951554/src/k_pii_bench/evaluation/evaluate.py)의 seqeval BIO 채점을 연결한다. 같은 저장소의 별도 [span_metrics.py](https://github.com/woohyun212/k-pii-bench/blob/1b480c515cc8425ea5c5675079bd7cf17b951554/src/k_pii_bench/evaluation/metrics/span_metrics.py)는 `strict`라는 이름으로 `(type, surface)` set을 비교하고 offset을 사용하지 않는다.

같은 이름이 두 번 있는 gold에서 한 번만 찾은 합성 반례를 이 helper에 실행하자 strict recall/F1=1.0이었다. occurrence 기반 gold라면 recall=0.5, F1=0.6667이다. **이는 해당 helper의 동작이며 공식 BIO scorer 전체가 틀렸다는 주장은 아니다.** 또한 프로토콜의 `--gold/--pred` 예시와 현재 CLI의 `--ground_truth/--prediction/--output` 인자도 다르다. 재현 시 함수·입력 단위·인자·version까지 고정해야 한다. [직접 probe 결과](evidence/kpii-scorer-probe.json)

## 4. 다국가 PII는 어떻게 하는가 — 방법과 수치 해석

| 방법·출처 | 다국가 처리 방식 | 한국어 비교에 적용할 점 |
|---|---|---|
| [Presidio 지원 유형](https://presidio.dataprivacystack.org/supported_entities/) | 국가별 형식·문맥·checksum/custom logic + 일반 이름/장소 NER. 예: 영국 NHS, 스페인 NIF, 인도 Aadhaar 등 | 국가 코드/언어/recognizer 활성화와 NER 모델을 별도 고정. 최신 엔진에 한국 규칙이 있다는 것과 Akto 기본 영어 설정에서 실제 활성화된다는 것은 다름 |
| [Presidio 한국 인식기 소스](https://github.com/data-privacy-stack/presidio/tree/d8847904621733f4eaad4f9bd977b96a11325c90/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/korea) | KR_RRN, KR_FRN, KR_PASSPORT, KR_DRIVER_LICENSE, KR_BRN | 단순 한국 번호 regex 추가만으로 신규 연구라고 주장할 수 없음. 한국어 자유서술과 API 필드 문맥의 오류를 측정 |
| [GLiNER2-PII 원문](https://arxiv.org/pdf/2605.09973) | 제약 조건으로 LLM 합성 문맥/라벨을 만든 뒤 span 모델 학습. 학습 7언어는 EN/FR/ES/DE/IT/PT/NL | 한국어 학습·성능 증거 없음. 공개 모델은 추가 ML 기준선 후보이나 한국어 보장 근거는 아님 |
| SPY | 영어 문맥에 여러 locale의 Faker 값을 삽입하고 방해 개체 추가 | 형식 다양성은 참고하되 영어 문맥을 한국어 평가라고 부르지 않음. 작성자 중심 gold 정책을 그대로 이식하지 않음 |
| OpenPII 1.5M | 한국 포함 여러 locale의 합성 문맥·값·BIO 제공 | 언어 metadata와 실제 국내 형식 적합성은 별개. 기본 유형이 같아도 이름 분할/주소 구성/번호 형식의 gold 매핑 필요 |

**국가별 정확도를 한 숫자로 비교할 근거는 확보하지 못했다.** 언어, 데이터, 라벨, decoder, threshold, 표본 추출과 scorer가 같지 않은 논문/카드 점수를 합쳐 국가별 순위표를 만들지 않는다.

GLiNER2-PII는 이번에 원문 **2차 읽기**(§1·§3–6, PDF pp.1–5)를 했다. Table 2의 SPY legal/medical 평균 F1은 **0.471**이고 현재 모델 카드의 **0.477**과 다르다. 둘의 모델/데이터 revision 동일성은 미확인이다. 논문이 평가 SPY를 자연 발생 자료처럼 기술하지만 SPY 원문은 합성 생성 절차를 설명한다. 그러므로 이 결과를 ‘실제 한국어 데이터에서 검증’한 증거로 쓸 수 없다. 학습 데이터 사람 검증 부재와 제한된 평가 도메인도 저자가 밝힌 한계다.

## 5. OpenPII와 Gretel을 추가로 확인한 결과

OpenPII 조회 당시 HF repository revision은 `a785eb528e28be2693c3718a27e066970de5dadb`다. Viewer 표본 요청 자체를 revision으로 고정하지 않았으므로 실제 감사 입력은 저장한 JSON과 조회 시점으로 식별한다. train/validation 첫 표본 60+66개 중 한국어 6+10개가 실제 포함되었다. 한국어 113개 span의 offset은 모두 일치했지만 한국어 negative는 0개였다. `GIVENNAME/SURNAME`을 합친 PERSON이나 `CITY/STREET/BUILDINGNUM/ZIPCODE`를 합친 ADDRESS로 자동 변환하면 단위가 달라질 수 있다.

표본에는 한국어 문장 속 매우 부자연스러운 이름, 국내 전화와 맞지 않는 모양, ‘최소 투자 금액’에 들어간 CARD 라벨 등 문맥 품질 문제가 보인다. 전체 오류율을 산출한 것은 아니다. HF `/filter`와 `/rows`는 HTTP 500을 반환하여 한국어 전량/무작위 표본은 확보하지 못했고, `/first-rows`에서 읽은 범위를 명시했다. [감사 JSON](evidence/openpii-korean-audit.json), [표본 검토 입력](evidence/openpii-korean-review-input.json), [요청·실패 기록](evidence/openpii-pages-manifest.json)

Gretel 원본의 한국어 지원은 확인되지 않은 정도가 아니라 **카드의 언어 목록과 실제 파일 목록에 한국어가 없다.** 또한 본문 train/test 50,776/5,164와 metadata의 50,346/5,594가 다르다. 원본 외국어 synthetic 문서 생성·검증 방법 참고용으로 보류하고, 제3자 번역본을 사용하면 번역 후 문자 offset·라벨 전수 검증과 별도 source/revision을 요구한다. 이 원본은 개인정보 정답을 NER로 보완하므로 해당 NER와의 비교에는 생성기/주석기 편향도 명시해야 한다. [고정 metadata](evidence/gretel-meta.json), [데이터 카드](evidence/gretel-card.md)

## 6. 추가 논문 원문 — 무엇을 가져오고 무엇을 제외하는가

### PII-Bench: Evaluating Query-Aware Privacy Protection Systems — ACL 2026

[원문](https://aclanthology.org/2026.acl-long.227.pdf). **2차 읽기:** Abstract/§1/§5/Limitations 후 §3.1–3.4·§4.1, PDF pp.3–6. 생성은 규칙형 식별자와 LLM형 문맥/개체를 조합하고, 주체 간 관계·질문 관련 개체를 별도로 구성한다. 5명 전문 주석자와 저자가 검토했다고 기술한다. PII-single 1,214, multi 1,228, hard 200, distract 200의 구조다. hard는 앞 집합에서 골라 만든 것이라고 하므로 2,842를 독립 문맥 2,842개로 단순 간주하지 않는다.

Strict-F1은 주체·유형·span을 함께, Ent-F1은 개체 경계만 평가한다. **개체 발견/누구의 정보인지/왜 필요한지를 분리**하는 설계는 AP-EYE에 유용하다. 그러나 질문에 필요하다는 것은 API 사용자가 조회할 권한이 있다는 뜻이 아니다. 요청자의 인가 정책을 질문 관련성으로 대신할 수 없다. 원문/학회 페이지에서 즉시 내려받을 저자 dataset/code 링크는 이번에 확보하지 못했다. 데이터 실행 `NOT_RUN`, **평가 설계만 채택**.

### PIIBench: A Unified Multi-Source Benchmark Corpus — arXiv:2604.15776

[원문](https://arxiv.org/pdf/2604.15776). **1차 읽기:** 제목·초록·§1·§6–7. 바로 위 PII-Bench와 다른 저자/다른 연구다. 여러 corpus와 라벨을 통합했지만 §6.2는 영어 레코드만 사용한다고 명시한다. 한국어 주평가군에서 **제외**, label schema 정규화의 참고로만 보류. 상세 실험·저자 scorer는 이번에 실행/정독하지 않았으므로 초록의 F1을 한국어 성능으로 사용하지 않는다.

### Subject-level Inference for Realistic Text Anonymization Evaluation (SPIA) — ACL 2026

[원문](https://aclanthology.org/2026.acl-long.778.pdf), [저자 저장소](https://github.com/maisonOP/spia). **1차 읽기:** 제목·초록·§1·§7·Limitations/Reproducibility. 개체 span을 가렸다는 것과 인물의 속성을 추론할 수 없다는 것은 다르며 여러 주체를 따로 평가해야 한다는 연구다. 한국어 생략 주어·존대가 만드는 어려움을 한계에서 직접 언급한다. 영어만 평가한 연구이므로 한국어 점수 근거로 쓰지 않는다.

**현재 핵심 범위에서는 보류.** AP-EYE가 탐지·인가 진단을 목표로 한다면 추론 공격 방어·완전 익명화까지 성과로 약속하지 않는다. 향후 확장할 때만 주체별 잔존 위험 평가를 검토한다. 원문은 확보/변환했지만 원문 모든 평가 절과 저장소 실험은 `NOT_RUN`/미정독.

새 PDF·Markdown은 저장소 [docs/papers](../../../../papers)에, 페이지별 추출과 SHA-256은 [원문 manifest](evidence/new-papers-manifest.json)에 보관했다. 저장소의 paper-reading/to-markdown 절차와 HF Dataset Viewer 스킬을 적용했다. 표·수식 자동 변환본을 평가 수치의 기준으로 쓰지 않았다. [재현 절차와 입력](REPRODUCTION.md)

## 7. AP-EYE용으로 확정할 평가 계약

### 정답을 세 층으로 분리

1. **형태/개체:** `(doc_id, start, end, type)`와 반복 출현별 고유 ID. 이름, 전화, 이메일, 주소, 주민번호, 계좌를 우선 공통 유형으로 매핑한다.
2. **개인과의 관련성/보호 정책:** 어떤 주체의 정보인지, 개인 연락처/공개 대표 연락처인지, 목적상 보호 대상인지. 공개 정보도 같은 형태의 개체일 수 있다.
3. **API 인가:** `(principal, object, operation, policy_version)`의 allow/deny와 실제 응답 객체/필드. 1·2층만으로 BOLA를 확정하지 않는다.

PII 존재=true를 BOLA=true로 라벨링하지 않는다. 이 구분은 ko-pii empty-gold IP와 K-PII의 IP positive가 충돌하는 것처럼, 데이터마다 암묵적으로 다른 목적을 통합할 때 특히 필요하다.

### 자료의 역할

- **개발·형식 회귀:** ko-pii 540 + 감사한 K-PII/OpenPII 표본. 이번에 본 자료는 개발에서 사용했다고 기록한다.
- **외부 숨김 시험:** K-PII 수정판의 아직 보지 않은 원형/도메인에서 품질 승인한 문서를 고정. 저자 split을 보존하고, 사후 수정 gold는 원본 대비 patch와 별도 버전을 공개한다.
- **독립 생성기 시험:** OpenPII 한국어 후보는 의미/국내 형식 검수 후 작은 독립 시험군으로 사용. 품질 미달이면 버리고 외부 문맥 구성 원칙을 따른 독립 합성 세트를 별도 구축한다.
- **API 표면 시험:** 문자열 본문과 JSON leaf/key+value를 구분. key 힌트 있음/없음, `phone` 대 `연락처`, 일반 날짜 대 생일, 13자리 주문번호 대 주민번호, 공개/공유 객체를 고정된 변형군으로 둔다. 변형 전후 원형은 같은 split 안에 둔다.
- **음성 시험:** 문서 전체가 정상인 자료와 한 문서 안의 distractor를 둘 다 포함한다. 테스트의 양성 비율을 공개하며 운영 트래픽과 같다고 가정하지 않는다.

### 비교군과 지표

비교군은 **Akto 고정 원본 → 한국 recognizer를 활성화한 Presidio → ko-pii 고정 규칙 → 한국어 NER/제안 방식**으로 구성한다. Akto 필드 분류는 field macro F1, span을 내는 도구는 strict `(doc, start, end, type)` entity P/R/F1으로 나누고 두 출력을 억지로 같은 지표에 넣지 않는다.

주 지표는 유형별 P/R/F1과 exact entity micro/macro F1이다. negative document의 ‘하나라도 잘못 탐지’ 비율과 1,000자당 FP도 병기한다. 전체 정확도 또는 O-token 비중에 지배되는 token accuracy를 주지표로 쓰지 않는다. 반복 출현 중 하나라도 누락한 민감 개체의 비율, 유형 혼동, 부분 경계 오류도 별도 집계한다.

최종 수치 목표는 이번 ko-pii 0.790을 복사하지 않는다. 이 값은 개발 감사 자료·substring set 기준이다. **동일한 숨김 시험/동일 라벨/동일 경계 채점에서, 고정 정밀도 조건의 유형별 재현율 개선 또는 고정 재현율 조건의 오탐 감소**를 목표로 정의한다. 최소 개선 폭은 개발 세트 기준선을 측정하고 시험을 열기 전에 동결한다. 문서/원형 단위 bootstrap을 사용하고, 희소 식별자는 분모를 함께 보고한다.

실제 최종 한국어 NER 학습, Akto end-to-end와의 동일 자료 비교, hidden test 동결, 사람 이중 주석은 아직 수행하지 않았다. 이것을 미완료로 명시하는 것이 현재 증거에 맞다.

## 8. 한 줄 정의의 PII 부분 수정안

> 기존 Akto는 API 응답 필드의 민감정보 분류와 인증 교체형 인가 테스트를 제공한다. 우리는 한국어 자유서술과 JSON 응답에서 일반 번호·공개 정보·개인 식별정보가 섞이고 여러 소유자의 객체가 반환되는 상황을 대상으로, 개인정보 유형·경계와 객체 인가 근거를 구분하여 진단하며, 외부 합성 자료를 검수한 숨김 시험과 취약·수정 API 쌍에서 유형별 exact F1·정상 문서 오탐률·읽기 BOLA 재현율 및 판정 커버리지로 평가한다.

이 문장은 목표와 평가 계약이다. 제안 방식의 우월성·독창성은 아직 입증되지 않았으며, 읽기 BOLA 정답과 한국어 PII 정답을 각각 검증한 뒤 결합 효과를 측정해야 한다.
