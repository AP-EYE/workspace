> 노션 원본: https://app.notion.com/p/3ed93f3d109680cdb032e227341a92a3 (마지막 수정 2026-10-02), 2026-10-03 이관

# BOLA 탐지 도구 비교
> 비교 기준: **"이 객체를 누가 봐도 되는가"를 어떻게 아는가**

## 1. 비교 대상

| 도구 | 종류 | 발표 | 링크 |
|---|---|---|---|
| **우리 연구** | 연구 가설 | 2026 | 가설 문서 |
| BOLABuster(오픈소스X) | 기술 블로그 + 발표 | Unit 42, 2024 | [블로그](https://unit42.paloaltonetworks.com/automated-bola-detection-and-ai/) |
| AuthProbe | 논문 (arXiv) | 2026-07 | [arXiv 2607.20574](https://arxiv.org/abs/2607.20574) |
| EvoMaster 보안 오라클 | 논문 (arXiv, JSS 게재 예정) | 2026-04 | [arXiv 2604.00702](https://arxiv.org/abs/2604.00702) |
| BACScan | 논문 (CCS) | 2025 | [PDF](https://yuanxzhang.github.io/paper/bacscan-ccs25.pdf) |
| VSF | 논문 (IEEE S&P) | 2025 | [PDF](https://swag.cispa.saarland/papers/chehade2025access.pdf) |
| RESTler 검사기 | 논문 (ICST) | 2020 | [PDF](https://patricegodefroid.github.io/public_psfiles/icst2020.pdf) |
| ZAP Access Control | 공식 문서 | - | [문서](https://www.zaproxy.org/docs/desktop/addons/access-control-testing/) |

## 2. 비교표

| 도구 | 테스트할 객체를 얻는 법 | 누가 봐도 되는지 판단 | 애매할 때 |
|---|---|---|---|
| **우리 연구** | 진단 계정이 직접 생성 | **공개·비공개·공유를 미리 지정** | 보류 |
| BOLABuster | 진단 계정이 직접 생성 | 지정 안 함. 타인 접근 성공 = BOLA 지표 | AI 판단 후 사람 검증 |
| AuthProbe | 목록 API 결과 | 내 목록에 나오면 내 것 | 없음 (확정 or 미보고) |
| EvoMaster | 퍼징 중 생성된 리소스 | 401/403 응답으로 추론 | 일부 규칙에 "결론 불가" |
| BACScan | 진단 계정이 데이터에 토큰 삽입 | 양쪽 탐색에서 URL·내용 같으면 공개 | 없음 (유사도 0.7 기준) |
| VSF | 연구자 계정 2개의 데이터 | 지정 안 함 | 사람이 수동 검사 |
| RESTler 검사기 | 퍼징 중 생성된 리소스 | 지정 안 함. 타인 접근 성공 = 위반 | 없음 |
| ZAP | 크롤링한 페이지 | **사람이 페이지마다 지정** | Unknown 값 |

## 3. 출처 위치

| 도구 | 표 내용의 근거 위치 |
|---|---|
| BOLABuster | 블로그 "4. Create Test Scripts"(생성·판정), "5. Execute Plans and Analyze"(사람 검증) |
| AuthProbe | §III 둘째 문단(소유권 = 목록), §V-B 식(1)(판정), §V-F(완전하지 않음) |
| EvoMaster | §3 도입부(401/403 추론), §3.2 끝(결론 불가), §3.3(단순 규칙은 오탐) |
| BACScan | §4.1.2 Token Insertion(토큰), §4.2.2(공개 판단·유사도 0.7) |
| VSF | 초록(후보 584개 중 결함 19개), GitHub README "Goal"·"Analysis" |
| RESTler 검사기 | §III-A User-namespace rule |
| ZAP | "Access Rules" 절(Allowed / Denied / Unknown) |

## 4. 결과 수치 (공개된 것만)

| 도구 | 평가 대상 | 결과 | 위치 |
|---|---|---|---|
| BOLABuster | 알려진 BOLA가 있는 오픈소스 3개 | 전부 탐지, RESTler 기본 설정은 0개 | BSides LV 2024 발표 소개 |
| AuthProbe | 직접 만든 합성 API 2개 | 심은 취약점 전부 탐지, 보안 버전에서 오탐 0 | §VII-B, Table III |
| BACScan | 오픈소스 웹앱 20개 | 읽기형 정밀도 83.33% / 재현율 75.00% (정답셋) | §5.2, Table 2 |
| VSF | 실제 웹사이트 100개 | 후보 584개 → 실제 결함 19개 | 초록 |
| EvoMaster | API 52개 | 여러 API에서 보안 결함 탐지 | 초록 |
| **우리 연구** | Gitea, Memos (후보) | 미측정 | - |
