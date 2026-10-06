# 합성 자료 표본의 출처와 사용 조건

이 폴더의 `inputs/`는 분석을 재현할 수 있도록 공개 합성 자산의 소규모 표본과 생성 평가 파일을 보관한다. 문서의 수치와 달리 모델의 학습/시험 승인이나 라벨의 사람 검증을 뜻하지 않는다.

| 입력 | 원본·버전 | 원본에 표시된 이용 조건 |
|---|---|---|
| `generated_eval.jsonl` | [Marker Inc Korea `ko-pii`](https://github.com/Marker-Inc-Korea/ko-pii/tree/9516cabd6f582935cae1536ccbd8c5448afae679), commit `9516cabd6f582935cae1536ccbd8c5448afae679`; [MIT LICENSE](https://github.com/Marker-Inc-Korea/ko-pii/blob/9516cabd6f582935cae1536ccbd8c5448afae679/LICENSE) | MIT. Copyright © 2026 Marker Inc. 이 파일은 연구 재현용 복제본이다. 원문의 `data/generated_eval.README.md`를 함께 확인한다. |
| `k-pii-*-firstrows.json` | [K-PII-Bench](https://huggingface.co/datasets/woohyun212/k-pii-bench), [코드 commit `1b480c…`](https://github.com/woohyun212/k-pii-bench/tree/1b480c515cc8425ea5c5675079bd7cf17b951554); first-rows API 표본 | [원본 `LICENSE-DATA`](https://github.com/woohyun212/k-pii-bench/blob/1b480c515cc8425ea5c5675079bd7cf17b951554/LICENSE-DATA)의 CC BY 4.0. 표본 취득 시 조회 범위를 별도 기록했다. |
| `openpii-*-firstrows.json`, `openpii-meta.json` | [ai4privacy OpenPII 1.5M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m), 조사 당시 repository SHA `a785eb528e28be2693c3718a27e066970de5dadb` | [데이터 카드](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m)의 CC BY 4.0 표기. Viewer first-rows 응답은 revision이 고정되지 않았으므로 이 보존 파일이 이번 분석 입력이다. |

코드와 데이터를 재배포·재사용할 때는 각 원본의 최신 라이선스 및 고지 조건을 확인한다. 이 폴더의 공개 자료는 기존 원본을 대체하지 않는다.
