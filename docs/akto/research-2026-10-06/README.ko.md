# Akto 심층 조사 자료

조사 기준: 2026-10-06. [본문 보고서](AKTO-DEEP-RESEARCH.ko.md)는 제품 구조, 유지보수, 6,581개 본체 이슈·PR 목록에서 선별한 변경, BOLA와 PII 소스, 국가별 탐지 방식, AP-EYE 기여 후보를 설명한다. [HTML 보고서](AKTO-DEEP-RESEARCH.html)로도 읽을 수 있다. 이 조사와 태스크 2·4의 [최신 프로젝트 방향·평가 보고서](../../research/evaluation-datasets-2026-10-06/README.md)를 함께 읽는다. 최신 보고서가 **읽기 BOLA를 본체·한국어 PII를 별도 확장**으로 좁힌 결정을 설명한다.

| 자료 | 내용 |
|---|---|
| [Akto 심층 조사](AKTO-DEEP-RESEARCH.ko.md) | 제품·구조·컴포넌트 실행·국가별 PII·정확도 비교·기여 후보 |
| [수정 이력](HISTORY-REVIEW.ko.md) | 관련 본체/테스트 정의 PR의 이전 문제·변경·병합/미병합 상태 |
| [문헌 기록](PAPER-NOTES.ko.md) | 원문 읽기 수준·실험 분모·한계 |
| [이슈·PR 검색 HTML](ISSUE-EXPLORER.html)와 [CSV](ISSUE-PR-INDEX.csv) | 본체 6,581건과 tests-library 347건의 당시 수집 목록. HTML은 로컬 정적 페이지 |
| [소스 컴포넌트 결과](probe-evidence/results.json)·[BOLA 비교 결과](probe-evidence/bola-results.json) | 전화번호/PII 63개 입력과 응답 비교 6개 입력의 진단 결과. 전체 Akto 서비스 실행 아님 |
| [공유본 파일 manifest](SHARED-COPY-MANIFEST.json) | 현재 Git 공유 폴더에 들어 있는 파일의 SHA-256. 수정된 Markdown/HTML도 이 목록으로 검증 |
| [원래 조사 manifest](EVIDENCE-MANIFEST.json) | 최초 로컬 조사 시점의 source·해시·수집 상태 기록. 이후 이 Git 공유본의 Markdown/HTML은 최신 팀 방향에 맞춰 수정했으므로 원래 manifest의 해당 두 파일 hash는 현재 공유본에 적용되지 않음. 대용량 원시 GitHub 응답·외부 checkout·JAR는 이 Git 공유본에 없음 |

원시 수집 JSON, 고정 소스 checkout, 재실행 스크립트/의존성은 이 PC의 `C:\Users\andyw\Desktop\AP-EYE\local-materials\akto-research-2026-10-06`에 보존되어 있다. 공유된 문서만으로 전체 Akto 배포·외부 대상 스캔이 완료됐다고 보지 않는다. 특히 소스의 응답 비교 함수가 배열 안 객체 연결을 잃는 구성요소 사례는 **전체 BOLA 경고의 오탐·미탐을 증명하지 않는다**. 실제 전체 기준선의 필수 증거는 [평가 보고서](../../research/evaluation-datasets-2026-10-06/README.md)에 정리했다.
