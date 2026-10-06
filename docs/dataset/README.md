# 기준 데이터셋

BOLA 판정 정확도(오탐률, 재현율)를 잴 기준 데이터셋을 고르고 근거를 남긴다. 2026-10-06 원문·공개 코드·로컬 실행 결과를 묶은 [태스크 2·4 팀 공유 보고서](../research/evaluation-datasets-2026-10-06/README.md)가 현재 상세 근거다.

## 기준 (2026-10-02 조재현 교수 피드백)

- **BOLA의 주 평가에서** 합성 API를 직접 만들어 성능 근거로 삼지 않는다. 연구 결과를 아는 사람이 만든 데이터는 정확도를 편향시킨다("그들만의 리그"). 기능 회귀와 stress test에는 활용하되 외부 실제 앱과 구분한다. 한국어 PII 평가는 별도 합성 데이터·독립 검수를 사용한다.
- 선행 논문이나 퍼저가 쓴 데이터셋을 써도 된다. 그 논문의 수치보다 개선됐음을 보이면 된다.
- 리뷰어가 납득할 만한 기준점을 고른다.

## 후보

| 데이터셋 / 대상 앱 | 쓴 논문·도구 | 규모 | 정답(ground truth) 구성 | 비고 |
|---|---|---|---|---|
| AuthProbe 취약·수정 FastAPI | [AuthProbe 원문](https://arxiv.org/abs/2607.20574)·[코드](https://github.com/jbarach2012/AuthProbe) | 이번 로컬 28개 정책 응답 중 비인가 노출 6개 요청 | 두 계정·세 객체씩 소유권 정책과 응답/fixture 직접 확인 | **기능 회귀 실행**. 하나의 결함에 대한 6개 요청이며 실서비스 일반화 근거 아님 |
| VAmPI 책 상세/공개 목록 | [EvoMaster 원문](https://arxiv.org/abs/2604.00702)·[VAmPI](https://github.com/erev0s/VAmPI) | 이번 로컬 10개 응답: 비공개 교차조회 2, 정상 8 | 원본 `vuln` 토글, 책 소유자와 보호 필드 직접 대조 | **앱 test client 실행**. 네트워크 scanner 평가 아님 |
| wger 영양 단건 조회 | [공식 GHSA](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)·[수정 commit](https://github.com/wger-project/wger/commit/29876a1954fe959e4b58ef070170e81703dab60e) | GET 3경로, **1 CVE family** | 취약 parent의 raw lookup과 `get_object()` 수정 diff 및 소유자 정책 | 공식 2.4/2.5 이미지에서 **계획 1경로의 자기/교차 8요청 실행**. 교차 2.4는 200/타인 값, 2.5는 404. 식사·식사항목 2경로 미실행. [재현 결과](../research/evaluation-datasets-2026-10-06/appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md) |
| wger 반복 목록 조회 | [공식 GHSA](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm)·[실제 수정 commit](https://github.com/wger-project/wger/commit/035a66161dcbdbac8bbd03adbc1bdb071f233274) | GET 2경로, **1 CVE family** | 무조건 `.all()`을 소유자 필터로 고친 diff | 공식 2.4/2.5 이미지에서 **두 목록·두 계정 8요청 실행**. 2.4에는 타인 객체 혼입, 2.5에는 자기 객체만 반환. [재현 결과](../research/evaluation-datasets-2026-10-06/appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md) |
| wger 공개 routine template | [maintainer 수정·테스트](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9) | 비소유자 공개 상세 GET 정상 1개 정책 유형 | 공식 테스트가 공개/비소유자 조회 200·동일 ID를 정상으로 허용 | 공식 2.7 이미지에서 원본 테스트 **8/8 통과**, [실행 로그·digest](../research/evaluation-datasets-2026-10-06/appendices/authz/real-app/public-normal/README.ko.md). 취약 2.4/수정 2.5와 다른 snapshot |
| BACScan 실서비스 pool | [CCS 2025 원문](https://yuanxzhang.github.io/paper/bacscan-ccs25.pdf) | 알려진 6앱/44결함 중 읽기 20 | 공개 PoC의 읽기 BAC; 개별 BOLA 여부와 정상/TN은 추가 확인 필요 | 대상 선정 자료. 전체 재현 **NOT_RUN** |
| 한국어 ko-pii 합성 | [ko-pii 공개 자산](https://github.com/Marker-Inc-Korea/ko-pii) | 540문서/3,635 문자열 gold/26유형 | 저자 LLM 생성·검수. offset 없는 문자열 set | 규칙 기준선 전체 **실행**. 저자 scorer F1 .79018, strict 문자 span 점수 아님 |
| K-PII-Bench 공개 수정판 | [HF 데이터](https://huggingface.co/datasets/woohyun212/k-pii-bench) | 카드상 300,000문서/18유형/12도메인 | 공개 span·BIO, 126문서/541개체 형식 검사 통과 | 표본에 음성 0·의미 오류 후보. 조건부 채택 |

도구 비교군은 대상 데이터와 별도다. 고정 Akto 원본, 기존 Test Role/YAML 설정 보정판, 동일 권한 근거를 받는 단순 규칙, [RESTler NameSpaceRuleChecker](https://github.com/microsoft/restler-fuzzer), 제안 방식을 비교한다. Akto·RESTler의 전체 실행 수치는 아직 없다. 자세한 실패 조건과 제외 후보는 위 [팀 공유 보고서](../research/evaluation-datasets-2026-10-06/README.md)에 기록했다.
