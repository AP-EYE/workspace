# AP-EYE 태스크 2·4: 팀 결정 요약

조사 기준 2026-10-06. [원문·실행·한계 전체 보고서](README.md)와 [재현 명령](reproduction.md)을 함께 공유한다.

## 이번에 정할 연구 범위

**읽기·조회 BOLA 판정을 연구 본체로, 한국어 PII 분류를 별도 확장으로 둔다.** 교수 피드백의 “한 단계만 본체”와 Akto 기여 우선·외부 평가 자료 확보 요구에 맞는다. PII가 없어도 타인의 비공개 운동·영양 객체 조회는 인가 위반일 수 있다. [9월 30일 질의응답](../../../review/2026-09-30%20조재현%20교수님%20질의응답.md) · [10월 2일 검토](../../../review/2026-10-02-최한림-조재현.md)

> 기존 Akto는 트래픽 기반 API 식별과 인증 교체형 BOLA 테스트를 제공한다. 우리는 공개·공유 객체와 금지 객체가 섞인 **읽기 응답에서 객체별 권한 근거와 실제 반환 내용을 대응시키는 판정**을 보강하고, **AuthProbe·VAmPI 기능 회귀와 wger 2.4/2.5 취약·수정 및 2.7 공개 정상 사례**에서 **종단 재현율·정상 유형별 오탐률·판정 커버리지·근거 입력 비용**으로 평가한다.

이 문장의 ‘보강’은 아직 **가설**이다. Akto 원본의 실제 실패와 개선판의 우수성은 측정 전이다. [Akto 원본 기능·이슈·수정 이력](../../akto/research-2026-10-06/README.ko.md)

## 태스크 2: 바로 쓸 정답과 보류할 후보

| 평가 용도 | 확인한 외부 자료와 이번 실행 | 채택 조건 |
|---|---|---|
| 기능 회귀 | [AuthProbe](https://github.com/jbarach2012/AuthProbe) 원본 테스트 11개 통과, 28개 정책 응답. 취약 BOLA **6요청은 결함 1개**. [VAmPI](https://github.com/erev0s/VAmPI) 책/공개 목록 10응답 확인 | 저자 합성·훈련 앱이므로 실제 서비스 일반화 성과로 쓰지 않음. [실행 결과](README.md#이번에-직접-실행한-인가-증거) |
| 실제 앱의 BOLA 정답 | [wger 영양 공지](https://github.com/wger-project/wger/security/advisories/GHSA-g8gc-6c4h-jg86)·[목록 공지](https://github.com/wger-project/wger/security/advisories/GHSA-xf68-8hjw-7mpm). 공식 이미지 2.4/2.5에서 총 16개 GET 정책 응답: 취약판 영양 교차 노출 2, 혼합 목록 4, 수정판에서 차단/필터링 | [digest·합성 fixture·요청별 응답·검증기](appendices/authz/real-app/WGER-PAIRED-REPRO.ko.md)를 gold로 채택. **2개 CVE family**, Akto 탐지 수치 아님 |
| 정상 공개·공유 | [wger 공개 template maintainer 테스트](https://github.com/wger-project/wger/commit/3515e61d8a246c7dccaf5453da3efd1d0d4937f9)는 비소유자 공개 조회 200을 허용. 공식 **2.7 이미지 원본 테스트 8/8 통과**, 공개 detail 200·동일 ID 확인 | [실행 로그·image digest](appendices/authz/real-app/public-normal/README.ko.md)를 정상군 근거로 채택. 2.4/2.5 CVE와 다른 snapshot. 명시적 공유 등 추가 필요 |
| 한국어 PII | 외부 [ko-pii](https://github.com/Marker-Inc-Korea/ko-pii) 합성 540문서에 저자 규칙을 실행해 부분문자열·set F1 **0.79018**, 같은 예측의 정확 표면형·set F1 **0.66481** 확인 | **문자 위치 exact-span F1이 아님.** [K-PII-Bench](https://huggingface.co/datasets/woohyun212/k-pii-bench)는 126문서/541개체의 형식 통과, 의미 오류 후보와 음성 문서 0개. 외부 자료를 품질 감사 후 쓰고 우리 API 합성 stress set은 따로 만든다. [PII 감사](appendices/pii/PII-REVIEW.ko.md) |

논문이 코드만 공개하고 **정상·BOLA 요청별 정답을 공개하지 않은 경우**, 그 논문의 높은 검출 숫자를 우리 FPR 기준선으로 가져오지 않는다. BACScan의 알려진 읽기 사례는 20개이지만 정상 TN이 없어 FPR을 계산할 수 없고, RESTler 논문의 실제 대상은 익명화되어 있다. [원문별 대상·공개 여부](appendices/authz/AUTHZ-REVIEW.ko.md)

## 태스크 4: 지표와 다음 결정

인가 gold를 `(앱/버전, 요청자, 객체, GET, 허용 정책)`으로 고정하고, **경고 없음·미실행·보류·정상 확인**을 구분한다. 전체 BOLA를 분모로 한 **종단 재현율**, 전체 정상 사례를 분모로 한 **FPR**, 양쪽의 **보류율/판정 커버리지**, 정책 입력·사람 시간으로 비교한다. 한국어 PII는 필드 유형 macro F1과 `(유형, 시작·끝 위치)` exact entity F1 및 빈 문서 오탐률을 별도로 측정한다. 실제 앱 수가 적고 Akto 원본을 아직 실행하지 않았으므로 **95% 같은 성능 목표 숫자는 정하지 않는다.** [평가 계약](README.md#태스크-4-평가-계약과-목표-수치-결정-순서)

팀이 다음에 결정할 것은 **내부 게이트웨이/외부 스캐너의 데이터 수집 경계**, Akto 원본과 Test Role/YAML 설정판에 제공할 동일 정보, 공개/공유 정상군을 추가할 앱 snapshot이다. 그 뒤 baseline을 실행하고 최소 개선 폭·허용 저하·시험군을 사전 동결한다. 현재 완료한 것은 **외부 정답과 설계 확보**이며 Akto·제안 방식의 종단 성능 비교는 `NOT_RUN`이다.
