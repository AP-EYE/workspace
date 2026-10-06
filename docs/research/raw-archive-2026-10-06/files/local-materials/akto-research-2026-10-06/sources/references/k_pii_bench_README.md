---
language:
- ko
license: cc-by-4.0
task_categories:
- token-classification
task_ids:
- named-entity-recognition
size_categories:
- 100K<n<1M
pretty_name: K-PII-Bench
tags:
- korean
- korean-nlp
- pii-detection
- privacy
- ner
- benchmark
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: dev
    path: data/dev.jsonl
  - split: test_track_a
    path: data/test_track_a.jsonl
---

# K-PII-Bench

**A Benchmark for Korean Personal Information Detection.**
12 domains · 18 PII types (37 BIO labels) · ~300,000 synthetic Korean documents · skeleton-disjoint splits.

- **Code & full docs:** https://github.com/woohyun212/k-pii-bench
- **License:** data CC BY 4.0 · code Apache-2.0
- **Paper:** *K-PII-Bench: A Benchmark for Korean Personal Information Detection* (Language Resources and Evaluation, Springer Nature)

## Load

```python
from datasets import load_dataset
ds = load_dataset("woohyun212/k-pii-bench")
ds["train"], ds["dev"], ds["test_track_a"]
```

## Splits (skeleton-disjoint, 0 template overlap)

| Split | Docs |
|---|---:|
| train | 243,711 |
| dev | 28,147 |
| test_track_a | 28,142 |

Track B (cross-domain) membership and Track C (robustness) perturbed test sets are in `data/splits/`.

## Record schema

`doc_id`, `template_id`, `domain`, `locale`, `text`, `template_text`,
`entities` (`{type,start,end,surface,normalized,placeholder,entity_id,value_id}`),
`meta`, `tokens`, `bio_tags`, `token_offsets`. `text[start:end] == surface` for every entity.

## PII types (18)

PERSON, EMAIL_ADDRESS, KR_PHONE_NUMBER, KR_RRN, KR_BANK_ACCOUNT, KR_DRIVER_LICENSE, KR_PASSPORT,
KR_NHIS, KR_VEHICLE_PLATE, KR_LOCATION, CREDIT_CARD, IP_ADDRESS, URL, USERNAME, ORGANIZATION, NRP,
DATE_OF_BIRTH, PERSONAL_ATTRIBUTE.

## Privacy

All PII is **synthetic**. No real personal data. The external KDPII corpus used for additional
validation in the paper is **not** redistributed here.

## Citation

```bibtex
@article{park2026kpiibench,
  title   = {K-PII-Bench: A Benchmark for Korean Personal Information Detection},
  author  = {Park, Woohyun and Oh, Jinyoung and Cha, Jeong-Won},
  journal = {Language Resources and Evaluation},
  year    = {2026}
}
```
