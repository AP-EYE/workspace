# Akto 조사 자료 안내

조사일: 2026-10-06 KST. 먼저 `AKTO-DEEP-RESEARCH.html`을 브라우저로 연다. 상단에서 수정 이력·문헌 검토·전체 이슈 검색으로 이동할 수 있다. 각 보고서는 수정 가능한 `.ko.md` 원본도 제공한다.

| 파일 | 내용 |
|---|---|
| AKTO-DEEP-RESEARCH.html / .ko.md | 제품·구조·수정 이력·국가별 PII·정확도·AP-EYE 실행 순서 |
| HISTORY-REVIEW.html / .ko.md | 본체 35개 주요 PR, 템플릿 11개 주요 PR의 상태·변경 의미와 확보한 PR 전체 표 |
| PAPER-NOTES.html / .ko.md | 원문 읽기 수준·평가 설정·인용 한계 |
| ISSUE-EXPLORER.html | 본체 6,581 + tests-library 347건 검색·필터·원본 링크 |
| ISSUE-PR-INDEX.csv | 같은 6,928건의 간결한 목록. 본문 제외, CSV 수식 시작 문자 보호 |
| EVIDENCE-MANIFEST.json | 소스 commit·원본 출처·수집 범위·파일 SHA-256 |
| evidence/probes/ | 원본 Java 메서드·규칙으로 실행한 63개 PII 입력 및 6개 비교 입력 |
| evidence/github/ | 원시 GitHub 수집 JSON과 상세 patch·댓글. 외부 사용자의 주장이 포함됨 |
| sources/ | 조사용 고정 소스 checkout 및 공개 원문 PDF·문서 |

HTML에는 CDN·추적·외부 JavaScript가 없다. 폴더 안에서 정적으로 열 수 있으며 원본 링크를 클릭할 때는 인터넷이 필요하다. 원시 GitHub 본문에는 스팸·공개 개인정보가 포함될 수 있으므로 일반 열람은 간결한 검색 페이지를 사용한다.

## 재현 범위

PII 진단은 전체 classifier가 아닌 원본 전화번호 메서드·원본 정규식의 단독 실행이다. BOLA 진단은 원본 JSON 값 추출·응답 비교 메서드의 단독 실행이다. 서비스 전체 배포·실제 대상 API·외부 PII 서비스 호출·한국어 비교 모델 실행은 NOT_RUN이다.

```powershell
# 이 README가 있는 폴더에서, 조사 당시 사용한 Python 3.12 / JDK 21 환경
python scripts/component_probe.py
python scripts/bola_probe.py
```

스크립트에는 조사 PC의 JDK 경로가 명시돼 있다. 다른 PC에서는 해당 경로를 맞춰야 한다. 의존성 JAR은 이 폴더에 보존돼 있으며 누락된 경우 공개 Maven 저장소에서 지정 버전을 내려받는다. 결과를 재실행해 바꿨다면 이전 manifest와 동일한 snapshot이 아님에 유의한다.

`build_appendices.py`는 보존된 JSON에서 이력·안전한 공개 목록을 만든다. `render_reports.mjs`는 설치된 marked로 HTML을 만든다. `check_artifacts.mjs`는 기존 Edge의 headless 모드로 표시·검색·페이지 이동을 검사한다. Node 패키지 경로 역시 조사 PC의 bundled runtime 위치다. `finalize_evidence.py`가 참조·개수·소스 경로·hash를 확인한다.

수집용 스크립트는 GitHub CLI 인증과 인터넷을 사용하며 기존 JSON을 재사용한다. 새 기준일의 자료를 수집하려면 별도의 새 조사 디렉터리에 저장해야 한다. 이 폴더의 고정 근거를 덮어쓰며 최신 조사라고 부르지 않는다.

Team Hub 및 제품 코드에는 변경·commit·push하지 않았다. 이 폴더는 조사 자료다.
