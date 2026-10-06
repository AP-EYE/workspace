"""Build review appendices from the frozen local evidence; makes no network calls."""
import csv, datetime, html, json, pathlib, re, subprocess

R=pathlib.Path(__file__).resolve().parents[1]
G=R/'evidence/github'
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def clean(s):
    s=str(s or '').replace('\n',' ').replace('\r',' ')
    # Public issue titles include spam and telephone numbers. The raw API capture
    # is retained separately; browsing and CSV do not need those numeric strings.
    return re.sub(r'(?<!\w)(?:\+?\d[\d ()\-]{7,}\d)', '[numeric string omitted]', s)
def cell(s): return html.escape(clean(s)).replace('|','\\|')

notes={
527:('분류','key 조건에 value 규칙을 잘못 넣던 매핑 수정. key/value 의미를 구분해야 한다.'),
883:('검사 오탐','cookie MaxAge 대소문자·날짜 처리, URL 정규식 escaping·wordlist 처리 등의 patch. 모든 BOLA 오탐이 해결됐다는 뜻은 아니다.'),
1121:('분류','AWS secret custom type을 비활성화하고 일반 타입으로 재분류하는 처리. 변경 이유나 전후 정확도는 이 patch만으로 확정하지 않는다.'),
1231:('마스킹','cookie와 GraphQL의 redaction 처리 확대. 적용되는 입력 경로·설정 조건은 별도 확인해야 한다.'),
1248:('마스킹','mini-runtime query parameter redaction 보완. redactAll 조건이 있으므로 무조건 적용으로 해석하지 않는다.'),
1249:('마스킹','api-runtime query parameter redaction 보완. mini-runtime의 동명 변경과 대상 모듈을 구분한다.'),
1359:('BOLA','인증 헤더 변경 경로에서 upsert를 사용하도록 수정. 없는 헤더의 추가도 다룬다.'),
1363:('BOLA','private_variable_context의 설명 작성용 StringBuilder 초기화로 null 오류 방지. 의미 판정의 정확도 개선과는 구별한다.'),
1491:('마스킹','민감 key 샘플의 redaction 및 타입 mapper의 redacted 설정 전달 보완. mini-runtime-release 대상.'),
1492:('마스킹','cyborg 타입 mapper에 redacted 상태 반영. master 병합으로 표기하지 않는다.'),
1619:('의존성','Struts 및 Spring 관련 의존성 버전 변경. CVE 영향은 사용 경로·배포 버전을 따로 분석해야 한다.'),
1965:('의존성','오래된 Jetty·SnakeYAML 직접 의존성 제거. shaded/transitive dependency까지 모두 제거됐다는 증거는 아니다.'),
2418:('정규식','test-editor helper의 전체 일치 matches를 부분 일치 find로 변경. 현재 PII RegexPredicate의 matches와 다른 코드다.'),
2674:('플랫폼 보안 제보','로그인 JSP에 사용자 이름을 JavaScript 문자열로 직접 삽입하는 XSS 제보의 수정안. open·미병합이며 현재 코드 형태와 일치. 전체 입력/실행 경로 재현은 NOT_RUN.'),
2908:('마스킹 예외','BURP 수집 소스를 global redaction 처리에서 제외하는 변경. 예외의 존재와 실제 계정별 redaction 결과를 구분한다.'),
3055:('마스킹 예외','global redaction을 MIRRORING 소스에 적용하는 조건 변경. 제품의 모든 입력 경로가 같은 정책을 쓰지 않는다.'),
3497:('마스킹','sample data redaction 및 기존 데이터/타입 갱신 경로의 보완. 과거 저장된 모든 원문이 제거됐다는 운영 검증은 하지 않았다.'),
5498:('검사 근거','검출 근거가 원문에 있는지 검증하고 호출자 credential을 누출 근거에서 제외하며 결정적 검출 결과와 LLM 결과를 결합. 문자열 존재가 권한 위반 증거를 대신하지는 않는다.'),
5519:('마스킹 UI','cookie/샘플 표시에서 마스킹 placeholder 처리를 개선. UI가 가려졌다는 사실만으로 DB 원문 제거를 주장할 수 없다.'),
5682:('성능 제안','Hyperscan을 다루는 미병합 제안. 현재 기본 Akto의 엔진이나 속도로 소개하지 않는다. 제목·구성 수준 확인.'),
5863:('문장 PII','기본 Presidio 결과에서 DATE_TIME·NRP·LOCATION 제외. entities를 지정한 경우와 다르며 오탐 감소와 탐지 범위 감소가 함께 있다.'),
5881:('인증정보 취급','session identifier 후보에서 Authorization header를 제거. 실제 외부 유출 사건을 입증한 자료는 아니다.'),
5902:('문장 PII','anonymizer score threshold 0.4와 목록 marker·이메일 등의 회귀 테스트 추가. threshold는 정확도 백분율이 아니다. 테스트 코드는 확인했으나 서비스 테스트 실행은 NOT_RUN.'),
5915:('의존성','Go 의존성 버전 보완. 프로젝트 전체 CVE 제거 또는 악용 가능성의 확정을 뜻하지 않는다.'),
6112:('OSS 사용성 제보','local_deploy의 plan gate 때문에 Access Restricted가 나타나는 문제를 다루는 미병합 수정안. 현재 UI 분기 확인, 실제 Docker 배포 NOT_RUN.'),
6121:('LLM 마스킹','redaction 설정 UI·DTO·Go 모듈 연결 추가. 내부 모델의 한국어 성능은 이 변경으로 확인할 수 없다.'),
6150:('외부 검사 모듈','PII block 우선순위라는 제목이나 본체의 핵심 patch는 모듈 버전 변경. 실제 내부 알고리즘의 수정 내용을 확보한 것으로 간주하지 않는다.'),
6240:('외부 검사 모듈','이메일 PII 탐지 수정이라는 제목이나 본체에서 확인되는 것은 주로 모듈 버전 변경. 전후 precision/recall 수치는 없다.'),
6278:('분류 확장','cyborg의 외부 datatype corrector 관련 HTTP·후보·캐시 등의 확장. 조사한 master에 동일 구현이 있다는 주장은 하지 않는다.'),
6279:('분류 확장','mini-runtime-release의 외부 datatype corrector 연계. branch-specific 구현이며 배포 이미지 채택 여부는 별도 확인.'),
6309:('플랫폼 접근통제','RBAC 요금제 검사 전에 product-level NO_ACCESS를 처리하도록 이동. 기존 early return이 접근 제한을 건너뛸 수 있다는 문제. master 현재 순서도 확인.'),
6402:('데이터 최소화','사용자명 lookup map을 브라우저 payload로 보내던 구조를 서버 조회로 이동. 모든 PII 전송·저장 경로 제거를 의미하지 않는다.'),
6487:('LLM 출력','탐지 이유에 PII/비밀값을 다시 인용하지 않도록 prompt 보완. 별도의 출력 검증 없이 완전한 누출 방지를 증명할 수 없다.'),
6513:('LLM 출력','추가 설명 경로도 값 대신 종류·개수로 설명하도록 보완. feat/async-reason 병합이며 관련 문구는 조사한 master에서도 확인.'),
6569:('플랫폼 보안 제보','역할 변경·비밀번호 초기화 대상의 account 범위와 호출자 권한 확인을 보완하는 미병합 수정안. 다른 interceptor를 포함한 실제 공격 가능성은 NOT_RUN.'),
}
t_notes={
80:'응답 일치 threshold를 90에서 80으로 낮추는 수정안. closed지만 merged_at이 없으므로 적용됐다고 기록하지 않는다.',
81:'28개 BOLA 템플릿에 오류 문구 제외를 추가. HTTP 200 업무 오류의 오탐을 줄이려는 변경이며 영어 문자열 목록에 의존한다.',
85:'잠긴/차단된 계정과 반복 실패 문구, 비어 있지 않은 응답 조건을 보완. 여전히 언어·문구 변형과 정상 본문의 단어 충돌 평가가 필요하다.',
86:'BOLAJSONBodyParamArray의 length 아래 gt: 0 누락으로 생긴 parsing 문제 보완. 탐지 의미보다 템플릿 유효성 문제다.',
167:'12개 BOLA 파일에 HTML tag 제외를 추가. 로그인/오류 HTML 응답의 오탐을 줄이는 휴리스틱; HTML 응답 전체의 의미 판정은 아니다.',
208:'응답 정규식으로 카드·SSN·인도 번호 후보를 찾는 PIIDataLeak threat 템플릿 추가. 권한/소유권을 직접 판단하는 규칙은 아니다.',
214:'앞서 추가한 PIIDataLeak.yml 삭제. 이유는 빈 본문에서 확인되지 않으므로 오탐 때문에 삭제됐다고 단정하지 않는다.',
216:'제목은 PII threat 제거지만 실제 diff는 SecurityMisconfig의 host 조건 제거와 stack trace regex 조정. #214의 삭제와 구별한다.',
227:'closed·미병합. API가 887개 파일 변경을 반환한 큰 제안이며 제목만으로 범위를 알 수 없다. 파일 목록·상태만 확인, 전체 patch 감사는 하지 않았다.',
228:'pro 브랜치에 병합. 28개 BOLA 템플릿의 duration FAST→SLOW 메타데이터 변경. 탐지 정확도 향상 PR로 소개하면 부정확하다.',
297:'agentic BOLA 테스트 추가안, open·미병합. 367개 파일 변경의 목록/대표 patch만 확인. 현재 기본 템플릿으로 평가하지 않는다.',
}

head='''# Akto 수정 이력 검토표

기준: 2026-10-06 KST. 공개 GitHub API 수집본을 사용한다. 이 문서는 보안 감사의 완료 증명서가 아니다.

## 읽는 방법

- **핵심 patch 검토**: 본문·관련 변경 부분을 읽고 의미를 요약한 항목이다. 모든 호출 경로를 동적으로 검증한 것은 아니다.
- **상세 확보**: 본문·파일 목록·GitHub가 제공한 patch를 확보했으나 개별 수정 의미를 충분히 검증하지 않은 항목이다.
- **목록 분류**: 제목·본문 키워드에 따른 자동 분류다. 보안 취약점 판정이 아니다.
- merged는 특정 base branch에 병합됐다는 의미다. master·상용 배포·실제 사용 이미지 적용과 구별한다.
- 원시 이슈에는 외부 사용자의 주장·스팸이 섞인다. 사실의 근거는 코드·재현·관리자 설명과 함께 판단한다.

본체 목록은 이슈 179 + PR 6,402 = 6,581건이다. 본체 PR 상세 164건, tests-library 관련 PR 상세 24건을 확보했다. 번호는 저장소마다 독립적이다. 공개 advisory API 0건은 취약점 부재를 의미하지 않는다.

## 1. 본체 핵심 변경

| PR·종류 | 상태·병합일(UTC)·대상 | 실제 변경과 남는 한계 |
|---|---|---|
'''
for n,(category,note) in notes.items():
    p=read(G/'details'/f'pr-{n}.json')
    status=('병합 '+p['merged_at'][:10]) if p.get('merged_at') else ('open·미병합' if p['state']=='open' else 'closed·미병합')
    head+=f"| [#{n}]({p['html_url']}) · {category} | {status} · `{p['base']['ref']}` | {note} |\n"
head+='''
## 2. 이슈의 해결 상태를 보수적으로 읽기

| 이슈 | 확인한 근거 | 조사 결론 |
|---|---|---|
| [#2673](https://github.com/akto-api-security/akto/issues/2673) | 사용자 이름의 로그인 JSP 삽입 및 #2674 수정안 | 소스와 일치하는 open 제보. 실제 공격 재현은 미실행 |
| [#5512](https://github.com/akto-api-security/akto/issues/5512) / [#4235](https://github.com/akto-api-security/akto/issues/4235) | OSS 로컬 설치의 접근 제한 관련 글 | 로컬 사용 가능 범위를 직접 검증해야 함. 댓글의 우회를 공식 정책으로 간주하지 않음 |
| [#6043](https://github.com/akto-api-security/akto/issues/6043) | shaded dependency와 SBOM 사각지대 제보 | 패키지 탐지와 악용 가능성을 구분. 제보도 exploitability는 조사하지 않았다고 명시 |
| [#5473](https://github.com/akto-api-security/akto/issues/5473) | Mongo 버전/driver 호환성 관련 closed 글 | 현재 Compose는 7.0.4. 과거 제보의 환경과 현재 코드를 섞지 않음 |
| [#5480](https://github.com/akto-api-security/akto/issues/5480) | OpenAPI 3.1에서 endpoint 0건이라는 제보와 해결 댓글 | closed·해결 주장 존재. 원인 patch 연결과 여러 3.1 schema에 대한 검증은 미확인 |

## 3. 검사 템플릿 저장소의 변경

| tests-library PR | 상태·병합일(UTC)·대상 | 검토 결과 |
|---|---|---|
'''
for n,note in t_notes.items():
    p=read(G/'template-details'/f'pr-{n}.json')
    status=('병합 '+p['merged_at'][:10]) if p.get('merged_at') else ('open·미병합' if p['state']=='open' else 'closed·미병합')
    head+=f"| [#{n}]({p['html_url']}) | {status} · `{p['base']['ref']}` | {note} |\n"
head+='''
검사 템플릿에 달린 CVE는 보통 검사 대상 취약점의 참고 자료다. 그 번호를 Akto 자체의 CVE 목록으로 옮기면 안 된다. 일부 템플릿은 INTRUSIVE로 표시돼 있으므로 실습 서버와 명시적인 검사 범위가 필요하다.

## 4. 이번에 확인한 원인 패턴

1. 데이터 취급의 누락: body뿐 아니라 query, cookie, GraphQL, 로그·설명문·export까지 관리해야 한다.
2. 분류의 단순화: key와 value, 전체 일치와 부분 일치, locale, checksum, 관측 부족을 별개로 다뤄야 한다.
3. 휴리스틱의 한계: 같은 2xx 응답·유사한 payload·영어 오류 제외는 객체 소유권의 정답이 아니다.
4. 제품 접근통제: 결제/라이선스 분기와 보안 권한 분기를 섞으면 의도한 제한을 건너뛸 수 있다.
5. 의존성 가시성: 직접 의존성만 갱신해서 shaded·transitive dependency까지 모두 해결했다고 할 수 없다.
6. 운영과 소스의 차이: feature/release branch의 fix, master, Docker image, 외부 검사 모듈은 서로 다른 증거다.

AP-EYE 회귀 사례로는 여러 수집 소스의 PII 잔존 여부, 한국어 200 오류, 다른 소유자의 배열 객체, 인증 헤더의 유무, NO_ACCESS와 요금제 조합을 우선한다. 이 목록은 구현·배포 성공을 주장하는 것이 아니라 조사에서 도출한 시험 제안이다.

## 5. 확보한 본체 PR 상세 전체 목록

아래 표는 상세 확보 범위를 공개하기 위한 것이다. 164건 전체를 완전한 보안 감사로 표시하지 않는다. GitHub patch 필드가 없거나 잘릴 수 있고 PR 본문의 전후 성능 주장도 독립 재현하지 않았다.

| PR | 제목 | 상태 / base | 검토 수준 |
|---|---|---|---|
'''
core={}
for f in sorted((G/'details').glob('pr-*.json'),key=lambda p:int(p.stem.split('-')[1])):
    p=read(f);core[p['number']]=p;n=p['number']
    level='핵심 patch 검토' if n in notes and n!=5682 else ('제안 구성 확인' if n==5682 else '상세 확보')
    state='merged' if p.get('merged_at') else p['state']+' / unmerged'
    head+=f"| [#{n}]({p['html_url']}) | {cell(p['title'])} | {state} / `{p['base']['ref']}` | {level} |\n"
head+='\n## 6. 확보한 tests-library PR 상세 전체 목록\n\n| PR | 제목 | 상태 / base | 검토 수준 |\n|---|---|---|---|\n'
tmpl={}
for f in sorted((G/'template-details').glob('pr-*.json'),key=lambda p:int(p.stem.split('-')[1])):
    p=read(f);tmpl[p['number']]=p;n=p['number'];state='merged' if p.get('merged_at') else p['state']+' / unmerged'
    level='관련 patch 검토' if n in t_notes and n not in [227,297] else ('목록/대표 변경 확인' if n in [227,297] else '상세 확보')
    head+=f"| [#{n}]({p['html_url']}) | {cell(p['title'])} | {state} / `{p['base']['ref']}` | {level} |\n"
(R/'HISTORY-REVIEW.ko.md').write_text(head,encoding='utf-8')

closed={p['number']:p for p in read(G/'closed_pulls.json')}
indexed={x['number']:x for x in read(G/'indexed_items.json')}
rows=[]
for repo,filename,details in [('akto','all_issues_and_prs.json',core),('tests-library','templates_issues.json',tmpl)]:
    for x in read(G/filename):
        n=x['number'];isp='pull_request' in x;p=details.get(n,closed.get(n,{}) if repo=='akto' else {})
        merged=p.get('merged_at') or (x.get('pull_request') or {}).get('merged_at')
        status='merged' if merged else x['state']
        if repo=='akto':tags=indexed[n]['tags'];review='핵심 patch 검토' if n in notes and n!=5682 else ('상세 확보' if n in core else '목록 분류')
        else:
            tags=','.join(k for k,pat in [('pii',r'pii|sensitive'),('bola',r'bola|bfla'),('bug',r'fix|false.positive')] if re.search(pat,x['title']+' '+(x.get('body') or ''),re.I))
            review='관련 patch 검토' if n in t_notes and n not in [227,297] else ('상세 확보' if n in tmpl else '목록 분류')
        rows.append({'repo':repo,'number':n,'kind':'PR' if isp else 'ISSUE','title':clean(x['title']),'status':status,'base':(p.get('base') or {}).get('ref',''),'created':x['created_at'][:10],'merged':merged or '', 'tags':tags,'review':review,'url':x['html_url']})
rows.sort(key=lambda x:(x['repo'], -x['number']))
def csvsafe(v):
    s=str(v)
    return "'"+s if s.startswith(('=','+','-','@','\t','\r')) else s
with (R/'ISSUE-PR-INDEX.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows({k:csvsafe(v) for k,v in row.items()} for row in rows)
(G/'public_index.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'core_detailed':len(core),'templates_detailed':len(tmpl),'public_index_rows':len(rows),'core_interpreted':len(notes),'template_interpreted':len(t_notes)},ensure_ascii=False))
