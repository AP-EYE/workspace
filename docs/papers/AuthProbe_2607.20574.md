> 원본: AuthProbe_2607.20574.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.6-7 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
|     | AuthProbe: |     |     |     | Specification-Driven, |        |             |              |            |      | Multi-Identity |               |     |     |     |     |
| --- | ---------- | --- | --- | --- | --------------------- | ------ | ----------- | ------------ | ---------- | ---- | -------------- | ------------- | --- | --- | --- | --- |
|     | Detection  |     |     |     | of                    | Broken |             | Object-Level |            |      |                | Authorization |     |     |     |     |
|     |            |     |     |     |                       | in     | Recruitment |              |            | APIs |                |               |     |     |     |     |
|     |            |     |     |     |                       |        |             | Jay          | Barach     |      |                |               |     |     |     |     |
|     |            |     |     |     |                       |        |             | Independent  | Researcher |      |                |               |     |     |     |     |
https://github.com/jbarach2012/AuthProbe
Abstract—Broken Object-Level Authorization (BOLA), also spanned on the order of sixty four million records [3]. The
|     | known as | Insecure | Direct | Object | Reference | (IDOR), |     | has topped |          |        |          |                |     |       |            |      |
| --- | -------- | -------- | ------ | ------ | --------- | ------- | --- | ---------- | -------- | ------ | -------- | -------------- | --- | ----- | ---------- | ---- |
|     |          |          |        |        |           |         |     |            | platform | vendor | disputes | the real-world |     | scale | and states | that |
theOWASPAPISecurityrankingsince2019andistherootcause
|     |     |     |     |     |     |     |     |     | only a | handful | of records | were | viewed | by  | the researchers, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | ---- | ------ | --- | ---------------- | --- |
ofsomeofthelargestexposuresofapplicantdatainrecruitment
|     |             |              |     |         |         |            |     |              | yet the | potential | exposure | and the | underlying |     | flaw | are not in |
| --- | ----------- | ------------ | --- | ------- | ------- | ---------- | --- | ------------ | ------- | --------- | -------- | ------- | ---------- | --- | ---- | ---------- |
|     | technology. | The defining |     | feature | of this | flaw class | is  | that a mali- |         |           |          |         |            |     |      |            |
cious request is byte-for-byte indistinguishable from a legitimate dispute. The flaw is a textbook case of Broken Object-Level
one, which is precisely why web application firewalls and single- Authorization: the endpoint authenticated the caller but never
identityscannersfailtocatchit.WepresentAuthProbe,anopen-
|     |     |     |     |     |     |     |     |     | checked | whether | that caller | was | permitted | to  | read the | specific |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | --- | --------- | --- | -------- | -------- |
source,black-boxscannerthatdetectsBOLAandIDORinHTTP
|                                          |         |         |           |      |            |               |     |        | object being | requested. |     |     |     |     |     |     |
| ---------------------------------------- | ------- | ------- | --------- | ---- | ---------- | ------------- | --- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- |
| 6202 luJ 22  ]RC.sc[  1v47502.7062:viXra | APIs by | driving | its tests | from | an OpenAPI | specification |     | and by |              |            |     |     |     |     |     |     |
BOLAhasheldthetoppositionintheOWASPAPISecurity
|     | acting under | two | or more | identities |     | that the | operator | controls. |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------- | ---------- | --- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
AuthProbe discovers, for each identity, the objects that identity TopTensincethelistwasfirstpublishedin2019,anditretains
legitimately owns, then attempts to read one identity’s objects that position in the 2023 revision as API1:2023 [1]. Industry
whileauthenticatedasanotherandconfirmsaleakbycomparing
|     |                 |             |                |              |               |          |             |             | telemetry   | places | it among | the most | frequently |         | exploited     | API     |
| --- | --------------- | ----------- | -------------- | ------------ | ------------- | -------- | ----------- | ----------- | ----------- | ------ | -------- | -------- | ---------- | ------- | ------------- | ------- |
|     | the response    | against     | a              | ground-truth |               | fetch by | the         | true owner. |             |        |          |          |            |         |               |         |
|     |                 |             |                |              |               |          |             |             | weaknesses  | [4],   | [5]. The | reason   | this class | is      | so persistent | is      |
|     | It also walks   | predictable |                | identifiers  | to            | expose   | enumeration | and         |             |        |          |          |            |         |               |         |
|     |                 |             |                |              |               |          |             |             | structural. | A BOLA | request  | uses     | a valid    | session | and           | a well- |
|     | reports missing |             | authentication |              | and existence |          | oracles.    | The tool    |             |        |          |          |            |         |               |         |
returns a severity-thresholded exit code and machine-readable formed path, so it carries no payload signature, no anomalous
reports so that it can gate a continuous integration build. On syntax,andnoinjectionstring.Asignature-basedwebapplica-
|     | a synthetic | recruitment |     | API in | which | the McHire |     | failure class |     |     |     |     |     |     |     |     |
| --- | ----------- | ----------- | --- | ------ | ----- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionfirewallseesanormalrequest,andaconventionaldynamic
|     | is reproduced, | AuthProbe |           | detects | every      | planted      | cross-identity |         |         |               |       |          |          |     |        |           |
| --- | -------------- | --------- | --------- | ------- | ---------- | ------------ | -------------- | ------- | ------- | ------------- | ----- | -------- | -------- | --- | ------ | --------- |
|     |                |           |           |         |            |              |                |         | scanner | that operates | under | a single | identity |     | has no | notion of |
|     | read with      | no false  | positives | on      | a hardened | counterpart, |                | and its |         |               |       |          |          |     |        |           |
whichobjectsbelongtowhichprincipal,soitcannotrecognize
|     | running | time grows | linearly | with | the | number | of objects | under |     |     |     |     |     |     |     |     |
| --- | ------- | ---------- | -------- | ---- | --- | ------ | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
test.AuthProbeisreleasedundertheApache2.0licensewithan thatareturnedobjectwasonethecallershouldnothaveseen.
authorized-use guardrail. Detecting BOLA therefore requires contextual testing that is
|     | Index        | Terms—API  | security, | broken       |          | object | level authorization, |             |          |                |            |                  |           |               |                    |          |
| --- | ------------ | ---------- | --------- | ------------ | -------- | ------ | -------------------- | ----------- | -------- | -------------- | ---------- | ---------------- | --------- | ------------- | ------------------ | -------- |
|     |              |            |           |              |          |        |                      |             | aware of | ownership      | and        | that operates    |           | under         | more               | than one |
|     | IDOR, access | control    |           | testing,     | OpenAPI, | DAST,  |                      | recruitment |          |                |            |                  |           |               |                    |          |
|     |              |            |           |              |          |        |                      |             | identity | at once.       |            |                  |           |               |                    |          |
|     | technology,  | continuous |           | integration. |          |        |                      |             |          |                |            |                  |           |               |                    |          |
|     |              |            |           |              |          |        |                      |             | This     | paper presents | AuthProbe, |                  | a scanner |               | built specifically |          |
|     |              |            |           |              |          |        |                      |             | for that | task. Its      | design     | rests            | on three  | observations. |                    | First,   |
|     |              |            | I.        | INTRODUCTION |          |        |                      |             |          |                |            |                  |           |               |                    |          |
|     |              |            |           |              |          |        |                      |             | modern   | APIs publish   | a          | machine-readable |           | contract      | in                 | the form |
Automated hiring platforms now sit between most job of an OpenAPI document, which enumerates the endpoints
seekers and most employers. An applicant tracking system andidentifieswhichonesreturnindividualobjects.Second,an
concentratesanunusuallyrichstoreofpersonaldata,including authorization flaw is only demonstrable when the tester holds
names, contact details, home addresses, employment history, atleasttwoidentitiesandcanshowthatonereachestheother’s
personality assessment results, and full chat transcripts, while data.Third,ausefulsecuritycheckmustfitintoanautomated
it is optimized for speed, automation, and scale. That com- pipeline, which means it must produce a deterministic verdict
bination has repeatedly come at the expense of security and a machine-readable report rather than a human-oriented
fundamentals, and the fundamental most often neglected is narrative. AuthProbe unites these three observations into a
|     | authorization | at  | the level | of the | individual | object. |     |     | single tool. |     |     |     |     |     |     |     |
| --- | ------------- | --- | --------- | ------ | ---------- | ------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
The clearest recent illustration is the McHire incident of Thescopeofthisworkisdeliberate.Wetargetthereadpath
2025. Two researchers logged into a dormant administrative of the item operation, which is the dominant Broken Object-
test account on a widely used recruitment chatbot platform LevelAuthorizationpatternandtheonebehindthemotivating
using the credentials 123456 for both the user name and incident, and we optimize for a low false-positive rate so
the password, with no second factor required. They then that the tool can run unattended on every build rather than
foundaninternalendpointthatacceptedasequentialapplicant as an occasional, expert-supervised audit. We do not attempt
identifier.Bydecrementingthatnumbertheycouldretrieveany to model every access-control property, and we treat source-
applicant’schattranscriptandcontactdetails,andtheexposure level analysis as a complement rather than a competitor. This

focus is what lets AuthProbe be both simple to deploy and SQL analysis with static analysis to check whether the code
trustworthy enough to gate a release. enforcestheappropriatemodel[7].Theseworksarepowerful,
We make the following contributions. and several achieve high precision, but most require either
|               |     |           |        |     |          |     |           | the application |     | binary, | the source | code, | or  | instrumentation |     |
| ------------- | --- | --------- | ------ | --- | -------- | --- | --------- | --------------- | --- | ------- | ---------- | ----- | --- | --------------- | --- |
| • A black-box |     | detection | method |     | for BOLA | and | IDOR that |                 |     |         |            |       |     |                 |     |
isdrivenbyanOpenAPIspecification,requiresnoaccess of the running server. AuthProbe occupies a different and
to the target’s source code, and confirms a finding by complementary point in the design space. It is fully black
response differencingagainst aground-truth fetch,which box, it needs only the published specification and network
keeps the false-positive rate low (Sections III and V). access under identities the operator holds, and it is built to
|     |     |     |     |     |     |     |     | run unattended |     | inside | a delivery | pipeline. | It does | not | compete |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ---------- | --------- | ------- | --- | ------- |
• Asetofcomplementaryprobesforidentifierenumeration,
missing authentication, and object-existence oracles, to- withastaticanalyzersuchasBolaRaysomuchasitcoversthe
getherwithaseveritymodelandacontinuousintegration deployment-timegapthatstaticanalysiscannotreach,namely
gate (Sections V and VI). a running service whose source may be unavailable.
| An  | open-source | implementation |     |     | that | ships with | an in- |     |     |     |     |     |     |     |     |
| --- | ----------- | -------------- | --- | --- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
•
|             |     |            |             |     |     |     |            | C. Specification-driven |     |     | API testing |     |     |     |     |
| ----------- | --- | ---------- | ----------- | --- | --- | --- | ---------- | ----------------------- | --- | --- | ----------- | --- | --- | --- | --- |
| tentionally |     | vulnerable | recruitment |     | API | and | a hardened |                         |     |     |             |     |     |     |     |
counterpart,sothetoolcanbedemonstratedandvalidated A separate line of work generates tests from an API
endtoendwithouttouchingathird-partysystem(Section contract.RESTlerinfersproducerandconsumerdependencies
|     |     |     |     |     |     |     |     | among | operations | and | performs | stateful | fuzzing |     | of REST |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | -------- | -------- | ------- | --- | ------- |
VI).
Anevaluationonthattestbedshowingcompletedetection services [10]. RESTest applies black-box, constraint-based
•
|        |         |              |     |       |      |          |        | testing | driven by | the | specification | [11], | and | EvoMaster | uses |
| ------ | ------- | ------------ | --- | ----- | ---- | -------- | ------ | ------- | --------- | --- | ------------- | ----- | --- | --------- | ---- |
| of the | planted | McHire-class |     | flaw, | zero | findings | on the |         |           |     |               |       |     |           |      |
hardenedtarget,andrunningtimethatscaleslinearlywith evolutionary search to generate test cases for RESTful APIs
the number of objects (Section VII). [12]. These tools target functional faults and server errors
|           |      |           |       |     |             |     |          | rather than | authorization |     | policy, | and | they | typically | operate |
| --------- | ---- | --------- | ----- | --- | ----------- | --- | -------- | ----------- | ------------- | --- | ------- | --- | ---- | --------- | ------- |
| AuthProbe | is a | defensive | tool. | It  | is intended | for | use only |             |               |     |         |     |      |           |         |
against systems the operator owns or is authorized to test, underasingleidentity.AuthProbeborrowstheideaoftreating
|                 |     |             |      |           |           |     |           | the specification |     | as the | source | of truth | for what | to  | test, then |
| --------------- | --- | ----------- | ---- | --------- | --------- | --- | --------- | ----------------- | --- | ------ | ------ | -------- | -------- | --- | ---------- |
| and it enforces |     | that intent | with | a runtime | guardrail |     | described |                   |     |        |        |          |          |     |            |
in Section IX. redirects it toward a security property that only becomes
|     |     |     |     |     |     |     |     | visible | when the | tester | holds | multiple | identities. |     | General- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | ----- | -------- | ----------- | --- | -------- |
II. BACKGROUNDANDRELATEDWORK purpose dynamic scanners such as the OWASP Zed Attack
A. Broken object-level authorization Proxyarewidelyusedtocrawlandfuzzwebapplications[18],
andtheycanbescriptedtocompareresponsesacrosssessions,
Accesscontrolonaresourceinvolvestwodistinctquestions.
Authentication asks who the caller is, and authorization asks buttheydonotmodelobjectownershipoutoftheboxandare
|           |             |      |         |         |           |        |          | not driven | by an | object-level   | authorization |            | contract, |           | so a team |
| --------- | ----------- | ---- | ------- | ------- | --------- | ------ | -------- | ---------- | ----- | -------------- | ------------- | ---------- | --------- | --------- | --------- |
| whether   | that caller | may  | perform | the     | requested | action | on the   |            |       |                |               |            |           |           |           |
|           |             |      |         |         |           |        |          | must build | the   | multi-identity |               | comparison | itself.   | AuthProbe |           |
| requested | object.     | BOLA | is the  | failure | of the    | second | question |            |       |                |               |            |           |           |           |
at the granularity of an individual object. The OWASP API packagesexactlythatcomparisonasafirst-class,specification-
|          |         |         |       |        |          |      |             | driven check. |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ----- | ------ | -------- | ---- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Security | project | defines | it as | an API | endpoint | that | receives an |               |     |     |     |     |     |     |     |
objectidentifierfromtheclientandactsonitwithoutverifying
|                        |               |        |          |          |            |          |          | D. Authorization |           | systems |                    |     |               |     |      |
| ---------------------- | ------------- | ------ | -------- | -------- | ---------- | -------- | -------- | ---------------- | --------- | ------- | ------------------ | --- | ------------- | --- | ---- |
| that the authenticated |               | caller | is       | entitled | to that    | specific | object   |                  |           |         |                    |     |               |     |      |
|                        |               |        |          |          |            |          |          | On the           | defensive | side,   | relationship-based |     | authorization |     | sys- |
| [1]. The               | corresponding |        | weakness | in       | the Common |          | Weakness |                  |           |         |                    |     |               |     |      |
Enumeration is CWE-639, authorization bypass through a temssuchasGoogleZanzibarprovideaconsistent,centralized
|                 |     |            |      |       |             |     |          | way to   | answer            | object-level | access | questions | at  | scale       | [13], and |
| --------------- | --- | ---------- | ---- | ----- | ----------- | --- | -------- | -------- | ----------------- | ------------ | ------ | --------- | --- | ----------- | --------- |
| user-controlled |     | key, which | sits | under | the broader |     | CWE-284, |          |                   |              |        |           |     |             |           |
|                 |     |            |      |       |             |     |          | its open | reimplementations |              | have   | become    | the | recommended |           |
improperaccesscontrol[2].IDORisthecommonnameforthe
same defect when the user-controlled key is a direct reference way to enforce the checks whose absence AuthProbe detects.
|           |          |         |             |     |     |     |     | Vulnerable     | application |        | benchmarks    | built | around        | the            | OWASP |
| --------- | -------- | ------- | ----------- | --- | --- | --- | --- | -------------- | ----------- | ------ | ------------- | ----- | ------------- | -------------- | ----- |
| such as a | database | row     | identifier. |     |     |     |     |                |             |        |               |       |               |                |       |
|           |          |         |             |     |     |     |     | API risks,     | such        | as the | one described |       | by Idris      | and colleagues |       |
| B. Access | control  | testing |             |     |     |     |     |                |             |        |               |       |               |                |       |
|           |          |         |             |     |     |     |     | [14], motivate | the         | value  | of a shipped, |       | intentionally | vulnerable     |       |
Detectingauthorizationflawshasanestablishedresearchlit- target for validating a detector. AuthProbe complements these
erature. AuthScope drives a mobile application automatically, by providing the offensive test that confirms whether a given
learns the request fields that carry object identifiers through deployment actually enforces the policy that a system like
differentialtrafficanalysis,andsubstitutesoneuser’sidentifier Zanzibar would express.
| into another | user’s | session |     | to reveal | missing | checks | [6]. |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------- | --- | --------- | ------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
MACE analyzes web applications to find privilege escalation E. Why recruitment APIs are a distinctive target
paths that arise from inconsistent access-control enforcement Recruitment platforms combine three properties that make
[8]. FlowWatcher defends against data disclosure by tracking object-level authorization both critical and frequently mishan-
an application’s intended ownership policy and blocking re- dled.Theyconcentrateabroadrangeofpersonaldataforevery
sponsesthatviolateit[9].Morerecently,BolaRaystudiesreal applicant, they are integration dense because an applicant
BOLA vulnerabilities in database-backed applications, distills tracking system typically connects to chatbots, background-
fourrecurringobject-levelauthorizationmodels,andcombines check services, job boards, and analytics through additional

BOLA
OpenAPI Resource Ownership Probe Findings
IDOR/enumeration
document detection discovery engine report
console/JSON/
missingauth/oracle
Markdown/JUnit
Identities +exitcode
(operator-controlled)
Fig. 1. AuthProbe pipeline. The OpenAPI document yields the set of object-returning resources. For each resource the tool discovers which objects each
operator-controlledidentityowns,thenrunsfourprobesandemitsareportplusaseverity-thresholdedexitcodesuitableforacontinuousintegrationgate.
TABLEI III. THREATMODELANDPROBLEMDEFINITION
AUTHPROBECOMPAREDWITHREPRESENTATIVEPRIORAPPROACHES.
We consider an HTTP API that manages objects on behalf
of principals. Let U be the set of principals and let R be a
Approach Black Nosrc Spec Multi CI
box needed driven identity native resourcetype,forexampleanapplicationrecord.Eachobjecto
oftypeRhasanownerown(o)∈U andisaddressedthrough
AuthScope[6] Yes Yes No Yes No
MACE[8] No No No Yes No an identifier. The API exposes a collection operation that lists
BolaRay[7] No No No N/A No the objects visible to the caller and an item operation that
FlowWatcher[9] No No No Yes No
returns a single object given its identifier.
RESTler[10] Yes Yes Yes No Part
RESTest[11] Yes Yes Yes No Part We define ownership as the ground truth that the API itself
EvoMaster[12] Part No Yes No Part asserts through its collection operation. If principal u lists the
AuthProbe Yes Yes Yes Yes Yes
collectionandtheobjectoappears,thenuisentitledtoreado.
This is a conservative and self-consistent definition because it
is derived from the target’s own behavior rather than from an
APIs,andtheyarebuiltundercommercialpressuretoonboard
external policy that the tester would otherwise have to guess.
applicants quickly and at scale. The result is a large, high-
The adversary in our model is a principal a ∈ U who
value object store reached through many endpoints, where a
holds a valid session but attempts to read an object o with
singlemissingownershipcheckcanexposetheentireapplicant
own(o) ̸= a and o not in the set that a is entitled to. A
population. The motivating incident followed exactly this
BrokenObject-LevelAuthorizationvulnerabilityexistsforthe
shape:achatbotfrontendcollectedapplicantdata,aninternal
item operation if there is a principal a and an object o such
API returned individual records by identifier, and the absence
that a is not entitled to o yet the item operation, invoked with
of an object-level check turned a predictable identifier into a
a’s credentials and the identifier of o, returns o.
corpus-wide leak [3]. A detector aimed at this domain must
The detection problem is to decide, for a given API and a
therefore treat the individual applicant record as the unit of
given set of tester-controlled identities, whether such a pair
protection and must reason about who owns each record,
(a,o) exists, and to do so from outside the server with no
which is the design center of AuthProbe.
view of its internals. Two subtleties shape the method. First,
a response with a success status is not sufficient evidence of
F. Positioning a leak, since some APIs return a generic body for a denied
request;thetoolmustconfirmthatthereturnedobjectisinfact
Table I places AuthProbe among representative prior ap-
the victim’s object. Second, the tester can only reason about
proaches.Thefunctionaltestingtoolsgenerateloadandinputs
objectsitcanname,soitmustfirstlearnwhichidentifiersexist
from a specification but do not model ownership, so they sur-
and who owns them, which is the purpose of the ownership
face server errors rather than authorization leaks. The access-
discovery step.
control analyzers model authorization well but generally need
thesource,thebinary,orserverinstrumentation.AuthProbeis IV. SYSTEMARCHITECTURE
thecombinationthatthedeploymentstagerequires:blackbox, Figure1showstheAuthProbepipeline.Theinputisatarget
specification driven, aware of multiple identities, and built to base URL, an OpenAPI document that is either fetched from
gate a pipeline. None of the prior systems occupies all four the running service or supplied as a file, and a configuration
positionsatonce,anditistheunionoftheseproperties,rather that lists two or more identities the operator controls. Each
than any single one, that makes a check both trustworthy and identity is expressed as a set of HTTP headers, which accom-
cheap enough to run continuously. The comparison is not a modatesbearertokens,APIkeys,andsessioncookieswithout
claim of superiority on detection depth, where source-level special cases.
analyzers retain an advantage, but a statement about where in The first stage detects resources. AuthProbe scans
the software lifecycle each approach is usable. the specification for a collection path and a sibling

Algorithm 1 Specification-driven resource detection Algorithm 2 Ownership discovery and BOLA detection
Require: OpenAPI document S Require: resource R, identities I, client H
Ensure: set of resources R Ensure: findings F
1: R←∅ 1: F ←∅; own←{}; view←{}
2: for each path p in S.paths do 2: for each identity u∈I do ▷ ownership discovery
3: ifpmatches(coll)/{param}andphasGETthen 3: own[u]←ids(H.get(R.list,u))
4: c←coll(p) 4: end for
5: if c∈S.paths and c has GET then 5: for each u∈I, each o∈own[u] do ▷ ground truth
6: f ←inferIdField(S,p) 6: view[o]←H.get(R.fetch(o),u)
7: R←R∪{(name(c),c,p,param(p),f)} 7: end for
8: end if 8: for each attacker a∈I do
9: end if 9: for each victim v ∈I with v ̸=a do
10: end for 10: for each o∈own[v] with o∈/ own[a] do
11: return R 11: r ←H.get(R.fetch(o),a)
12: if ok(r)∧obj(r)∧id(r)=o then
13: add BOLA finding (a,v,o) to F
item path that carries a single path parameter, for ex- 14: end if
ample a list at /applications beside a fetch at 15: end for
/applications/{app_id}. Each such pair becomes a 16: end for
resource with a list path, a fetch path, a path parameter name, 17: end for
and an identifier field that the tool infers from the response 18: return F
schema and defaults to id. The operator may override this
detectioninconfigurationwhenacontractdoesnotfollowthe
common convention. every ordered pair of distinct identities it fetches the victim’s
The second stage discovers ownership. For every identity objectswhileauthenticatedastheattackerandappliestheleak
and every resource, AuthProbe calls the collection operation predicate.
and records the identifiers that the operation returns for that The leak predicate is the heart of the false-positive control.
identity. This yields, for each identity, the set of objects the For an attacker a requesting the identifier of a victim object
targetitselfconsidersvisibletoit,whichisexactlytheground o, let the response be r. We declare a leak when the status of
truth the threat model relies upon. r is a success and the body of r is an object whose identifier
The third stage runs the probes. The engine executes four field equals the identifier of o. Formally,
probes per resource, described in Section V, and each probe
(cid:0) (cid:1)
emits zero or more findings. The final stage renders the Leak(a,o)≡ok(r)∧obj(r)∧ id(r)=id(o) , (1)
findings to the console and, on request, to JSON, Markdown,
and a finding is raised when Leak(a,o) holds for an object
and JUnit formats, and it sets the process exit code according
o that belongs to another identity and does not belong to
to a configured severity threshold so that a pipeline step fails
a. Requiring the returned identifier to match the requested
when a finding at or above that threshold is present.
one rules out the common case in which a denied request
The tool is deliberately stateless between runs and requires
returns a generic error body with a success status, and it rules
no agent inside the target. This keeps deployment simple: a
out responses that echo a placeholder rather than the victim’s
continuous integration job starts the service, runs AuthProbe
record.
againstit,andinspectstheexitcode,inthesamewayitwould
The cost of Algorithm 2 is dominated by its final triple
run a unit test suite.
loop, which performs O(|I|2·m) item requests, where m is
V. DETECTIONMETHODOLOGYANDALGORITHMS the number of objects per identity. In practice the number of
A. Resource detection tester identities is small and fixed, so the cost is linear in
the number of objects, a property we confirm empirically in
Algorithm 1 formalizes resource detection. The tool walks
Section VII.
the paths in the specification, matches each path against the
pattern of a collection followed by a single brace-delimited
C. Identifier enumeration
parameter, and pairs it with the corresponding collection path
when both expose a read operation. Algorithm3addressestheenumerationfacetoftheMcHire
flaw. It first flags identifiers as enumerable when every ob-
B. Ownership discovery and BOLA detection
served identifier is numeric, which signals a predictable and
The core of the method is Algorithm 2. For each resource, therefore walkable scheme. It then takes an identifier the
thetoolfirstrecordstheobjectseachidentityownsbyreading attacker owns and probes a bounded neighborhood around
the collection operation. It then fetches every owned object it. Reaching any object the attacker does not own is a
as its true owner to capture a ground-truth view. Finally, for demonstration that the identifiers are both predictable and

Algorithm 3 Identifier enumeration probe Since a tester typically configures a small, fixed number of
| Require: resource | R, identity | u, radius k, client | H   |     |     |     |     |     |     |     |     |
| ----------------- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
identities,therequestcountislinearinm,whichisthesample
Ensure: findings F size the operator chooses rather than the size of the target’s
| F ←∅ |     |     |     | store. |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
1:
2: if all observed identifiers are numeric then Theconfirmationpredicatemakesthetoolconservativeina
3: add enumerable-identifier finding to F useful direction. A finding is raised only when the attacker’s
end if
| 4:  |     |     |     | responsecarriesasuccessstatusandanobjectwhoseidentifier |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
5: b← an identifier owned by u equals the requested one. If that condition holds, the service
for δ ∈{±1,...,±k} do genuinely returned the victim’s object to an unauthorized
6:
7: c←b+δ caller, so a raised finding corresponds to a real leak under the
8: r ←H.get(R.fetch(c),u) ownership definition of Section III. In this sense the method
| if ok(r)∧obj(r)∧c∈/ |     | own[u] then |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9: is sound with respect to that definition, and the empty result
10: record c as reached by enumeration on the hardened target in Section VII is consistent with that
11: end if property. The method is not complete. It can only test objects
12: end for it discovers, so a service that exposes no listing and uses
13: if any c was reached then unguessable identifiers yields little to test, and it can miss
| add | IDOR finding | to F |     |     |     |     |     |     |     |     |     |
| --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14: a leak when the victim’s data is returned in a transformed
15: end if body that does not echo the requested identifier. Both gaps
16: return F are visibility limits rather than logical errors, and both are
|     |     |     |     | addressable | by                | supplying | explicit   | seeds        | or  | a custom | body |
| --- | --- | --- | --- | ----------- | ----------------- | --------- | ---------- | ------------ | --- | -------- | ---- |
|     |     |     |     | matcher     | in configuration. |           | The design | deliberately |     | trades   | some |
unprotected, which is the precise combination that made the completeness for a low false-positive rate, because a scanner
McHire exposure possible. that cries wolf is quickly ignored inside a build pipeline.
D. Missing authentication and existence oracle VI. IMPLEMENTATION
Two further probes round out coverage. The missing- AuthProbe is implemented in Python. The scanner core
authentication probe repeats the collection and item requests depends only on a small HTTP client and a YAML parser,
with no credentials and raises a critical finding when data is which keeps installation light and portable. The tool parses
returned,whichcorrespondstoAPI2:2023intheOWASPlist. theOpenAPIdocument,performsthealgorithmsofSectionV,
Theexistence-oracleprobecomparesthestatusreturnedforan
|     |     |     |     | and renders | reports | in  | four formats. | The | console | format | gives |
| --- | --- | --- | --- | ----------- | ------- | --- | ------------- | --- | ------- | ------ | ----- |
unauthorized but existing object with the status returned for a human summary, the JSON format is intended for program-
a non-existent one. When a denied request yields a forbidden matic consumption, the Markdown format is convenient for
status while a missing object yields a not-found status, the pull-request comments, and the JUnit format lets an existing
difference lets an attacker confirm which identifiers are real, test dashboard display each finding as a failed test case. A
andthetoolreportsalow-severityfinding.Ahardenedservice command-line interface exposes a single scan subcommand
avoids this by returning a uniform not-found status in both that reads a configuration file, selects output formats, writes
| cases.      |                      |             |      | reports  | to a directory, |               | and sets      | the exit     | code.  |          |       |
| ----------- | -------------------- | ----------- | ---- | -------- | --------------- | ------------- | ------------- | ------------ | ------ | -------- | ----- |
|             |                      |             |      | To make  | the             | tool testable | and           | demonstrable |        | without  | any   |
| E. Severity | model and continuous | integration | gate |          |                 |               |               |              |        |          |       |
|             |                      |             |      | external | system,         | the           | project ships | two          | target | services | built |
Eachfindingcarriesaseveritydrawnfromanorderedscale with a standard Python web framework. The vulnerable target
of informational, low, medium, high, and critical. Missing reproducestheMcHirefailureclass:itissuessequentialinteger
authentication is critical, a confirmed cross-identity read and identifiers and its item endpoint authenticates the caller but
a successful enumeration walk are high, a purely enumerable omits the ownership check, so any authenticated user can
identifier scheme is medium, and an existence oracle is low. read any application. The hardened target is the corrected
Thetoolexitswithanon-zerostatuswhenanyfindingreaches counterpart:itissuesnon-sequentialuniversallyuniqueidenti-
a configured threshold, which defaults to high. This turns fiers, enforces a deny-by-default ownership check at the point
AuthProbe into a build gate: a change that reintroduces an of access, and returns a uniform not-found status for both
object-level authorization flaw causes the pipeline step to fail unauthorized and missing objects. Both services expose an
before the change reaches production. identical contract, so a single configuration scans either one,
|                |            |                  |     | which makes | the         | pair    | a clean before-and-after |             |     | demonstration. |            |
| -------------- | ---------- | ---------------- | --- | ----------- | ----------- | ------- | ------------------------ | ----------- | --- | -------------- | ---------- |
| F. Complexity, | soundness, | and completeness |     |             |             |         |                          |             |     |                |            |
|                |            |                  |     | Two         | engineering | choices | support                  | responsible |     | use.           | First, the |
LetI bethesetoftesteridentitiesandletmbethenumber tool prints an authorized-use banner on every run. Second, it
ofobjectsdiscoveredperidentity.Ownershipdiscoveryissues refuses to scan a target whose host is not local unless the
|I|collectionrequests,theground-truthpassissues|I|·mitem operator passes an explicit acknowledgment flag or sets an
requests,andthecross-identitypassissuesatmost|I|·(|I|−1)· allow-remote option in configuration. These measures do not
O(|I|2
m item requests. The total is therefore ·m) requests. prevent misuse by a determined operator, but they make the

|     |     |     | TABLEII |     |     |     |     |     |     |     | TABLEIII |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
AUTHPROBEPROBESANDTHEIRTRIGGERSIGNALS. FINDINGSBYSEVERITYONTHETWOTARGETS,THREEAPPLICATIONS
PERIDENTITY.
| Probe |     | OWASP     | Sev. | Triggersignal                  |     |     |     |     |        |     |          |      |        |     |     |
| ----- | --- | --------- | ---- | ------------------------------ | --- | --- | --- | --- | ------ | --- | -------- | ---- | ------ | --- | --- |
|       |     |           |      |                                |     |     |     |     | Target |     | Critical | High | Medium | Low |     |
| BOLA  |     | API1:2023 | high | victimobjectreturnedtoattacker |     |     |     |     |        |     |          |      |        |     |     |
IDORwalk API1:2023 high non-ownedobjectreachedbysteppingid Vulnerable 0 7 1 0
Enumerableid API1:2023 med allidentifiersarenumeric Hardened 0 0 0 0
| Missingauth     |       | API2:2023  | crit  | datareturnedwithnocredentials     |          |     |               |                 |          |                |              |            |                |               |             |
| --------------- | ----- | ---------- | ----- | --------------------------------- | -------- | --- | ------------- | --------------- | -------- | -------------- | ------------ | ---------- | -------------- | ------------- | ----------- |
| Existenceoracle |       | API1:2023  | low   | forbiddenandmissingdifferinstatus |          |     |               |                 |          |                |              |            |                |               |             |
|                 |       |            |       |                                   |          |     |               | to console,     | JSON,    | Markdown,      |              | and JUnit, | and            | how           | a further   |
|                 |       |            |       |                                   |          |     |               | format          | such     | as SARIF       | could        | be added   | for            | code-scanning |             |
| intended        | scope | explicit   | and   | reduce                            | the risk | of  | an accidental |                 |          |                |              |            |                |               |             |
|                 |       |            |       |                                   |          |     |               | dashboards.     | Identity |                | construction | is         | a small        | adapter       | as well,    |
| scan            | of an | unintended | host. |                                   |          |     |               |                 |          |                |              |            |                |               |             |
|                 |       |            |       |                                   |          |     |               | so establishing |          | a session      | through      | a login    | exchange       |               | rather than |
|                 |       |            |       |                                   |          |     |               | a static        | header   | is a localized |              | change.    | This structure |               | keeps the   |
A. Configuration
toolsmallwhileleavingclearseamsfortheextensionsoutlined
| A          | scan      | is described | by a        | short    | configuration |      | file, shown    |            |     |     |     |     |     |     |     |
| ---------- | --------- | ------------ | ----------- | -------- | ------------- | ---- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|            |           |              |             |          |               |      |                | in Section | X.  |     |     |     |     |     |     |
| in Listing |           | 1. It names  | the target, |          | points at     | the  | specification, |            |     |     |     |     |     |     |     |
| and        | lists the | identities   | the         | operator | controls,     | each | as a set       |            |     |     |     |     |     |     |     |
VII. EVALUATION
| of headers. |          | Optional     | settings      | select   | the severity | threshold, | the            |            |              |       |            |             |           |                 |            |
| ----------- | -------- | ------------ | ------------- | -------- | ------------ | ---------- | -------------- | ---------- | ------------ | ----- | ---------- | ----------- | --------- | --------------- | ---------- |
|             |          |              |               |          |              |            |                | We         | evaluate     | three | questions. | Does        | AuthProbe |                 | detect the |
| enumeration |          | radius,      | and whether   | remote   | targets      | are        | permitted.     |            |              |       |            |             |           |                 |            |
|             |          |              |               |          |              |            |                | planted    | McHire-class |       | flaw?      | Does it     | avoid     | false positives | on         |
| Resources   |          | are detected | automatically |          | from         | the        | specification, |            |              |       |            |             |           |                 |            |
|             |          |              |               |          |              |            |                | a hardened | service?     | How   | does       | its running | time      | scale           | with the   |
| and         | the file | may add      | explicit      | resource | definitions  |            | when a con-    |            |              |       |            |             |           |                 |            |
|             |          |              |               |          |              |            |                | size of    | the target?  |       |            |             |           |                 |            |
tractdoesnotfollowtheusualcollectionanditemconvention.
|     |     |           |                                 |     |     |     |     | A. Experimental |     | setup |     |     |     |     |     |
| --- | --- | --------- | ------------------------------- | --- | --- | --- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- |
|     |     | Listing1. | AminimalAuthProbeconfiguration. |     |     |     |     |                 |     |       |     |     |     |     |     |
target: All experiments run against the two shipped target services
|     | base_url: | "http://127.0.0.1:8000" |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onasinglehost,withtwotesteridentitiesnamedaliceandbob.
|     | spec: | "auto" |     |     |     |     |     |         |           |     |                |             |     |      |          |
| --- | ----- | ------ | --- | --- | --- | --- | --- | ------- | --------- | --- | -------------- | ----------- | --- | ---- | -------- |
|     |       |        |     |     |     |     |     | For the | detection | and | false-positive | experiments |     | each | identity |
identities:
- name: alice creates three applications. For the scaling experiment each
|     | headers: | { Authorization: |     |     | "Bearer | alice-token" |     |          |         |           |     |           |               |     |          |
| --- | -------- | ---------------- | --- | --- | ------- | ------------ | --- | -------- | ------- | --------- | --- | --------- | ------------- | --- | -------- |
|     |          |                  |     |     |         |              |     | identity | creates | a varying |     | number of | applications, |     | from one |
}
|     |         |     |     |     |     |     |     | to fifty. | The targets | store | data | in memory | and | are reset | before |
| --- | ------- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ----- | ---- | --------- | --- | --------- | ------ |
|     | - name: | bob |     |     |     |     |     |           |             |       |      |           |     |           |        |
headers: { Authorization: "Bearer bob-token" } each run so that results are reproducible. Because the targets
settings: are synthetic and contain only fabricated data, the evaluation
|     | fail_on: | high |     |     |     |     |     |          |         |          |              |     |     |     |     |
| --- | -------- | ---- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ------------ | --- | --- | --- | --- |
|     |          |      |     |     |     |     |     | involves | no real | personal | information. |     |     |     |     |
B. Probes and continuous integration B. Detection and false positives
| Table | II  | summarizes | the four | probes, | the | OWASP | category |     |     |     |     |     |     |     |     |
| ----- | --- | ---------- | -------- | ------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
TableIIIsummarizestheoutcome.Onthevulnerabletarget
each maps to, and the signal that triggers a finding. In a with three applications per identity, AuthProbe reports seven
pipeline, AuthProbe is invoked as a single step that starts the high-severity findings and one medium-severity finding. The
| service, | runs | the scan, | and inspects |     | the exit | code, | as shown | in            |     |          |          |     |           |                |     |
| -------- | ---- | --------- | ------------ | --- | -------- | ----- | -------- | ------------- | --- | -------- | -------- | --- | --------- | -------------- | --- |
|          |      |           |              |     |          |       |          | high-severity |     | findings | comprise | the | confirmed | cross-identity |     |
Listing 2. When any finding reaches the configured threshold reads in both directions, that is alice reading each of bob’s
| the | step fails, | so a | regression | that reintroduces |     | an  | object-level |         |     |             |     |                  |     |          |        |
| --- | ----------- | ---- | ---------- | ----------------- | --- | --- | ------------ | ------- | --- | ----------- | --- | ---------------- | --- | -------- | ------ |
|     |             |      |            |                   |     |     |              | objects | and | bob reading |     | each of alice’s, |     | together | with a |
authorizationflawblocksthechangebeforerelease.TheJUnit successfulenumerationwalk,andthemedium-severityfinding
outputcanbeattachedtothebuildsothateachfindingappears is the enumerable-identifier scheme. On the hardened target,
| as a | failed    | test case                              | in the existing |     | dashboard. |     |     |           |               |          |       |             |           |         |          |
| ---- | --------- | -------------------------------------- | --------------- | --- | ---------- | --- | --- | --------- | ------------- | -------- | ----- | ----------- | --------- | ------- | -------- |
|      |           |                                        |                 |     |            |     |     | AuthProbe | reports       | nothing. |       | The tool    | therefore | detects | the      |
|      |           |                                        |                 |     |            |     |     | planted   | vulnerability |          | class | in full and | produces  | no      | findings |
|      | Listing2. | AuthProbeasacontinuousintegrationgate. |                 |     |            |     |     |           |               |          |       |             |           |         |          |
- name: AuthProbe against the corrected service, which is the behavior a build
|     | run: | |     |     |     |     |     |     | gate requires. |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
authprobe scan --config authprobe.yaml \ Figure2showsthesameresultasachart.Theseparationis
|     | --format | junit | --out | out/ | --fail-on |     | high |     |     |     |     |     |     |     |     |
| --- | -------- | ----- | ----- | ---- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
categoricalratherthanmarginal:thevulnerabletargetproduces
high-severityfindings,andthehardenedtargetproducesnone,
C. Extensibility
|     |     |     |     |     |     |     |     | so a threshold |     | at the | high level | cleanly | distinguishes |     | the two. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ---------- | ------- | ------------- | --- | -------- |
Theimplementationseparatesconcernssothatnewcapabil-
C. Scalability
itycanbeaddedwithoutdisturbingthecore.Eachprobeisan
independent function that receives the discovered ownership Figure 3 plots the running time of a full scan against the
map and returns findings, so a new check, for example one number of applications per identity, from one to fifty, on
that tests write verbs, is a self-contained addition. Reporters the vulnerable target. The measured times grow from sixteen
are likewise pluggable, which is how the same result renders milliseconds at a single object per identity to one hundred

8
7
6
4
2
1
0 0 0 0 0 0
0
High Medium Low Critical
sgnidnfi
Vulnerable
Hardened
Fig.2. Findingsbyseverity.Thevulnerabletargetyieldssevenhighandone
mediumfinding,whilethehardenedtargetyieldsnone.
100
50
0
0 10 20 30 40 50
objects per identity
)sm(
emit
nacs
TABLEIV
RAWSCALABILITYMEASUREMENTSONTHEVULNERABLETARGET.
Objectsperidentity Scantime(ms) Findings
1 16 4
2 19 6
5 24 12
10 33 22
20 54 42
50 114 102
quentialintegeridentifiers.Whenaliceandbobeachcreatean
application, alice owns identifier one and bob owns identifier
two.TheBOLAprobefetchesbob’sobjectwhileauthenticated
as alice, receives a success status and a body whose identifier
equals two, and raises the finding shown in Listing 3. The
enumeration probe independently starts from alice’s identifier
one, steps to two, reaches bob’s object, and raises an IDOR
finding, which mirrors the decrementing walk used in the real
incident.Theenumerableidentifierschemeitselfisreportedat
mediumseveritybecausenumericidentifiersarewalkableeven
whereacheckiscurrentlypresent.Thehardenedtargetdefeats
all three findings at once by enforcing ownership, returning a
uniform not-found status, and issuing unguessable identifiers.
Fig.3. Scantimeagainstthenumberofobjectsperidentityonthevulnerable Listing3. AconfirmedBOLAfindinginJSONform.
target.Thetrendisclosetolinear,consistentwiththecostanalysiswhenthe {
numberoftesteridentitiesissmallandfixed. "probe": "bola",
"severity": "high",
"resource": "applications",
"endpoint": "/applications/{app_id}",
fourteenmillisecondsatfifty,andthegrowthisclosetolinear,
"evidence": {"attacker": "alice", "victim": "bob
as predicted by the cost analysis of Algorithm 2 with a fixed, ",
small number of identities. Over the same range the number "object_id": 2, "status": 200}
}
of findings grows from four to one hundred two, because the
tool reports one confirmed read per victim object per attacker
F. Comparison with conventional defenses
inadditiontothefixedenumerationandenumerable-identifier
findings. The tool therefore remains fast on realistically sized It is worth stating plainly why the defenses most teams
collections when seeded with a bounded sample per identity, already run do not catch this class. A signature-based web
and the linear trend means the cost is governed by the sample application firewall inspects a request for known malicious
size the operator chooses rather than by the total size of the patterns, yet the attacker’s request here is a well-formed fetch
target’s data store. with a valid session and an ordinary identifier, so there is
no signature to match. A conventional dynamic scanner that
D. Interpretation
operates under a single identity can exercise the endpoint and
Theevaluationsupportsthecentralclaim.AuthProbedetects confirm that it returns data, but with only one identity it has
a BOLA and IDOR pattern that a signature-based firewall no way to know that the returned object belongs to someone
and a single-identity scanner would miss, it does so with a else, so it cannot label the response as a leak. AuthProbe
confirmation predicate that produced no false positives on the succeedspreciselybecauseitholdsthesecondidentityandthe
hardened target, and it runs quickly enough to sit inside a ownership map, which lets it recognize a cross-identity read
routine build. The result is modest in scope by design, since for what it is. The requirement for two identities is therefore
the targets are synthetic and the purpose of this evaluation is not an inconvenience but the very feature that makes the flaw
to establish correctness of the mechanism rather than a field observable.
study of prevalence. A larger study against real, authorized
G. Why the hardened target yields no findings
targets is future work and is discussed below.
It is instructive to trace each probe against the hardened
E. Case study: reproducing the McHire failure chain
target, because the empty result is not an accident of con-
The vulnerable target reproduces the two defects that com- figuration but a direct consequence of three corrections. The
bined in the motivating incident. Its item endpoint authenti- BOLA probe fetches a victim object as the attacker, but the
catesthecallerbutomitstheownershipcheck,anditissuesse- service compares the object’s owner against the caller and

returns a not-found status, so the leak predicate is never wrapped or transformed body. The predicate is configurable
satisfied. The enumeration probe cannot even begin its walk to accommodate such shapes, but a default deployment may
in a meaningful way, because the identifiers are universally under-report in those cases, which is a conservative failure
| unique values | rather | than | integers, | so  | there | is no | neighbor | to mode. |     |     |     |     |     |     |     |
| ------------- | ------ | ---- | --------- | --- | ----- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
steptoandthenumericcheckthatflagsenumerableidentifiers Taken together these limitations position AuthProbe as a
does not fire. The missing-authentication probe receives an complement to, rather than a replacement for, source-level
unauthorized status for every credential-free request, and the analysis and manual review. Its value is that it turns the
existence-oracle probe observes the same not-found status for most common and most damaging API flaw into a repeatable,
an unauthorized object and for a missing one, so no oracle is evidence-producing check that a team can run on every build
reported. Each probe is defeated by the specific control it is without specialist tooling. Used together with a source-level
designed to exercise, which is the behavior a faithful detector analyzer during development and a manual review before a
|                |     |       |       |            |     |              |        | major release, |     | it closes | the | deployment-time |     | gap | in which |
| -------------- | --- | ----- | ----- | ---------- | --- | ------------ | ------ | -------------- | --- | --------- | --- | --------------- | --- | --- | -------- |
| should exhibit | and | which | gives | confidence |     | that a green | result |                |     |           |     |                 |     |     |          |
is meaningful rather than a blind spot. a flaw can slip into a running service unnoticed. The three
layersreinforceoneanother:staticanalysisreasonsaboutcode
| H. Request | volume |     |     |     |     |     |     |          |       |              |     |        |        |       |          |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | -------- | ----- | ------------ | --- | ------ | ------ | ----- | -------- |
|            |        |     |     |     |     |     |     | that may | never | ship, manual |     | review | brings | human | judgment |
The scan cost is easiest to reason about in terms of to complex cases, and AuthProbe checks the artifact that is
request volume rather than wall-clock time, since the latter actually deployed.
| depends        | on the             | environment. |       | For the      | reported | setup          | with two |            |             |       |            |          |          |             |         |
| -------------- | ------------------ | ------------ | ----- | ------------ | -------- | -------------- | -------- | ---------- | ----------- | ----- | ---------- | -------- | -------- | ----------- | ------- |
|                |                    |              |       |              |          |                |          | A. Threats | to validity |       |            |          |          |             |         |
| identities     | and                | m objects    | each, | ownership    |          | discovery      | issues   |            |             |       |            |          |          |             |         |
|                |                    |              |       |              |          |                |          | Several    | factors     | bound | the        | strength | of the   | evaluation. | The     |
| two collection | requests,          |              | the   | ground-truth | pass     | issues         | 2m item  |            |             |       |            |          |          |             |         |
|                |                    |              |       |              |          |                |          | construct  | we measure  |       | is whether | a        | returned | object      | belongs |
| requests,      | the cross-identity |              | pass  | issues       | 2m       | item requests, | and      |            |             |       |            |          |          |             |         |
the enumeration probe issues a bounded number proportional to a principal that did not own it, which we operationalize
throughtheownershipdefinitionofSectionIII;atargetwhose
toitsradius.Thedominanttermistherefore4mitemrequests,
collectionoperationdoesnotfaithfullyreflectownershipcould
| which matches |     | the near-linear |     | timing | curve | of Figure | 3 and |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ------ | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
distortthatconstruct,althoughsuchadiscrepancywoulditself
confirmsthatanoperatorcontrolsthecostdirectlythroughthe
|             |            |     |               |     |        |        |           | be a finding | worth | surfacing. |     | Internally, | the | targets | are in- |
| ----------- | ---------- | --- | ------------- | --- | ------ | ------ | --------- | ------------ | ----- | ---------- | --- | ----------- | --- | ------- | ------- |
| sample size | configured |     | per identity. | A   | larger | sample | increases |              |       |            |     |             |     |         |         |
confidencethataflawwouldbecaughtwhilekeepingthescan memory services on a single host, so the absolute timings
|          |             |         |     |     |     |     |     | exclude  | network    | latency | and would | be      | larger | against  | a remote |
| -------- | ----------- | ------- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | --------- | ------- | ------ | -------- | -------- |
| within a | predictable | budget. |     |     |     |     |     |          |            |         |           |         |        |          |          |
|          |             |         |     |     |     |     |     | service; | the linear | trend,  | however,  | follows |        | from the | request- |
VIII. DISCUSSIONANDLIMITATIONS count analysis and does not depend on the absolute constants.
|           |     |       |        |         |     |             |        | Externally, | the | two targets | are | synthetic | and | were authored | to  |
| --------- | --- | ----- | ------ | ------- | --- | ----------- | ------ | ----------- | --- | ----------- | --- | --------- | --- | ------------- | --- |
| AuthProbe | is  | black | box by | design, | and | that choice | brings |             |     |             |     |           |     |               |     |
both its strengths and its limits. Because it needs only the exhibit and to fix the studied flaw, so the results establish that
|               |     |         |         |            |     |             |       | the mechanism |           | works rather | than | how      | common | the        | flaw is in |
| ------------- | --- | ------- | ------- | ---------- | --- | ----------- | ----- | ------------- | --------- | ------------ | ---- | -------- | ------ | ---------- | ---------- |
| specification | and | network | access, | it applies |     | to services | whose |               |           |              |      |          |        |            |            |
|               |     |         |         |            |     |             |       | the field.    | Measuring | prevalence   |      | requires | an     | authorized | study      |
sourcecodeisunavailableanditfitsnaturallyintodeployment
pipelines, which is where static analyzers such as BolaRay across real deployments, which we identify as future work.
|        |            |      |     |               |     |        |             | We mitigate | author | bias | in the | target | design | by keeping | the |
| ------ | ---------- | ---- | --- | ------------- | --- | ------ | ----------- | ----------- | ------ | ---- | ------ | ------ | ------ | ---------- | --- |
| cannot | reach. The | cost | of  | the black-box |     | stance | is that the |             |        |      |        |        |        |            |     |
hardenedtargetafaithfulminimalcorrectionofthevulnerable
| tool can | only reason |     | about | objects | it can | name. | It therefore |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ----- | ------- | ------ | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
one,changingonlytheidentifierscheme,theownershipcheck,
| depends         | on the      | collection       | operation | to        | discover | ownership, | or          |               |                   |        |            |         |              |        |          |
| --------------- | ----------- | ---------------- | --------- | --------- | -------- | ---------- | ----------- | ------------- | ----------------- | ------ | ---------- | ------- | ------------ | ------ | -------- |
|                 |             |                  |           |           |          |            |             | and the       | error uniformity. |        |            |         |              |        |          |
| on explicit     | seeds       | in configuration |           | when      | no       | suitable   | collection  |               |                   |        |            |         |              |        |          |
| operation       | exists.     | An               | API that  | exposes   | no       | listing    | and uses    |               |                   |        |            |         |              |        |          |
|                 |             |                  |           |           |          |            |             | B. Deployment |                   | models |            |         |              |        |          |
| unguessable     | identifiers |                  | will      | yield few | objects  | to         | test, which |               |                   |        |            |         |              |        |          |
|                 |             |                  |           |           |          |            |             | AuthProbe     | fits              | three  | deployment |         | models.      | In the | pipeline |
| is a limitation | of          | visibility       | rather    | than      | a false  | negative   | in the      |               |                   |        |            |         |              |        |          |
|                 |             |                  |           |           |          |            |             | model it      | runs on           | every  | build      | against | an ephemeral |        | instance |
usual sense. of the service, which catches regressions early and keeps
| The present     |            | version        | focuses | on        | read access | through | the         |             |           |               |            |           |          |                  |            |
| --------------- | ---------- | -------------- | ------- | --------- | ----------- | ------- | ----------- | ----------- | --------- | ------------- | ---------- | --------- | -------- | ---------------- | ---------- |
|                 |            |                |         |           |             |         |             | the check   | close     | to the        | code       | change    | that     | caused           | it. In the |
| item operation, |            | which          | is the  | dominant  | BOLA        |         | pattern and |             |           |               |            |           |          |                  |            |
|                 |            |                |         |           |             |         |             | staging     | model it  | runs on       | a schedule |           | against  | a pre-production |            |
| the one         | behind     | the motivating |         | incident. | Write       | verbs   | such as     |             |           |               |            |           |          |                  |            |
|                 |            |                |         |           |             |         |             | environment | seeded    | with          | synthetic  | accounts, |          | which            | exercises  |
| update          | and delete | can            | carry   | the same  | flaw,       | and     | extending   |             |           |               |            |           |          |                  |            |
|                 |            |                |         |           |             |         |             | a more      | realistic | configuration |            | including | gateways | and              | reverse    |
the probes to those verbs is a natural next step that reuses proxies. In the assessment model an authorized tester runs it
| the same            | ownership |               | model. | AuthProbe      | also | targets        | object- |              |              |     |                    |     |     |        |            |
| ------------------- | --------- | ------------- | ------ | -------------- | ---- | -------------- | ------- | ------------ | ------------ | --- | ------------------ | --- | --- | ------ | ---------- |
|                     |           |               |        |                |      |                |         | once against | a production |     | or production-like |     |     | system | as part of |
| level authorization |           | specifically. |        | Function-level |      | authorization, |         |              |              |     |                    |     |     |        |            |
abroaderreview,usingtheexplicitacknowledgmentflag.The
| the fifth  | item on | the       | OWASP   | list, concerns |           | whether | a caller |                    |                               |         |          |             |       |         |            |
| ---------- | ------- | --------- | ------- | -------------- | --------- | ------- | -------- | ------------------ | ----------------------------- | ------- | -------- | ----------- | ----- | ------- | ---------- |
|            |         |           |         |                |           |         |          | same configuration |                               | and     | the same | probes      | serve | all     | three, and |
| may invoke | an      | operation | at      | all, and       | detecting | it      | requires | a                  |                               |         |          |             |       |         |            |
|            |         |           |         |                |           |         |          | only the           | cadence                       | and the | target   | environment |       | change. |            |
| notion of  | roles   | that the  | current | tool           | does not  | model.  | Finally, |                    |                               |         |          |             |       |         |            |
|            |         |           |         |                |           |         |          | IX.                | ETHICALANDLEGALCONSIDERATIONS |         |          |             |       |         |            |
theconfirmationpredicatekeepsfalsepositiveslow,butitcan
missaleakwhenaservicereturnsthevictim’sdatainashape A tool that reads one user’s data as another user is only
that does not carry the requested identifier, for example a ethical when the operator is authorized to test the target.

AuthProbe is built for that setting. The bundled vulnerable exchange, extracting a token from a sign-in response,
serviceexistssolelysothatthetoolcanbevalidatedagainsta which removes the need to pre-provision static headers
system the operator controls, and it is clearly marked as unfit and better mirrors real client behavior.
fordeployment.TheruntimeguardraildescribedinSectionVI • Standardized reporting. Emitting results in the Static
refuses non-local targets without an explicit acknowledgment, Analysis Results Interchange Format would let findings
which reduces the chance of an accidental scan and records appear directly in code-scanning dashboards alongside
the operator’s assertion of authorization. Operators remain other security results, improving triage.
responsible for compliance with applicable law, including • An authorized field study. Measuring the prevalence of
computer-misusestatutes,andforcoordinateddisclosurewhen the flaw across real, authorized recruitment APIs, and
a finding concerns a third party. Because recruitment data comparing the black-box detection rate against source-
is personal data, testing against real systems also engages level tools, would move the work from a correctness
data-protection obligations such as those in the General Data demonstration to an empirical characterization of the
Protection Regulation [17], and operators should prefer syn- problem in the wild.
thetic or consented data when validating a deployment. The
Beyond the specific tool, the broader aim is to make object-
project itself ships only fabricated data and encourages the
level authorization a property that teams verify by default
same practice downstream. When AuthProbe is used against
rather than discover after a breach. The history of software
a system operated by another party under authorization, any
security suggests that a class of flaw recedes only when
confirmed finding should be handled through coordinated dis-
checking for it becomes routine, cheap, and automatic, as
closure.Inpracticethismeansreportingthespecificendpoint,
happened with memory safety scanners and dependency au-
the ownership violation, and the minimal evidence needed to
diting. Broken Object-Level Authorization is overdue for the
reproduce it, allowing the operator a reasonable window to
same treatment, and a small, specification-driven, pipeline-
remediate before any public description, and never retaining
nativecheckisasteptowardthatroutine.Theimplementation,
orredistributingthepersonaldatathataleakexposes.Thetool
the demonstration targets, and the experimental scripts are
supportsthisworkflowbyrecording,foreachfinding,onlythe
available under the Apache 2.0 license at the address on the
identifiersandstatuscodesrequiredtoreproduceitratherthan
title page.
the full contents of a victim record, which keeps the evidence
actionable while minimizing the sensitive data it captures. REFERENCES
X. CONCLUSIONANDFUTUREWORK
[1] OWASP Foundation, “OWASP API Security Top 10 2023: API1:2023
Broken Object-Level Authorization remains the most com- Broken Object Level Authorization,” 2023. [Online]. Available: https:
//owasp.org/API-Security/
monandmostdamagingflawintheAPIsthathandleapplicant
[2] MITRE, “CWE-639: Authorization Bypass Through User-Controlled
data, and it is invisible to the defenses that most teams Key,”CommonWeaknessEnumeration.[Online].Available:https://cwe.
already run. AuthProbe addresses that gap with a black- mitre.org/data/definitions/639.html
[3] I.CarrollandS.Curry,“WouldyoulikeanIDORwiththat?Leaking64
box, specification-driven scanner that detects the flaw by
millionMcDonald’sjobapplications,”2025.[Online].Available:https:
acting under multiple identities and confirming a leak through //ian.sh/mcdonalds
responsedifferencing,andthatfitsadeliverypipelinethrough [4] SaltSecurity,“StateofAPISecurityReport,”SaltLabs,2024.
[5] Imperva,“TheStateofAPISecurityin2024,”ImpervaThreatResearch,
aseverity-thresholdedexitcodeandmachine-readablereports.
2024.
On a testbed that reproduces the McHire failure class the tool [6] C.Zuo,Q.Zhao,andZ.Lin,“AuthScope:Towardsautomaticdiscovery
detectseveryplantedcross-identityread,producesnofindings ofvulnerableauthorizationsinonlineservices,”inProc.ACMSIGSAC
Conf. Computer and Communications Security (CCS), 2017, pp. 799-
on the hardened counterpart, and scales linearly with the size
813.
of the sample under test. [7] Y. Huang, C. Shi, J. Lu, H. Li, H. Meng, and L. Li, “Detecting
Future work proceeds along several lines that reuse the brokenobject-levelauthorizationvulnerabilitiesindatabase-backedap-
plications,”inProc.ACMSIGSACConf.ComputerandCommunications
present design.
Security(CCS),2024,pp.2934-2948.
• Write-verb and nested-resource coverage. Extending [8] M. Monshizadeh, P. Naldurg, and V. N. Venkatakrishnan, “MACE:
the probes to update and delete operations, and to nested Detecting privilege escalation vulnerabilities in web applications,” in
Proc. ACM SIGSAC Conf. Computer and Communications Security
resources such as an application under a requisition,
(CCS),2014,pp.690-701.
broadens coverage while reusing the same ownership [9] D.Muthukumaran,D.O’Keeffe,C.Priebe,D.Eyers,B.Shand,andP.
model, since the leak predicate and the discovery step Pietzuch, “FlowWatcher: Defending against data disclosure vulnerabil-
itiesinwebapplications,”inProc.ACMSIGSACConf.Computerand
carry over unchanged.
CommunicationsSecurity(CCS),2015.
• Function-level authorization. Adding a notion of roles [10] V. Atlidakis, P. Godefroid, and M. Polikarpova, “RESTler: Stateful
enables detection of broken function-level authorization, RESTAPIfuzzing,”inProc.IEEE/ACMInt.Conf.SoftwareEngineering
(ICSE),2019.
the fifth item on the OWASP list, which asks whether a
[11] A. Martin-Lopez, S. Segura, and A. Ruiz-Cortes, “RESTest: Black-
caller may invoke an operation at all rather than whether boxconstraint-basedtestingofRESTfulwebAPIs,”inProc.Int.Conf.
it may touch a specific object. Service-OrientedComputing(ICSOC),2020,pp.459-475.
[12] A.Arcuri,“RESTfulAPIautomatedtestcasegenerationwithEvoMas-
• Richer identity establishment. A login-flow adapter ter,” ACM Trans. Software Engineering and Methodology, vol. 28, no.
would let an identity be established through a credential 1,2019.

[13] R.Pang,R.Caceres,M.Burrows,etal.,“Zanzibar:Google’sconsistent,
globalauthorizationsystem,”inProc.USENIXAnnualTechnicalConf.
(ATC),2019.
| [14] M. Idris, | I.    | Syarif, and | I. Winarno, | “Development | of vulnerable    | web       |
| -------------- | ----- | ----------- | ----------- | ------------ | ---------------- | --------- |
| application    | based | on          | OWASP       | API security | risks,” in Proc. | IEEE Int. |
ElectronicsSymp.(IES),2021,pp.190-194.
[15] OpenAPIInitiative,“OpenAPISpecificationversion3.1.0,”2021.[On-
line].Available:https://spec.openapis.org/oas/v3.1.0
| [16] V. C. | Hu et | al., “Guide | to Attribute | Based | Access Control | (ABAC) |
| ---------- | ----- | ----------- | ------------ | ----- | -------------- | ------ |
definitionandconsiderations,”NISTSpecialPublication800-162,2014.
[17] EuropeanParliamentandCouncil,“Regulation(EU)2016/679(General
DataProtectionRegulation),”2016.
[18] OWASPFoundation,“OWASPZedAttackProxy(ZAP),”open-source
webapplicationscanner.[Online].Available:https://www.zaproxy.org/
| [19] R. T. | Fielding,       | “Architectural |       | styles and    | the design of     | network-based |
| ---------- | --------------- | -------------- | ----- | ------------- | ----------------- | ------------- |
| software   | architectures,” |                | Ph.D. | dissertation, | Univ. California, | Irvine,       |
2000.
