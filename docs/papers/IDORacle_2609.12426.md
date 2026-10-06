> 원본: IDORacle_2609.12426.pdf; 변환: markitdown; 2026-10-06

<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->

IDORacle: Template-Guided SQL-Sink Mediation for Object-Level Authorization in Java
Applications
YuewantongSonga,1,GuanhangShib,c,1,YinCaib,c,ChanghuiWangb,c,JinWeib,c,PingChenc,∗,LeiShid,JiangxingWua,c
aSchoolofComputerScienceandArtificialIntelligence,ZhengzhouUniversity,Zhengzhou,China
bSchoolofComputerScience,FudanUniversity,Shanghai,China
cInstituteofBigData,FudanUniversity,Shanghai,China
dSchoolofCyberScienceandEngineering,ZhengzhouUniversity,Zhengzhou,China
6202 peS 11  ]RC.sc[  1v62421.9062:viXra Abstract
InsecureDirectObjectReference(IDOR),frequentlymodeledasBrokenObject-LevelAuthorization(BOLA),remainsprevalent
in Java database applications. The root cause is an architectural disconnect between identity and authorization checks enforced
at the Controller or Service layer and the underlying SQL execution layer, which performs object-level operations based solely
on resource identifiers. Existing research predominantly addresses detection of such vulnerabilities in source code, leaving a
gap in low-intrusion runtime defense solutions for legacy Java-SQL applications. This paper presents IDORacle, a template-
guidedSQL-sinkinterceptionandrewritingframeworkdesignedtomitigatehorizontalprivilegeescalationatruntime. IDORacle
propagatesauthenticatedidentitycontextsacrossHTTPrequests,asynchronoustasks,anddata-accessboundariesviaaserver-side
traceidentifier. AttheMyBatis/JDBCboundary,itextractsSQLtemplatesandcomputesdualfingerprints,performingaone-time
template-levelanalysistogeneratereusablemediationplans. Duringinstanceexecution,theframeworkcombinesruntimesubject
context,ASTstructures,tablemetadata,andcachedauthorizationproofstopermit,rewrite,orblockeachSQLoperation.IDORacle
supportsdirectownershippredicateinjection,join-derivedownershipguards,probe-basedauthorizationforgroup-ownedresources,
role-sensitivestate-transitionchecks,andsensitive-columnmediation.Thisguardtaxonomyavoidstheunsoundassumptionthatall
authorizationfailuresreducetoasinglerowpredicate. Tocontainoverheadinproductionenvironments,IDORaclearchitecturally
decouplestemplate-levelanalysisfrominstance-levelcaching.AdedicatedJava-SQLbenchmarksuiteisconstructedtoevaluatethe
frameworkagainstdiverseIDORscenariosgroundedinreal-worldCVEreports. ExperimentalresultsdemonstratethatIDORacle
preventshorizontalauthorizationviolationswithaworst-caseguardlatencyof0.17ms. Itsredundancy-awareoptimizationreduces
averageper-instanceoverheadbyover90%(to0.017ms)forhotSQLtemplates,bridgingthegapbetweendetection-phaseBOLA
analysisandpractical,low-overheadruntimeenforcement.
Keywords: Insecuredirectobjectreference,Brokenobject-levelauthorization,SQL-sinkmediation,Runtimeauthorization
enforcement,Javaapplications
1. Introduction secure Direct Object Reference (IDOR) is a concrete instanti-
|     |     |     |     |     | ation of | this problem: | an  | authenticated |     | user substitutes |     | an ob- |
| --- | --- | --- | --- | --- | -------- | ------------- | --- | ------------- | --- | ---------------- | --- | ------ |
Broken access control remains one of the most persistent jectidentifier—suchasanorderID,jobID,tenantID,oruser
| classes of web-application |     | security | failures. | In the OWASP |     |     |     |     |     |     |     |     |
| -------------------------- | --- | -------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ID—andtheserveromitsverificationthatthereferencedobject
Top10:2025,BrokenAccessControlretainsitsrankingasthe
|     |     |     |     |     | falls within | the | user’s authorized |     | scope | (MITRE | Corporation, |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | ----- | ------ | ------------ | --- |
leading application-security risk (OWASP Foundation, 2021, 2026b;PortSwiggerWebSecurityAcademy,2026a,b).
| 2025;MITRECorporation,2026a). |     |     | IntheOWASPAPISecu- |     |        |           |                  |     |     |      |      |          |
| ----------------------------- | --- | --- | ------------------ | --- | ------ | --------- | ---------------- | --- | --- | ---- | ---- | -------- |
|                               |     |     |                    |     | Unlike | injection | vulnerabilities, |     |     | IDOR | is a | semantic |
rityTop102023,BrokenObjectLevelAuthorization(BOLA)
|     |     |     |     |     | vulnerability. | An  | HTTP | request | may | be syntactically |     | valid, |
| --- | --- | --- | --- | --- | -------------- | --- | ---- | ------- | --- | ---------------- | --- | ------ |
is listed as API1:2023, reflecting the broad attack surface cre- theSQLstatementmaybewell-formed, andtheauthenticated
| ated when APIs | expose | object identifiers |     | through URLs, re- |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
usermaybepermittedtoinvoketheendpoint,yettheconcrete
quest bodies, and API parameters without enforcing object- databaseobjectaccessedbythebackendmaybelongtoanother
| level authorization | checks | (OWASP | Foundation, | 2023a). In- |                      |     |               |             |            |           |         |         |
| ------------------- | ------ | ------ | ----------- | ----------- | -------------------- | --- | ------------- | ----------- | ---------- | --------- | ------- | ------- |
|                     |        |        |             |             | user, tenant,        | or  | group.        | Correctness |            | therefore | depends | on      |
|                     |        |        |             |             | application-specific |     | authorization |             | invariants |           | rather  | than on |
inputsyntax(Felmetsgeretal.,2010;PellegrinoandBalzarotti,
∗Correspondingauthor.
|     |     |     |     |     | 2014; Wang | et  | al., 2026). | Object-level |     | authorization |     | cannot |
| --- | --- | --- | --- | --- | ---------- | --- | ----------- | ------------ | --- | ------------- | --- | ------ |
Emailaddresses:sywt149@gs.zzu.edu.cn(YuewantongSong),
|     |     |     |     |     | be addressed | as  | a pure | input-sanitization |     | problem; |     | it must be |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | ------------------ | --- | -------- | --- | ---------- |
guanhang@bu.edu(GuanhangShi),ycai25@m.fudan.edu.cn(YinCai),
changhuiwang25@m.fudan.edu.cn(ChanghuiWang), enforced at the layer where subjects, objects, and backend
j_wei@fudan.edu.cn(JinWei),pchen@fudan.edu.cn(PingChen),
operationsconverge.
shilei@zzu.edu.cn(LeiShi),ndscwjx@126.com(JiangxingWu)
Asubstantialbodyofresearchhasinvestigatedstaticanal-
1YuewantongSongandGuanhangShicontributedequallytothiswork.

ysis,directedfuzzing,andruntimeobservationtodetectBOLA entry, it propagates the authenticated subject context via a
and missing owner-check vulnerabilities in web applications server-side trace identifier. At the data-access boundary, it
(Huangetal.,2024;Liuetal.,2025a,b;Dharmaadietal.,2025; separates template planning from instance mediation: a SQL
Thesedetection-orientedapproacheseffec-
Zhangetal.,2025). template is parsed, normalized, and compiled into a reusable
tively identify whether a vulnerable endpoint exists, yet they mediation plan once, while per-execution work is limited
operate within a testing-phase paradigm. In enterprise envi- to context binding, resource-key extraction, proof lookup,
ronments, legacy codebases frequently contain large numbers and guard evaluation. Guard types cover direct ownership
of endpoints in which authorization logic is interleaved with predicates, join-derived ownership, group/tenant membership
businessSQL.Evenwhenascannersuccessfullyflagsamiss- probes, role-sensitive state transitions, and sensitive-column
ingownershipcheck,retrofittingauthorizationintomonolithic policies,avoidingtheunsoundassumptionthatallauthorization
legacyservicesiserror-proneandtime-consuming. Adeploy- failuresreducetoasinglerowpredicate.
able,low-intrusionruntimepreventionmechanismistherefore Thispapermakesthefollowingcontributions:
neededasacomplementarylastlineofdefense.
•
|            |             |            |          |                 |        |           |         | Template-guided  |        | SQL-sink        |     | reference     | monitor.        | IDO- |
| ---------- | ----------- | ---------- | -------- | --------------- | ------ | --------- | ------- | ---------------- | ------ | --------------- | --- | ------------- | --------------- | ---- |
| A natural  | enforcement |            | point    | is the database |        | access    | bound-  |                  |        |                 |     |               |                 |      |
|            |             |            |          |                 |        |           |         | Racle introduces |        | a low-intrusion |     | reference     | monitor         | at   |
| ary. Prior | work        | has        | explored | fine-grained    |        | access    | control |                  |        |                 |     |               |                 |      |
|            |             |            |          |                 |        |           |         | the database     | access | boundary        |     | that binds    | trusted subject |      |
| through    | query       | rewriting, |          | authorization   | views, | row-level |         |                  |        |                 |     |               |                 |      |
|            |             |            |          |                 |        |           |         | context          | to SQL | executions.     |     | By separating | template-       |      |
security,andmiddlewaremediation(Rizvietal.,2004;Chaud-
|              |        |             |     |                  |         |            |       | level planning |        | from instance-level |            | mediation, | it           | reuses |
| ------------ | ------ | ----------- | --- | ---------------- | ------- | ---------- | ----- | -------------- | ------ | ------------------- | ---------- | ---------- | ------------ | ------ |
| huri et al., | 2007;  | Mehta       | et  | al., 2017;       | Eykholt | et al.,    | 2017; |                |        |                     |            |            |              |        |
|              |        |             |     |                  |         |            |       | authorization  | plans  | across              | normalized | SQL        | fingerprints |        |
| PostgreSQL   | Global | Development |     | Group,           | 2026;   | Microsoft, |       |                |        |                     |            |            |              |        |
|              |        |             |     |                  |         |            |       | and enforces   | checks |                     | on runtime | context    | and          | policy |
| 2025; Zhang  | et     | al., 2022). |     | These mechanisms |         | establish  | that  |                |        |                     |            |            |              |        |
SQL-level mediation is both security-relevant and practical. metadataforeachexecution.
However, applying them directly to Java web stacks exposes • Heterogeneous guard model for object-level authori-
| a critical | semantic | gap: | legacy | Java applications |     | enforce | au- |         |          |         |     |                |          |     |
| ---------- | -------- | ---- | ------ | ----------------- | --- | ------- | --- | ------- | -------- | ------- | --- | -------------- | -------- | --- |
|            |          |      |        |                   |     |         |     | zation. | IDORacle | defines | a   | guard taxonomy | covering |     |
thenticationandrolechecksinfilters, annotations, controllers, direct ownership, derived ownership, group/tenant
or service methods, while MyBatis or JDBC mappers execute role/state
|                                            |     |     |     |     |     |               |     | membership, |      |       | policy,  | and sensitive-column |               |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---- | ----- | -------- | -------------------- | ------------- | --- |
| SQLstatementsusingonlyresourceidentifiers. |     |     |     |     |     | Theauthorized |     |             |      |       |          |                      |               |     |
|                                            |     |     |     |     |     |               |     | policy.     | This | model | supports | diverse              | authorization |     |
subject identity is therefore separated from the SQL sink that semantics within a unified declarative configuration,
commitsthedatabaseoperation.
|         |            |           |            |            |               |     |          | complementing |     | existing | controller- | and | service-layer |     |
| ------- | ---------- | --------- | ---------- | ---------- | ------------- | --- | -------- | ------------- | --- | -------- | ----------- | --- | ------------- | --- |
| This    | paper      | addresses | this       | deployment | gap           | by  | studying | checks.       |     |          |             |     |               |     |
| runtime | prevention | of        | horizontal | Java-SQL   | authorization |     | vio-     |               |     |          |             |     |               |     |
lations, where an authenticated low-privilege user attempts to • Benchmark design and empirical evaluation. We
|     |     |     |     |     |     |     |     | construct | a dedicated |     | Java-SQL | IDOR | benchmark |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | -------- | ---- | --------- | --- |
read,update,delete,ortriggerstatechangesonobjectsoutside
her authorized scope—the core semantics of IDOR/BOLA grounded in real-world CVE reports to evaluate the
|        |             |     |           |             |     |      |           | framework | across | diverse | ownership | patterns. | Results |     |
| ------ | ----------- | --- | --------- | ----------- | --- | ---- | --------- | --------- | ------ | ------- | --------- | --------- | ------- | --- |
| (OWASP | Foundation, |     | 2023c,b). | The primary |     | goal | is not to |           |        |         |           |           |         |     |
replace framework-level authentication, RBAC, or ABAC demonstratethatIDORaclepreventsalltestedhorizontal
(Sandhu et al., 1996; Hu et al., 2014), but to add a last-mile privilege escalation attempts with zero false positives.
|     |     |     |     |     |     |     |     | The redundancy-aware |     |     | caching | mechanism | reduces |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------- | --------- | ------- | --- |
SQL-sinkreferencemonitorthatcomplementsexistingchecks
by requiring sufficient object-level evidence before protected averageoverheadbyover90%(to0.017ms)forhotSQL
templates,withaworst-caselatencyof0.17ms.
SQLinstancesreachthedatabase.
| Realizingthisgoalsurfacesfourchallenges. |     |                |         |             |           | First,authori- |         |            |     |     |     |     |     |     |
| ---------------------------------------- | --- | -------------- | ------- | ----------- | --------- | -------------- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
| zation evidence                          |     | is fragmented: |         | ownership   |           | semantics      | vary    |            |     |     |     |     |     |     |
|                                          |     |                |         |             |           |                | 2.      | Background |     |     |     |     |     |     |
| widely across                            |     | tables,        | ranging | from direct | ownership |                | columns |            |     |     |     |     |     |     |
(e.g., user_id) to derivation via multi-hop joins, tenant 2.1. ScopingtheDefense: BOLA,BFLA,andBOPLA
groupings, or dynamic states. Second, SQL-sink enforcement Broken access control is a broad category. For this pa-
mustbesemantics-aware; uniformlyappendingAND user_id per,threesubcategoriesareespeciallyrelevant. BrokenObject-
= ? would disrupt dictionary tables, administrator opera- LevelAuthorizationconcernswhethertheauthenticatedsubject
tions, and legitimate cross-user workflows. Third, runtime isallowedtoaccesstheconcreteobjectreferencedbyarequest.
enforcement must be efficient for production services, where BOLAistheAPI-securityformulationofIDOR:ausermaybe
SQLstatementsexecuteinsideloops,scheduledjobs,orasyn- allowed to call an endpoint, but not allowed to access the ob-
chronous tasks, making per-instance full parsing prohibitively jectidentifiedbythesuppliedparameter(OWASPFoundation,
costly. Fourth, credible evaluation requires paired benign 2023a;MITRECorporation,2026b). Thisisusuallyahorizon-
and adversarial traces covering diverse ownership patterns, talauthorizationproblemwhenuserswithsimilarrolesaccess
subquery-shapedbypasses,andperformancestresscases. oneanother’sobjects.
To address these challenges, we present IDORacle, a Broken Function-Level Authorization concerns whether
template-guided runtime prevention framework for Java-SQL a subject is allowed to invoke a function or endpoint at all.
IDOR vulnerabilities. IDORacle places a lightweight media- BFLAiscommonlyassociatedwithrolehierarchies, adminis-
MyBatis/JDBC-style
tion layer at SQL sinks. At application trator functions, and missing function-level checks (OWASP
2

Foundation, 2023c). A user invoking an administrator-only siblewithoutcomplexsession-variablemanipulationsinlegacy
endpoint is therefore a function-level or vertical authorization configurations.
problem, even if the SQL statement later touches ordinary ThepersistenceofIDORdirectlyfollowsfromthishetero-
rows. Broken Object Property-Level Authorization concerns geneityofownershipsemantics.WhileScenarioAcanbefixed
whether a subject is allowed to access or modify particular by injecting a simple user_id predicate, Scenario B derives
propertiesofanotherwiseaccessibleobject,suchaspasswords, ownershipindirectly. Furthermore,someresourcesmaybelong
tokens, phone numbers, addresses, or internal status fields toatenantratherthanauser,andadministrativeendpointsmay
(OWASPFoundation,2023b). bypassthesechecksentirely. Thesecasesdemonstratethathor-
This distinction matters for system design. A SQL-sink izontal authorization cannot be handled by a naive, one-size-
defense is well-positioned for BOLA/IDOR because the SQL fits-allrowpredicate.
| statement | exposes | the | target | table, | operation, | predicate, | and |     |     |     |     |     |     |     |
| --------- | ------- | --- | ------ | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
bound object identifiers immediately before database execu- 2.3. FromDetectiontoRuntimeEnforcement
| tion. | By contrast, | a   | pure SQL-layer |     | mechanism |     | cannot fully |     |     |     |     |     |     |     |
| ----- | ------------ | --- | -------------- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ExistingworkonBOLAandmissingowner-checkvulner-
infer whether a route is administrator-only without additional abilitiesspansstaticanalysis,directedfuzzing,anddifferential
| route-permission |     | evidence. |     | Similarly, | property-level |     | authori- |                |     |            |     |         |          |               |
| ---------------- | --- | --------- | --- | ---------- | -------------- | --- | -------- | -------------- | --- | ---------- | --- | ------- | -------- | ------------- |
|                  |     |           |     |            |                |     |          | testing (Huang | et  | al., 2024; | Liu | et al., | 2025a,b; | Zhang et al., |
zationmayrequirecolumnpoliciesratherthanrowownership 2025). Theseapproacheseffectivelyidentifywhetheravulner-
| predicates.   |     | IDORacle       | therefore | treats | horizontal  |                | object-level |               |          |      |         |         |          |               |
| ------------- | --- | -------------- | --------- | ------ | ----------- | -------------- | ------------ | ------------- | -------- | ---- | ------- | ------- | -------- | ------------- |
|               |     |                |           |        |             |                |              | able endpoint | exists,  | but  | they    | operate | within a | testing-phase |
| authorization |     | as its primary |           | target | and handles | function-level |              |               |          |      |         |         |          |               |
|               |     |                |           |        |             |                |              | paradigm:     | scanners | flag | missing | checks  | before   | deployment,   |
sufficient
and property-level cases only when evidence can be leavinglegacyproductioncodebasesunprotected. Evenwhena
carriedtotheSQLboundary.
scannersuccessfullyidentifiesaflaw,retrofittingauthorization
constraintsacrossalargemonolithicserviceiserror-proneand
| 2.2. TheArchitecturalRootCauseofJava-SQLIDOR |     |     |     |     |     |     |     | time-consuming. |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
Java web applications commonly distribute authorization Database-level mechanisms such as row-level security
logic across multiple layers. Authentication may be enforced (RLS) and query-rewriting frameworks (Rizvi et al., 2004;
in a servlet filter or gateway. Coarse permission checks may PostgreSQL Global Development Group, 2026; Mehta et al.,
be implemented using annotations, route rules, Shiro, Spring 2017) establish that SQL-layer mediation is feasible, but they
Security, or custom interceptors. Business-specific ownership assume a one-to-one mapping between database users and ap-
checksmayappearinservicemethods. Finally,MyBatisXML plicationusers—anassumptionbrokenbytheconnection-pool
mappers, annotation-based SQL, or JDBC calls execute con- architecturedescribedinSection2.2. Furthermore,theydonot
creteSQLstatements. Thisseparationisusefulforengineering bind Java runtime subject context to individual SQL instances
modularity,butitalsointroducesasemanticgap: thelayerthat across asynchronous boundaries, and they cannot express the
knowsthecurrentsubjectmaynotbethelayerthatobservesthe heterogeneous ownership policies (direct, derived, group, and
concretedatabaseobject. role-sensitive)foundinrealJavaapplications.
Toillustratewhyasinglehard-codedfixisinsufficient,con- ThesetwogapstogetherdefinethedesignspaceforIDORa-
siderthetwovulnerablescenariosshownbelow: cle: aruntimeenforcementlayerthatmediatesSQLexecutions
againstauthenticatedsubjectcontext,operateswithnosource-
| // [Scenario |     | A] Direct | Ownership |     | (Easy) |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
codechangestolegacyservices,andamortizesthecostofpol-
| Controller: |     | requireLogin() |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Mapper: SELECT * FROM t_order icy evaluation through ahead-of-time template planning rather
WHERE id = ? than per-query dynamic rewriting. Detailed comparison with
| // Missing: |     | AND user_id | =   | {curr_user} |     |     |     |                   |     |                 |     |         |             |         |
| ----------- | --- | ----------- | --- | ----------- | --- | --- | --- | ----------------- | --- | --------------- | --- | ------- | ----------- | ------- |
|             |     |             |     |             |     |     |     | related detection |     | and enforcement |     | systems | is provided | in Sec- |
tion9.
| // [Scenario |        | B] Join-Derived |              | (Complex) |        |     |     |                |     |     |     |     |     |     |
| ------------ | ------ | --------------- | ------------ | --------- | ------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
| Controller:  |        | requireLogin()  |              |           |        |     |     |                |     |     |     |     |     |     |
| Mapper:      | SELECT | * FROM          | t_order_item |           |        |     |     |                |     |     |     |     |     |     |
|              | WHERE  | item_id         | =            | ?         |        |     |     | 3. ThreatModel |     |     |     |     |     |     |
| // Missing:  |        | Requires        | JOIN         | t_order   | ON ... |     |     |                |     |     |     |     |     |     |
// AND t_order.user_id = {curr_user} 3.1. AttackerCapabilitiesandObjectives
|                |                 |          |              |     |               |       |               | The           | adversary               | is an | authenticated |                  | low privilege | user of a     |
| -------------- | --------------- | -------- | ------------ | --- | ------------- | ----- | ------------- | ------------- | ----------------------- | ----- | ------------- | ---------------- | ------------- | ------------- |
| In             | both scenarios, |          | the endpoint |     | authenticates |       | the user and  |               |                         |       |               |                  |               |               |
|                |                 |          |              |     |               |       |               | Java database | application.            |       | The           | adversary        | can           | send ordinary |
| the SQL        | selects         | a valid  | row,         | but | no component  |       | verifies that |               |                         |       |               |                  |               |               |
|                |                 |          |              |     |               |       |               | HTTP or       | RPC requests            |       | and freely    | modify           | request       | controlled    |
| the referenced |                 | resource | belongs      | to  | the current   | user. | The bug       |               |                         |       |               |                  |               |               |
|                |                 |          |              |     |               |       |               | identifiers,  | includingpathvariables, |       |               | queryparameters, |               | request       |
isnotamissinglogincheck;itisamissingobject-levelinvari-
|          |            |              |        |           |          |            |             | bodyfields,andRPCarguments.         |     |     |     | Theseidentifiersmaylaterbe |                  |     |
| -------- | ---------- | ------------ | ------ | --------- | -------- | ---------- | ----------- | ----------------------------------- | --- | --- | --- | -------------------------- | ---------------- | --- |
| ant. A   | further    | complication |        | arises    | from the | widespread | use of      |                                     |     |     |     |                            |                  |     |
|          |            |              |        |           |          |            |             | boundtoSQLstatementsasbusinesskeys. |     |     |     |                            | Theadversaryaims |     |
| database | connection | pools        | (e.g., | HikariCP, |          | Druid)     | in Java en- |                                     |     |     |     |                            |                  |     |
toread,update,delete,ortriggerstatechangesonobjectsout-
| terprise | applications. |              | Because | all        | application | users | share the   |                           |     |     |                               |     |     |     |
| -------- | ------------- | ------------ | ------- | ---------- | ----------- | ----- | ----------- | ------------------------- | --- | --- | ----------------------------- | --- | --- | --- |
|          |               |              |         |            |             |       |             | sidetheirauthorizedscope. |     |     | Theadversarymayexploitmissing |     |     |     |
| same     | database      | credentials, | the     | underlying |             | DBMS  | has no vis- |                           |     |     |                               |     |     |     |
ownerchecks,incompleteservicevalidation,controllerpermis-
| ibility | into the | end-user | identity | associated |     | with | each query, |     |     |     |     |     |     |     |
| ------- | -------- | -------- | -------- | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
making native enforcement of user-specific constraints infea- sion omissions, subquery shaped SQL paths, or inconsistent
|     |     |     |     |     |     |     |     | treatment | of group | and | tenant | resources. | The adversary | does |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------ | ---------- | ------------- | ---- |
3

Vanilla SQL App
|     |     | Input Request |     |     |                          |     |     |     |                   |     |     |     | Unauthorized DB Access |     |     |
| --- | --- | ------------- | --- | --- | ------------------------ | --- | --- | --- | ----------------- | --- | --- | --- | ---------------------- | --- | --- |
|     |     | (HTTP/RPC)    |     |     | Fragmented Authorization |     |     |     | Raw SQL Execution |     |     |     |                        |     |     |
DB Result: Tenant B data
Alice / USER
GET /system/dict/type/list?id=2 Controller/ Service checks Query reaches the DB without Output Response: HTTP 200
|     |     |     |     |     | may be missing or inconsistent |     |     |     | ownership constraints |     |     |     | OK cross-tenant data returned |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --------------------- | --- | --- | --- | ----------------------------- | --- | --- |
e.g. SELECT * FROM sys_dict_type
| WHERE dict_id=? |     |     |     |     |     |     |     |     |     |     |     |     |     | IDOR succeeds! |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
IDORacle
Phase 1: Context-Aware Rewrite Phase 2: Runtime Authorization Oracle Protected DB Access
ALLOW
DB Result: 0 Rows
REWRITE
|     |     | Context Propagation |     |     |     |     |     |     |     |     |     |     | Output Response: HTTP |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
404/[] no cross-tenant data
|     |     | Template Planning |     |     |     |     |     |     |     | BLOCK |     |     | returned |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | -------- | --- | --- |
Guard Construction Guard Matching Runtime Validation Redundancy-Aware AUDIT IDOR prevented!
Optimization
Audit Log
decision, context, SQL, resource IDs, outcome
Figure1:OverviewofIDORaclecomparingtheVanillaSQLAppexecutionpathwiththetemplateguidedmediationpath.
not have database credentials, cannot directly modify the pol- by binding the TraceID security context of the user and inter-
icymetadatastore,andcannotforgeauthenticatedidentitiesor ceptingthequeryattheDAOandJDBCboundarytogenerate
servertracebindings. a secured SQL candidate. Phase 2 then engages the runtime
authorizationoracletoevaluatethiscandidateviaguardmatch-
3.2. DefenderCapabilitiesandAssumptions ing, runtime validation, and redundancy aware optimization.
ThedefendercontrolstheJavaapplicationdeployment,the The oracle outputs a definitive action, selecting among allow,
|                  |     |            |     |         |               |     |          | rewrite, | block, | or audit | decisions, | and | records | the | outcome in |
| ---------------- | --- | ---------- | --- | ------- | ------------- | --- | -------- | -------- | ------ | -------- | ---------- | --- | ------- | --- | ---------- |
| SQL interception |     | component, |     | and the | authorization |     | metadata |          |        |          |            |     |         |     |            |
used by IDORacle. The defender can recover authenticated anauditlog. Byenforcingstrictownershipboundariespriorto
|                 |        |           |          |          |            |     |           | execution,   | this | pipeline  | guarantees |         | protected | database | access.    |
| --------------- | ------ | --------- | -------- | -------- | ---------- | --- | --------- | ------------ | ---- | --------- | ---------- | ------- | --------- | -------- | ---------- |
| subject context |        | from the  | existing | security | framework, |     | register  |              |      |           |            |         |           |          |            |
|                 |        |           |          |          |            |     |           | The database |      | evaluates | the        | secured | query     | to yield | zero rows, |
| table and       | column | policies, | and      | deploy   | the system |     | in shadow |              |      |           |            |         |           |          |            |
or enforce mode. The defender does not assume that all con- compellingtheapplicationtoreturnasafeHTTP404orempty
listresponse,therebypreventingcrosstenantdataleakageand
trollers,services,ormapperSQLstatementsarecorrectlypro-
neutralizingtheIDORattempt.
tected.Thetrustedcomputingbaseconsistsoftheentrycontext
extractor, thecontextstore, theSQLhook, themetadatastore, TheIDORacledesigndoesnotreplaceexistingframework
levelauthenticationorroleauthorization.Instead,ittreatsthese
| the mediator, | as  | well as | the underlying |     | JVM | environment | and |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the database engine. These components are assumed to pre- mechanisms as evidence sources and revalidates the concrete
|     |     |     |     |     |     |     |     | objectleveloperationattheSQLsink. |     |     |     |     | Thispositioningispar- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
servetheintegrityoftheinterceptionagentandSQLexecution.
|          |         |      |              |     |          |             |     | ticularly | relevant | for | legacy | Java applications, |     | where | the con- |
| -------- | ------- | ---- | ------------ | --- | -------- | ----------- | --- | --------- | -------- | --- | ------ | ------------------ | --- | ----- | -------- |
| IDORacle | assumes | that | the upstream |     | identity | propagation | in- |           |          |     |        |                    |     |       |          |
frastructureistrustworthyanduncompromised. troller may encode route permissions, the service may apply
|     |     |     |     |     |     |     |     | partial | business | checks, | and | the SQL | mapper | ultimately | exe- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | --- | ------- | ------ | ---------- | ---- |
cutesthedatabaseoperation.
4. Methodology
|     |     |     |     |     |     |     |     | 4.2. Phase1: |     | Context-AwareRewrite |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------------- | --- | --- | --- | --- | --- |
4.1. Overview
|                |     |           |     |                   |     |               |     | Phase | 1   | establishes | the | trusted | identity | anchor | for each |
| -------------- | --- | --------- | --- | ----------------- | --- | ------------- | --- | ----- | --- | ----------- | --- | ------- | -------- | ------ | -------- |
| As illustrated |     | in Figure | 1,  | the architectural |     | vulnerability |     |       |     |             |     |         |          |        |          |
SQLexecutionandcompilesareusablemediationplanbefore
| emerges          | when an | authenticated |            | user, | such as       | Alice, | submits  |              |       |           |            |     |           |              |       |
| ---------------- | ------- | ------------- | ---------- | ----- | ------------- | ------ | -------- | ------------ | ----- | --------- | ---------- | --- | --------- | ------------ | ----- |
|                  |         |               |            |       |               |        |          | any concrete |       | parameter | values     | are | bound.    | It comprises | three |
| a data retrieval |         | request       | triggering |       | an underlying |        | database |              |       |           |            |     |           |              |       |
|                  |         |               |            |       |               |        |          | sequential   | steps | that      | correspond | to  | the three | operational  | lines |
query. WithintheVanillaSQLAppexecutionpath,fragmented
|                         |          |        |                                 |         |           |            |           | shown        | in Figure | 1:         | binding | the         | TraceID | security   | context, |
| ----------------------- | -------- | ------ | ------------------------------- | ------- | --------- | ---------- | --------- | ------------ | --------- | ---------- | ------- | ----------- | ------- | ---------- | -------- |
| authorization           | allows   | this   | request                         | to      | bypass    | incomplete | con-      |              |           |            |         |             |         |            |          |
|                         |          |        |                                 |         |           |            |           | intercepting |           | the SQL    | at the  | Data Access | Object  | (DAO)/JDBC |          |
| trollerorservicechecks. |          |        | Consequently,therawSQLexecution |         |           |            |           |              |           |            |         |             |         |            |          |
|                         |          |        |                                 |         |           |            |           | boundary,    | and       | generating |         | the secured | SQL     | candidate  | that is  |
| proceeds                | directly | to the | database                        | without | enforcing |            | ownership |              |           |            |         |             |         |            |          |
forwardedtoPhase2forevaluation.
| constraints. | Thisstructuralflawleadstounauthorizeddatabase |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
access, ultimately yielding an HTTP 200 OK response that Contextpropagation.
ASQLinstancecanbemediatedonlyif
| exposes | cross tenant | data | and | signifies | a   | successful | IDOR |     |     |     |     |     |     |     |     |
| ------- | ------------ | ---- | --- | --------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
itisboundtotheauthenticatedsubjectthattriggeredit.IDORa-
attack.
clethereforepropagatesaserver-sideidentityrecordratherthan
Fortheidenticalinputrequest,theIDORacleexecutionpath
|     |     |     |     |     |     |     |     | trustinguser-controlledrequestparameters. |     |     |     |     |     | Attheapplication |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- |
mitigatesthevulnerabilitythroughatwophasetemplateguided
entrypoint,thesystemextractstheauthenticatedprincipaland
| mediation | pipeline. | Phase | 1 executes |     | a context | aware | rewrite |     |     |     |     |     |     |     |     |
| --------- | --------- | ----- | ---------- | --- | --------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
4

Table1:MainfieldsinaTemplatePlan.
storesacompactidentityrecord(Eq.(1)):
ctx:{traceId}(cid:55)→{userId, role, tenantId, Field Description
(1)
sessionAttr, policyVersion}. templateHash Fingerprint of the normalized SQL tem-
plateanditsexecutioncontext.
| Only the       | identity | record | is propagated    | through | Mapped     | Diag-   |           |     |     |         |       |      |            |
| -------------- | -------- | ------ | ---------------- | ------- | ---------- | ------- | --------- | --- | --- | ------- | ----- | ---- | ---------- |
|                |          |        |                  |         |            |         | operation |     | SQL | command | type, | such | as SELECT, |
| nostic Context | (MDC),   |        | Remote Procedure |         | Call (RPC) | attach- |           |     |     |         |       |      |            |
UPDATE,DELETE,orINSERT.
ments, message headers, or scheduled-task wrappers to reli- tables DatabasetablestouchedbytheSQLAST,
ablybridgethesemanticgapacrossthreadboundaries;thisfol- includingsubqueries.
lowsthegeneralpracticeofcarryingopaqueexecutioncontext columns Selected, updated, or predicate-related
rather than trusting user-supplied identity fields (World Wide columns.
Web Consortium, 2021). The full identity record remains in riskClass Public table, direct ownership, derived
ownership,groupownership,statetransi-
| the trusted | server-side |     | store. At | the SQL | sink, | the mediator |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --------- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
tion,sensitivecolumn,oradmin-onlyac-
firstchecksashort-livedlocalcacheandthenfallsbacktothe
cess.
| sharedcontextstore. |           | Missingorexpiredcontextistreatedasa |              |     |            |            |        |     |                                     |     |     |     |     |
| ------------------- | --------- | ----------------------------------- | ------------ | --- | ---------- | ---------- | ------ | --- | ----------------------------------- | --- | --- | --- | --- |
|                     |           |                                     |              |     |            |            | guards |     | Metadata-boundguardsthatmustbeeval- |     |     |     |     |
| fail-closed         | condition | unless                              | the callsite | is  | explicitly | registered |        |     |                                     |     |     |     |     |
uatedforthetemplate.
| asasystemtask. |     | Thisrulepreventssilentlyallowingattacker- |     |     |     |     |              |     |                                       |     |     |     |     |
| -------------- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------ | --- | ------------------------------------- | --- | --- | --- | --- |
|                |     |                                           |     |     |     |     | resourceKeys |     | Parameterpositionsorexpressionsusedto |     |     |     |     |
triggeredSQLstatementswhencontextpropagationfails. deriveprotectedresources.
|     |     |     |     |     |     |     | action |     | Plannedmediationaction: |     |     | allow, | rewrite, |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------------------- | --- | --- | ------ | -------- |
Template planning. IDORacle separates SQL-template analy- probe,block,mask,oraudit.
sisfromper-instancemediation.TheSQLhookinterceptsapa-
rameterizedSQLtemplateattheDAO/JDBCboundarybefore
Table2:GuardtypesusedforJava-SQLIDORmediation.
concretevaluesareboundandconstructsatemplatefingerprint
h (Eq.(2)):
| T   |     |     |     |     |     |     | Guard |     | Purpose |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
h = H(mapperId,normalizedAst,commandType, Directownership Addsorverifiesanownerpredicatewhenthe
T
parameterMappings,callsiteHash,policyVersion). targettablehasanexplicitownercolumn.
|     |     |     |     |     |     |     | Derivedownership |     | Derivesauthorizationthroughaparenttable, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
(2)
foreign-keyrelation,orconfiguredjoinpath.
|           |            |     |             |           |          |          | Group/tenant | mem- | Resolves |     | group or   | tenant | membership  |
| --------- | ---------- | --- | ----------- | --------- | -------- | -------- | ------------ | ---- | -------- | --- | ---------- | ------ | ----------- |
| Including | the mapper |     | identifier, | parameter | mapping, | callsite |              |      |          |     |            |        |             |
|           |            |     |             |           |          |          | bership      |      | through  | a   | membership | table  | or resource |
hash, and policy version prevents unrelated SQL statements probe.
with similar Abstract Syntax Tree (AST) shapes from sharing Role/statepolicy
Checksactorrole,forbiddenself-approval,or
| anauthorizationplan. |     | Thisstrictfingerprintingreducestherisk |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allowedstatetransition.
thattemplateplansareinadvertentlysharedacrosssemantically Sensitive-column Blocks,masks,orauditsunauthorizedaccess
distinct SQL statements or invalidated policy versions. If the policy toprotectedcolumns.
fingerprint is unseen, the planner normalizes the SQL, parses Publictable Allows explicitly registered dictionary or
its AST, extracts command type, tables, joins, subqueries, configurationtables.
selected or updated columns, and predicate-related parameter Admin-onlypolicy Requires administrator or privileged-route
evidenceforprotectedoperations.
| positions,     | and then       | binds | these facts   | to policy | metadata.   | The          |             |          |            |     |          |            |           |
| -------------- | -------------- | ----- | ------------- | --------- | ----------- | ------------ | ----------- | -------- | ---------- | --- | -------- | ---------- | --------- |
| output is      | a TemplatePlan |       | (summarized   | in        | Table       | 1), which is |             |          |            |     |          |            |           |
| cached locally | and            | can   | be replicated | to a      | distributed | cache in     |             |          |            |     |          |            |           |
|                |                |       |               |           |             |              | centralized | approach | eliminates |     | the need | to scatter | redundant |
multi-instancedeployments.
|            |              |     |                  |             |        |           | authorization                  | checks | across | various | services,                | ensuring | easier |
| ---------- | ------------ | --- | ---------------- | ----------- | ------ | --------- | ------------------------------ | ------ | ------ | ------- | ------------------------ | -------- | ------ |
| Template   | planning     |     | is the principal | performance |        | optimiza- |                                |        |        |         |                          |          |        |
|            |              |     |                  |             |        |           | auditinganduniformenforcement. |        |        |         | Table2liststheguardtypes |          |        |
| tion. Java | applications |     | often execute    | a small     | number | of SQL    |                                |        |        |         |                          |          |        |
usedbyIDORacle.
templatesmanytimesinloops,scheduledjobs,orbranch-heavy
business logic. IDORacle therefore performs expensive pars- A table can carry multiple guards. For example, an order
|     |     |     |     |     |     |     | table may | use direct | ownership |     | for ordinary | user | operations |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------- | --- | ------------ | ---- | ---------- |
ing,normalization,tableclassification,andpolicybindingonce
|              |     |       |               |      |         |             | andanadmin-onlyguardforback-officeoperations. |       |             |     |                  |     | Atenant-   |
| ------------ | --- | ----- | ------------- | ---- | ------- | ----------- | --------------------------------------------- | ----- | ----------- | --- | ---------------- | --- | ---------- |
| per template | and | keeps | per-execution | work | limited | to identity |                                               |       |             |     |                  |     |            |
|              |     |       |               |      |         |             | membership                                    | table | may combine |     | group membership |     | and state- |
recordbinding,parameterextraction,prooflookup,andguard-
|     |     |     |     |     |     |     | transition | guards. | A user | table may | combine | direct | ownership |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------ | --------- | ------- | ------ | --------- |
specificmediation.
|     |     |     |     |     |     |     | with sensitive-column |     | mediation. |     | Table | 3 illustrates | represen- |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---------- | --- | ----- | ------------- | --------- |
Guard construction. The planner attaches guards to a SQL tative policy metadata entries. The guards are deliberately ex-
|          |           |     |              |        |         |         | plicit: IDORacle |     | does not | infer | ownership | from | arbitrary col- |
| -------- | --------- | --- | ------------ | ------ | ------- | ------- | ---------------- | --- | -------- | ----- | --------- | ---- | -------------- |
| template | according | to  | the metadata | of the | touched | tables, |                  |     |          |       |           |      |                |
columns,andoperations. Aguarddescribeshowauthorization umn names alone, because such inference would create both
should be established for a protected database object. To falsepositivesandunsafebypasses.
| minimize    | deployment  |          | overhead,      | these guards | and           | associated |     |     |     |     |     |     |     |
| ----------- | ----------- | -------- | -------------- | ------------ | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| metadata    | are defined | via      | a centralized, | declarative  |               | configura- |     |     |     |     |     |     |     |
| tion (e.g., | YAML        | or JSON) | maintained     | by           | the defender. | This       |     |     |     |     |     |     |     |
5

Table3:Examplesofauthorizationmetadata.
|     |     |     |     |     |     |     |     | Runtime                | validation. |     | Not every                      | protected | operation |     | can be ex- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | ----------- | --- | ------------------------------ | --------- | --------- | --- | ---------- |
|     |     |     |     |     |     |     |     | pressedasrowownership. |             |     | Atenant-joinapprovalmayrequire |           |           |     |            |
Object Policymetadata theactortobeanadministratorofthetenantandnottheappli-
t_order Directownercolumnuser_id. cantwhoserequestisbeingapproved. Auser-listquerymaybe
t_order_item Derived owner via order_id → legitimate for ordinary users but unsafe if it returns password
t_order.id. hashes, tokens, phone numbers, or addresses. IDORacle han-
xxl_job_info Groupownerviajob_group. dlesthesecaseswithrole/stateandsensitive-columnguards.
sys_user_tenant Role/stateguardfortenantapproval. A role/state guard checks the actor role, the protected re-
| sys_user.password |     |     | Sensitive |     | column | blocked | for non- |         |     |            |         |           |            |     |            |
| ----------------- | --- | --- | --------- | --- | ------ | ------- | -------- | ------- | --- | ---------- | ------- | --------- | ---------- | --- | ---------- |
|                   |     |     |           |     |        |         |          | source, | the | old state, | and the | requested | transition |     | before the |
adminusers.
|            |     |     |                        |     |     |     |     | DML | statement | is executed. |     | When | the condition |     | can be ex- |
| ---------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ---- | ------------- | --- | ---------- |
| t_sku_dict |     |     | Publicdictionarytable. |     |     |     |     |     |           |              |     |      |               |     |            |
pressedsafelyinSQL,itiscompiledintoanEXISTSpredicate.
|              |                            |     |         |     |           |          |     | Otherwise,                           |            | the mediator | issues                            | a   | proof query | and         | blocks the |
| ------------ | -------------------------- | --- | ------- | --- | --------- | -------- | --- | ------------------------------------ | ---------- | ------------ | --------------------------------- | --- | ----------- | ----------- | ---------- |
|              |                            |     |         |     |           |          |     | updateiftheprooffails.               |            |              | Asensitive-columnguardinspectsthe |     |             |             |            |
| 4.3. Phase2: | RuntimeAuthorizationOracle |     |         |     |           |          |     |                                      |            |              |                                   |     |             |             |            |
|              |                            |     |         |     |           |          |     | SELECT                               | projection |              | and applies                       | the | configured  | action:     | block,     |
| Phase        | 2 evaluates                | the | secured | SQL | candidate | produced | by  |                                      |            |              |                                   |     |             |             |            |
|              |                            |     |         |     |           |          |     | rewritetoNULL,maskthecolumn,oraudit. |            |              |                                   |     |             | Forexample: |            |
Phase1againsttheruntimeidentityrecordandboundparame-
Allow,Rewrite,Block,or
ters,issuingoneoffourdecisions: SELECT user_id, username, password, mobile FROM sys_user
⇒
| Audit(showninFigure1). |     |     | Theoraclecomprisesthreeconcur- |     |     |     |     |        |          |           |     |         |           |     |     |
| ---------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | ------ | -------- | --------- | --- | ------- | --------- | --- | --- |
|                        |     |     |                                |     |     |     |     | SELECT | user_id, | username, |     | NULL AS | password, |     |     |
rentsub-components—guardmatching,runtimevalidation,and CONCAT(’***’, RIGHT(mobile, 4)) AS mobile FROM sys_user
redundancy-awareoptimization—formalizedinAlgorithm1.
|     |     |     |     |     |     |     |     | High-risk | columns | such | as  | passwords | and | tokens | are blocked |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | --- | --------- | --- | ------ | ----------- |
Guard matching. At runtime, the instance mediator evaluates by default unless route and role evidence explicitly authorize
| theTemplatePlanagainstthecurrentidentityrecordandbound |        |     |          |               |     |      |            | theaccess.       |     |               |     |     |            |     |            |
| ------------------------------------------------------ | ------ | --- | -------- | ------------- | --- | ---- | ---------- | ---------------- | --- | ------------- | --- | --- | ---------- | --- | ---------- |
| parameters.                                            | If the | SQL | template | is registered |     | as a | public ta- |                  |     |               |     |     |            |     |            |
|                                                        |        |     |          |               |     |      |            | Redundancy-aware |     | optimization. |     |     | The result | of  | each guard |
bleaccess,themediatorissuesanAllowdecisionimmediately.
|     |     |     |     |     |     |     |     | evaluationiscachedasanauthorizationproofh |     |     |     |     |     | P (Eq.(3)): |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
Ifthetemplatetouchesaprotectedtable,themediatorextracts
| concreteresourcekeysaccordingtotheplanandevaluatesthe |     |     |     |     |     |     |     |     |     | =                                   |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|                                                       |     |     |     |     |     |     |     |     | h   | H(traceId,subjectHash,templateHash, |     |     |     |     |     |
| attachedguards.                                       |     |     |     |     |     |     |     |     | P   |                                     |     |     |     |     | (3) |
operation,resourceKey,policyVersion).
Fordirectownership,theguardinsertsatrustedownerpred-
icateusingtheSQLASTratherthanstringconcatenation:
|     |     |     |     |     |     |     |     | Theauthorizationproofrecordsthedecision, |     |     |     |     |     | evidencesource, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
SELECT * FROM t_order WHERE id = ? resolved resource attributes, guard type, and expiration time.
⇒
|        |        |         |       |        |             |     |     | To  | balance | performance | and | consistency |     | in concurrent | envi- |
| ------ | ------ | ------- | ----- | ------ | ----------- | --- | --- | --- | ------- | ----------- | --- | ----------- | --- | ------------- | ----- |
| SELECT | * FROM | t_order | WHERE | id = ? | AND user_id | =   | ?   |     |         |             |     |             |     |               |       |
ronments,authorizationproofsareassignedashorttime-to-live
The appended parameter is bound from ctx:{traceId}, not (TTL).Writeoperationstriggerabest-effortcacheevictionfor
| from the | attacker-controlled |     | request. |     | UPDATE | and | DELETE |     | affected |          |       |       |                |     |             |
| -------- | ------------------- | --- | -------- | --- | ------ | --- | ------ | --- | -------- | -------- | ----- | ----- | -------------- | --- | ----------- |
|          |                     |     |          |     |        |     |        | the |          | resource | keys, | while | policy-version |     | changes im- |
statementsareconstrainedinthesamewaysothatunauthorized mediatelyinvalidateallstaleauthorizationproofs. Thismech-
rowsarenotmodified.
|     |     |     |     |     |     |     |     | anism | is directly | reflected | in  | Algorithm | 1   | (lines | 6–8), where |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --------- | --- | --------- | --- | ------ | ----------- |
Forderivedownership,themediatorusesmetadatatocon- acachehitshort-circuitsguardevaluationentirely,eliminating
nectachildtabletoanowner-bearingparenttable. Whensafe redundantmediationforhotSQLtemplatesthatrecurinloops,
SQLrewritingispossible—typicallyinsingle-tablequeriesor
paginatedqueries,orscheduledtasks.
straightforwardjoins—itinsertsanEXISTSpredicate:
SELECT * FROM t_order_item i WHERE i.id = ? Algorithm1SQL-SinkMediationLogic
⇒
Require: SQLtemplateT;boundparametersB;identityrecord
| SELECT | * FROM | t_order_item |     | i WHERE | i.id = | ?   |     |     | r   |     |     |     |     |     |     |
| ------ | ------ | ------------ | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MediatedSQLAST,oraBlockdecision
| AND EXISTS | (SELECT | 1   | FROM t_order | o   |     |     |     | Ensure: |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
C←LoadContext(r)
| WHERE o.id | = i.order_id |     | AND | o.user_id | = ?) |     |     | 1:  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ifC=∅and¬IsSystemTask(T)then
| However, | AST     | rewriting | can     | inadvertently | alter | query  | seman- | 2:       |        |                   |     |     |     |     |     |
| -------- | ------- | --------- | ------- | ------------- | ----- | ------ | ------ | -------- | ------ | ----------------- | --- | --- | --- | --- | --- |
|          |         |           |         |               |       |        |        | 3:       | return | Block{failclosed} |     |     |     |     |     |
| tics. If | the SQL | dialect,  | complex | aggregations  |       | (GROUP | BY),   | 4: endif |        |                   |     |     |     |     |     |
unions(UNION),orcertainDataManipulationLanguage(DML) 5: P←GetOrCompilePlan(T)
structuresrenderrewritingunsafe,themediatorgracefullyfalls 6: ifP.riskClass=Publicthen
backtoaproofquery(Probe-then-Allow)underthesamere- 7: return Allow
8: endif
| questtrace. |     |     |     |     |     |     |     | K←ExtractResourceKey(B,P) |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
9:
Forgroup-ortenant-ownedresources,themediatorfirstre- 10: hP ←H(r,C,P,K)
ifCacheHas(hP)then
| solves the     | protected | resource |     | and then | checks | membership. | A     | 11: |        |              |     |     |     |     |     |
| -------------- | --------- | -------- | --- | -------- | ------ | ----------- | ----- | --- | ------ | ------------ | --- | --- | --- | --- | --- |
|                |           |          |     |          |        |             |       | 12: | return | CacheGet(hP) |     |     |     |     |     |
| job operation, | for       | example, | may | receive  | only   | job_id,     | while |     |        |              |     |     |     |     |     |
13: endif
authorization is defined over job_group. The mediator re- 14: D←EvaluateGuards(P.guards,C,K)
solves the group and verifies membership before the original 15: CachePut(hP,D){shortTTL}
|     |     |     |     |     |     |     |     | 16: | return D |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
SQLispermitted.
6

4.4. ProtectedDatabaseAccessandEnforcementOutcomes object-level authorization is missing, incomplete, or incon-
TheoracledecisionproducedbyPhase2determinestheob- sistently placed in Java application code. Instead of testing
servableoutcomeatboththedatabaselayerandtheapplication onlywhetheranHTTPendpointisreachable,eachbenchmark
responselayer,correspondingtotheProtectedDBAccessbox
casefollowsthecompletepathfromrequesttodatabaseeffect.
in Figure 1. When the identity record is bound and the Tem- A case therefore specifies the authenticated principal, the
platePlancarriesavalidownership-constrainedSQLcandidate, attacker-controllablerequestfield,theSQLtemplateissuedby
thedatabaseevaluatestherewrittenstatementandreturnszero theapplication,theprotected-tablemetadata,andtheexpected
rowsforunauthorizedobjectreferences,compellingtheappli- databaseandresponse-leveloutcomes.
cationtoreturnasafeHTTP404oranemptylistresponse. No
5.1. DesignGoals
cross-tenantdataisexposed, andtheIDORattemptisneutral-
ized.Eachdecisionisrecordedintheauditlogwiththeidentity The benchmark has three primary goals. First, it covers
record,SQLfingerprint,guardtype,andoutcometimestamp. common object-level authorization failures in Java-SQL ap-
plications, including unauthorized reads, updates, deletes, and
Operationalmodes. IDORaclesupportstwomodesgoverning batch operations. Second, it includes ownership patterns that
how oracle decisions are applied. In shadow mode, the cannot be handled by a single hard-coded predicate, such as
framework records decisions and potential SQL differences ownership derived through a parent table, group membership,
without altering application behavior; this mode is used tenantmembership,oraconfiguredresolverrelation. Third,it
to validate metadata configurations, estimate false-positive stresses the runtime cost of mediation by including repeated
rates, and identify legitimate cross-object queries that require SQLtemplates,loop-generatedmappercalls,andbranch-heavy
explicit policy exceptions prior to production enforcement. In service paths. These goals allow the benchmark to measure
enforce mode, the oracle decision is applied before the SQL boththesecurityefficacyofIDORacleandthepracticalbenefit
statement reaches the database. An Allow decision permits ofitsredundancy-awareoptimization.
the original SQL to execute unmodified. A Rewrite decision
substitutes the original AST with the ownership-constrained 5.2. PrincipalsandProtectedObjects
SQL candidate, producing the zero-row database result and
The benchmark uses a compact but heterogeneous Java-
safeHTTPresponseillustratedinFigure1. ABlockdecision
SQL data model. The schemas cover users, orders, addresses,
prevents database execution entirely. An Audit decision
dictionary records, notices, scheduled jobs, job groups, job
permitsexecutionwhilerecordingatamper-evidentlogentry.
logs, tenants, and user-profile data. In total, the benchmark
comprises comprehensive vulnerability scenarios synthesized
Fail-closedstrategy. Toensureoperationalresilience,IDORa-
from real-world CVE reports affecting open-source Java
cleadoptsafail-closedstrategyforallcriticalerrorconditions.
applications. TheRuoYi-derived casesaregrounded inpublic
Missing identity record, absent policy metadata for protected
CVE and advisory records (National Vulnerability Database,
tables,conflictingownerpredicates,failedmembershipprobes,
2025a,b,c,d,e,f,g,h; CVE Public Advisory Repository, 2025;
andunauthorizedsensitive-columnaccessesareallblockedby
RuoYi Project, 2026), while the additional XXL-Job and
default rather than permitted. This design guarantees that un-
BootDo cases are grounded in their public vulnerability
certainty in the authorization state is resolved conservatively,
and project sources (National Vulnerability Database, 2023;
preventing attacker-triggered SQL statements from executing
XXL-JOB Project, 2026; CTFIOT Security, 2024; BootDo
silently when context propagation fails or metadata is incom-
Project, 2026). The protected tables are selected to represent
plete.
different authorization shapes. For example, sys_dict_type
Explicit exception management. Explicit allow rules are and sys_notice use direct ownership through create_by;
required for public dictionary tables, migration tasks, sched- datax_job_info uses direct ownership through a numeric
uled system jobs, and administrator-only workflows. These user_id; xxl_job_info uses group-derived ownership
exceptions are maintained in declarative metadata rather than through job_group; and sys_job_log uses resolver-style
in ad hoc code comments, ensuring that the policy configura- ownership because a log record must be linked back to an
tion remains auditable and version-controlled. Original SQL owner-bearingjobrecord.
comments are normalized and are not trusted as authorization The principal set contains at least two low-privilege users
evidence. When an audit comment is emitted, it carries only from different ownership domains and an administrator. This
an opaque proof identifier; the corresponding evidence is setup separates three behaviors: legitimate self-access, hori-
storedexclusivelyinthetrustedserver-sidechannel,preventing zontalcross-userorcross-tenantaccess,andlegitimateadmin-
comment-injectionbypasses. istrative access. Each protected object is associated with the
security-contextfield thatshouldbeused asauthorizationevi-
dence, such as userId, username, role, or tenantId. The
5. BenchmarkDesign
samemetadataisusedbytheruntimeoracleduringevaluation,
assummarizedlaterinTable5.
ThebenchmarkisdesignedtoevaluatewhetherSQL-level
runtime mediation can prevent IDOR vulnerabilities when
7

5.3. PairedBenignandAdversarialTraces legitimatepublicoradministrativeaccesses. Publicdictionary
Eachfunctionalscenarioisencodedasapairoftraces. The or configuration tables should be allowed when they are not
benign trace uses a resource identifier that belongs to the au- registered as protected objects. Administrator-only operations
thenticated principal and should preserve the original applica- should be allowed only when the authenticated role satisfies
tion behavior. The adversarial trace keeps the same princi- the configured policy. Column-sensitive cases are retained as
pal and endpoint but changes the identifier, transition target, anextensionforsensitive-fieldprotection, buttheyarenotthe
or batch item to a resource owned by another user, group, or main focus of the overview because the central threat in this
tenant. This paired construction is critical to demonstrate that workisobject-levelIDORratherthangeneraldatamasking.
IDORaclemitigatesthevulnerabilitywithoutintroducingfalse Optimization stress cases. These cases expose redundant
positivesthatbreaklegitimateworkflows. mediation work. They include paginated list queries that re-
The overview case follows this construction. Alice is au-
peatedlyexecutethesameSQLtemplatewithdifferentoffsets,
thenticatedasanormaluserandsendsthefollowingrequest: batch updates or deletes that invoke the same mapper method
inside a loop, and switch-branch service paths where differ-
GET /system/dict/type/list?id=2 ent actions reach the same protected table. These cases eval-
uatewhethertemplate-planreuse,metadatareuse,andrequest-
TheapplicationissuestheSQLtemplate:
local deduplication reduce repeated parsing, guard matching,
SELECT * FROM sys_dict_type WHERE dict_id = ? and rewrite-decision generation without changing the security
outcome.
In the vanilla application, the query reaches the database
without an ownership constraint and may return a dictionary
5.5. ExpectedOutcomes
record belonging to another user. Under IDORacle, the same
SQL execution is mediated at the DAO/JDBC boundary. The Foreachcase,thebenchmarkdefinesbothadatabase-level
outcome and a response-level outcome. In the vanilla mode,
securedSQLcandidateaddsthetrustedownershippredicate:
an adversarial trace is expected to reach the database without
SELECT * FROM sys_dict_type WHERE dict_id = ? anownershipconstraintandmayreturnormodifycross-useror
AND create_by = ?
cross-tenant data. In the protected mode, IDORacle produces
one of four outcomes: Allow, Rewrite, Block, or Audit. A
Theadditionalvalueisderivedfromtheserver-sidesecurity
benign trace should be allowed or rewritten without changing
contextratherthanfromattacker-controlledrequestparameters.
thelegitimateresult. Anadversarialreadshouldnotreturnthe
Therefore, the adversarial trace returns zero rows or a safe re-
unauthorizedrow.Anadversarialupdateordeleteshouldeither
sponse such as HTTP 404 or an empty list, while the benign
affectzerorowsafterrewritingorbeblockedbeforeexecution.
traceremainsaccessible.
Anauditrecordshouldcontaintheidentityrecord,subjectcon-
text, SQL fingerprint, protected table, decision, and final out-
5.4. CaseFamilies
come.
Thebenchmarkcontainsfourcasefamilies:
Thisdecoupledexpected-outcomedesignseparatessecurity
Object-level IDOR cases. These cases evaluate the core
correctnessfromapplicationpresentation. DifferentJavaappli-
threat. Horizontal read cases test whether a user can retrieve
cationsmaytranslateanemptyprotectedresultintoHTTP 404,
another user’s row by modifying an identifier in the request.
anemptylist,oragenericforbiddenresponse. Thebenchmark
Horizontal update and delete cases test whether the same ma-
thereforetreatstheabsenceofunauthorizeddataatthedatabase
nipulation can modify or remove unauthorized rows. Batch
level as the core security condition and records the concrete
cases model service code that iterates over a list of attacker-
HTTPresponseassupportingevidence.
supplied identifiers and invokes the same mapper method re-
peatedly. Theexpectedprotectedbehavioriseitherarewritten
5.6. ExecutionModesandMeasurements
SQL statement whose ownership predicate reduces the result
or affected rows to zero, or a Block decision before database Thebenchmarkisexecutedinthreemodes,designedtoiso-
latetheperformanceimpactofIDORacle’scoremechanisms:
execution.
Derived-ownership cases. These cases cover objects
• NO_GUARD: SQL statements are executed as they
whose authorization evidence is not stored directly in the
wouldbeinthevanillaapplication. Thismodeprovides
accessed table. Join-derived cases require the mediator to
the vulnerable baseline and exposes the unauthorized
constrainthetargetrowthrougharelatedparenttable. Group-
databaseresultforadversarialtraces.
andtenant-derivedcasesrequiretheoracletovalidatewhether
thetargetgrouportenantisinthecurrentsubject’spermission • GUARD_NO_CACHE: Every guarded SQL statement
scope. Resolver cases require an EXISTS predicate or an goesthroughthefullruntimeoraclepath,includingSQL
equivalent resolver query to connectthe accessed record to an normalization, guard matching, metadata lookup, own-
owner-bearingtable. Thesecasespreventthebenchmarkfrom ership validation, and rewrite construction. This mode
overfittingtodirectowner = subjectpredicates. representstheworst-caseprotectedexecutionpath.
Policy-boundary cases. These cases check whether
the mediator distinguishes protected object resources from
8

Table4:ImplementationmodulesofIDORacle
|     |     |     |     |     |     |     | ownership | predicate | into | SELECT, | UPDATE, | and | DELETE | state- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---- | ------- | ------- | --- | ------ | ------ |
ments.
Module Technology Responsibility For a direct ownership table, the original query is dynam-
GuardServer SpringBoot Policymanagement icallyrewrittenintoaguardedquerywithanadditionalowner
|             |     |            |     |     | andrewriteservice |     | predicate,asshownbelow: |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --- | ----------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| SQLRewriter |     | JSqlParser |     |     | SQLparsingandAST  |     |                         |     |     |     |     |     |     |     |
|             |     |            |     |     |                   |     | // Original             | SQL |     |     |     |     |     |     |
rewriting
|           |     |           |     |     |            |     | SELECT | * FROM | sys_notice |     | WHERE | notice_id | =   | ?   |
| --------- | --- | --------- | --- | --- | ---------- | --- | ------ | ------ | ---------- | --- | ----- | --------- | --- | --- |
| JavaAgent |     | ByteBuddy |     |     | RuntimeSQL |     |        |        |            |     |       |           |     |     |
interception
|               |     |                    |     |     |                    |     | // Rewritten  | Guarded | SQL           |     |       |           |     |     |
| ------------- | --- | ------------------ | --- | --- | ------------------ | --- | ------------- | ------- | ------------- | --- | ----- | --------- | --- | --- |
| IdentityLayer |     | Servlet/ShiroHooks |     |     | Identityextraction |     |               |         |               |     |       |           |     |     |
|               |     |                    |     |     |                    |     | SELECT        | * FROM  | sys_notice    |     | WHERE | notice_id | =   | ?   |
|               |     |                    |     |     |                    |     | AND create_by |         | = currentUser |     |       |           |     |     |
andpropagation
| RewriteCache |     | ConcurrentHashMap |     |     | Rewritedecision |     |     |          |       |            |      |                 |     |          |
| ------------ | --- | ----------------- | --- | --- | --------------- | --- | --- | -------- | ----- | ---------- | ---- | --------------- | --- | -------- |
|              |     |                   |     |     |                 |     | The | injected | value | is derived | from | the server-side |     | identity |
reuse
ObservabilityUI React+Vite Visualizationand recordratherthanfromattacker-controlledrequestparameters.
benchmarkcontrol Therefore,changinganobjectidentifierintheHTTPrequestis
insufficienttobypasstheguard.
|     |     |     |     |     |     |     | To support |     | external | applications, | we  | implemented |     | a Java |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------- | --- | ----------- | --- | ------ |
• GUARD_WITH_CACHE: IDORacle enables agent. The agent instruments JDBC prepareStatement
redundancy-aware optimization and reuses decisions calls in common connection implementations, including
for repeated normalized SQL templates and repeated MySQL JDBC and Druid. Before a candidate SQL statement
resource checks. This mode represents the common is prepared, the agent checks whether the SQL operation
hot-templatepathinproductionJavaapplications. and table match the configured metadata. If so, it sends
|     |     |     |     |     |     |     | the SQL | and identity |     | record | to the guard | server. | The | guard |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------ | ------------ | ------- | --- | ----- |
Foreveryexecution,thebenchmarkdriverrecordstheorig-
|                                        |     |     |     |     |                |     | server returns |     | one of | three access-control |     | decisions: |     | ALLOW, |
| -------------------------------------- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ------ | -------------------- | --- | ---------- | --- | ------ |
| inalSQL,therewrittenSQLwhenapplicable, |     |     |     |     | theoracledeci- |     |                |     |        |                      |     |            |     |        |
REWRITE,orDENY.AnALLOWdecisionindicatesthatthetarget
sion,theaffectedrows,theresponseclass,thecachehitormiss
|               |                   |         |       |            |             |              | object belongs |                  | to the   | current     | user or   | is a public | resource, |        |
| ------------- | ----------------- | ------- | ----- | ---------- | ----------- | ------------ | -------------- | ---------------- | -------- | ----------- | --------- | ----------- | --------- | ------ |
| status, and   | the processing    |         | time. | These logs | are         | used to com- |                |                  |          |             |           |             |           |        |
|               |                   |         |       |            |             |              | requiring      | no modification. |          | A           | REWRITE   | decision    | indicates | that   |
| pute security | metrics—including |         |       | successful | attack      | prevention   |                |                  |          |             |           |             |           |        |
|               |                   |         |       |            |             |              | the table      | is protected     | and      | requires    | AST-level | injection   |           | of the |
| rate and      | false-positive    | rate—as |       | well as    | performance | metrics,     |                |                  |          |             |           |             |           |        |
|               |                   |         |       |            |             |              | current user’s |                  | identity | constraint. | A DENY    | decision    | is        | issued |
includingaverageoverhead,maximumoverhead,andcacheef-
|     |     |     |     |     |     |     | when the | required | identity | information |     | is unavailable |     | due to |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ----------- | --- | -------------- | --- | ------ |
fectiveness. propagationfailure,enforcingafail-closedbehaviorthataborts
theoperationbeforedatabaseexecution.
6. Implementation Tobridgethesemanticgapbetweenapplication-leveliden-
|     |     |     |     |     |     |     | tities and | JDBC | executions | in  | real-world | systems, | we  | imple- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | --- | ---------- | -------- | --- | ------ |
We implemented IDORacle as a low-intrusion Java-SQL mented framework-specific identity extraction hooks for rep-
runtime defense prototype. The prototype comprises approx- resentative open-source enterprise systems, including RuoYi,
| imately 5.8K | lines | of self-developed |     | Java | code, | excluding |     |     |     |     |     |     |     |     |
| ------------ | ----- | ----------------- | --- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
BootDo,andXXL-Job(RuoYiProject,2026;BootDoProject,
third-party benchmark applications and framework dependen- 2026;XXL-JOBProject,2026). ByinterceptingShiroorcus-
cies, organized into two major components: (1) a backend tom authentication filters, the extracted userId, username,
(∼4.0K
policy engine lines) for ownership metadata manage- androlesarereliablyboundtotheidentityrecordwithoutmod-
ment,access-controldecision-making,andSQLrewriting;and ifyinglegacybusinesscode.
| (2) a Java | agent | (∼1.8K lines) | for | runtime | JDBC | interception, |                  |     |     |       |            |                    |     |     |
| ---------- | ----- | ------------- | --- | ------- | ---- | ------------- | ---------------- | --- | --- | ----- | ---------- | ------------------ | --- | --- |
|            |       |               |     |         |      |               | For performance, |     | the | agent | implements | a rewrite-decision |     |     |
identity propagation, and transparent SQL enforcement. cache. The cache key contains the application name, identity
Table 4 lists the six implementation modules. Concretely, the record, and a fingerprint of the normalized SQL. This opti-
| system exposes |     | three deployment |     | artifacts: | a   | guard server, |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mizationensuresthatrepeatedexecutionsofhigh-frequencyhot
an in-process MyBatis interceptor for the evaluation testbed, templatesavoidredundantparsingandinter-processcommuni-
andtheJavaagentforprotectingexternalapplicationswithout
cationoverhead.
source-codemodification.
| The guard | server | is implemented |     | in  | Spring | Boot. It main- |     |     |     |     |     |     |     |     |
| --------- | ------ | -------------- | --- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tainstheruntimeswitch,identityrecord,guarddecisions,eval- 7. Evaluation
uationlogs,andtable-levelownershipmetadata. Themetadata WeevaluateIDORacletoassessitssecurityefficacy,
prac-
alsosupportsadministratorbypassesforcaseswherecross-user
|     |     |     |     |     |     |     | tical deployability, |     | and | runtime | efficiency | through | a   | series of |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------- | ---------- | ------- | --- | --------- |
accessislegitimate. empiricalexperiments. Theevaluationaddressesthefollowing
ForSQLinterceptioninsidetheevaluationtestbed,IDORa-
fourdistinctresearchquestions:
cleusesaMyBatisStatementHandler.prepareinterceptor.
Before SQL reaches the database, the interceptor obtains the • RQ1(SecurityEffectiveness): DoesIDORacleprevent
| current identity | record, | parses | the | SQL with | JSqlParser | (JSql- |     |     |     |     |     |     |     |     |
| ---------------- | ------- | ------ | --- | -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
horizontalobjectreferenceviolationsacrossdiverseJava
ParserProject,2026),detectstheguardedtable,andinjectsan
9

[VulnerableSQL] [VulnerableLogic] [VulnerableSQL]
UPDATE sys_dict_type job = find(jobId); SELECT * FROM sys_user
SET dict_name = ? update(job);
WHERE dict_id = ?
[IDORacleRewrite] [IDORacleCheck] [IDORacleRewrite]
UPDATE sys_dict_type job = find(jobId); SELECT * FROM sys_user
SET dict_name = ? assert(userOwnsJobGroup); WHERE user_id = ?
WHERE dict_id = ? update(job);
AND create_by = ’alice’
(a)RuoYi(CVE-2025-28407) (b)XXL-Job(CVE-2023-33779) (c)BootDo(CNVD-C-2024-22302)
Figure2:ComparisonofvulnerabledatabaseoperationsandIDORacle’sruntimemediationoutcomesacrossthreereal-worldvulnerabilities.
Table5:Evaluationresourcesandownershipassignmentsusedinthereal-worldcasestudy.
ResourceType ResourceID ResourceName OwnershipAttribute Owner RelatedCVE
DictionaryType 9001 AliceDictionaryType create_by=alice Alice CVE-2025-28407
9002 BobDictionaryType create_by=bob Bob CVE-2025-28407
Notice 9001 AliceNotice create_by=alice Alice CVE-2025-28412
9002 BobNotice create_by=bob Bob CVE-2025-28412
ScheduledJob 9001 AliceJob create_by=alice Alice CVE-2025-28402
9002 BobJob create_by=bob Bob CVE-2025-28402
SQLscenarioswithoutintroducingfalsepositives? (Sec- 7.2. RQ1: SecurityEffectiveness
tion7.2) ToevaluatethefundamentalsecurityefficacyofIDORacle,
• RQ2(PracticalDeployability): Cantheframeworkin- we execute paired benign and adversarial execution traces
across diverse object level authorization configurations. The
tegrate with real world legacy Java web applications to
experimental data reveals a structural vulnerability pattern in
mitigatedocumentedCVEs? (Section7.3)
legacy applications where database mappers execute queries
• RQ3 (Micro Level Performance): What is the latency relying entirely on request supplied resource identifiers. We
overhead introduced by the SQL sink reference monitor classify the evaluated data access paths into two structural
and how effective is the template caching mechanism? paradigms consisting of direct ownership validation and
(Section7.4) complexderivedrelationalvalidation.
For the direct ownership paradigm represented by tables
• RQ4(EndtoEndImpact): HowdoesIDORacleaffect
such as sys dict type and sys notice, the primary threat stems
the end to end response latency of web endpoints under
fromsimpleparametersubstitution. Thebaselinedatademon-
realisticoperationalconditions? (Section7.5)
strates that an adversary can retrieve data belonging to other
tenantswithoutrestriction. UndertheIDORacleconfiguration,
7.1. ExperimentalSetup
theframeworkdynamicallyinterceptsthequeryatthedatabase
The prototype evaluation is conducted on a dedicated
boundaryandappendsanexplicituseridentifierpredicatetothe
testbed utilizing the Spring Boot framework version 2.7 with
abstract syntax tree structure. When Alice attempts an unau-
MyBatis 3.5 and a MySQL 8.0 database management system.
thorizedaccesstargetingBob,theinjectedconstraintforcesthe
TheunderlyingstoragelayerleveragesHikariCPforconnection
databaseenginetoevaluateanemptyresultset.Theapplication
pooling under a shared credential architecture. The hardware
subsequentlytranslatesthisemptypayloadintoasaferesponse
environment comprises an Intel Core i7 processor operating
classsuchasanHTTP404errororanemptydatalist,success-
at 3.6 GHz paired with 16 GB of memory running an Ubuntu
fullyneutralizingthehorizontalescalationattempt.
20.04 long term support operating system. We evaluate and
For the derived relational validation paradigm where
compare three operational configurations. The NO_GUARD
authorizationevidenceresidesinsecondarytables,thesecurity
configurationexecutesqueriesintheiroriginalstatetoestablish
risksexpandsignificantlyduetotheabsenceofexplicitowner
the baseline database behavior. The GUARD_NO_CACHE
columns in the primary target sink. IDORacle addresses this
configuration enforces the entire reference monitor validation
challenge by generating complex subqueries or executing the
flow including parsing and guard matching for every single
probe then allow fallback mechanism. The results confirm a
database statement. The GUARD_WITH_CACHE config-
one hundred percent attack prevention rate across all synthe-
uration activates the dual fingerprint template plan cache to
sizedscenarioswithzerofalsepositives. Legitimateoperations
eliminateredundantanalyticaloverhead.
10

|     |     |     |     |     |     |     |     | Configuration      |     | Statistic               |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------------- |
|     |     |     |     |     |     |     |     | No guard           |     | Avg (label inside bar)  |
|     |     |     |     |     |     |     |     | Guard (no cache)   |     | Max (↑ label above bar) |
| 140 |     |     |     |     |     |     |     | Guard (with cache) |     |                         |
↑128.4
120
100
)sm( ycnetaL
↑88.8
| 80  | ↑76.0 |       |       |     |     |     |     |       |     |       |
| --- | ----- | ----- | ----- | --- | --- | --- | --- | ----- | --- | ----- |
| 60  |       |       | ↑55.0 |     |     |     |     | ↑55.8 |     |       |
|     |       | ↑50.4 |       |     |     |     |     | ↑52.8 |     | ↑49.0 |
↑48.4
|     |     |     |       | ↑41.2 | ↑42.2 |                   |     | ↑43.6 |       |     |
| --- | --- | --- | ----- | ----- | ----- | ----------------- | --- | ----- | ----- | --- |
| 40  |     |     | ↑33.8 |       | ↑36.6 |                   |     |       |       |     |
|     |     |     |       |       |       | ↑29.6 ↑30.2 ↑30.0 |     |       | ↑32.4 |     |
20
31.8 25.8
| 12.2 |     |     | 13.6 |     |         |             |     | 14.3 13.1 |     | 13.4 12.8 |
| ---- | --- | --- | ---- | --- | ------- | ----------- | --- | --------- | --- | --------- |
|      |     | 9.9 | 11.1 | 5.9 | 9.2 8.4 | 5.0 8.3 8.1 |     | 8.7       | 7.3 |           |
0
CVE-2025-28407 CVE-2025-28407 CVE-2025-28412 CVE-2025-28412 CVE-2025-28402 CVE-2025-28402
Auth. (A→A) Unauth. (A→B) Auth. (A→A) Unauth. (A→B) Auth. (A→A) Unauth. (A→B)
|     | Dictionary Type |     |     |     | Notice |     |     | Scheduled Job |     |     |
| --- | --------------- | --- | --- | --- | ------ | --- | --- | ------------- | --- | --- |
Figure3:EndtoendrequestlatencyperexecutionmodeacrossthreeRuoYiIDORvulnerabilitiesreportingmeanandmaximumperformancevalues.
executed by true resource owners consistently pass validation upon the integrity of the primary upstream authentication tier.
without semantic distortion or data reduction. However, the Should the initial JWT or session validation component be
evaluation also indicates that highly convoluted analytical entirely compromised by an attacker, the metadata bound to
structures containing deeply nested aggregations restrict safe the server side trace identity becomes invalid, which validates
rewriteoptions,requiringthemediatortodegradegracefullyto IDORacle as a powerful defense in depth mechanism rather
standalone validation probes which demands optimization to thanatotalreplacementforfundamentalentrycontrol.
sustainoperationalthroughput.
|     |     |     |     |     |     | 7.4. RQ3: MicroLevelPerformance |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
7.3. RQ2: PracticalDeployability
|     |     |     |     |     |     | To evaluate | the micro | level computational | cost | introduced |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------------- | ---- | ---------- |
We assess the practical deployability of the framework by bythedatabasereferencemonitor,wesubjecttheoracleengine
installing the automated Java agent into three widely adopted tohighconcurrencystresstestsundervaryingcachestates. The
opensourceenterpriseplatformsconsistingofRuoYi,BootDo, baselineNOGUARDprocessinglatencyremainsbelow0.001
and XXL Job. The underlying operational problem in these msperqueryinstance. IntheworstcaseGUARDNOCACHE
legacyarchitecturesisthecompletedisconnectionbetweenup- scenario,wheretheengineisforcedtoperformcompletelexi-
stream web authentication and downstream persistence layers, calparsing,tableclassification,contextextraction,andabstract
asdataaccesscallsoperateentirelyviaanonymizedconnection syntaxtreerewritegenerationforeveryexecutioninstance,the
pool flows. We classify the evaluation by framework integra- mean latency reaches 0.17 ms. This performance penalty in-
tion types spanning Apache Shiro security configurations and troducesadiscerniblebottleneckthatscaleslinearlywithquery
customfilterstructures. frequencyinsidebatchapplicationloops.
TheJavaagentachievestransparentenforcementacrossall The activation of the redundancy aware template plan
target applications without requiring any manual source code cache in the GUARD WITH CACHE configuration signif-
modifications to existing business services or mapper XML icantly mitigates this performance limitation. By utilizing
structures. Wevalidatethiscapabilityagainstfourdistinctreal normalized SQL template fingerprints and identity context
worldvulnerabilitiescomprisingCVE202528407,CVE2025 recordstolookupprecompiledmediationstrategies,themean
28412, CVE 2025 28402, and CVE 2025 28413. The agent processing cost drops sharply to 0.017 ms, representing an
successfully hooks the lower level JDBC prepareStatement average performance optimization of ninety percent. This
effectively
interfaceandinterceptseverycandidatequerybeforedatabase reduction demonstrates that the system separates
interaction. ByextractingidentitycontextsfromShirosession the expensive initial structural analysis from the lightweight
attributes and mapping them to downstream trace identifiers, perinstanceparameterbindingwork.
the framework establishes a reliable identity propagation However, a granular evaluation of the cache behavior
bridgeacrossasynchronousexecutionboundaries. reveals a specific operational variance depending on the type
The deployment evaluation demonstrates that IDORacle of persistence framework used by the host application. While
functionsasanonintrusivesafetynetforlegacyinfrastructure staticmappingtoolssuchasMyBatismaintainstabletemplates
where retrofitting security annotations directly into scattered that yield near perfect cache hit ratios, fully dynamic Object
service modules is technically impractical. Nevertheless, the Relational Mapping implementations such as Hibernate or
empirical findings also underscore an inherent architectural JPA often generate highly fragmented and volatile raw SQL
constraint. The deployment success is strictly contingent texts at runtime. In such environments, the template plan
11

fingerprint uniqueness increases, causing a reduction in the realized through Java-SQL database operations. Its protection
overall cache hit rate and driving performance down toward boundary is intentionally narrower than the full space of
the uncached baseline. This finding highlights that lifting access-control failures. The system is effective when an
the interception boundary to higher level abstraction APIs attacker-controlled object identifier reaches a protected SQL
constitutes an essential requirement for highly dynamic data sink and when the relevant authorization relation can be rep-
accessarchitectures. resented by table metadata, ownership predicates, or column
policies.
7.5. RQ4: EndtoEndImpact Several limitations inherently bound this architectural
Weexaminethemacroscopicimpactofthedefenseframe- scope. First, privilege escalation requests executing through
workbytrackingtheendtoendresponselatencyofindividual third-party opaque APIs, rather than downstream observable
web endpoints across the four reproduced enterprise vulnera- SQL sinks, evade interception. Without local protected SQL
bilities. AsillustratedinFigure3,theevaluationencompasses operations, IDORacle lacks the runtime AST manipulation
fourspecificindicatorscomprisingtheaveragetotallatency,the leverage necessary to enforce constraints. Second, accesses
averagerequestlatency, themaximumrequestceiling, andthe that bypass instrumented JDBC drivers—such as complex
average minimum request baseline. The experimental results encapsulated stored procedures without explicit resource
revealastarkcontrastinthebaselineperformancecharacteris- semantics—require manual adapter interventions. Third, if
ticsacrossdifferentbusinessdomains.Forexample,Dictionary access-control decisions rely exclusively on volatile transient
TypeoperationsunderCVE202528407exhibitahigherinher- business states unmapped to database schemas or the identity
entmeanlatencyofapproximately30mswithmaximumspikes record, a purely SQL-layer reference monitor cannot inde-
exceeding120ms,whereasNoticemanagementendpointsun- pendently infer such intent. Fourth, fully automated ORM
derCVE202528412operatewithinatighterdistributionaver- frameworks such as Hibernate or JPA often generate highly
aging around 10 ms due to simpler configuration lookups and dynamic and fragmented SQL strings at runtime; applying
fewerinternaljoinoperations. IDORacledirectlyattherawJDBClayerinsuchenvironments
Whenanalyzingtheexecutionbehavior,weclassifythere- may reduce template cache hit rates, potentially approaching
questsintoauthorizedselfaccesspathsandunauthorizedhori- the GUARD_NO_CACHE performance baseline (∼0.17ms). A
zontalprivilegeescalationpaths.Forauthorizedoperations,the viable mitigation is to lift the interception point to the HQL
referencemonitorintroducesamarginallatencyincreaseacross or Criteria API abstraction layer, where query structure re-
allendpointsduetothemandatoryinterceptionandcontextex- mains stable and the dual-fingerprint mechanism retains its
traction steps. The caching mechanism successfully absorbs a efficiency—though this requires framework-specific adapters
major fraction of this cost, as evidenced by the average mini- beyondthecurrentprototype.
mumrequestindicatorwherecachedrequestsconsistentlyrun A broader avenue for future work is the integration of
severalmillisecondsfasterthantheiruncachedcounterparts. IDORacle with static analysis or authorization-inference tools
A highly compelling and non intuitive finding emerges suchasBolaRayorMOCGuard(Huangetal.,2024;Liuetal.,
when analyzing the unauthorized horizontal escalation paths 2025a). Automatically generating baseline policy templates
where Alice targets resources owned by Bob. Across all from inferred ownership relations would reduce the manual
evaluated CVE scenarios, the end to end latency for blocked configuration overhead for large-scale legacy deployments,
or rewritten adversarial requests is consistently lower than allowingIDORacletoserveastheruntimeenforcementengine
the latency recorded for the corresponding authorized paths. forstaticallyderivedpolicies.
This phenomenon is directly attributable to the structural
effects of the AST rewrite on the database engine execution 8.2. LayerPlacementandDeploymentTrade-offs
plan. Becausetheinjecteduseridentitypredicaterestrictsrow IDORacle does not require developers to rewrite MVC
visibilitytoAlice,thequeryyieldsanemptyresultsetearlyin controllers, service methods, or mapper definitions. This
the database processing pipeline. This early termination short low-intrusion deployment model is important for legacy Java
circuits heavy internal data serialization, memory allocation, systems, where authorization logic is often scattered. By
and large network payload transfers back to the application enforcing object-level constraints at the DAO/JDBC bound-
server. Consequently, the defense mechanism turns a security ary, IDORacle provides a resilient safety net even when
enforcement boundary into an accidental performance opti- service-layerchecksareabsentorincomplete.
mizationformalicioustraffic,ensuringthattheaverageendto However, delaying enforcement to the JDBC layer in-
end response latency remains safely below 35 ms even under troduces specific deployment trade-offs. When a malicious
intensiveautomatedattackcampaigns. request could have been denied at the routing layer via strict
RBAC annotations, intercepting it at the SQL sink means
the application has already expended CPU cycles on routing,
8. Discussion
parameterparsing,andintermediatebusinesslogic. Whilethis
late-enforcement model ensures the database state remains
8.1. ScopeofSQL-SinkEnforcement
secure, it incurs a marginal computational cost prior to rejec-
IDORacle is designed to prevent horizontal object-level tion. Nonetheless,asthemicro-benchmarkandcachingresults
authorization violations whose security effect is ultimately demonstrate, thisoverheadiseffectivelycontained. IDORacle
12

prioritizes a deterministic, unified enforcement point at the 2025a). BACScan and BACFuzz demonstrate that HTTP re-
data-access boundary, complementing rather than supplanting sponseobservationalonemaybeinsufficient,andimprovede-
existingearly-stageauthorizationmechanisms. tection through multi-user differential analysis, runtime infor-
mation,andSQL-levelevidence(Liuetal.,2025b;Dharmaadi
|     |     |     |     |     |     |     |     | et al., 2025). |     | UABScan | further | reveals | inconsistent |     | authenti- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ------- | ------- | ------------ | --- | --------- |
9. RelatedWork
|     |     |     |     |     |     |     |     | cation and | authorization |     | assumptions |     | across | Java | web layers |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ----------- | --- | ------ | ---- | ---------- |
9.1. WebLogicVulnerabilities (Zhang et al., 2025). Empirical and zero-trust-oriented stud-
|                |     |       |     |        |            |     |             | ies reinforce | the | need | to reason | about | BOLA | beyond | simple |
| -------------- | --- | ----- | --- | ------ | ---------- | --- | ----------- | ------------- | --- | ---- | --------- | ----- | ---- | ------ | ------ |
| Access-control |     | flaws | are | widely | recognized |     | as semantic |               |     |      |           |       |      |        |        |
web logic vulnerabilities, distinct from syntactic input- identifierguessing(Wuetal.,2025;Kaur,2026). Collectively,
validation errors. Early systems such as NoTamper, MACE, theseworksadvancethestateofvulnerabilitydiscovery.IDOR-
acleispositioneddifferently:itshiftstheobjectivefromdetect-
andAuthScopereasonabouthiddenparameters,usersessions,
and protocol fields to identify parameter tampering and hor- ingwhetheravulnerableendpointexiststopreventingunautho-
izontal privilege escalation (Bisht et al., 2010; Monshizadeh rizedobjectoperationsattheSQLexecutionboundary,provid-
et al., 2014; Zuo et al., 2017). Complementary static and ingaruntimesafetynetforapplicationswheredetection-phase
black-box studies further demonstrate that authorization remediationisincomplete.
| defects | depend | on application-specific |     |     | workflows, |     | state tran- |     |     |     |     |     |     |     |     |
| ------- | ------ | ----------------------- | --- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
sitions, and business invariants (Sun et al., 2011; Felmetsger 9.3. SQL-LevelPolicyEnforcement
| et al., 2010; |     | Pellegrino | and | Balzarotti, |     | 2014; | Wang et al., |          |     |            |     |          |     |          |          |
| ------------- | --- | ---------- | --- | ----------- | --- | ----- | ------------ | -------- | --- | ---------- | --- | -------- | --- | -------- | -------- |
|               |     |            |     |             |     |       |              | Database | and | middleware |     | research |     | has long | explored |
2026). These analyses establish that the legitimacy of a given fine-grained policy enforcement through query rewriting,
| request | parameter | is  | determined | by  | the authenticated |     | subject, |               |     |        |            |         |     |           |           |
| ------- | --------- | --- | ---------- | --- | ----------------- | --- | -------- | ------------- | --- | ------ | ---------- | ------- | --- | --------- | --------- |
|         |           |     |            |     |                   |     |          | authorization |     | views, | predicated | grants, |     | row-level | security, |
the referenced object, and the backend operation jointly—a and policy-aware adapters. Classical approaches encode
perspective that motivates treating IDOR prevention as a fine-grained authorization decisions as SQL predicates inside
subject–object–operationconsistencyproblem.
|     |     |     |     |     |     |     |     | query processing |     | (Rizvi | et al., | 2004; | Chaudhuri |     | et al., 2007), |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------- | ----- | --------- | --- | -------------- |
Building on this foundation, recent testing systems im- and modern database systems provide row-level-security
| prove logic-vulnerability |     |     | discovery |     | through | stateful | crawling, |            |     |                   |     |     |                |     |             |
| ------------------------- | --- | --- | --------- | --- | ------- | -------- | --------- | ---------- | --- | ----------------- | --- | --- | -------------- | --- | ----------- |
|                           |     |     |           |     |         |          |           | mechanisms | for | policy-controlled |     |     | row visibility |     | (PostgreSQL |
differential
directed fuzzing, multi-user testing, and runtime GlobalDevelopmentGroup,2026;Microsoft,2025). Security
validation. Atropos, EvoCrawl, and Predator emphasize systems such as Qapla, Authorized Updates, and Blockaid
| that realistic |     | vulnerability | discovery |     | requires | valid | sessions, |                     |     |      |                   |     |     |             |        |
| -------------- | --- | ------------- | --------- | --- | -------- | ----- | --------- | ------------------- | --- | ---- | ----------------- | --- | --- | ----------- | ------ |
|                |     |               |           |     |          |       |           | further demonstrate |     | that | application-layer |     |     | data access | can be |
reachable program states, and semantically meaningful inputs protected by mediating SQL outside ordinary business logic
| (Güleretal.,2024;Guoetal.,2025;Wangetal.,2025). |     |     |     |     |     |     | A2CT |           |            |         |     |         |             |     |                |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---------- | ------- | --- | ------- | ----------- | --- | -------------- |
|                                                 |     |     |     |     |     |     |      | (Mehta et | al., 2017; | Eykholt |     | et al., | 2017; Zhang |     | et al., 2022). |
and DRacv further address automated testing and repair for Related middleware and policy-extraction studies address
function-androle-basedaccess-controlflaws(Schlaubitzetal., scalable database access control, query-control interfaces,
| 2025; Xu | et al., | 2025). | These | techniques |     | are complementary |     |               |     |          |                |     |                |     |          |
| -------- | ------- | ------ | ----- | ---------- | --- | ----------------- | --- | ------------- | --- | -------- | -------------- | --- | -------------- | --- | -------- |
|          |         |        |       |            |     |                   |     | and automated |     | recovery | of application |     | access-control |     | policies |
toIDORacle: theyexposeaccess-controldefectsduringtesting (Pappachan et al., 2020; Bogaerts et al., 2021; Shay et al.,
| and analysis | phases, |     | whereas | this | work focuses |     | on enforcing |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | ------- | ---- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
2018;Zhangetal.,2023,2024).
| object-level | authorization |     | for | deployed | Java-SQL |     | applications |       |       |         |           |     |             |     |              |
| ------------ | ------------- | --- | --- | -------- | -------- | --- | ------------ | ----- | ----- | ------- | --------- | --- | ----------- | --- | ------------ |
|              |               |     |     |          |          |     |              | While | these | systems | establish | the | feasibility |     | of SQL-level |
wherevulnerablecodepathsmaypersistinproduction. mediation, typical Java web deployments introduce an ad-
|     |     |     |     |     |     |     |     | ditional | semantic | gap | not addressed |     | by prior | work. | JDBC |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------------- | --- | -------- | ----- | ---- |
9.2. BOLADetectionandOwnershipAnalysis
|              |                  |               |     |            |       |          |               | connection | pools     | execute       | SQL        | under | shared   | database   | cre-       |
| ------------ | ---------------- | ------------- | --- | ---------- | ----- | -------- | ------------- | ---------- | --------- | ------------- | ---------- | ----- | -------- | ---------- | ---------- |
| IDOR         | is characterized |               | as  | a concrete |       | instance | of Broken     |            |           |               |            |       |          |            |            |
|              |                  |               |     |            |       |          |               | dentials,  | rendering | the           | underlying |       | DBMS     | unable     | to observe |
| Object-Level |                  | Authorization |     | (BOLA),    | where | an       | authenticated |            |           |               |            |       |          |            |            |
|              |                  |               |     |            |       |          |               | end-user   | identity. | Authenticated |            | user  | context, | maintained | in         |
user manipulates an object reference to access data or trigger framework security components such as filters, controllers, or
| state transitions |     | outside | the | authorized | scope | (OWASP | Foun- |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | --- | ---------- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
servicemethods,isthereforeinvisibleatthedatabaseboundary.
| dation, | 2023a; | MITRE | Corporation, |     | 2026b; | PortSwigger | Web |           |      |          |      |        |       |          |       |
| ------- | ------ | ----- | ------------ | --- | ------ | ----------- | --- | --------- | ---- | -------- | ---- | ------ | ----- | -------- | ----- |
|         |        |       |              |     |        |             |     | Moreover, | IDOR | policies | span | direct | owner | columns, | join- |
Security Academy, 2026b). Unlike Broken Function-Level derivedownership,grouportenantmembership,role-sensitive
Authorization,theendpointitselfmaybelegitimatelycallable;
|     |     |     |     |     |     |     |     | transitions, | and | sensitive-column |     |     | constraints—a |     | breadth not |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- | ------------- | --- | ----------- |
the violation arises when the concrete object selected by the captured by generic query-rewriting or row-level-security
| request | is not  | owned  | by, visible | to, | or administrable |     | by the    |                   |                                              |          |         |     |              |     |            |
| ------- | ------- | ------ | ----------- | --- | ---------------- | --- | --------- | ----------------- | -------------------------------------------- | -------- | ------- | --- | ------------ | --- | ---------- |
|         |         |        |             |     |                  |     |           | primitives.       | ThisgapmotivatesaJava-SQL-specificdesignthat |          |         |     |              |     |            |
| current | subject | (OWASP | Foundation, |     | 2023c,b).        |     | Effective |                   |                                              |          |         |     |              |     |            |
|         |         |        |             |     |                  |     |           | binds server-side |                                              | identity | context | to  | SQL-template |     | mediation, |
IDOR reasoning therefore requires connecting the authenti- asrealizedbyIDORacle.
| cated principal, |     | attacker-controlled |     |     | object | identifiers, | and the |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------- | --- | --- | ------ | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
backendoperationthatdereferencesthem. 9.4. Java-SQLAccessControl
| Recent        | BOLA-oriented |             | systems      |     | provide | increasingly | pre-   |      |     |      |        |           |     |            |         |
| ------------- | ------------- | ----------- | ------------ | --- | ------- | ------------ | ------ | ---- | --- | ---- | ------ | --------- | --- | ---------- | ------- |
|               |               |             |              |     |         |              |        | RBAC | and | ABAC | remain | important |     | frameworks | for ex- |
| cise evidence |               | for missing | object-level |     | checks. | BolaRay      | infers |      |     |      |        |           |     |            |         |
pressingroles,attributes,andcoarse-grainedauthorizationpoli-
| object-level | authorization |     | models | in  | database-backed |     | applica- |                                      |     |     |     |     |                    |     |     |
| ------------ | ------------- | --- | ------ | --- | --------------- | --- | -------- | ------------------------------------ | --- | --- | --- | --- | ------------------ | --- | --- |
|              |               |     |        |     |                 |     |          | cies(Sandhuetal.,1996;Huetal.,2014). |     |     |     |     | InlegacyJavaenter- |     |     |
tions,whileMOCGuardtargetsmissing-owner-checkvulnera-
prisesystems,however,authorizationlogicisdistributedacross
bilitiesinJavawebapplications(Huangetal.,2024;Liuetal.,
13

filters,annotations,controllers,servicemethods,MyBatismap- References
pers, scheduled jobs, and JDBC calls. The layer that holds
Bisht,P.,Hinrichs,T.,Skrupsky,N.,Bobrowicz,R.,Venkatakrishnan,
the authenticated subject identity is typically separated from
V.N.,2010.NoTamper:Automaticblackboxdetectionofparameter
thelayerthatexecutestheconcreteSQLstatementagainstthe
tamperingopportunitiesinwebapplications,in:Proceedingsofthe
database. This separation creates a last-mile enforcement gap
17thACMConferenceonComputerandCommunicationsSecurity,
thatupstreamframeworkmechanismsdonotdirectlyaddress.
Association for Computing Machinery, New York, NY, USA. pp.
IDORacle targets this gap by placing a reference monitor
607–618. doi:10.1145/1866307.1866375.
at the MyBatis/JDBC boundary as a complementary enforce-
ment point, rather than a replacement for upstream authenti- Bogaerts, J., Lagaisse, B., Joosen, W., 2021. SEQUOIA:Amiddle-
cation or role authorization. Its template-guided design amor- waresupportingpolicy-basedaccesscontrolforsearchandaggre-
gationindata-drivenapplications. IEEETransactionsonDepend-
tizesexpensiveparsing,normalization,tableclassification,and
ableandSecureComputing18,325–339. doi:10.1109/TDSC.201
guard binding at the SQL-template level. Per-instance medi-
8.2889309.
ation then performs context binding, resource-key extraction,
prooflookup,andguard-specificvalidationwithlowoverhead. BootDoProject,2026.BootDo:AnOpen-SourceJavaEEFramework
Thisplacementpreservesexistingbusinesscodewhileenforc- BasedonSpringBootandMyBatis.GitHubrepository.URL:https:
ingobject-levelconstraintsimmediatelybeforeprotectedSQL //github.com/lcg0124/bootdo.accessed:2026-06-20.
statementsreachthedatabase,makingitwell-suitedforlegacy
Chaudhuri, S., Dutta, T., Sudarshan, S., 2007. Finegrainedauthori-
Java-SQLapplicationswhereretrofittingauthorizationintoser-
zationthroughpredicatedgrants,in: Proceedingsofthe23rdIEEE
vicemethodsisimpractical.
International Conference on Data Engineering, IEEE. pp. 1174–
1183. doi:10.1109/ICDE.2007.368972.
10. Conclusion
CTFIOTSecurity,2024. BootDoFrameworkVulnerabilityAnalysis:
UnauthorizedAccess,SQLInjection,InformationDisclosure,and
ThispaperpresentedIDORacle,atemplate-guidedruntime
StoredXSS. URL:https://www.ctfiot.com/206530.html.accessed:
prevention framework for Java-SQL IDOR vulnerabilities.
2026-06-20.
IDORacle bridges the semantic gap between application-level
identity and SQL-level object operations by propagating CVEPublicAdvisoryRepository,2025.PublicRuoYiCVEAdvisory
trusted subject context, compiling reusable SQL-template Cases. GitHubrepository. URL:https://github.com/20210607/cv
mediation plans, and enforcing ownership, membership,
e_public/tree/main/ruoyi_case.accessed:2026-06-20.
resolver-based, role/state, and sensitive-column guards before
Dharmaadi, I.P.A., Alhanahnah, M., Pham, V.T., Mohsen, F., Turk-
protectedstatementsreachthedatabase. Theevaluationshows
men, F., 2025. BACFuzz: Exposing the silence on broken ac-
that IDORacle prevents the tested horizontal object-reference cess control vulnerabilities in web applications. URL: https:
violationswhilepreservingbenignaccesses,withaworst-case //arxiv.org/abs/2507.15984,doi:10.48550/arXiv.2507.15984,
guard latency of 0.17ms and a 90.1% overhead reduction arXiv:2507.15984.
underrewrite-decisioncaching. Theseresultsdemonstratethat
Eykholt, K., Prakash, A., Mozafari, B., 2017. Ensuring autho-
SQL-sinkmediationcanprovideapracticallast-milesafetynet
rizedupdatesinmulti-userdatabase-backedapplications, in: 26th
for legacy Java database-backed applications, complementing
USENIX Security Symposium, USENIX Association, Vancouver,
existing controller-, service-, and external-API authorization BC,Canada.pp.1445–1462. URL:https://www.usenix.org/confe
mechanisms. rence/usenixsecurity17/technical-sessions/presentation/eykholt.
Felmetsger, V., Cavedon, L., Kruegel, C., Vigna, G., 2010. Toward
Declarationofcompetinginterest
automateddetectionoflogicvulnerabilitiesinwebapplications,in:
Proceedings of the 19th USENIX Security Symposium, USENIX
Theauthorsdeclarethattheyhavenoknowncompetingfi- Association. URL:https://www.usenix.org/legacy/event/sec10/te
nancial interests or personal relationships that could have ap- ch/full_papers/Felmetsger.pdf.
pearedtoinfluencetheworkreportedinthispaper.
Güler, E., Schumilo, S., Schloegel, M., Bars, N., Görz, P., Xu, X.,
Kaygusuz, C., Holz, T., 2024. Atropos: Effective fuzzing of
Dataavailability web applications for server-side vulnerabilities, in: Proceedings
ofthe33rdUSENIXSecuritySymposium, USENIXAssociation,
Datawillbemadeavailableonrequest. Philadelphia,PA,USA.pp.1523–1538. URL:https://www.usenix
.org/conference/usenixsecurity24/presentation/guler.
Funding
Guo, X., Kawlay, A., Liu, E., Lie, D., 2025. EvoCrawl: Explor-
ing web application code and state using evolutionary search, in:
Thisresearchdidnotreceiveanyspecificgrantfromfund-
Proceedingsofthe32ndNetworkandDistributedSystemSecurity
ingagenciesinthepublic,commercial,ornot-for-profitsectors. Symposium, The Internet Society. URL: https://www.ndss-
symposium.org/ndss-paper/evocrawl-exploring-web-
application-code-and-state-using-evolutionary-search/,
doi:10.14722/ndss.2025.230366.
14

Hu,V.C.,Ferraiolo,D.,Kuhn,R.,Schnitzer,A.,Sandlin,K.,Miller, National Vulnerability Database, 2025a. CVE-2025-28400 Detail.
R., Scarfone, K., 2014. GuidetoAttributeBasedAccessControl URL: https://nvd.nist.gov/vuln/detail/CVE-2025-28400.
(ABAC)DefinitionandConsiderations. TechnicalReportSpecial accessed:2026-06-20.
Publication800-162.NationalInstituteofStandardsandTechnol-
|     |     |     |     |     |     |     | National Vulnerability | Database, | 2025b. |     | CVE-2025-28402 |     | Detail. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
ogy. doi:10.6028/NIST.SP.800-162.
URL: https://nvd.nist.gov/vuln/detail/CVE-2025-28402.
Huang, Y., Shi, C., Lu, J., Li, H., Meng, H., Li, L., 2024. Detect- accessed:2026-06-20.
| ing broken           | object-level | authorization |             | vulnerabilities |          | in database- |                        |           |        |     |                |     |         |
| -------------------- | ------------ | ------------- | ----------- | --------------- | -------- | ------------ | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
|                      |              |               |             |                 |          |              | National Vulnerability | Database, | 2025c. |     | CVE-2025-28406 |     | Detail. |
| backed applications, |              | in:           | Proceedings | of the          | 2024 ACM | SIGSAC       |                        |           |        |     |                |     |         |
URL: https://nvd.nist.gov/vuln/detail/CVE-2025-28406.
| ConferenceonComputerandCommunicationsSecurity, |     |     |     |     |     | Associa- |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tion for Computing Machinery, New York, NY, USA. pp. 2934– accessed:2026-06-20.
2948. doi:10.1145/3658644.3690227.
|     |     |     |     |     |     |     | National Vulnerability | Database, | 2025d. |     | CVE-2025-28407 |     | Detail. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
https://nvd.nist.gov/vuln/detail/CVE-2025-28407.
| JSqlParserProject,2026.JSqlParser:JavaSQLparser.Softwaredocu- |     |     |     |     |     |     | URL: |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
mentation. URL:https://jsqlparser.github.io/JSqlParser/.accessed: accessed:2026-06-20.
2026-05-29.
|     |     |     |     |     |     |     | National Vulnerability | Database, | 2025e. |     | CVE-2025-28411 |     | Detail. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
https://nvd.nist.gov/vuln/detail/CVE-2025-28411.
| Kaur, B., 2026. | Broken | object | level | authorization | in  | the wild: An | URL: |     |     |     |     |     |     |
| --------------- | ------ | ------ | ----- | ------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
empiricaltaxonomyfrom100+bugbountydisclosures.URL:https: accessed:2026-06-20.
//arxiv.org/abs/2605.25865,doi:10.48550/arXiv.2605.25865,
|     |     |     |     |     |     |     | National Vulnerability | Database, | 2025f. |     | CVE-2025-28412 |     | Detail. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
arXiv:2605.25865. https://nvd.nist.gov/vuln/detail/CVE-2025-28412.
URL:
accessed:2026-06-20.
| Liu,F.,Shi,Y.,Zhang,Y.,Yang,G.,Li,E.,Yang,M.,2025a. |     |               |                     |             |        | MOC-         |                        |           |        |     |                |     |         |
| --------------------------------------------------- | --- | ------------- | ------------------- | ----------- | ------ | ------------ | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
| Guard: Automatically                                |     | detecting     | missing-owner-check |             |        | vulnerabili- |                        |           |        |     |                |     |         |
|                                                     |     |               |                     |             |        |              | National Vulnerability | Database, | 2025g. |     | CVE-2025-28413 |     | Detail. |
| ties in Java                                        | web | applications, | in:                 | Proceedings | of the | 2025 IEEE    |                        |           |        |     |                |     |         |
URL: https://nvd.nist.gov/vuln/detail/CVE-2025-28413.
| SymposiumonSecurityandPrivacy, |     |     |     | IEEEComputerSociety.pp. |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accessed:2026-06-20.
| 903–919. | doi:10.1109/SP61157.2025.00010. |     |     |     |     |     |                        |           |        |     |                |     |         |
| -------- | ------------------------------- | --- | --- | --- | --- | --- | ---------------------- | --------- | ------ | --- | -------------- | --- | ------- |
|          |                                 |     |     |     |     |     | National Vulnerability | Database, | 2025h. |     | CVE-2025-70985 |     | Detail. |
Liu,F.,Zhang,Y.,Li,E.,Meng,W.,Shi,Y.,Wang,Q.,Wang,C.,Lin,
URL: https://nvd.nist.gov/vuln/detail/CVE-2025-70985.
| Z.,Yang,M.,2025b. |     | BACScan: |     | Automaticblack-boxdetectionof |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accessed:2026-06-20.
| broken-access-controlvulnerabilitiesinwebapplications,in: |     |     |     |     |     | Pro- |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
ceedingsofthe2025ACMSIGSACConferenceonComputerand OWASP Foundation, 2021. A01:2021 – Broken Access Control.
CommunicationsSecurity, AssociationforComputingMachinery, OWASP Top 10. URL: https://owasp.org/Top10/A01_2021-
NewYork,NY,USA.pp.1320–1333. doi:10.1145/3719027.37 Broken_Access_Control/.accessed:2026-05-29.
44825.
|                      |     |             |     |           |           |           | OWASP Foundation, | 2023a. | API1:2023    |     | – Broken | Object | Level  |
| -------------------- | --- | ----------- | --- | --------- | --------- | --------- | ----------------- | ------ | ------------ | --- | -------- | ------ | ------ |
| Mehta, A., Elnikety, |     | E., Harvey, | K., | Garg, D., | Druschel, | P., 2017. |                   |        |              |     |          |        |        |
|                      |     |             |     |           |           |           | Authorization.    | OWASP  | API Security |     | Top 10.  | URL:   | https: |
Qapla: Policy compliance for database-backed systems, in: 26th //owasp.org/API-Security/editions/2023/en/0xa1-broken-
USENIX Security Symposium, USENIX Association, Vancouver, object-level-authorization/.accessed:2026-05-29.
URL:https://www.usenix.org/confe
BC,Canada.pp.1463–1479.
rence/usenixsecurity17/technical-sessions/presentation/mehta. OWASP Foundation, 2023b. API3:2023 – Broken Object Property
|     |     |     |     |     |     |     | LevelAuthorization. | OWASPAPISecurityTop10. |     |     |     | URL:https: |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ---------------------- | --- | --- | --- | ---------- | --- |
Microsoft,2025. Row-LevelSecurity. MicrosoftSQLServerDocu- //owasp.org/API-Security/editions/2023/en/0xa3-broken-object-
mentation. URL:https://learn.microsoft.com/en-us/sql/relational- property-level-authorization/.accessed:2026-05-30.
databases/security/row-level-security?view=sql-server-ver17.
accessed:2026-05-30. OWASP Foundation, 2023c. API5:2023 – Broken Function Level
|     |     |     |     |     |     |     | Authorization. | OWASP | API Security |     | Top 10. | URL: | https: |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------ | --- | ------- | ---- | ------ |
MITRE Corporation, 2026a. CWE-284: Improper Access Control. //owasp.org/API-Security/editions/2023/en/0xa5-broken-
CommonWeaknessEnumeration. URL:https://cwe.mitre.org/data function-level-authorization/.accessed:2026-05-29.
/definitions/284.html.accessed:2026-05-30.
|     |     |     |     |     |     |     | OWASP Foundation, | 2025. | A01:2025 | –   | Broken | Access | Control. |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | -------- | --- | ------ | ------ | -------- |
MITRE Corporation, 2026b. CWE-639: Authorization Bypass URL:https://owasp.org/Top10/2025/A01_2025-
OWASPTop10.
Through User-Controlled Key. Common Weakness Enumeration. Broken_Access_Control/.accessed:2026-05-29.
URL:https://cwe.mitre.org/data/definitions/639.html.accessed:
2026-05-30. Pappachan, P., Yus, R., Mehrotra, S., Freytag, J.C., 2020. Sieve: A
middlewareapproachtoscalableaccesscontrolfordatabaseman-
Monshizadeh,M.,Naldurg,P.,Venkatakrishnan,V.N.,2014. MACE: agementsystems.ProceedingsoftheVLDBEndowment13,2424–
Detecting privilege escalation vulnerabilities in web applications, 2437. doi:10.14778/3407790.3407835.
| in: Proceedings | of  | the 2014 | ACM | SIGSAC | Conference | on Com- |     |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
puter and Communications Security, Association for Computing Pellegrino, G., Balzarotti, D., 2014. Toward black-box detection of
Machinery. doi:10.1145/2660267.2660337. logicflawsinwebapplications,in:ProceedingsoftheNetworkand
|     |     |     |     |     |     |     | DistributedSystemSecuritySymposium. |     |     |     | URL:https://www.ndss- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --------------------- | --- | --- |
National Vulnerability Database, 2023. CVE-2023-33779 Detail. symposium.org/wp-content/uploads/2017/09/04_2_1.pdf.
URL: https://nvd.nist.gov/vuln/detail/CVE-2023-33779.
accessed:2026-06-20.
15

PortSwiggerWebSecurityAcademy, 2026a. Accesscontrolvulner- Xu,K.,Zhang,B.,Li,J.,He,H.,Ren,R.,Ren,J.,2025. DRacv: De-
abilities and privilege escalation. Web Security Academy. URL: tectingandauto-repairingvulnerabilitiesinrole-basedaccesscon-
https://portswigger.net/web-security/access-control.accessed: trolinwebapplication.JournalofNetworkandComputerApplica-
| 2026-05-29. |     |     |     | tions240,104191. | doi:10.1016/j.jnca.2025.104191. |     |     |
| ----------- | --- | --- | --- | ---------------- | ------------------------------- | --- | --- |
PortSwigger Web Security Academy, 2026b. Insecure direct object XXL-JOBProject,2026. XXL-JOB:ADistributedTaskScheduling
references. WebSecurityAcademy. URL:https://portswigger.net/ Platform.GitHubrepository.URL:https://github.com/xuxueli/xxl-
web-security/access-control/idor.accessed:2026-05-29.
job.accessed:2026-06-20.
PostgreSQL Global Development Group, 2026. PostgreSQL Docu- Zhang, Q., Liu, F., Lin, Z., Zhang, Y., 2025. Beawareofwhatyou
| mentation: | Row Security | Policies. PostgreSQL | Documentation. |          |                                                   |     |     |
| ---------- | ------------ | -------------------- | -------------- | -------- | ------------------------------------------------- | --- | --- |
|            |              |                      |                | letpass: | DemystifyingURL-basedauthenticationbypassvulnera- |     |     |
URL: https://www.postgresql.org/docs/current/ddl-
|     |     |     |     | bilityinJavawebapplications,in: |     | Proceedingsofthe2025ACM |     |
| --- | --- | --- | --- | ------------------------------- | --- | ----------------------- | --- |
rowsecurity.html.accessed:2026-05-30.
SIGSACConferenceonComputerandCommunicationsSecurity,
|                                                          |                           |          |                     | Association | for Computing Machinery,     | New York, | NY, USA. pp. |
| -------------------------------------------------------- | ------------------------- | -------- | ------------------- | ----------- | ---------------------------- | --------- | ------------ |
| Rizvi, S.,                                               | Mendelzon, A., Sudarshan, | S., Roy, | P., 2004. Extending |             |                              |           |              |
|                                                          |                           |          |                     | 1874–1888.  | doi:10.1145/3719027.3765199. |           |              |
| queryrewritingtechniquesforfine-grainedaccesscontrol,in: |                           |          | Pro-                |             |                              |           |              |
ceedingsofthe2004ACMSIGMODInternationalConferenceon
|            |                      |               |                | Zhang,W.,Bali,D.,Kerney,J.,Panda,A.,Shenker,S.,2023. |     |                          | Access |
| ---------- | -------------------- | ------------- | -------------- | ---------------------------------------------------- | --- | ------------------------ | ------ |
| Management | of Data, Association | for Computing | Machinery. pp. |                                                      |     |                          |        |
|            |                      |               |                | controlfordatabaseapplications:                      |     | Beyondpolicyenforcement, | in:    |
551–562. doi:10.1145/1007568.1007631. ProceedingsoftheWorkshoponHotTopicsinOperatingSystems,
RuoYiProject,2026. RuoYi: ASpringBoot-BasedPermissionMan- AssociationforComputingMachinery. doi:10.1145/3593856.
| agementSystem. | GitHubrepository. | URL:https://github.com/yan |     | 3595905. |     |     |     |
| -------------- | ----------------- | -------------------------- | --- | -------- | --- | --- | --- |
gzongzhuan/RuoYi.accessed:2026-06-20.
|     |     |     |     | Zhang,W.,Bali,D.,Kerney,J.,Panda,A.,Shenker,S.,2024. |     |     | Extract- |
| --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | -------- |
Sandhu,R.S.,Coyne,E.J.,Feinstein,H.L.,Youman,C.E.,1996.Role- ingdatabaseaccess-controlpoliciesfromwebapplications. arXiv
basedaccesscontrolmodels. Computer29,38–47. doi:10.1109/ preprintarXiv:2411.11380.URL:https://arxiv.org/abs/2411.11380.
2.485845.
|     |     |     |     | Zhang,W.,Bali,D.A.,Panda,A.,Shenker,S.,2022. |     |     | Blockaid: Data |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | -------------- |
Schlaubitz,M.,Veyisoglu,O.,Rennhard,M.,2025.A2CT:Automated accesspolicyenforcementforwebapplications,in:Proceedingsof
detectionoffunctionandobject-levelaccesscontrolvulnerabilities the 16th USENIX Symposium on Operating Systems Design and
inwebapplications,in: Proceedingsofthe11thInternationalCon- Implementation,USENIXAssociation. URL:https://www.usenix
ference on Information Systems Security and Privacy, INSTICC. .org/conference/osdi22/presentation/zhang.
| SciTePress.pp.425–436. |     | doi:10.5220/0013092700003899. |     |                |                    |                    |           |
| ---------------------- | --- | ----------------------------- | --- | -------------- | ------------------ | ------------------ | --------- |
|                        |     |                               |     | Zuo, C., Zhao, | Q., Lin, Z., 2017. | AuthScope: Towards | automatic |
Shay,R.,Blumenthal,U.,Gadepally,V.,Hamlin,A.,Darby,J.,Cun-
|          |                   |                    |                | discoveryofvulnerableauthorizationsinonlineservices, |     |     | in: Pro- |
| -------- | ----------------- | ------------------ | -------------- | ---------------------------------------------------- | --- | --- | -------- |
| ningham, | R.K., 2018. Don’t | even ask: Database | access control |                                                      |     |     |          |
ceedingsofthe2017ACMSIGSACConferenceonComputerand
throughquerycontrol.SIGMODRecord47,20–25.doi:10.1145/
|                                            |                       |                  |                   | CommunicationsSecurity, | AssociationforComputingMachinery. |     |     |
| ------------------------------------------ | --------------------- | ---------------- | ----------------- | ----------------------- | --------------------------------- | --- | --- |
| 3316416.3316420.                           |                       |                  |                   | pp.799–813.             | doi:10.1145/3133956.3134089.      |     |     |
| Sun, F.,                                   | Xu, L., Su, Z., 2011. | Static detection | of access control |                         |                                   |     |     |
| vulnerabilities                            | in web applications,  | in: Proceedings  | of the 20th       |                         |                                   |     |     |
| USENIXSecuritySymposium,USENIXAssociation. |                       |                  | URL:https:        |                         |                                   |     |     |
//www.usenix.org/conference/usenix-security-11/static-detection-
access-control-vulnerabilities-web-applications.
Wang,C.,Meng,W.,Luo,C.,Li,P.,2025.Predator:Directedwebap-
plicationfuzzingforefficientvulnerabilityvalidation,in:
Proceed-
ingsofthe2025IEEESymposiumonSecurityandPrivacy,IEEE
| ComputerSociety.pp.886–902. |     | doi:10.1109/SP61157.2025.0 |     |     |     |     |     |
| --------------------------- | --- | -------------------------- | --- | --- | --- | --- | --- |
0066.
Wang,M.,Görz,P.,Schilling,J.,Hassler,K.,Guo,L.,Holz,T.,Ab-
| basi,A.,2026. | Anota:Identifyingbusinesslogicvulnerabilitiesvia |     |     |     |     |     |     |
| ------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
annotation-basedsanitization,in:Proceedingsofthe33rdNetwork
andDistributedSystemSecuritySymposium,TheInternetSociety.
URL: https://www.ndss-symposium.org/ndss-paper/anota-
identifying-business-logic-vulnerabilities-via-annotation-based-
sanitization/.
| World Wide | Web Consortium,                                    | 2021. Trace Context. | W3C Recom- |     |     |     |     |
| ---------- | -------------------------------------------------- | -------------------- | ---------- | --- | --- | --- | --- |
| mendation. | URL:https://www.w3.org/TR/trace-context/.accessed: |                      |            |     |     |     |     |
2026-05-30.
Wu,A.,Feng,Z.,Feng,R.,Xing,Z.,Liu,Y.,2025.Rethinkingbroken
| objectlevelauthorizationattacksunderzerotrustprinciple. |     |     | URL: |     |     |     |     |
| ------------------------------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
https://arxiv.org/abs/2507.02309,doi:10.48550/arXiv.2507.02
309,arXiv:2507.02309.
16