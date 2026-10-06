---
license: other
license_name: cc-by-4.0
language:
  - en
  - fr
  - de
  - es
  - it
  - nl
  - pt
  - bg
  - cs
  - da
  - el
  - et
  - fi
  - hr
  - hu
  - lt
  - lv
  - pl
  - ro
  - sk
  - sl
  - sr
  - sv
  - id
  - ja
  - ko
  - ms
  - tl
  - vi
  - zh
task_categories:
  - token-classification
  - text-generation
tags:
  - privacy
  - pii
  - sensitive-data
  - data-masking
  - data-anonymization
  - ner
  - synthetic
  - multilingual
  - ai4privacy
  - openpii
  - asia-pacific
pretty_name: "OpenPII 1.5M: Multilingual PII Masking with Asia Pacific Extension"
size_categories:
  - 1M<n<10M
source_datasets:
  - extended
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: validation
        path: data/validation.jsonl
---

# OpenPII 1.5M: Multilingual PII Masking Dataset (Asia Pacific Extension)

<p align="center">
  <img src="assets/pii_masking_3m_coverage.png" alt="PII-Masking-3M Coverage" width="500"/>
</p>

📖 **More information:** [www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific](https://www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific/)

## Overview

The **OpenPII 1.5M** dataset extends [OpenPII 1M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1m)
with a new **Asia Pacific** corpus, bringing global coverage to **30 languages**
across **Europe, Americas, and Asia Pacific**.

This is the flagship release of the **PII-Masking-3M family**, the world's
largest open multilingual PII masking corpus. Built to advance open research in
privacy-preserving NLP, this dataset enables the development and benchmarking of
**Named Entity Recognition (NER)** models, **token classification** pipelines, and
**data masking** systems that work across languages and borders.

Each example contains the original text, a masked version with labeled placeholders,
span-level annotations, and pre-computed BIO token labels compatible with
transformer-based models (mBERT, XLM-R, ModernBERT, etc.).

## Dataset Details

| Total Examples | Train | Validation | Labels | Languages | Regions | Annotations | Format | License |
|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **1,636,375** | 1,309,912 | 326,463 | 19 | 30 | 37 | 11,866,674 | JSONL | CC-BY-4.0 |

## Language Coverage

The dataset spans **37 regions** across Europe, the Americas, and Asia Pacific,
including the seven new Asia Pacific locales: Vietnamese (vi-VN), Indonesian (id-ID),
Malay (ms-MY), Filipino (tl-PH), Chinese (zh-CN), Japanese (ja-JP), Korean (ko-KR),
plus English variants in Singapore (en-SG) and India (en-IN).

<p align="center">
  <img src="assets/language_distribution.png" alt="Language Distribution" width="800"/>
</p>

## Label Taxonomy (19 Labels)

<p align="center">
  <img src="assets/label_distribution.png" alt="Label Distribution" width="800"/>
</p>

| Label | Count | Label | Count | Label | Count |
| :---|---: | :---|---: | :---|---: |
| `DATE` | 1,398,279 | `AGE` | 588,562 | `GENDER` | 319,615 |
| `GIVENNAME` | 1,396,075 | `STREET` | 559,329 | `TAXNUM` | 308,680 |
| `SURNAME` | 1,200,212 | `BUILDINGNUM` | 549,425 | `SEX` | 292,600 |
| `EMAIL` | 881,036 | `ZIPCODE` | 506,109 | `SOCIALNUM` | 281,424 |
| `CITY` | 824,793 | `IDCARDNUM` | 387,266 | `PASSPORTNUM` | 239,123 |
| `TITLE` | 770,782 | `CREDITCARDNUMBER` | 374,409 |  |  |
| `TELEPHONENUM` | 660,834 | `DRIVERLICENSENUM` | 328,121 |  |  |

## Data Structure

Each line in the JSONL files is a JSON object:

```json
{
  "source_text": "Tanaka Yuki lives at 1-2-3 Shibuya, Tokyo 150-0002.",
  "masked_text": "[SURNAME_1] [GIVENNAME_1] lives at [BUILDINGNUM_1] [STREET_1], [CITY_1] [ZIPCODE_1].",
  "privacy_mask": [
    {"value": "Tanaka", "start": 0, "end": 6, "label": "SURNAME"},
    {"value": "Yuki", "start": 7, "end": 11, "label": "GIVENNAME"}
  ],
  "split": "train",
  "uid": "openpii-xyz789",
  "language": "ja",
  "region": "JP",
  "script": "Jpan",
  "mbert_tokens": ["[CLS]", "Tanaka", "Yuki", "..."],
  "mbert_token_classes": ["O", "B-SURNAME", "B-GIVENNAME", "..."]
}
```

## Use Cases

* **Multilingual NER Research**: Train and evaluate PII detection models across
  Latin, Cyrillic, Greek, Han, Kana, Hangul and Brahmic-derived scripts.
* **Privacy-Preserving NLP**: Build data anonymization and masking pipelines for
  global products operating across Europe, Americas, and Asia Pacific.
* **Cross-Region Benchmarking**: Compare PII detection performance across regulatory
  regimes (GDPR, PDPA, APPI, K-PIPA, PDP, etc.).
* **Compliance Tools**: Develop systems for GDPR, CCPA, Singapore PDPA, Japan APPI,
  Korea PIPA, Indonesia UU PDP, and emerging Asia Pacific data protection laws.
* **AI Safety**: Prevent language models from memorising or exposing sensitive
  personal information across the global majority of languages.

## Extended Taxonomies

This dataset covers the **19 core identity labels**. For research or
enterprise applications requiring extended label taxonomies, including health
(PHI), financial (PFI), digital (PDI), work (PWI), and location (PLI) categories
in their Asia Pacific extended editions, contact our team:

🌐 **Website:** [www.Ai4Privacy.com](https://www.ai4privacy.com)
🔗 **Contact Form:** [https://forms.gle/oDDYqQkyoTB93otHA](https://forms.gle/oDDYqQkyoTB93otHA)

## Related Datasets (PII-Masking-3M Family)

| Dataset | Size | Link |
|:---|:---|:---|
| **Health (PHI)** | 400k | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-health-phi-400k) |
| **Financial (PFI)** | 400k | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-financial-pfi-400k) |
| **Location (PLI)** | 400k | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-location-pli-400k) |
| **Work (PWI)** | 400k | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-work-pwi-400k) |
| **Digital (PDI)** | 350k | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-digital-pdi-350k) |
| **Open PII** | 1.5M | [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m) |

---

## p5y Data Analytics

This dataset is built on the [p5y](https://p5y.org) framework, think of it as i18n but for privacy.
Just as i18n (internationalization) translates content into different locales, p5y translates
sensitive data into privacy-safe formats through a standardized 3-step approach:

1. **Awareness**, Scan and markup private entities in unstructured text, producing a structured privacy mask with entity types, distribution, density, and risk assessment.
2. **Protection**, Control identified personal data through masking, pseudonymization, or k-anonymization, tailored to the specific use case and regulatory requirements.
3. **Quality Assurance**, Measure remaining privacy risk after anonymization, evaluating de-anonymization risks through expert annotation and automated assessment.

Learn more at [p5y.org](https://p5y.org)

---

## About Ai4Privacy

At Ai4Privacy, we are building the global seatbelt for Artificial Intelligence, enabling innovation while safeguarding personal information. We develop state-of-the-art datasets and tools for privacy-preserving AI.

* **Newsletter & Updates:** [www.Ai4Privacy.com](https://www.ai4privacy.com)
* **Join our Community:** [Discord](https://discord.gg/kxSbJrUQZF)
* **Contribute/Feedback:** [Open Data Access Form](https://forms.gle/iU5BvMPGkvvxnHBa7)

---

## Licensing and Terms of Use

* **License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Copyright © 2026 Ai Suisse SA.
* **Permitted Use:** Research, commercial use, redistribution, and modification, subject to attribution requirements under CC-BY-4.0.
* **Attribution:** When using this dataset, please credit "Ai4Privacy / Ai Suisse SA" and link to this repository.
* **Responsible Use:** Use must comply with all applicable data privacy laws and regulations. This dataset contains **synthetic PII only**, no real personal data is included.
* **Citation:**
    ```bibtex
    @dataset{ai4privacy_openpii_1_5m_2026,
      author = {Ai4Privacy},
      title = {OpenPII 1.5M: Multilingual PII Masking Dataset with Asia Pacific Extension},
      year = 2026,
      publisher = {Hugging Face},
      url = {https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m}
    }
    ```

## Legal Disclaimer

**No Warranty & Use at Your Own Risk:** This dataset is provided **"as is"** without warranties of any kind. Ai4Privacy and Ai Suisse SA make **no representations** regarding accuracy, completeness, or suitability. Use is **at your own risk**.

**No Liability:** Ai4Privacy, Ai Suisse SA, and affiliates **shall not be liable** for any damages (direct, indirect, consequential, etc.) arising from the use or inability to use this dataset.

**Compliance & Responsibility:** Users are solely responsible for ensuring their use complies with **all applicable laws, regulations, and ethical guidelines**, including data privacy laws (e.g., GDPR, CCPA, PDPA, APPI, PIPA, UU PDP) and AI regulations. **This dataset contains synthetic PII only, no real personal data is included.**

Ai4Privacy is a project affiliated with [Ai Suisse SA](https://www.aisuisse.com/).
