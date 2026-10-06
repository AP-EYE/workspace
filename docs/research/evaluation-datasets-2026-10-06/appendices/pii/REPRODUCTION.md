# 한국어 PII 감사 재현

Windows/Python 3.12에서 완료한 **오프라인 규칙 기준선과 데이터 품질 감사**다. 학습·외부 API 호출은 없다. 이 폴더의 `inputs/`에는 당시 읽은 합성 자료 표본을 저장했다. K-PII-Bench·OpenPII의 first-rows는 무작위/대표 표본이 아니며, OpenPII Viewer 요청 자체는 revision을 고정할 수 없었다. 저장 파일과 해시를 입력으로 사용한다. [출처와 재배포 조건](ATTRIBUTION.md)

저장소 `team_hub` 루트의 PowerShell에서 다음을 실행한다. 소스만 공개 저장소의 지정 commit으로 내려받으며, 원본 데이터와 결과는 수정하지 않는다.

```powershell
$piiReview = 'docs/research/evaluation-datasets-2026-10-06/appendices/pii'
git clone https://github.com/Marker-Inc-Korea/ko-pii.git "$piiReview/sources/ko-pii"
git -C "$piiReview/sources/ko-pii" checkout 9516cabd6f582935cae1536ccbd8c5448afae679
git clone https://github.com/woohyun212/k-pii-bench.git "$piiReview/sources/k-pii-bench"
git -C "$piiReview/sources/k-pii-bench" checkout 1b480c515cc8425ea5c5675079bd7cf17b951554
python "$piiReview/scripts/audit_and_baseline.py"
python "$piiReview/scripts/probe_kpii_scorer.py"
python "$piiReview/scripts/audit_openpii.py"
```

이미 지정 소스 체크아웃이 있다면 clone 대신 `AP_EYE_KO_PII_SOURCE`와 `AP_EYE_KPII_SOURCE` 환경 변수로 두 경로를 지정할 수 있다. 이 세 스크립트는 Python 표준 라이브러리와 체크아웃한 두 소스만 사용한다. `sources/`의 내려받은 전체 저장소는 `.gitignore`로 제외하며 결과 JSON은 `evidence/`에 기록한다.

| 감사 | 재현할 결과 | 해석 |
|---|---|---|
| ko-pii 전체 540문서 + K-PII 공개 표본 | [기준선 JSON](evidence/ko-pii-full-audit-and-baseline.json), [감사 JSON](evidence/kpii-deep-sample-audit.json), [로그](evidence/audit-and-baseline.log) | ko-pii `person_min_length=3`에서 저자 substring-set F1 0.79017857; 같은 예측 exact-surface-set F1 0.66480603. 둘 다 문자 위치를 세는 strict span F1 아님 |
| K-PII scorer 반복 출현 반례 | [JSON](evidence/kpii-scorer-probe.json), [로그](evidence/kpii-scorer-probe.log) | 별도 helper F1=1.0, 실제 출현별 exact F1=2/3. 공식 seqeval CLI 전체의 오류를 뜻하지 않음 |
| OpenPII 첫 표본 | [JSON](evidence/openpii-korean-audit.json), [요청 기록](evidence/openpii-pages-manifest.json) | 혼합 126문서 중 한국어 16문서/113 span. 전체 한국어 모집단 추정 불가 |

원본 `ko-pii` JSONL의 SHA-256, 소스 commit, 설정과 혼동 행렬은 [기준선 JSON](evidence/ko-pii-full-audit-and-baseline.json)에 있다. 이 결과는 개발 감사 자료이며 숨김 최종 시험이나 사람 주석 검증이 아니다. Akto·Presidio·NER의 동일 자료 비교는 **NOT_RUN**이다.
