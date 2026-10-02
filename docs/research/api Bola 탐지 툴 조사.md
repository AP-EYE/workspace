> 노션 원본: https://app.notion.com/p/3ed93f3d1096807a8f0ec9cee83ce8c8 (문서 허브, 카테고리 자료 조사, 마지막 수정 2026-10-02), 2026-10-03 이관

# api Bola 탐지 툴 조사

하위 페이지:
- [BOLA 툴 비교표 (Claude)](api%20Bola%20%ED%83%90%EC%A7%80%20%ED%88%B4%20%EC%A1%B0%EC%82%AC/BOLA%20%ED%88%B4%20%EB%B9%84%EA%B5%90%ED%91%9C%20%28Claude%29.md)
- [AuthzTrace 테스트](api%20Bola%20%ED%83%90%EC%A7%80%20%ED%88%B4%20%EC%A1%B0%EC%82%AC/AuthzTrace%20%ED%85%8C%EC%8A%A4%ED%8A%B8.md)
- [Authztrace 정탐 오탐 비교표](api%20Bola%20%ED%83%90%EC%A7%80%20%ED%88%B4%20%EC%A1%B0%EC%82%AC/Authztrace%20%EC%A0%95%ED%83%90%20%EC%98%A4%ED%83%90%20%EB%B9%84%EA%B5%90%ED%91%9C.md)

<details>
<summary>LLM으로 BOLA 자동 탐지 하는 툴</summary>

[노션 북마크](https://app.notion.com/p/3ed93f3d1096807a8f0ec9cee83ce8c8#3ed93f3d109680a99d6de44bebd573c6)

# BOLABuster vs 우리 연구
> BOLABuster는 **테스트를 자동으로 만드는 도구**,<br>우리 연구는 **테스트 결과를 판정하는 방법**이다.
## BOLABuster란
- Palo Alto Networks **Unit 42**가 만든 LLM 기반 BOLA 자동 탐지 방법
- 블로그(2024-08)와 BSides LV 2024 발표로만 공개. 논문·오픈소스 아님
- Grafana, Harbor, Easy!Appointments에서 실제 BOLA를 찾아 CVE 받음
## 어떻게 동작하나
1. LLM이 BOLA 후보 엔드포인트를 고른다
2. API끼리 어떤 순서로 호출해야 하는지 파악한다
3. 두 계정으로 테스트 스크립트를 만든다 (A가 만든 객체에 B가 접근)
4. 실행 후 LLM이 결과를 보고, 취약해 보이면 사람이 확인한다
## 같은 점
- 두 계정으로 교차 접근한다
- 진단 계정이 객체를 직접 만든다
- 권한표 전체가 필요 없다
- 애매한 건 결국 사람이 본다
## 다른 점
- **목적**: BOLABuster는 테스트 생성 자동화, 우리는 판정 방법
- **객체 상태**: 우리는 공개·비공개·공유를 미리 지정. BOLABuster 공개 자료에는 이 단계가 없음
- **판정**: BOLABuster는 "B가 접근 성공 = BOLA 지표". 우리는 "금지 근거 + 실제 수신 = 확정", 근거 없으면 보류
- **측정**: 우리는 확정 범위·오탐률·보류율·재현율을 잼. BOLABuster는 오탐률 미공개
## 참고할 점
- 테스트 생성 부분은 BOLABuster 아이디어를 빌려 쓸 수 있음
- "B가 접근 성공 = 위반" 규칙을 비교 기준선으로 쓸 수 있음
## 주의
- 공개 자료가 블로그뿐이라 내부 동작은 확인 불가
- "공개·공유를 구분 못 한다"고 단정하지 말 것 → "공개 자료에 설명이 없다"로 표현
## 출처
- Unit 42 블로그 (Mazon & Chen, 2024): https://unit42.paloaltonetworks.com/automated-bola-detection-and-ai/
- BSides LV 2024 발표 (Jay Chen): https://pretalx.com/bsideslv24/talk/FSYWPG/

</details>

# 1. BOLABuster 정리
> Palo Alto Networks **Unit 42**가 만든 LLM 기반 BOLA 자동 탐지 방법.<br>API 명세만 받아서 테스트를 자동으로 만들고 돌린다.
## 기본 정보
- 만든 곳: Palo Alto Networks Unit 42 (Ravid Mazon, Jay Chen)
- 공개: 블로그(2024-08), BSides Las Vegas 2024 발표
- 논문 없음. 블로그에 코드·다운로드 링크가 없고, 공개 저장소도 찾지 못함
- 입력: OpenAPI 3 명세
## 동작 방식
1. LLM이 BOLA 후보 엔드포인트를 고른다 (인증 필요 + 객체 ID 파라미터)
2. API 간 의존 관계를 찾는다 (값을 만드는 API → 값을 쓰는 API)
3. 후보까지 가는 호출 순서를 짠다
4. 두 계정 테스트 스크립트를 만든다 (A가 만든 객체에 B가 접근)
5. 실행 후 LLM이 결과를 보고, 취약해 보이면 사람이 확인한다
## 성과
- Grafana, Harbor, Easy!Appointments 등에서 새 CVE 발견
	- BSides 발표 소개: 16개
	- 블로그에 나열된 CVE를 세면: 17개 (Grafana 1, Harbor 1, Easy!Appointments 15)
	- 집계 시점 차이로 보이며, 어느 쪽이 맞는지는 확인 불가
- 알려진 BOLA가 있는 프로젝트 3개에서 **알려진 BOLA 전부 탐지**
- RESTler(기본 설정)는 0개 탐지
- RESTler 대비 요청 수 **1% 미만**
## 한계
**저자가 직접 밝힌 것**
- **명세 품질 의존**: OpenAPI 명세의 정확도에 성능이 크게 좌우된다. 경로별 보안 범위, 필수 파라미터 표시 등이 지켜져야 유효한 테스트가 나온다.
	- 출처: BSides LV 2024 발표 소개 \> "Remaining Challenges" \> "Spec quality"
- **LLM 성능 의존**: LLM에 무관하게 설계했지만, 초기 세대 LLM과 조합하면 정확도가 떨어졌다.
	- 출처: BSides LV 2024 발표 소개 \> "Lessons learned from AI partnership" \> "Not all LLMs are equal"
- **비용**: 성능 좋은 모델은 비싸고, 직접 운영하는 LLM도 고성능 GPU·CPU가 필요해 대규모 적용의 장벽이 된다.
	- 출처: BSides LV 2024 발표 소개 \> "Remaining Challenges" \> "Cost"
- **사람 검증 필수**: AI가 테스트 로그를 분석하고, 취약하다고 판단한 건은 사람이 앱 맥락에서 검증한다. 사람의 검증은 여전히 필수라고 쓴다.
	- 출처: Unit 42 블로그 \> "BOLABuster: AI-Assisted BOLA Detection" \> "5. Execute Plans and Analyze" 마지막 두 문단
	- 같은 내용: BSides LV 2024 발표 소개 \> "The use of LLMs for automating BOLA hunting" \> "Executing Plans and Analyzing Responses"
- **휴리스틱으로 되는 일에 AI는 비효율**: LLM은 불확실성과 환각 때문에, 휴리스틱으로 풀리는 일에서는 휴리스틱보다 효율·정확도가 떨어졌다.
	- 출처: BSides LV 2024 발표 소개 \> "Lessons learned from AI partnership" \> "Triumph and failure"

**외부에서 지적된 것**
- 블로그에 프롬프트 설계도, 사용한 LLM도, 결과를 뒷받침할 실증 근거도 없다.
	- 출처: Johansens, *Detecting BOLA Vulnerabilities with Large Language Models*, Univ. of Twente (2025) \> §3 Related Work \> BOLABuster를 설명한 문단의 마지막 문장

**공개 자료로 확인할 수 없는 것**
> 확인한 자료: Unit 42 블로그 본문, BSides LV 2024 발표 소개, Unit 42 Harbor·Grafana 사례 글
- **오탐률·정밀도 수치 없음**: 위 자료 어디에도 오탐률, 정밀도, 재현율 수치가 없다. 평가 결과는 "알려진 BOLA 전부 탐지", "RESTler(기본 설정) 0개", "요청 1% 미만"으로만 제시된다.
	- 위치: BSides LV 2024 발표 소개 \> "Evaluation" \> "Testing Apps with Known BOLA"
- **평가 대상 미공개**: 알려진 BOLA가 있는 오픈소스 3개로 평가했다고만 쓰고, 프로젝트 이름과 BOLA 개수는 없다. 그래서 "전부 탐지"가 몇 개 중 몇 개인지 알 수 없다.
	- 위치: BSides LV 2024 발표 소개 \> "Evaluation" \> "Testing Apps with Known BOLA"
- **판정 기준**: 각 테스트 스크립트에서 두 사용자 중 한 명이 다른 사용자의 데이터에 접근·조작하는 데 성공하면 BOLA의 지표로 본다고만 설명한다.
	- 위치: Unit 42 블로그 \> "BOLABuster: AI-Assisted BOLA Detection" \> "4. Create Test Scripts"
- **객체 상태 지정 단계 없음**: 예시(Figure 6)는 Alice가 글과 댓글을 만들고 Bob이 댓글 삭제를 시도하는 흐름이다. 만든 객체에 공개·공유 상태를 지정하는 단계는 설명되어 있지 않다. 공개 자료에 없다는 뜻이며, 내부에서 하지 않는다는 증거는 아니다.
	- 위치: Unit 42 블로그 \> "BOLABuster: AI-Assisted BOLA Detection" \> "4. Create Test Scripts" \> Figure 6과 그 설명 문단
## 우리 연구에 주는 시사점
> 이 절은 원문 내용이 아니라, 위 자료를 바탕으로 한 우리 연구 쪽 해석이다.

**1. 수치 비교 대상으로 쓸 수 없다**
- BOLABuster는 오탐률·재현율 수치와 코드를 공개하지 않았다.
- 따라서 우리 결과와 수치로 비교하는 대상은 수치와 코드가 공개된 BACScan, AuthProbe로 한다.

**2. 판정 기준만 구현해 비교 기준선으로 쓸 수 있다**
- 블로그에 적힌 판정 기준은 "한 사용자가 다른 사용자의 데이터에 접근·조작하는 데 성공하면 BOLA 지표"이다.
- 이 기준을 직접 구현해 같은 테스트 객체에 적용하면, 우리 판정 방법과 오탐 수를 비교할 수 있다.
- 이때 결과는 "BOLABuster 성능"이 아니라 "BOLABuster 블로그에 기술된 판정 기준을 재구현한 결과"로 표기한다.

**3. API 호출 순서를 정하는 방식은 실험 준비에 참고할 수 있다**
- BOLABuster는 어떤 API가 다른 API에 필요한 값(예: 생성된 객체 ID)을 만들어 주는지 분석해 호출 순서를 정했다.
- 테스트 객체를 만들고, 공개 범위를 바꾸고, 계정별로 조회하는 순서를 정할 때 같은 방식을 쓸 수 있다.
- 이는 판정 방법이 아니라 실험 준비 단계에 해당한다.

**4. 위반 판정 기준은 대상 앱이 정한 접근 규칙에서 가져온다**
- Harbor 사례에서 Unit 42는 Maintainer의 설정 변경을 위반으로 판단할 때 두 가지를 근거로 들었다. Harbor 공식 문서상 설정 변경은 ProjectAdmin만 가능하다는 점, 그리고 Maintainer로 로그인한 화면에서 설정 항목이 비활성화되어 있다는 점이다.
- 우리 판정에도 "이 계정은 이 객체를 읽으면 안 된다"는 기준이 필요하다. 이 기준을 연구자가 임의로 정하면 판정 결과의 타당성을 설명하기 어렵다.
- 따라서 기준은 대상 앱의 공식 문서나, 앱이 다른 경로에서 실제로 수행하는 접근 검사에서 가져온다.
- 예: Memos 0.9.0은 개별 메모 조회(`GET /memo/:memoId`)에서 PRIVATE 메모를 작성자가 아닌 계정에 403으로 거부한다(`server/memo.go`). 이 규칙을 기준으로 삼으면, 다른 경로에서 같은 메모가 작성자 아닌 계정에 반환될 때 위반으로 판정할 근거가 된다.
## 출처
- Unit 42 블로그 (2024-08): https://unit42.paloaltonetworks.com/automated-bola-detection-and-ai/
- BSides LV 2024 발표 소개: https://pretalx.com/bsideslv24/talk/FSYWPG/
- Harbor 사례 (2024-07): https://unit42.paloaltonetworks.com/bola-vulnerability-impacts-container-registry-harbor/
- Grafana 사례 (2024-03): https://unit42.paloaltonetworks.com/new-bola-vulnerability-grafana/
- Johansens, *Detecting BOLA Vulnerabilities with LLMs*, Univ. of Twente (2025), §3: https://essay.utwente.nl/fileshare/file/107423/Johansens_BA_BIT.pdf
- Memos v0.9.0 `server/memo.go` (시사점 4의 예시): https://raw.githubusercontent.com/usememos/memos/v0.9.0/server/memo.go

⇒ 음 대충 얘는 명세서의 품질에 크게 좌우하는게 단점이 될 수 있을 것 같습니다. 

---

# 2. AuthzTrace 정리
[노션 북마크](https://app.notion.com/p/3ed93f3d1096807a8f0ec9cee83ce8c8#3ed93f3d1096804eaa6efca82708ff3e)
> 테스트 계정, 테스트 객체의 소유자, 엔드포인트별 허용 계정을 사람이 "계약" 파일에 적으면,<br>그 계약과 실제 응답을 대조해 BOLA를 판정하는 오픈소스 도구.
## 기본 정보
- 만든 사람: Mohamed Taha Slimani (GitHub @Asttr0). PyPI 관리자 1명
- 공개: GitHub 저장소, PyPI 패키지, GitHub Action (MIT 라이선스)
- 관련 논문은 찾지 못함. README 기준으로 REST 권한 회귀 테스트에 초점을 둔 CI(지속적 통합)용 도구
- 버전: 0.1.0(2026-07-09) → 0.6.0(2026-07-14)
	- CHANGELOG상 7개 버전, GitHub 릴리스 6개, PyPI 배포 이력 4개(0.3.1부터)
- 저자 표현: 알파 단계
- 입력: 계약 파일(YAML). OpenAPI 명세는 선택 사항
## 동작 방식
1. 사람이 계약 파일에 세 가지를 적는다
	- 계정: alice, bob, 비로그인(anon)과 각 인증 정보
	- 테스트 객체: 계정별 객체 ID와 표식 문자열 (예: alice의 `inv_A`, 표식 "Alice private")
	- 엔드포인트 규칙: 예) `GET /api/invoices/{id}`는 `allow: [owner]`
		- 허용 대상: `owner`, 특정 계정 이름, `authenticated`(로그인 사용자), `anonymous`, `all`
2. 엔드포인트 × 객체 × 계정 조합을 전부 만든다
3. 허용된 계정의 조회가 먼저 성공하는지 확인한다 (사전 확인)
4. 거부돼야 할 계정으로 요청을 보내 판정한다
	- 계약에 정한 거부 상태 코드(README 예시에서는 401·403·404)가 아니면 → BOLA
	- 거부됐어도 응답에 소유자 표식이나 금지 필드가 있으면 → 누출
5. 결과를 분류해 보고한다: `bola`, `leak`, `setup`, `over_restrictive`, `unsafe_skipped`

**명세 사용 여부**
- 명세는 계약 초안을 만드는 데만 쓴다 (`authztrace init --from openapi.yaml`). 저자는 이 기능이 권한을 추론하는 기능이 아니라 시작점이라고 밝힌다.
- 명세가 없으면 예제 계약 파일에서 시작해 사람이 직접 적는다.
- 판정 근거는 명세가 아니라 계약 파일이다.
## 현황
- README·CHANGELOG에 실제 앱 평가 결과나 발견한 CVE에 대한 언급이 없음
- 저장소에 있는 검증은 일부러 취약하게 만든 Flask 데모 API와 CI 스모크 테스트뿐
- GitHub 스타 2개, 포크 0개 (2026-10-02 확인 시점)
## 한계
**저자가 직접 밝힌 것**
- **알파 단계, 고정 테스트 객체 전제**: 고정된 테스트 객체와 로그인 정보를 쓰는 REST 권한 회귀 테스트에 초점을 둔다.
	- 출처: GitHub README \> "Current scope"
- **소스 분석은 FastAPI만**: 동적 라우트 등록, 임의의 서비스 계층 정책, 요청 본문 분석, 다른 프레임워크는 지원하지 않는다.
	- 출처: GitHub README \> "Current scope"
- **미지원 패턴**: 순차 ID 열거, 소유자 필드 조작(mass assignment), GraphQL, 메서드 우회 헤더는 계획 단계다.
	- 출처: GitHub README \> "Current scope" / docs/CORPUS.md 표 9~12번
- **부분 지원 패턴**: 403/404 차이는 경고만 하고, 수직 권한 상승은 특정 계정 지정만 가능하며 역할 개념은 다음 단계다.
	- 출처: docs/CORPUS.md 표 4번, 5번
- **수정·삭제 요청은 기본으로 건너뜀**: 자동 실행은 GET·HEAD·OPTIONS만 하고, 나머지는 `safe: true` 표시나 `-include-unsafe` 옵션이 있어야 실행한다.
	- 출처: GitHub README \> "Built for trustworthy CI" \> "Read-only default"
- **권한 규칙은 사람이 정함**: 도구가 권한 규칙을 추측하지 않는다. 소유자 검사 코드가 없다고 해서 다른 사용자 접근이 의도된 것으로 보지 않고 "미해결"로 남긴다.
	- 출처: docs/CORPUS.md \> "Design principle" / CHANGELOG.md \> 0.6.0

**외부에서 지적된 것**
- 찾지 못함. 2026년 7월에 나온 도구라 리뷰나 인용을 확인하지 못했다.

**공개 자료로 확인할 수 없는 것**
> 확인한 자료: GitHub README, docs/CORPUS.md, CHANGELOG.md, PyPI 페이지
- **오탐률·재현율 수치 없음**: 실제 앱 평가가 없다. 검증은 데모 API 대상 CI 스모크 테스트뿐이다.
	- 위치: CHANGELOG.md \> 0.1.0, 0.3.1
- **계약 밖의 객체는 검사하지 않음**: 검사는 계약에 적은 객체로만 만들어진다. 계약에 없는 객체를 판정하거나 보류하는 단계는 설명되어 있지 않다.
	- 위치: GitHub README \> "The contract"
- **같은 엔드포인트 안에서 객체별 공개 범위 차이**: 예시 계약은 허용 규칙을 엔드포인트에 붙이고, 객체는 계정당 하나씩 적는다. "A의 공개 메모"와 "A의 비공개 메모"를 같은 엔드포인트에서 다르게 다루는 예시는 없다. 리소스를 나눠 정의하면 될 것으로 보이지만 확인하지 않았다.
	- 위치: GitHub README \> "The contract"
## 우리 연구에 주는 시사점
> 이 절은 원문 내용이 아니라, 위 자료를 바탕으로 한 우리 연구 쪽 해석이다.

**1. 우리 판정 절차의 핵심이 이미 도구로 구현되어 있다**
- 진단 계정이 만든 고정 테스트 객체, 응답과 별도로 적은 권한 기록과의 대조, 합성 표식으로 실제 객체 반환 확인, 근거 없는 권한을 추측하지 않는 원칙이 AuthzTrace에 있다.
- 브리핑의 차별성 후보인 "관찰 결과와 권한 의도를 구분한다"만으로는 새롭다고 주장하기 어렵다.
- AuthzTrace를 선행 도구로 인용하고, 차별성을 다시 정해야 한다.

**2. 남는 차별성 후보**
- 테스트 객체 밖의 객체(미표시 객체)를 응답 필드 근거로 확정하거나 보류하는 판정
- 설정 근거 기반 판정이 관찰 기반 방법(BACScan식 공개 필터, AuthProbe식 목록 소유권)보다 실제 앱에서 오탐을 얼마나 줄이는지, 그 대가(준비 비용, 보류율)는 얼마인지 측정하는 연구
- 허용 근거의 출처: AuthzTrace는 사람이 기대 권한을 직접 적는다. 브리핑은 앱에서 실제로 설정한 공개 범위·공유 대상과 설정 성공 근거를 기록해 허용 여부를 정한다. 이 차이가 연구 기여로 충분한지는 팀 검토가 필요하다.

**3. 실험 도구로 쓸 수 있다**
- 코드가 공개되어 있고 바로 실행할 수 있다.
- Gitea·Memos 테스트 객체를 AuthzTrace 계약으로 적어 돌리면, "사람이 적은 권한 기록 기반 판정"의 실제 구현으로 비교에 쓸 수 있다.
- 계약 작성에 걸린 시간과 항목 수는 브리핑의 "준비 비용" 측정에도 쓸 수 있다.

**4. 사전 확인(preflight) 방식은 참고할 만하다**
- 허용된 계정의 조회가 먼저 성공해야 거부 검사를 돌린다. 테스트 객체 준비가 잘못돼서 생기는 거짓 "정상" 판정을 막기 위해서다.
- 브리핑의 "설정 시각과 설정 성공 근거를 남겨 진단 직전 상태를 확인한다"와 같은 목적이다.
## 출처
- GitHub 저장소 README: https://github.com/Asttr0/AuthzTrace
- docs/CORPUS.md: https://raw.githubusercontent.com/Asttr0/AuthzTrace/main/docs/CORPUS.md
- CHANGELOG.md: https://raw.githubusercontent.com/Asttr0/AuthzTrace/main/CHANGELOG.md
- PyPI: https://pypi.org/project/authztrace/
- PyPI 0.5.0 (명세 기능 설명): https://pypi.org/project/authztrace/0.5.0/
