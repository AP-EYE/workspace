# PII 문헌·평가 자료 읽기 기록

기준: 2026-10-06. 원문 PDF와 공개 benchmark 문서를 구분한다. 아래 성능은 **저자 보고**이며 AP-EYE 재현 실험은 NOT_RUN이다. 논문의 데이터 정의를 개인정보의 보편적인 법적 정의로 사용하지 않는다.

## 1. SPY: Enhancing Privacy with Synthetic PII Detection Dataset

- 저자: Maksim Savkin, Timur Ionov, Vasily Konovalov. NAACL 2025 Student Research Workshop, 인쇄 pp.236–246.
- 원문: [ACL Anthology PDF](https://aclanthology.org/2025.naacl-srw.23.pdf). 로컬 `sources/references/SPY_2025.naacl-srw.23.pdf`.
- 읽기 수준: 1차(초록·도입·결론·한계) 후 2차(§3 데이터 생성, §5 실험, §6 결과·표 3, §7·Limitations). Appendix의 모든 prompt를 실행한 것은 아니다.

문제는 이름·이메일이라는 형태와 문맥상 보호해야 할 개인정보가 같지 않다는 점이다. 저자들은 글쓴이의 정보와 공개된 타인의 정보를 구분하는 합성 benchmark를 만든다. Llama-3-70B가 문맥과 placeholder를 생성하고 Faker가 값을 채운다. 법률 4,197문서, 의료 4,491문서이며 7유형을 다룬다. 생성 절차는 pp.238–239에 있다. 반복 생성 중 이전 placeholder가 사라지는 현상도 보고한다.

평가·결과는 p.240 표 3에 있다. Presidio·Llama-3-70B의 zero-shot과 반대 도메인으로 학습한 DeBERTa를 비교하므로 동일 학습 비용의 제품 대결로 읽지 않는다. 의료 문서의 이름 F1은 28.2/67.6/87.8, 이메일은 53.4/91.8/98.5, 전화번호는 47.6/89.9/95.0이다. 순서는 Presidio/Llama/DeBERTa다. 국가별 주민번호·한국어 성능표는 아니다.

한계(p.241): 합성 자료의 실제 데이터 전이를 충분히 검증하지 못했고, 데이터 생성·평가가 현실의 모든 개인정보 문맥을 포괄하지 않는다. 높은 수치를 실제 운영 recall로 옮길 수 없다. AP-EYE에는 공개 연락처·업무 계정·타인 소유 정보처럼 **PII 정책이 다른 정상 사례**를 포함하는 설계가 유용하다.

## 2. GLiNER2-PII: A Multilingual Model for Personally Identifiable Information Extraction

- 저자: Urchade Zaratiana, Ash Lewis, George Hurn-Maloney, Fastino Labs.
- 원문: [arXiv 2605.09973v1](https://arxiv.org/pdf/2605.09973v1). 로컬 `GLiNER2_PII_2605.09973.pdf`, 6쪽.
- 읽기 수준: 1차 후 2차, §1–6 및 표 2. 모델 다운로드·추론·fine-tuning은 NOT_RUN.

0.3B 모델을 42 PII label로 확장하고, 4,910개 합성 문서로 학습한다. 명시된 언어는 영어·프랑스어·스페인어·독일어·이탈리아어·포르투갈어·네덜란드어다. 한국어 검증 근거로 사용하지 않는다.

§4와 표 2(p.4)는 SPY 법률/의료 각 100문서에서 label과 문자 경계를 모두 맞춰야 하는 exact span 평가다. 서로 다른 label을 공통 7유형으로 매핑한다. GLiNER2-PII의 법률 P/R/F1은 .354/.722/.475, 의료는 .355/.681/.467이다. 평균 F1 .471은 다른 비교 모델의 .368–.391보다 높지만 precision은 약 .35이므로 과잉 마스킹까지 고려해야 한다. SPY 원 논문의 전체 평가 수치와 직접 비교하지 않는다.

논문의 포럼/의료 문서 설명은 원 SPY의 합성 생성 절차와 함께 읽는다. 현실 트래픽에서 추출한 사람 라벨 benchmark라고 소개할 근거는 없다. 저자 자체 비교이며 독립 재현·한국 API 문서 검증은 별개다. AP-EYE에는 exact span, label mapping, 같은 test set, precision/recall 동시 보고 방식이 참고가 된다.

## 3. ko-pii 공개 benchmark: 논문과 구별

- 자료: [고정 commit의 BENCHMARK.md](https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/docs/BENCHMARK.md).
- 읽기 수준: benchmark 설정·표·평가 코드 관련 부분 확인. 독립 학술 peer review나 실행 재현은 확인하지 않았다.

KDPII v1.1의 4,891문서에서는 ko-pii F1 .660, Presidio kr_adapt .273, privacy-filter .264로 보고한다. 자체 합성 행정/서식 540문서·3,635span·26label에서는 각각 .790/.483/.451이다. 두 평가의 실행 backend와 데이터 성격도 다르다.

주의할 평가 정의는 위치를 무시하는 substring 집합 매칭과 1~2글자 PERSON 제외다. 이는 한글 두 글자 이름이나 같은 문자열의 여러 출현을 엄격히 채점하는 마스킹 평가와 다르다. KDPII 표의 TP+FN도 ko-pii/privacy-filter는 1,302, Presidio는 1,305여서 label mapping을 확인해야 한다. Presidio kr_adapt가 이번 조사 시점의 최신 한국 recognizer와 동일한 구성이라고 검증하지 않았다.

KDPII 대화 평가에서 ko-pii의 PERSON F1 .135, ADDRESS .241은 번호 규칙과 자유문장 처리가 별도 문제임을 보여준다. 이 수치들은 그 개발자의 데이터·채점법에 한정된다. ‘ko-pii가 한국어 전체에서 79% 정확도’라는 표현은 쓰지 않는다.

## 4. K-PII-Bench: 데이터셋 카드 확인

- 자료: [Hugging Face dataset card](https://huggingface.co/datasets/woohyun212/k-pii-bench), 로컬 `k_pii_bench_README.md`.
- 읽기 수준: 카드·schema 확인. 30만 행 전수 검사, 논문 원문 검토, 탐지기 실행은 NOT_RUN.

카드는 한국어 합성 문서 300,000건, 18유형, 12도메인과 template skeleton 분리 split을 설명한다. train 243,711, dev 28,147, test_track_a 28,142로 합계가 맞는다. 데이터 CC BY 4.0과 코드 Apache 2.0 표기를 구분한다. 카드의 출판·품질 주장 자체를 독립 검증 결과로 옮기지 않았다.

AP-EYE에서는 이 데이터만으로 API 지원을 주장하지 않는다. JSON 위치, 숫자형/문자열형, query/cookie/header, 중첩 배열, 한국어 업무 오류를 추가해야 한다. 합성 template 분리가 실제 문서·인물·API별 누수를 모두 막는지도 확인해야 한다.

## 5. Cross-Lingual 평가: 버전 차이로 순위 채택 보류

- 자료: [arXiv 2608.02616](https://arxiv.org/abs/2608.02616), 로컬 `CrossLingual_2608.02616.pdf`.
- 읽기 수준: 1차 초록·도입·결론/한계와 일부 평가 설명 확인. 모든 표의 재검산·버전 간 대조는 완료하지 않았다.

수집된 최신 PDF는 *OpenAI Privacy Filter: A Cross-Lingual, Cross-Domain PII Evaluation Across 32 Benchmarks*라는 제목이며 14언어·5도메인을 설명한다. 검색/HTML v1에서 읽은 42-benchmark 서술과 다르다. 최신 PDF에는 학습 데이터 크기에 따른 비교도 있어 숫자를 섞기 쉽다. 따라서 이번 핵심 순위표에서 제외했고, 한국어·국가별 정확도의 확정 근거로도 사용하지 않았다. 향후 활용하려면 동일 version의 PDF·code·dataset revision부터 고정해야 한다.

## 6. AP-EYE에서 인용할 수 있는 것과 없는 것

| 인용 가능한 제한된 결론 | 아직 말할 수 없는 결론 |
|---|---|
| 문맥상 PII 정책과 span 정의가 성능에 크게 영향을 준다 | 특정 제품이 모든 국가에서 가장 정확하다 |
| 한국어 번호 규칙과 이름·주소 인식은 별도로 평가해야 한다 | 정규식 몇 개를 추가하면 한국어 PII가 해결된다 |
| 여러 공개 평가의 데이터·학습·채점 조건이 다르다 | 서로 다른 표의 F1을 한 순위로 정렬할 수 있다 |
| 합성 한국어 자료는 baseline 개발에 활용할 후보가 된다 | 합성 test의 점수가 운영 API에 그대로 재현된다 |
| 모델 출력의 confidence와 측정된 precision은 다르다 | threshold .4 또는 score .95가 정확도 40%/95%다 |

공통 test set, 요구 label의 동일 mapping, exact span, 타입별 P/R/F1·표본 수·CI, 실제 마스킹 잔존 검사를 준비한 뒤 새 결과를 추가해야 한다.
