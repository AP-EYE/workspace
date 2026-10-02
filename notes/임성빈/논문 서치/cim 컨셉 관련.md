> 노션 원본: https://app.notion.com/p/91993f3d109683eb93d5019049004d3e (마지막 수정 2026-09-28), 2026-10-03 이관

# cim 컨셉 관련

### 1. 시맨틱 임베딩 기반 유사도 매핑 (Vector Embedding & Cosine Similarity)
필드명의 **'의미'를 수학적 벡터(Vector)로 변환**하여 공통 키워드와 가장 가까운 것을 찾아내는 기술입니다.
- **작동 방식:**
	1. 미리 표준화된 공통 표준 사전(Canonical Schema)을 정의합니다. (예: `communication_content`)
	2. API 응답의 새로운 필드명(예: `상담내용`, `customer_notes`)이 들어오면, 가벼운 임베딩 모델(Sentence-Transformers 등)을 통해 임베딩 벡터로 변환합니다.
	3. 코사인 유사도(Cosine Similarity)를 계산하여, `상담내용`이 `communication_content`와 유사도가 90% 이상이면 자동으로 해당 표준 필드로 변환(Mapping)합니다.
- **장점:** 하드코딩 없이 처음 보는 임의의 필드명도 의미가 비슷하면 자동으로 공통화됩니다.

### 2. Jev / LLM 기반의 Zero-Shot 스키마 정렬 (Context-aware Mapping)
필드명뿐만 아니라 **필드에 담긴 실제 데이터값(Value)의 문맥까지 함께 AI에 넘겨 분류**하는 기술입니다.
- **작동 방식:**
	- 필드명만 보면 `content`가 상담 내용인지, 게시글 내용인지 알 수 없습니다.
	- 이때 초고속 분류 AI인 **Jev**에 필드명과 데이터 샘플을 함께 입력합니다.
	- Jev가 "이 필드는 98% 확률로 \[고객 상담 및 민감 대화 데이터\] 범주에 속함"이라고 판단(`Choice`)하면, 이를 OCSF 표준 스키마의 `user_communication` 객체로 자동 변환합니다.
- **장점:** 필드명이 `data_1`처럼 무의미하게 지정되어 있어도, 내용물(Value)을 보고 정확한 표준 필드로 정규화할 수 있습니다.

### 3. OCSF Custom Class & JSON Schema Validator
앞서 구상한 OCSF 프레임워크 내에 기업용 확장 스키마(Custom Event Class/Object)를 정의하는 방식입니다.
- **작동 방식:**
	- OCSF 기본 스키마에 존재하지 않는 비즈니스 특화 데이터(상담내용, 결제내역 등)를 담기 위해, OCSF의 `Custom Object`로 `Unstructured_Text` 또는 `Customer_Interaction`이라는 포맷을 새로 정의해 둡니다.
	- 앞선 1, 2단계에서 추출된 변환 결과를 이 OCSF JSON Schema에 맞춰 검증(Validate)한 뒤 후속 단계로 넘깁니다.

### 우리 아키텍처 내 '자동 공통화 및 스코어링' 전체 파이프라인
이 기술들을 조합하면 논문에 제시할 완벽한 자동 정규화 파이프라인이 완성됩니다.
```plain text
[1. 비표준 API 응답 수집]
  - 예: { "counsel_notes": "주민번호 900101-1****** 고객 문의사항..." }
        │
        ▼
[2. AI 기반 시맨틱 스키마 매핑 계층 (Semantic Schema Mapper)]
  - 임베딩/Jev가 필드명("counsel_notes")과 값의 문맥을 읽고 의미 파악
  - "counsel_notes" ➔ 표준 OCSF 필드인 "user_communication.text"로 자동 매핑
        │
        ▼
[3. OCSF 표준 규격 변환]
  - { "user_communication": { "text": "주민번호 900101-1******..." } }
        │
        ▼
[4. Jev 초고속 PII 분류 및 FPE(형태보존암호) 판별]
  - 평문 PII 여부 및 암호화 상태 판별 (0.5초 이내)
        │
        ▼
[5. 최종 영향도 정량 산정 (Scoring)]
  - API 인가 취약점(BOLA) x PII 보호 상태 = 최종 Risk Score 도출
```

**최신 논문: "Beyond Collection: Measuring the Detection Efficacy of Modern Security Logging Standards"**
- **링크:** [https://arxiv.org/abs/2605.05531](https://arxiv.org/abs/2605.05531)
- **발행일:** 2026년 5월
- **내용 요약:**
	- 원격 코드 실행 취약점 등 50개의 익스플로잇 시나리오를 바탕으로 CIM, OCSF, ECS와 같은 최신 보안 로깅 표준의 탐지 효용성을 정량적으로 평가한 논문입니다.
	- 각 로깅 표준이 공격 지표를 얼마나 잘 포착하는지에 대한 중대한 차이와 간극(gaps)을 식별해 냈습니다. 우리 아키텍처에 어떤 로깅 표준을 채택해야 하는지 정당성을 부여하기 좋은 학술 자료입니다.

**심층 분석 자료: "Six schemas into OCSF: the mapping is the hard part" (CIM 매핑의 한계점 분석)**
- **링크:** [https://securitydataworks.com/writing/ocsf/six-schemas-into-ocsf/](https://securitydataworks.com/writing/ocsf/six-schemas-into-ocsf/)
- **발행일:** 2026년 6월
- **내용 요약 (CIM 역설의 핵심):**
	- Splunk CIM은 20여 년간 실무적 편의를 위해 만들어진 1차원적인 평면(flat) 네임스페이스(예: `src`, `dest`, `user` 등)를 사용하고 있습니다.
	- 이를 최신 OCSF의 중첩된(nested) 객체 구조로 리모델링하여 매핑할 때, 기계적으로 변환되지 않고 수많은 '자의적 판단(judgment calls)'이 개입되어야만 합니다.
	- 결과적으로 코드로 한 번에 매핑하고 100% 신뢰하기 어려운 병목 현상(bottleneck)이 발생하며, 이것이 바로 기존 CIM 구조가 가진 태생적인 역설적 한계임을 날카롭게 지적하고 있습니다.
