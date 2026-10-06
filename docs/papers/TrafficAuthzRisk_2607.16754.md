> 원본: TrafficAuthzRisk_2607.16754.pdf; 변환: markitdown; 2026-10-06

<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->

| A             | Non-Intrusive |          |        |      | Traﬀic     |     | Analysis      | Framework   |             | for |
| ------------- | ------------- | -------- | ------ | ---- | ---------- | --- | ------------- | ----------- | ----------- | --- |
| Authorization |               |          |        | Risk | Detection  |     |               | and         | Coordinated |     |
|               |               | Response |        |      | in         | Web | Applications* |             |             |     |
|               | Siqi          | Lin1,2,† | Yuchao |      | Luo3 Zihan |     | Zhu4          | Yiran Wang1 | Borui Qiu3  |     |
1Ara Institute of Canterbury International Engineering College, Shenyang Jianzhu University,
|     |     |         |         |     | Shenyang   | 110168, | China |                |       |     |
| --- | --- | ------- | ------- | --- | ---------- | ------- | ----- | -------------- | ----- | --- |
|     |     | 2Xiamen | Moefire |     | Technology | Co.,    | Ltd., | Xiamen 361000, | China |     |
3School
of Computer Science and Engineering, Shenyang Jianzhu University, Shenyang 110168, China
4School
|     |     | of  | Management,    |     | Shenyang | Jianzhu | University,  | Shenyang        | 110168, China |     |
| --- | --- | --- | -------------- | --- | -------- | ------- | ------------ | --------------- | ------------- | --- |
|     |     |     | †Corresponding |     | author:  | Siqi    | Lin, E-mail: | lsq@moefire.net |               |     |
Abstract: Objective: Authorization violations under valid Web sessions are diﬀicult to identify and
handle in real time from traﬀic because they depend strongly on business semantics and exhibit few
distinctive protocol-level features. This paper proposes a non-intrusive traﬀic analysis framework for
6202 luJ 81  ]ES.sc[  1v45761.7062:viXra
| authorization | risk | detection | and | coordinated |     | response. |     |     |     |     |
| ------------- | ---- | --------- | --- | ----------- | --- | --------- | --- | --- | --- | --- |
Methods: Request–response transactions are correlated to extract runtime context, including the ac-
cesssubject,businessendpoint,objectidentifier,authenticationstate,andbehavioralsequence. Object-
access evidence, identity consistency, behavioral anomalies, authentication context, network environ-
ment, and endpoint-operation risk are mapped to interpretable risk components. Weighted fusion and
high-riskpriorityconstraintsproducegradeddecisionsthatdriveallow,alert,block,andexternalpolicy
actions. The risk components are instantiated using deterministic and interpretable rules so that the
study can evaluate multi-source evidence organization, risk fusion, and the coordinated-response loop
| at the | framework | level. |     |     |     |     |     |     |     |     |
| ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Results: Thecontrolledlocaltestbedcontained2,000balancedlabeledsamples,including1,000normal
accessesand1,000authorization-riskevents. Theframeworkclassified998ofthe1,000authorization-risk
events as risky and produced no false positives among normal accesses. Accuracy, precision, recall, and
F1 score were 99.90%, 100.00%, 99.80%, and 99.90%, respectively. Removing runtime object evidence
reducedtheF1scoreto81.31%,whileremovingthehigh-riskpriorityconstraintreduceditto73.90%. In
aprototypefeasibilitytestwith100concurrentrequestsand1,000totalrequests,themeanrisk-decision
| computation | latency |     | was 0.077ms | and | the P99 | latency | was | 0.137ms. |     |     |
| ----------- | ------- | --- | ----------- | --- | ------- | ------- | --- | -------- | --- | --- |
Conclusions: Thecontrolledevaluationshowsthattheframeworkcanorganizeheterogeneousruntime
evidenceandestablishanexecutableauthorization-riskdecisionandcoordinated-responseloopwithout
modifying application code. The results demonstrate the feasibility of the overall mechanism in the
specified validation scenarios, but do not establish general applicability in production environments.
Keywords: Web application security; authorization risk; non-intrusive traﬀic analysis; run-
| time evidence; |         | coordinated |     | response |     |     |     |     |     |     |
| -------------- | ------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| CLC            | number: | TP393.08    |     |          |     |     |     |     |     |     |
*ThisworkisoneoftheoutcomesoftheLiaoningProvincialCollegeStudentInnovationandEntrepreneurship
Training Program project “Web Application Authorization Risk Identification and Response System Based on
| Non-Intrusive | Traﬀic | Analysis” |     | (Project | No. S202610153008). |     |     |     |     |     |
| ------------- | ------ | --------- | --- | -------- | ------------------- | --- | --- | --- | --- | --- |
1

1 Introduction
1.1 Background
Web applications and API systems have become the principal service form for govern-
mentandenterpriseinformationsystems, businessplatforms, andmobileapplicationbackends.
Business-object identifiers such as user IDs, contract IDs, order IDs, file IDs, and device IDs
are commonly transmitted between clients and servers as URL path segments, query param-
eters, form fields, or JSON request-body fields. Explicit object identifiers improve interface
composability but also enlarge the attack surface for object-level authorization failures. The
OWASP API Security Top 10 ranks Broken Object Level Authorization among the foremost
API security risks and notes that attackers may access resources they do not own by modifying
object identifiers in requests[1].
Compared with unauthenticated access, SQL injection, and cross-site scripting, authoriza-
tionviolationsdependmoreheavilyonbusinesssemantics. Maliciousrequestsoftencarryvalid
sessions, legitimate tokens, and correctly formatted parameters. Network-layer features, status
codes, and URL blocklists alone therefore cannot determine whether the current subject is
authorized to perform the requested operation. As Web systems evolve toward microservices,
gateways, and separated front- and backends, access subjects, business objects, role claims,
and authentication events become distributed across multiple interfaces and services, further
complicating runtime authorization-risk detection.
Existing systems generally rely on code-level authorization checks, RBAC or ABAC poli-
cies, API gateway rules, and WAF signatures. These mechanisms remain the primary means of
access control, but rapid interface evolution, third-party component integration, legacy-system
modernization, and cross-system invocation may lead to delayed rules, invisible object seman-
tics, or fragmented policy enforcement points. A complementary capability is therefore needed
to extract runtime access evidence from request–response traﬀic and support independent risk
detection, auditing, and coordinated response without replacing application authorization.
1.2 Problem Analysis
The central question in authorization-risk detection is not whether a user is logged in, but
whether the current subject is authorized to access the target object or perform the requested
operation. When an attacker modifies an object identifier while legitimately authenticated, or
when an ordinary user invokes a privileged operation, the HTTP method, parameter format,
and response status may resemble normal business traﬀic. Authorization violations in produc-
tionmayalsobeinfrequent, slow, triggeredbyasinglerequest, ordistributedacrossendpoints,
making them diﬀicult to cover reliably with a single threshold rule.
A complementary traﬀic-side protection framework must address four general problems.
First, it must correlate requests and responses to recover interpretable business transactions.
Second, it must provide a unified representation of heterogeneous context, including subjects,
endpoints, objects, authentication state, and historical behavior. Third, without direct access
to the application’s permission database, it must convert multi-source evidence into actionable
risk decisions. Fourth, its decisions must form a response loop with gateways, WAFs, and
security operations platforms.
This study focuses on the unified organization of multi-source traﬀic-side evidence, risk
2

fusion, and coordinated response, examining how different evidence sources work together
within the same transaction and decision chain.
1.3 Contributions
This paper presents a non-intrusive traﬀic analysis framework for authorization risk de-
tection and coordinated response in Web applications. Its main contributions are as follows:
(1) A request–response transaction-driven runtime context extraction process is proposed
to obtain access-subject, endpoint, object, authentication-state, and behavioral-sequence
information consistently at a proxy or gateway.
(2) A framework-level runtime evidence abstraction maps object-access evidence, identity
consistency, behavioral anomalies, authentication context, network environment, and
endpoint-operation risk into unified risk components rather than relying on a single URL
rule or access-frequency threshold.
(3) An interpretable decision mechanism combines weighted fusion with high-risk priority
constraintsandmapstheresulttoallow, alert, block, andexternalpolicyactions, thereby
forming a decision–response loop.
(4) Overall comparison, framework-level ablation, and prototype feasibility tests are con-
ducted in a controlled testbed to evaluate risk-decision capability, the contribution of key
evidence, and basic runtime overhead.
2 Related Work
2.1 Object-Level Authorization Violations in Web Applications
Object-levelauthorizationviolationsarecommonlyassociatedwithInsecureDirectObject
Reference (IDOR) and Broken Object Level Authorization (BOLA). The OWASP Web Secu-
rityTestingGuidedefinesIDORasthedirectuseofuser-controlledinputtoreferencedatabase
records, files, or other resources, allowing an attacker to bypass authorization checks by modi-
fying parameters[2]. Broken access control has also remained one of the most important Web
application security risks in the OWASP Top 10[3].
Object-level authorization violations are not simple authentication failures. A user may
have authenticated successfully and hold a valid token while the backend fails to verify the
authorization relationship between the user and the target object. Such risks can affect read
operations as well as higher-impact modification, deletion, approval, and export operations.
Compared with conventional vulnerabilities, object-level authorization failures depend more
strongly on business data structures and access context and are therefore harder to detect
automatically.
2.2 Rule-Based Protection and Automated Scanning
Rule-based Web protection typically filters traﬀic using URL allowlists or blocklists, pa-
rameter constraints, sensitive-path matching, and signature detection. WAFs and API gate-
ways can quickly block known attack patterns, but their policies require manual maintenance
and cannot automatically understand whether user A is entitled to access object B. Frequent
interface changes and inconsistent object-field names can therefore result in missing rules and
false positives.
3

Automated black-box scanners can identify some input-validation, injection, and config-
uration vulnerabilities. Bau et al.[4] and Doupé et al.[5] systematically evaluated black-box
Web vulnerability scanners and reported limitations in state maintenance, post-authentication
path coverage, and business-logic vulnerability detection. RESTler infers producer–consumer
dependencies from API specifications and generates stateful request sequences[6], improving
state coverage for complex REST APIs. Its primary objective, however, is defect discovery
during testing rather than online authorization decisions over production traﬀic. Object-level
authorization testing generally requires comparisons across users, objects, and roles; generic
scanners and request-sequence generation alone are insuﬀicient to reconstruct complete autho-
rization semantics.
2.3 Access-Control Models and Runtime Monitoring
Role-Based Access Control (RBAC) associates permissions with roles and reduces
permission-management complexity[7]. Attribute-Based Access Control (ABAC) further
incorporates subject, object, operation, and environmental attributes into authorization
decisions[8]. These models provide a theoretical basis for internal permission design, but
an external runtime traﬀic monitor generally cannot read complete permission configu-
rations, database relationships, or application logic. Sun et al.[9] used static analysis to
infer role-specific access-control assumptions, whereas AUTHSCOPE discovered vulnerable
authorizations in online services through differential traﬀic analysis and field substitution[10].
The former requires source code, and the latter targets active testing; both demonstrate the
importance of cross-role or cross-subject comparison for identifying authorization defects.
Runtime monitoring methods use application state, request sequences, and historical be-
havior to identify anomalies. Cova et al.[11] proposed anomaly detection based on internal ap-
plication state, while Felmetsger et al.[12] studied runtime Web detection from the perspective
of logic vulnerabilities. These studies show that business-logic security problems require state
and contextual reasoning. In contrast to static analysis, active scanning, and in-application
instrumentation, the present framework accepts passive or proxy-side request–response trans-
actions as input, organizes several forms of runtime authorization-risk evidence on the traﬀic
side,andmapsriskdecisionsdirectlytogradedresponseactions. Thefocusistheoverallframe-
work and coordination mechanism, while the individual evidence components are instantiated
only to support the unified decision chain.
3 Overall Framework
3.1 Architecture
The framework consists of traﬀic ingress, transaction correlation, context extraction, run-
timeevidenceorganization, riskfusion, coordinatedresponse, statemanagement, andauditing,
as shown in Fig. 1. It can be deployed at a reverse proxy, API gateway, or passive observation
point. In online mode, the system evaluates the current request against its context and pre-
viously established runtime evidence before forwarding the request, and updates transaction
state after the response returns; passive mode primarily generates audit and alert outputs. In
this paper, “non-intrusive” means that the protected application’s business code and internal
authorization logic do not need to be modified; reverse-proxy and gateway deployments may
4

| still operate | on the inline | forwarding | path.                      |     |               |     |
| ------------- | ------------- | ---------- | -------------------------- | --- | ------------- | --- |
|               |               |            | Non-IntrusiveTraﬀicIngress |     | Protected Web |     |
|               | Client/Caller |            | ReverseProxy/API           |     | Application   |     |
|               |               |            | Gateway/PassiveTap         |     | or API System |     |
Request–Response
|     |         |     | Transaction Correlation |            |     |     |
| --- | ------- | --- | ----------------------- | ---------- | --- | --- |
|     | Subject | and |                         |            |     |     |
|     |         |     | Endpoint and            |            |     |     |
|     |         |     |                         | Behavioral | and |     |
Authentication
Object Context
|     |     |     |     | Network | Context |     |
| --- | --- | --- | --- | ------- | ------- | --- |
Context
Runtime
Authorization-Risk
Evidence
SharedStateStore
|     |     |     | Risk Fusion and |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
TransactionsandContext
|     |     |     | Priority Constraints |     | EvidenceandPolicies |     |
| --- | --- | --- | -------------------- | --- | ------------------- | --- |
AuditLogs
|     |     |     | Coordinated Response |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- |
|     |     |     | and Audit Output     |     |     |     |
Figure 1 Overall framework for authorization risk detection and coordinated response
| 3.2 Main | Notation | and Data | Objects |     |     |     |
| -------- | -------- | -------- | ------- | --- | --- | --- |
AnHTTPrequestistheunitofonlineriskdecision-making. Aftertheresponsereturns,the
system forms the correlated transaction T for runtime-evidence updates and auditing. Table 1
lists the main data objects used by the framework. UserKey, EndpointKey, and ObjectId iden-
tify the access subject, normalized endpoint, and business-resource instance, respectively. The
set E (t) contains the runtime object-access evidence established for subject u and resource
u,r
| type r before | time t. |                                                      |                       |              |                   |     |
| ------------- | ------- | ---------------------------------------------------- | --------------------- | ------------ | ----------------- | --- |
|               |         | Table                                                | 1 Main notation       | and meanings |                   |     |
| Symbol        |         | Meaning                                              |                       |              |                   |     |
| T             |         | AcorrelatedHTTPrequest–responsetransactionanditstem- |                       |              |                   |     |
|               |         | poral,                                               | network, and business | context,     | used for evidence | up- |
|               |         | dates                                                | and auditing          |              |                   |     |
UserKey Access-subject identifier derived from an account, session, or
|     |     | low-confidence | temporary | identity |     |     |
| --- | --- | -------------- | --------- | -------- | --- | --- |
EndpointKey Endpoint identifier formed by the HTTP method and nor-
|     |     | malized | path |     |     |     |
| --- | --- | ------- | ---- | --- | --- | --- |
ObjectId Candidate identifier of a business-resource instance
E (t) Basic runtime object-access evidence established for subject
u,r
|     |     | u and | resource type r | before time t |     |     |
| --- | --- | ----- | --------------- | ------------- | --- | --- |
5

3.3 Data Processing and Deployment Modes
The system first receives an HTTP/HTTPS request sent by a client to a Web application.
It extracts context such as UserKey, EndpointKey, ObjectId, and authentication state from
requestheaders, cookies, JWTs, queryparameters, formparameters, andJSONrequestbodies,
and combines this context with existing object evidence and recent access sequences to form
the risk components. Before forwarding the request, the risk-fusion component outputs an
overall risk level, according to which the response component allows, alerts, blocks, or sends
instructions to an external policy enforcement point. The decision for the current request
uses only the context available at request arrival and runtime evidence established by earlier
transactions. For an allowed request, after the response returns, the system correlates the
request and response as transaction T, adds the response summary and business outcome, and
updates evidence for subsequent requests and the audit state; the current response is not used
retrospectively to classify the same request.
In reverse-proxy and API-gateway deployments, the system can obtain complete trans-
actions from plaintext HTTP after TLS termination and support online blocking. In passive
mode, it observes mirrored traﬀic, gateway logs, or audit logs and produces alerts. When
application-layer plaintext is unavailable, only metadata-level analysis is possible, and com-
plete extraction of object identifiers and business outcomes cannot be guaranteed.
3.4 Prototype Implementation and Study Scope
This study focuses on the overall framework and the coordination among its components.
To make the framework-level mechanism executable and reproducible, the prototype instanti-
ates each risk component with deterministic and interpretable rules. Object-access evidence is
maintained as a binary set confirmed jointly by a valid subject, a successful business outcome,
preconfigured transaction semantics, and the current risk decision. Identity and authentication
risk is calculated from consistency among account, session, token, role, and recent authenti-
cation context. Behavioral risk is determined from object switching, request frequency, and
sequencecharacteristicswithinatimewindow. Endpoint-operationriskisconfiguredaccording
to the HTTP method, path semantics, and predefined business impact level.
The evaluation examines whether these components can operate within a unified data flow
and decision chain, whether the principal evidence and fusion mechanisms affect the decision
outcome, and whether the prototype can perform online decisions in the controlled testbed.
Theconclusionsarethereforelimitedtoframework-levelmechanismvalidationunderthestated
experimental conditions.
4 Key Mechanisms
4.1 Request–Response Correlation and Context Extraction
Request–response correlation restores protocol messages as interpretable business trans-
actions. Transaction T includes the request method, normalized path, headers, parameter and
request-body summaries, response status, response-body summary, business-success indicator,
client address, and timestamp. HTTP semantics and URI structure follow RFC 9110[13], and
JWT claim fields follow RFC 7519[14].
Proxy and gateway deployments can correlate messages deterministically using connection
6

context, request sequence numbers, TraceId values, or gateway-injected identifiers. Passive
deployments can approximate correlation using the five-tuple, request features, and a time
window. For persistent connections, asynchronous interfaces, and batch requests, the sys-
tem records correlation confidence and avoids using incomplete transactions to update high-
| confidence |     | evidence. |     |     |     |     |     |     |     |
| ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
UserKey preferentially uses an account identifier, followed by a session or token identifier.
If these values are unavailable, a low-confidence temporary identifier can be derived from the
source address, User-Agent, and device characteristics. EndpointKey combines the HTTP
method with a normalized path in which numeric strings, UUIDs, and random identifiers are
replaced by placeholders. ObjectId is extracted from paths, query parameters, forms, or JSON
fields; field semantics, value patterns, and response structure are used to exclude obvious page
| numbers, |         | timestamps, |                    | and | monetary | values.  |     |     |     |
| -------- | ------- | ----------- | ------------------ | --- | -------- | -------- | --- | --- | --- |
| 4.2      | Runtime |             | Authorization-Risk |     |          | Evidence |     |     |     |
The framework maps heterogeneous context to six basic risk components:
(1) Object-access evidence risk x , indicating whether the current ObjectId has confirmed
obj
|     | runtime |     | access | evidence. |     |     |     |     |     |
| --- | ------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
(2) Identity-consistency risk x , indicating obvious conflicts among account, session, token,
id
|     | and | role | claims. |     |     |     |     |     |     |
| --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
(3) Behavioral-anomaly risk x beh , indicating rapid object switching, sequential identifier ac-
|     | cess, | or  | anomalous | request | sequences. |     |     |     |     |
| --- | ----- | --- | --------- | ------- | ---------- | --- | --- | --- | --- |
(4) Authentication-context risk x , indicating whether a sensitive operation is supported
auth
|     | by  | a recent | valid | authentication |     | or privilege-change |     | event. |     |
| --- | --- | -------- | ----- | -------------- | --- | ------------------- | --- | ------ | --- |
(5) Network-environment risk x , representing auxiliary evidence such as address drift,
net
|     | anomalous |     | proxies, | or  | shared | egress. |     |     |     |
| --- | --------- | --- | -------- | --- | ------ | ------- | --- | --- | --- |
(6) Endpoint-operation risk s , representing the potential business impact of the current
ep
|     | HTTP |     | method | and | endpoint | operation. |     |     |     |
| --- | ---- | --- | ------ | --- | -------- | ---------- | --- | --- | --- |
The basic object-access evidence is defined in Eq. (1). In the prototype, a transaction
is treated as trusted only when the subject is valid, the response confirms business success,
the transaction matches preconfigured confirmation semantics, and the request has not been
assigned a medium- or high-risk decision. Such a transaction may update evidence for later
requests but cannot alter the decision already made for itself. This definition provides an
| executable |     | evidence |     | interface | for | framework-level | validation. |     |     |
| ---------- | --- | -------- | --- | --------- | --- | --------------- | ----------- | --- | --- |
|            |     | E        |     | {o |      |     |                 |             |     | t}  |
u,r (t) = o is confirmed for subject u by a trusted transaction before (1)
If the current object is already present in E (t), its object-evidence risk is low. If the
u,r
object is absent and is accompanied by anomalous object switching, a sensitive operation, or
an identity-context conflict, the risk increases. To avoid penalizing users on shared or mobile
| networks, |     | network-environment |     |     | risk | alone never | triggers | denial. |     |
| --------- | --- | ------------------- | --- | --- | ---- | ----------- | -------- | ------- | --- |
7

| 4.3 Risk | Fusion |     | and High-Risk |     |     | Priority |     | Constraints |     |
| -------- | ------ | --- | ------------- | --- | --- | -------- | --- | ----------- | --- |
All risk components are normalized to [0,1]. The base risk is a fixed-weight sum with
∑
| ≥   |     | 6   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w i 0and w i = 1. Topreventseverallow-riskcomponentsfrommaskingasmallamount
i=1
of high-severity evidence, the framework applies interpretable high-risk priority constraints.
| The total | risk | is calculated |     | as  |     |     |     |     |     |
| --------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|           |      |               |     |     | {   |     | [   | ]}  |     |
∑6
|     |     |     | R base | = min | 1,max |     | 0,  | w i x i , |     |
| --- | --- | --- | ------ | ----- | ----- | --- | --- | --------- | --- |
(2)
i=1
|     |     |     | R     | = max(R |     | ,max({h |     | | j ∈ H}∪{0})), |     |
| --- | --- | --- | ----- | ------- | --- | ------- | --- | --------------- | --- |
|     |     |     | total |         |     | base    |     | j               |     |
H
where x = (x obj ,x id ,x beh ,x auth ,x net ,s ep ); is the set of triggered high-risk conditions,
∈
andh [0,1]isthecorrespondinglowerriskbound. Including0intheinnermaximumdefines
j
the result when no high-risk condition is triggered. A high-risk condition is triggered only by
an interpretable combination of evidence, such as “missing object evidence and a sensitive
operation” or “conflicting identity claims without a valid authentication event,” rather than by
| a single network |          | feature. |     |         |         |         |      |          |     |
| ---------------- | -------- | -------- | --- | ------- | ------- | ------- | ---- | -------- | --- |
| The              | decision | process  | is  | shown   | in Fig. | 2.      |      |          |     |
|                  |          |          |     | Extract |         | Runtime | Risk | Evidence |     |
Endpoint-
|     |     | Object-Access |     | Identityand |     |     |     | Behaviorand |     |
| --- | --- | ------------- | --- | ----------- | --- | --- | --- | ----------- | --- |
Operation
|     |     | Evidence |     | AuthContext |     |     | NetworkContext |     |     |
| --- | --- | -------- | --- | ----------- | --- | --- | -------------- | --- | --- |
Risk
|     |     |     |     |           | Weighted   |          | Fusion  | and         |     |
| --- | --- | --- | --- | --------- | ---------- | -------- | ------- | ----------- | --- |
|     |     |     |     | High-Risk |            | Priority |         | Constraints |     |
|     |     |     |     |           | Risk-Level |          | Mapping |             |     |
High Risk
|     |     | Low | Risk |     |     | Medium | Risk |     |     |
| --- | --- | --- | ---- | --- | --- | ------ | ---- | --- | --- |
Block or
|     |     | Allow |     |     |     | Alert | or Observe |     |     |
| --- | --- | ----- | --- | --- | --- | ----- | ---------- | --- | --- |
Coordinate
|                 |     | Figure | 2        | Runtime | risk-evidence |     | fusion | and response | process |
| --------------- | --- | ------ | -------- | ------- | ------------- | --- | ------ | ------------ | ------- |
| 4.4 Coordinated |     |        | Response |         |               |     |        |              |         |
The response component divides requests into low-, medium-, and high-risk classes ac-
cording to R and policy thresholds. Low-risk requests are allowed and recorded in the
total
audit log. Medium-risk requests trigger alerts, session flags, or observation policies. In online
deployment, high-risk requests are blocked, and policy instructions can be sent to a WAF, API
| gateway, | zero-trust | gateway, |     | or security |     | operations |     | platform. |     |
| -------- | ---------- | -------- | --- | ----------- | --- | ---------- | --- | --------- | --- |
The framework retains fail-open bypass, policy rollback, and allowlist mechanisms. If de-
tectionbecomesunavailableorthecontextisincomplete,thesystemcandegradetoobservation
8

mode so that a security-component failure does not directly interrupt the application. All evi-
dence, decisions, and response actions are written to audit records for subsequent explanation
| and policy review. |     |             |     |             |     |     |
| ------------------ | --- | ----------- | --- | ----------- | --- | --- |
| 5 Experimental     |     | Design      |     | and Results |     |     |
| 5.1 Experimental   |     | Environment |     | and Data    |     |     |
To evaluate the feasibility of the overall mechanism, a Web application testbed and a
reverse-proxy detection prototype were constructed in a controlled local environment. Ex-
perimental scripts generated reproducible request sequences and recorded the ground-truth
label, framework decision, and decision latency for each request. The experiment contained
no real user data, and its sample distribution does not represent the natural prevalence of
| authorization-risk | events | in  | production. |     |     |     |
| ------------------ | ------ | --- | ----------- | --- | --- | --- |
The dataset contained 2,000 samples: 1,000 normal accesses, 600 object-access risk events,
and400permission-and-contextriskevents, asshowninTable2. Object-accessriskeventscon-
sisted of horizontal object substitution and sequential object probing. Permission-and-context
risk events consisted of privileged operations, conflicting identity claims, and anomalous au-
thentication context. These aggregate categories evaluate how different evidence sources work
together within the same framework; they are not used for separate fine-grained performance
comparisons.
|               |                        | Table      | 2    | Experimental sample | composition        |       |
| ------------- | ---------------------- | ---------- | ---- | ------------------- | ------------------ | ----- |
|               | Sample                 | category   |      |                     | Count Percentage/% |       |
|               | Normal                 | access     |      |                     | 1000               | 50.0  |
|               | Object-access          |            | risk | event               | 600                | 30.0  |
|               | Permission-and-context |            |      | risk event          | 400                | 20.0  |
|               | Total                  |            |      |                     | 2000               | 100.0 |
| 5.2 Baselines | and                    | Evaluation |      | Metrics             |                    |       |
| Four methods  | were                   | compared:  |      |                     |                    |       |
(1) URL rules, which classify requests using path terms such as admin, delete, role, export,
| and download. |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
(2) Frequency detection, which identifies anomalies using the number of requests or distinct
| ObjectId | changes | within | a time | interval. |     |     |
| -------- | ------- | ------ | ------ | --------- | --- | --- |
(3) Rules plus frequency, which takes the union of the first two strategies.
(4) The proposed framework, which jointly uses transaction correlation, object-access evi-
dence, identity and authentication context, behavioral anomalies, network environment,
| and endpoint-operation |     |     | risk. |     |     |     |
| ---------------------- | --- | --- | ----- | --- | --- | --- |
The evaluation metrics are accuracy, precision, recall, F1 score, false-positive rate (FPR),
and false-negative rate (FNR). TP denotes an authorization-risk event correctly classified as
risky; FP denotes a normal access misclassified as risky; TN denotes a normal access correctly
9

classified as non-risky; and FN denotes an authorization-risk event not classified as risky. The
| metrics       | are calculated |        | as         |         |     |     |           |      |                  |     |     |     |
| ------------- | -------------- | ------ | ---------- | ------- | --- | --- | --------- | ---- | ---------------- | --- | --- | --- |
|               |                |        |            | TP +TN  |     |     |           |      | TP               |     |     |     |
|               | Accuracy       |        | =          |         |     | ,   | Precision | =    |                  | ,   |     |     |
|               |                |        | TP +FP     | +TN     | +FN |     |           |      | TP +FP           |     |     |     |
|               |                |        | TP         |         |     |     |           |      | 2PrecisionRecall |     |     |     |
|               |                | Recall | =          | ,       |     |     |           | F1 = |                  |     | ,   | (3) |
|               |                |        | TP +FN     |         |     |     |           |      | Precision+Recall |     |     |     |
|               |                |        | FP         |         |     |     |           |      | FN               |     |     |     |
|               |                | FPR    | =          | ,       |     |     | FNR       | =    |                  | .   |     |     |
|               |                |        | FP +TN     |         |     |     |           |      | FN +TP           |     |     |     |
| 5.3 Framework |                |        | Validation | Results |     |     |           |      |                  |     |     |     |
Table 3 reports the validation results of the four methods on 2,000 samples. URL rules
classified 517 authorization-risk events as risky but also misclassified 231 normal accesses,
yielding an F1 score of 59.15%. Frequency detection produced no false positives among normal
accesses but classified only 552 authorization-risk events as risky, for a recall of 55.20%. Rules
plus frequency improved recall to 83.70% but still misclassified 231 normal accesses. The
proposed framework classified 998 authorization-risk events as risky and produced no false
positives among normal accesses. Its accuracy, recall, and F1 score were 99.90%, 99.80%, and
| 99.90%,   | respectively. |       |              |        |            |            |       |             |         |     |          |       |
| --------- | ------------- | ----- | ------------ | ------ | ---------- | ---------- | ----- | ----------- | ------- | --- | -------- | ----- |
|           |               | Table | 3 Comparison |        | of overall | framework  |       | validation  | results |     |          |       |
| Method    |               |       | TP FP        |        | TN FN      | Accuracy/% |       | Precision/% |         |     | Recall/% | F1/%  |
| URL rules |               |       | 517 231      |        | 769 483    |            | 64.30 |             | 69.12   |     | 51.70    | 59.15 |
| Frequency | detection     |       | 552          | 0 1000 | 448        |            | 77.60 |             | 100.00  |     | 55.20    | 71.13 |
| Rules +   | frequency     |       | 837 231      |        | 769 163    |            | 80.30 |             | 78.37   |     | 83.70    | 80.95 |
| Proposed  | framework     |       | 998          | 0 1000 |            | 2          | 99.90 |             | 100.00  |     | 99.80    | 99.90 |
Figure 3 provides a visual comparison of the four evaluation metrics across the methods.
100
80
%/eulav
60
cirteM
40
20
0
|     |     | URL    | rules        |     | Frequency |            |         | Combined  |         |     | Framework |     |
| --- | --- | ------ | ------------ | --- | --------- | ---------- | ------- | --------- | ------- | --- | --------- | --- |
|     |     |        |              |     | Accuracy  |            |         | Precision |         |     |           |     |
|     |     |        |              |     | Recall    |            |         | F1 score  |         |     |           |     |
|     |     | Figure | 3 Comparison |     | of        | validation | metrics | across    | methods |     |           |     |
10

In the controlled samples, URL keywords could not represent changes in object owner-
ship, while frequency thresholds failed to cover low-frequency authorization-risk events. The
proposed framework’s results arose from the joint use of multiple forms of context within the
same transaction and risk model. Because a fixed testbed script generated the data, the met-
rics demonstrate only the feasibility of framework-level decisions in the specified scenarios and
| should |                 | not be generalized |     | as universal |     | production |     | performance. |     |     |     |     |
| ------ | --------------- | ------------------ | --- | ------------ | --- | ---------- | --- | ------------ | --- | --- | --- | --- |
| 5.4    | Framework-Level |                    |     | Ablation     |     | Study      |     |              |     |     |     |     |
To evaluate the contribution of the key mechanisms, three framework-level ablations were
selected to isolate the effects of key evidence categories and the priority-constraint mechanism.
The results are listed in Table 4. Removing runtime object-access evidence reduced recall
from 99.80% to 68.50%, showing that object context is an important basis for authorization-
risk identification. Removing behavioral-sequence evidence yielded an F1 score of 99.70%,
indicating that this evidence mainly supplements sequential object switching and slow probing.
Removing the high-risk priority constraint reduced recall to 58.60%, suggesting that linear
weighting alone can allow low-risk components to mask high-severity evidence.
|     |          |                     |     | Table    | 4        | Framework-level |            | ablation | results |          |       |       |
| --- | -------- | ------------------- | --- | -------- | -------- | --------------- | ---------- | -------- | ------- | -------- | ----- | ----- |
|     | Ablation |                     |     |          |          |                 | Accuracy/% |          |         | Recall/% | F1/%  | FNR/% |
|     | Full     | framework           |     |          |          |                 |            | 99.90    |         | 99.80    | 99.90 | 0.20  |
|     | Without  | object-access       |     | evidence |          |                 |            | 84.25    |         | 68.50    | 81.31 | 31.50 |
|     | Without  | behavioral-sequence |     |          | evidence |                 |            | 99.70    |         | 99.40    | 99.70 | 0.60  |
Without high-risk priority constraints 79.30 58.60 73.90 41.40
Here, object-access evidence refers to the basic binary set in Eq. (1). The ablation re-
sult establishes the contribution of this evidence category within the current framework-level
implementation.
| 5.5 | Prototype |     | Runtime |     | Feasibility |     |     |     |     |     |     |     |
| --- | --------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
To confirm that the framework can operate in a proxy path, a single-host prototype test
was conducted with 100 concurrent requests and 1,000 total requests. The results are shown in
Table 5. The mean decision-computation latency was 0.077ms, the P99 latency was 0.137ms,
and the end-to-end throughput was 91.924RPS. Mean computation latency includes only risk-
evidence retrieval and decision processing, whereas throughput also includes proxy forwarding,
testbed application processing, client scheduling, and queueing; the two measurements are not
directly convertible.
|     |     |     | Table | 5   | Single-host | prototype |     | runtime | feasibility |     | test |     |
| --- | --- | --- | ----- | --- | ----------- | --------- | --- | ------- | ----------- | --- | ---- | --- |
Concurrency Requests Throughput/RPS Mean decision latency/ms P99/ms Peak memory/MB
|     |     | 100 | 1000 |     | 91.924 |     |     |     |     | 0.077 | 0.137 | 357.426 |
| --- | --- | --- | ---- | --- | ------ | --- | --- | --- | --- | ----- | ----- | ------- |
This result shows only that the current single-host prototype can complete online risk
decisions. It does not support conclusions about performance at other operating scales or
11

under long-duration and complex deployment conditions.
5.6 Summary of Experimental Findings
Intheconstructedscenarios,themulti-sourceruntime-evidenceframeworkachievedhigher
recallandF1scoresthantheselectedURL-ruleandfrequency-basedbaselines. Theframework-
level ablation shows that object-access evidence and high-risk priority constraints are the prin-
cipal mechanisms affecting recall in the current prototype. The single-host test verifies basic
feasibility for online risk decisions. Together, these results support the mechanism-level feasi-
bility of the overall framework in the specified validation environment.
6 Discussion
6.1 Applicability and Operating Mechanism
This study provides unified definitions of data objects, evidence interfaces, risk con-
straints, and response processes to explain how multi-source traﬀic-side evidence forms action-
able authorization-risk decisions. Framework validation and ablation show that object-access
evidence, high-risk priority constraints, and the joint use of identity, behavior, and endpoint
context affect the decision outcome. The overall design therefore forms a relatively complete
detection and response loop in the specified controlled environment.
The framework is applicable to Web applications and API systems that require enhanced
runtime authorization-risk auditing. In new systems, it can operate as a monitoring layer com-
plementarytoRBACorABAC.Inlegacysystems,itcanprovideindependentauditingwithout
large-scale application-code changes. In multi-gateway or multi-microservice environments, it
can organize cross-endpoint context at a common ingress. The framework can also cooperate
with continuous evaluation, least privilege, and policy enforcement points in a zero-trust ar-
chitecture[15], exporting risk results to gateways or security operations platforms for unified
response.
Inthecurrentprototype,E (t)isrepresentedasabinaryobject-evidenceset,identityand
u,r
authentication context is evaluated through deterministic consistency rules, and endpoint risk
is configured from request semantics and predefined business impact. The conclusions there-
fore concern the feasibility of the unified evidence-organization, risk-fusion, and coordinated-
response mechanism.
6.2 Threats to Validity and Limitations
The experiment has four principal threats to validity. First, the samples were generated
by local testbed scripts and were balanced between positive and negative cases; this differs
from production environments, where authorization-risk events are rare and business traﬀic
has a long-tail distribution. Second, the baselines consist mainly of URL rules and frequency
strategies and do not cover all static-analysis, differential-testing, and learning-based methods.
Third, evidence-confirmation rules, risk weights, and decision thresholds depend on the seman-
tics of the testbed interfaces and would require recalibration for other systems. Fourth, the
performance measurements come from a single-host prototype and do not reflect long-duration
operation or complex deployment conditions. The findings should therefore be interpreted
as framework validation in a controlled environment rather than universal performance for
arbitrary Web applications.
12

The method has three general limitations. First, traﬀic-side analysis depends on the visi-
bilityofapplication-layercontentandkeybusinessfields;whenencryptedcontentisunavailable
or identifiers are heavily obfuscated, evidence completeness may be reduced. Second, the pro-
totype’s evidence rules, risk weights, thresholds, and endpoint configuration are tied to the
semantics of the testbed and require recalibration when transferred to another application.
Third, the controlled balanced samples and single-host implementation do not capture the
class imbalance, long-term state variation, and deployment complexity of production traﬀic.
Further evaluation with heterogeneous Web applications and real gateway traﬀic is needed to
assess cross-scenario applicability and operational stability.
7 Conclusion
This paper addresses the diﬀiculty of identifying and responding to authorization risks
under valid Web sessions from traﬀic by proposing an overall non-intrusive traﬀic analysis
framework. TheframeworktreatseachHTTPrequestastheunitofonlineriskdecision-making
and uses the correlated request–response transaction to organize and update object-access
evidence, identity and authentication context, behavioral sequences, network environment,
and endpoint-operation risk. Weighted fusion and high-risk priority constraints then produce
graded response decisions.
On a controlled testbed with synthetic balanced samples, the framework achieved higher
risk-decision metrics than the selected URL-rule, frequency-detection, and combined baselines.
Framework-level ablation confirmed the roles of object-access evidence and high-risk priority
constraints, and the single-host test showed that the prototype could complete online risk
decisions. These results demonstrate mechanism-level feasibility in the specified validation
environment; broader applicability requires evaluation with heterogeneous Web applications
and real gateway traﬀic.
Author Contributions
Siqi Lin: conceptualization, overall framework design, primary drafting, and final revision.
Yuchao Luo and Borui Qiu: system design and implementation, experimental-scenario
construction, and authorization-risk sample design.
Yiran Wang: experimental data organization, result analysis, and figure preparation.
Zihan Zhu: related-work review, manuscript formatting, and reference checking.
13

中文版本
基于非侵入式流量分析的Web应用
越权风险识别与联动处置框架*
林思齐1,2,† 罗宇超3 朱梓涵4 王怡然1 邱博睿3
1（沈阳建筑大学中新国际工程学院，沈阳 110168）
2（厦门萌火科技有限公司，厦门 361000）
3（沈阳建筑大学计算机科学与工程学院，沈阳 110168）
4（沈阳建筑大学管理学院，沈阳 110168）
†通信作者：林思齐，E-mail: lsq@moefire.net
摘要：【目的】针对Web应用合法会话下的越权访问具有业务语义依赖强、协议层特征不显著且难以在
流量侧实时处置的问题，提出一种基于非侵入式流量分析的越权风险识别与联动处置框架。
【方法】通过请求–响应事务关联提取访问主体、业务端点、对象标识、认证状态和行为序列等运行时上
下文，将对象访问证据、身份一致性、行为异常、认证上下文、网络环境和端点操作风险统一映射为可
解释的风险分量，并采用加权融合与高风险优先约束形成分级判定结果，驱动放行、告警、阻断和外部
策略联动。各风险分量采用确定性、可解释的规则化方法实现，本文重点验证多源证据组织、风险融合
和联动处置闭环的总体机制。
【结果】在实验环境中构造的2000条类别平衡样本中，正常访问样本和授权风险事件样本各1000条。框架
验证结果显示，1000条授权风险事件中有998条被判定为风险，正常访问未出现误判；准确率、精确率、
召回率和F1值分别为99.90%、100.00%、99.80%和99.90%。去除运行时对象证据后F1值降至81.31%，去
除高风险优先约束后降至73.90%。在并发数为100、请求总数为1000的运行可行性测试中，单次风险决
策的平均计算时延为0.077ms，P99时延为0.137ms。
【结论】实验结果表明，该框架能够在不修改业务代码的条件下组织多源运行时证据，并形成可执行的
越权风险判定与联动处置闭环。上述结果仅表明总体机制在所设验证场景下具有可行性，尚不足以说明
其在生产环境中的普遍适用性。
关键词：Web应用安全；越权访问；非侵入式流量分析；运行时证据；联动处置
中图分类号：TP393.08
1 引言
1.1 研究背景
Web应用与API系统已经成为政企信息系统、业务中台和移动应用后端的主要服务形态。用
户编号、合同编号、订单编号、文件编号和设备编号等业务对象标识，通常以URL路径段、查询
参数、表单字段或JSON请求体字段的形式在客户端与服务端之间传递。对象标识的显式传递
提高了接口调用与系统集成效率，也扩大了对象级授权失效的攻击面。OWASP API Security
Top 10将Broken Object Level Authorization列为API安全的首要风险之一，指出攻击者可能通
过修改请求中的对象标识访问不属于自己的资源[1]。
与未登录访问、SQL注入和跨站脚本等传统漏洞相比，越权访问具有更强的业务语义依赖。
攻击请求往往携带有效会话、有效令牌和正常参数格式，仅依靠网络层特征、状态码或URL黑
*本文系辽宁省大学生创新创业训练计划基金项目“基于非侵入式流量分析的Web应用越权访问风险识别与处置
系统”（项目编号：S202610153008）的研究成果之一。
14

名单难以判断当前主体是否有权执行目标操作。随着Web系统向微服务化、网关化和前后端分
离演进，访问主体、业务对象、角色声明和认证事件分布在多个接口与服务之间，授权风险的
运行时识别难度进一步上升。
现有系统通常依赖代码级鉴权、RBAC/ABAC策略、API网关规则和WAF签名完成防护。
这些机制仍是访问控制的主体，但在接口快速迭代、第三方组件接入、存量系统改造和跨系统
调用等场景中，可能出现规则滞后、对象语义不可见或策略执行点分散的问题。因此，需要在
不替代业务鉴权的前提下，从请求–响应流量中提取运行时访问证据，形成独立的风险识别、审
计和联动处置能力。
1.2 问题分析
越权风险的核心不是“用户是否已登录”，而是“当前访问主体是否有权访问目标对象或执
行当前操作”。当攻击者在合法登录状态下修改对象编号，或普通用户尝试调用高权限操作时，
请求的HTTP方法、参数格式和响应状态均可能与正常业务请求相似。生产环境中的越权行为
还具有低频、慢速、单次触发和跨端点分布等特点，难以由单一阈值规则稳定覆盖。
从流量侧建立补充防护框架，需要解决四个共性问题：一是关联请求与响应，恢复可解释
的业务事务；二是统一表示访问主体、端点、对象、认证状态和历史行为等异构上下文；三是
在缺乏业务权限数据库的情况下，将多源证据转换为可执行的风险判断；四是使风险判定结果
能够与网关、WAF和安全运营平台形成处置闭环。
本文聚焦流量侧多源证据的统一组织、风险融合与联动处置，研究不同证据来源如何在同
一事务和同一决策链中协同发挥作用。
1.3 本文贡献
本文提出一种基于非侵入式流量分析的Web应用越权风险识别与联动处置框架，主要贡献
如下：
（1）提出请求–响应事务驱动的运行时上下文提取流程，在代理或网关侧统一获得访问主体、
端点、对象、认证状态和行为序列等信息；
（2）构建统一的运行时证据抽象，将对象访问证据、身份一致性、行为异常、认证上下文、
网络环境和端点操作风险映射为统一风险分量，而不依赖单一URL规则或访问频率；
（3）设计加权融合与高风险优先约束相结合的可解释判定机制，并将结果映射为放行、告
警、阻断和外部策略联动，形成判定–处置闭环；
（4）在实验环境中开展总体对比、框架级消融和运行可行性测试，验证总体框架的风险判
定能力、关键机制贡献及运行开销。
2 相关工作
2.1 Web应用对象级越权访问
对象级越权通常与IDOR（Insecure Direct Object Reference）和BOLA（Broken Object
Level Authorization）相关。OWASP Web Security Testing Guide将IDOR定义为应用直接使
用用户可控输入指向数据库记录、文件或其他资源，导致攻击者可以通过修改参数绕过授权检
查[2]。OWASP Top 10也长期将访问控制失效列为Web应用最重要的安全风险之一[3]。
对象级越权并非简单的认证失败。用户可能已经通过登录认证，令牌也处于有效期内，但
后端未校验该用户与目标对象之间的授权关系。该类风险既可能发生在读取操作中，也可能发
生在修改、删除、审批、导出等具有更高危害的操作中。与传统漏洞相比，对象级越权更依赖
业务数据结构和访问上下文，自动化检测难度更高。
15

2.2 规则防护与自动化扫描方法
基于规则的Web防护方法通常通过URL黑白名单、参数约束、敏感路径匹配和签名检测完
成过滤。WAF和API网关可快速拦截已知攻击模式，但其策略维护依赖人工配置，难以自动理
解“用户A是否有权访问对象B”。当业务接口频繁变化或对象字段命名不统一时，规则方法容
易出现漏配和误报。
自动化黑盒扫描工具能够发现部分输入校验、注入和配置类漏洞。Bau等[4]和Doupé等[5]对
黑盒Web漏洞扫描工具进行了系统评估，指出该类工具在状态保持、认证后路径覆盖和业务逻
辑漏洞识别方面仍存在局限。RESTler通过API规范推断请求间的生产者–消费者依赖并生成有
状态请求序列[6]，增强了复杂REST API的状态覆盖，但其主要目标是测试阶段的缺陷发现，而
非生产流量中的在线授权判定。对象级越权通常需要比较不同用户、不同对象和不同角色下的
响应与状态，因此仅依靠通用扫描器或接口序列生成仍难以恢复完整授权语义。
2.3 访问控制模型与运行时监测
RBAC将权限与角色关联，能够降低权限管理复杂度[7]；ABAC进一步将主体、对象、操
作和环境等属性纳入授权决策[8]。这些访问控制模型为系统内部权限设计提供了理论基础，但
在运行时外部流量分析场景中，检测系统通常无法直接读取业务系统的完整权限配置、数据库
关系和代码逻辑。Sun等[9]利用静态分析推断不同角色的访问控制假设，AuthScope则通过差分
流量分析与字段替换发现在线服务中的授权缺陷[10]。前者依赖源代码，后者面向主动测试，两
者均说明跨角色或跨主体对照是识别授权缺陷的重要依据。
运行时监测方法尝试通过应用状态、请求序列和历史行为识别异常。Cova等[11]提出基于应
用内部状态的异常检测方法，Felmetsger等[12]从逻辑漏洞角度探索Web应用运行时检测。上述
研究说明，业务逻辑类安全问题需要结合状态和上下文进行判断。本文与现有静态分析、主动
扫描和应用内插桩方法的区别在于：本文以被动或代理侧请求–响应事务为输入，研究如何在流
量侧组织多类运行时授权风险证据，并将风险判断直接映射为分级处置。本文关注总体框架与
协同机制，各类证据分量仅作为统一决策链中的组成部分进行实现与验证。
3 方法总体框架
3.1 总体架构
本文框架由流量接入、事务关联、上下文提取、运行时证据组织、风险融合、联动处置和
状态审计等部分构成，如图1所示。系统可部署于反向代理、API网关或旁路观测节点。在线模
式在请求转发前基于当前请求上下文和既有运行时证据完成风险判定，并在响应返回后更新事
务状态；旁路模式则主要输出审计与告警结果。本文所称“非侵入式”是指无需修改被保护应
用的业务代码和内部授权逻辑；反向代理和API网关模式仍可能位于业务流量的在线转发链路
中。
16

非侵入式流量接入层 被保护Web应用
客户端/调用方
反向代理/API网关/旁路流量 或API系统
请求–响应事务关联
主体与认证上下文 端点与对象上下文 行为与网络上下文
运行时授权风险证据
共享状态存储
风险融合与优先约束 事务、上下文、证据
策略与审计日志
联动处置与审计输出
图 1 越权风险识别与联动处置总体框架
3.2 主要符号与数据对象
本文以一次HTTP请求作为在线风险判定单元，并在响应返回后形成关联事务T，用于运行
时证据更新与审计。表1列出了框架使用的主要数据对象。UserKey、EndpointKey和ObjectId
分别用于表示访问主体、归一化端点和业务资源实例；E (t)表示在时刻t前，主体u对资源类型
u,r
r已形成的运行时对象访问证据集合。
表 1 主要符号及含义
符号 含义
T 一次已关联的HTTP请求–响应事务及其时间、网络和业务
上下文，用于证据更新与审计
UserKey 访问主体标识，可由账号、会话或低可信临时标识表示
EndpointKey HTTP方法与归一化路径组合形成的端点标识
ObjectId 指向业务资源实例的候选标识
E (t) 时刻t前主体u对资源类型r已形成的基础运行时对象访问证
u,r
据集合
3.3 数据处理流程与部署模式
系统接收客户端发往Web应用的HTTP/HTTPS请求后，首先从请求头、Cookie、JWT、查
询参数、表单参数和JSON请求体中提取UserKey、EndpointKey、ObjectId及认证状态等上下
文，并结合既有对象证据和近期访问序列形成风险分量。风险融合模块在请求转发前输出综合
风险等级，处置模块据此执行放行、告警、阻断或向外部策略执行点发送指令。当前请求的风
险判定仅使用请求到达时可获得的上下文以及此前事务已经形成的运行时证据。对于已放行的
请求，系统在响应返回后将请求与响应关联为事务T，补充响应摘要和业务结果，并更新供后
续请求使用的运行时证据与审计状态；当前响应不反向参与同一请求的风险判定。
17

在反向代理或API网关模式下，系统可在TLS终止后的明文HTTP层获取完整事务，并支持
在线阻断；在旁路模式下，系统通过镜像流量、网关日志或审计日志进行观测和告警。当无法
获得应用层明文时，只能进行元数据级分析，无法保证对象标识和业务结果提取的完整性。
3.4 原型实现与研究范围
本文聚焦总体框架及其协同机制。为保证框架级机制能够运行并具备可解释性，原型系统
采用确定性规则实现各风险分量。对象访问证据由有效访问主体、成功业务结果、预配置事务
语义和当前风险判定共同确认，并以二值集合进行维护；身份与认证风险依据账号、会话、令
牌、角色声明及近期认证上下文之间的一致性计算；行为风险根据时间窗口内的对象切换、访
问频率和请求序列特征确定；端点操作风险则结合HTTP方法、路径语义和预设业务影响等级
进行配置。
本文实验主要验证上述组件能否在统一数据流和决策链中协同运行，关键证据与融合机制
是否影响判定结果，以及原型能否在受控环境中完成在线风险决策。因此，本文结论限定于所
述实验条件下的框架级机制验证。
4 关键机制设计
4.1 请求–响应关联与上下文提取
请求–响应关联用于将协议消息恢复为可解释的业务事务。事务T包含请求方法、归一化路
径、请求头、参数与请求体摘要、响应状态码、响应体摘要、业务成功状态、客户端地址和时
间戳等信息。HTTP方法与消息语义遵循RFC 9110[13]，JWT声明字段参考RFC 7519[14]。
在代理和网关模式下，可依据连接上下文、请求序号、Trace ID或网关注入标识完成确定
性关联；旁路模式可依据五元组、请求特征和时间窗口进行近似关联。对于长连接、异步接口
和批量请求，系统记录关联置信度，避免将不完整事务用于高可信证据更新。
UserKey优先使用账号标识，其次使用会话或令牌标识；当上述信息不可见时，可结合源
地址、User-Agent和设备特征形成低可信临时标识。EndpointKey通过HTTP方法与归一化路径
组合生成，路径中的数字串、UUID和随机标识被替换为占位符。ObjectId则从路径、查询参数、
表单或JSON字段中提取，并通过字段语义、取值形态和响应结构过滤明显的页码、时间戳和金
额字段。
4.2 运行时授权风险证据
框架将异构上下文映射为六类基础风险分量：
（1）对象访问证据风险x ：反映当前ObjectId是否具备已确认的运行时访问证据；
obj
（2）身份一致性风险x ：反映账号、会话、令牌和角色声明之间是否存在明显冲突；
id
（3）行为异常风险x ：反映短时间对象切换、连续编号访问或异常访问序列；
beh
（4）认证上下文风险x ：反映敏感操作是否存在近期有效认证或权限变更事件作为支撑；
auth
（5）网络环境风险x ：反映地址漂移、异常代理或共享出口等辅助信息；
net
（6）端点操作风险s ：反映当前HTTP方法和端点操作的潜在业务影响。
ep
对象访问证据的基础表示如式（1）所示。在当前原型中，只有同时满足主体有效、响应确
认业务成功、事务符合预配置确认语义，且请求未被判定为中风险或高风险时，该事务才被视
为可信事务。可信事务仅用于更新后续请求所使用的证据，不能改变其自身已经形成的判定结
果。该定义为框架级验证提供可执行的证据接口。
E (t) = {o | o在时刻t前由主体u的可信事务确认} (1)
u,r
若当前对象已存在于E (t)中，则对象证据风险较低；若当前对象尚未出现在该集合中，且
u,r
18

同时伴随异常对象切换、敏感操作或身份上下文冲突，则风险提高。为避免共享网络和移动网
络用户受到不合理影响，网络环境风险不单独触发阻断。
4.3 风险融合与高风险优先约束
∑
6
| 各风险分量归一化至[0,1]。基础风险采用固定权重求和，权重满足w |     |     |     |     |     |     |     | ≥ 0且 | w = 1。 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ |
|                                   |     |     |     |     |     |     |     | i    | i=1 i  |
为避免高危证据在多个低风险分量的加权结果中被稀释，框架设置可解释的高风险优先约束。
总风险按式（2）计算：
|     |     |     |     |     | {   | [ ]} |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
∑6
|     |     |     | R    | = min | 1,max | 0, w x | ,   |     |     |
| --- | --- | --- | ---- | ----- | ----- | ------ | --- | --- | --- |
|     |     |     | base |       |       | i i    |     |     |     |
(2)
i=1
|      |     |     |        |         | ,max({h | | ∈ H}∪{0})),      |     |     |          |
| ---- | --- | --- | ------ | ------- | ------- | ------------------ | --- | --- | -------- |
|      |     |     | R      | = max(R |         | j                  |     |     |          |
|      |     |     | total  |         | base    | j                  |     |     |          |
| 其中，x | =   | (x  | ,x ,x  | ,x      | ,x ,s   | )；H表示被触发的高风险条件集合，h |     |     | ∈ [0,1]表 |
|      |     | obj | id beh | auth    | net ep  |                    |     |     | j        |
示对应风险下限。内层最大值中加入0，用于定义未触发任何高风险条件时的计算结果。高风险
条件仅由可解释的组合证据触发，例如“对象证据缺失且操作敏感”或“身份声明冲突且缺少
有效认证事件”，而不是由单一网络特征触发。
风险判定流程如图2所示。
提取运行时风险证据
|     | 对象访问证据 |     |     | 身份/认证上下文 |     | 行为/网络上下文 |     | 端点操作风险 |     |
| --- | ------ | --- | --- | -------- | --- | -------- | --- | ------ | --- |
加权融合与高风险优先约束
风险等级映射
|     |     | 低风险：放行 |     |     | 中风险：告警/观察      |     | 高风险：阻断/联动 |     |     |
| --- | --- | ------ | --- | --- | -------------- | --- | --------- | --- | --- |
|     |     |        |     | 图 2 | 运行时风险证据融合与处置流程 |     |           |     |     |
联动处置机制
4.4
处置模块根据R
|     |     |     | total 和策略阈值将请求划分为低、中、高风险。低风险请求放行并记录审计 |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
日志；中风险请求触发告警、会话标记或持续观测策略；高风险请求在在线部署模式下予以阻
断，并可向WAF、API网关、零信任网关或安全运营平台输出策略指令。
框架保留故障旁路、策略回滚和白名单机制。当检测模块不可用或上下文不完整时，可降
级为观察模式，避免安全组件故障直接造成业务不可用。所有证据、判定结果和处置动作均写
入审计记录，支持事后解释与策略复核。
19

5 实验设计与结果分析
实验环境与数据来源
5.1
为验证总体框架的机制可行性，本文在实验环境中搭建Web应用测试系统，并实现反向代
理式检测系统。预设实验脚本生成可重复的请求序列，实验系统同步记录样本标签、框架判定
结果和决策耗时。实验不包含真实用户隐私数据，样本类别比例也不代表生产环境中授权风险
事件的自然分布。
样本共2000条，其中正常访问1000条、对象访问风险事件600条、权限与上下文风险事件400
条，如表2所示。对象访问风险事件由跨主体对象标识替换和连续对象探测样本组成；权限与上
下文风险事件由超出当前角色权限的操作、身份声明冲突和认证上下文异常样本组成。上述聚
合分类用于验证不同证据来源在同一框架中的协同判定能力，不对各细分类别作独立性能比较。
|     |            | 表 2 实验样本构成 |      |      |       |     |     |
| --- | ---------- | ---------- | ---- | ---- | ----- | --- | --- |
|     | 样本类别       |            | 数量/条 |      | 占比/%  |     |     |
|     | 正常访问       |            |      | 1000 | 50.0  |     |     |
|     | 对象访问风险事件   |            |      | 600  | 30.0  |     |     |
|     | 权限与上下文风险事件 |            |      | 400  | 20.0  |     |     |
|     | 合计         |            |      | 2000 | 100.0 |     |     |
5.2 对比方法与评价指标
实验设置四组方法进行对比：
（1）URL规则方法，仅依据admin、delete、role、export和download等路径或关键词进行判
定；
（2）频率检测方法，根据单位时间请求次数或不同ObjectId的切换次数判断异常；
（3）规则+频率方法，对前两类策略的判定结果取并集；
（4）本文框架，综合事务关联、对象访问证据、身份与认证上下文、行为异常、网络环境
和端点操作风险进行判定。
评价指标包括准确率（Accuracy）、精确率（Precision）、召回率（Recall）、F1值、误报率
（FPR）和漏报率（FNR）。其中TP表示授权风险事件被正确判定为风险，FP表示正常访问被误
判为风险，TN表示正常访问被正确判定为非风险，FN表示授权风险事件未被判定为风险。各
指标按式（3）计算。
|          |        | TP +TN  |     |           | TP               |     |       |
| -------- | ------ | ------- | --- | --------- | ---------------- | --- | ----- |
| Accuracy | =      |         | ,   | Precision | =                | ,   |       |
|          | TP +FP | +TN +FN |     |           | TP +FP           |     |       |
|          | TP     |         |     |           | 2PrecisionRecall |     |       |
| Recall   | =      | ,       |     | F1        | =                |     | , (3) |
|          | TP +FN |         |     |           | Precision+Recall |     |       |
|          | FP     |         |     |           | FN               |     |       |
| FPR      | =      | ,       |     | FNR       | =                | .   |       |
|          | FP +TN |         |     |           | FN +TP           |     |       |
框架验证结果
5.3
表3给出了四组方法在2000条样本上的框架验证结果。URL规则方法将517条授权风险事件
判定为风险，同时将231条正常访问误判为风险，F1值为59.15%；频率检测方法未产生正常访
问误判，但仅将552条授权风险事件判定为风险，召回率为55.20%；规则+频率方法的召回率提
高至83.70%，但仍误判231条正常访问。本文框架将998条授权风险事件判定为风险，正常访问
20

未出现误判，准确率、召回率和F1值分别为99.90%、99.80%和99.90%。
|     |       |     | 表 3 总体框架验证结果对比 |       |       |     |       |      |
| --- | ----- | --- | -------------- | ----- | ----- | --- | ----- | ---- |
|     | TP FP | TN  | FN             | 准确率/% | 精确率/% |     | 召回率/% | F1/% |
方法
| URL规则 | 517 231 | 769    | 483 | 64.30   |     | 69.12  | 51.70 | 59.15 |
| ----- | ------- | ------ | --- | ------- | --- | ------ | ----- | ----- |
| 频率检测  | 552     | 0 1000 | 448 | 77.60   |     | 100.00 | 55.20 | 71.13 |
| 规则+频率 | 837 231 | 769    | 163 | 80.30   |     | 78.37  | 83.70 | 80.95 |
| 本文框架  | 998     | 0 1000 |     | 2 99.90 |     | 100.00 | 99.80 | 99.90 |
图3直观比较了四种方法在各项评价指标上的结果。
100
80
%/值标指
60
40
20
0
|     | URL规则 |     | 频率检测 |     | 规则+频率 |     | 本文框架 |     |
| --- | ----- | --- | ---- | --- | ----- | --- | ---- | --- |
|     |       |     |      | 准确率 | 精确率   |     |      |     |
|     |       |     |      | 召回率 | F1值   |     |      |     |
图 3 不同方法的框架验证指标对比
实验样本中，URL关键词难以表征对象归属关系的变化，频率策略则难以覆盖低频授权风
险事件。本文框架的验证结果来自多类上下文在同一事务中的协同使用。由于测试数据由预设
实验脚本生成，相关指标仅用于说明总体框架在所设场景下的判定可行性，不能外推为生产系
统中的普遍性能。
5.4 框架级消融实验
为验证总体框架中关键机制的贡献，本文设置三组框架级消融，用于分别考察关键证据类别
和优先约束机制对判定结果的影响。结果见表4。去除运行时对象访问证据后，召回率由99.80%
降至68.50%，说明对象访问证据是识别授权风险的重要基础；去除行为序列证据后，F1值为
99.70%，表明该证据主要补充连续对象切换和慢速探测；去除高风险优先约束后，召回率降至
58.60%，说明仅采用线性加权容易使高危证据在其他低风险分量的加权结果中被稀释。
本文所称“对象访问证据”指式（1）所示的基础二值集合，消融结果用于说明该类证据在
当前框架级实现中的作用。
21

|           |     | 表 4 框架级消融实验结果 |       |            |       |
| --------- | --- | ------------- | ----- | ---------- | ----- |
| 消融组       |     | 准确率/%         | 召回率/% | F1/% 漏报率/% |       |
| 完整框架      |     | 99.90         | 99.80 | 99.90      | 0.20  |
| 去除对象访问证据  |     | 84.25         | 68.50 | 81.31      | 31.50 |
| 去除行为序列证据  |     | 99.70         | 99.40 | 99.70      | 0.60  |
| 去除高风险优先约束 |     | 79.30         | 58.60 | 73.90      | 41.40 |
5.5 运行可行性
为验证框架在代理链路中的运行可行性，本文在并发数为100、请求总数为1000的条件下开
展单机测试，结果见表5。决策模块平均计算时延为0.077ms，P99时延为0.137ms，端到端吞吐
量为91.924RPS。平均计算时延仅统计风险证据读取与决策过程，吞吐量则包含代理转发、实
验应用处理、客户端调度和排队等待，两者不可直接换算。
|          |         | 表 5 单机运行可行性测试 |       |        |         |
| -------- | ------- | ------------- | ----- | ------ | ------- |
| 并发数 请求数  | 吞吐量/RPS | 平均决策时延/ms     |       | P99/ms | 峰值内存/MB |
| 100 1000 | 91.924  |               | 0.077 | 0.137  | 357.426 |
该结果仅表明当前单机实现能够完成在线风险决策，不能据此推断其他运行规模或长周期、
复杂部署条件下的系统性能。
5.6 实验小结
在所构造的实验场景中，多源运行时证据框架相较所选URL规则和频率策略取得了更高的
召回率与F1值；框架级消融说明对象访问证据和高风险优先约束是当前实现中影响召回率的主
要机制；单机测试则验证了在线风险决策的运行可行性。上述结果共同表明，总体框架在所设
验证环境中具有可行性。
6 讨论
6.1 框架适用性与作用机制
本文围绕流量侧多源证据如何形成可执行的授权风险决策，统一定义数据对象、证据接口、
风险约束和处置流程。框架验证与消融结果表明，对象访问证据、高风险优先约束以及身份、行
为和端点上下文的联合使用共同影响风险判定结果，说明总体设计在所设实验环境中能够形成
可执行的识别与处置闭环。
该框架适用于需要增强运行时授权风险审计的Web应用和API系统。对于新建系统，可作
为RBAC或ABAC机制的补充监测层；对于存量系统，可在不大规模修改业务代码的情况下提
供独立的风险审计能力；对于多网关或多微服务场景，可在统一入口处组织跨端点上下文。框
架还可与零信任架构中的持续评估、最小权限和策略执行点协同[15]，将风险结果输出至网关或
安全运营平台，形成统一的联动处置机制。
| 在当前原型中，E | (t)采用二值对象证据表示，身份与认证上下文通过确定性一致性规则 |     |     |     |     |
| -------- | -------------------------------- | --- | --- | --- | --- |
u,r
进行评价，端点操作风险则依据请求语义和预设业务影响等级配置。因此，本文结论主要用于
说明统一证据组织、风险融合和联动处置机制的可行性。
22

6.2 有效性威胁与方法局限
本文实验存在四类主要有效性威胁。其一，样本由实验环境中的预设脚本生成且正负样本
均衡，与生产环境中授权风险事件发生率较低、业务流量呈长尾分布的情况存在差异；其二，对
比基线主要由URL规则和频率策略构成，尚未覆盖静态分析、差分测试和学习型检测等其他代
表性方法；其三，证据确认规则、风险权重和判定阈值与实验接口语义相关，迁移到其他系统
时需要结合业务特征重新标定；其四，性能数据来自单机实现，尚不能反映长周期运行和复杂
部署条件下的运行开销。因此，本文结果应理解为实验环境中的框架验证，而不能直接外推为
任意Web应用中的通用性能水平。
本文方法存在三类一般性局限。第一，流量侧分析依赖应用层内容和关键业务字段的可见
性，当加密内容不可访问或对象标识高度混淆时，证据完整性可能下降。第二，原型中的证据
规则、风险权重、判定阈值和端点配置与实验系统语义相关，迁移到其他应用时需要重新配置
和标定。第三，受控的类别平衡样本和单机实现尚不能反映生产流量中的类别不均衡、长期状
态变化和复杂部署条件。因此，仍需结合更多异构Web应用和真实网关流量，对框架的跨场景
适用性与运行稳定性进行检验。
7 结论
本文针对Web应用合法会话下的越权风险难以从流量侧识别并实时处置的问题，提出一种
基于非侵入式流量分析的总体框架。该框架以HTTP请求为在线判定单元，并利用关联后的请
求–响应事务组织和更新对象访问证据、身份与认证上下文、行为序列、网络环境及端点操作风
险信息，通过加权融合与高风险优先约束形成分级处置结果。
在实验环境中构造的类别平衡测试样本上，本文框架在所设评价指标上优于URL规则、频
率检测及二者组合基线；框架级消融验证了对象访问证据和高风险优先约束的作用；单机测试
表明当前实现能够完成在线风险决策。上述结果表明，总体机制在所设验证环境中具有可行性，
其更广泛适用性仍需结合异构Web应用和真实网关流量进一步检验。
作者贡献声明
林思齐：提出研究命题，设计总体方法框架，完成论文主要起草与最终修订；
罗宇超、邱博睿：参与系统设计与实现、实验场景构造及授权风险样本设计；
王怡然：参与实验数据整理、结果分析和图表绘制；
朱梓涵：参与相关工作梳理、论文格式整理和文献校对。
23

References / 参考文献
[1] OWASP Foundation. API1:2023 broken object level authorization[EB/OL]. 2023[2026-
07-17]. https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-aut
horization/.
[2] OWASP Foundation. Testing for insecure direct object references (WSTG-ATHZ-04)
[EB/OL]. 2020[2026-07-17]. https://owasp.org/www-project-web-security-testing-g
uide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing
_for_Insecure_Direct_Object_References.
[3] OWASP Foundation. A01:2025 broken access control[EB/OL]. 2025[2026-07-17]. https:
//owasp.org/Top10/2025/A01_2025-Broken_Access_Control/.
[4] BAU J, BURSZTEIN E, GUPTA D, et al. State of the art: automated black-box web
application vulnerability testing[C/OL]//2010 IEEE Symposium on Security and Privacy.
Piscataway, NJ: IEEE, 2010: 332-345. DOI: 10.1109/SP.2010.27.
[5] DOUPÉA,COVAM,VIGNAG. WhyJohnnycan’tpentest: ananalysisofblack-boxweb
vulnerability scanners[C/OL]//Lecture Notes in Computer Science: Vol. 6201 Detection
of Intrusions and Malware, and Vulnerability Assessment. Berlin, Heidelberg: Springer,
2010: 111-131. DOI: 10.1007/978-3-642-14215-4_7.
[6] ATLIDAKIS V, GODEFROID P, POLISHCHUK M. RESTler: stateful REST API
fuzzing[C/OL]//2019 IEEE/ACM 41st International Conference on Software Engineer-
ing (ICSE). Piscataway, NJ: IEEE, 2019: 748-758. DOI: 10.1109/ICSE.2019.00083.
[7] SANDHU R S, COYNE E J, FEINSTEIN H L, et al. Role-based access control models
[J/OL]. Computer, 1996, 29(2): 38-47. DOI: 10.1109/2.485845.
[8] HU V C, FERRAIOLO D, KUHN D R, et al. Guide to attribute based access control
(ABAC) definition and considerations: 800-162[R/OL]. Gaithersburg, MD: National In-
stitute of Standards and Technology, 2014. https://doi.org/10.6028/NIST.SP.800-162.
[9] SUN F, XU L, SU Z. Static detection of access control vulnerabilities in web applications
[C/OL]//20th USENIX Security Symposium (USENIX Security 11). San Francisco, CA:
USENIX Association, 2011. https://www.usenix.org/conference/usenix-security-11/stat
ic-detection-access-control-vulnerabilities-web-applications.
[10] ZUO C, ZHAO Q, LIN Z. AUTHSCOPE: towards automatic discovery of vulnerable au-
thorizations in online services[C/OL]//Proceedings of the 2017 ACM SIGSAC Conference
on Computer and Communications Security. New York, NY: ACM, 2017: 799-813. DOI:
10.1145/3133956.3134089.
[11] COVA M, BALZAROTTI D, FELMETSGER V, et al. Swaddler: an approach for the
anomaly-based detection of state violations in web applications[C/OL]//Lecture Notes in
Computer Science: Vol. 4637 Recent Advances in Intrusion Detection. Berlin, Heidel-
berg: Springer, 2007: 63-86. DOI: 10.1007/978-3-540-74320-0_4.
24

[12] FELMETSGER V, CAVEDON L, KRUEGEL C, et al. Toward automated detection of
logicvulnerabilitiesinwebapplications[C/OL]//Proceedingsofthe19thUSENIXSecurity
Symposium. Berkeley, CA: USENIX Association, 2010: 143-160. https://www.usenix.org
/legacy/event/sec10/tech/full_papers/Felmetsger.pdf.
[13] FIELDING R T, NOTTINGHAM M, RESCHKE J. HTTP semantics: RFC 9110[S/OL].
RFC Editor, 2022. https://www.rfc-editor.org/info/rfc9110. DOI: 10.17487/RFC9110.
[14] JONES M B, BRADLEY J, SAKIMURA N. JSON web token (JWT): RFC 7519[S/OL].
RFC Editor, 2015. https://www.rfc-editor.org/info/rfc7519. DOI: 10.17487/RFC7519.
[15] ROSE S, BORCHERT O, MITCHELL S, et al. Zero trust architecture: 800-207[R/OL].
Gaithersburg, MD: National Institute of Standards and Technology, 2020. https://doi.or
g/10.6028/NIST.SP.800-207.
25