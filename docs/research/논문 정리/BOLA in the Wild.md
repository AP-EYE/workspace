> 노션 원본: https://app.notion.com/p/3ed93f3d10968089bb06d3025f7a42ac (마지막 수정 2026-10-02), 2026-10-03 이관. 원문 PDF: [BOLA-Taxonomy_2605.25865.pdf](../../papers/BOLA-Taxonomy_2605.25865.pdf)

# Broken Object Level Authorization in the Wild: An Empirical Taxonomy from 100+ Bug Bounty Disclosures

## 논문 정보
**제목**: Broken Object Level Authorization in the Wild: An Empirical Taxonomy from 100+ Bug Bounty Disclosures

**저자**: Bandana Kaur

**공개일**: 2026년 5월 24일

**arXiv**: 2605.25865

**학술지**: 미기재

## 한 줄 요약
HackerOne 공개 보고서 107건을 분석해 84건의 BOLA를 확인하고, 다른 사용자의 객체에 상태 변경 작업을 수행하는 유형과 직접 객체 참조 유형이 가장 흔하게 관찰됐다고 보고한다.

## 핵심 키워드
### BOLA와 IDOR
- **BOLA (Broken Object Level Authorization)**: 사용자가 특정 객체에 접근하거나 작업할 권한이 있는지 서버가 제대로 확인하지 않는 취약점
- **IDOR (Insecure Direct Object Reference)**: 객체 식별자를 직접 참조하거나 바꿔 접근하는 흔한 공격 기법
### BOLA의 주요 유형
- **Action-Level Object BOLA**: 다른 사용자의 객체에 대한 수정·삭제·실행 등 무단 상태 변경
- **Direct Object Reference BOLA**: 알려져 있거나 쉽게 예측 가능한 객체 식별자를 이용한 무단 접근
### 방어 및 기술
- **권한 검증**: 요청마다 사용자와 대상 객체 간의 권한 관계를 확인하는 통제
- **GraphQL Global ID**: 인코딩된 ID도 내부 식별자가 추측 가능하거나 노출되면 악용될 수 있는 GraphQL 객체 참조
### 연구 방법론
- **버그 바운티 공개 데이터**: 실제 취약점 보고서를 활용한 보안 실증 분석 방식

## 3줄 요약
- 본 연구는 100건 이상의 HackerOne 버그 바운티 공개 보고서를 분석하여 Broken Object Level Authorization (BOLA)에 대한 6가지 유형의 실증적 분류 체계를 제시했습니다.
- 연구 결과, Action-Level Object BOLA(41.7%)와 Direct Object Reference BOLA(36.9%)가 전체 사례의 대부분을 차지하며, 기존 OWASP 가이드라인이 간과했던 상태 변경 공격의 위험성을 확인했습니다.
- 보안 테스터와 개발자는 단순히 읽기 권한을 넘어 삭제, 수정 등 상태 변경 액션에 대한 인증을 필수적으로 점검하고, 특히 Vertical BOLA와 같은 비대칭 권한 실패 패턴에 주목해야 합니다.

## 간략히 보기
### 요약
본 논문은 Broken Object Level Authorization(BOLA) 취약점에 대한 최초의 대규모 실증적 분석을 다루며, 2021년부터 2026년 사이 HackerOne에 공개된 200개의 IDOR 및 Improper Access Control 보고서를 기반으로 BOLA의 실제 발생 양상과 그 패턴을 체계화했습니다.

### 1. 핵심 방법론 (Methodology)
연구진은 재현 가능한 샘플링 프레임워크를 통해 200개의 보고서를 수집한 뒤, 3단계 포함 필터(구체적인 객체 참조 여부, 경계 간 접근 권한 증거, 기술적 상세 정보 포함)를 적용하여 107개의 보고서를 선별했습니다. 이후 다음의 과정으로 분석을 수행했습니다.
#### LLM 활용 분류
Claude Sonnet(claude-sonnet-4-6)을 활용하여 정의된 6개 BOLA 패밀리 분류 체계에 따라 보고서를 스키마화했습니다.
#### 인간 검증 루프
LLM의 낮은 신뢰도 출력물과 분류 불일치 사례에 대해 인간 연구자가 직접 검토 및 재분류를 수행하는 이중 검증 체계를 구축했습니다.
#### 통계적 신뢰도
표본 크기가 작고 비율이 극단적인 경우를 고려하여, 신뢰 구간($CI$) 계산 시 일반적인 Wald 구간 대신 Wilson score interval을 사용했습니다.

$$CI = z \pm 1.96 \times \sqrt{\frac{p(1-p)}{n}}$$ (연속성 보정 적용)

#### 가중치 분석
단일 프로그램(예: HackerOne, U.S. Department of Defense)의 보고서가 결과에 미치는 영향을 최소화하기 위해 각 프로그램에 동일한 가중치를 부여하는 program-weighted robustness analysis를 병행하여 결과의 객관성을 확보했습니다.

### 2. BOLA 6개 패밀리 분류 (Taxonomy)
연구진은 실증 데이터를 바탕으로 BOLA를 6가지 유형으로 구분했습니다.
#### Direct Object Reference BOLA
예측 가능한 식별자를 통한 즉각적인 권한 없는 접근.
#### Action-Level Object BOLA
객체에 대한 읽기뿐만 아니라 상태 변경(수정, 삭제, 트리거) 동작을 수행하는 유형.
#### Tenant Isolation BOLA
조직/테넌트 간의 권한 경계를 침범하는 접근.
#### Workflow-Context BOLA
객체의 상태나 생애 주기(예: 삭제됨, 보관됨)에 따른 조건부 승인 실패.
#### Chained Disclosure BOLA
별도의 엔드포인트에서 식별자를 획득한 후 이를 이용해 권한 없는 접근을 수행하는 다단계 공격.
#### Object Rebinding BOLA
요청 내의 소유권 필드(예: owner_id)를 클라이언트 측에서 조작하여 승인 범위 자체를 변경하는 공격.

### 3. 주요 결과 (Key Findings)
#### 분류 노이즈
HackerOne의 IDOR/Improper Access Control 태그가 붙은 보고서 중 실제 BOLA로 확인된 사례는 42.0%(84/200)에 불과하여, 플랫폼 태그를 통한 취약점 노출 측정은 실제보다 수치가 과대평가될 가능성이 큼을 입증했습니다.
#### 패밀리 분포
- **Action-Level Object BOLA(41.7%)**와 **Direct Object Reference BOLA(36.9%)**가 전체의 약 78.6%를 차지하는 공동 지배적인 유형임을 확인했습니다.
#### 공격 방향
권한 수준이 같은 사용자 간의 수평적(Horizontal) 공격이 85.7%로 지배적이었으나, 11.9%의 수직적(Vertical) 공격은 관리자 권한을 탈취할 수 있어 높은 위험도를 내포하고 있음이 드러났습니다.
#### 기술적 지표
순차적 정수(Sequential integer) 식별자가 여전히 가장 흔한(36.9%) 공격 매개체이며, GraphQL Global IDs(GIDs)가 Base64 디코딩 및 정수 증분 방식으로 체계적으로 악용되고 있음을 확인했습니다.

### 4. 결론 및 시사점
본 연구는 현재의 OWASP 가이드라인이 Action-Level Object BOLA나 수직적 권한 상승과 같은 실제 주요 위협을 충분히 반영하지 못하고 있음을 지적합니다.

저자들은 개발자에게 서버 측 세션 기반의 소유권 검증을 권고하고, 테스터들에게는 단순히 GET 요청의 ID 조작을 넘어 삭제/수정 등 상태 변경 동작과 생애 주기 전반에 걸친 권한 검증 테스트를 포함할 것을 제안합니다.

## 주요 인용문
### 테스트 범위: 읽기뿐 아니라 상태 변경 작업까지
> 읽기 중심 테스트는 다른 사용자의 객체에 대한 수정·삭제·트리거 등 무단 상태 변경 취약점을 놓칠 수 있으므로, 이러한 작업도 테스트 범위에 포함할 필요가 있다.

**출처**: Kaur, 2026, p. 18 (6.1절)

**의미**: 기존 BOLA 테스트가 GET 읽기 권한 검증에 치중했으나, 실제 공격의 41.7%는 PUT/DELETE 같은 상태 변경 작업에서 발생함을 강조

### 탐지 방법론: ID 퍼징을 넘어 의미론적·교차 사용자 검증으로
> 순차 정수 열거는 분석 표본에서 가장 흔한 단일 탐지 메커니즘이었지만, 비순차 식별자 형식도 관찰됐다. 따라서 순차 ID 증감만으로 충분하다고 단정하기 어렵고, 객체 참조의 의미와 사용자 간 응답 차이가 실제 권한 경계 위반인지 검증하는 탐지가 필요하다.

**출처**: Kaur, 2026, p. 14 (5.7절); Kaur, 2026, p. 18 (6.1절)

**의미**: 식별자 퍼징(ID 증감)만으로는 전체 BOLA의 약 1/4~1/5만 탐지 가능하며, 의미론적 컨텍스트와 교차 사용자 응답 비교를 통한 검증이 필수적임을 지적

**주의**: 논문은 특정 도구의 실제 탐지율을 평가한 것은 아니므로, "ID 퍼징만으로 전체 취약점의 1/5~1/4만 탐지된다"고 단정하기보다 표본에서 순차 정수 열거가 36.9%(=직접 객체 참조의 100%)를 차지했다고 표현하는 것이 정확합니다.
