> 원본: EvoMaster-Security_2604.00702.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.18-21 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
Enhancing REST API Fuzzing with Access Policy Violation Checks
|     |     |      |           | and | Injection |         | Attacks |            |           |
| --- | --- | ---- | --------- | --- | --------- | ------- | ------- | ---------- | --------- |
|     |     | Omur | Sahin1,2, |     | Man       | Zhang3, |         | and Andrea | Arcuri2,4 |
1Erciyes
|     |     |     |     |     |     | University, |     | Tu¨rkiye |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- |
2Kristiania
|     |     |     |       |              | University |             | College,    | Norway |     |
| --- | --- | --- | ----- | ------------ | ---------- | ----------- | ----------- | ------ | --- |
|     |     |     |       | 3Beihang     |            | University, |             | China  |     |
|     |     |     | 4Oslo | Metropolitan |            |             | University, | Norway |     |
6202 rpA 1  ]ES.sc[  1v20700.4062:viXra
Abstract
Due to their widespread use in industry, several techniques have been proposed in the literature to fuzz
RESTAPIs. ExistingfuzzersforRESTAPIshavebeenfocusingondetectingcrashes(e.g.,500HTTPserver
error status code). However, security vulnerabilities can have major drastic consequences on existing cloud
infrastructures.
In this paper, we propose a series of novel automated oracles aimed at detecting violations of access
policies in REST APIs, as well as executing traditional attacks such as SQL Injection and XSS. These novel
automated oracles can be integrated into existing fuzzers, in which, once the fuzzing session is completed,
a ‘‘security testing’’ phase is executed to verify these oracles. When a security fault is detected, as output
our technique is able to general executable test cases in different formats, like Java, Kotlin, Python and
| JavaScript | test suites. |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
EvoMaster,
Our novel techniques are integrated as an extension of a state-of-the-art open-source fuzzer
for REST APIs. Experiments are carried out on 9 artificial examples, 8 vulnerable-by-design REST APIs
with black-box testing, and 36 REST APIs from the WFD corpus with white-box testing, for a total of 52
distinct APIs. Results show that our novel oracles and their automated integration in a fuzzing process can
| lead to   | detect security | issues | in       | several   | of these | APIs. |      |     |     |
| --------- | --------------- | ------ | -------- | --------- | -------- | ----- | ---- | --- | --- |
| Keywords: | REST,           | API,   | fuzzing, | security, |          | BOLA, | BFLA |     |     |
1 Introduction
The Open Worldwide Application Security Project (OWASP) keeps track of the most common security
vulnerabilitiesinwebapplications.1 Intheir2023-reporttargetedatwebAPIs,2 themostcommonvulnerabilityis
Broken Object Level Authorization (BOLA). A similar vulnerability, called Broken Function Level Authorization
(BFLA), ranks fifth. Wrong authorization checks in the APIs can lead users to access resources they are not
supposed to access (BOLA), or do operations they do not have rights to (BFLA).
Based on the ‘‘State of API Security 2026’’ made by 42crunch,3 which is based on 200 real-world API
vulnerabilities and exploits discussed in the APISecurity.io newsletter coverage between 2024 and 2025, ‘‘the
most frequent API vulnerability across all categories in 2025 was Missing Authentication. This occurs when
an API fails to enforce authentication for sensitive operations, allowing anonymous users to access data or
| perform actions | that | should | be restricted |     | to authenticated |     | users’’.3 |     |     |
| --------------- | ---- | ------ | ------------- | --- | ---------------- | --- | --------- | --- | --- |
As of 2024, it is estimated4 that 94% of companies worldwide use cloud computing, with costs measured in
thehundredsofbillionsofeuros. Assuch,reliabilityandcorrectnessofthesesystemsisofparamountimportance
| in modern society. |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Currently, REST APIs are the most common type of APIs on the web. As testing the functionalities of
APIs can be expensive and time consuming, a lot of research has been carried out to automatically generate
test cases for them [22]. However, to deal with authorization-related faults, a fuzzer should be able to handle
the authentication of different users with different roles and access rights. Unfortunately, many fuzzers in the
literature are unable to handle authentication information during the fuzzing process [41]. For the few fuzzers
that can handle authentication of different users, they are unable to automatically detect BOLA and BFLA
related vulnerabilities.
1https://owasp.org/www-project-top-ten/
2https://owasp.org/www-project-api-security/
3https://42crunch.com/state-of-api-security-2026-report/
4https://edgedelta.com/company/blog/how-many-companies-use-cloud-computing
1

To fill this gap in the literature, in this paper we define seven novel automated oracles aimed at detecting
faults related to misconfigured authorization checks. Furthermore, as the verification of authorization checks is
only one aspect of security testing, we also integrated in our approach the evaluation of SQL Injection and XSS
attacks.
We integrated our novel oracles in a state-of-the-art fuzzer for REST APIs, namely EvoMaster [10].
Experiments on eight artificial APIs widely used in security research, as well as on 36 APIs from the WFD
corpus [41], show that our novel automated oracles can be used to automatically detect several new security
vulnerabilities that cannot be detected with other current approaches in the literature.
OurapproachisintegratedandevaluatedinEvoMaster,butanyotherstate-of-the-artfuzzerthatsupports
authentication of users (e.g., via authorization headers, or dynamic login tokens) could had been used for our
study. We chose to use EvoMaster as starting point for our implementation, as developing a robust fuzzer
from scratch is a major engineering effort [7]. We chose EvoMaster because it is among the oldest [2] and
maturefuzzerstillinactivedevelopment[10], givingamongthebestresultsinlargetoolcomparisons[29,48,43].
Although EvoMaster is focused on white-box testing, its black-box mode was able to achieve second position
in the SBFT’26 black-box fuzzer competition [11]. As it is a mature tool with extensive documentation, it is
used in several enterprises worldwide, such as Meituan in China [49, 51] and Volkswagen in Germany [39, 5].
EvoMaster has been downloaded thousands of times [10].
This paper is an extension of conference paper [6]. Compared with the conference version, we introduced six
additional novel oracles (9 vs. 3) and conducted empirical studies on a larger set of APIs (52 vs. 13). Besides the
novel security oracles presented in this paper, EvoMaster is also able to detect Server-Side Request Forgery
(SSRF) vulnerabilities [44]. However, the details of how it is done have been presented and analyzed in a
different previous publication [44], and they are not going to be discussed here.
The paper is organized as follows. Section 2 discusses related work. Our novel security oracles are presented
in Section 3. How the use of these oracles can be integrated into a fuzzer is discussed in Section 4. Section 5
shows our empirical study. Threats to validity follows in Section 6. Finally, Section 7 concludes the paper.
2 Related Work
There is a large body of research related to fuzz REST APIs [22]. Several fuzzers have been proposed in
the literature, including, in alphabetic order: APIRL [21], APIF [46], ARAT-RL[26], AutoRestTest [28],
bBOXRT [30], DeepREST [17], EvoMaster [10], LlamaRestTest [27], MINER [33], Morest [32], Nautilus [19],
ResTest[37],RestCT[47],RESTler[13],RestTestGen[45],Schemathesis[23],VoAPI2[20]andWuppieFuzz[40].
Thesefuzzersaimatachievinghighcoverage(e.g.,intermsofschemacoverageandcodecoverage),anddetecting
faults. Themostcommontypeoforacleisdetectingservererrors[34],usuallyrepresentedwitha500HTTPstatus
code [22]. Other types of oracles include checking for schema mismatches (i.e., the test API is returning data
that is not valid according to the API’s schema), and robustness properties (i.e., sending wrong data on purpose,
and then check whether the API correctly flags them as user errors). In large empirical comparisons [29, 48],
fuzzers for REST APIs are typically compared on code coverage and on the number of detected 500 status codes.
When it comes to verify security properties in REST APIs, some initial work on this topic exists. One of the
earlier approaches was in RESTler [14], in which 4 security rules were defined. These included checking the
semantics of HTTP operations (e.g., ‘‘A resource that has been deleted must no longer be accessible’’ [14]) as
wellascheckinguser-namespaceproperties(e.g.,‘‘A resource created in a user namespace must not be accessible
from another user namespace’’ [14]). However, this latter rule might be too restrictive, and not considering that
there can be complex access control policies in place where some users might have access to some resources of
other users (e.g., a typical case would be administrator users).
TheworkpresentedinNautilusaimsatdetecting‘‘vulnerabilitiescausedbyimproperuserinputhandling’’[19].
However, the presented approach is not fully automated, as it requires the testers to manually annotate the
OpenAPI schemas with extra information needed by Nautilus to detect vulnerabilities. VoAPI2 [20] does
different kinds of security attacks, including SSRF, XSS, and Command Injection testing. Different techniques
are used to identify subsets of the API operations and parameters that are more likely to be affected by these
kinds of security issues. Similarly, APIF [46] does different kinds of security attacks based on SecLists,5 like for
example XSS, SQL Injection and SSRF. However, APIF is not able to handle OpenAPI schemas, and it requires
first to capture live data via a reversed proxy.
‘‘Mass assignment’’ is one of the most common security vulnerabilities in APIs, according to OWASP’2023
report.2 This issue happens when an attacker can update object properties that they should not have access to.
The authors of RestTestGen [45] provided an extension to it to enable detection of this kind of vulnerability [18].
The work in [38] presents an LLM-based approach to generate tests aimed at Broken Object Level Authoriza-
tion (BOLA) vulnerabilities in REST APIs. However, it is unclear how the automated oracles are designed. In
5https://github.com/danielmiessler/SecLists
2

particular, ‘‘this does not represent the detection of actual BOLA vulnerabilities ...The potential for generating
tests that incorrectly identify non-existent vulnerabilities needs further investigation’’ [38].
An alternative approach to detect BOLA vulnerabilities in REST APIs has been presented in [42]. In this
approach, OpenAPI schemas are transformed into Petri nets, and then server logs are used to analyze possible
BOLA vulnerabilities. However, a limitation is that it ‘‘requires having an OpenAPI specification with links.
Unfortunately, this field is not widely used’’ [42].
Our work is significantly different from this existing literature. In our approach, we define a series of
automated oracles aimed at detecting faults related to access control. The only requirements are the presence of
an OpenAPI schema describing the API, and login information for at least two different users. Then, given a
fuzzer that generates a set of test cases maximizing different criteria (e.g., schema and code coverage), we apply
a post-processing strategy to generate new test cases designed to evaluate those automated oracles. With our
approach, no further manual effort or custom schema annotation is required. As far as we know, none of these
automated oracles presented in this paper have been proposed and evaluated in the literature so far.
Note that, in this work, we also discuss how we extended EvoMaster to do SQLi and XSS attacks. Those
are not novel, as based on existing malicious payloads from the literature,6 and they have been evaluated
already in tools such as VoAPI2 [20]. However, a clear difference here is that in our approach we are able to
generate executable test cases (e.g., in JUnit format) to enable testers/developers to verify and debug any found
vulnerability.
3 Security Oracles
In this paper, we define seven new automated oracles to detect different kinds of faults related to authorization
and access control, as well as two further oracles related to executing SQLi and XSS attacks. To detect these
faults, we need to generate test cases with specific scenario patterns, and then verify if the HTTP status codes
and body responses we get back from the tested API might reveal the presence of these faults.
To enable some of these security oracles, authentication information for at least two different users are
required by the fuzzer. Better if more (at least one per different role), especially considering different access
policies they might have (e.g., administrators). No assumption on their relative access policies is needed, and
no formal description of these policies is needed either. Such information is inferred dynamically based on
the 401 (not authenticated) and 403 (not authorized) HTTP status codes received back during the fuzzing
session. The functionalities of an API can be expressed with an OpenAPI7 schema, specifying which endpoints
(combination of URL paths and HTTP verbs) are available, and what type of data they expect as input (e.g.,
query parameters and JSON body payloads). However, OpenAPI schemas are not able to express information
about access policies.
To simplify the explanations of how our novel automated oracles work, in our examples we will provide
HTTP call sequences in the following format:
1(AUTH) VERB PATH -> CODES
Like for example a test case T could be:
k
1(A) POST /items -> 201
2(A) GET /items/42 -> 200
3(B) GET /items/42 -> 403
In parentheses we have the user (where ‘‘?’’ means it does not matter), followed by the verb (e.g., GET)
and the URL path, with then the resulting HTTP status code(s) of making this call. For simplicity, here
we are omitting any query parameters, headers and body payloads. How those are handled will be discussed
next. In this 3-step test case example T , a user A creates (status 201) a new item via a POST request, and
k
then successfully accesses it with a GET request (status 200). However, another user B fails to access the same
resource created by A (status 403) as they are not authorized.
To obtain calls on specific endpoints (e.g., POST /items) returning some specific HTTP status codes (e.g.,
201), there might be the need for the right input data in the query parameters, body payloads and headers. If
some data is not correct (e.g., according to some defined constraints), then the API most likely would return a
4xx user error status code. As such data and constraints could be arbitrarily complex, it is not necessarily the
case that a fuzzer is able to generate such HTTP calls. When evaluating our novel automated oracles, we need
to create test scenarios with specific HTTP call sequences, where each call might require to return some specific
HTTP status code. To achieve this, we use and copy valid test cases generated during the fuzzing session. If for
example a fuzzer is left running for 1-hour, and it generates n test cases T (with |T|=n) as output (based on
maximizing some coverage criteria), we use those n test cases T as our initial pool to construct our new security
i
tests.
6https://github.com/minimaxir/big-list-of-naughty-strings
7https://swagger.io/specification/
3

Assume we need a call on GET /items/id that returns a 200 status code. This might not be trivial to obtain,
if the call to generate such resource (e.g., via a POST or a PUT) requires complex input data. At the end of the
fuzzing session, we can check if in the set T there is any test case with such an HTTP call. Assume the previous
example T was generated. That would fit our needs. Nevertheless, all calls after our target call would not be
k
necessary. Those unnecessary calls can be sliced away. However, calls before the target might or might not be
needed, as they might modify the state of the API. Hence, it cannot be determined with certainty whether they
are required. In this particular case, the first call POST /items creates the resource used in our target call GET
/items/id. We can therefore make a copy C of T , and remove all calls after the target, but leave as they are
k k
all calls before. In this case, C would be:
k
1(A) POST /items -> 201
2(A) GET /items/42 -> 200
When generating security tests that identify the presence of faults, it is of paramount importance that users
are properly informed about it. EvoMaster can output test cases in different formats, including Java, Kotlin,
JavaScript and Python. When a test case identifies a security fault, we make sure that in the generated test
cases a comment is generated and added before the HTTP call triggering/showcasing the fault.
Inthefollowingsubsections,wepresentindetailthenineoraclesthataredesignedtodetectthesecurityfaults.
These include not recognized authentication (Section 3.1), existence leakage (Section 3.2), missed authorization
checks (Section3.3),anonymousmodifications (Section3.4),ignoredanonymousaccess (Section3.5),leakedstack
traces (Section 3.6), and hidden but accessible endpoints (Section 3.7), together with input-related vulnerabilities
such as SQL injection (Section 3.8) and cross-site scripting (Section 3.9). These oracles form a comprehensive
detection for API vulnerabilities, covering multiple facets of API security, from authentication and authorization
to information disclosure and input validation.
Moreover, to better explain these novel automated oracles, we will provide some examples of artificial APIs
with seeded faults, on which we show what kinds of test cases we can be automatically generated. Those are
written in Kotlin, using the popular SpringBoot framework. All these examples are open-source and also used
internally in EvoMaster as E2E tests (and so part of its code repository), run as part of its Continuous
Integration [7], to verify EvoMaster’s own correctness (e.g., it should not crash, and its generated tests should
be able to be compiled and run without issues).
Note that the code of the test cases that we will show are as generated by EvoMaster version 5.1.0, as
they are. No manual modification of any kind was done on any of these test cases for readability concerns in this
paper.
3.1 Not Recognized Authentication
Typically, if an HTTP request is made without any authentication information, and the called endpoint requires
authentication, then the API would answer with a 401 status code. If the user is authenticated, but, if they try
to access a resource that does not belong to them, then the API should return a 403 status code (authenticated
but not authorized).
If a user makes an authenticated call, but if then they receive a 401 status code (instead of for example a
403), then it is a fault. This is not a security vulnerability, but rather a usability fault. Based on the returned
401, the user might wrongly believe that their authentication info is wrong or outdated, and waste time in trying
to resolve such issue (e.g., by contacting the IT support of the API). As such, it would be best to fix this kind of
usability fault.
In a fuzzer, simply flag as fault any 401 returned status code with an authenticated user would be unwise, as
it could create many false-positives. For example, if a tester misconfigures the fuzzer, and provide a wrong user
info, or such auth info has expired, then false-positive faults could be identified on each single API endpoint.
Depending on the size of the API, this could result in hundreds of wrongly identified faults that could make
harder to highlight any found real fault.
To avoid this kind of false-positives, we designed the following strategy. First, for each endpoint X in the
OpenAPI schema, we check if the fuzzer has generated any test case T with an authenticated user (e.g., A) in
1
which a 401 was returned. If so, X is potentially faulty. We then check if authentication information for A was
correct. To do so, we check if the fuzzer has generated any test T in which A was used on an endpoint Y ≠ X
2
in which a 2xx, success status code was returned (i.e., no 401 for A). This is a first step to check the validity of
A, as Y could be an open endpoint in which no authentication check is required. To verify this, we check if in
the generated tests of the fuzzer there is any test T in which any call on Y resulted in either a 401 or 403. If so,
3
it would mean that Y requires authentication (T ), the credentials of A on Y are correct as we get a 2xx status
3
code (T ), while the call on X with A identifies a fault as a wrong 401 is returned (T ).
2 1
For each endpoint in the OpenAPI schema, if these three conditions are met, then we create a new test
K ={C ,C ,C }, where C is a copy of test T , where all unnecessary calls after the target are sliced away, as
3 2 1 i i
previously explained.
4

1/**
2* Calls:
| 3* 1 -   | (201) PUT:/api/resources/{id} |              |     |
| -------- | ----------------------------- | ------------ | --- |
| 4* 2 -   | (403) PUT:/api/resources/{id} |              |     |
| 5* 3 -   | (201) PUT:/api/resources/{id} |              |     |
| 6* 4 -   | (401) POST:/api/resources/    |              |     |
| 7* Found | 1 potential fault             | of type-code | 205 |
8*/
9@Test @Timeout(60)
10fun test_1_postOnResourcesAuthenticatedButWronglyToldNot() {
11
12 given().accept("*/*")
| 13  | .header("Authorization",                  |     | "BAR") // BAR |
| --- | ----------------------------------------- | --- | ------------- |
| 14  | .header("x-EMextraHeader123",             |     | "")           |
| 15  | .put("${baseUrlOfSut}/api/resources/721") |     |               |
| 16  | .then()                                   |     |               |
| 17  | .statusCode(201)                          |     |               |
| 18  | .assertThat()                             |     |               |
| 19  | .body(isEmptyOrNullString())              |     |               |
20
21 given().accept("*/*")
| 22  | .header("Authorization", |     | "FOO") // FOO |
| --- | ------------------------ | --- | ------------- |
.header("x-EMextraHeader123",
| 23  |                                           |     | "") |
| --- | ----------------------------------------- | --- | --- |
| 24  | .put("${baseUrlOfSut}/api/resources/721") |     |     |
| 25  | .then()                                   |     |     |
| 26  | .statusCode(403)                          |     |     |
| 27  | .assertThat()                             |     |     |
.body(isEmptyOrNullString())
28
29
30 given().accept("*/*")
| 31  | .header("Authorization",      |     | "FOO") // FOO  |
| --- | ----------------------------- | --- | -------------- |
| 32  | .header("x-EMextraHeader123", |     | "_EM_43_XYZ_") |
.put("${baseUrlOfSut}/api/resources/577")
33
| 34  | .then()                      |     |     |
| --- | ---------------------------- | --- | --- |
| 35  | .statusCode(201)             |     |     |
| 36  | .assertThat()                |     |     |
| 37  | .body(isEmptyOrNullString()) |     |     |
38
| 39 // | Fault205. Wrongly | Not Recognized | as Authenticated. |
| ----- | ----------------- | -------------- | ----------------- |
40 given().accept("*/*")
| 41  | .header("Authorization",      |     | "FOO") // FOO |
| --- | ----------------------------- | --- | ------------- |
| 42  | .header("x-EMextraHeader123", |     | "")           |
.post("${baseUrlOfSut}/api/resources/?EMextraParam123=_EM_45_XYZ_")
43
| 44  | .then()                      |     |     |
| --- | ---------------------------- | --- | --- |
| 45  | .statusCode(401)             |     |     |
| 46  | .assertThat()                |     |     |
| 47  | .body(isEmptyOrNullString()) |     |     |
48}
Figure 1: Example of generated test for an artificial API in which a not-recognized authentication fault is
correctly identified.
5

Figure 1 shows an example of generated test for an artificial API we developed to verify if our novel oracles
can identify this kind of faults. Two users are set up: FOO and BAR. According to the internal access policies of
the API, the user FOO has no rights to call POST /api/resources/. However, instead of getting a 403 response,
the last call in that test returns a wrong 401. The previous call shows that the authentication info for FOO was
correct, i.e., this detected fault is not a false-positive due to a misconfiguration of the authentication information
| provided | to the    | fuzzer. |         |     |     |     |
| -------- | --------- | ------- | ------- | --- | --- | --- |
| 3.2      | Existence |         | Leakage |     |     |     |
Assume that the fuzzing process generated at least one test case on an endpoint definition X in which a 403
status code is returned, and one test case in which a 404 is returned. The two test cases do not need to use
the same or different users to get these results. For example, we could have X being something like /data/id
where a GET call on /data/42 returns a 403 status code, and a call on /data/77 returns 404. These two calls
| could be | done | with | the same | user, or with | two different | users. |
| -------- | ---- | ---- | -------- | ------------- | ------------- | ------ |
Such scenario is problematic, as it leads to information leakage on the existence of resources. If a user has
no access to some resources (i.e., 403), they should not be able to learn which resources exist (403) and which
ones do not exist (404), as such information can be used to narrow down follow up security attacks targeted at
existing protected resources. The HTTP standards in RFC91108 acknowledge the issue and explicitly states:
‘‘An origin server that wishes to ‘‘hide’’ the current existence of a forbidden target resource MAY instead
respond with a status code of 404 (Not Found)’’. For non-authorized users, to avoid information leakage either
the APIs should always return 403 or always 404, regardless of whether the resource exists or not.
However,therearecasesinwhicha404isnotleadingtoinformationleakage. Thishappenswhentherequested
resource is a subresource that belongs to the user. Consider a new URL path Y, like for example /data/id/bar.
Considering /data/42/bar returning 403, having /data/77/bar returning 404 with an authenticated user A
does not necessarily mean a leakage. It could happen for example that a GET on /data/77 returns 200, i.e., user
A owns it and all its sub-resources like for example /data/77/bar. But what if /data/77 does not exist (404)?
Or the user A has no access to it (403)? Or A is actually no user (i.e., making a call with no authentication
information, which should had rather led to a 401)? Then, we would have an information leakage.
To test this oracle, for each GET endpoint in the OpenAPI we need to create a new test representing the
| following | scenario: |            |     |     |     |     |
| --------- | --------- | ---------- | --- | --- | --- | --- |
| 1(?) GET  | /P/X      | -> 403     |     |     |     |     |
| 2(A) GET  | /P/X      | -> 404     |     |     |     |     |
| 3(A) GET  | /P        | -> 403,404 |     |     |     |     |
Here we have two steps, with an optional third step. First, for each GET endpoint we check if we have at
least one test case (T ) returning 403 and one (T ) returning 404. If yes, we can instantiate this scenario. We
|     |     |     | 1   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- |
first make a copy of T (including all input data, like query parameters and body payloads), and slice away all
1
calls after that target GET /P/X. A test case is composed of one or more HTTP calls. As previously discussed,
calls after our target are not needed for our oracle. However, calls before the target might be required, as they
might set the state of the API (e.g., by creating the resource). For example, T could be something like:
1
| 1(B) POST | /data    |     | -> 201 |     |     |     |
| --------- | -------- | --- | ------ | --- | --- | --- |
| 2(C) GET  | /data/42 |     | -> 403 |     |     |     |
| 3(B) GET  | /data/42 |     |        |     |     |     |
-> 200
| 4(B) DELETE | /data/42 |     | -> 204     |              |     |     |
| ----------- | -------- | --- | ---------- | ------------ | --- | --- |
| Then,       | after    | the | slice, our | copy C would | be: |     |
1
| 1(B) POST | /data    |     | -> 201 |     |     |     |
| --------- | -------- | --- | ------ | --- | --- | --- |
| 2(C) GET  | /data/42 |     | -> 403 |     |     |     |
Then, we apply the same process to T : we make a copy C , where we slice all calls after the target. For
|          |        |     |        |        | 2   | 2   |
| -------- | ------ | --- | ------ | ------ | --- | --- |
| example, | assume | we  | have T | being: |     |     |
2
| 1(A) GET  | /data/77 |     | -> 404 |     |     |     |
| --------- | -------- | --- | ------ | --- | --- | --- |
| 2(A) POST | /data    |     | -> 201 |     |     |     |
Then, the copy C would be just the first call. Then, we can create a new test K by combining C and C :
2 1 2
| 1(B) POST | /data    |     | -> 201 |     |     |     |
| --------- | -------- | --- | ------ | --- | --- | --- |
| 2(C) GET  | /data/42 |     |        |     |     |     |
|           |          |     | -> 403 |     |     |     |
| 3(A) GET  | /data/77 |     | -> 404 |     |     |     |
One possible issue here is that the execution of C might have side effects on the execution of C , as it
1 2
might change the state of the API (e.g., creating new data in the database, if any). This is not a problem when
EvoMaster
executing tests in isolation, as state-of-the-art tools such as can automatically reset the state of
databases after executing each test [4]. This means that we must execute K, and verify that, for each call, we
receive the same HTTP status codes as those returned in the original T 1 and T 2 tests. If the status codes remain
| the same, | then | we have | detected | a potential | security-related | fault. |
| --------- | ---- | ------- | -------- | ----------- | ---------------- | ------ |
8https://www.rfc-editor.org/rfc/rfc9110.html
6

1/**
2* Calls:
| 3* 1 -   | (201) PUT:/api/resources/{id} |       |     |           |     |     |
| -------- | ----------------------------- | ----- | --- | --------- | --- | --- |
| 4* 2 -   | (403) GET:/api/resources/{id} |       |     |           |     |     |
| 5* 3 -   | (404) GET:/api/resources/{id} |       |     |           |     |     |
| 6* Found | 1 potential                   | fault | of  | type-code | 204 |     |
7*/
| 8@Test | @Timeout(60) |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- |
9fun test_5_getOnResourcAllowsUnauthorizedAccessToProtectedResource() {
10
given().accept("*/*")
11
| 12  | .header("Authorization",                 |     |     | "BAR") | //  | BAR |
| --- | ---------------------------------------- | --- | --- | ------ | --- | --- |
| 13  | .header("x-EMextraHeader123",            |     |     |        | "") |     |
| 14  | .put("${baseUrlOfSut}/api/resources/12") |     |     |        |     |     |
| 15  | .then()                                  |     |     |        |     |     |
| 16  | .statusCode(201)                         |     |     |        |     |     |
| 17  | .assertThat()                            |     |     |        |     |     |
| 18  | .body(isEmptyOrNullString())             |     |     |        |     |     |
19
20 given().accept("*/*")
| 21  | .header("Authorization",      |     |     | "FOO") | //  | FOO |
| --- | ----------------------------- | --- | --- | ------ | --- | --- |
| 22  | .header("x-EMextraHeader123", |     |     |        | "") |     |
.get("${baseUrlOfSut}/api/resources/12")
23
| 24  | .then()                      |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- |
| 25  | .statusCode(403)             |     |     |     |     |     |
| 26  | .assertThat()                |     |     |     |     |     |
| 27  | .body(isEmptyOrNullString()) |     |     |     |     |     |
28
| 29 // | Fault204. | Leakage | Information | Existence |     | of Protected Resource. |
| ----- | --------- | ------- | ----------- | --------- | --- | ---------------------- |
30 given().accept("*/*")
| 31  | .header("Authorization",      |     |     | "BAR") | //  | BAR |
| --- | ----------------------------- | --- | --- | ------ | --- | --- |
| 32  | .header("x-EMextraHeader123", |     |     |        | "") |     |
.get("${baseUrlOfSut}/api/resources/339")
33
| 34  | .then()                      |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- |
| 35  | .statusCode(404)             |     |     |     |     |     |
| 36  | .assertThat()                |     |     |     |     |     |
| 37  | .body(isEmptyOrNullString()) |     |     |     |     |     |
38}
Figure 2: Example of generated test for an artificial API in which a leakage information fault is correctly
identified.
However, we are not done, as we need to check if the 404 in the last call was valid, i.e., if the user owns any
ancestor resource. If there is no authenticated user doing such call (i.e., in our example if A represents no user),
then there is nothing more to check, and the fault is identified. Otherwise, given the called target endpoint, i.e.,
/data/id in this case, we check in the OpenAPI the top ancestor resource (in the URL path) that has a GET
endpoint. If there is none, then there is nothing more to check, and the fault is identified. Otherwise, we create
a new GET call on this ancestor resource using the same user authentication (e.g., A in this example). If we still
get a 404, then the fault is identified. If not, the result remains inconclusive.
Figure 2 shows an example of generated test for an artificial API we developed to verify if our novel oracles
can identify this kind of faults. Two users are set up: FOO and BAR. When FOO accesses a resource that belongs
to BAR, they get a 403 unauthorized response. However, accessing a non-existing resource on the same endpoint
| leads to a | 404, which | leads         | to information |        | leakage. |     |
| ---------- | ---------- | ------------- | -------------- | ------ | -------- | --- |
| 3.3 Missed |            | Authorization |                | Checks |          |     |
Resources should be protected from unauthorized access. For example, a user of a bank should not be able to do
transactions on the accounts belonging to other users. However, access policies could be arbitrarily complex.
Simply stating that a user should not access or manipulate resources of other users would just result in many
| false-positive | faults. |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |
The most obvious example is administrator users. A tester using a fuzzer could provide authentication
information for some basic users as well as for an administrator one. This latter would be essential for testing
endpoints that only administrators can have access to. An administrator would likely be able to access and
manipulate resources of other users (albeit possibly still with some constraints). However, there are plenty of
cases in which more complex scenarios would arise. For example, in a web application for discussion forums,
the ‘‘moderator’’ for a specific forum might not have administration rights on the whole application. However,
they might have special rights on all the messages created by other users in that forum (e.g., to delete them
if they violate the terms of access of the application). Another example is websites related to children (e.g.,
government benefits or application for kindergarten), where groups of users (e.g., guardians for a child, typically
their parents) share the same rights and resources, but cannot access the resources of other groups (i.e., other
families). While these scenarios illustrate only a few examples, similarly complex access control rules can exist
| in various | contexts. |     |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- |
7

Ideally, iftherewasaformalspecificationoftheseaccesspolicyrules, afuzzercouldusesuchspecificationsas
automated oracle, i.e., by checking if any rule is violated during the fuzzing session (e.g., getting a resource with
a 2xx whereas it was supposed to get a 403). Unfortunately, we are aware of no existing formal specification
for access policies in REST APIs which is widely used. Some languages exist, like for example XACML9
(used for example in [35]), but we have never encountered any REST API using those formal specifications for
access policies. Some languages/tools such as Open-Policy-Agent10 and Cerbos11 seem to have some degree of
popularity, but none of the open-source APIs we found, or industries we collaborate with, make use of them.
Without a formal specification telling us what are the access policies for a REST API, how can a fuzzer
identify that a resource should had not been accessed? For example, if a user A accesses resource X and they
get a 200 HTTP status code, how can a fuzzer tell that being a fault (i.e., a 403 was expected with no returned
data)? This is an instance of the more general oracle problem: given f(x)=y, how can we be sure that y is the
correct output for software f given the input x? If f crashes, then clearly we have identified a fault for input x.
But what about all other cases? The ‘‘oracle problem’’ is indeed one of the major challenges in software testing
research [16].
In our particular case, we use the following strategy to address the oracle problem. In REST APIs, there are
three distinct HTTP operators that can manipulate a specific resource: PUT (for whole updates), PATCH (for
partial updates) and DELETE (for removing the resource). Our hypothesis is that, if any two of these operations
are forbidden (i.e., 403), but the third is allowed (i.e., 2xx), then it is most likely a misconfiguration of the API.
For example, an authorization check on an endpoint could had been forgotten. This would be a major security
vulnerability, with possibly catastrophic consequences.
The intuition about this oracle is rather straightforward. Would it make any sense for a user to be forbidden
to do any modification on a resource (e.g., with PUT and PATCH), but then be allowed to just delete it from the
system with a DELETE? Likewise, would it make any sense that a user is not allowed to DELETE a resource, but
then be allowed to do any kind of changes on it that they want with a PUT or PATCH? Or could it be just that an
authorization check is wrongly missing? Among all possible APIs and different kinds of access policy rules, there
could be cases in which these scenarios could happen and be correct. As such, we cannot exclude the presence of
some false-positives when using these rules as automated oracles. Still, as they can be used to detect critical
security faults, a non-zero amount of false-positive identified faults could be tolerable in practical contexts.
Our approach works as following. For each path X and each one of the verb V such as DELETE, PUT and
PATCH, we check if it exists in the OpenAPI schema (not all defined paths might support all different HTTP
verbs, such as for example PATCH). If so, we check in the generated tests T of the fuzzer if there is any T for
k
which on that verb/path V :X we get a 403 response. If T exists, we make a copy C in which all calls after
k k
the 403 are sliced away. If not, we try to create it. This is done by first checking for a test T that creates
c
the resource at X, and then add new call with a different user executing V : X on it (due to its length and
complexity, we do not provide here full details of all the edge cases dealing with such resource creation; we
refer the interested reader to check our open-source implementation). If this latter call returns a 403, then such
instantiated test will be our C . If not, our oracle is not applicable for V :X.
k
Given C in which the last call returns a 403 with a user A on path X for verb V, we need to add a new call
k
V′ :X with same user A with a different verb V′ out of the considered three. For example, if V is DELETE, for
V′ we consider PUT and PATCH. As making a success call with V′ might require specific input data (e.g., query
parameters and body payloads), we check if in T there is any existing T satisfying all these criteria. If not, we
j
cannot apply our oracle on this path X. Otherwise, we make a copy C of T , where all calls before and after
j j
the target V′ :X are sliced away, i.e., C is composed of only a single call. Then, there are two further steps.
j
First, in C we modify the authentication information to rather use A (in case it was using a different user).
j
Second, we need to make sure that both C and C handle the same resource. For example, C could deal
k j k
with /items/42 whereas C with /items/77. We create a new test Z which is the concatenation of C and C ,
j k j
where the resource path of C is bound to be the same as in C . For example, given C being:
j k k
1(B) POST /items -> 201
2(A) DELETE /items/42 -> 403
and C being:
j
1(C) PUT /items/66 -> 200
then Z would be:
1(B) POST /items -> 201
2(A) DELETE /items/42 -> 403
3(A) PUT /items/42 -> 200
The binding is done by either modifying the variables in the path elements of the endpoint URL, or by
using the same dynamic updates used in the tests when resources are generated dynamically. For example, a
9https://groups.oasis-open.org
10https://github.com/open-policy-agent/opa
11https://github.com/cerbos/cerbos
8

1/**
2* Calls:
| 3* 1     | - (201)     | PUT:/api/forbiddendelete/resources/{id}    |          |           |     |     |
| -------- | ----------- | ------------------------------------------ | -------- | --------- | --- | --- |
| 4* 2     | - (403)     | DELETE:/api/forbiddendelete/resources/{id} |          |           |     |     |
| 5* 3     | - (204)     | PUT:/api/forbiddendelete/resources/{id}    |          |           |     |     |
| 6* Found | 1 potential |                                            | fault of | type-code | 206 |     |
7*/
| 8@Test | @Timeout(60)                                  |     |     |     |     |     |
| ------ | --------------------------------------------- | --- | --- | --- | --- | --- |
| 9fun   | test_7_putOnResourcMissedAuthorizationCheck() |     |     |     |     | {   |
10
given().accept("*/*")
11
| 12  |     | .header("Authorization",                                  |     |     | "BAR") // BAR |     |
| --- | --- | --------------------------------------------------------- | --- | --- | ------------- | --- |
| 13  |     | .header("x-EMextraHeader123",                             |     |     | "")           |     |
| 14  |     | .put("${baseUrlOfSut}/api/forbiddendelete/resources/214") |     |     |               |     |
| 15  |     | .then()                                                   |     |     |               |     |
| 16  |     | .statusCode(201)                                          |     |     |               |     |
| 17  |     | .assertThat()                                             |     |     |               |     |
| 18  |     | .body(isEmptyOrNullString())                              |     |     |               |     |
19
20 given().accept("*/*")
| 21  |     | .header("Authorization",      |     |     | "FOO") // FOO |     |
| --- | --- | ----------------------------- | --- | --- | ------------- | --- |
| 22  |     | .header("x-EMextraHeader123", |     |     | "")           |     |
.delete("${baseUrlOfSut}/api/forbiddendelete/resources/214")
23
| 24  |     | .then()                      |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- |
| 25  |     | .statusCode(403)             |     |     |     |     |
| 26  |     | .assertThat()                |     |     |     |     |
| 27  |     | .body(isEmptyOrNullString()) |     |     |     |     |
28
29 // Fault206. Allowed To Modify Resource That Likely Should Had Been Protected.
| 30  | val res_2: | ValidatableResponse           |     |     | = given().accept("*/*") |     |
| --- | ---------- | ----------------------------- | --- | --- | ----------------------- | --- |
| 31  |            | .header("Authorization",      |     |     | "FOO") // FOO           |     |
| 32  |            | .header("x-EMextraHeader123", |     |     | "")                     |     |
.put("${baseUrlOfSut}/api/forbiddendelete/resources/214")
33
| 34  |                     | .then()                      |                                    |     |     |     |
| --- | ------------------- | ---------------------------- | ---------------------------------- | --- | --- | --- |
| 35  |                     | .statusCode(204)             |                                    |     |     |     |
| 36  |                     | .assertThat()                |                                    |     |     |     |
| 37  |                     | .body(isEmptyOrNullString()) |                                    |     |     |     |
|     | val location_id__32 |                              | res_2.extract().header("location") |     |     |     |
| 38  |                     |                              | =                                  |     |     |     |
39 assertTrue(isValidURIorEmpty(location_id__32));
40}
Figure 3: Example of generated test for an artificial API in which a missed authorization check fault is correctly
identified.
resource could be created with a POST request, where the id of the newly generated resource could be dynamic
and non-deterministic. The id could be then returned in the response of the POST request, e.g., in the location
header or as a field in the body payload. Such id needs to be extracted, and then used in the following HTTP
Toachievethis,wesimplyrelyontheexistingalgorithmsinEvoMaster
callsforreferringtothesameresource.
| to bind | endpoints | on same | resources |     | [10]. |     |
| ------- | --------- | ------- | --------- | --- | ----- | --- |
Once Z is created, we execute it, and verify if the status codes are as expected, i.e., the DELETE returns a
403, followed by a PUT or PATCH on same resource with same user returning a 2xx. If this happens, then we have
| identified | a potential | security | vulnerability. |     |     |     |
| ---------- | ----------- | -------- | -------------- | --- | --- | --- |
Figure 3 shows an example of generated test for an artificial API we developed to verify if our novel oracles
can identify this kind of faults. Two users are set up: FOO and BAR. BAR creates a resource via a PUT. A different
user FOO is forbidden from deleting this resource (403 on DELETE). However, this user can completely replace the
| resource      | with | a PUT (as | it gives      | a 204). |     |     |
| ------------- | ---- | --------- | ------------- | ------- | --- | --- |
| 3.4 Anonymous |      |           | Modifications |         |     |     |
The lack of authentication checks is one of most common type of security vulnerabilities.3 However, it is not the
case that all APIs, or all of their endpoints, must be secured. A read-only API (e.g., enabling just GET requests)
might provide data without need of authentication credentials (e.g., an API for a web store, where items can be
browsed before needing to login to buy them). Simply flagging as a vulnerability a GET endpoint, that returns a
successful 2xx status code on a non-authenticated request, would just lead to false positives.
Also,itmightbepossibleforAPIstocreatenewdata(e.g.,viaaPOSTcall)withouttheneedofauthentication.
Acommonexampleiswhenregisteringanewuserinasystem,ordiscussionforumsthatallowaddinganonymous
comments. Without any other available information, it is not really possible for a fuzzer to reliable decide
| whether | GET/POST | endpoints | must | require | authentication | or not. |
| ------- | -------- | --------- | ---- | ------- | -------------- | ------- |
However, this is not the case for modification operations, such as DELETE, PUT and PATCH. If anonymous (i.e.,
non-authenticated) DELETE operations are allowed, then a user could delete all existing data, and delete data of
other users as soon as they create new entries. If anonymous PUT/PATCH operations are allowed, then as soon as
a user creates some data, immediately another user could modify them, which would likely be detrimental for
| the original | user. |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- |
9

1/**
2* Calls:
| 3* (204) | PUT:/api/resources/{id} |       |              |     |     |     |
| -------- | ----------------------- | ----- | ------------ | --- | --- | --- |
| 4* Found | 1 potential             | fault | of type-code | 901 |     |     |
5*/
| 6@Test | @Timeout(60)                                 |     |     |     |     |     |
| ------ | -------------------------------------------- | --- | --- | --- | --- | --- |
| 7fun   | test_12_putOnResourcAnonymousModifications() |     |     |     |     | {   |
8
| 9   | // Fault901. | Anonymous | Modifications. |     |     |     |
| --- | ------------ | --------- | -------------- | --- | --- | --- |
10 given().accept("*/*")
.header("x-EMextraHeader123",
| 11  |     |     |     | "") |     |     |
| --- | --- | --- | --- | --- | --- | --- |
12 .put("${baseUrlOfSut}/api/resources/196?EMextraParam123=42")
| 13  | .then()                      |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- |
| 14  | .statusCode(204)             |     |     |     |     |     |
| 15  | .assertThat()                |     |     |     |     |     |
| 16  | .body(isEmptyOrNullString()) |     |     |     |     |     |
17}
Figure4: ExampleofgeneratedtestforanartificialAPIinwhichaPUTwassuccessfulwithoutanyauthentication
info.
Of course, to delete/modify the data of other users, somehow an attacker would need to determine the ids
of those resources belonging to these other users. Depending on the complexity of those ids (e.g., incremental
counters or UUIDs), these ids could be predicted, or directly retrieved if there are GET operations on collections
| of resources | (e.g., to | GET all the | comments | in a | discussion | forum). |
| ------------ | --------- | ----------- | -------- | ---- | ---------- | ------- |
Basedontheseintuitions, wecanflagaspotentialsecurityvulnerabilitiesany DELETE,PUTorPATCHendpoint
for which we get a 2xx response without any valid authenticated user information. It might not be possible
to be 100% sure that those are indeed vulnerabilities, i.e., for some special APIs those could be false positives.
practice,3
However, considering how common the issue of missing authentication is in industrial those cases are
definitively something worth to flag as potential issues to manually verify/review.
In contrast to the other oracles discussed previously, to flag this type of Anonymous Modifications, there is
no need to create any special new test. We can simply check the tests generated during the fuzzing, and see,
for each DELETE/PUT/PATCH endpoint, if any test was created in which a 2xx response was obtained without
authentication credentials. An edge case is PUT returning a 201 (meaning resource is created). Besides doing
modifications, by HTTP specs it is possible for a PUT to create a new resource. But, in such cases, the API is
supposed to return a 201 status code. Therefore, we ignore those cases, i.e., anonymous returning a 201 are
PUT
| not flagged | as a security | vulnerability. |     |     |     |     |
| ----------- | ------------- | -------------- | --- | --- | --- | --- |
Figure 4 shows an example of generated test for an artificial API we developed to verify if our novel oracles
can identify this kind of faults. A PUT was successful without any authentication info, and without creating any
| new resource | (status          | code 204). |     |     |     |     |
| ------------ | ---------------- | ---------- | --- | --- | --- | --- |
| 3.5          | Ignore Anonymous |            |     |     |     |     |
Automatically detecting Missing Authentication might not be possible with 100% certainty, as some APIs might
have endpoints that do not require authentication (e.g., GET operation on data that is public, and not restricted
to some specific users). The use of the Anonymous Modifications oracle (recall the previous Section 3.4) would
| cover some | of the Missing | Authentication |     | cases, | but not | all. |
| ---------- | -------------- | -------------- | --- | ------ | ------- | ---- |
A complementary approach is to check cases in which an API does verify users’ credentials, but only if those
are provided. For example, assume that on an endpoint we get a 401 or 403 when making an HTTP call with
some credentials (where 401 would mean the credentials are invalid, e.g., like an expired JWT token). If it is
possible to get a 2xx on the same endpoint without any credential, then that is a clear security vulnerability.
This could happen if the API is wrongly configured to verify the validity of credentials when provided, but then
doing no authentication control if no credential is provided, i.e., the validity of anonymous requests is ignored.
To generate a test case to verify such scenario for each endpoint, we do the following. First, we check if any
test case T 1 was created with a 401 or 403 on such endpoint for any given user A. If so, we make a copy C 1 ,
where all calls after the 401/403 are sliced away. Then, we check if there was any test case T on the same
2
| endpoint | in which a | 2xx was | returned | with no | authenticated | user. |
| -------- | ---------- | ------- | -------- | ------- | ------------- | ----- |
If T exists, then we have found an Ignore Anonymous fault, which can be showcased with a new test with
2
| concatenated | C and | C , where | C is | a sliced copy | of  | T . |
| ------------ | ----- | --------- | ---- | ------------- | --- | --- |
|              | 1     | 2         | 2    |               |     | 2   |
If T 2 does not exist, we verify if any T 3 test case was generated in which the endpoint was covered with 2xx
for a given different user B. If so, we make a sliced copy C , where the credentials of B are removed. If C still
3 3
lead to get a 2xx, the fault is found, which can be shown by concatenating C and C . For example, given T as:
1 3 1
| POST        | /items    |        |     |     |     |     |
| ----------- | --------- | ------ | --- | --- | --- | --- |
| 1(?)        |           | -> 201 |     |     |     |     |
| 2(A) DELETE | /items/42 | -> 403 |     |     |     |     |
3...
10

1/**
2* Calls:
| 3* 1     | - (201) PUT:/api/resources/{id} |       |     |           |     |
| -------- | ------------------------------- | ----- | --- | --------- | --- |
| 4* 2     | - (200) GET:/api/resources/{id} |       |     |           |     |
| 5* 3     | - (403) GET:/api/resources/{id} |       |     |           |     |
| 6* 4     | - (200) GET:/api/resources/{id} |       |     |           |     |
| 7* Found | 1 potential                     | fault | of  | type-code | 900 |
8*/
| 9@Test | @Timeout(60)                         |     |     |     |     |
| ------ | ------------------------------------ | --- | --- | --- | --- |
| 10fun  | test_5_getOnResourcIgnoreAnonymous() |     |     |     | {   |
11
12 given().accept("*/*")
| 13  | .header("Authorization",                  |     |     |     | "FOO") // FOO |
| --- | ----------------------------------------- | --- | --- | --- | ------------- |
| 14  | .header("x-EMextraHeader123",             |     |     |     | "42")         |
| 15  | .put("${baseUrlOfSut}/api/resources/483") |     |     |     |               |
| 16  | .then()                                   |     |     |     |               |
| 17  | .statusCode(201)                          |     |     |     |               |
| 18  | .assertThat()                             |     |     |     |               |
| 19  | .body(isEmptyOrNullString())              |     |     |     |               |
20
21 given().accept("*/*")
| 22  | .header("Authorization", |     |     |     | "FOO") // FOO |
| --- | ------------------------ | --- | --- | --- | ------------- |
.header("x-EMextraHeader123",
| 23  |                                           |     |     |     | "42") |
| --- | ----------------------------------------- | --- | --- | --- | ----- |
| 24  | .get("${baseUrlOfSut}/api/resources/483") |     |     |     |       |
| 25  | .then()                                   |     |     |     |       |
| 26  | .statusCode(200)                          |     |     |     |       |
| 27  | .assertThat()                             |     |     |     |       |
.contentType("text/plain")
28
| 29  | .body(containsString("FOO")) |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- |
30
31 given().accept("*/*")
| 32  | .header("Authorization", |     |     |     | "BAR") // BAR |
| --- | ------------------------ | --- | --- | --- | ------------- |
.header("x-EMextraHeader123",
| 33  |                                           |     |     |     | "42") |
| --- | ----------------------------------------- | --- | --- | --- | ----- |
| 34  | .get("${baseUrlOfSut}/api/resources/483") |     |     |     |       |
| 35  | .then()                                   |     |     |     |       |
| 36  | .statusCode(403)                          |     |     |     |       |
| 37  | .assertThat()                             |     |     |     |       |
.body(isEmptyOrNullString())
38
39
40 // Fault900. A Protected Resource Is Accessible Without Providing Any Authentication.
41 given().accept("*/*")
| 42  | .header("x-EMextraHeader123", |     |     |     | "42") |
| --- | ----------------------------- | --- | --- | --- | ----- |
.get("${baseUrlOfSut}/api/resources/483")
43
| 44  | .then()                      |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- |
| 45  | .statusCode(200)             |     |     |     |     |
| 46  | .assertThat()                |     |     |     |     |
| 47  | .contentType("text/plain")   |     |     |     |     |
| 48  | .body(containsString("FOO")) |     |     |     |     |
49}
Figure 5: Example of generated test for an artificial API in which a protected resource is accessible without
| providing | authentication. |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- |
| and       | T as:           |     |     |     |     |
3
| 1(B) POST   | /items    | ->  | 201 |     |     |
| ----------- | --------- | --- | --- | --- | --- |
| 2(B) DELETE | /items/66 | ->  | 200 |     |     |
3...
| then,       | the resulting | C 1 -C | 3 would | become: |     |
| ----------- | ------------- | ------ | ------- | ------- | --- |
| 1(?) POST   | /items        | ->     | 201     |         |     |
| 2(A) DELETE | /items/42     | ->     | 403     |         |     |
| 3(B) POST   | /items        | ->     | 201     |         |     |
| DELETE      | /items/66     |        |         |         |     |
| 4(-)        |               | ->     | 200     |         |     |
Note that, simply removing the authentication credential A in T 1 to create C 3 (instead of searching for a
different test T that returned 2xx) might not work. This is because the call might require specific data (e.g., in
3
query parameters and body payloads) to avoid 400 user error responses. So that is the reason why we try to
start from a test T that has no input validation errors (i.e., returning 2xx).
3
Figure 5 shows an example of generated test for an artificial API we developed to verify if our novel oracles
can identify this kind of faults. Two users are set up: FOO and BAR. FOO creates a resource via a PUT, and it is
able to successfully retrieve it with a GET. A different user BAR is forbidden from accessing this resource (403 on
GET). However, trying to access such protected resource without any authentication info is successful (i.e., 200
on GET).
| 3.6 | Leaked Stack |     | Traces |     |     |
| --- | ------------ | --- | ------ | --- | --- |
Software faults are common. In a REST API, when an application crash due to a fault (e.g., a null-pointer
exception), then typically only the application layer of the API fails, and a 500 HTTP status code is sent back
11

1/**
2* Calls:
| 3* (500) | GET:/api/resources/null-pointer-json |     |         |             |      |     |
| -------- | ------------------------------------ | --- | ------- | ----------- | ---- | --- |
| 4* Found | 2 potential                          |     | faults. | Type-codes: | 100, | 902 |
5*/
| 6@Test | @Timeout(60) |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- |
7fun test_1_getOnNull_pointer_jsonShowsFaults_100_902() {
8
9 // Fault100. HTTP Status 500. com/foo/rest/examples/spring/openapi/v3/security/stacktrace/json/
StackTraceJSONApplication_34_nullPointerJson
| 10 // | Fault902. | Leaked | Stack | Trace. |     |     |
| ----- | --------- | ------ | ----- | ------ | --- | --- |
11 given().accept("application/json")
| 12  | .header("x-EMextraHeader123", |     |     |     |     | "") |
| --- | ----------------------------- | --- | --- | --- | --- | --- |
13 .get("${baseUrlOfSut}/api/resources/null-pointer-json?EMextraParam123=_EM_0_XYZ_")
| 14  | .then() |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
15 .statusCode(500)// com/foo/rest/examples/spring/openapi/v3/security/stacktrace/json/
StackTraceJSONApplication_34_nullPointerJson
| 16  | .assertThat()                    |     |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- |
| 17  | .contentType("application/json") |     |     |     |     |     |
18 .body("’error’.’type’", containsString("java.lang.NullPointerException"))
| 19  | .body("’error’.’message’",      |     |     |     | containsString(""))                        |              |
| --- | ------------------------------- | --- | --- | --- | ------------------------------------------ | ------------ |
| 20  | .body("’error’.’stack’.size()", |     |     |     |                                            | equalTo(56)) |
|     | .body("’error’.’stack’",        |     |     |     | hasItems("java.lang.NullPointerException", |              |
21 "\tat com.foo.rest.
examples.spring.openapi.v3.security.stacktrace.json.StackTraceJSONApplication.nullPointerJson(
StackTraceJSONApplication.kt:36)", "\tat jdk.internal.reflect.GeneratedMethodAccessor90.invoke(
Unknown Source)", "\tat java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(
DelegatingMethodAccessorImpl.java:43)", "\tat java.base/java.lang.reflect.Method.invoke(Method.java
:569)", "\tat org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(
InvocableHandlerMethod.java:197)", "\tat org.springframework.web.method.support.
InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:141)",
| 22  | ... |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Figure 6: Excerpt of a generated test for an artificial API in which an exception stack-trace is present in the
response body. Due to long stack-trace (56 lines), the test is not displayed in its entirety.
to the client (i.e., the entire HTTP server does not crash, so the TCP connection is still open and an error
| message | can be sent | back). |     |     |     |     |
| ------- | ----------- | ------ | --- | --- | --- | --- |
To help debugging the fault, the server could log the stack trace of the exception to a log file, and/or send
it back in the body payload of the HTTP 500 response. Where this latter behavior can be useful during the
development of an API (e.g., while an engineering is developing a new feature, like a new endpoint), it can be a
major security vulnerability for APIs run in production. An attacker that triggers a 500 fault (e.g., by using a
fuzzer) would be able to see such stack traces. From the stack traces they could infer the programming language
and framework used to develop the API. Such information could then be used for more targeted attacks (e.g., if
| that specific | framework |     | has known | zero-day | vulnerabilities). |     |
| ------------- | --------- | --- | --------- | -------- | ----------------- | --- |
As a rule of thumb, HTTP 500 status responses should provide no information to the clients about any
internal details of the API, as such information can be exploited by malicious actors. Developers could enable
stack traces in the responses during development, and, then, forget to disable such feature when the API is
| deployed | to production. |     | This | is a security | vulnerability. |     |
| -------- | -------------- | --- | ---- | ------------- | -------------- | --- |
To verify whether a HTTP 500 response contains stack traces, we developed a series of regular expressions
targeted at all the major programming languages (e.g., Java, Python, C#, JavaScript, Go, PHP, Ruby and
Rust). Stack traces could be returned in plain-text, or embedded in a JSON response. Both cases are handled.
As such text analyses have a non-negligible computational cost, they are not executed on each HTTP 500
response. During a 1-24 hour fuzzing campaign, hundreds of thousands of such tests could be evaluated. Once
the fuzzing session is completed, for each endpoint we check if any test was generated returning a 500. If so, the
text analysis is applied only on that test for that endpoint. Given N different endpoints in the API, these text
| analyses | are run | at most | N times | on N | different | tests. |
| -------- | ------- | ------- | ------- | ---- | --------- | ------ |
EvoMaster,
When doing fuzzing with by default the Leaked Stack Traces is activated. However, in case
of its use by developers that willingly want to have stack traces in their HTTP responses, such oracle should
be deactivated, as it would otherwise generate only false positives. EvoMaster is a highly tunable fuzzer,
documented12)
with hundreds of available (and options [7]. The use of each single oracle can be toggled via
configuration settings (command-line input arguments and/or configuration files).
Figure 6 shows an example of a test case that leads to an internal crash (HTTP status code 500), in which
the stack-trace ends up in the response body. Here, two distinct faults are found and flagged: the fact that the
API crashed (status code 500), and that a stack-trace leaked in the response.
12https://github.com/WebFuzzing/EvoMaster/blob/master/docs/options.md
12

1/**
2* Calls:
| 3* 1 -   | (200) OPTIONS:/api/resources |     |         |             |          |     |
| -------- | ---------------------------- | --- | ------- | ----------- | -------- | --- |
| 4* 2 -   | (200) GET:/api/resources     |     |         |             |          |     |
| 5* Found | 3 potential                  |     | faults. | Type-codes: | 101, 903 |     |
6*/
| 7@Test                                          | @Timeout(60) |     |     |     |     |     |
| ----------------------------------------------- | ------------ | --- | --- | --- | --- | --- |
| 8fun test_1_getOnResourcesShowsFaults_101_903() |              |     |     |     | {   |     |
9
10 // Fault101. Received A Response From API With A Structure/Data That Is Not Matching Its Schema. Type
: validation.request.operation.notAllowed OPTIONS operation not allowed on path ’/api/resources’.
11 given().accept("*/*")
.options("${baseUrlOfSut}/api/resources")
12
| 13  | .then()                      |                  |     |                          |     |     |
| --- | ---------------------------- | ---------------- | --- | ------------------------ | --- | --- |
| 14  | .statusCode(200)             |                  |     |                          |     |     |
| 15  | .assertThat()                |                  |     |                          |     |     |
| 16  | //                           | .header("Allow", |     | "HEAD,POST,GET,OPTIONS") |     |     |
| 17  | .body(isEmptyOrNullString()) |                  |     |                          |     |     |
18
19 // Fault101. Received A Response From API With A Structure/Data That Is Not Matching Its Schema. Type
: validation.request.operation.notAllowed GET operation not allowed on path ’/api/resources’.
| 20 // | Fault903. | Hidden | Accessible | Endpoint. |     |     |
| ----- | --------- | ------ | ---------- | --------- | --- | --- |
given().accept("*/*")
21
| 22  | .get("${baseUrlOfSut}/api/resources") |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- |
| 23  | .then()                               |     |     |     |     |     |
| 24  | .statusCode(200)                      |     |     |     |     |     |
| 25  | .assertThat()                         |     |     |     |     |     |
.contentType("text/plain")
26
| 27  | .body(containsString("OK")) |     |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- |
28}
Figure 7: Example of generated test for an artificial API in which first a call is made via OPTIONS to determine
which methods are allowed, followed by a successful call to a GET that is not defined in the schema.
| 3.7 Hidden |     | Accessible |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- |
An OpenAPI schema defines what the API can provide. What if the API has working endpoints that are not
declared in the schema? This could be a bug in the schema itself, i.e., the designers/developers of the API forgot
to specify the endpoint. This can be the case when schemas are written manually (and not automatically derived
from the source code of the API, e.g., using libraries such as SpringDoc for SpringBoot applications). Although
| this is not | a security | issue, | it is | still a usability | fault that requires | fixing. |
| ----------- | ---------- | ------ | ----- | ----------------- | ------------------- | ------- |
However, it might also be that those endpoints are not supposed to be accessible. They could be used just
for debugging/testing, or being work-in-progress. Having those endpoints accessible in production by users could
become a security risk. If an endpoint is ‘‘hidden’’ (i.e., not declared in the schema), but it is still ‘‘accessible’’
when clients call it directly, we have a problem (either a usability or a security one).
If a client makes a call to an endpoint for a resource that exists, but the ‘‘verb’’ used is not supported for it,
then the server should return either a HTTP 405 status code (Method Not Allowed) or a 501 (Not Implemented).
To limit disclosing information for security reasons, the server might even decide to return a 403 in those cases
instead. If a call is made to an endpoint that is not declared in the schema, but the response contains a status
| different | from 403, | 405 | and 501, | then there | is a problem. |     |
| --------- | --------- | --- | -------- | ---------- | ------------- | --- |
To check these properties, we use the following approach. For each distinct resource path declared in the
schema, we do make a OPTIONS HTTP call. This will provide information about the available verbs for that
path, returned in the Allow HTTP header. We then check if there is any allowed verb not declared in the
schema (excluding OPTIONS itself and HEAD). If so, for each of those hidden verbs, we make a call with it on that
resource path, with no body payloads and no query parameters (as there is no info about them in the schema).
If we obtain a result different than a 403, 405 or 501, we flag it as an error. To reproduce this problem, we
instantiate a new test case with the OPTIONS call, followed by the call with the hidden verb.
Technically, the call with OPTIONS might be redundant. One could simply directly call all endpoints with
verbs not declared in the schema, and see what is returned as status code. The use of OPTIONS just makes the
| tests more | clear, | better | highlighting | the | severity of the issue. |     |
| ---------- | ------ | ------ | ------------ | --- | ---------------------- | --- |
Figure 7 shows an example of test in which first an OPTIONS call is made on a path resource. Based on the
Allow header in the response, considering that no GET is declared in the schema (not shown), a follow up call
with a GET is done. As this is successful, such call is marked as a potential security vulnerability (besides being
| as well a | violated  | schema | fault). |     |     |     |
| --------- | --------- | ------ | ------- | --- | --- | --- |
| 3.8 SQL   | Injection |        |         |     |     |     |
In 2025, Injection is still one of the most common security vulnerability in web applications,1 although its
prevalent.2
presence in APIs is less In the research literature, there is a large body of knowledge regarding how
13

to automatically detect injection vulnerabilities such as SQL Injection (e.g., [25, 1, 15, 31]), including work on
REST APIs [20].
In our work, we do not only try to detect security vulnerabilities, but we also aim at being able to generate
executable test cases to enable engineers to effectively debug such faults. In our approach, for each endpoint,
we check if any test case T was generated in which a successful 2xx response was obtained. Responses that
i
end up with user errors (i.e., 4xx) or server errors (5xx) might be less likely to involve database interactions.
Then, for each input variable that is a string (e.g., in query parameters and fields in body payloads), we append
a malicious SQL injection payload. This is as long as such extended string is still valid for any constraints
expressed in the OpenAPI schema (e.g., length, enum and pattern constraints, if any is defined), as otherwise
the API will just return a 400 status code without executing any business logic.
We need to make sure that we can automatically detect if a SQL Injection attack is successful, also when
dealing with black-box testing where no direct access to the database is possible. For this case, we focus on
sleep payloads, like for example ’ OR SLEEP(5)-- -. Given N endpoints and P different malicious payloads to
evaluate (with P =16 in our case), at most N×P new test cases need to be evaluated. In the case of white-box
testing, in which we can detect if the API is using any SQL database, if no database is used, then the evaluation
of this SQL Injection oracle is automatically skipped.
If the injection of a sleep of S seconds is successful, then the test case should take at least S seconds longer to
run. However, execution time of a test case for a REST API is non-deterministic, as it depends on many factors
such as network load, and OS CPU schedule. Even when re-executing the same test twice, a certain amount of
time variability is expected. The injected sleep time should be long enough to minimize risks of this source of
variability, but not too long to make the testing unpractical. Ideally, HTTP calls to an API should just take
few tens or hundreds of milliseconds. In those cases, a sleep of few seconds would unlikely to be affected by
noise. But, if for any reason the execution time of HTTP calls for some endpoints are expected to be taking
seconds, then such time variability might have negative effects. To handle this, we exclude from our analysis
any HTTP call that is taking longer than M seconds (e.g., M =2).
To create test cases to find and showcase SQL Injection vulnerabilities, we do as follow. For each endpoint,
we check if any test case T was created where an HTTP call returned a 2xx and lasted less than M seconds. If
1
any is found, we make a copy C in which any call after the target (let’s call it X) is sliced away. Then, we
1
make a copy of the target HTTP call (let’s call this copy Y), in which we inject malicious payloads, and append
it to C . If the target HTTP call X required the ids of dynamically generated resources in the test, we need to
1
make sure the appended copied call Y refers to the same dynamic ids. For example, given T for the endpoint
1
GET /items/{id}:
1(?) POST /items -> 201
2(?) GET /items/42 -> 200
3...
then the resulting C would be:
1
1(?) POST /items -> 201
2(?) GET /items/42 -> 200
3(?) GET /items/42 -> 200
When evaluating C , if X takes less than M = 2 seconds, and Y takes more than S = 5 seconds, then
1
we have detected and can reproduced the SQL Injection vulnerability. Note, to be able to properly convey
this information to the final users (e.g., developers and testers), our output test suites are enhanced with time
tracking of the HTTP execution times, with assertions based on the values M and S.
Figure 8 shows an example of a test case with two HTTP calls. The first call is executed, and we make
sure to verify it takes less than 2 seconds. The second call is a copy of the first, but with some SQL Injection
payloads. Here, we verify the call takes more than 5 seconds.
3.9 Cross Site Scripting (XSS)
Cross-Site Scripting (XSS) is a widespread type of security vulnerability where attackers could inject malicious
client-side scripts (usually JavaScript) into the frontend of web applications. As it is a common vulnerability in
web applications, a significant body of research has been dedicated to analyze and design techniques to identify
it and prevent it [24]. For example, a payload like <img src=x onerror=alert(’XSS’)> would execute an
alert command if displayed directly in the HTML of a web page without escaping first the opening/closing tag
characters.
In the case of REST APIs, there is no web frontend, though. As such, the API itself is no subject to XSS
vulnerabilities. However, the API ‘‘might’’ store malicious XSS payloads that, if later retrieved by a faulty web
frontend application, they ‘‘might’’ result in XSS exploits if not escaped. As such, Stored XSS payloads are a
potential threat, if malicious payloads are saved as they are without any input sanitization. This could happen
with operations like POST, PUT and PATCH.
14

1/**
2* Calls:
| 3*  | 1 - (200) | POST:/api/sqli/body/vulnerable |          |           |     |     |
| --- | --------- | ------------------------------ | -------- | --------- | --- | --- |
| 4*  | 2 - (200) | POST:/api/sqli/body/vulnerable |          |           |     |     |
| 5*  | Found     | 1 potential                    | fault of | type-code | 200 |     |
6*/
7@Test @Timeout(60)
8fun test_3_postOnVulnerableVulnerableToSQLInjection()
{
9
10
| 11  | // res_0_ms | stores                                | the | start time | in milliseconds |     |
| --- | ----------- | ------------------------------------- | --- | ---------- | --------------- | --- |
| 12  | val         | res_0_ms = System.currentTimeMillis() |     |            |                 |     |
13
14 given().accept("*/*")
| 15  |     | .header("x-EMextraHeader123",    |       |                   |     | "") |
| --- | --- | -------------------------------- | ----- | ----------------- | --- | --- |
| 16  |     | .contentType("application/json") |       |                   |     |     |
| 17  |     | .body("                          | { " + |                   |     |     |
| 18  |     | " \"password\":                  |       | \"_EM_110_XYZ_\", |     | " + |
| 19  |     | " \"username\":                  |       | \"_EM_111_XYZ_\"  |     | " + |
| 20  |     | " }                              | ")    |                   |     |     |
21 .post("${baseUrlOfSut}/api/sqli/body/vulnerable?EMextraParam123=_EM_112_XYZ_")
| 22  |     | .then()                        |     |     |     |      |
| --- | --- | ------------------------------ | --- | --- | --- | ---- |
| 23  |     | .statusCode(200)               |     |     |     |      |
| 24  |     | .assertThat()                  |     |     |     |      |
| 25  |     | .contentType("text/plain")     |     |     |     |      |
| 26  |     | .body(containsString("MATCHED: |     |     |     | 0")) |
27
| 28  | // res_2_ms | stores                                | the | total execution |     | time in milliseconds |
| --- | ----------- | ------------------------------------- | --- | --------------- | --- | -------------------- |
| 29  | val         | res_2_ms = System.currentTimeMillis() |     |                 |     | - res_0_ms           |
30
31 // Note: No SQL Injection vulnerability detected in this call. Expected response time (
|     | sqliBaselineMaxResponseTimeMs) |     |         |     | should | be less than 2000 ms. |
| --- | ------------------------------ | --- | ------- | --- | ------ | --------------------- |
| 32  | assertTrue(res_2_ms            |     | < 2000) |     |        |                       |
33
34
| 35  | // res_3_ms | stores                                | the | start time | in milliseconds |     |
| --- | ----------- | ------------------------------------- | --- | ---------- | --------------- | --- |
| 36  | val         | res_3_ms = System.currentTimeMillis() |     |            |                 |     |
37
| 38  | // Fault200. | SQL | Injection | (SQLi). |     |     |
| --- | ------------ | --- | --------- | ------- | --- | --- |
given().accept("*/*")
39
| 40  |     | .header("x-EMextraHeader123",    |       |     |     | "") |
| --- | --- | -------------------------------- | ----- | --- | --- | --- |
| 41  |     | .contentType("application/json") |       |     |     |     |
| 42  |     | .body("                          | { " + |     |     |     |
43 " \"password\": \"_EM_2_XYZ_\u0027 OR SLEEP(5.00)-- -\", " +
44 " \"username\": \"_EM_3_XYZ_\u0027 OR SLEEP(5.00)-- -\" " +
| 45  |     | " } | ")  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
.post("${baseUrlOfSut}/api/sqli/body/vulnerable?EMextraParam123=_EM_4_XYZ_%27+OR+SLEEP
46
%285.00%29--+-")
| 47  |     | .then() |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- |
.statusCode(200)
48
| 49  |     | .assertThat()                  |     |     |     |      |
| --- | --- | ------------------------------ | --- | --- | --- | ---- |
| 50  |     | .contentType("text/plain")     |     |     |     |      |
| 51  |     | .body(containsString("MATCHED: |     |     |     | 0")) |
52
| 53  | // res_5_ms | stores                                | the | total execution |     | time in milliseconds |
| --- | ----------- | ------------------------------------- | --- | --------------- | --- | -------------------- |
| 54  | val         | res_5_ms = System.currentTimeMillis() |     |                 |     | - res_3_ms           |
55
56 // Note: SQL Injection vulnerability detected in this call. Expected response time (
|     | sqliInjectedSleepDurationMs) |     |         | should | be  | greater than 5000 ms. |
| --- | ---------------------------- | --- | ------- | ------ | --- | --------------------- |
| 57  | assertTrue(res_5_ms          |     | > 5000) |        |     |                       |
58}
Figure 8: Example of generated test for an artificial API in which a SQL Injection vulnerability is detected.
15

1/**
2* Calls:
| 3* 1 -   | (200) POST:/api/stored/json/guestbook |       |     |           |     |     |     |
| -------- | ------------------------------------- | ----- | --- | --------- | --- | --- | --- |
| 4* 2 -   | (200) GET:/api/stored/json/guestbook  |       |     |           |     |     |     |
| 5* Found | 1 potential                           | fault | of  | type-code | 201 |     |     |
6*/
| 7@Test                                      | @Timeout(60) |     |     |     |     |     |     |
| ------------------------------------------- | ------------ | --- | --- | --- | --- | --- | --- |
| 8fun test_3_getOnGuestbookVulnerableToXSS() |              |     |     |     |     | {   |     |
9
10 given().accept("application/json")
.header("x-EMextraHeader123",
| 11  |                                                    |     |     |     | "<img | src=x onerror=alert(’XSS’)>") |     |
| --- | -------------------------------------------------- | --- | --- | --- | ----- | ----------------------------- | --- |
| 12  | .post("${baseUrlOfSut}/api/stored/json/guestbook?" |     |     |     |       |                               | +   |
13 "name=%3Cimg+src%3Dx+onerror%3Dalert%28%27XSS%27%29%3E&" +
14 "entry=%3Cimg+src%3Dx+onerror%3Dalert%28%27XSS%27%29%3E&" +
15 "EMextraParam123=%3Cimg+src%3Dx+onerror%3Dalert%28%27XSS%27%29%3E")
| 16  | .then()                          |     |     |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| 17  | .statusCode(200)                 |     |     |     |     |     |     |
| 18  | .assertThat()                    |     |     |     |     |     |     |
| 19  | .contentType("application/json") |     |     |     |     |     |     |
20 .body("’message’", containsString("Guestbook Entry Stored! Thank you for signing our
guestbook!"))
| 21  | .body("’success’", |     |     | equalTo(true)) |     |     |     |
| --- | ------------------ | --- | --- | -------------- | --- | --- | --- |
22
| 23 // | Fault201. | Cross-Site |     | Scripting | (XSS). |     |     |
| ----- | --------- | ---------- | --- | --------- | ------ | --- | --- |
24 given().accept("application/json")
25 .header("x-EMextraHeader123", "<img src=x onerror=alert(’XSS’)>")
26 .get("${baseUrlOfSut}/api/stored/json/guestbook?EMextraParam123=%3Cimg+src%3Dx+onerror%3
Dalert%28%27XSS%27%29%3E")
| 27  | .then()                          |     |     |     |             |     |     |
| --- | -------------------------------- | --- | --- | --- | ----------- | --- | --- |
| 28  | .statusCode(200)                 |     |     |     |             |     |     |
| 29  | .assertThat()                    |     |     |     |             |     |     |
| 30  | .contentType("application/json") |     |     |     |             |     |     |
|     | .body("’entries’.size()",        |     |     |     | equalTo(1)) |     |     |
31
32 .body("’entries’[0].’name’", containsString("<img src=x onerror=alert(’XSS’)>"))
33 .body("’entries’[0].’entry’", containsString("<img src=x onerror=alert(’XSS’)>"))
34}
Figure 9: Example of generated test for an artificial API in which a stored XSS potential vulnerability is
detected.
Besides storing malicious XSS payloads, Reflected XSS are problematic as well. A GET request with a
malicious payload would be dangerous if the payload is returned as part of the response, and if the response is
displayed without sanitization. A typical example of this problem is in search web forms where the searched
query is displayed with its results. Triggering a malicious search could be as easy as clicking on a compromised
| link, if the | searched | query | is passed | by  | URL query | parameters. |     |
| ------------ | -------- | ----- | --------- | --- | --------- | ----------- | --- |
TocreatetestcasestoflagpotentialXSSvulnerabilities, wedoasfollow,usingasimilarapproachasdonefor
SQL Injection handling. Foreachendpoint,wecheckifanytestcaseT 1 wascreatedreturninga2xx. Wemakea
copy C where we slice away any call after the target endpoint. Given P different XSS payloads, we apply them
1
to each string input, i.e., we replace any string value (e.g., in query parameters and body payloads), but only as
long as the OpenAPI constraints are satisfied (e.g., on string length, enumeration and pattern constraints). If
the execution of this new test C still returns an HTTP 2xx, and the malicious payload is present in the body
1
payload of this response as it is (i.e., with no sanitization), then we have detected a potential Reflected XSS.
For the case of Stored XSS, this approach might not be enough, as the results of POST, PUT and PATCH
might, or might not, return any data in the body payload of their responses (e.g., a POST could return a
representation of the created resource, including a dynamically generated id on the server-side, but that is not a
requirement). Furthermore, even if data is returned, it does not mean that such data was actually stored in the
backend system of the API. To handle these cases, we need to append to C 1 a GET request on the same resource
manipulated/created by the POST, PUT and PATCH. In this GET call, we apply the same P payloads, and verify if
its execution lead to see back the any of this payload as they are, without any input sanitization.
Given N endpoints, at most N ×P new test cases are generated and evaluated to verify the presence of
| potential | XSS vulnerabilities. |     |     |     |     |     |     |
| --------- | -------------------- | --- | --- | --- | --- | --- | --- |
Figure 9 shows an example of generated test case in which a resource is created with a POST, where some
XSS payloads are passed as query parameters. This call is followed by a GET on the same resource, in which we
| verify that | the XSS | payload     | appears | in  | the response’s | body. |     |
| ----------- | ------- | ----------- | ------- | --- | -------------- | ----- | --- |
| 4 Fuzzer    |         | Integration |         |     |                |       |     |
To use our novel oracles, we need to create specific scenarios, and then verify if any fault is detected based
on the HTTP status codes and body responses we receive back from the tested API. To check and verify
authentication and authorization properties, we need to be able to generate test cases that can exercise all the
16

different functionalities of the API. Input data can have complex constraints (e.g., in query parameters and
body payloads), and so test cases that trivially return 400 user errors would not be helpful for our goals.
The integration of our approach into existing fuzzers is as follows. We apply our security validation as
a post-processing phase. We let a fuzzer run for the amount of time specified by the users. In academic
experiments, this is typically 1 hour [22]. Within 1-hour, a fuzzer could evaluate hundreds of thousands of
HTTP calls. However, most likely no human test engineer would be interested in analyzing and using test suites
with hundreds of thousands of test cases [5]. It is simply not feasible. As such, fuzzers typically provide as
output a minimized test suite, aimed at maximizing different criteria. These could be about covering different
black-box aspects of the API [36] (e.g., based on the OpenAPI schema, like covering different HTTP status
codes for each defined endpoint), or code coverage metrics in white-box testing [3].
After the fuzzing session is over, the fuzzer would have generated a set T of test cases. These tests are then
used as a base to create new test scenarios, as previously described in Section 3. As such, how these T tests are
created is not so important, and any state-of-the-art fuzzer could be used, as long as it can generate tests using
authentication information. Furthermore, technically there would not even be the need of a fuzzer, as existing
manually written tests (if any) could be used as starting point T. The technical challenge there would then be
how to effectively carve those tests to enable their manipulation and modifications for generating new test cases.
For our experiments, we used EvoMaster, as it fits those constraints. However, one limitation is that it
wasnotgoodatgeneratingtestsinwhich403unauthorizedaccessesweredetected. Givenasetofauthentication
EvoMaster
information as input to the fuzzer (besides a copy of the OpenAPI schema for the tested API),
can generate tests with and without authentication information. However, calls with different users on the same
resources (which could lead to 403 errors) were not handled. As such, we needed to make sure to try to create
such kind of tests before applying our novel oracles, as some of those rely on existing tests with 403 responses to
| create the | needed test scenarios. |     |     |     |
| ---------- | ---------------------- | --- | --- | --- |
For each verb/path V : X in the OpenAPI schema, we check if we have any test case generated in T in
which such a call returns a 403 (unauthorized). If not, we try to create a new test for it and add it to T. If
there is no call in T with a 401 (not authenticated), then most likely there is no authentication mechanism on
that endpoint, and it can be skipped. Otherwise, we then check if there is any test T for which a successful 2xx
a
response is obtained with any authenticated user A. If so, we make a copy C in which all calls after the target
a
are sliced away. Then, for each other defined user B, we create a copy C b of C a , and we duplicate the last call
| in C by   | replacing A with | B. For example, | if we have | C being: |
| --------- | ---------------- | --------------- | ---------- | -------- |
| b         |                  |                 |            | a        |
| 1(A) POST | /data -> 201     |                 |            |          |
| 2(A) GET  | /data/42 -> 200  |                 |            |          |
| then C    | would be:        |                 |            |          |
b
| 1(A) POST | /data -> 201    |     |     |     |
| --------- | --------------- | --- | --- | --- |
| 2(A) GET  | /data/42 -> 200 |     |     |     |
| 3(B) GET  | /data/42        |     |     |     |
-> 403
If executing C b returns a 403 from the last call, then we are done for V : X, and C b can be added to T.
Otherwise, we repeat this process for the other users (if there is more than two) and for any other tests T that
a
| meet those | criteria. |     |     |     |
| ---------- | --------- | --- | --- | --- |
The number of new test cases we generate to evaluate security properties in our post-processing phase is
linearly dependent on the number of endpoints N in the tested API, i.e., its complexity is O(N). Typically,
these are at most a few hundreds. As such, creating and evaluating these security tests takes just a few seconds
or minutes, depending on the tested API. In the context of fuzzing an API for hours (e.g., between 1 and 24
hours), in most cases the overhead of our novel techniques is practically negligible, as we will show in our
| empirical   | study in Section | 5.6. |     |     |
| ----------- | ---------------- | ---- | --- | --- |
| 5 Empirical | Study            |      |     |     |
In this paper, we carried out an empirical study aimed at answering the following research questions:
RQ1: Are our novel techniques able to identify injected faults in artificial examples?
RQ2: Are our novel techniques able to identify faults in example APIs used in the security literature?
| RQ3: What | security faults | can be found    | in existing real-world | APIs?    |
| --------- | --------------- | --------------- | ---------------------- | -------- |
| RQ4: What | is the overhead | cost of running | our novel              | oracles? |
17

Table 1: Statistics of the employed REST APIs in our empirical study for black-box testing, including number of
source files, numbers of lines of code (LOCs), the number of HTTP endpoints, and their identifier on GitHub.
| SUT     |     | #SourceFiles |     | #LOCs  | #Endpoints |     | GitHub            |
| ------- | --- | ------------ | --- | ------ | ---------- | --- | ----------------- |
| capital |     |              | 103 |        | 4481       | 21  | Checkmarx/capital |
| crapi   |     |              | 564 | 129026 |            | 44  | OWASP/crAPI       |
damn-vulnerable-rest 75 4470 21 theowni/Damn-Vulnerable-RESTaurant-API-Game
| dvapi     |     |     | 13  |     | 1211 | 16  | payatu/DVAPI             |
| --------- | --- | --- | --- | --- | ---- | --- | ------------------------ |
| dvws-node |     |     | 27  |     | 3083 | 31  | snoopysecurity/dvws-node |
| vampi     |     |     | 11  |     | 520  | 14  | erev0s/VAmPI             |
vulnerable-rest-api 30 837 19 bnematzadeh/vulnerable-rest-api
| webgoat |           |     | 401  | 25972  |     | 201 | WebGoat/WebGoat |
| ------- | --------- | --- | ---- | ------ | --- | --- | --------------- |
| Total 8 |           |     | 1224 | 169600 |     | 367 |                 |
| 5.1 API | Selection |     |      |        |     |     |                 |
To answer RQ1, we created nine small APIs, using Kotlin and SpringBoot. In each one, we injected a security
fault for each of our seven novel oracles and the two injection cases. These APIs are simple, with no complex
input constraints, or code execution flow depending on database state. Faults might not be detected if the code
in which they reside is never executed due to the complexity of generating the right data. Our goal here in RQ1
is to study the feasibility of our novel techniques without confounding factors.
For reason of space, we do not provide here full code of these nine example APIs. They are provided
open-source with our extension to EvoMaster. The examples shown in Section 3 were based on these artificial
| APIs, like | the generated | tests | shown | in Figures | 1 -- | 9.  |     |
| ---------- | ------------- | ----- | ----- | ---------- | ---- | --- | --- |
To answer RQ2, we looked at the security research literature for existing APIs used for demonstrating
different types of security vulnerabilities. After a search in popular resources such as OWASP, we selected
eight widely used open-source APIs. Table 1 shows some statistics on these eight APIs, including links to their
repository on GitHub. All these APIs are run through Docker Compose, where all of their dependencies are
started as well (e.g., databases). Note that crapi is a microservice running different services. All are run in our
| experiments. | We fuzz | the | whole application |     | through | its API | Gateway. |
| ------------ | ------- | --- | ----------------- | --- | ------- | ------- | -------- |
Note that these APIs are deliberately vulnerable, with several different types of injected security faults. All
these APIs require authentication information (e.g., valid usernames/passwords for some existing users). When
the applications start, such info is set in their databases. Authentication information for the fuzzer is provided
| in YAML | files, using | the Web | Fuzzing | Commons | (WFC) | format | [41]. |
| ------- | ------------ | ------- | ------- | ------- | ----- | ------ | ----- |
ToanswerRQ3,weselectedanexistingcorpusofRESTAPIsusedinseveralstudiesinAPIfuzzingresearch,
called WFD [41], formerly known as EMB [8], which has been available open-source and extended throughout
the years since 2017. We selected all APIs in its most recent version.13 Table 2 shows some statistics on these
36 APIs. WFD is a variegated corpus, including small example APIs, as well as large real-world APIs (e.g.,
coming from public administrations from different countries such as Germany, Norway, Thailand and the United
Kingdom). For the APIs that need it, authentication information in WFD is provided in YAML files, using the
| WFC format | [41], like | for | the experiments |     | for RQ2. |     |     |
| ---------- | ---------- | --- | --------------- | --- | -------- | --- | --- |
Note that security faults can be found only if they are present. Access policy violations cannot be found if an
API has no authentication mechanism. Likewise, no SQL Injection can be found if the API does not use any
SQL database. We have not injected any artificial fault in any of these APIs. In our experiments, these 36 APIs
| are used | as they are. |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- |
To answer RQ4, we use the data from the experiments for RQ3, where we measure the execution time of
| our security | testing | phase | after the | fuzzing | phase. |     |     |
| ------------ | ------- | ----- | --------- | ------- | ------ | --- | --- |
In total, for our experiments in this paper we used 9+8+36−1=52 distinct APIs, for a total of more
than 800 thousand lines of code (for business logic, not including third-party libraries), and more than 1600
endpoints. Notethatwebgoat isusedtwice, bothforRQ2andRQ3. TheAPIwebgoat isadeliberatelyinsecure
application, built and maintained by OWASP. As such, it is part of RQ2. However, as it is written in Java, it
was added to WFD in the past. Therefore, we run it as well in RQ3. Note that, as discussed in the next section,
experiments for RQ2 and RQ3 are run differently (i.e., black-box vs. white-box testing). As such, reusing a
| single API      | twice should | not   | be problematic. |     |     |     |     |
| --------------- | ------------ | ----- | --------------- | --- | --- | --- | --- |
| 5.2 Experiments |              | Setup |                 |     |     |     |     |
The 9 artificial examples used for answering RQ1 are small and simple. As such, experiments were run with our
EvoMaster
extension of for just 1 minute, 10 times, for a total of 90 minutes.
13https://github.com/WebFuzzing/Dataset
18

Table 2: Statistics of the employed 36 REST APIs in our empirical study for white-box testing, including
number of source files, numbers of lines of code (LOCs), the number of HTTP endpoints, whether they require
| authentication,    | and the | databases    | they | use (if any).    |     |      |     |     |           |
| ------------------ | ------- | ------------ | ---- | ---------------- | --- | ---- | --- | --- | --------- |
| SUT                |         | #SourceFiles |      | #LOCs #Endpoints |     | Auth |     |     | Databases |
| bibliothek         |         |              | 33   | 2176             |     | 8    |     |     | MongoDB   |
| blogapi            |         |              | 89   | 4787             | 52  | ✓    |     |     | MySQL     |
| catwatch           |         |              | 106  | 9636             | 14  |      |     |     | H2        |
| cwa-verification   |         |              | 47   | 3955             |     | 5    |     |     | H2        |
| erc20-rest-service |         |              |      | 7 1378           | 13  |      |     |     |           |
✓
| familie-ba-sak    |     |     | 1089 | 143556 | 183 |     |     |     | PostgreSQL |
| ----------------- | --- | --- | ---- | ------ | --- | --- | --- | --- | ---------- |
| features-service  |     |     | 39   | 2275   | 18  |     |     |     | H2         |
| genome-nexus      |     |     | 405  | 30004  | 23  |     |     |     | MongoDB    |
| gestaohospital    |     |     | 33   | 3506   | 20  |     |     |     | MongoDB    |
| http-patch-spring |     |     | 30   | 1450   |     | 6   |     |     |            |
| languagetool      |     |     | 1385 | 174781 |     | 2   |     |     |            |
✓
| market            |     |     | 124 | 9861  | 13  |     |     |            | H2      |
| ----------------- | --- | --- | --- | ----- | --- | --- | --- | ---------- | ------- |
| microcks          |     |     | 471 | 66186 | 88  | ✓   |     |            | MongoDB |
| ocvn              |     |     | 526 | 45521 | 258 | ✓   |     | H2;MongoDB |         |
| ohsome-api        |     |     | 87  | 14166 | 134 |     |     |            | OSHDB   |
| pay-publicapi     |     |     | 377 | 34576 | 10  | ✓   |     |            | Redis   |
| person-controller |     |     | 16  | 1112  | 12  |     |     |            | MongoDB |
| proxyprint        |     |     | 73  | 8338  | 74  | ✓   |     |            | H2      |
✓
| quartz-manager       |     |     | 129 | 5068  | 11  |     |                             |     |            |
| -------------------- | --- | --- | --- | ----- | --- | --- | --------------------------- | --- | ---------- |
| reservations-api     |     |     | 39  | 1853  |     | 7 ✓ |                             |     | MongoDB    |
| rest-ncs             |     |     |     | 9 605 |     | 6   |                             |     |            |
| rest-news            |     |     | 11  | 857   |     | 7   |                             |     | H2         |
| rest-scs             |     |     | 13  | 862   | 11  |     |                             |     |            |
| restcountries        |     |     | 24  | 1977  | 22  |     |                             |     |            |
| scout-api            |     |     | 93  | 9736  | 49  | ✓   |                             |     | H2         |
| session-service      |     |     | 15  | 1471  |     | 8   |                             |     | MongoDB    |
| spring-actuator-demo |     |     |     | 5 117 |     | 2 ✓ |                             |     |            |
| spring-batch-rest    |     |     | 65  | 3668  |     | 5   |                             |     |            |
| spring-ecommerce     |     |     | 58  | 2223  | 26  | ✓   | MongoDB;Redis;Elasticsearch |     |            |
| spring-rest-example  |     |     | 32  | 1426  |     | 9   |                             |     | MySQL      |
| swagger-petstore     |     |     | 23  | 1631  | 19  |     |                             |     |            |
| tiltaksgjennomforing |     |     | 472 | 27316 | 79  | ✓   |                             |     | PostgreSQL |
✓
| tracking-system |     |     | 87  | 5947 | 67  |     |     |     | H2    |
| --------------- | --- | --- | --- | ---- | --- | --- | --- | --- | ----- |
| user-management |     |     | 69  | 4274 | 21  |     |     |     | MySQL |
✓
| webgoat      |     |     | 355  | 27638            | 204  |     |                              |     | H2  |
| ------------ | --- | --- | ---- | ---------------- | ---- | --- | ---------------------------- | --- | --- |
| youtube-mock |     |     | 29   | 3229             |      | 1   |                              |     |     |
| Total 36     |     |     | 6465 | 657162           | 1487 | 15  |                              |     | 25  |
|              |     |     |      | modeofEvoMaster. |      |     | Oneachofthese8APIs,EvoMaster |     |     |
ExperimentsforRQ2wererunusingblack-box
was run for 1 hour. Experiments were repeated 10 times per API, for a total of 80 hours.
As all the APIs used for RQ3 are written in Java or Kotlin, to answer this research question we use
the white-box mode of EvoMaster. We use the same time budget and repetition settings as in RQ2, i.e.,
EvoMaster was run for 1 hour, with each experiments repeated 10 times. This resulted in a duration of 360
hours.
Our novel oracles can work both for black-box and white-box testing. We use different settings in RQ2 and
RQ3 to show this being indeed the case. In total, our experiments took more than 440 hours, i.e., more than 18
| days if run | in sequence. |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Answering RQ4 did not require running any further experiment, as based on the same data for the other
RQs.
| 5.3 Results | for | RQ1 |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In every single experiment for RQ1, the injected faults were correctly identified. When there are no complex
input constraints that prevent reaching the execution of the faulty code, our novel oracles are able to correctly
19

Table 3: Detected faults on the 8 vulnerable APIs.
SUT #Endp F100 F201 F204 F205 F902 F903
capital 21 1.0
crapi 44 6.0 3.0
damn-vulnerable-rest 21 5.3 1.0 0.3 1.2
dvapi 16 3.0 10.0
dvws-node 31 4.0 4.0
vampi 14 2.2 0.1 0.7 5.0
vulnerable-rest-api 19 5.0
webgoat 201 31.0 12.4 5.0 28.0 3.0
Mean 46 7.1 2.2 0.2 0.8 3.6 2.6
Median 21 4.5 0.1 0.0 0.0 0.0 1.5
Sum 367 56.5 17.5 1.3 6.2 28.7 21.0
identify all the security vulnerabilities that we have manually injected.
EvoMasterhasanadvancedandsophisticatedsystemofend-to-endteststoverifyitscorrectness[7]. There
are several artificial APIs in which EvoMaster is automatically run on, and the generated tests are compiled
and run, verifying different properties (e.g., if injected faults are properly identified). These checks on these
artificial APIs are run as JUnit tests as part of EvoMaster’s own continuous integration (CI) system [7] (e.g.,
on GitHub Actions). These nine new artificial examples are now part of these regression test suites, executed in
CI at each new code commit of EvoMaster, as they can be reliably handled by EvoMaster.
RQ1: On simple APIs with injected faults, our techniques are able to reliably identify those security
vulnerabilities.
5.4 Results for RQ2
Table 3 shows the results for RQ2 on eight vulnerable APIs. Besides the results for our novel oracles, we also
report the number of faults related to HTTP 500 status codes, which is the most common oracle in the REST
API fuzzing literature. EvoMaster can also detect other types of functional faults (e.g., schema mismatches)
and SSRF, but those are not discussed and presented in this paper. Faults are based on the endpoint calls that
led to trigger them. For example, if an API has n endpoints, there could be detected at most n distinct faults
related to HTTP 500. It could be possible that the code of an endpoint has more than one fault that could be
triggered differently, or that the same one single fault can lead to more than one endpoint to fail. Counting
based on number of failing endpoints is a common, reasonable compromise when counting the number of faults,
especially in black-box testing, where a root-cause analysis cannot be easily automated.
To simplify the discussion and references to these faults, each one has a unique label, based on the labeling
system defined in WFC [41]. In particular, we have:
• F100: HTTP Status 500
• F200: SQL Injection (Section 3.8)
• F201: Cross Site Scripting (XSS) (Section 3.9)
• F204: Existence Leakage (Section 3.2)
• F205: Not Recognized Authentication (Section 3.1)
• F206: Missed Authorization Checks (Section 3.3)
• F900: Ignore Anonymous (Section 3.5)
• F901: Anonymous Modifications (Section 3.4)
• F902: Leaked Stack Trace (Section 3.6)
• F903: Hidden Accessible (Section 3.7)
Note that codes F1xx are for functional oracles, whereas F2xx are for security faults. Codes in the group 9xx
are for work-in-progress codes not part of WFC yet [41]. The use of unique, stable codes is meant for simplifying
automated comparisons of fuzzers that use the WFC convention. Table 3 shows only data for which faults were
found. If a fault type was never found in any of the 10 runs on any of the 8 APIs, such data is not present in
the table (to avoid cluttering tables with 0-value columns).
20

In these experiments, tens of security faults were found, but only of five different kinds. No fault for
F200 (SQL Injection), F206 (Missed Authorization Checks), F900 (Ignore Anonymous) and F901 (Anonymous
Modifications) were found. Faults can only be found if they exist. We have not manually reviewed the whole
code and documentation of those 8 APIs to see if there are any other faults that could had been found with our
oracles, or if what found is all that is there. Still, the fact that our novel techniques could generate test cases
that can detect these faults show that they can be of practical value.
Looking at the generated tests and logs of these experiments, one issue was clear though. Some of these
vulnerable-by-design example APIs (e.g., crapi, capital and vampi) have endpoints that allow modifying login
information about the users. This is currently a major issue for fuzzers in black-box testing, as such data can be
modified, making the login credentials provided at the beginning of fuzzing no longer valid. This could explain
why some faults were not found. However, this is a not a problem in white-box testing, as database state can be
automatically and efficiently reset after each test execution (e.g., [4]). Also, for real-world APIs, typically login
credentials are handled and managed in separated, ad-hoc APIs.
An alternative would be to run experiments by excluding these endpoints. For example, that is what we did
previously in [6], where it was then possible to detect a F206 (Missed Authorization Checks) in capital. However,
it would be better to design some automated system to handle this issue.
RQ2: Our novel oracles were effective at detecting tens of faults in vulnerable APIs used as security examples.
5.5 Results for RQ3
When it comes to white-box testing of the APIs in WFD, in Table 4 we can see that security faults are found in
most of the APIs, with hundreds of distinct cases. However, no fault of types F200 (SQL Injection) and F206
(Missed Authorization Checks) were found. These are among the most critical types of faults that we can detect
with our novel techniques.
Table 4 shows that, on the 36 analyzed APIs, in total our oracles detected more than 300 distinct faults
(although not all were found in all runs). This provides evidence for the practical value of our novel techniques.
An API like familie-ba-sak is large and complex (Table 2). It is made by the public administration in
Norway, dealing with ‘‘child benefit case processing’’, used by millions of people.14 Finding a Missed-Check or
SQL Injection would had rather been unsettling, and we are glad none was found. (If any was found, we would
have contacted the Norwegian authorities before making this paper public).
Interestingly, there were several cases of Not Recognized Authentication (Section 3.1). Figure 10 shows an
example of generated test detecting a Not Recognized Authentication (Section 3.1) fault. This automatically
generated test case starts with 2 calls to the authentication service, to get dynamic authentication tokens for the
usersVeileder(Line8)andTaskRunner(Line15). Thefirstcallon/api/task/logg/710withVeiledershows
that such endpoint requires authentication/authorization, as a 401 status code is returned (Line 24). A second
call on the same endpoint with TaskRunner gets a 200 status code (Line 33). This provides evidence that the
credentialsforTaskRunnerarenotwronglyset. However,acallwithsameuseron/api/ekstern/pensjon/hent-
barnetrygd returns a 401 (Line 52), which would imply the user is not recognized. Based on previous calls, this
is wrong. Note that, even if access tokens might have a short life-span, they are dynamically retrieved in the
same test case, and, as such, after a few (milli)seconds they should still be valid. Interestingly, the error message
(in Norwegian at Line 56) seems to support the fact that this is a bug (i.e., a 403 should had been returned), as
it states, translated with Google Translate: ‘‘Pension service can only be called by pension or logged in user
with ADMINISTRATOR role’’.
Not all faults have the same severity. For example, a 500 status does not really mean that the API crashed.
If it crashed, then it would not be able to send back a HTTP response with status 500, and the TCP socket
would had been closed. Typically, when an exception is thrown, then the framework (e.g., Spring for Java)
running the API catches the exception, and sends back an error response. The API will keep running. If the
crash is due to invalid input, then the fault is related to improper input validation, and rather a 4xx status error
(indicating an user error) should had been returned. A typical example is assuming a requested resource to exist,
and crashing on a null-pointer exception instead of returning a 404 not found user error status [34]. This is
still a fault that needs to be fixed, but it is not as critical as it might look at a first sight. In this paper, we
have proposed 7 novel oracles, but we cannot say how critical they are for certain, unless empirical studies or
interviews/surveys with practitioners were carried out to assess their assumed importance. However, we argue
that a security vulnerability that leads to unauthorized access of resources (e.g., Missed-Check) is likely much
more important than wrongly returning a 500 status code instead of a 404.
In the data generated in our experiments, there are hundreds of interesting cases that could be worth
discussing. For reason of space, we cannot discuss all of them. However, we noticed that, in a few cases, when
our novel oracles detected faults, the problem was not due to a security vulnerability, but rather due to severe
faults related to HTTP semantics. To clarify, we will discuss here some of these cases in more details.
14https://github.com/navikt/familie-ba-sak
21

1@Test @Timeout(60)
2public void test_138_postOnHent_barnetrygdAuthenticatedButWronglyToldNot() throws Exception
{
3
4 final String token_Veileder = given()
5 .contentType("application/x-www-form-urlencoded")
6 .body("name=Veileder&grant_type=client_credentials&code=foo&client_id=foo&
client_secret=secret")
7 .post("http://localhost:10512/azuread/token")
8 .then().extract().response().path("access_token");
9
10 final String auth_Veileder = "Bearer " + token_Veileder;
11 final String token_TaskRunner = given()
12 .contentType("application/x-www-form-urlencoded")
13 .body("name=TaskRunner&grant_type=client_credentials&code=foo&client_id=foo&
client_secret=secret")
14 .post("http://localhost:10512/azuread/token")
15 .then().extract().response().path("access_token");
16
17 final String auth_TaskRunner = "Bearer " + token_TaskRunner;
18
19 given().accept("*/*")
20 .header("x-EMextraHeader123", "_EM_14362_XYZ_")
21 .header("Authorization", auth_Veileder) // Veileder
22 .get(baseUrlOfSut + "/api/task/logg/710?page=352")
23 .then()
24 .statusCode(401)
25 .assertThat()
26 .contentType("text/html");
27
28 given().accept("*/*")
29 .header("x-EMextraHeader123", "42")
30 .header("Authorization", auth_TaskRunner) // TaskRunner
31 .get(baseUrlOfSut + "/api/task/logg/718")
32 .then()
33 .statusCode(200)
34 .assertThat()
35 .contentType("application/json")
36 .body("’data’", nullValue())
37 .body("’status’", containsString("FEILET"))
38 .body("’melding’", containsString("Henting av tasklogg feilet."))
39 .body("’frontendFeilmelding’", containsString("Henting av tasklogg feilet."));
40
41 // Fault205. Wrongly Not Recognized as Authenticated.
42 given().accept("application/json")
43 .header("x-EMextraHeader123", "42")
44 .header("Authorization", auth_TaskRunner) // TaskRunner
45 .contentType("application/json")
46 .body(" { " +
47 " \"ident\": \"_EM_14364_XYZ_\", " +
48 " \"fraDato\": \"2020-12-01\" " +
49 " } ")
50 .post(baseUrlOfSut + "/api/ekstern/pensjon/hent-barnetrygd?EMextraParam123=
_EM_14366_XYZ_")
51 .then()
52 .statusCode(401)
53 .assertThat()
54 .contentType("application/json")
55 .body("’servlet’", containsString("dispatcherServlet"))
56 .body("’message’", containsString("Pensjon tjeneste kan kun kalles av pensjon
eller innlogget bruker med FORVALTER rolle"))
57 .body("’url’", containsString("/api/ekstern/pensjon/hent-barnetrygd"))
58 .body("’status’", containsString("401"));
59}
Figure 10: Snippet example of generated test case in which a Not Recognized Authentication (Section 3.1) fault
is identified in familie-ba-sak. Due to reason of space, the generated test’s JavaDoc is not shown.
22

1/**
2* Calls:
| 3* 1 -   | (200)       | OPTIONS:/api/users/checkEmailAvailability |         |             |      |     |     |     |     |
| -------- | ----------- | ----------------------------------------- | ------- | ----------- | ---- | --- | --- | --- | --- |
| 4* 2 -   | (415)       | PUT:/api/users/checkEmailAvailability     |         |             |      |     |     |     |     |
| 5* Found | 3 potential |                                           | faults. | Type-codes: | 101, | 903 |     |     |     |
6*/
| 7@Test(timeout |     | = 60000) |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
8public void test_46_putOnCheckEmailAvailabilityShowsFaults_101_903() throws Exception {
9
| 10 final | String | token_admin                                       |       | = given()  |                     |     |     |     |     |
| -------- | ------ | ------------------------------------------------- | ----- | ---------- | ------------------- | --- | --- | --- | --- |
| 11       |        | .contentType("application/json")                  |       |            |                     |     |     |     |     |
| 12       |        | .body("                                           | { " + |            |                     |     |     |     |     |
| 13       |        | " \"usernameOrEmail\":                            |       |            | \"admin\",          |     | " + |     |     |
| 14       |        | " \"password\":                                   |       | \"bar123\" |                     | " + |     |     |     |
| 15       |        | " }                                               | ")    |            |                     |     |     |     |     |
| 16       |        | .post(baseUrlOfSut                                |       | +          | "/api/auth/signin") |     |     |     |     |
| 17       |        | .then().extract().response().path("accessToken"); |       |            |                     |     |     |     |     |
18
| 19 final | String | auth_admin |     | = "Bearer | " + | token_admin; |     |     |     |
| -------- | ------ | ---------- | --- | --------- | --- | ------------ | --- | --- | --- |
20
21 // Fault101. Received A Response From API With A Structure/Data That Is Not Matching Its Schema. Type
: validation.request.operation.notAllowed OPTIONS operation not allowed on path ’/api/users/
checkEmailAvailability’.
22 given().accept("*/*")
|     |     | .header("Authorization", |     |     | auth_admin) |     |          |     |     |
| --- | --- | ------------------------ | --- | --- | ----------- | --- | -------- | --- | --- |
| 23  |     |                          |     |     |             |     | // admin |     |     |
24 .options(baseUrlOfSut + "/api/users/checkEmailAvailability")
| 25  |     | .then()                       |     |                                |     |     |     |     |     |
| --- | --- | ----------------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- |
| 26  |     | .statusCode(200)              |     |                                |     |     |     |     |     |
| 27  |     | .assertThat()                 |     |                                |     |     |     |     |     |
| 28  |     | // .header("Allow",           |     | "HEAD,DELETE,GET,OPTIONS,PUT") |     |     |     |     |     |
| 29  |     | .body(isEmptyOrNullString()); |     |                                |     |     |     |     |     |
30
31 // Fault101. Received A Response From API With A Structure/Data That Is Not Matching Its Schema. Type
: validation.response.body.unexpected No response body is expected but one was found.
| 32 // | Fault903. | Hidden | Accessible |     | Endpoint. |     |     |     |     |
| ----- | --------- | ------ | ---------- | --- | --------- | --- | --- | --- | --- |
33 given().accept("*/*")
| 34  |     | .header("Authorization",         |     |                                        | auth_admin) |     | // admin |               |     |
| --- | --- | -------------------------------- | --- | -------------------------------------- | ----------- | --- | -------- | ------------- | --- |
| 35  |     | .put(baseUrlOfSut                |     | + "/api/users/checkEmailAvailability") |             |     |          |               |     |
| 36  |     | .then()                          |     |                                        |             |     |          |               |     |
| 37  |     | .statusCode(415)                 |     |                                        |             |     |          |               |     |
| 38  |     | .assertThat()                    |     |                                        |             |     |          |               |     |
| 39  |     | .contentType("application/json") |     |                                        |             |     |          |               |     |
| 40  |     | .body("’status’",                |     | numberMatches(415))                    |             |     |          |               |     |
| 41  |     | .body("’error’",                 |     | containsString("Unsupported            |             |     |          | Media Type")) |     |
42 .body("’message’", containsString("Content type ’application/x-www-form-urlencoded;charset=
| UTF-8’ |     | not supported")) |     |                                                       |     |     |     |     |     |
| ------ | --- | ---------------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|        |     | .body("’path’",  |     | containsString("/api/users/checkEmailAvailability")); |     |     |     |     |     |
43
44}
Figure 11: Example of generated test for blogapi finding a F903 Hidden Accessible Endpoint fault.
1/**
2* Calls:
| 3* 1 -   | (404)       | OPTIONS:/v2/projects/{project} |       |              |     |     |     |     |     |
| -------- | ----------- | ------------------------------ | ----- | ------------ | --- | --- | --- | --- | --- |
| 4* 2 -   | (404)       | POST:/v2/projects/{project}    |       |              |     |     |     |     |     |
| 5* Found | 1 potential |                                | fault | of type-code | 903 |     |     |     |     |
6*/
7@Test @Timeout(60)
| 8public | void | test_6_postOnProjectHiddenAccessible() |     |     |     |     | throws | Exception | {   |
| ------- | ---- | -------------------------------------- | --- | --- | --- | --- | ------ | --------- | --- |
9
10 given().accept("*/*")
.options(baseUrlOfSut
| 11  |     |                  |     |     | + "/v2/projects/omm_postfix") |     |     |     |     |
| --- | --- | ---------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
| 12  |     | .then()          |     |     |                               |     |     |     |     |
| 13  |     | .statusCode(404) |     |     |                               |     |     |     |     |
| 14  |     | .assertThat()    |     |     |                               |     |     |     |     |
15 // .header("Allow", "HEAD,DELETE,POST,GET,OPTIONS,PUT,PATCH")
.contentType("application/json")
16
| 17  |     | .body("’error’", |     | containsString("Endpoint |     |     |     | not found.")); |     |
| --- | --- | ---------------- | --- | ------------------------ | --- | --- | --- | -------------- | --- |
18
| 19 // | Fault903. | Hidden | Accessible |     | Endpoint. |     |     |     |     |
| ----- | --------- | ------ | ---------- | --- | --------- | --- | --- | --- | --- |
20 given().accept("*/*")
.post(baseUrlOfSut
| 21  |     |                                  |     | +                        | "/v2/projects/omm_postfix") |     |     |                |     |
| --- | --- | -------------------------------- | --- | ------------------------ | --------------------------- | --- | --- | -------------- | --- |
| 22  |     | .then()                          |     |                          |                             |     |     |                |     |
| 23  |     | .statusCode(404)                 |     |                          |                             |     |     |                |     |
| 24  |     | .assertThat()                    |     |                          |                             |     |     |                |     |
| 25  |     | .contentType("application/json") |     |                          |                             |     |     |                |     |
|     |     | .body("’error’",                 |     | containsString("Endpoint |                             |     |     |                |     |
| 26  |     |                                  |     |                          |                             |     |     | not found.")); |     |
27}
Figure 12: Example of generated test for bibliotek finding a F903 Hidden Accessible Endpoint fault.
23

|                      |     | Table | 4: Detected | faults on | the 36 | APIs from | WFD. |      |       |      |
| -------------------- | --- | ----- | ----------- | --------- | ------ | --------- | ---- | ---- | ----- | ---- |
| SUT                  |     | #Endp | F100        | F201      | F204   | F205      | F900 | F901 | F902  | F903 |
| bibliothek           |     |       | 8           | 2.7       |        |           |      |      |       | 26.0 |
| blogapi              |     |       | 52 28.5     | 0.1       |        | 0.5       |      |      |       | 7.0  |
| catwatch             |     |       | 14          | 6.4       |        |           | 6.2  |      | 2.5   |      |
| cwa-verification     |     |       | 5           | 5.0       |        |           |      |      |       |      |
| erc20-rest-service   |     |       | 13 12.0     |           |        |           |      |      |       |      |
| familie-ba-sak       |     |       | 183 151.2   | 2.0       |        | 12.0      | 4.6  |      |       |      |
| features-service     |     |       | 18 12.5     |           |        |           |      | 1.0  | 12.3  |      |
| genome-nexus         |     |       | 23          | 5.0       |        |           |      |      |       | 2.0  |
| gestaohospital       |     |       | 20          | 1.9 2.2   |        |           |      | 3.6  |       | 6.0  |
| http-patch-spring    |     |       | 6           | 0.5       |        |           |      | 1.2  |       |      |
| languagetool         |     |       | 2           | 1.0       |        |           |      |      |       |      |
| market               |     |       | 13          | 5.3       |        |           |      |      |       |      |
| microcks             |     |       | 88 10.2     | 7.9       |        |           |      |      |       | 14.0 |
| ocvn                 |     |       | 258 194.3   |           |        |           |      |      | 82.9  |      |
| ohsome-api           |     |       | 134         | 1.6       |        |           |      |      |       |      |
| pay-publicapi        |     |       | 10 10.0     |           |        |           |      |      |       |      |
| person-controller    |     |       | 12 11.0     |           |        |           |      |      | 5.0   | 2.0  |
| proxyprint           |     |       | 74 33.9     |           | 2.0    | 3.7       |      |      | 8.7   |      |
| quartz-manager       |     |       | 11          | 5.9       |        |           |      |      |       |      |
| reservations-api     |     |       | 7           | 3.8       |        | 0.1       |      |      |       | 2.0  |
| rest-ncs             |     |       | 6           |           |        |           |      |      |       |      |
| rest-news            |     |       | 7           | 2.9       |        |           |      | 2.4  |       |      |
| rest-scs             |     |       | 11          |           |        |           |      |      |       |      |
| restcountries        |     |       | 22          | 1.0       |        |           |      |      |       |      |
| scout-api            |     |       | 49 15.2     | 0.3       |        |           |      |      |       |      |
| session-service      |     |       | 8           | 3.6       |        |           |      |      |       | 2.0  |
| spring-actuator-demo |     |       | 2           | 1.0       |        |           |      |      |       |      |
| spring-batch-rest    |     |       | 5           | 1.8 1.0   |        |           |      |      |       |      |
| spring-ecommerce     |     |       | 27 15.8     |           |        | 3.1       | 0.3  |      |       |      |
| spring-rest-example  |     |       | 9           | 1.0 0.4   |        |           |      | 4.0  |       |      |
| swagger-petstore     |     |       | 19          | 9.2 3.8   |        |           |      | 3.0  |       |      |
| tiltaksgjennomforing |     |       | 79 28.7     | 1.0       |        |           |      |      |       | 8.0  |
| tracking-system      |     |       | 67          | 10.6      |        |           |      | 1.9  |       | 21.0 |
| user-management      |     |       | 21          | 6.7 5.2   |        |           |      | 3.7  |       | 4.0  |
| webgoat              |     |       | 204         | 5.0       |        |           |      |      | 4.0   | 2.0  |
| youtube-mock         |     |       | 1           |           |        |           |      |      |       |      |
| Mean                 |     |       | 41 16.3     | 1.1       | 0.1    | 0.5       | 0.3  | 0.6  | 3.2   | 2.7  |
| Median               |     |       | 14          | 5.0 0.0   | 0.0    | 0.0       | 0.0  | 0.0  | 0.0   | 0.0  |
| Sum                  |     |       | 1488 588.1  | 41.0      | 2.0    | 19.4      | 11.1 | 20.8 | 115.4 | 96.0 |
Figure 11 and Figure 12 show two distinct examples of F903 Hidden Accessible Endpoint faults, in the
blogapi and bibliotek APIs. After a manual investigation of these APIs, there is no hidden accessible endpoint
in these APIs. There are two other problems though. First, the OPTIONS is returning what could be consider
as ‘‘garbage’’, claiming in the Allow header the presence of endpoints that do not exist. Second, calling those
endpoints does not return a 405 (or 501), as expected by HTTP specifications. They rather return a 415 (for
blogapi) or 404 (bibliotek). Either case, these response statuses make no sense according the semantics of HTTP.
This is not a fault in the implementation of the business logic of these APIs, but a rather a serious fault or
| misconfiguration | in their | employed | HTTP | frameworks. |     |     |     |     |     |     |
| ---------------- | -------- | -------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
Figure 13 and Figure 14 show two distinct examples of F900 Ignore Anonymous faults, in the catwatch
and familie-ba-sak APIs. In theory, this is a potentially catastrophic vulnerability. The API catwatch has no
defined authentication information in WFD (recall Table 2). A call to the endpoint GET:/config without any
authentication info returns a 200 with some data. However, a non-authenticated call with the query parameter
access token=cvOYB8K5cuf (Line 15) leads to return a 403. Without an in-depth analysis of the semantics of
24

1/**
2* Calls:
| 3* 1 - (403) | GET:/config |                     |     |      |     |     |     |     |
| ------------ | ----------- | ------------------- | --- | ---- | --- | --- | --- | --- |
| 4* 2 - (200) | GET:/config |                     |     |      |     |     |     |     |
| 5* Found     | 3 potential | faults. Type-codes: |     | 101, | 900 |     |     |     |
6*/
| 7@Test(timeout | = 60000) |     |     |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
8public void test_69_getOnConfigShowsFaults_101_900() throws Exception {
9
10 // Fault101. Received A Response From API With A Structure/Data That Is Not
Matching Its Schema. Type: validation.response.body.unexpected No response body is
| expected | but                                | one was found.                   |                             |                                  |            |             |     |     |
| -------- | ---------------------------------- | -------------------------------- | --------------------------- | -------------------------------- | ---------- | ----------- | --- | --- |
| 11       | given().accept("application/json") |                                  |                             |                                  |            |             |     |     |
| 12       |                                    | .header("x-EMextraHeader123",    |                             |                                  |            | "")         |     |     |
| 13       |                                    | .header("X-Organizations",       |                             |                                  |            | "urLJpDVv") |     |     |
| 14       |                                    | .get(baseUrlOfSut                |                             | +                                | "/config?" | +           |     |     |
| 15       |                                    |                                  | "access_token=cvOYB8K5cuf&" |                                  |            |             | +   |     |
| 16       |                                    |                                  | "q=HXDhFkqk")               |                                  |            |             |     |     |
| 17       |                                    | .then()                          |                             |                                  |            |             |     |     |
| 18       |                                    | .statusCode(403)                 |                             |                                  |            |             |     |     |
| 19       |                                    | .assertThat()                    |                             |                                  |            |             |     |     |
| 20       |                                    | .contentType("application/json") |                             |                                  |            |             |     |     |
| 21       |                                    | .body("’error’",                 |                             | containsString("access_denied")) |            |             |     |     |
22 .body("’error_description’", containsString("Unable to obtain a new
access token for resource &#39;null&#39;. The provider manager is not configured to
| support | it.")); |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
23
24 // Fault101. Received A Response From API With A Structure/Data That Is Not
Matching Its Schema. Type: validation.response.body.schema.type [Path ’/github.login’]
Instance type (null) does not match any allowed primitive type (allowed: ["string"])
25 // Fault900. A Protected Resource Is Accessible Without Providing Any
Authentication.
| 26  | given().accept("application/json") |                                  |                                  |     |            |     |     |     |
| --- | ---------------------------------- | -------------------------------- | -------------------------------- | --- | ---------- | --- | --- | --- |
| 27  |                                    | .header("x-EMextraHeader123",    |                                  |     |            | "") |     |     |
| 28  |                                    | .get(baseUrlOfSut                |                                  | +   | "/config?" | +   |     |     |
| 29  |                                    |                                  | "q=_EM_6668_XYZ_&"               |     |            | +   |     |     |
| 30  |                                    |                                  | "organizations=LVszttcjhEwqOL1&" |     |            |     |     | +   |
| 31  |                                    |                                  | "limit=tawdhQdONfwwEwo")         |     |            |     |     |     |
| 32  |                                    | .then()                          |                                  |     |            |     |     |     |
| 33  |                                    | .statusCode(200)                 |                                  |     |            |     |     |     |
| 34  |                                    | .assertThat()                    |                                  |     |            |     |     |     |
| 35  |                                    | .contentType("application/json") |                                  |     |            |     |     |     |
36 .body("’cache.path’", containsString("D:\\WORK\\EXPERIMENTS\\2026-
security\\wb_0_9/temp/tmp_catwatch/cache_10212"))
| 37  |     | .body("’cache.size’",        |     |     | containsString("50")) |                          |     |     |
| --- | --- | ---------------------------- | --- | --- | --------------------- | ------------------------ | --- | --- |
| 38  |     | .body("’endpoints.enabled’", |     |     |                       | containsString("false")) |     |     |
39 .body("’endpoints.health.enabled’", containsString("true"))
| 40  |     | .body("’github.login’", |     |     | nullValue()) |     |     |     |
| --- | --- | ----------------------- | --- | --- | ------------ | --- | --- | --- |
41 .body("’organization.list’", containsString("zalando,zalando-stups,
zalando-incubator"))
| 42  |     | .body("’schedule’", |     |     | containsString("0 |     |     | 1 8 * * *")) |
| --- | --- | ------------------- | --- | --- | ----------------- | --- | --- | ------------ |
43 .body("’scoring.project’", containsString("function(project) {var
daysSinceLastPush = 0;if (project.lastPushed) {var tokens = project.lastPushed.split(\"
\");var day = tokens[2];var month = tokens[1];var year = tokens[5];var lastPushedDate
= new Date(day + ’ ’ + month + ’ ’ + year);var millisInDay = 86400000;daysSinceLastPush
= Math.floor((new Date() - lastPushedDate) / millisInDay);}var maintainersPenalty = 0;
if (project.maintainers.length < 2) {maintainersPenalty = 100;}return project.
starsCount * 3 + project.forksCount * 2 + project.contributorsCount * 5 -
| daysSinceLastPush |     | - maintainersPenalty}"))                   |     |     |     |     |     |              |
| ----------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | ------------ |
| 44                |     | .body("’spring.database.driverClassName’", |     |     |     |     |     | nullValue()) |
| 45                |     | .body("’spring.datasource.platform’",      |     |     |     |     |     | nullValue()) |
46 .body("’spring.datasource.username’", containsString("sa"))
| 47  |     | .body("’spring.jpa.database’", |     |     |     | nullValue()) |     |     |
| --- | --- | ------------------------------ | --- | --- | --- | ------------ | --- | --- |
48 .body("’spring.jpa.hibernate.ddl-auto’", containsString("update"));
49}
Figure 13: Example of generated test for catwatch finding a F900 Ignore Anonymous fault.
25

| 1   | ...                   |                                  |              |     |                |     |             |
| --- | --------------------- | -------------------------------- | ------------ | --- | -------------- | --- | ----------- |
| 2   | given().accept("*/*") |                                  |              |     |                |     |             |
| 3   |                       | .header("x-EMextraHeader123",    |              |     |                | "") |             |
| 4   |                       | .header("Authorization",         |              |     | auth_Veileder) |     | // Veileder |
| 5   |                       | .contentType("application/json") |              |     |                |     |             |
| 6   |                       | .body("                          | { " +        |     |                |     |             |
| 7   |                       |                                  | " \"ident\": |     | \"\" "         | +   |             |
| 8   |                       |                                  | " } ")       |     |                |     |             |
9 .post(baseUrlOfSut + "/testverktoy/vedtak-om-overgangsstønad")
| 10  |     | .then()                          |     |              |                           |     |     |
| --- | --- | -------------------------------- | --- | ------------ | ------------------------- | --- | --- |
| 11  |     | .statusCode(200)                 |     |              |                           |     |     |
| 12  |     | .assertThat()                    |     |              |                           |     |     |
| 13  |     | .contentType("application/json") |     |              |                           |     |     |
| 14  |     | .body("’data’",                  |     | nullValue()) |                           |     |     |
| 15  |     | .body("’status’",                |     |              | containsString("FEILET")) |     |     |
16 .body("’melding’", containsString("Fant ikke aktiv ident for aktør"
))
| 17  |     | .body("’frontendFeilmelding’", |     |     |               | nullValue()) |     |
| --- | --- | ------------------------------ | --- | --- | ------------- | ------------ | --- |
| 18  |     | .body("’stacktrace’",          |     |     | nullValue()); |              |     |
19
| 20  | given().accept("*/*") |                                  |              |     |                 |     |              |
| --- | --------------------- | -------------------------------- | ------------ | --- | --------------- | --- | ------------ |
| 21  |                       | .header("x-EMextraHeader123",    |              |     |                 | "") |              |
| 22  |                       | .header("Authorization",         |              |     | auth_Forvalter) |     | // Forvalter |
| 23  |                       | .contentType("application/json") |              |     |                 |     |              |
| 24  |                       | .body("                          | { " +        |     |                 |     |              |
| 25  |                       |                                  | " \"ident\": |     | \"\" "          | +   |              |
| 26  |                       |                                  | " } ")       |     |                 |     |              |
27 .post(baseUrlOfSut + "/testverktoy/vedtak-om-overgangsstønad")
| 28  |     | .then()                    |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- |
| 29  |     | .statusCode(403)           |     |     |     |     |     |
| 30  |     | .assertThat()              |     |     |     |     |     |
| 31  |     | .contentType("text/html"); |     |     |     |     |     |
32
33 // Fault900. A Protected Resource Is Accessible Without Providing Any
Authentication.
| 34  | ValidatableResponse | res_2                            | = given().accept("*/*") |     |        |     |     |
| --- | ------------------- | -------------------------------- | ----------------------- | --- | ------ | --- | --- |
| 35  |                     | .header("x-EMextraHeader123",    |                         |     |        | "") |     |
| 36  |                     | .contentType("application/json") |                         |     |        |     |     |
| 37  |                     | .body("                          | { " +                   |     |        |     |     |
| 38  |                     |                                  | " \"ident\":            |     | \"\" " | +   |     |
| 39  |                     |                                  | " } ")                  |     |        |     |     |
40 .post(baseUrlOfSut + "/testverktoy/vedtak-om-overgangsstønad")
| 41  |     | .then()                          |     |              |                           |     |     |
| --- | --- | -------------------------------- | --- | ------------ | ------------------------- | --- | --- |
| 42  |     | .statusCode(200)                 |     |              |                           |     |     |
| 43  |     | .assertThat()                    |     |              |                           |     |     |
| 44  |     | .contentType("application/json") |     |              |                           |     |     |
| 45  |     | .body("’data’",                  |     | nullValue()) |                           |     |     |
| 46  |     | .body("’status’",                |     |              | containsString("FEILET")) |     |     |
47 .body("’melding’", containsString("Fant ikke aktiv ident for aktør"
))
| 48  |     | .body("’frontendFeilmelding’", |     |     |               | nullValue()) |     |
| --- | --- | ------------------------------ | --- | --- | ------------- | ------------ | --- |
| 49  |     | .body("’stacktrace’",          |     |     | nullValue()); |              |     |
50 String location_vedtak_om_overgangsst_nad__98 = res_2.extract().header("location");
51 assertTrue(isValidURIorEmpty(location_vedtak_om_overgangsst_nad__98));
52}
Figure 14: Snippet example of generated test for familie-ba-sak finding a F900 Ignore Anonymous fault. For
| reason of | space, the calls retrieving | the | authentication |     | tokens are | omitted. |     |
| --------- | --------------------------- | --- | -------------- | --- | ---------- | -------- | --- |
26

this API, it is unclear if this is a major security vulnerability, or misuse of HTTP status codes. Either way, it is
problematic.
Thecaseoffamilie-ba-sak inFigure14iseasiertoanalyze,butpotentiallymoredisturbing. Anauthenticated
user ‘‘Veileder’’ makes a POST to an endpoint, successfully returning a 200 status code (Line 11). A different
user ‘‘Forvalter’’, with different permission rights, is blocked from doing the same operation, and obtains a 403
(Line 29). Finally, a call without any authentication information is successful with a 200 status code (Line 42).
Without looking at the response, this could be a major security issue. However, FEILET in Norwegian means
‘‘the error’’, and ‘‘Fant ikke aktiv ident for aktør’’ means ‘‘No active ident found for actor’’. In other
words, the call fails, but the API decides to return a 200 success status code, which seems completely wrong in
this context.
The case of Figure 14 is interesting because, without a natural-language processing (NLP) of the text of the
responses, it could be difficult to automatically detect when an API is wrongly returning a 2xx on a failed call.
And, even if NLP techniques are used, there is the need to make sure they work for different human languages
(e.g., Norwegian Bokm˚al or Nynorsk, as in this case). Several of our security oracles rely on the correct use
of the HTTP protocol (e.g., user errors should return a status code in the 4xx family). When they detect a
fault, they could indeed detect a security fault, or, like in this case, they might detect a major issue in the use of
HTTP semantics in the tested API. Either case, these are serious faults that need fixing.
RQ3: Our novel security oracles were effective at finding new faults in existing real-world APIs. They either
detect security vulnerabilities, or serious issues in the use of the HTTP protocol.
5.6 Results for RQ4
In fuzzing, there is a balance to strike between the time spent in generating high coverage test cases (either
code coverage and/or REST API schema coverage) and the time spent in crafting ad-hoc test cases targeted
at specific security vulnerabilities. As explained in Section 4, our security-phase is run as a post-processing,
after the main fuzzing is completed. In our context, the number of generated tests evaluated for security is
fixed, depending on the number of endpoints and the type and quality of the generated tests during the initial
fuzzing. If the main fuzzing session is run for 1 hour, it is important to evaluate what is the additional overhead
introduced by our security phase.
Table 5 shows, for each API in WFD used for RQ3, the overhead in seconds of our additional security phase.
To better analyze those results, we also report the 2xx schema coverage (i.e., the percentage of endpoints for
which successful 2xx calls were created). If no success call is made, and the execution of test cases ends at the
first layer of input validation with a 4xx response, then it would be unlikely that any security testing would be
successful, as most of our oracles require the ability to generate success calls to build upon. Fuzzing REST APIs
has witnessed significant improvements in the research literature, but it still has many open research problems
that need addressing [48].
As shown in Table 5, in most cases our security phase is fast, taking few tens of seconds, or up to 2 minutes,
which is a reasonable and practical amount of time considering a budget of 1-hour for the initial fuzzing session.
On these APIs, the median time is less than 14 seconds, whereas the average is less than 3 minutes. Out of 36
APIs in WFD, there are, though, three outliers: familie-ba-sak (13 minutes), ocvn (33 minutes) and proxyprint
(38minutes). Fromausabilityandpracticalstandpoint,inthenextversionsofEvoMasteritwillbeimportant
to provide some further parameters to put timeouts on the security-phase, either in absolute terms (e.g., 10
minutes), or as proportion of the search budget (e.g., 20% of the budget, which would be 12 minutes if the
budget is 1 hour).
RQ4: In the large majority of cases, our novel techniques have small, negligible computational overhead.
6 Threats to Validity
Our experiments rely on randomized algorithms. To take their randomness into account, experiments were
repeated 10 times.
In our empirical study, 52 distinct APIs were used (9 toy examples, 8 examples for security research, and 36
from theWFD corpus). Consideringthe use of 52APIs, although this study might be currently thelargest study
in literature so far on open-source REST APIs, a larger case study would be needed to be able to generalize our
results, especially for APIs developed in industry.
Our novel oracles are not specific nor tailored to any fuzzer. In our experiments, we used EvoMaster, but
in theory any other state-of-the-art fuzzer could had been used. How easy or difficult would it be for our novel
techniques to be integrated in other fuzzers is a matter that would require further investigation.
27

Table 5: For the 36 APIs in WFD, we report the obtained 2xx coverage of their endpoints, and the overhead in
| seconds of | our new security     | phase. |            |       |                   |        |
| ---------- | -------------------- | ------ | ---------- | ----- | ----------------- | ------ |
|            | SUT                  |        | #Endpoints | % 2xx | Coverage Overhead |        |
|            | bibliothek           |        |            | 8     | 20.0              | 1.2    |
|            | blogapi              |        |            | 52    | 30.4              | 123.7  |
|            | catwatch             |        |            | 14    | 49.3              | 110.2  |
|            | cwa-verification     |        |            | 5     | 0.0               | 0.0    |
|            | erc20-rest-service   |        |            | 13    | 7.7               | 0.4    |
|            | familie-ba-sak       |        |            | 183   | 49.5              | 818.2  |
|            | features-service     |        |            | 18    | 21.1              | 5.4    |
|            | genome-nexus         |        |            | 23    | 72.9              | 37.1   |
|            | gestaohospital       |        |            | 20    | 58.3              | 12.4   |
|            | http-patch-spring    |        |            | 6     | 73.3              | 8.2    |
|            | languagetool         |        |            | 2     | 92.9              | 49.7   |
|            | market               |        |            | 13    | 43.1              | 58.3   |
|            | microcks             |        |            | 88    | 46.3              | 81.9   |
|            | ocvn                 |        |            | 258   | 84.0              | 1986.5 |
|            | ohsome-api           |        |            | 134   | 2.8               | 14.8   |
|            | pay-publicapi        |        |            | 10    | 57.5              | 5.1    |
|            | person-controller    |        |            | 12    | 43.5              | 3.0    |
|            | proxyprint           |        |            | 74    | 67.7              | 2325.6 |
|            | quartz-manager       |        |            | 11    | 36.4              | 7.3    |
|            | reservations-api     |        |            | 7     | 57.1              | 91.5   |
|            | rest-ncs             |        |            | 6     | 100.0             | 1.0    |
|            | rest-news            |        |            | 7     | 91.4              | 9.2    |
|            | rest-scs             |        |            | 11    | 100.0             | 1.0    |
|            | restcountries        |        |            | 22    | 100.0             | 6.4    |
|            | scout-api            |        |            | 49    | 34.1              | 21.8   |
|            | session-service      |        |            | 8     | 65.3              | 10.1   |
|            | spring-actuator-demo |        |            | 2     | 100.0             | 21.7   |
|            | spring-batch-rest    |        |            | 5     | 100.0             | 1.0    |
|            | spring-ecommerce     |        |            | 27    | 47.7              | 156.9  |
|            | spring-rest-example  |        |            | 9     | 92.6              | 35.0   |
|            | swagger-petstore     |        |            | 19    | 69.0              | 2.4    |
|            | tiltaksgjennomforing |        |            | 79    | 8.9               | 8.7    |
|            | tracking-system      |        |            | 67    | 38.7              | 142.8  |
|            | user-management      |        |            | 21    | 66.7              | 61.2   |
|            | webgoat              |        |            | 204   | 16.7              | 54.3   |
|            | youtube-mock         |        |            | 1     | 22.2              | 0.0    |
|            | Average              |        |            |       | 54.6              | 174.3  |
|            | Median               |        |            |       | 53.3              | 13.6   |
7 Conclusion
In this paper, we have presented nine novel oracles aimed at detecting authorization-related faults and common
injection vulnerabilities in REST APIs. These techniques were used to detect hundreds of new faults in an
| empirical study | consisting | of 52 REST APIs. |     |     |     |     |
| --------------- | ---------- | ---------------- | --- | --- | --- | --- |
OurnoveltechniqueswereimplementedasanextensionofEvoMaster,astate-of-the-artopen-sourcefuzzer.
Once our novel techniques detect new faults, executable test cases (e.g., in JUnit format) are automatically
generated to help practitioners in industry to reproduce the faults and debug them.
Future work will aim at designing new automated oracles to identify other kinds of security faults in REST
EvoMaster,
APIs, and carry out empirical studies in industry (for example at Fortune 500 enterprises that use
| like Volkswagen | [5] and | Meituan [50]). |     |     |     |     |
| --------------- | ------- | -------------- | --- | --- | --- | --- |
EvoMaster
Our extension to is released as open-source at www.evomaster.org. The novel techniques
presentedinthispaperarenowactivatedbydefaultinEvoMasterlatest’sreleases. Thehundreds/thousandsof
practitioners in industry that use EvoMaster are already directly benefitting from the research work presented
in this paper.
28

Data Availability
All the techniques presented in this paper are implemented as part of EvoMaster. The fuzzer EvoMaster is
open-source on GitHub,15 where each new release is automatically published on Zenodo for long-term storage
(e.g., [9]).
WFD is open-source on GitHub,16 with as well each new release automatically uploaded to Zenodo for
long-term storage (e.g., [12]).
The vulnerable APIs used for RQ2 are all open-source on GitHub, with IDs as specified in Table 1.
Acknowledgment
This work is funded by the European Research Council (ERC) under the European Union’s Horizon 2020
research and innovation programme (EAST project, grant agreement No. 864972). Omur Sahin is supported by
the TU¨BI˙TAK 2219 International Postdoctoral Research Fellowship Program (Project ID: 1059B192300060).
Man Zhang is supported by the National Science Foundation of China (grant agreement No. 62502022).
References
[1] Dennis Appelt, Cu Duy Nguyen, Lionel C Briand, and Nadia Alshahwan. 2014. Automated testing for SQL
injection vulnerabilities: an input mutation approach. In Proceedings of the 2014 International Symposium
on Software Testing and Analysis. 259--269.
[2] Andrea Arcuri. 2017. RESTful API Automated Test Case Generation. In IEEE International Conference
on Software Quality, Reliability and Security (QRS). IEEE, 9--20.
[3] Andrea Arcuri. 2019. RESTful API Automated Test Case Generation with EvoMaster. ACM Transactions
on Software Engineering and Methodology (TOSEM) 28, 1 (2019), 3.
[4] Andrea Arcuri and Juan P Galeotti. 2020. Handling SQL databases in automated system test generation.
ACM Transactions on Software Engineering and Methodology (TOSEM) 29, 4 (2020), 1--31.
[5] A. Arcuri, A. Poth, and O. Rrjolli. 2025. Introducing Black-Box Fuzz Testing for REST APIs in Indus-
try: Challenges and Solutions. In IEEE International Conference on Software Testing, Verification and
Validation (ICST).
[6] Andrea Arcuri, Omur Sahin, and Man Zhang. 2025. Fuzzing for Detecting Access Policy Violations in
REST APIs. In IEEE International Symposium on Software Reliability Engineering (ISSRE).
[7] AndreaArcuri,ManZhang,AsmaBelhadi,BogdanMarculescu,AmidGolmohammadi,JuanPabloGaleotti,
and Susruthan Seran. 2023. Building an open-source system test generation tool: lessons learned and
empirical analyses with EvoMaster. Software Quality Journal (2023), 1--44.
[8] Andrea Arcuri, Man Zhang, Amid Golmohammadi, Asma Belhadi, Juan P Galeotti, Bogdan Marculescu,
and Susruthan Seran. 2023. EMB: A curated corpus of web/enterprise applications and library support
for software testing research. In 2023 IEEE Conference on Software Testing, Verification and Validation
(ICST). IEEE, 433--442.
[9] Andrea Arcuri, Man Zhang, Susruthan Seran, Asma Belhadi, Juan Pablo Galeotti, Bogdan, Amid Golmo-
hammadi,OnurDuman,Philip,AgustinaAldasoro,O¨mu¨rS¸ahin,MohsenTaheriShalmani,FrancoCastagna,
Alberto Mart´ın L´opez, Hernan Ghianni, aszyrej, Miguel Rodriguez, Franco Nicol´as Castagna, Lucas Mas
Roca, IvaK, Annibale Panichella, Kyle Niemeyer, and Marcello Maugeri. 2026. WebFuzzing/EvoMaster:
v5.0.2. https://doi.org/10.5281/zenodo.18262322
[10] Andrea Arcuri, Man Zhang, Susruthan Seran, Juan Pablo Galeotti, Amid Golmohammadi, Onur Duman,
Agustina Aldasoro, and Hernan Ghianni. 2025. Tool report: EvoMaster—black and white box search-based
fuzzing for REST, GraphQL and RPC APIs. Automated Software Engineering 32, 1 (2025), 1--11.
[11] Andrea Arcuri, Man Zhang, Susruthan Seran, Juan P. Galeotti, Amid Golmohammadi, Philip Garrett,
OmurSahin, MohsenTaherShalmani, FrancoCastagna, IvaKertusha, FannyFebrianiSusilo, GuruPrasad
Bhandari, Gebremariam Assres, and Jefferson Seide Moll´eri. 2026. EvoMaster at REST League 2026 Tool
Competition. In 19th Search-Based and Fuzz Testing Workshop (SBFT ’26).
15https://github.com/WebFuzzing/EvoMaster
16https://github.com/WebFuzzing/Dataset
29

[12] Andrea Arcuri, Man Zhang, O¨mu¨r S¸ahin, Amid Golmohammadi, Asma Belhadi, Susruthan Seran, Onur
Duman,JuanPabloGaleotti,GebremariamMesfinAssres,andHernanGhianni.2026. WebFuzzing/Dataset:
v4.1.0. https://doi.org/10.5281/zenodo.18196038
[13] Vaggelis Atlidakis, Patrice Godefroid, and Marina Polishchuk. 2019. RESTler: Stateful REST API Fuzzing.
In ACM/IEEE International Conference on Software Engineering (ICSE). 748–758.
[14] Vaggelis Atlidakis, Patrice Godefroid, and Marina Polishchuk. 2020. Checking security properties of cloud
service rest apis. In IEEE International Conference on Software Testing, Verification and Validation
(ICST). IEEE, 387--397.
[15] Benjamin Aziz, Mohamed Bader, and Cerana Hippolyte. 2016. Search-based sql injection attacks testing
using genetic programming. In Genetic Programming: 19th European Conference, EuroGP 2016, Porto,
Portugal, March 30-April 1, 2016, Proceedings 19. Springer, 183--198.
[16] Earl T Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz, and Shin Yoo. 2015. The oracle problem in
software testing: A survey. IEEE Transactions on Software Engineering (TSE) 41, 5 (2015), 507--525.
[17] Davide Corradini, Zeno Montolli, Michele Pasqua, and Mariano Ceccato. 2024. DeepREST: Automated
Test Case Generation for REST APIs Exploiting Deep Reinforcement Learning. In Proceedings of the 39th
IEEE/ACM International Conference on Automated Software Engineering. 1383--1394.
[18] Davide Corradini, Michele Pasqua, and Mariano Ceccato. 2023. Automated black-box testing of mass
assignmentvulnerabilitiesinRESTfulAPIs.In2023 IEEE/ACM 45th International Conference on Software
Engineering (ICSE). IEEE, 2553--2564.
[19] Gelei Deng, Zhiyi Zhang, Yuekang Li, Yi Liu, Tianwei Zhang, Yang Liu, Guo Yu, and Dongjin Wang.
2023. {NAUTILUS}: Automated {RESTful}{API} Vulnerability Detection. In 32nd USENIX Security
Symposium (USENIX Security 23). 5593--5609.
[20] Wenlong Du, Jian Li, Yanhao Wang, Libo Chen, Ruijie Zhao, Junmin Zhu, Zhengguang Han, Yijun Wang,
and Zhi Xue. 2024. Vulnerability-oriented testing for restful apis. In 33rd USENIX Security Symposium
(USENIX Security 24). USENIX Association, 739--755.
[21] Myles Foley and Sergio Maffeis. 2025. APIRL: Deep Reinforcement Learning for REST API Fuzzing. In
Thirty-ninth Conference on Artificial Intelligence (AAAI 2025).
[22] Amid Golmohammadi, Man Zhang, and Andrea Arcuri. 2023. Testing RESTful APIs: A Survey. ACM
Transactions on Software Engineering and Methodology (aug 2023). https://doi.org/10.1145/3617175
[23] Zac Hatfield-Dodds and Dmitry Dygalo. 2022. Deriving Semantics-Aware Fuzzers from Web API Schemas.
In 2022 IEEE/ACM 44th International Conference on Software Engineering: Companion Proceedings
(ICSE-Companion). IEEE, 345--346.
[24] Isatou Hydara, Abu Bakar Md Sultan, Hazura Zulzalil, and Novia Admodisastro. 2015. Current state of
research on cross-site scripting (XSS)--A systematic literature review. Information and Software Technology
58 (2015), 170--186.
[25] A. Kieyzun, P.J. Guo, K. Jayaraman, and M.D. Ernst. 2009. Automatic creation of SQL injection and
cross-site scripting attacks. In ACM/IEEE International Conference on Software Engineering (ICSE).
199--209.
[26] Myeongsoo Kim, Saurabh Sinha, and Alessandro Orso. 2023. Adaptive rest api testing with reinforcement
learning. In 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE).
IEEE, 446--458.
[27] Myeongsoo Kim, Saurabh Sinha, and Alessandro Orso. 2025. LlamaRestTest: Effective REST API Testing
with Small Language Models. In ACM Symposium on the Foundations of Software Engineering (FSE).
[28] Myeongsoo Kim, Tyler Stennett, Saurabh Sinha, and Alessandro Orso. 2025. A Multi-Agent Approach for
REST API Testing with Semantic Graphs and LLM-Driven Inputs. ACM/IEEE International Conference
on Software Engineering (ICSE) (2025).
[29] Myeongsoo Kim, Qi Xin, Saurabh Sinha, and Alessandro Orso. 2022. Automated Test Generation for
REST APIs: No Time to Rest Yet. In Proceedings of the 31st ACM SIGSOFT International Symposium
on Software Testing and Analysis (ISSTA 2022). Association for Computing Machinery, New York, NY,
USA, 289–301. https://doi.org/10.1145/3533767.3534401
30

[30] Nuno Laranjeiro, Jo˜ao Agnelo, and Jorge Bernardino. 2021. A black box tool for robustness testing of
REST services. IEEE Access 9 (2021), 24738--24754.
[31] Muyang Liu, Ke Li, and Tao Chen. 2020. DeepSQLi: Deep semantic learning for testing SQL injection.
In Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis.
286--297.
[32] Yi Liu, Yuekang Li, Gelei Deng, Yang Liu, Ruiyuan Wan, Runchao Wu, Dandan Ji, Shiheng Xu, and
Minli Bao. 2022. Morest: Model-based RESTful API Testing with Execution Feedback. In ACM/IEEE
International Conference on Software Engineering (ICSE).
[33] Chenyang Lyu, Jiacheng Xu, Shouling Ji, Xuhong Zhang, Qinying Wang, Binbin Zhao, Gaoning Pan, Wei
Cao, Peng Chen, and Raheem Beyah. 2023. MINER: A Hybrid Data-Driven Approach for REST API
Fuzzing. In 32nd USENIX Security Symposium (USENIX Security 23). 4517--4534.
[34] Bogdan Marculescu, Man Zhang, and Andrea Arcuri. 2022. On the Faults Found in REST APIs by
Automated Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM) 31,
3 (2022), 1--43.
[35] Evan Martin, Tao Xie, and Ting Yu. 2006. Defining and measuring policy coverage in testing access control
policies. In Information and Communications Security: 8th International Conference, ICICS 2006, Raleigh,
NC, USA, December 4-7, 2006. Proceedings 8. Springer, 139--158.
[36] Alberto Martin-Lopez, Sergio Segura, and Antonio Ruiz-Cort´es. 2019. Test coverage criteria for RESTful
web APIs. In Proceedings of the 10th ACM SIGSOFT International Workshop on Automating TEST Case
Design, Selection, and Evaluation. 15--21.
[37] Alberto Martin-Lopez, Sergio Segura, and Antonio Ruiz-Cort´es. 2021. RESTest: Automated Black-Box
Testing of RESTful Web APIs. In ACM Int. Symposium on Software Testing and Analysis (ISSTA). ACM,
682--685.
[38] Emil Marian Pasca, Daniela Delinschi, Rudolf Erdei, and Oliviu Matei. 2025. LLM-Driven, Self-Improving
Framework for Security Test Automation: Leveraging Karate DSL for Augmented API Resilience. IEEE
Access (2025).
[39] AlexanderPoth,OlsiRrjolli,andAndreaArcuri.2025. Technologyadoptionperformanceevaluationapplied
to testing industrial REST APIs. Automated Software Engineering 32, 1 (2025), 5.
[40] Thomas Rooijakkers, Anne Nijsten, Cristian Daniele, Erieke Weitenberg, Ringo Groenewegen, and
Arthur Melissen. 2025. WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing. arXiv preprint
arXiv:2512.15554 (2025).
[41] Omur Sahin, Man Zhang, and Andrea Arcuri. 2025. WFC/WFD: Web Fuzzing Commons, Dataset
and Guidelines to Support Experimentation in REST API Fuzzing. arXiv:cs.SE/2509.01612 https:
//arxiv.org/abs/2509.01612
[42] Ailton Santos Filho, Ricardo J Rodr´ıguez, and Eduardo L Feitosa. 2025. Automated broken object-level
authorization attack detection in REST APIs through OpenAPI to colored petri nets transformation.
International Journal of Information Security 24, 2 (2025), 83.
[43] Hassan Sartaj, Shaukat Ali, and Julie Marie Gjøby. 2024. REST API Testing in DevOps: A Study on an
Evolving Healthcare IoT Application. arXiv:cs.SE/2410.12547 https://arxiv.org/abs/2410.12547
[44] Susruthan Seran, Guru Prasad Bhandari, and Andrea Arcuri. 2026. Detecting Server-Side Request Forgery
(SSRF) Vulnerabilities In REST API Fuzz Testing. In 19th Search-Based and Fuzz Testing Workshop
(SBFT ’26).
[45] Emanuele Viglianisi, Michael Dallago, and Mariano Ceccato. 2020. RESTTESTGEN: Automated Black-
Box Testing of RESTful APIs. In IEEE International Conference on Software Testing, Verification and
Validation (ICST). IEEE.
[46] Yu Wang and Yue Xu. 2024. Beyond REST: Introducing APIF for Comprehensive API Vulnerability
Fuzzing. In Proceedings of the 27th International Symposium on Research in Attacks, Intrusions and
Defenses. 435--449.
[47] Huayao Wu, Lixin Xu, Xintao Niu, and Changhai Nie. 2022. Combinatorial Testing of RESTful APIs. In
ACM/IEEE International Conference on Software Engineering (ICSE).
31

[48] Man Zhang and Andrea Arcuri. 2023. Open Problems in Fuzzing RESTful APIs: A Comparison of
Tools. ACM Transactions on Software Engineering and Methodology (TOSEM) (may 2023). https:
//doi.org/10.1145/3597205
[49] Man Zhang, Andrea Arcuri, Yonggang Li, Yang Liu, and Kaiming Xue. 2023. White-Box Fuzzing RPC-
Based APIs with EvoMaster: An Industrial Case Study. ACM Transactions on Software Engineering and
| Methodology | 32, 5 (2023), | 1--38. |     |     |
| ----------- | ------------- | ------ | --- | --- |
[50] Man Zhang, Andrea Arcuri, Yonggang Li, Yang Liu, Kaiming Xue, Zhao Wang, Jian Huo, and Weiwei
Huang.2025. Fuzzingmicroservices: Aseriesofuserstudiesinindustryonindustrialsystemswithevomaster.
| Science of | Computer | Programming (2025), | 103322. |     |
| ---------- | -------- | ------------------- | ------- | --- |
[51] Man Zhang, Andrea Arcuri, Piyun Teng, Kaiming Xue, and Wenhao Wang. 2024. Seeding and Mocking in
White-BoxFuzzingEnterpriseRPCAPIs: AnIndustrialCaseStudy.InProceedingsofthe39thIEEE/ACM
| International | Conference | on Automated | Software Engineering. | 2024--2034. |
| ------------- | ---------- | ------------ | --------------------- | ----------- |
32
