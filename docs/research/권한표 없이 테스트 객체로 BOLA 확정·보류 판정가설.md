> 노션 원본: https://app.notion.com/p/3ea93f3d109680138a25feb148812f0c (문서 허브, 카테고리 제안·자료 조사, 상태 완료, 마지막 수정 2026-10-02), 2026-10-03 이관.

# 권한표 없이 테스트 객체로 BOLA 확정·보류 판정가설

이 노션 페이지는 [연구 주제 정의와 근거.md](연구%20주제%20정의와%20근거.md)를 발행한 사본이다. 본문(주제 정의, 용어, 근거 1~6, APIs.guru 조사, 정리)은 그 파일과 같아서 옮기지 않았다. 노션에서만 추가된 부분은 아래와 같다. 노션 첨부 PDF는 모두 [docs/papers/](../papers/)에 같은 이름으로 있다.

## 노션에서 추가된 내용

> **연구 방향 검토 (2026-10-02, 차별성 검증 후보)**
> 기존 연구의 공개 필터와 다중 계정 검사를 출발점으로, 테스트 객체의 설정 근거가 관찰 기반 권한 추정의 오류를 얼마나 줄이는지, 그 대가로 얼마의 준비 시간과 판정 범위 제한이 생기는지를 검증한다.
> BACScan도 두 계정이 공통으로 탐색한 공유 페이지를 거를 수 있다. 공유·로그인 공개 처리가 불가능하다고 단정하지 않고, 허용 객체가 한쪽 탐색에서 빠지는 조건에서 차이가 생기는지 비교한다.
> 전체 운영 객체의 권한표 대신 테스트 객체의 소유자·공개 범위·공유 대상을 입력한다. 권한 입력 자체를 없애는 것은 아니며 한 객체의 결과를 다른 객체에 자동 확대하지 않는다.
> 예비 결과는 단순 규칙의 오탐 Gitea 8/18, Memos 개별 조회 3/6이다. 제안 판정기의 재현율·보류율·입력 비용은 미측정이다. 보류한 실제 위반은 미탐으로 센다.
> 근거: [BACScan §4·§6](https://seclab.cse.cuhk.edu.hk/papers/ccs25-BACScan.pdf), [AuthProbe §III·§V](https://arxiv.org/html/2607.20574).

> 테스트 객체 몇 개만 지정해서 권한표 없이 BOLA를 확정하고, 근거 없는 객체는 보류로 분리한다.
> 이 방식은 접근 성공 여부만 쓰는 판정보다 공개·공유 객체 조회에서 오탐률이 낮다.
>
> **필요한 이유**: 단순 "타인 접근 = 위반" 규칙은 공개·공유 조회를 오탐한다. 그렇다고 권한표 전체를 쓰기에는 비용이 크다. 국내 사고 원인도 권한 검증 누락이다.
>
> **직접적인 선행논문**: Sahin et al. (arXiv 2604.00702) [PDF](../papers/EvoMaster-Security_2604.00702.pdf), Atlidakis et al. (ICST 2020) [PDF](../papers/ICST2020_REST-API-security-rules.pdf)
>
> **차이점**: 기존 연구는 관찰한 응답 코드나 사람이 쓴 권한표에 의존한다. 이 연구는 테스트 객체 단위로 확정하고 보류를 분리하며 확정 범위·오탐률·보류율을 함께 측정한다.

"공개 조회 API와 BOLA를 어떻게 구분하나"라는 가설을 공개 여부를 미리 지정한 테스트 객체로 풀어보는 주제

### 근거 4의 정정 (2026-10-01)
이전에는 이 방식을 "엔드포인트 단위"라고 적었으나, 원문(§4 RBAC 탐지)은 두 세션의 탐색 결과에서 URL과 내용이 같은 페이지를 공개로 본다. 객체마다 URL이 다르면 사실상 객체 단위다.<br>한계는 공개 여부를 탐색 도달로 추정한다는 점, 특정 사용자 공유·로그인 사용자 공개 범주가 없다는 점, 근거 없는 객체를 보류로 분리하지 않는다는 점이다. 테스트 객체에 공개 상태를 미리 지정하는 이유다.

### 정리의 추가 항목
- 관찰 기반 공개 필터가 허용 객체의 탐색 누락 조건에서 어떤 오류를 만드는지는 비교 검증할 질문이다. BACScan도 공통 탐색된 공유 페이지를 거를 수 있으므로 공유·로그인 공개 처리가 불가능하다고 단정하지 않는다 (BACScan §4).

**→** 소수의 공개·비공개·공유 테스트 객체만 지정했을 때 어느 범위까지 위반을 확정할 수 있고 오탐과 보류가 각각 얼마나 나오는가

### 참고 문헌 첨부
| 식별자 | 문헌 | 파일 |
|---|---|---|
| ICST'20 | Atlidakis et al., Checking Security Properties of Cloud Service REST APIs, ICST 2020 | [PDF](../papers/ICST2020_REST-API-security-rules.pdf) |
| 2604.00702 | Sahin et al., Enhancing REST API Fuzzing with Access Policy Violation Checks, 2026 | [PDF](../papers/EvoMaster-Security_2604.00702.pdf) |
| 2212.06606 | OpenAPI Specification Extended Security Scheme, 2022 | [arXiv](https://arxiv.org/abs/2212.06606) |
| AuthProbe | AuthProbe, arXiv 2607.20574, 2026 | [PDF](../papers/AuthProbe_2607.20574.pdf) |
| 2607.16754 | Non-Intrusive Traffic Analysis Framework for Authorization Risk Detection, 2026 | [PDF](../papers/TrafficAuthzRisk_2607.16754.pdf) |
| BACScan | Liu et al., BACScan, CCS 2025 | [PDF](../papers/BACScan_CCS25.pdf) |
| 2605.25865 | Broken Object Level Authorization in the Wild, 2026 | [PDF](../papers/BOLA-Taxonomy_2605.25865.pdf) |
