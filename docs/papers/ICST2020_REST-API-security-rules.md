> 원본: ICST2020_REST-API-security-rules.pdf; 변환: markitdown; 2026-10-06

<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->

Checking Security Properties of
Cloud Service REST APIs
Vaggelis Atlidakis∗ Patrice Godefroid Marina Polishchuk
Columbia University Microsoft Research Microsoft Research
Abstract—Most modern cloud and web services are program- in order to thoroughly exercise the cloud service deployed
matically accessed through REST APIs. This paper discusses behindthatAPI,withthegoaloffindingunhandledexceptions
how an attacker might compromise a service by exploiting (service crashes) that can be detected by a test client as “500
vulnerabilitiesinitsRESTAPI.Weintroducefoursecurityrules
Internal Server Errors”. While that work looks promising and
that capture desirable properties of REST APIs and services.
We then show how a stateful REST API fuzzer can be extended reports many new bugs found, its scope is restricted to the
with active property checkers that automatically test and detect detection of unhandled exceptions.
violations of these rules. We discuss how to implement such In this paper, we introduce four security rules that capture
checkersinamodularandefficientway.Usingthesecheckers,we
desirable properties of REST APIs and services.
foundnewbugsinseveraldeployedproductionAzureandOffice-
365cloudservices,andwediscusstheirsecurityimplications.All • Use-after-free rule. A resource that has been deleted
these bugs have been fixed. must no longer be accessible.
Keywords-Test generation; Security; Cloud and Web services; • Resource-leak rule. A resource that was not created
REST APIs successfully must not be accessible and must not “leak”
any side-effect in the backend service state.
I. INTRODUCTION
• Resource-hierarchy rule. A child resource of a parent
Cloud computing is exploding. Over the last few years, resource must not be accessible from another parent
thousandsofnewcloudserviceshavebeendeployedbycloud resource.
platform providers, like Amazon Web Services [2] and Mi- • User-namespace rule. A resource created in a user
crosoft Azure [13], and by their customers who are “digitally namespace must not be accessible from another user
transforming” their businesses by modernizing their processes namespace.
while collecting and analyzing all kinds of new data.
Violationsofsuchrulesmightallowanattackertohijackcloud
Today, most cloud services are programmatically accessed
resources or bypass quotas (Elevation-of-Privilege attack), or
through REST APIs [9]. REST APIs are implemented on
to steal information from other users (Information-Disclosure
top of the ubiquitous HTTP/S protocol, and offer a uni-
attack), or to corrupt the backend service state so that it no
form way to create (PUT/POST), monitor (GET), manage
longer operates properly (Denial-of-Service attack), as will be
(PUT/POST/PATCH) and delete (DELETE) cloud resources.
discussed later.
Cloud service developers can document their REST APIs and
We show how a stateful REST API fuzzer can be extended
generate sample client code by describing their APIs using
to test and detect violations of such rules. For each rule, we
an interface-description language such as Swagger (recently
defineanactivepropertycheckerwhich(1)generatesnewAPI
renamed OpenAPI) [25]. A Swagger specification describes
requeststotestspecificruleviolationsand(2)detectsanysuch
howtoaccessacloudservicethroughitsRESTAPI,including
rule violation. In other words, each checker actively tries to
what requests the service can handle, what responses may be
break its rule in addition to monitoring for any rule violation.
received, and the response format.
Wediscusshowtoimplementsuchcheckersinamodularway,
How secure are all those APIs? Today, this question is still
so that checkers do not interfere with each other. Since each
largely open. Tools for automatically testing cloud services
checker generates new tests, in addition to an already-large
via their REST APIs and checking whether these services
statespaceexploration,wealsodiscusshowtoimplementeach
are reliable and secure are still in their infancy. Some tools
individual checker efficiently, by eliminating likely-redundant
available for testing REST APIs capture live API traffic,
tests whenever possible.
and then parse, fuzz, and replay the traffic with the hope
By construction, these checkers can find security rule vio-
of finding bugs [4], [21], [6], [26], [3]. Recently, stateful
lations beyond the “500 Internal Server Errors” that can be
REST API fuzzing [5] was proposed to specifically test more
detected by baseline stateful REST API fuzzing. Using these
deeplyservicesdeployedbehindRESTAPIs.GivenaSwagger
checkers, we found new bugs in several production Azure
specification of a REST API, this approach automatically
and Office-365 cloud services. The use of security checkers
generates sequences of requests, instead of single requests,
increases the value of REST API fuzzing by detecting more
types of bugs at a modest incremental testing cost.
∗The work of this author was mostly done while visiting Microsoft
Research. This paper makes the following contributions:

• We introduce rules that describe security properties of delete. The request body b may include additional parameters
REST APIs. and their values that may be required or optional for the
• We design and implement active checkers to test and request to be executed successfully.
detect violations of these rules. For instance, here is a request to get the properties of a
• We present detailed experimental results evaluating the specific Azure DNS zone [14] (shown on multiple lines):
performance and effectiveness of these active checkers (cid:104) User-auth-token (cid:105) GET
on three production cloud services. https://management.azure.com/
• With these checkers, we found new bugs in several
subscriptions/{subscriptionId}/
production Azure and Office-365 cloud services, and we
resourceGroups/{resourceGroupName}/
providers/Microsoft.Network/
discuss their security implications.
dnsZones/{zoneName}
The rest of the paper is organized as follows. In Sec-
?api-version=2018-03-01 { }
tion II, we recall background information on stateful REST
This request is of type GET, its path requires three
API fuzzing. In Section III, we introduce rules that capture
resource names, namely a subscriptionID, a
desirable properties of secure REST APIs and present active
resourceGroupName, and a zoneName, and its body (at
checkers to test and detect violations of these rules. In Sec-
the end) denoted by { } is empty.
tion IV, we present experimental results with active checkers
REST API requests of type PUT or POST typically cre-
on production cloud services. In Section V, we discuss new
ate new resources, while DELETE requests destroy existing
bugs found by these checkers and their security implications.
resources. A request whose execution creates a new resource
In Section VI, we discuss related work, and we conclude the
of type T is called a producer for the resource type T. A
paper in Section VII.
newly created resource is represented by its identifier, or
II. STATEFULRESTAPIFUZZING id for short. Because resources are dynamically created, we
Inthissection,werecallthedefinitionofstatefulRESTAPI will sometimes call them dynamic objects. A request which
fuzzing [5],beforeintroducinginSectionIIIsecurityproperty requiresaresourcenameoftypeT initspathorinitsbodyis
checkers that can be implemented as extensions of this basic calledaconsumerfortheresourcetypeT.Wewillsometimes
scheme. refer to the resource name of type T as the dynamic object
We consider cloud services accessible through REST APIs. type.IntheAzureDNSzoneexampleabove,theGETrequest
Aclientprogramsendsmessages,calledrequests,toaservice shown consumes three resources of type subscriptions,
and receives messages back, called responses. Such messages resourceGroups, and dnsZones respectively, but does
aresentovertheHTTP/Sprotocol.Eachresponseisassociated not produce any new resource.
with a single HTTP status code which is either in the 2xx, Inside resource paths or request bodies of individual re-
3xx, 4xx or 5xx ranges. quests,theuserisallowedtospecifythatsomespecificvalues,
Swagger [25], also known as OpenAPI, is an example called fuzzable values, are to be chosen randomly among a
of specification language to define REST APIs. A Swagger (small finite) set of specific values. For instance, a user might
specification describes how to access a service through its specify that a given integer value in the body of a request
REST API, including what requests the service can handle, may be, say, either 0, 10, 1000000, or -10. Such a set
what responses may be received, and the respective response of values is called a fuzzing dictionary. Given a request with
format. fuzzablevalues,arenderingofthatrequestdenotesamapping
We define a REST API as a finite set of requests. Each of each fuzzable value to a single concrete value selected in
request r is a tuple of the form (cid:104)a,t,p,b(cid:105) where its fuzzing dictionary. Thus, a request with n fuzzable values
• a is an authentication token, which can each take k possible values results in nk possible
renderings. A rendering is called valid if the execution of the
• t is the request type,
corresponding request returns a valid response (defined in the
• p is a resource path, and
next paragraph). Users are responsible for identifying values
• b is the request body.
they want to fuzz and their associated fuzzing dictionaries.
A request type t is any of the following five REST-allowed
We define the state space of a service as a directed graph
values:PUT(createorupdate),POST(createorupdate),GET
where nodes represent service states and edges are transitions
(read, list or query), DELETE (delete), PATCH (update). The
between these. Given a state s of the service, executing a
resource path p is a string identifying a cloud resource and single request r leads to a successor state s(cid:48): this execution is
its parent hierarchy. Typically, p is a (non-empty) sequence denotedbys→ r s(cid:48).Theexecutionofarequestr inastatesis
matching the regular expression
eithervalidifittriggersa2xxresponse,invalidifittriggersa
(/(cid:104)resourceType(cid:105)/(cid:104)resourceName(cid:105)/)+ 3xx or 4xx response, or a bug if it triggers a 5xx response.
where resourceType denotes the type of a cloud resource Given an initial state where no resources exist, the state
and resourceName is the specific name of the resource of space of the service reachable from that initial state can
that type. The last resource named in the path is typically be explored by executing sequences of requests. Such an
the specific resource that the request tries to create, access, or explorationisstatefulwhenitattemptstoexploreservicestates

that are reachable only using sequences of multiple requests: must fail and thus return a “404 Not Found” HTTP status
earlier requests in a sequence may produce resources that are code in their response.
consumed in subsequent requests in that sequence in order to A use-after-free violation occurs when a resource that has
exercise more requests and reach deeper service states. been deleted still remains accessible through the API. This
State-space exploration can be performed using various mustneverhappen.Itisaclearbugthatmayleadtobypassing
search strategies, e.g., a systematic breadth-first search or a resource quotas and corrupting the service backend state.
randomsearch[5].Statespacescanbelarge,eveninfinite,be- Resource-leak rule. A resource that was not successfully
causethelengthofrequestsequencesisnotbounded,because created must not be accessible, and must not “leak” any
the sets of possible renderings can be very large, and because associated resources in the backend service state. In other
the service under test is viewed as a blackbox. Fortunately, words, if the execution of a PUT or POST request to create a
a partial state-space exploration may be sufficient to reveal new resource fails (for any reason), any subsequent operation
interesting bugs. In our context, a bug is defined as a 500 on that resource must also fail with a 4xx response. Fur-
HTTPstatuscodebeingreceivedasaresponseafterexecuting thermore, no side-effects associated with successful creation
a request sequence. Such “500 Internal Server Errors” are of that resource type must occur in the backend service state
unhandled exceptions triggered by unexpected input request and be visible to the user. For instance, a failed-to-be-created
sequences, which may corrupt the service state and severely resource must not be counted in the user’s resource counter
damage the service health: it is safer to fix such bugs rather towards service quotas, and the name of the failed-to-be-
than risk a live incident with unknown consequences. created resource must be reusable by the user.
In what follows, we will sometimes use the term test cases As an example, after issuing a malformed PUT request to
to refer to executions of request sequences, while tests refer create URI /users/user-id1, a 4xx response must be
to executions of single requests. We will also call the general received. Any subsequent request to access (read, update, or
state-space exploration algorithm of this section the main delete) this URI must also fail.
driver of stateful REST API fuzzing. A resource-leak violation occurs when a resource that was
not successfully created nevertheless “leaks” some side-effect
III. SECURITYCHECKERSFORRESTAPIS
inthebackendservicestate.Forinstance,theresourcemaybe
In this section, we define and describe active checkers listed by a subsequent GET request, yet it cannot be deleted
for security rules of REST APIs. First, in Section III-A, we with a DELETE request, or subsequent attempts to re-create
introduce four REST API security rules. In Section III-B, we thisresourcereturn“409Conflict”responses.Suchviolations
describe how to implement active checkers for testing and mustneverhappen,astheymayhaveunintendedconsequences
detecting security rule violations. Each active checker focuses on the capacity for that resource type (e.g., if resource quota
onasingletypeofsecurityruleviolation.InSectionIII-C,we limits are reached and no new resources can be created) and
discuss how each checker can be combined in a modular way on the performance of the service (e.g., due to unnecessarily
with the other checkers and with the main driver of stateful large database tables).
RESTAPIfuzzing.InSectionIII-D,weproposeanewsearch Resource-hierarchy rule. A child resource of a parent
strategy for scalable test generation with property checkers. resource must not be accessible from another parent
In Section III-E, we describe how to group together checker resource. In other words, if a resource child is
violations in order to avoid reporting the same bug multiple successfully created from a resource parent and
times to the user. identified as such in service resource paths of the form
(cid:104)parentType(cid:105)/parent/(cid:104)childType(cid:105)/child/, the
A. Security Rules
child resource must not be accessible (i.e., must not be
We introduce four security rules that capture desirable successfully read, updated or deleted) when substituting the
properties of REST APIs and services. We illustrate each rule parent resource by any other parent resource.
withanexampleanddiscussitssecurityimplications.Allfour For example, after issuing POST requests to URIs
rulesareinspiredbypastrealbugsindeployedcloudservices, /users/user-id1, /users/user-id2, and
which were found either by manual penetration testing or by /users/user-id1/reports/report-id1 to create
rootcauseanalysisofcustomer-visibleincidents.Examplesof users user-id1, user-id2, and then add report
new, previously-unknown bugs we found as rule violations report-id1 to user user-id1, subsequent requests
in deployed production Azure and Office-365 services are to URI /users/user-id2/reports/report-id1
presented later in Section V. must fail since, according to the resource-hierarchy rule,
Use-after-free rule. A resource that has been deleted must report report-id1 belongs to user user-id1 but not to
no longer be accessible. In other words, after a successful user user-id2.
DELETEoperationonanyresource,anysubsequentoperation A resource-hierarchy violation occurs when a sub-resource
– like read, update, or delete – on that resource must fail. originally created from a parent resource is accessible from
For example, after issuing a DELETE request to URI a different parent resource with no parent-child relation-
/users/user-id1inordertodeletetheaccountwithiden- ship. When such violations are possible, an attacker might
tifier user-id1, all subsequent attempts to use user-id1 be able to provide an unauthorized parent object identifier

1 Inputs:seq,global cache,reqCollection 1 Inputs:seq,global cache,reqCollection
2 #Retrievetheobjecttypesconsumedbythelastrequestand 2 #Retrievetheobjecttypesproducedbythewholesequenceandby
3 #locallystorethemostrecentobjectidofthelastobjecttype. 3 #thelastrequestseparatelytoperformtypecheckinglateron.
4 n=seq.length 4 seq obj types=PRODUCES(seq)
5 req obj types=CONSUMES(seq[n]) 5 target obj types=PRODUCES(seq[−1])
6 #Onlytheidofthelastobjectiskept,sincethisisthe 6 fortarget obj typeintarget obj types:
7 #objectactuallydeleted. 7 forguessed valueinGUESS(target obj type):
8 target obj type=req obj types[−1] 8 global cache[target obj type]=guessed value
9 target obj id=global cache[target obj type] 9 forreqinreqCollection:
10 #Usethelatestvalueofthedeletedobjectandexecute 10 #Skipconsumersthatdon’tconsumethetargettype.
11 #anyrequestthattype−checks. 11 ifCONSUMES(req)!=target obj type:
12 forreqinreqCollection: 12 continue
13 #Onlyconsiderrequeststhattypecheck. 13 #Skiprequeststhatdon’ttypecheck.
14 iftarget obj typenotinCONSUMES(req) 14 ifCONSUMES(req)−seq obj types:
15 continue 15 continue
16 #Restoreidofdeletedobject. 16 #Executetherequestaccessingthe’’guessed’’objectid.
17 global cache[target obj type]=target obj id 17 EXECUTE(req)
18 #Executerequestondeletedobject. 18 assert’’HTTPstatuscodein4xxclass’’
19 EXECUTE(req) 19 ifmode!=’exhaustive’:
20 assert’’HTTPstatuscodeis4xx’’ 20 break
21 ifmode!=’exhaustive’: Fig. 2: Resource-leak checker.
22 break
Fig. 1: Use-after-free checker. We enforce the first principle by running all the checkers
whenever the main driver has finished executing a new test
(e.g., user-id3), and then steal (read) or hijack (write)
case.Weenforcethesecondprinciplebyprioritizingtheorder
an unauthorized child object (e.g., report-id1). Resource-
of applying checkers based on their semantics, so that they
hierarchy violations are clear bugs, are potentially dangerous,
operate on different test cases and do not interfere with each
and must never happen.
other (more on this later in this section). In what follows,
User-namespacerule.Aresourcecreatedinausernamespace
we present implementation details of each checker as well as
must not be accessible from another user namespace. In the
optimizations to limit state-space explosion.
context of REST APIs, we consider user namespaces defined
Use-after-free checker. The implementation of the use-after-
by the user token used to interact with the API (e.g., OAUTH
free rule checker is described in Figure 1 in python-like
token-based authentication [18]).
For example, after issuing a POST request to create URI notation.Thealgorithmiscalledafterthemaindriverexecutes
/users/user-id1 using token token-of-user-id1, a DELETE request (see Figure 4) and takes three inputs:
resource user-id1 must not be accessible using another a sequence seq of requests, which is the latest test case
token token-of-user-id2 of another user. executed by the main driver; the global cache of dynamic
objects, denoted global_cache, which contains the most
Ausernamespaceviolationoccurswhenaresourcecreated
recent object types and ids for the dynamic objects created so
withinthenamespaceofoneuserisaccessiblefromwithinthe
far; and the request collection, denoted reqCollection,
namespace of another user. If such a violation ever occurs, an
which is the set of all available API requests.
attackermightbeabletoexecuteRESTAPIrequestsusingan
unauthorized authentication token, and perform unauthorized First, the types of the dynamic objects consumed by the
operations on resources belonging to another (victim) user. last request are retrieved (line 5) and the id of the last
object type, denoted target_obj_type, is stored in a
B. Active Checkers temporaryvariable,denotedtarget_obj_id.Althoughthe
We implement active checkers for the rules defined in last request may be consuming more than one object type, we
Section III-A. An active checker monitors the state space consider the last type in req_object_types as the actual
exploration performed by the main driver of stateful REST typeofthedeletedobject.(Forexample,aDELETErequeston
API fuzzing and suggests new tests to assert that specific the URI /users/userId1/reports/reportId1 con-
rules are not violated. Thus, an active checker augments the sumes two object types (users and reports) but only deletes
search space by executing new tests targeted at violating report objects.) After this initial setup, the for-loop (line 12)
specific rules. In contrast, a passive checker monitors the iterates over all requests available in reqCollection and
search performed by the main driver without executing new skipsthosethatdonotconsumethetargetobjecttype(line14).
tests. Once a request, req, that consumes the target object type is
Wedesignactivecheckersfollowingamodulardesignbased found, the target object id is restored in the global cache of
on two principles: dynamicobjects(line17)andisthereforeusedbythefunction
1) Checkers are independent from the main driver of state- EXECUTE (line 19) which executes request req. Note that
ful REST API fuzzing and do not affect its state space the target object id is repeatedly restored in the global cache
exploration. because the function EXECUTE uses object ids available in
2) Checkers are independent from each other and generate global_cache when executing a request. If any of these
tests by analyzing the requests executed by the main requestssucceeds,line20willtriggerause-after-freeviolation
driver, excluding those executed by other checkers. (see Section III-A).

1 Inputs:seq,global cache 1 Inputs:seq,global cache,reqCollection
2 #Recordtheobjecttypesconsumedbythelastrequest 2 #Executethecheckersafterthemaindriver.
| 3 #aswellasthoseofallpredecessorrequests. |     |     |     |     |     | 3 n=seq.length  |     |                   |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | --- | --- | --- |
| 4 n=seq.length                            |     |     |     |     |     | 4 ifseq[n].http |     | type==’’DELETE’’: |     |     |     |     |     |
5 last request=seq[n] 5 UseAfterFreeChecker(seq,global cache,reqCollection)
| 6 target obj | types=CONSUMES(seq[n]) |     |     |     |     | 6 else: |     |     |     |     |     |     |     |
| ------------ | ---------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
7 predecessor obj types=CONSUMES(seq[:n]) 7 ifseq[n].http response==’’4xx’’:
8 #Retrievethemostrecentidofeachchildobjectconsumed 8 ResourceLeakChecker(seq,global cache,reqCollection)
| 9 #onlybythelastrequest.Thesearetheobjectswhose |     |     |     |     |     | 9 else: |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
10 #hierarchywewilltrytoviolate. 10 ResourceHierarchyChecker(seq,global cache)
| 11 local cache={} |     |     |     |     |     | 11  | UserNamespaceChecker(seq,global |     |     |     | cache) |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ------ | --- | --- |
12 forobj typeintarget obj types−predecessor obj types: Fig. 4: Checkers dispatcher.
| 13 local | cache[obj | type]=global | cache[obj | type] |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ------------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14 #Rendersequenceuptobeforethelastrequest
|     |     |     |     |     |     | trigger a | resource-leak |     | violation | (see Section |     | III-A) or | asserts |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --------- | ------------ | --- | --------- | ------- |
15 EXECUTE(seq,n−1)
|     |     |     |     |     |     | that no | such violation |     | occurs | for the | given request |     | sequence |
| --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------ | ------- | ------------- | --- | -------- |
16 #RestoreoldchildrenobjectidsthatdoNOTbelongto
(line 18).
17 #thecurrentparentidsandmustNOTbeaccessiblefromthose.
| 18 forobj       | typeinlocal | cache:      |           |       |     |            |          |             |           |            |            |              |          |
| --------------- | ----------- | ----------- | --------- | ----- | --- | ---------- | -------- | ----------- | --------- | ---------- | ---------- | ------------ | -------- |
|                 |             |             |           |       |     | Finally,   | in       | order to    | limit     | the number | of         | additional   | tests    |
| 19 global       | cache[obj   | type]=local | cache[obj | type] |     |            |          |             |           |            |            |              |          |
|                 |             |             |           |       |     | generated  | for each | input       | sequence, | the        | inner loop | (optionally) |          |
| 20 EXECUTE(last |             | request)    |           |       |     |            |          |             |           |            |            |              |          |
|                 |             |             |           |       |     | terminates | when     | one request |           | for each   | guessed    | object       | is found |
21 assert’’HTTPstatuscodeis4xx’’
Fig. 3: Resource-hierarchy checker. (line 19). We evaluate this optimization in Section IV.
|     |     |     |     |     |     | Resource-hierarchy |     | checker. |     | The | implementation |     | of the |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | --- | -------------- | --- | ------ |
Finally,inordertolimitthenumberofadditionaltestsgen-
|            |      |                   |     |       |                   | resource-hierarchy |       | rule        | checker | is described | in           | Figure | 3. The  |
| ---------- | ---- | ----------------- | --- | ----- | ----------------- | ------------------ | ----- | ----------- | ------- | ------------ | ------------ | ------ | ------- |
| erated for | each | request sequence, | the | inner | loop (optionally) |                    |       |             |         |              |              |        |         |
|            |      |                   |     |       |                   | algorithm          | takes | two inputs: | a       | sequence     | of requests, |        | denoted |
terminates when one request for each target object type is seq, which is the latest test case executed by the main driver
found(line21).Thisoptionisusedifthevariablemodeisnot
|     |     |     |     |     |     | and the | current | global | cache | of dynamic | objects, |     | denoted |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ----- | ---------- | -------- | --- | ------- |
set to value exhaustive. We present detailed experimental global_cache.First,thealgorithmrecordstheobjecttypes
resultsregardingtheimpactofthisoptimizationinSectionIV.
|     |     |     |     |     |     | consumed | by  | the last | request | of the | current | sequence, | de- |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------- | ------ | ------- | --------- | --- |
Resource-leak checker. The resource-leak rule checker is noted target_obj_types (line 6), and the object types
described in Figure 2. The algorithm takes the same three consumed by all other requests of the sequence before the
inputs as the use-after-free checker. This checker operates on last request, denoted predecessor_obj_types (line 7).
request sequences executed by the main driver whose last Afterwards, the ids of the objects consumed only by the last
| request led | to an | invalid | HTTP status | code | in the response |         |            |         |        |     |          |       |         |
| ----------- | ----- | ------- | ----------- | ---- | --------------- | ------- | ---------- | ------- | ------ | --- | -------- | ----- | ------- |
|             |       |         |             |      |                 | request | are stored | locally | (lines | 12  | and 13). | These | are the |
(see Figure 4). Initially, the algorithm identifies the dy- child objects whose hierarchy the checker will try to violate
namic object types produced by the whole sequence, denoted by executing requests that try to access them using invalid
seq_obj_types,andproducedbythelastrequest,denoted
|     |     |     |     |     |     | parent objects. |     | To this | end, in | line 15, | the current |     | sequence |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | ------- | -------- | ----------- | --- | -------- |
target_obj_types (lines 4 and 5). The main logic of is executed up to (and not including) the last request. Finally,
| the algorithm | is  | implemented | in three | nested | for loops. The |         |              |     |              |        |     |         |         |
| ------------- | --- | ----------- | -------- | ------ | -------------- | ------- | ------------ | --- | ------------ | ------ | --- | ------- | ------- |
|               |     |             |          |        |                | the old | child object | ids | are restored | (lines | 18  | and 19) | and the |
first loop (line 6) iterates over all object types produced by last request is executed using the old child object ids on top
the last request. The second loop (line 7) iterates over object of new parent object ids (line 20). These parent object ids
| ids “guessed” | for | the current | object | type for | which an invalid |         |        |                |     |                 |     |              |      |
| ------------- | --- | ----------- | ------ | -------- | ---------------- | ------- | ------ | -------------- | --- | --------------- | --- | ------------ | ---- |
|               |     |             |        |          |                  | are not | proper | parent objects |     | of the restored |     | child object | ids. |
HTTPstatuscodewasreceived.ThefunctionGUESStakesas This way, the algorithm tries to trigger a resource-hierarchy
argumentanobjecttypeandreturnsasetofpossibleobjectids
|     |     |     |     |     |     | violation | (see | Section | III-A) | or asserts | that no | such | violation |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ------- | ------ | ---------- | ------- | ---- | --------- |
matching this type and which were not created successfully. occurs for the given request sequence (line 21).
For instance, if the creation of a dynamic object with object User-namespacechecker.Duetospaceconstraints,weomita
type“x”andobjectid“objx1”failsthroughtheAPI(according
detailedpresentationofthischecker.Inanutshell,thischecker
to the response received), the checker will attempt to execute attempts to re-execute the valid last request of any test case
anyrequestthatconsumestheobjecttype“x”andassertitfails executed by the main driver using a different authentication
when using the object id “objx1”. Note that the total number token. If this succeeds, an attacker with a different authenti-
of guessed values per object id is limited to a user-provided cation token could hijack the objects used in the last request,
| parameter | value | in order | to avoid an | explosion | in the number |     |     |     |     |     |     |     |     |
| --------- | ----- | -------- | ----------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andausernamespaceviolation(seeSectionIII-A)isreported.
| of additional | tests. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In line 8, a guessed object-id value is temporarily added C. Combining All Checkers
to the global cache of properly-created dynamic objects. The four checkers defined in the previous section are
Then the inner loop (line 9) iterates over all requests in executed as follows. Whenever the stateful REST API fuzzer
reqCollection
to find requests that are executable (given reaches a new state (as defined in Section II), its main driver
the object types produced by the current sequence) and that callsthecodeshowninFigure4.Dependingonthelastrequest
consume the given target object type. These requests are executed, this code activates the checkers that are applicable
executed (line 17) using the “guessed” object ids previously to the current state. We now discuss important properties of
registered inthe globalcache. This way,the algorithm triesto these checkers and of their combination.

Contribution beyond stateful REST API fuzzing. The of length n, instead of to all of them as in BFS [5]. BFS-
checkers extend the main driver of baseline stateful REST Fast provides full grammar coverage only with respect to all
API fuzzing in two ways: (1) they extend the state space by possiblerenderingsofindividualrequestsbutdoesnotexplore
executing additional tests and (2) they check for responses all request sequences of a given sequence length.
other than 5xx and can flag unexpected 2xx responses as Although BFS-Fast scales better compared to BFS, it does
rule-violationbugs.Thus,theyclearlyincreasethebug-finding sobyexploringonlyasubsetofallpossiblerequestsequences.
capabilitiesofthemaindriver:theycanfindbugsthatthemain Unfortunately,thislimitsthenumberofviolationsthesecurity
driver alone would not find. checkers can actively check. To alleviate this limitation, we
Active property checking versus passive monitoring. As introduce a new search strategy, called BFS-Cheap.
discussed earlier, the checkers we define extend the search BFS-Cheap follows the inverse trade-off of BFS-Fast: it
|                |     |        |      |        |                 |     |            | sacrifices | full | coverage | of all | possible | request | renderings | at  |
| -------------- | --- | ------ | ---- | ------ | --------------- | --- | ---------- | ---------- | ---- | -------- | ------ | -------- | ------- | ---------- | --- |
| space explored |     | by the | main | driver | with additional |     | test cases |            |      |          |        |          |         |            |     |
aimed at triggering and detecting specific rule violations. In every state but explores all possible request sequences for a
contrast,passiveruntimemonitoringoftheserulesinconjunc- given sequence length, albeit not with all possible renderings.
tion with the main driver, i.e., without executing those new Specifically, given a set of sequences of length n, called
tests, would likely be unable to detect rule violations. Specif- seqSet, and a set of requests, called reqCollection,
|                        |     |     |                   |     |      |            |       | BFS-Cheap | operates | as  | follows: |     |     |     |     |
| ---------------------- | --- | --- | ----------------- | --- | ---- | ---------- | ----- | --------- | -------- | --- | -------- | --- | --- | --- | --- |
| ically, use-after-free |     |     | and resource-leak |     | rule | violations | would |           |          |     |          |     |     |     |     |
likely not be detected with passive monitoring alone because For each sequence seq ∈ seqSet, append each
the default state space exploration, performed by the main req ∈ reqCollection to the end of seq, execute
driver, would likely not attempt to re-use deleted resources the new sequence while considering the possible
or resources after a failure, respectively. Similarly, resource- renderings of req, and add to seqSet at most
| hierarchy   | and        | user-namespace |            | rule          | violations | would  | not be      |                  |       |          |         |         |                 |           |     |
| ----------- | ---------- | -------------- | ---------- | ------------- | ---------- | ------ | ----------- | ---------------- | ----- | -------- | ------- | ------- | --------------- | --------- | --- |
|             |            |                |            |               |            |        |             | one              | valid | (if any) | and one | invalid | (if any)        | sequence  |     |
| detected    | by passive |                | monitoring | either        | because    | the    | baseline    | rendering.       |       |          |         |         |                 |           |     |
| main driver | does       | not            | attempt    | to substitute |            | object | identifiers |                  |       |          |         |         |                 |           |     |
|             |            |                |            |               |            |        |             | Valid renderings |       | are      | used by | the     | use-after-free, | resource- |     |
or authentication tokens, respectively. In other words, the hierarchy, and user-namespace checkers, while invalid render-
additional test cases generated by the checkers are necessary ings are used by the resource-leak checker.
| to find | rule violations |     | and | are not | redundant | with | respect | to        |     |               |     |                 |     |         |     |
| ------- | --------------- | --- | --- | ------- | --------- | ---- | ------- | --------- | --- | ------------- | --- | --------------- | --- | ------- | --- |
|         |                 |     |     |         |           |      |         | BFS-Cheap |     | thus provides |     | a middle-ground |     | between | BFS |
non-checker tests. and BFS-Fast (see Section IV-B for an experimental eval-
| Complementarity |     | among |     | the checkers. |     | The four | checkers |          |             |     |          |         |           |     |      |
| --------------- | --- | ----- | --- | ------------- | --- | -------- | -------- | -------- | ----------- | --- | -------- | ------- | --------- | --- | ---- |
|                 |     |       |     |               |     |          |          | uation). | It explores | all | possible | request | sequences | up  | to a |
we define complement each other: no two checkers will ever given sequence length (like BFS) and adds at most two new
generate the same new tests, by construction, because their renderings for each sequence in order to avoid an enormous
| preconditions | are | all | mutually | exclusive. |     | First, the | use-after- |        |       |            |     |     |            |              |     |
| ------------- | --- | --- | -------- | ---------- | --- | ---------- | ---------- | ------ | ----- | ---------- | --- | --- | ---------- | ------------ | --- |
|               |     |     |          |            |     |            |            | seqSet | (like | BFS-Fast). | Two | new | renderings | per sequence |     |
freecheckeristheonlycheckeractivatedbyrequestsequences explored allow for active checking of all the security rules
| that end | in a | DELETE | request. | Second, |     | the resource-leak |     |         |            |       |       |             |     |             |        |
| -------- | ---- | ------ | -------- | ------- | --- | ----------------- | --- | ------- | ---------- | ----- | ----- | ----------- | --- | ----------- | ------ |
|          |      |        |          |         |     |                   |     | defined | in Section | III-A | while | maintaining |     | a tractable | number |
checker is the only checker activated when the last request of sequences in seqSet as the sequence length increases.
executed returns an invalid HTTP status code. Third, the Notethatthesuffix“cheap”comesfromthefactBFS-Cheap
| resource-ownership |     | checker |     | is the | only checker | activated | on  |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | --- | ------ | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
isacheaperversionofBFSwhereatmostonevalidrendering
request sequences with valid renderings that do not end in a isaddedtotheBFS“frontier”setSeqforeachnewsequence.
DELETErequest.Fourthandlast,theuser-namespacechecker
|     |     |     |     |     |     |     |     | This leads | to  | the creation |     | of fewer | resources | than | those |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | -------- | --------- | ---- | ----- |
executed tests using an attacker token different from the createdwhenallvalidrenderingsofeachrequestsequenceare
authentication token used by the main driver and all other explored,asinBFS.Forinstance,imaginearequestdefinition
| checkers, | so it | clearly | extends | the | state | space in | another, |         |      |                 |     |     |           |          |        |
| --------- | ----- | ------- | ------- | --- | ----- | -------- | -------- | ------- | ---- | --------------- | --- | --- | --------- | -------- | ------ |
|           |       |         |         |     |       |          |          | with an | enum | type describing |     | ten | different | flavours | of the |
orthogonal dimension. same resource type. BFS-Cheap will stop creating resources
|           |            |     |              |     |     |     |     | once one  | resource | of one        | flavour | is          | successfully | created.  | In     |
| --------- | ---------- | --- | ------------ | --- | --- | --- | --- | --------- | -------- | ------------- | ------- | ----------- | ------------ | --------- | ------ |
| D. Search | Strategies |     | for Checkers |     |     |     |     |           |          |               |         |             |              |           |        |
|           |            |     |              |     |     |     |     | contrast, | BFS      | and BFS-Fast, |         | will create | ten          | resources | of the |
Themainsearchstrategyusedfortestgenerationinstateful same type with ten different flavours.
| REST API     | fuzzing | [5] | is a   | breadth-first | search  | (BFS)      | in the |        |               |     |     |     |     |     |     |
| ------------ | ------- | --- | ------ | ------------- | ------- | ---------- | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- |
|              |         |     |        |               |         |            |        | E. Bug | Bucketization |     |     |     |     |     |     |
| search space | defined |     | by all | possible      | request | sequences. | This   |        |               |     |     |     |     |     |     |
search strategy provides full grammar coverage both with Before discussing examples of real violations found with
respect to all possible renderings of each individual request active checkers, we define the bucketization scheme used to
and with respect to all possible request sequences up to group together similar violations. In the context of active
a given sequence length. However, since the search space checkers, we define “bugs” as rule violations. Each bug is
|          |        |              |     |           |     |            |          | associated | with | the request |     | sequence | that | was executed | to  |
| -------- | ------ | ------------ | --- | --------- | --- | ---------- | -------- | ---------- | ---- | ----------- | --- | -------- | ---- | ------------ | --- |
| explored | by BFS | is typically |     | enormous, |     | the search | does not |            |      |             |     |          |      |              |     |
scale well as the sequence length increases. Therefore, an trigger it. Given this property, we use the following procedure
optimization called BFS-Fast was introduced. With BFS-Fast, to create per-checker bug buckets:
whenever the search depth increases to a new value n+1, Whenever a new bug is found, compute all non-
each request is appended to at most one request sequence empty suffixes of the request sequence that triggers

|        | Total | Search    |     | Max  |             |          |              |       | Checker | Stats     |      |           |     |
| ------ | ----- | --------- | --- | ---- | ----------- | -------- | ------------ | ----- | ------- | --------- | ---- | --------- | --- |
| API    |       |           |     |      | Tests Main  | Checkers |              |       |         |           |      |           |     |
|        | Req.  | Strategy  |     | Len. |             |          |              |       |         |           |      |           |     |
|        |       |           |     |      |             |          | Use-Aft-Free |       | Leak    | Hierarchy |      | NameSpace |     |
| AzureA | 13    | BFS       |     | 3    | 3255 48.1%  | 51.9%    |              | 11.5% | 1.5%    |           | 0.1% | 38.8%     |     |
|        |       | BFS-Cheap |     | 4    | 4050 55.0%  | 45.0%    |              | 10.0% | 0.8%    |           | 2.4% | 31.8%     |     |
|        |       | BFS-Fast  |     | 9    | 4347 59.2%  | 40.8%    |              | 15.5% | 0.2%    |           | 0.1% | 25.1%     |     |
| AzureB | 19    | BFS       |     | 5    | 7721 46.4%  | 53.6%    |              | 3.6%  | 0.4%    |           | 0.2% | 49.4%     |     |
|        |       | BFS-Cheap |     | 5    | 7979 46.2%  | 53.8%    |              | 3.5%  | 0.4%    |           | 0.2% | 49.7%     |     |
|        |       | BFS-Fast  |     | 40   | 17416 65.3% | 34.7%    |              | 0.3%  | 0.0%    |           | 0.1% | 34.3%     |     |
| O-365C | 18    | BFS       |     | 3    | 11693 89.4% | 10.6%    |              | 0.0%  | 1.0%    |           | 0.1% | 9.5%      |     |
|        |       | BFS-Cheap |     | 4    | 10982 95.9% | 4.1%     |              | 0.0%  | 0.0%    |           | 0.1% | 4.0%      |     |
BFS-Fast
|     |     |     |     | 33  | 18120 66.9% | 33.1% |     | 0.0% | 0.0% |     | 0.1% | 33.0% |     |
| --- | --- | --- | --- | --- | ----------- | ----- | --- | ---- | ---- | --- | ---- | ----- | --- |
TABLEI:ComparisonofBFS,BFS-FastandBFS-Cheap.Showsthemaximumsequencelength(MaxLen.),thenumberofrequestssent
(Tests), the percentage of tests generated by the main driver (Main) and by all four checkers combined (Checkers) and individually, with
each search strategy after 1 hour of search. The second column shows the total number of requests in each API.
the bug, starting with the smallest one. If a suffix in this section. There is no randomness in the renderings
exists in a previously-recorded bug bucket, add the generated. We ran our fuzzing experiments using a single-
newsequencetothatexistingbugbucket.Otherwise, threadedfuzzerrunningonaPCconnectedtotheinternetand
create a new bug bucket for the new sequence. a valid service subscription that allows access to each service
This bug bucketization scheme is the same as the one in API. No other special test setup or service knowledge was
stateful REST API fuzzing [5], but we maintain separate, per- required.Asin[5],ourfuzzerincludesagarbage-collectorthat
deletesno-longer-usedresources(dynamicobjects)inorderto
checkerbugbucketsbecausethefailureconditionsaredefined
differentlyforeachrule.Eachbugwillalwaysbetriggeredby avoid exceeding service quota limits.
|     |     |     |     |     |     | We  | fuzz | production | services | already |     | deployed | and acces- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | -------- | ------- | --- | -------- | ---------- |
onecheckerforaspecificsequencelength(becauseofchecker
complementarity),exceptfor“500InternalServerError”bugs sible to anyone with a valid subscription, but we have no
whichmaybetriggeredbyboththemaindriverandcheckers. visibilityastowhathappensinsidethebackendoftheservices
wetest.OurfuzzeronlyobservestheHTTPstatuscodesofthe
| For 500 | bugs, the | new sequence | will | be added | only once | to  |     |     |     |     |     |     |     |
| ------- | --------- | ------------ | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
the bug bucket of the main driver or checker that triggered it responses it receives. All client-side requests are sent over the
|     |     |     |     |     |     | internet | to  | the target | services, | and | responses | are | parsed when |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --------- | --- | --------- | --- | ----------- |
first.
|     |     |     |     |     |     | they | are received. |     | Because | we do | not control | the | deployment |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ------- | ----- | ----------- | --- | ---------- |
IV. EXPERIMENTALEVALUATION of these services, the experiments reported in this section are
notfullycontrolled.However,weperformedtheseexperiments
| In this | section, we | report results | of  | experiments | with three |     |     |     |     |     |     |     |     |
| ------- | ----------- | -------------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
production cloud services. These services and our experimen- several times and the results did not vary significantly.
| tal setup  | are described | in Section   | IV-A.      | Then, | we compare        |     |           |        |            |     |     |     |     |
| ---------- | ------------- | ------------ | ---------- | ----- | ----------------- | --- | --------- | ------ | ---------- | --- | --- | --- | --- |
|            |               |              |            |       |                   | B.  | Comparing | Search | Strategies |     |     |     |     |
| in Section | IV-B the      | three search | strategies |       | described in Sec- |     |           |        |            |     |     |     |     |
tionIII-D.Next,wepresentresultsshowingthenumberofrule Wenowcompareournewsearchstrategy,BFS-Cheap,with
violationsreportedbyeachcheckeronthethreecloudservices BFS and BFS-Fast when using security checkers to fuzz real
as well as the impact of various optimizations (Section IV-C). services. We present results of experiments with two Azure
|                 |       |     |     |     |     | and | one Office-365 |                 | services, | denoted | by  | Azure | A, Azure B, |
| --------------- | ----- | --- | --- | --- | --- | --- | -------------- | --------------- | --------- | ------- | --- | ----- | ----------- |
| A. Experimental | Setup |     |     |     |     | and | O-365          | C respectively. |           |         |     |       |             |
Wereportresultsofexperimentsperformedwiththreecloud Table I shows individual experiments with the three search
services, whose names are anonymized (to avoid targeting strategies on each service, over a fixed time budget of one
them):AzureAandAzureBaretwoAzure[13]management hour per experiment. For each experiment, we report the total
services,andO-365CisanOffice365[16]messagingservice. number of requests in the API (Total Req.), the maximum
The number of requests in the REST API of each of these sequence length generated (Max Len.), the total number of
three services ranges from 13 to 19 requests. We selected requests sent (Tests), the percentage of the requests sent by
those three services because their size and complexity are the main driver (Main) and the active checkers (Checkers) as
representative among the cloud services we analyzed. So far, well as the individual contribution of each checker.
we have performed similar experiments with about a dozen Table I clearly shows that, for all services, BFS reaches
production services, and our general experience with these the smallest depth, BFS-Fast reaches the largest depth, and
other services is summarized in Section V. BFS-Cheap provides a trade-off between these two extremes,
Everyserviceweconsiderhasapublicly-availableSwagger whilebeingclosertoBFSthanBFS-Fast.Thetotalnumberof
specification [15]. For each service, we compile its specifica- tests generated varies across services, depending on the speed
tion to produce a test-generation grammar, similarly to prior of the responses received from each service. For any given
work[5].Eachgrammarisencodedasexecutablepythoncode. service, this number remains roughly similar except for BFS-
For a given service and API, the same grammar and fuzzing FAST with Azure B and O-365 C where the total number of
dictionaries were used across all the experiments reported tests increases significantly. For O-365 C, this increase seems

|     |     | Total |      | Statistics |     |     |     | Bug Buckets |     |     |
| --- | --- | ----- | ---- | ---------- | --- | --- | --- | ----------- | --- | --- |
|     | API |       | Mode |            |     |     |     |             |     |     |
Req.
|     |       |      |            | Tests Checkers |       | Main Use-Aft-Free |     | Leak | Hierarchy | NameSpace |
| --- | ----- | ---- | ---------- | -------------- | ----- | ----------------- | --- | ---- | --------- | --------- |
|     | Azure | A 13 | optimized  | 4050           | 45.0% | 4                 | 3   | 0    | 0         | 0         |
|     |       |      | exhaustive | 2174           | 54.5% | 4                 | 3   | 0    | 0         | 0         |
|     | Azure | B 19 | optimized  | 7979           | 46.2% | 0                 | 0   | 1    | 0         | 0         |
|     |       |      | exhaustive | 9031           | 63.9% | 0                 | 0   | 1    | 0         | 0         |
|     | O-365 | C 18 | optimized  | 10982          | 4.1%  | 1                 | 0   | 0    | 1         | 0         |
|     |       |      | exhaustive | 11724          | 11.4% | 0                 | 0   | 0    | 1         | 0         |
TABLE II: Comparison of modes optimized and exhaustive for two Azure and one Office-365 services. Shows the number of requests
sent in 1 hour (Tests) with BFS-Cheap, the percentage of tests generated by all four checkers combined (Checkers), and the number of bug
bucketsfoundbythemaindriverandeachofthefourcheckers.Optimizedfindsallthebugsfoundbyexhaustivebutitsmaindriverexplores
| more | states faster | given a fixed | test budget | (1 hour). |     |     |     |     |     |     |
| ---- | ------------- | ------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
to be due to a significantly lower number of failed requests We observe that the number of tests varies for different
generated by BFS-FAST for these two services compared to services and checker modes. However, the percentage of tests
BFSandBFS-Cheap.Suchfailedrequestsaresentbacktothe generatedbythecheckersisalwayshigherwiththeexhaustive
optimized
client(ourfuzzer)withlargertimedelays.Delayingresponses mode, as expected. Since in the mode the checkers
tofailedrequestsisawell-knownmechanismusedbyservices producefewertestspervisitedstate,themaindriverisallowed
to throttle future requests, i.e., to try to slow them down. For toexploremorestatesfaster.Yet,despitethelowernumberof
Azure B, BFS-Fast executes more tests because its request checkertestspervisitedstate,forallthreeservicesconsidered,
sequences are deeper but include many DELETE requests the optimized mode finds all the unique bugs (bug buckets)
whicharefastertoexecute(theirresponsesarereceivedalmost found bythe exhaustive mode.Also, for theO-365 C service,
instantly): BFS-Fast executes about 9 times more DELETE the main driver finds one more bug with the optimized mode
requests than BFS or BFS-Cheap. compared to the exhaustive mode within one hour of search.
The total percentage of checker tests (Checkers) is the Table II reveals an interesting inversion that further demon-
highest for BFS and the lowest for BFS-FAST, while BFS- strates the value of the optimized checkers mode. In Azure
Cheap is again in between. Indeed, while BFS-Fast generates A, we observe that the optimized mode produces almost
the largest number of tests, its search space is pruned and twice as many tests than than the exhaustive mode (4050
activates checkers less often, as discussed in Section III-D versus 2174). At first sight, this is counter-intuitive. After
– this is the precise motivation for introducing BFS-Cheap a deeper investigation, we discovered that some of the tests
in that section. An exception is the 33% spike in checker- produced by the exhaustive mode of the user-namespace
generated tests by BFS-FAST for O-365 C. This spike seems checker have significantly larger response times for service
to be due to a larger number of successful requests (see the Azure A. Indeed, this specific checker in exhaustive mode
previous paragraph), which in turn led to more checker tests. executes additional tests compared to the optimized mode, but
FromtheindividualcheckerstatisticsinTableI,weobserve containing expensive operations (i.e., high latency) that slow
thatthenumberofteststheyeachgeneratevariesfromservice down the overall test throughput.
to service. This number depends on the number of DELETE During the course of all experiments with these three
requestsexecutedfortheuse-after-freechecker,thenumberof services, we found and reported a total of 7 unique bugs to
failedresource-creationrequestsfortheresource-leakchecker, the developers of those services, including 4 500 bugs found
andthedepthoftheobjecthierarchyfortheresource-hierarchy by the main driver and 3 bugs found by each of the checkers
checker. In contrast, the user-namespace checker is triggered except the user-namespace checker. In the next section, we
more consistently more often and contributes the largest per- discuss several interesting bugs found thanks to the checkers
centage of checker-generated tests. introduced in this paper.
|     | For all three | services,        | the number | of bugs found    | is nearly |     |                              |     |     |     |
| --- | ------------- | ---------------- | ---------- | ---------------- | --------- | --- | ---------------------------- | --- | --- | --- |
|     |               |                  |            |                  |           |     | V. EXAMPLESOFRESTAPISECURITY |     |     |     |
| the | same for      | all three search | strategies | and is discussed | next.     |     |                              |     |     |     |
VULNERABILITIES
| C.  | Comparing | Checker | Optimizations |     |     |             |     |               |         |                       |
| --- | --------- | ------- | ------------- | --- | --- | ----------- | --- | ------------- | ------- | --------------------- |
|     |           |         |               |     |     | At the time | of  | this writing, | we have | fuzzed nearly a dozen |
We now compare the performance of the two modes opti- production Azure and Office-365 cloud services of size and
mized and exhaustive discussed in Section III. complexity similar to the three services used in the previous
Table II shows how many requests were sent in one hour section.Inalmostallcases,ourfuzzingwasabletofindabout
of fuzzing with BFS-Cheap in the Tests column, and what a handful of new bugs in each of these services. About two
percentageofthoserequestsweregeneratedbyeitherthemain thirds of those bugs are “500 Internal Server Errors”, and
driver of Section II or by any of the four checkers. The table aboutonethirdareruleviolationsreportedbyournewsecurity
also shows how many unique bugs (bug buckets) were found checkers. We reported these bugs to the service owners, and
in one hour of search by the main driver and by each of the all have been fixed.
checkers. Results are presented for both the optimized and the We emphasize that, even when the security checkers do
exhaustive modes previously discussed. not find any bugs, they increase confidence that the rules

they check cannot be violated and therefore they increase shows that the user view is correct: the CM resource named
confidence in the overall service reliability and security. X attempted to be created in Step 1 has not been created.
This section presents examples of real bugs found in However, the second PUT request in Step 3 proves that the
deployed Azure and Office-365 services and discuss their service still remembersthe failed creation of theCM resource
security relevance. We anonymize the name of those services named X attempted in the first PUT request of Step 1. This
and key details not to target any specific service. bug is potentially dangerous: an attacker could create an
Use-after-free violation in Azure. In an Azure service, we unbounded number of such “zombie” resources by repeating
found the following use-after-free violation. Step1usingmanydifferentnames,andexceedhis/herofficial
1) Create a new resource R (with a PUT request). quota since such failed resource creations are (correctly) not
countedtowardstheuser’resourcequota.Yet,theyareclearly
| 2) Delete | resource | R   | (with a | DELETE | request). |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3) Create a new child resource of the deleted resource R remembered (incorrectly) somewhere in the backend service.
and of a specific type (with another PUT request). Other Example: Eager Resource-Accounting DoS Attack.
|     |     |     |     |     |     |     |     | After fuzzing | another |     | Azure | service | for about | five | hours, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ----- | ------- | --------- | ---- | ------ |
Thissequenceofrequestsresultsina“500InternalServerEr-
|           |                |               |         |          |         |           |          | we accidentally |              | triggered | a severe | health   | degradation |          | for that |
| --------- | -------------- | ------------- | ------- | -------- | ------- | --------- | -------- | --------------- | ------------ | --------- | -------- | -------- | ----------- | -------- | -------- |
| ror”. The | Use-after-free |               | checker | catches  | this    | as (1) it | attempts |                 |              |           |          |          |             |          |          |
|           |                |               |         |          |         |           |          | service.        | We summarize |           | here the | findings | on          | its root | cause.   |
| to re-use | in Step        | 3 the deleted |         | resource | in Step | 2 and     | (2) the  |                 |              |           |          |          |             |          |          |
response of Step 3 is different from the expected “404 Not Our fuzzing tool uses a garbage collector not to exceed
|     |     |     |     |     |     |     |     | quotas | for the | cloud | resources | created | during | fuzzing. | For |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----- | --------- | ------- | ------ | -------- | --- |
Found” response.
instance,ifadefaultquotaforaresourcetypeYis100,atmost
| Resource-hierarchy |     | violation |     | in Office365. |     | In an Office365 |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
messaging service where users can post messages and then 100 resources of that type can be created at any time, and our
garbagecollectormakessurethatthenumberofliveresources
| reply and     | edit | these, the    | resource-hierarchy |     |       | checker   | detected |               |                              |           |          |         |          |                 |             |
| ------------- | ---- | ------------- | ------------------ | --- | ----- | --------- | -------- | ------------- | ---------------------------- | --------- | -------- | ------- | -------- | --------------- | ----------- |
|               |      |               |                    |     |       |           |          | never exceeds | quotas                       | by        | deleting | (using  | a DELETE |                 | request)    |
| the following |      | bug.          |                    |     |       |           |          |               |                              |           |          |         |          |                 |             |
|               |      |               |                    |     |       |           |          | resources     | that are                     | no longer | used.    | Without | garbage  |                 | collection, |
| 1) Create     | a    | first message | msg-1              |     | (with | a request | POST     |               |                              |           |          |         |          |                 |             |
|               |      |               |                    |     |       |           |          | ourfuzzing    | toolwouldtypicallyreachquota |           |          |         |          | limitsinminutes |             |
/api/posts/msg-1).
|           |     |                |     |       |       |           |      | and would | not be   | able  | to continue | state-space |             | exploration. |             |
| --------- | --- | -------------- | --- | ----- | ----- | --------- | ---- | --------- | -------- | ----- | ----------- | ----------- | ----------- | ------------ | ----------- |
| 2) Create | a   | second message |     | msg-2 | (with | a request | POST |           |          |       |             |             |             |              |             |
|           |     |                |     |       |       |           |      | In this   | specific | Azure | service,    | any         | PUT request |              | to create a |
/api/posts/msg-2).
resourceofaspecifictype,letuscallitIM,returnsaresponse
reply-1
| 3) Create | a   | reply                                   |     | to the | first | message | (with | a       |              |          |       |       |      |      |            |
| --------- | --- | --------------------------------------- | --- | ------ | ----- | ------- | ----- | ------- | ------------ | -------- | ----- | ----- | ---- | ---- | ---------- |
|           |     |                                         |     |        |       |         |       | quickly | but actually | triggers | other | tasks | that | take | minutes to |
| request   |     | POST /api/posts/msg-1/replies/reply-1). |     |        |       |         |       |         |              |          |       |       |      |      |            |
completeintheservicebackend.Similarly,aDELETErequest
| 4) Edit | the | reply reply-1 |            | with | a PUT | request   | using |              |             |      |              |         |              |          |          |
| ------- | --- | ------------- | ---------- | ---- | ----- | --------- | ----- | ------------ | ----------- | ---- | ------------ | ------- | ------------ | -------- | -------- |
|         |     |               |            |      |       |           |       | for an       | IM resource | also | returns      | quickly |              | but also | triggers |
| msg-2   |     | as message    | identifier |      | (with | a request | PUT   |              |             |      |              |         |              |          |          |
|         |     |               |            |      |       |           |       | delete tasks | that        | also | take minutes |         | to complete. |          | However, |
/api/posts/msg-2/replies/reply-1).
|               |          |                  |         |      |           |        |     | such PUT | and     | DELETE | requests |     | for IM   | resources | update  |
| ------------- | -------- | ---------------- | ------- | ---- | --------- | ------ | --- | -------- | ------- | ------ | -------- | --- | -------- | --------- | ------- |
| Surprisingly, |          | the last request | in      | Step | 4 returns | a “200 | Al- |          |         |        |          |     |          |           |         |
|               |          |                  |         |      |           |        |     | counters | towards | quotas | eagerly, | too | quickly, | without   | waiting |
| lowed”        | response | while            | it must | have | returned  | a “404 | Not |          |         |        |          |     |          |           |         |
fortheseveralminutesactuallyneededtofullycompletethese
| Found”    | response. | This    | rule violation |         | reveals | that the | imple-  |           |           |             |     |                          |         |        |         |
| --------- | --------- | ------- | -------------- | ------- | ------- | -------- | ------- | --------- | --------- | ----------- | --- | ------------------------ | ------- | ------ | ------- |
|           |           |         |                |         |         |          |         | tasks. As | a result, | an attacker |     | could create-then-delete |         |        | quickly |
| mentation | of        | the API | that posts     | a reply | does    | not      | analyze |           |           |             |     |                          |         |        |         |
|           |           |         |                |         |         |          |         | many IM   | resources | without     |     | exceeding                | his/her | quota, | while   |
the full hierarchy when checking permissions for a reply. triggering a huge number of backend tasks, hence literally
| Missing           | hierarchy | validation   |           | checks  | are potential |            | security |                  |             |               |      |             |                   |         |            |
| ----------------- | --------- | ------------ | --------- | ------- | ------------- | ---------- | -------- | ---------------- | ----------- | ------------- | ---- | ----------- | ----------------- | ------- | ---------- |
|                   |           |              |           |         |               |            |          | flooding         | the backend | service.      |      | Such a      | Denial-of-Service |         | attack     |
| vulnerabilities:  |           | an attacker  | might     | be able | to            | exploit    | them     | to               |             |               |      |             |                   |         |            |
|                   |           |              |           |         |               |            |          | was accidentally |             | triggered     | by   | our fuzzing | tool.             |         |            |
| access child      | objects   | by           | bypassing | the     | parent        | hierarchy. |          |                  |             |               |      |             |                   |         |            |
|                   |           |              |           |         |               |            |          | A fix            | to this     | vulnerability |      | is to       | update            | usage   | counters   |
| Resource-leak     |           | violation    | in Azure. | In      | another       | Azure      | service, |                  |             |               |      |             |                   |         |            |
|                   |           |              |           |         |               |            |          | towards          | quotas      | for DELETE    |      | requests    | only              | when    | all delete |
| the resource-leak |           | checker      | triggered | the     | following     | bug.       |          |                  |             |               |      |             |                   |         |            |
|                   |           |              |           |         |               |            |          | backend          | operations  | have          | been | completed,  | i.e.,             | minutes | later      |
| 1) Create         | a         | new resource | of        | type CM | and           | of name    | X with   |                  |             |               |      |             |                   |         |            |
|                   |           |              |           |         |               |            |          | in the case      | of IM       | resources.    | This | way,        | the amount        | of      | backend    |
a specific malformed body (with a PUT request). This tasks is still linearly bounded by the official quota, since
| returns | a   | “500 Internal | Server | Error”, |     | which is | already |     |     |     |     |     |     |     |     |
| ------- | --- | ------------- | ------ | ------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
subsequentIMresource-creationPUTrequestswillbeblocked
a bug.
untilprecedingDELETErequestshavebeenfullycompleted.
| 2) Get | a list | of all resources |     | of type | CM: | the returned | list |     |     |     |             |     |     |     |     |
| ------ | ------ | ---------------- | --- | ------- | --- | ------------ | ---- | --- | --- | --- | ----------- | --- | --- | --- | --- |
| is     | empty. |                  |     |         |     |              |      |     |     | VI. | RELATEDWORK |     |     |     |     |
3) CreateanewresourceoftypeCMwiththesamenameX Our work extends stateful REST API fuzzing [5]. Given
as in Step 1 with a well-formed body but in a different a Swagger specification of a REST API, this specification
| region | (e.g., | US-West | versus | US-Central) |     | with | a PUT |             |      |           |          |     |       |         |         |
| ------ | ------ | ------- | ------ | ----------- | --- | ---- | ----- | ----------- | ---- | --------- | -------- | --- | ----- | ------- | ------- |
|        |        |         |        |             |     |      |       | is compiled | into | a fuzzing | grammar, |     | which | is then | used to |
request. automatically generate sequences of requests that satisfy the
Unexpectedly, the last request in Step 3 returns a response specification.StatefulRESTAPIfuzzingautomatesthegener-
“409 Conflict” instead of an expected “200 Created”. This ation of a fuzzing grammar compared to traditional grammar-
behavior means that the service has reached an inconsistent basedfuzzing[20],[22],[24]wheretheusermanuallywritesa
state: the failed request in Step 1 has left unintended side- grammar.TheBFSandBFS-Fastsearchstrategiesareinspired
effects on the service state. Indeed, the GET request in Step 2 bytestgenerationalgorithmsusedinmodel-basedtesting[27],

[12],[28]forgeneratingminimaltestsuitesthatcoveranentire of API requests and their responses as in traditional runtime
finite-state-machine model of a system under test. This paper verification [8], [11], but also generate new tests specifically
extends stateful REST API fuzzing (i) by introducing a set of aimed at triggering rule violations. Similarly to [10], we use
security rules for REST APIs and corresponding checkers for multiple independent security checkers simultaneously. But
efficiently testing and detecting violations of these rules; and unlike [10], we do not use symbolic execution, constraint
(ii) by introducing a new search strategy, BFS-Cheap, which generation and solving in order to generate new tests. Indeed,
offersamiddle-groundbetweenBFSandBFS-Fastwhenusing the inner workings of the services we test are invisible to
active checkers. our fuzzing tool and its checkers, which only see REST
SinceRESTAPIrequestsandresponsesaretransmittedover API requests and responses. Since cloud services are usually
the HTTP protocol, HTTP-fuzzers can be used to fuzz REST complex distributed systems whose components are written
APIs. Fuzzers like Burp [7], Sulley [23], BooFuzz [6], or in different languages, general symbolic-execution-based ap-
the commercial AppSpider [4] and Qualys’s WAS [21], can proaches seem problematic, but it would be worth exploring
capture/replay HTTP traffic, parse HTTP requests/responses this option further in future work.
and their contents (like embedded JSON data), and then fuzz In practice, the main technique used today to ensure the
those using either pre-defined heuristics [4], [21] or user- securityofcloudservicesispenetrationtesting,orpentesting
| definedrules[23],[6].Some |     |     | toolstocapture,parse,fuzz,and |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forshort,whichmeanssecurityexpertsreviewthearchitecture,
replay HTTP traffic have recently been extended to leverage design,andcodeofcloudservicesfromasecurityperspective.
| Swagger | specifications |     | in order | to parse | HTTP | requests | over |     |     |     |     |     |     |     |
| ------- | -------------- | --- | -------- | -------- | ---- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Sincepentestingislaborintensive,itisexpensiveandlimited
REST APIs and guide their fuzzing [4], [21], [26], [3]. in scope and depth. Fuzzing tools and security checkers,
However, these tools do not perform any global analysis of like those discussed in this paper, can partly automate the
| Swagger | specifications |     | and therefore |     | cannot | generate | new |           |                     |     |             |                  |     |     |
| ------- | -------------- | --- | ------------- | --- | ------ | -------- | --- | --------- | ------------------- | --- | ----------- | ---------------- | --- | --- |
|         |                |     |               |     |        |          |     | discovery | of specific classes |     | of security | vulnerabilities, |     | and |
sequences of requests: their fuzzing is stateless, i.e., restricted are complementary to pen testing.
| to fuzzing      | parameter | values       | of           | individual | requests. | Therefore,       |      |               |      |            |       |              |           |     |
| --------------- | --------- | ------------ | ------------ | ---------- | --------- | ---------------- | ---- | ------------- | ---- | ---------- | ----- | ------------ | --------- | --- |
| adding active   | checkers  |              | to stateless | fuzzers    |           | is problematic.  | In   |               |      |            |       |              |           |     |
|                 |           |              |              |            |           |                  |      |               | VII. | CONCLUSION |       |              |           |     |
| contrast,       | our work  | extends      | stateful     |            | REST      | API fuzzing      | with |               |      |            |       |              |           |     |
| active checkers | targeting |              | specific     | REST       | API       | rule violations. |      |               |      |            |       |              |           |     |
|                 |           |              |              |            |           |                  |      | We introduced | four | security   | rules | that capture | desirable |     |
| Because         | most      | HTTP-fuzzers |              | were       | born      | as extensions    | of   |               |      |            |       |              |           |     |
traditionalweb-pagecrawlersandscanners,theyoftensupport propertiesofRESTAPIsandservices.Wethenshowedhowa
statefulRESTAPIfuzzercanbeextendedwithactiveproperty
| a long list | of HTTP-focused |        | properties |     | they         | can check, | such     |          |                    |      |            |            |     |       |
| ----------- | --------------- | ------ | ---------- | --- | ------------ | ---------- | -------- | -------- | ------------------ | ---- | ---------- | ---------- | --- | ----- |
|             |                 |        |            |     |              |            |          | checkers | that automatically | test | and detect | violations | of  | these |
| as checking | for             | proper | HTTP-usage |     | in responses |            | and even |          |                    |      |            |            |     |       |
checking for cross-site-scripting attacks or SQL-injections rules.Sofar,wehavefuzzednearlyadozenproductionAzure
|          |           |       |      |     |            |       |     | and Office-365 | cloud services |     | using the | fuzzer | and checkers |     |
| -------- | --------- | ----- | ---- | --- | ---------- | ----- | --- | -------------- | -------------- | --- | --------- | ------ | ------------ | --- |
| if whole | web-pages | (with | HTML | and | Javascript | code) | are |                |                |     |           |        |              |     |
returned as part of the responses. However, for most REST described in this paper. In almost all cases, our fuzzing was
|                 |          |        |              |            |                 |          |        | able to   | find about a handful |     | of new     | bugs in each | of       | these |
| --------------- | -------- | ------ | ------------ | ---------- | --------------- | -------- | ------ | --------- | -------------------- | --- | ---------- | ------------ | -------- | ----- |
| APIs, responses |          | do not | include      | web-pages, |                 | and most | of the |           |                      |     |            |              |          |       |
|                 |          |        |              |            |                 |          |        | services. | About two thirds     | of  | those bugs | are “500     | Internal |       |
| aforementioned  | checking |        | capabilities |            | are irrelevant. |          |        |           |                      |     |            |              |          |       |
Compared to HTTP-fuzzers and web scanners, our paper ServerErrors”,andaboutonethirdareruleviolationsreported
|            |              |     |       |          |          |              |     | by our new | security checkers. |     | We reported | all | these bugs | to  |
| ---------- | ------------ | --- | ----- | -------- | -------- | ------------ | --- | ---------- | ------------------ | --- | ----------- | --- | ---------- | --- |
| introduces | new security |     | rules | that are | targeted | specifically |     | at         |                    |     |             |     |            |     |
RESTAPIusage.Theserulesaresecurity-relatedbecausetheir the service owners, and all have been fixed.
violations might be exploited by a malicious attacker to harm Indeed, violations of the four security rules introduced in
the health of a service or steal unauthorized information or this paper are clearly potential security vulnerabilities. The
resources. In contrast, we do not discuss in this paper how bugs we found have all been taken seriously by the respective
|          |            |     |       |       |      |         |         | service | owners: our current | bug | “fixed/found” | ratio | is  | nearly |
| -------- | ---------- | --- | ----- | ----- | ---- | ------- | ------- | ------- | ------------------- | --- | ------------- | ----- | --- | ------ |
| to check | other REST | API | usage | rules | [9], | such as | request |         |                     |     |               |       |     |        |
idempotence (i.e., repeating identical requests like GET or 100%. Moreover, it is safer to fix these bugs rather than risk
PATCH have no further effect on the outcome), which are a live incident – provoked intentionally by an attacker or
not “exploitable” when violated. triggered by accident – with unknown consequences. Finally,
Given the widespread use of REST APIs, there is sur- it helps that these bugs are easily reproducible and that our
|           |                 |     |          |     |        |      |         | fuzzing | approach reports | no false | alarms. |     |     |     |
| --------- | --------------- | --- | -------- | --- | ------ | ---- | ------- | ------- | ---------------- | -------- | ------- | --- | --- | --- |
| prisingly | little guidance |     | provided | on  | secure | REST | API us- |         |                  |          |         |     |     |     |
age. Most of the security guidance from organisations like How general are these results? To find out, we need to
OWASP [19] (Open Web Application Security Project) or fuzz more services through their REST APIs and check
frombooksonRESTAPIs[1]ormicro-services[17]isabout more properties to detect different kinds of bugs and security
managing authentication tokens and API keys. No detailed vulnerabilities. Given the recent explosion of REST APIs for
guidance is provided regarding REST API input validation cloud and web services, there is surprisingly little guidance
and resource management. To the best of our knowledge, the about REST API usage from a security point of view. Our
four security rules introduced in this paper are new. paper makes a step in that direction by contributing four rules
In Section III, we used the term active checker from [10] whose violations are security-relevant and which are non-
to denote that our checkers do not simply monitor sequences trivial to check and satisfy.

REFERENCES
[1] S.Allamaraju. RESTfulWebServicesCookbook. O’Reilly,2010.
[2] Amazon. AWS. https://aws.amazon.com/.
[3] APIFuzzer. https://github.com/KissPeter/APIFuzzer.
[4] AppSpider. https://www.rapid7.com/products/appspider.
[5] V.Atlidakis,P.Godefroid,andM.Polishchuk. RESTler:StatefulREST
APIFuzzing. In41stACM/IEEEInternationalConferenceonSoftware
Engineering(ICSE’2019),May2019.
[6] BooFuzz. https://github.com/jtpereyda/boofuzz.
[7] BurpSuite. https://portswigger.net/burp.
[8] D.Drusinsky.TheTemporalRoverandtheATGRover.InProceedings
ofthe2000SPINWorkshop,volume1885ofLectureNotesinComputer
Science,pages323–330.Springer-Verlag,2000.
[9] R. T. Fielding. Architectural Styles and the Design of Network-based
SoftwareArchitectures. PhDThesis,UCIrvine,2000.
[10] P.Godefroid,M.Levin,andD.Molnar. ActivePropertyChecking. In
Proceedings of EMSOFT’2008 (8th Annual ACM & IEEE Conference
onEmbeddedSoftware),pages207–216,Atlanta,October2008.ACM
Press.
[11] K. Havelund and G. Rosu. Monitoring Java Programs with Java
PathExplorer. InProceedingsofRV’2001(FirstWorkshoponRuntime
Verification), volume 55 of Electronic Notes in Theoretical Computer
Science,Paris,July2001.
[12] R. La¨mmel and W. Schulte. Controllable Combinatorial Coverage in
Grammar-BasedTesting. InProceedingsofTestCom’2006,2006.
[13] Microsoft. Azure. https://azure.microsoft.com/en-us/.
[14] Microsoft.AzureDNSZoneRESTAPI.https://docs.microsoft.com/en-
us/rest/api/dns/zones/get.
[15] Microsoft. MicrosoftAzureSwaggerSpecifications. https://github.com/
Azure/azure-rest-api-specs.
[16] Microsoft. Office. https://www.office.com/.
[17] S.Newman. BuildingMicroservices. O’Reilly,2015.
[18] OAuth. OAuth2.0. https://oauth.net/.
[19] OWASP(OpenWebApplicationSecurityProject). https://www.owasp.
org.
[20] PeachFuzzer. http://www.peachfuzzer.com/.
[21] Qualys Web Application Scanning (WAS). https://www.qualys.com/
apps/web-app-scanning/.
[22] SPIKEFuzzer. http://resources.infosecinstitute.com/fuzzer-automation-
with-spike/.
[23] Sulley. https://github.com/OpenRCE/sulley.
[24] M.Sutton,A.Greene,andP.Amini.Fuzzing:BruteForceVulnerability
Discovery. Addison-Wesley,2007.
[25] Swagger. https://swagger.io/.
[26] TnT-Fuzzer. https://github.com/Teebytes/TnT-Fuzzer.
[27] M.Utting,A.Pretschner,andB.Legeard.ATaxonomyofModel-Based
TestingApproaches. Intl.JournalonSoftwareTesting,Verificationand
Reliability,22(5),2012.
[28] M.YannakakisandD.Lee. TestingFinite-StateMachines. InProceed-
ingsofthe23rdAnnualACMSymposiumontheTheoryofComputing,
pages476–485,1991.