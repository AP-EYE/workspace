# 메서드 분리 실행 재현

Akto 전체 실행이 아니다. 고정 커밋의 Java 메서드 본문을 그대로 추출하고 입력·필드·출력용 틀을 붙여 실행한다. 길이·90% 조건은 실험 코드에서 재구성한다. 실제 YAML 엔진과 DB 경로는 실행하지 않는다.

## 준비와 실행

Python 3, Git, JDK 8 이상과 Maven Central 접근이 필요하다. java·javac가 실행 경로에 있어야 한다. Maven 설치는 필요 없다. 레포 루트에서 실행한다.

```powershell
git clone https://github.com/akto-api-security/akto.git .runtime/akto-audit-20261004/upstream
git -C .runtime/akto-audit-20261004/upstream checkout 302dad92e1549b7a84ce73eded447ad5d18124f0
git clone https://github.com/akto-api-security/tests-library.git .runtime/akto-audit-20261004/tests-library
git -C .runtime/akto-audit-20261004/tests-library checkout ce2267da7e28927876b41d944e63bdde10e41e00
python docs/akto/reproduction/run_checks.py --source .runtime/akto-audit-20261004/upstream --templates .runtime/akto-audit-20261004/tests-library --work .runtime/akto-audit-20261004/jvm-checks --output docs/akto/evidence/2026-10-04-component-results.json
```

기존 clone은 다시 만들지 않는다. HEAD 고정값을 검사하지만 작업 트리 변경은 검사하지 않으므로 깨끗한 원본을 사용한다. 파일·메서드·템플릿 해시를 결과에 기록한다. 실험 파일은 Git에서 제외되는 .runtime에 둔다.

## 범위와 제한

- 원본 메서드: compareWithOriginalResponse, extractAllValuesFromPayload 2개 overload, isPhoneNumber, getIsPrivate, RegexPredicate.validate.
- 메서드의 ObjectMapper·필드·상수 등은 실험 틀로 제공한다.
- 입력 20개: 응답 9개, 전화번호 4개, 한국어 형식 4개, 문장 키워드 2개, STI 새 객체 대입 1개.
- 핵심 기대 결과와 원본 덮어쓰기 코드 존재에 대해 8개 assertion.
- Jackson 2.16.1, libphonenumber 8.12.41을 다운로드하고 게시된 SHA-1과 대조한다. SHA-256도 기록한다.
- 전화번호·정규식은 해당 메서드 결과다. UI 등록과 runtime 전체 분류 결과가 아니다.
- 공개 10/10 STI의 교체는 원본 getIsPrivate와 같은 대입문을 실행한다. DB 조회·URL fallback 전체는 미실행이다.
- 전체 테스트 통과, BOLA 확정, 법적 분류, 제품 오탐률을 주장하지 않는다.

[실행 결과](../evidence/2026-10-04-component-results.json)와 [해석](../2026-10-04-akto-deep-analysis.md)을 함께 읽는다. 기록일은 고정된 2026-10-04 실험을 나타낸다.
