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

## 2026-10-05: 실제 DAO와 기존 설정 검증

[후속 결과](../2026-10-05-candidate-validation.md), [실행 환경·원본 해시](../evidence/2026-10-05-run-provenance.json).

추가 준비: Docker 엔진, Maven 3.9.11, Buf 1.73.0, protoc 3.25.5. 각 도구는 실험 폴더에만 다운로드했고 시스템 설정은 바꾸지 않았다. 원본 pom의 make 실행은 건너뛰되 Buf로 생성 코드를 먼저 준비했다.

도구 원본:

- [Maven 배포본](https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.11/apache-maven-3.9.11-bin.zip), 게시 SHA-512 대조.
- [Buf Windows 실행 파일](https://github.com/bufbuild/buf/releases/download/v1.73.0/buf-Windows-x86_64.exe).
- [protoc Windows 실행 파일](https://repo.maven.apache.org/maven2/com/google/protobuf/protoc/3.25.5/protoc-3.25.5-windows-x86_64.exe), 게시 SHA-1 대조.

아래 예는 도구가 `.runtime/akto-audit-20261005/tools/`에 준비된 상태에서 레포 루트 기준으로 실행한다. 해당 폴더에 buf.exe와 protoc.exe를 두고 Maven 배포본을 푼다. MongoDB는 이 실험 전용이다. 이미 같은 이름의 컨테이너를 만들었다면 `docker start ap-eye-akto-audit-20261005`를 사용한다.

```powershell
docker run --detach --name ap-eye-akto-audit-20261005 --publish 127.0.0.1:27105:27017 mongo:7.0.4
$auditRoot = (Get-Location).Path
$auditSource = Join-Path $auditRoot '.runtime/akto-audit-20261004/upstream'
$auditTools = Join-Path $auditRoot '.runtime/akto-audit-20261005/tools'
$env:PATH = $auditTools + ';' + $env:PATH
Copy-Item -LiteralPath docs/akto/reproduction/UrlPrivateContextAuditTest.java -Destination "$auditSource/libs/utils/src/test/java/com/akto/test_editor/filter/UrlPrivateContextAuditTest.java"
Push-Location $auditSource
buf generate protobuf --template buf.gen.yaml
& "$auditTools/apache-maven-3.9.11/bin/mvn.cmd" -B -ntp "-Dmaven.repo.local=$auditRoot/.runtime/akto-audit-20261005/m2" -pl libs/utils -am test '-Dtest=UrlPrivateContextAuditTest' '-Dsurefire.failIfNoSpecifiedTests=false' '-Dexec.skip=true' '-Daudit.variant=baseline' "-Daudit.output=$auditRoot/docs/akto/evidence/2026-10-05-url-baseline.json"
Pop-Location
python docs/akto/reproduction/run_url_context.py --source .runtime/akto-audit-20261004/upstream --report .runtime/akto-audit-20261004/upstream/libs/utils/target/surefire-reports/TEST-com.akto.test_editor.filter.UrlPrivateContextAuditTest.xml --work .runtime/akto-audit-20261005/url-variants --output docs/akto/evidence
javac -encoding UTF-8 -cp .runtime/akto-audit-20261005/url-variants/classpath.jar -d .runtime/akto-audit-20261005/url-variants/runner docs/akto/reproduction/ExistingSettingsAudit.java
java '-Dfile.encoding=UTF-8' -cp '.runtime/akto-audit-20261005/url-variants/runner;.runtime/akto-audit-20261005/url-variants/classpath.jar' ExistingSettingsAudit .runtime/akto-audit-20261004/tests-library/Broken-Object-Level-Authorization/BOLAByChangingAuthToken.yaml docs/akto/evidence
docker stop ap-eye-akto-audit-20261005
```

Maven의 BUILD SUCCESS만으로 실행을 판정하지 않는다. 실제 보고서의 테스트 수 1·실패 0·오류 0을 확인해야 한다. 이번 실행에서 JUnit 5를 사용했다. 변형 실행 스크립트도 이 조건과 고정 소스를 검사하며 원본 운영 소스를 바꾸지 않는다. 출력은 원본·한 줄 제거·분기 보완 각각 8개 사례다.

기존 설정 실험은 사용자 정의 유형을 DAO로 저장하고 fetchCustomDataTypes·KeyTypes를 사용한다. UI 등록은 실행하지 않는다. 목록 실험은 실제 YAML validate 노드와 대체 contains_all 조건을 원본 ConfigParser·Filter에서 비교한다. API 선택이나 HTTP 재전송은 실행하지 않는다.

자세한 조건과 합성 입력은 Java 파일에 있다. 정상 종료 시 시험용 STI·사용자 정의 유형을 제거하며, 실패 시 fixture가 전용 실험 DB에 남을 수 있다. 이 컨테이너를 제품이나 개인 데이터 저장용으로 사용하지 않는다. 실험 종료 후 전용 컨테이너를 중지했고 데이터·생성 코드·도구는 무시되는 실험 폴더에 남겼다.
