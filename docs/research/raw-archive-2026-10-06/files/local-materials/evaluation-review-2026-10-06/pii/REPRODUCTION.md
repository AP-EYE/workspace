# 한국어 PII 감사 재현

2026-10-06에 Windows / Python 3.12에서 아래 로컬 실행을 완료했다. 실제 모델 학습·추론 서버·유료 API 호출은 없다. 감사 스크립트는 원본 데이터를 변경하지 않고 `evidence/` 결과 파일을 다시 쓴다. 여기의 재현은 공개 합성 자료의 형식 검사와 규칙 탐지기 점수 재현이며, 독립 사람 정답 검증을 의미하지 않는다.

## 입력 배치

스크립트는 다음 디렉터리 관계를 사용한다. 보고서만 다른 폴더로 복사하면 실행되지 않으므로 재현 패키지에는 입력도 함께 보존한다.

```text
local-materials/
  evaluation-datasets-2026-10-06/
    evidence/k-pii-train-firstrows.json
    evidence/k-pii-dev-firstrows.json
    evidence/k-pii-test_track_a-firstrows.json
    sources/k-pii-bench/
  evaluation-review-2026-10-06/pii/
    scripts/
    sources/ko-pii/
    evidence/openpii-train-firstrows.json
    evidence/openpii-validation-firstrows.json
```

- ko-pii 코드·데이터: `9516cabd6f582935cae1536ccbd8c5448afae679`.
- K-PII-Bench 코드: `1b480c515cc8425ea5c5675079bd7cf17b951554`.
- OpenPII 당시 HF repository revision: `a785eb528e28be2693c3718a27e066970de5dadb`. Viewer first-rows는 revision 파라미터로 고정한 다운로드가 아니므로, 분석 입력은 저장한 JSON 파일과 조회 시점으로 식별한다. 변경 가능한 API를 재호출한 결과가 이 표본과 같다고 가정하지 않는다.

## 로컬 실행

저장소 루트 `C:\Users\andyw\Desktop\AP-EYE`의 PowerShell에서:

```powershell
$env:PYTHONIOENCODING='utf-8'
python local-materials/evaluation-review-2026-10-06/pii/scripts/audit_and_baseline.py
python local-materials/evaluation-review-2026-10-06/pii/scripts/probe_kpii_scorer.py
python local-materials/evaluation-review-2026-10-06/pii/scripts/audit_openpii.py
```

이 세 스크립트는 Python 표준 라이브러리와 체크아웃한 소스만 사용한다. 원문 PDF 변환/추출에 쓴 markitdown/pypdf는 이 세 감사 실행의 의존성이 아니다.

## 확인할 출력

| 실행 | 완료 근거 | 해석의 범위 |
|---|---|---|
| ko-pii 전체 540문서 + 기존 KPII 표본 | [로그](evidence/audit-and-baseline.log), [기준선 JSON](evidence/ko-pii-full-audit-and-baseline.json), [KPII 감사](evidence/kpii-deep-sample-audit.json) | `person_min_length=3`, 저자 substring-set F1 0.79017857; 같은 예측의 exact-surface-set F1 0.66480603. 둘 다 문자 위치를 포함하는 strict span F1 아님 |
| KPII span helper 반례 | [로그](evidence/kpii-scorer-probe.log), [JSON](evidence/kpii-scorer-probe.json) | 동일 인명 두 출현 중 하나만 탐지해도 helper F1=1. 실제 출현별 exact F1=2/3. 공식 seqeval CLI 전체의 오류라고 확장하지 않음 |
| OpenPII 첫 표본 | [JSON](evidence/openpii-korean-audit.json) | 혼합 언어 126문서 중 한국어 16문서/113개체; 전수·무작위 표본 아님 |

한국어 NER 모델 실행, Presidio 구성 실행, Akto end-to-end 동시 비교, 숨김 시험 동결, 독립 사람 이중 주석, K-PII 전체 300,000문서 감사는 `NOT_RUN`이다. 외부 HTTP 500과 조회 실패는 [요청 manifest](evidence/openpii-pages-manifest.json)에 보존했으며 성공으로 계산하지 않는다.
