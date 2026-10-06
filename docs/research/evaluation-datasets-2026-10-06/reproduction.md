# 실행 범위와 재현 방법

실행일 2026-10-06. Windows / Python 3.12의 별도 가상환경과 격리한 공식 Docker 이미지를 사용했다. 논문 수치와 이번 실행 수치는 [본문](README.md)에서 구분했다.

## 실제 실행한 것

| 대상 | 고정 commit | 방식 |
|---|---|---|
| AuthProbe | `d9cb4bdd7fabbf56d91935034a245ac8092d0fe6` | 저자 pytest 11개, 저자 FastAPI 두 대상의 localhost HTTP 실행, 논문의 m=3 조건 |
| VAmPI | `f16052dce83f05847133ec98f01c5193a41de7d8` | 임시 복사본·합성 DB·Flask/Connexion test client로 책 조회 확인 |
| wger 2.4/2.5 | 공식 `wger/server` image digest를 [실행 패키지](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md)에 고정 | 각 버전의 빈 SQLite에 두 합성 계정·비공개 객체를 만들고 원본 Django GET 경로를 DRF APIClient로 실행. 영양 8요청·반복 설정 목록 8요청의 취약/수정 차이 확인 |
| wger 2.7 공개 template | 공식 `wger/server:2.7` image digest를 [실행 패키지](appendices/authz/real-app/public-normal/README.ko.md)에 고정 | 네트워크 없는 컨테이너의 Django test runner로 원본 `test_templates` 8개 실행·통과. 비소유자 공개 detail GET 200·동일 ID 포함 |
| K-PII-Bench | 코드 `1b480c515cc8425ea5c5675079bd7cf17b951554` | 공개 HF Dataset Viewer의 126건 형식·BIO 검사, 이후 별도 span helper의 반복 출현 반례 **실행**. 공식 모델/전체 데이터 성능은 미실행 |
| ko-pii | `9516cabd6f582935cae1536ccbd8c5448afae679` | 합성 540건 전체에 원본 오프라인 규칙과 저자 scorer·추가 표면형 scorer **실행**. [입력·스크립트·라이선스·명령](appendices/pii/REPRODUCTION.md) |
| OpenPII 1.5M | 당시 Hub SHA `a785eb528e28be2693c3718a27e066970de5dadb` | 저장된 first-rows 편의 표본에서 한국어 16건/113 span offset **감사**. Viewer 요청 자체는 revision 고정이 아니므로 보존 JSON을 입력으로 식별 |

K-PII-Bench 코드 commit과 데이터 revision은 같은 것이 아니다. 이번 Dataset Viewer는 조회 시점의 공개 응답이다. 원본 응답 SHA-256을 결과에 남겼지만, 고정 Hub revision으로 전체 데이터를 내려받은 것은 아니다. 본 실험 전에 데이터 revision을 별도 동결해야 한다.

## AuthProbe

소스의 `targets/`, `_serve.py`, scanner/probe 및 tests를 읽은 뒤 실행했다. 실제 사용한 가상환경의 패키지 목록은 [authprobe-environment.txt](evidence/authprobe-environment.txt)에 있다. markitdown 등 PDF 처리용 패키지도 같은 환경에 설치되어 있어 목록이 검사기 최소 의존성보다 길다.

로컬 작업 기준 경로는 `C:\Users\andyw\Desktop\AP-EYE`다. 저장소만 공유받은 경우 `--source`, `--output`을 자신의 clone/출력 경로로 바꾸면 된다.

```powershell
# 소스 clone에서 실행한 저자 테스트
Push-Location 'local-materials/evaluation-datasets-2026-10-06/sources/AuthProbe'
& '../../.venv/Scripts/python.exe' -m pytest -q
Pop-Location

# 이번 조사용 재현 harness: 대상 코드는 바꾸지 않는다.
& 'local-materials/evaluation-datasets-2026-10-06/.venv/Scripts/python.exe' -X utf8 `
  'team_hub/docs/research/evaluation-datasets-2026-10-06/scripts/reproduce_authprobe.py' `
  --source 'local-materials/evaluation-datasets-2026-10-06/sources/AuthProbe' `
  --output 'local-materials/evaluation-datasets-2026-10-06/evidence/authprobe-reproduction.json'
```

새 환경에서는 Python venv를 만들고 `requests`, `pyyaml`, `fastapi`, `uvicorn`, `pytest`를 설치한다. 이번 환경의 직접 관련 버전은 requests 2.34.2, PyYAML 6.0.3, FastAPI 0.142.2, uvicorn 0.54.0, pytest 9.1.1이다. 완전 동일 의존성이 필요하면 환경 목록을 따른다.

기대되는 이번 결과: 취약 대상 `bola=6, enumerable_id=1, idor=1`; 수정 대상 finding 없음. 각각 GET item 12건과 GET collection 2건을 독립 확인한다. 각 객체에 별칭을 붙였고 실제 인증 헤더나 응답 본문은 보고서에 저장하지 않는다.

주의: AuthProbe의 기본 `demo.py`는 사용자당 객체 1개를 만든다. 이번 harness는 논문의 주요 표와 맞추어 **3개**를 만든다. 기본 demo의 finding 개수와 다른 것이 곧 재현 실패는 아니다. 매 실행마다 대상 상태를 초기화하고 서버 context를 종료한다. 측정 목적이 아니므로 실행 시간을 논문 속도와 비교하지 않는다.

## VAmPI

공개 README, `config.py`, `api_views/books.py`, 사용자 인증 함수, DB 모델을 읽었다. 소스의 의존성 파일을 별도 venv에 설치했다. 이번 환경은 Connexion 2.14.2, Flask 2.2.2, Flask-SQLAlchemy 3.0.3, SQLAlchemy 2.0.2, PyJWT 2.6.0, Werkzeug 2.2.3이다. 설치 시 `werkzeug<3`도 명시했다. [전체 환경](evidence/vampi-environment.txt)

```powershell
& 'local-materials/evaluation-datasets-2026-10-06/.venv-vampi/Scripts/python.exe' -X utf8 `
  'team_hub/docs/research/evaluation-datasets-2026-10-06/scripts/reproduce_vampi.py' `
  --source 'local-materials/evaluation-datasets-2026-10-06/sources/VAmPI' `
  --output 'local-materials/evaluation-datasets-2026-10-06/evidence/vampi-reproduction.json'
```

원본을 임시 디렉터리에 복사하고 DB 경로가 그 안에 있음을 확인한다. 두 사용자와 사용자당 한 권의 책을 만든 뒤 upstream 책 handler의 기존 `vuln` 플래그를 1/0으로 전환한다. 서버 전체의 환경변수를 바꾸어 재기동한 실험은 아니고, 책 조회 경로의 두 원본 분기를 실행한 검사다. 네트워크 소켓으로 Akto에 연결한 전체 시스템 실험도 아니다.

검증 행렬:

| 모드 | 요청 | 정책상 기대 | 관측 |
|---|---|---|---|
| 취약 | Alice→Alice, Bob→Bob 책 | 허용 | 200, 해당 비공개 내용 있음 |
| 취약 | Alice→Bob, Bob→Alice 책 | 비공개 내용 차단 | 200, 타인 비공개 내용 있음: BOLA |
| 수정 | Alice→Alice, Bob→Bob 책 | 허용 | 200, 해당 비공개 내용 있음 |
| 수정 | Alice→Bob, Bob→Alice 책 | 차단 | 404, 비공개 내용 없음 |
| 두 모드 각각 | 익명→전체 책 목록 | 제목·사용자 공개, 비공개 내용 제외 | 200, 2개 책, secret 필드 없음: 정상 |

총 10건이 예상과 일치했다. 토큰·암호는 메모리에서만 사용하고 결과에는 넣지 않았다. 종료 시 DB 연결과 임시 복사본을 정리했다. 원본 인증/인가 로직에 패치는 없다.

## wger 공식 취약·수정 이미지

[공식 영양 조회 공지](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)와 [반복 목록 공지](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm)를 기준으로, 공식 이미지 `2.4`와 `2.5`를 각각 네트워크 없는 임시 컨테이너에서 실행했다. 자체 fixture는 두 계정의 소유 관계와 반환 고유값을 고정한다. 원본 view·queryset·serializer를 통과한 총 16개 GET 응답에서 영양 교차 조회는 `2.4=200/타인 값`, `2.5=404`, 반복 설정 두 목록은 `2.4=자기+타인`, `2.5=자기만`이었다. 두 결함은 **2개 CVE family**다.

이미지 digest, 경로, 요청별 JSON, 재실행 명령, 결과 검증기와 해시를 [wger 재현 패키지](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md)에 보존했다. `APIClient.force_authenticate`로 요청자를 주입했으므로 로그인·토큰 발급/검증이나 외부 네트워크 공격은 시험하지 않았다. 이 실행은 **평가 정답 확보**이며 Akto·RESTler 탐지율이 아니다. 영양 공지의 나머지 meal/mealitem 두 경로는 남아 있다.

공개 정상군은 [wger 공식 2.7 이미지의 원본 maintainer 테스트 실행](appendices/authz/real-app/public-normal/README.ko.md)으로 별도 확인했다. `test_public_template_detail_api`는 로그인 사용자가 소유하지 않은 공개 객체를 목록에서 고른 뒤 상세 GET **200·같은 ID**를 assert하고 통과했다. 자기 template 상세 GET도 200·동일 ID다. 테스트 8/8이 통과했으며 로그·digest·원본 소스 revision·재실행 스크립트를 보존했다. 이 snapshot은 공개 정상 접근을 추가한 커밋보다 **36커밋 후속**이고 2.4/2.5 CVE 실행과 다른 버전이다. 따라서 같은 버전의 양성/음성 쌍이나 Akto의 오탐률로 합산하지 않는다.

## K-PII-Bench 표본

Hugging Face datasets 스킬의 읽기 API 흐름으로 split을 확인했다.

```text
GET https://datasets-server.huggingface.co/splits?dataset=woohyun212%2Fk-pii-bench
GET https://datasets-server.huggingface.co/first-rows?dataset=woohyun212%2Fk-pii-bench&config=default&split=train
GET https://datasets-server.huggingface.co/first-rows?dataset=woohyun212%2Fk-pii-bench&config=default&split=dev
GET https://datasets-server.huggingface.co/first-rows?dataset=woohyun212%2Fk-pii-bench&config=default&split=test_track_a
```

처음 `/rows?offset=0&length=100` 요청은 HTTP 500으로 실패했고 `/first-rows`로 전환했다. 실제 받은 문서는 train 41, dev 41, test 44건이다. 임의로 100개씩 검사했다고 보고하지 않는다. 각 split의 첫부분이므로 랜덤 표본도 아니다.

```powershell
python -X utf8 `
  'team_hub/docs/research/evaluation-datasets-2026-10-06/scripts/audit_kpii_samples.py' `
  --samples 'local-materials/evaluation-datasets-2026-10-06/evidence' `
  --output 'local-materials/evaluation-datasets-2026-10-06/evidence/k-pii-sample-audit.json'
```

126문서·541 entity의 문자 범위/표면 문자열, token/tag/offset 배열 길이, 표본 내 template ID 교집합을 검사했다. 후속 재감사에서 제공 BIO를 문자 gold로 다시 계산해 불일치 0을 확인하고, 표본의 문맥 라벨 오류 후보와 별도 scorer 반례를 기록했다. 모두 entity가 있는 표본이어서 PII가 전혀 없는 음성 문서 비율은 평가할 수 없다. 전체 template 중복·모델 성능을 검사한 결과가 아니다. 재현용 first-rows는 [PII 입력 폴더](appendices/pii/inputs)에 출처·라이선스와 함께 보존했다.

## 실행하지 않은 것

- 전체 Akto를 두 외부 대상에 연결한 비교 실험, 수정 Akto/새 탐지기 구현.
- BACScan 전체 pipeline, 논문 속 44개 취약점/20개 앱 재현, Memos/Lunary의 CVE별 수정 전후 실험.
- wger 영양 취약점의 나머지 meal/mealitem 두 GET 경로, 그리고 취약·수정 사례와 같은 앱 snapshot에서 더 다양한 공개·명시적 공유 정상 정책의 확인.
- EvoMaster 52개 API 전체 평가와 논문 시간/검출 수 재현.
- 한국어 PII **NER 모델 학습·추론** 및 Akto/Presidio/제안 방식의 동일 조건 비교. ko-pii 규칙은 540건에서 저자 방식 F1을 실제 측정했으므로 미실행으로 묶지 않는다.
- K-LegalDeID/Thunder-DeID 전체 자산 다운로드와 학습 재현.
- 독립 한국어 합성 평가셋 제작, 전체 데이터의 의미 주석 검수.

위 항목들은 과제를 위해 앞으로 필요한 실험과 현재 사실을 구분하기 위한 실행 범위 기록이다. 이번 과제의 완료 범위는 외부 기준 조사, 일부 재현 가능성 확인, 한국어 규칙 기준선, 비교·평가 설계와 한 줄 정의다. 추가 상세 원문·실행 상태는 [최신 팀 보고서](README.md)를 따른다.
