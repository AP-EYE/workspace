> 원본: PII_Bench_ACL26.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 표 참조. PDF의 다단 편집·표·수식이 선형화되었으므로 보고 수치는 원본 PDF를 확인함. -->

| PII-Bench: |     | Evaluating |     | Query-Aware |     | Privacy |     | Protection | Systems |     |     |
| ---------- | --- | ---------- | --- | ----------- | --- | ------- | --- | ---------- | ------- | --- | --- |
HaoShen1,2,ZhouhongGu3,HaoKaiHong1,WeiliHan1,2*,HongfengChai1
1InstituteofFintech,FudanUniversity
2LaboratoryofDataAnalyticsandSecurity,FudanUniversity
3FudanUniversity
|     | {hshen22, | zhgu22, | hkhong23}@m.fudan.edu.cn |     |     | {wlhan, | hfchai}@fudan.edu.cn |     |     |     |     |
| --- | --------- | ------- | ------------------------ | --- | --- | ------- | -------------------- | --- | --- | --- | --- |
NoMasking
|     |     | Abstract |     |     |                                           |     |     |                       |     | I know who you are       |     |
| --- | --- | -------- | --- | --- | ----------------------------------------- | --- | --- | --------------------- | --- | ------------------------ | --- |
|     |     |          |     |     | Hello, my name is Ozer. I am 23years old  |     |     | Can you help me find  |     |                          |     |
|     |     |          |     |     | and I hold a Master's degree. I work at   |     |     | the latest company    |     | now!                     |     |
|     |     |          |     |     | TikTokwith the employee ID EP001.         |     |     | policy?               |     | ⚠️Leakprivacybut helpful |     |
ThewidespreadadoptionofLargeLanguage
All PII Masking
| Models(LLMs)hasraisedsignificantprivacy |     |     |     |     |     |                                |                                    |                              |         | Please specify your  |                   |
| --------------------------------------- | --- | --- | --- | --- | --- | ------------------------------ | ---------------------------------- | ---------------------------- | ------- | -------------------- | ----------------- |
|                                         |     |     |     |     | H   | e l l o ,   m y   n a m e  i s |   < N a m e > .   I   a m   < Age> | C a n   y o u   h e lp  m e  | f in d  | c o m p              | a n y   n a m e . |
concernsregardingtheexposureofpersonally a n d  I   h o l d   a   < D e g r e e > .   I   w o r k   a t  t h e   l a t e s t  c o m pa n y
|                                            |     |     |     |     | <                          | C o m p a n y   N a m e | > w i t h   t h e   < I D > .  | p o l i c y ? |     | Prote c t pr iv | a c y   bu t  h e lpless⚠️ |
| ------------------------------------------ | --- | --- | --- | --- | -------------------------- | ----------------------- | ------------------------------ | ------------- | --- | --------------- | -------------------------- |
| identifiableinformation(PII)inuserprompts. |     |     |     |     | Query-unrelated PIIMasking |                         |                                |               |     |                 |                            |
Toaddressthischallenge,weproposeaquery- H e ll o ,  m y   n a m e  i s   < N a m e > .  I   a m  < A ge > C a n   y o u   h e lp  m e  f in d  H e ll o   < N a m e > !  I ' d  b e   h a p p y
|     |     |     |     |     | an              | d  I   h ol d   a  < D e g | r e e > .  I  w o r k   a t T i kT | o k th e  l a t e s t  c o m pa n | y   | to  h e l p  y o u  f    | in d   t h e  l a t e st   … |
| --- | --- | --- | --- | --- | --------------- | -------------------------- | ---------------------------------- | --------------------------------- | --- | ------------------------ | ---------------------------- |
|     |     |     |     |     | with the <ID>.  |                            |                                    | policy?                           |     | Protectprivacy & helpful |                              |
unrelatedPIImaskingstrategyandintroduce
PII-Bench,thefirstcomprehensiveevaluation
Figure1: TheoverallperformanceofthreePIIMasking
frameworkforassessingprivacyprotectionsys-
|     |     |     |     |     | strategies: |     | NoMasking,AllPIIMasking,andQuery- |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --------------------------------- | --- | --- | --- | --- |
tems. PII-Benchcomprises2,842testsamples unrelated PII Masking. Effective Privacy Protection
across7PIItypeswith55fine-grainedsubcate-
SystemsarerequiredtomaintainLLMs’functionality
gories,featuringdiversescenariosfromsingle- whileprotectuser’sprivacyasmuchaspossible.
subjectdescriptionstocomplexmulti-partyin-
teractions. Each sample is carefully crafted intosubsequentmodeltraining,leadingtoperma-
withauserquery,contextdescription,andstan- nentprivacybreaches(Liuetal.,2023).
dardanswerindicatingquery-relevantPII.Our
Currentpracticesrevealthatthevastmajorityof
empiricalevaluationrevealsthatwhilecurrent users adopt a zero-protection approach when uti-
modelsperformadequatelyinbasicPIIdetec-
lizingLLMservices,submittingoriginalprompts
tion,theyshowsignificantlimitationsindeter-
|        |           |            |      |          | containingPIIdirectlytotheLLMs. |     |     |     |     | Whileanob- |     |
| ------ | --------- | ---------- | ---- | -------- | ------------------------------- | --- | --- | --- | --- | ---------- | --- |
| mining | PII query | relevance. | Even | advanced |                                 |     |     |     |     |            |     |
viousprotectionstrategywouldbetomaskallPII
| LLMs | struggle | with this task, | particularly | in  |     |     |     |     |     |     |     |
| ---- | -------- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
(Nakamuraetal.,2020;Biesneretal.,2022;Lukas
handlingcomplexmulti-subjectscenarios,in-
dicatingsubstantialroomforimprovementin etal.,2023), asshowninFigure1, thisapproach
achievingintelligentPIImasking. significantlycompromisesservicequality. Anideal
PrivacyProtectionSystemshouldmaintainLLMs’
1 Introduction
|     |     |     |     |     | functionality |     | while | maximizing | user | privacy | pro- |
| --- | --- | --- | --- | --- | ------------- | --- | ----- | ---------- | ---- | ------- | ---- |
Recentyearshavewitnessedthewidespreadadop- tection. For instance, when a user inquires about
tionofLargeLanguageModels(LLMs),withan acandidate’ssuitabilityforaseniorresearcherpo-
increasingnumberofusersdirectlyinteractingwith sition,maskingtheireducationalbackgroundand
thesemodelsthroughAPIsforvarioustasks,rang- workexperiencewouldrendertheLLMincapable
ingfromdailyconversationstocomplexanalytical ofmakinganeffectiveassessment.
work(Sunetal.,2023;Yangetal.,2024b;Wong This observation motivates our proposal of a
et al., 2023). Despite the convenience these ser- query-unrelated PII masking strategy: Masking
vices offer, users often overlook a significant pri- onlythePIIirrelevanttouserquerieswhileretain-
vacy risk: the prompts submitted to LLMs fre- ing essential information. In the aforementioned
quentlycontainsubstantialpersonallyidentifiable example, this approach would preserve the can-
information (PII) (Achiam et al., 2023). Such in- didate’seducationalandprofessionalinformation
formationisvulnerablenotonlytointerceptionby while masking unrelated personal details such as
| maliciousactorsduringtransmission(Parastetal., |     |     |     |     | contactinformation. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
2022)butalsotopotentialmisusebyunethicalser- The implementation of query-unrelated PII
viceproviderswhomightcollectandincorporateit masking strategy faces two-tier challenges. The
|                |     |          |     |           | first | involves | accurate | identification |     | of  | all PII |
| -------------- | --- | -------- | --- | --------- | ----- | -------- | -------- | -------------- | --- | --- | ------- |
| *Corresponding |     | authors: |     | Weili Han |       |          |          |                |     |     |         |
wlhan@fudan.edu.cn within the prompt, serving as foundational work.
4991
Proceedingsofthe64thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),pages4991–5026
July2-7,2026©2026AssociationforComputationalLinguistics

Thesecondrequiresdeterminingtherelevanceof riskassessmenttoguidemaskingdecisions. Shen
identified PII to user queries. While existing re- et al. (2024) extended this approach with an end-
search has made progress in basic PII detection, to-endframeworkthatpreservestaskutilityduring
systematicstudiesconsideringqueryrelevancere- privacyprotection. Exploringinformationpreserva-
| mainscarce. |     |     |     |     |     |     | tion,MeisenbacherandMatthes(2024)introduced |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
To advance the field of privacy-preserving lan- differential privacy techniques for text modifica-
guage models, we present PII-Bench, a compre- tion, demonstrating improved semantic retention
hensive evaluation framework designed to assess over traditional masking methods. While these
approacheshaveadvancedprivacyprotectiontech-
| Privacy Protection |     | Systems’ |     | efficacy | in preserv- |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
ing LLMs’ core functionalities while optimizing niques,theyprimarilyfocusondocument-levelsan-
user privacy safeguards. PII-Bench comprising itization without considering the dynamic nature
2,842carefullydesignedtestsamplesacross7PII of user interactions. Our work introduces query-
typeswith55fine-grainedsubcategories,ranging awareprivacyprotectionthatadaptivelybalances
from basic personal information to complex so- informationutilitywithprivacyrequirements.
| cial relationship |             | data. | Each  | sample     | consists | of  |                             |     |     |     |     |
| ----------------- | ----------- | ----- | ----- | ---------- | -------- | --- | --------------------------- | --- | --- | --- | --- |
|                   |             |       |       |            |          |     | 2.2 Query-AwarePIIDetection |     |     |     |     |
| three key         | components: |       | (1) A | user query | simulat- |     |                             |     |     |     |     |
ing real-world information needs. (2) A context Traditional PII detection has evolved from rule-
descriptioncontainingdiversePII.(3)Astandard basedsystems(Ruchetal.,2000;Douglassetal.,
answerindicatingquery-relevantPIIandmasking 2005) to neural architectures (Deleger et al.,
requirements. 2013; Dernoncourt et al., 2017; Johnson et al.,
Ourexperimentalanalysisrevealsthatwhileex- 2020), with recent work demonstrating the effec-
istingmodels,includingBidirectionalLongShort- tivenessoftransformer-basedmodelsinidentifying
|             |     |                  |     |        |     |        | sensitive | information |     | (Asimopoulos | et al., 2024). |
| ----------- | --- | ---------------- | --- | ------ | --- | ------ | --------- | ----------- | --- | ------------ | -------------- |
| Term Memory |     | with Conditional |     | Random |     | Fields |           |             |     |              |                |
(BiLSTM-CRF) (Chen et al., 2017), perform ad- Largelanguagemodelshaveshownpromisingre-
equately in basic PII detection, they demonstrate sultsinrecognizingdiversePIItypes(Singhaletal.,
notablelimitationsindeterminingPIIqueryrele- 2024; Bubeck et al., 2023), yet they treat all sen-
vance. EvenadvancedLLMsfacechallengesinthis sitive information with uniform importance. Our
task,indicatingsubstantialroomforimprovement framework introduces a novel dimension to PII
in achieving intelligent PII masking. Despite the detectionbyincorporatingqueryrelevanceassess-
|     |     |     |     |     |     |     | ment. | Rather | than applying | uniform | protection |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ------------- | ------- | ---------- |
recentadvancesinmodelarchitectureandtraining
techniques, Small Language Models (SLM) still measures, we focus on identifying which PII el-
showconsiderableperformancegapscomparedto ements are essential for addressing user queries.
largerLLMs,particularlyindeterminingPIIquery Thisapproachenablesmorenuancedprivacypro-
| relevance. |     |     |     |     |     |     | tection | by distinguishing |     | between | query-related |
| ---------- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ------- | ------------- |
Theprimarycontributionsofthisworkinclude: andquery-unrelatedsensitiveinformation,though
1. Thefirstproposalofquery-unrelatedPIImask- theactualmaskingorprotectionmechanismsare
lefttodownstreamapplications.
ingstrategy,offeringnovelapproachestomaintain
| LLM service | quality | while | protecting |     | privacy. | 2.  |                                 |     |     |     |     |
| ----------- | ------- | ----- | ---------- | --- | -------- | --- | ------------------------------- | --- | --- | --- | --- |
|             |         |       |            |     |          |     | 2.3 PrivacyProtectionBenchmarks |     |     |     |     |
DevelopmentofPII-Benchevaluationframework,
Existingbenchmarksforevaluatingprivacyprotec-
| enabling | systematic | assessment |     | of models’ |     | capa- |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
bilitiesinPIIidentificationandqueryrelevancede- tion methods have primarily focused on general
termination. 3. Experimentalrevelationofcurrent PII detection capabilities. Pilán et al. (2022) in-
modellimitationsinthistask,providingdirection troducedTAB,abenchmarkbasedonlegalcourt
cases,whichevaluatestextanonymizationperfor-
forfutureresearch.
|     |     |     |     |     |     |     | mance. | However, | it does | not assess | the model’s |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------- | ---------- | ----------- |
2 RelatedWork ability to distinguish query-related information.
|     |     |     |     |     |     |     | The recent | work | by Sun | et al. | (2024) proposed |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | ------ | --------------- |
2.1 Privacy-PreservingTextProcessing
evaluationmetricsforprivacy-preservingprompts,
Text privacy protection has emerged as a critical buttheirfocusremainslimitedtogeneraldesensi-
challengeinnaturallanguageprocessingapplica- tization effectiveness. Li et al. (2024) developed
tions. Papadopoulouetal.(2022)proposedtextsan- LLM-PBEtoassessprivacyrisksinlanguagemod-
itizationthatcombinesentitydetectionwithprivacy els,thoughtheiremphasisisonmodel-sideprivacy
4992

| Symbol | Description                                  |     |     |     |     |     | sonalinformation.                 |         |         |     |         |      |         |
| ------ | -------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------- | ------- | ------- | --- | ------- | ---- | ------- |
| p      | Apromptconsistingofauserdescriptionandaquery |     |     |     |     |     |                                   |         |         |     |         |      |         |
|        |                                              |     |     |     |     |     | (3)Query-UnrelatedPIIMaskingTask: |         |         |     |         |      | This    |
| d      | Userdescriptioncontainingpersonalinformation |     |     |     |     |     |                                   |         |         |     |         |      |         |
|        |                                              |     |     |     |     |     | task is                           | what we | propose | the | optimal | form | of pri- |
| q      | Userqueryspecifyingtheinformationneed        |     |     |     |     |     |                                   |         |         |     |         |      |         |
d′ ModifieddescriptionwithmaskedPII vacyprotectionsystem. Givenpromptp,themodel
| p′  | Modifiedprompt(d′,q)afterPIImasking |     |     |     |     |     |        |          |            |             |     |     |         |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | ----------- | --- | --- | ------- |
|     |                                     |     |     |     |     |     | should | generate | a modified | description |     | d   | ′ where |
Setofsubjectindividualsmentionedinthedescription
| S   |                            |     |     |     |     |     | query-unrelatedPIIentitiesaremaskedwhilepre- |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
| s   | i Thei-thsubjectindividual |     |     |     |     |     |                                              |     |     |     |     |     |     |
CompletesetofPIIentitiesintheprompt serving the necessary ones. Formally, the model
E
|     | i S e t | o f P II e  | nt i ti e s a | ss o c i a t e d w | ithsubjectsi |     |        |          |     |          |         |     |         |
| --- | ------- | ----------- | ------------- | ------------------ | ------------ | --- | ------ | -------- | --- | -------- | ------- | --- | ------- |
| Ei  |         |             |               |                    |              |     | should | identify | and | generate | d where |     | all PII |
| e   | T h e   | j -t h P II | e n t i ty    | o f s u b j e c t  | si           |     |        |          | E q |          | ′       |     |         |
j
Eq SubsetofPIIentitiesnecessaryforansweringqueryq entitiesin q aremaskedwhilepreservingthose
E\E
SetofpredefinedPIItypes in . Themaskingoperationshouldmaintaintext
| T   |     |     |     |     |     |     | q   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E
coherenceandreadabilitywhileensuringeffective
Table1: NotationusedthroughoutinTaskDefinition.
privacyprotectionfornon-essentialpersonalinfor-
ratherthaninputtextprotection. mation. Theresultingpromptp = (d,q)should
|     |     |     |     |     |     |     |     |     |     |     | ′   | ′   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PII-Bench addresses these limitations by pro- enableLLMstoaccuratelyaddressthequerywhile
vidingacomprehensiveevaluationframeworkthat minimizingexposureofirrelevantpersonalinfor-
| assessesbothPIIdetectionaccuracyandtheability |     |     |     |     |          |     | mation.                   |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | -------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
| todeterminequery-relatedinformation.          |     |     |     |     | Thisdual |     |                           |     |     |     |     |     |     |
|                                               |     |     |     |     |          |     | 3.2 PII-BenchConstruction |     |     |     |     |     |     |
focusenablesmorerealisticevaluationofprivacy
protectionsystemsininteractivescenarios,where Basedonthetaskdefinitionabove,wedesignedan
therelevanceofsensitiveinformationvarieswith
automatedprocessforconstructingthePIIevalua-
| userqueries.    |     |     |     |     |     |     | tiondataset,asillustratedinFigure2. |                     |     |     |             |     |        |
| --------------- | --- | --- | --- | --- | --- | --- | ----------------------------------- | ------------------- | --- | --- | ----------- | --- | ------ |
| 3 PII-Benchmark |     |     |     |     |     |     | 3.2.1                               | PIIEntityGeneration |     |     |             |     |        |
|                 |     |     |     |     |     |     | Following                           | Papadopoulou        |     | et  | al. (2022), |     | we ex- |
3.1 TaskDefinition
|     |     |     |     |     |     |     | pandedthePIItypeset |     |     | with7maintypesinto55 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------------------- | --- | --- | --- |
T
| Privacy | Protection |     | Systems | target | at maintaining |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fine-grainedsubcategoriesasdetailedinTable11,
LLMfunctionalitywhilemaximizinguserprivacy employingtwocomplementarystrategiesforentity
| protection.             |     | Letpbeapromptconsistingofauser |     |                     |     |     | generation:              |     |     |     |                     |     |     |
| ----------------------- | --- | ------------------------------ | --- | ------------------- | --- | --- | ------------------------ | --- | --- | --- | ------------------- | --- | --- |
| descriptiondandaqueryq. |     |                                |     | Thedescriptiondcon- |     |     |                          |     |     |     |                     |     |     |
|                         |     |                                |     |                     |     |     | (1)Rule-basedGeneration: |     |     |     | Applicablefordeter- |     |     |
tainsinformationaboutmultiplesubjectindividuals
ministicPIItypeswithfixedformatsorenumerable
= s ,...,s . Foreachsubjects ,thereexists value sets (e.g., phone numbers, email addresses,
| S   | { 1 | m } |     |     | i    |         |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | = ei | ,...,ei |     |     |     |     |     |     |     |
an associated set of PII entities i 1 . IDnumbers). (2)LLM-basedGeneration: Applica-
|     |     |     |     |     | E { | k}  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThecompletesetofPIIentitiesinpromptpisde-
blefornon-deterministicPIItypesrequiringcon-
m
fined as = , where each entity e textual understanding and real-world knowledge
|     | E   | i=1E | i   |     |     | ∈ E |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
belongs to a predefined PII type from set (see (e.g.,occupationdescriptions,detailedaddresses).
|          |       | S   |     |        |            | T   |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Appendix | A.2). | Let |     | denote | the subset | of  |     |     |     |     |     |     |     |
q
|     |     |     | E   | ⊆ E |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PIIentitiesthatarenecessaryforansweringquery 3.2.2 UserDescriptionGeneration
| q.  |     |     |     |     |     |     | Single-Subject |     | Description |     | Construction: |     | The |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ------------- | --- | --- |
Basedonthisdefinition,weproposethreefun- constructionofsingle-subjectdescriptionsfollows
damental evaluation tasks for Privacy Protection athree-stageprocess:
| Systems: |     |     |     |     |     |     | (1) Entity | Selection: |     | For | subject | s, randomly |     |
| -------- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- | ------- | ----------- | --- |
(1) PII Detection Task: Given prompt p, the sample n entities (4 n 16) from different
≤ ≤
model needs to: identify the minimal text spans PII types to construct entity set . The sampling
E
for all PII entities e ; establish associations processensuresdiversityofPIItypeswhileconsid-
∈ E
betweeneachentityeanditscorrespondingsubject eringtheirnaturaldistributioninreal-worldscenar-
s ; assign the correct PII type t to each ios. (2)ConsistencyOptimization: Ensurelogical
| ∈        | S   |     |     |     | ∈ T |     |               |       |     |          |            |     |      |
| -------- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | -------- | ---------- | --- | ---- |
| entitye. |     |     |     |     |     |     | compatibility | among |     | entities | in through |     | LLM- |
E
(2)Query-RelatedPIIDetectionTask: Given basedverificationwithcraftedprompts(detailedin
prompt p, the model needs to determine the min- AppendixC).Forexample,verifiesreasonablecor-
imal subset of PII entities q . This subset respondencebetweenageandeducationalhistory
|     |     |     |     | E   | ⊆ E |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
shouldonlycontainPIIentitiesnecessarytoanswer as shown in Figure 2. (3) User Desc Generation:
queryq,maximizingprotectionofnon-relevantper- Selects appropriate expression styles to generate
4993

Figure 2: PII-Bench synthesis process consists of three main modules: (a) PII Entity Generation, (b) User
DescriptionGeneration,and(c)QueryGeneration.
theuserdescription. Itemploysformaldescription containing work experience and educational
E q
formats like job resumes and employee records background, we design scenarios such as recruit-
inprofessionalscenarios;casualexpressionslike mentevaluationorcareerplanning. (3)EntityAb-
personal profiles and self-introductions in social straction: Transform specific entities in into
E q
| scenarios. |     |     |     |     |     | abstractrepresentationswhilepreservingsemantic |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
Multi-SubjectDescriptionConstruction: The properties. (4)QueryGeneration: Synthesizenatu-
construction process for multi-subject related de- ralqueriesq byintegratingabstractedentitiesinto
scriptionsincludesthesekeysteps: theircorrespondingscenarios.
| (1)EntitySelection: |                       | Constructrelationshipnet- |               |                 |      |                         |              |         |              |           |
| ------------------- | --------------------- | ------------------------- | ------------- | --------------- | ---- | ----------------------- | ------------ | ------- | ------------ | --------- |
|                     |                       |                           |               |                 |      | 3.2.4 HumanVerification |              |         |              |           |
| workR(s             | ,s )forsubjectpairs(s |                           |               | ,s ). Relation- |      |                         |              |         |              |           |
|                     | i j                   |                           |               | i j             |      |                         |              |         |              |           |
|                     |                       |                           |               |                 |      | All content             | generated    | by      | GPT-4-0806   | undergoes |
| ship types          | include               | intersection              | relationships |                 | like |                         |              |         |              |           |
|                     |                       |                           |               |                 |      | rigorous                | verification | by five | professional | annota-   |
| colleagues          | and                   | alumni, hierarchical      |               | relationships   |      |                         |              |         |              |           |
like parent-child and teacher-student, and non- torsandtheauthors,focusingon: (1)Completeness
intersectionrelationshipswithnodirectconnection. andaccuracyofPIIentityannotationsindescrip-
|                             |     |          |                    |          |        | tion d.                 | (2) Correspondence |     | between              | query q and |
| --------------------------- | --- | -------- | ------------------ | -------- | ------ | ----------------------- | ------------------ | --- | -------------------- | ----------- |
| (2)ConsistencyOptimization: |     |          | Applyrelationship- |          |        |                         |                    |     |                      |             |
|                             |     |          |                    |          |        | query-relevantentityset |                    |     | . (3)Overallsemantic |             |
| aware verification          |     | based on | R to               | maintain | cross- |                         |                    |     | E q                  |             |
subject coherence (detailed in Appendix C). The coherenceandscenarioauthenticity. Completean-
notationguidelinesandqualitycontrolprocedures
| optimization | enforces | shared | attributes | for | inter- |     |     |     |     |     |
| ------------ | -------- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- |
aredetailedinAppendixG.
| section | relationships | (e.g., | company | address | for |     |     |     |     |     |
| ------- | ------------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- |
colleagues),structuralconstraintsforhierarchical
|     |     |     |     |     |     | 3.3 DatasetPartitioningandStatistics |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
relationships(e.g.,agedifferencesforparent-child
Table3presentsthepartitionandkeystatisticsof
pairs),andremovessampleswithirresolvablecon-
PII-Bench,whichcomprisestwomaindatasets(PII-
| tradictions. | (3)UserDescGeneration: |     |     | Thisstage |     |     |     |     |     |     |
| ------------ | ---------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
designsnaturalinteractionenvironmentsmatching singleandPII-multi)andtwospecializedtestsets
|     |     |     |     |     |     | (PII-hard | and PII-distract). |     | Each sample | follows |
| --- | --- | --- | --- | --- | --- | --------- | ------------------ | --- | ----------- | ------- |
relationshipcharacteristics,placingsubjectsinreal-
|     |     |     |     |     |     | a consistent | JSON | structure | containing | four key |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | ---------- | -------- |
isticscenarios(likemeetings,familyactivities)and
constructingmulti-partydialogueflowstoreflect components: userdescription,query,comprehen-
interactiverelationships. sivePIIentityannotations,andquery-relevantPII
labels,asillustratedinFigure3.
3.2.3 QueryConstruction PII-SingleandPII-Multi: Basedonthenum-
For each description d, we construct queries ber of subjects in descriptions, the dataset is di-
throughfourphases: vided into two main subsets. PII-Single contains
(1)EntitySelection: Randomlysamplekentities 1,214description-querypairsinvolvingsinglesub-
(1 k 3)from toformquery-relevantentity jects,focusingonmodelperformanceinhandling
| ≤ ≤ |     | E   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
set q . (2) Scenario Design: Generate domain- individual information. PII-Multi contains 1,228
E
specificcontextsalignedwithreal-worldapplica- description-querypairsinvolvingmultiplerelated
tions(detailedinAppendixD).Forinstance,given subjects,evaluatingmodelcapabilityinhandling
4994

|     | Dataset    |     | PII-F1   | Query-F1 |     |     |              |             | Avg#Char   | Avg#PII | Avg#Char | Avg#PII |
| --- | ---------- | --- | -------- | -------- | --- | --- | ------------ | ----------- | ---------- | ------- | -------- | ------- |
|     |            |     |          |          |     |     | Name #Sample | Avg#Subject | (Desc)     | (Desc)  | (Query)  | (Query) |
|     | PII-single |     | 97.2 1.1 | 95.1     | 1.3 |     |              |             |            |         |          |         |
|     |            |     | ±        |          | ±   |     | PII-single   | 1,214       | 1.0 893.48 | 7.67    | 211.21   | 1.95    |
PII-multi 95.4 1.2 94.3 1.5 PII-multi 1,228 2.0 652.65 13.14 236.21 2.06
|     |     |     | ±   |     | ±   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PII-hard 91.3 1.1 90.3 1.2 PII-hard 200 1.5 778.03 10.60 222.09 2.10
|     |              |     | ±        |      | ±   |     | PII-distract | 200   | 7.5 4,403.64  | 51.08 | 859.69 | 5.82 |
| --- | ------------ | --- | -------- | ---- | --- | --- | ------------ | ----- | ------------- | ----- | ------ | ---- |
|     | PII-distract |     | 92.8 1.8 | 91.5 | 2.1 |     |              |       |               |       |        |      |
|     |              |     |          |      |     |     | All          | 2,842 | 1.92 1,028.32 | 13.30 | 268.41 | 2.28 |
|     |              |     | ±        |      | ±   |     |              |       |               |       |        |      |
Table3: StatisticsofPII-Bench.
| Table                                            | 2: Human | performance |     | in PII-Bench. |     | PII-F1 |               |     |     |     |     |     |
| ------------------------------------------------ | -------- | ----------- | --- | ------------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
| measuresaccuracyinthePIIdetectiontaskwhileQuery- |          |             |     |               |     |        | 4 Experiments |     |     |     |     |     |
F1evaluatesthequery-relevantPIIdetectiontask.
|     |     |     |     |     |     |     | 4.1 OverallSetup |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
privacyinformationwithincomplexinterpersonal Traditional Model Baselines: We implemented
BiLSTM-CRFasatraditionalsequencelabeling
networks.
|                        |     |     |     |                    |     |     | baseline, | following   | the architecture |     | proposed  | by    |
| ---------------------- | --- | --- | --- | ------------------ | --- | --- | --------- | ----------- | ---------------- | --- | --------- | ----- |
| Test-HardConstruction: |     |     |     | Select200challeng- |     |     |           |             |                  |     |           |       |
|                        |     |     |     |                    |     |     | Huang et  | al. (2015). | We trained       |     | the model | using |
inginstancesfromPII-SingleandPII-Multitocon-
|                         |     |     |                        |     |     |     | Adam optimizer |       | with a learning |     | rate of       | 1e-3 and |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | -------------- | ----- | --------------- | --- | ------------- | -------- |
| structTest-Harddataset, |     |     | basedoncriteriainclud- |     |     |     |                |       |                 |     |               |          |
|                         |     |     |                        |     |     |     | batch size     | of 32 | for 50 epochs   | on  | the PII-Bench |          |
ing: (1)Maximumcharacterlengthofdescription
trainingset.
| text | d. (2) | Highest | PII entity | density | (   | / d ). |               |     |                          |     |     |     |
| ---- | ------ | ------- | ---------- | ------- | --- | ------ | ------------- | --- | ------------------------ | --- | --- | --- |
|      |        |         |            |         | |E| | | |    | LLMBaselines: |     | Theevaluationencompassed |     |     |     |
(3)Sampleswiththemostquery-relevantentities
|     |     |     |     |     |     |     | both API-based |     | and open-source |     | large | language |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | ----- | -------- |
( ).
| q   |     |     |     |     |     |     | models. | API-based | models | included |     | GPT-4o- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | -------- | --- | ------- |
|E |
Test-Distract Construction: Construct 200 2024-0806 (GPT4o) (OpenAI, 2024), Claude-
samplessimulatingcomplexmulti-userinteraction 3.5-Sonnet (Claude3.5) (Anthropic, 2024), and
scenarios. Each sample integrates five different DeepSeek-ChatDeepseekV3(Liuetal.,2024),ac-
descriptions from PII-Single and PII-Multi, and cessed through their respective official APIs be-
constructsqueriesinvolvingthreeofthesedescrip- tween January 1 and February 10, 2025. Open-
tionsbasedonprofessionalnetworks,knowledge source alternatives comprised Llama-3.1-70B-
platforms,andcommunityforuminteractiontem- Instruct (Llama3.1) (Dubey et al., 2024), and
plates. Thegenerationprocessemploysdialogue Qwen-2.5-72B-Instruct (Qwen2.5) (Yang et al.,
| flow | transformation |     | strategies | to  | ensure | natural | 2024a). |     |     |     |     |     |
| ---- | -------------- | --- | ---------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- |
transitionsandsemanticcoherence,simulatingreal-
|     |     |     |     |     |     |     | SLM | Baselines: | To  | investigate | scaling | ef- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ------- | --- |
worldinformationinterferenceandcomplexinter- fects,weincludedtwosmall-scalelanguagemod-
| actionpatterns. |     |     |     |     |     |     | els: Llama-3.1-8B-Instruct(Llama3.1-SLM)and |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
Qwen-2.5-7B-Instruct(Qwen2.5-SLM).Allexper-
imentsutilizeddefaultparameterswithtemperature
3.4 HumanPerformance setto0toensurereproducibility. Additionally,we
conductedacomprehensiveevaluationonsmaller,
deployment-readymodels(0.5B-3Bparameters)to
| To establish |     | a human | baseline, | we  | recruited | 25  |     |     |     |     |     |     |
| ------------ | --- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
graduatestudentswithatleasttwoyearsofresearch assesstheirviabilityforon-devicePIIprotection,
experienceinprivacyprotectionanddatasecurity withdetailedresultspresentedinAppendixF.3.
fromtopChineseuniversities. Allparticipantscom- Prompt Baselines: The assessment incorpo-
pletedcomprehensivetrainingandpassedaqual- rated multiple prompting strategies for query-
ification test before formal evaluation (details in relatedPIIdetection. Naiveinputstheuserdescrip-
AppendixE).Weevaluated400randomlysampled tion and query. Naive /w Choice includes a list
instances(200eachfromPII-singleandPII-multi) ofcandidatePIIentitiestoconstraintheselection
and100instancesfromPII-distract,witheachin- space;wereportitasanoracleupperboundthatiso-
stanceindependentlyassessedbyfiveparticipants. latesrelevancereasoningfromdetection,notasa
Participantsperformedtwosequentialtasks: PIIde- deployablestrategy. Self-CoT(Weietal.,2022)in-
tection,whichinvolveddeterminingminimaltext corporatingstep-by-stepreasoningprompts.
Auto-
spans, associated subjects, and PII types for all CoT(Zhangetal.,2022),whichautomatesthegen-
entitiesintheuserdescription,followedbyquery- erationofchain-of-thoughtdemonstrationsthrough
relevantPIIdetectiontoidentifyentitiesessential three-shotsetting. Self-Consistency(SC)(Wang
for addressing the given query. The result of the etal.,2022),whichsynthesizesmultiplereasoning
humanbaselineisshowninTable2. paths to derive the final output. Plan-and-Solve
4995

Figure3: AnexamplefromPII-Bench,whichaimstoevaluatePrivacyProtectionSystem’sabilitybymasking
maximizePIIwhilemaintainingLLM’sfunctionality. Theevaluationisseparatedbytwofundamentaltasks: (a)
ThePIIDetectionTask: IdentifyandclassifyPIIentitiesforeachsubjectintheprompt,withgroundtruthlabels
shownontherightside. (b)TheQuery-RelatedPIIDetectionTask: DeterminewhichPIIentitiesarenecessaryfor
answeringtheuserquery,enablingselectivemaskingofirrelevantpersonalinformation.
(PS-CoT) (Wang et al., 2023) develops a els achieve higher F1 scores in this combined
CoT
strategicplanbeforeexecutingthesolutionprocess. taskcomparedtoindividualquery-relevancetasks.
AppendixF.6providesdetailsofeachprompts. GPT4o reaches 0.77 F1 with Self-Consistency
Metrics: ThePIIdetectiontaskevaluatesmodel prompting, suggesting complementary signals
|             |         |          |             |         | from the joint | objective. | Open-source | models |
| ----------- | ------- | -------- | ----------- | ------- | -------------- | ---------- | ----------- | ------ |
| performance | through | two sets | of metrics: | Strict- |                |            |             |        |
F1measurestheaccuracyofsubjectidentification, demonstrate comparable capabilities, with both
entity span detection, and PII type classification Llama3.1 and Qwen2.5 achieving 0.76 F1 using
Auto-CoT.
| simultaneously. | Ent-F1focusesonentityspande- |     |     |     |     |     |     |     |
| --------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
tectionindependentofsubjectattributionandtype
classification. Forquery-relateddetection,model 4.3 PerformanceonPIIDetection
| performance | is measured | through | Precision, | Re- |     |     |     |     |
| ----------- | ----------- | ------- | ---------- | --- | --- | --- | --- | --- |
ResultsonthePIIdetectiontask(Table6)reveal:
| call, and | F1. Considering | the | inherent | variation |                |        |             |       |
| --------- | --------------- | --- | -------- | --------- | -------------- | ------ | ----------- | ----- |
|           |                 |     |          |           | Large Language | Models | demonstrate | supe- |
inentityexpressionsandpotentialpartialmatches,
|     |     |     |     |     | rior detection | capabilities. | API-based | LLMs |
| --- | --- | --- | --- | --- | -------------- | ------------- | --------- | ---- |
RougeL-Fisemployedforbothtaskstocomple-
achievestrongperformance,withDeepSeekV3and
| ment the | exact matching | metrics. | Detailed | com- |     |     |     |     |
| -------- | -------------- | -------- | -------- | ---- | --- | --- | --- | --- |
GPT4oleadinginStrict-F1scores(0.903and0.891
putationproceduresareprovidedinAppendixF.1.
|     |     |     |     |     | onPII-SingleandPII-Multi,respectively). |     |     | Open- |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | ----- |
Allreportedmodelperformancemetricsaremean
sourceLlama3.1showscompetitiveperformance,
scoresovertestsets(temperature=0,top_k=1).
|     |     |     |     |     | particularlyinentityrecognition(Ent-F1: |     |     | 0.942on |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | ------- |
PII-Multi).
4.2 PerformanceonQuery-UnrelatedPII
|     |     |     |     |     | Entity type | classification | remains | challeng- |
| --- | --- | --- | --- | --- | ----------- | -------------- | ------- | --------- |
Masking
AconsistentgapbetweenStrict-F1andEnt-F1
ing.
We evaluate models’ performance on the query- scoresindicatesthataccuratePIItypeclassification
unrelated PII masking task, which requires both posesgreaterchallengesthanentityboundaryde-
| accurate | PII detection | and relevance | assessment. |     |     |     |     |     |
| -------- | ------------- | ------------- | ----------- | --- | --- | --- | --- | --- |
tection. Thisdisparitybecomesmorepronounced
Table4presentsourresults: inthePII-Distractdataset,suggestingincreaseddif-
Jointtaskyieldsimprovedperformance. Mod- ficultyinprecisePIIcategorizationundercomplex
4996

|     |     |     | GPT4o | Llama3.1 |     | Qwen2.5 | Llama3.1-SLM |     | Qwen2.5-SLM |     |
| --- | --- | --- | ----- | -------- | --- | ------- | ------------ | --- | ----------- | --- |
Method
|     |     |     | F1 RougeL-F | F1 RougeL-F |     | F1 RougeL-F | F1  | RougeL-F | F1  | RougeL-F |
| --- | --- | --- | ----------- | ----------- | --- | ----------- | --- | -------- | --- | -------- |
BasicMethod
| Naive |     |     | 0.72 0.72 | 0.72 0.73 |     | 0.70 0.70 | 0.42 |     | 0.43 0.54 | 0.58 |
| ----- | --- | --- | --------- | --------- | --- | --------- | ---- | --- | --------- | ---- |
AdvancedMethod
| Self-CoT |     |     | 0.76 0.77 | 0.75 0.75 |     | 0.73 0.73 | 0.53 |     | 0.54 0.54 | 0.58 |
| -------- | --- | --- | --------- | --------- | --- | --------- | ---- | --- | --------- | ---- |
Auto-CoT(3-shot) 0.75 0.75 0.76 0.77 0.76 0.76 0.57 0.58 0.54 0.58
Self-Consistency 0.77 0.77 0.71 0.72 0.71 0.72 0.49 0.50 0.49 0.53
| PS-CoT |     |     | 0.74 0.74 | 0.72 0.73 |     | 0.73 0.73 | 0.48 |     | 0.50 0.56 | 0.60 |
| ------ | --- | --- | --------- | --------- | --- | --------- | ---- | --- | --------- | ---- |
w/ExtraInformation
Naivew/Choice 0.82 0.82 0.77 0.78 0.79 0.79 0.46 0.48 0.67 0.71
Table4: PerformancecomparisonontheQuery-UnrelatedPIIMaskingtask(PII-singleandPII-multidatasets). The
bestperformanceforeachmodel(excludingNaivew/Choice)isinbold.
Subject Count PII Count Description Length Query-Related PII Count
| 1.0          |     |     | 1.0          |     | 1.0          |     |     | 1.0          |     |     |
| ------------ | --- | --- | ------------ | --- | ------------ | --- | --- | ------------ | --- | --- |
| 0.8          |     |     | 0.8          |     | 0.8          |     |     | 0.8          |     |     |
| 1F tcaxE 0.6 |     |     | 1F tcaxE 0.6 |     | 1F tcaxE 0.6 |     |     | 1F tcaxE 0.6 |     |     |
| 0.4          |     |     | 0.4          |     | 0.4          |     |     | 0.4          |     |     |
| 0.2          |     |     | 0.2          |     | 0.2          |     |     | 0.2          |     |     |
| 0.0          |     |     | 0.0          |     | 0.0          |     |     | 0.0          |     |     |
1 2 5 6 7 8 9 10 8 16 33 42 50 58 67 605 1207 3014 3616 4218 4820 5422 1 2 3 4 5 5 6 7
|     | # of Subject |     |     | # of PII |     | # of Char |     |     | # of Query-Related PII |     |
| --- | ------------ | --- | --- | -------- | --- | --------- | --- | --- | ---------------------- | --- |
Figure4: TheperformanceofGPT-4oiscorrelatedwiththenumberofsubject,thenumberofPII,decriptionlength,
andthenumberofquery-relatedPII.
Test-Hard Test-Distract of-thought approaches generally improve perfor-
Method
|     |     | F1  | RougeL-F | F1 RougeL-F |     |     |     |     |     |     |
| --- | --- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
mance,withSelf-ConsistencyandAuto-CoTprov-
| BasicMethod |     |      |      |           |     | ingmosteffective(0.716F1forGPT4owithSelf- |       |     |             |            |
| ----------- | --- | ---- | ---- | --------- | --- | ----------------------------------------- | ----- | --- | ----------- | ---------- |
| Naive       |     | 0.36 | 0.36 | 0.57 0.57 |     |                                           |       |     |             |            |
|             |     |      |      |           |     | Consistency;                              | 0.710 | F1  | for Qwen2.5 | with Auto- |
AdvancedMethod
Self-CoT 0.45 0.45 0.66 0.67 CoT). However, these benefits are highly depen-
dentonmodelscale—smallermodelsoftenshow
| Auto-CoT(3-shot) |     | 0.45 | 0.40 | 0.62 0.63 |     |     |     |     |     |     |
| ---------------- | --- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- |
Self-Consistency 0.46 0.46 0.62 0.63 degraded performance with complex prompting
| PS-CoT |     | 0.38 | 0.38 | 0.67 0.67 |     |     |     |     |     |     |
| ------ | --- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- |
strategies.
w/ExtraInformation
|               |     |      |      |           |     | EffectivenessofEntityCandidates. |              |        |            | Providing |
| ------------- | --- | ---- | ---- | --------- | --- | -------------------------------- | ------------ | ------ | ---------- | --------- |
| Naivew/Choice |     | 0.53 | 0.53 | 0.66 0.66 |     |                                  |              |        |            |           |
|               |     |      |      |           |     | candidate                        | PII entities | (Naive | w/ Choice) | substan-  |
Table5: Performancecomparisononchallengingtest tiallyimprovesperformanceacrossallmodels(e.g.,
| setsusingGPT4o. |     |     |     |     |     | GPT4o improves |     | from 0.627 | to 0.842 | F1). How- |
| --------------- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | -------- | --------- |
ever,practicalapplicabilityislimitedascandidate
| scenarios. |     |     |     |     |     | entitiesarerarelyavailableinreal-worldscenarios. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
4.4 PerformanceonQuery-RelatedPII 4.5 Privacy-UtilityTradeoffAnalysis
| Detection |     |     |     |     |     | Weevaluatedthetradeoffbetweenprivacyprotec- |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
Table 7 presents the results on PII-single dataset tionandqueryutilityacrossdifferentPIImasking
| acrossdifferentmodelscalesandpromptingstrate- |     |     |     |     |     | strategies         |     |     |                     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------------------- | --- |
| gies.                                         |     |     |     |     |     | ExperimentalSetup. |     |     | Weselected200unique |     |
LimitedPerformanceofCurrentLLMs. Ad- userdescriptionsfromPII-Benchandappliedthree
vanced LLMs exhibit limited performance, with masking methods: (1) No Mask: Original text
GPT4oachievingonly0.627F1scorewithNaive with all PII preserved; (2) Mask: All de-
|     |     |     |     |     |     |     |     |     | All PII |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
prompting—substantially below human perfor- tectedPIIentitiesreplacedwiththeircorresponding
mance(0.951F1). Open-sourcealternativesshow tags;(3)Query-unrelatedPIIMask: Onlyquery-
competitiveperformance,withQwen2.5reaching irrelevant PII entities masked. For each method,
| 0.615F1. |     |     |     |     |     | wegeneratedresponsesusingGPT4o. |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
Impact of Advanced Prompting. Chain- Metrics. The privacy-utility tradeoff is eval-
4997

|     |     | PII-Single |     |     | PII-Multi |     |     | PII-Hard |     |     | PII-Distract |     |
| --- | --- | ---------- | --- | --- | --------- | --- | --- | -------- | --- | --- | ------------ | --- |
BaselineModels
Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F
TraditionalModel
| BiLSTM-CRF |     | - 0.851 |     | -   | - 0.828 | -   | -   | 0.684 | -   | -   | 0.787 | -   |
| ---------- | --- | ------- | --- | --- | ------- | --- | --- | ----- | --- | --- | ----- | --- |
API-basedLargeLanguageModel
GPT4o 0.893 0.914 0.895 0.891 0.923 0.893 0.817 0.869 0.819 0.715 0.868 0.716
Claude3.5 0.858 0.891 0.862 0.890 0.920 0.892 0.813 0.857 0.818 0.910 0.948 0.911
DeepSeekV3 0.903 0.921 0.905 0.884 0.927 0.886 0.838 0.893 0.838 0.658 0.945 0.658
Open-sourceLargeLanguageModel
Llama3.1 0.881 0.913 0.883 0.883 0.942 0.884 0.840 0.893 0.841 0.834 0.946 0.835
Qwen2.5 0.866 0.908 0.869 0.853 0.918 0.855 0.804 0.876 0.806 0.647 0.941 0.649
Open-sourceSmallLanguageModel
Llama3.1-SLM 0.748 0.800 0.752 0.778 0.869 0.781 0.718 0.798 0.722 0.551 0.876 0.552
Qwen2.5-SLM 0.787 0.846 0.792 0.451 0.806 0.453 0.591 0.810 0.594 0.454 0.815 0.456
Table6: PerformanceofbaselinemodelsunderthePIIDetectiontask. Resultsinboldindicatethebestperformance
foreachdatasetandmetriccategory.
|     |     |     | GPT4o |     | Llama3.1 | Qwen2.5 |     | Llama3.1-SLM |     |     | Qwen2.5-SLM |     |
| --- | --- | --- | ----- | --- | -------- | ------- | --- | ------------ | --- | --- | ----------- | --- |
Method
|     |     | F1  | RougeL-F | F1  | RougeL-F | F1  | RougeL-F | F1  | RougeL-F |     | F1  | RougeL-F |
| --- | --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | --- | -------- |
BasicMethod
| Naive |     | 0.63 | 0.63 | 0.63 | 0.63 | 0.62 | 0.62 | 0.33 |     | 0.33 | 0.41 | 0.41 |
| ----- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | ---- | ---- | ---- |
AdvancedMethod
| Self-CoT |     | 0.71 | 0.72 | 0.69 | 0.69 | 0.67 | 0.68 | 0.39 |     | 0.39 | 0.40 | 0.41 |
| -------- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | ---- | ---- | ---- |
Auto-CoT(3-shot) 0.66 0.66 0.70 0.72 0.71 0.72 0.43 0.44 0.37 0.38
Self-Consistency 0.72 0.72 0.63 0.64 0.65 0.65 0.31 0.32 0.32 0.33
| PS-CoT |     | 0.65 | 0.65 | 0.65 | 0.66 | 0.67 | 0.67 | 0.35 |     | 0.36 | 0.45 | 0.46 |
| ------ | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | ---- | ---- | ---- |
w/ExtraInformation
Naivew/Choice 0.84 0.84 0.76 0.76 0.83 0.83 0.52 0.52 0.77 0.77
Table7: PerformancecomparisonontheQuery-RelatedPIIDetectiontask(PII-singledataset).
| Method |     |     | P   | U   | B   | PII-Real | demonstrates |     | consistent |     | alignment | with |
| ------ | --- | --- | --- | --- | --- | -------- | ------------ | --- | ---------- | --- | --------- | ---- |
NoMask 0.00 1.00 0.50 synthetic data. Comprehensive experimental re-
| AllPIIMask             |     |     | 1.00 | 0.52 | 0.76 |       |                |     |          |     |          |        |
| ---------------------- | --- | --- | ---- | ---- | ---- | ----- | -------------- | --- | -------- | --- | -------- | ------ |
|                        |     |     |      |      |      | sults | and validation |     | analysis | are | provided | in Ap- |
| Query-unrelatedPIIMask |     |     | 0.83 | 0.89 | 0.86 |       |                |     |          |     |          |        |
pendixF.4.
| Table 8: Privacy-utility |     | tradeoff | across |     | different PII |     |     |     |     |     |     |     |
| ------------------------ | --- | -------- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
maskingstrategies. Balancedscores(B)combineboth 4.7 In-depthPerformanceAnalysis
metricswithequalweights.
|     |     |     |     |     |     | Factors | Influencing |     | Performance. |     |     | Figure 4 re- |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ------------ | --- | --- | ------------ |
vealsseveralcriticalfactorsaffectingmodelaccu-
racy: performancedegradessharplybeyond5sub-
| uated through | two | metrics: | Privacy |     | Score (P): |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
jects(F1dropsfrom0.85to0.52),33PIIentities,
QuantifiestheproportionofPIIsuccessfullypro-
|           |               |            |               |     |            | or 3000 | characters |       | in text | length. | Query-Related |         |
| --------- | ------------- | ---------- | ------------- | --- | ---------- | ------- | ---------- | ----- | ------- | ------- | ------------- | ------- |
| tected in | the processed |            | text. Utility |     | Score (U): |         |            |       |         |         |               |         |
|           |               |            |               |     |            | entity  | count      | shows | modest  | impact, | with          | gradual |
| Combines  | semantic      | similarity | and           | LLM | evalua-    |         |            |       |         |         |               |         |
declinefrom1to7entities.
tionforqualityassessmentbetweenmaskandun-
|                   |     |          |             |     |        | Performance |     | on  | Challenging |     | Scenarios. | Re- |
| ----------------- | --- | -------- | ----------- | --- | ------ | ----------- | --- | --- | ----------- | --- | ---------- | --- |
| masked responses. |     | Detailed | computation |     | proce- |             |     |     |             |     |            |     |
sultsonspecializedtestsets(Table5)revealsignifi-
duresareprovidedinAppendixF.2.
cantperformancedegradationincomplexscenarios.
| Results. | Table | 8 shows | that | Query-unrelated |     |     |     |     |     |     |     |     |
| -------- | ----- | ------- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
OnTest-Hard,featuringhighPIIdensityandlong
| PII Mask         | achieves | optimal                       | balance | between | pri- |                              |      |                     |     |     |                  |     |
| ---------------- | -------- | ----------------------------- | ------- | ------- | ---- | ---------------------------- | ---- | ------------------- | --- | --- | ---------------- | --- |
|                  |          |                               |         |         |      | texts,                       | even | the best-performing |     |     | Self-Consistency |     |
| vacyprotection(P |          | = 0.83)andutilitypreservation |         |         |      |                              |      |                     |     |     |                  |     |
|                  |          |                               |         |         |      | approachachievesonly0.463F1. |      |                     |     |     | Test-Distract’s  |     |
(U = 0.89),outperformingotherstrategiesinbal-
multi-subjectscenariosposesimilarchallenges.
| ancedscore(B |     | = 0.86). |     |     |     |            |          |     |           |                |         |        |
| ------------ | --- | -------- | --- | --- | --- | ---------- | -------- | --- | --------- | -------------- | ------- | ------ |
|              |     |          |     |     |     | Evaluation |          | on  | Reasoning |                | Models. | We ad- |
|              |     |          |     |     |     | ditionally | evaluate |     | GPT-5,    | DeepSeek-V3.2, |         | and    |
4.6 Real-WorldDatasetValidation
DeepSeek-R1onallthreetasks(Table9),withan
To validate the reliability of synthetic data, we extendedcomparisonoverfourQwen3variantsre-
constructedPII-Real,adatasetcomprising100in- ported in Appendix H. On PII Detection, scores
stancesderivedfrompubliclyavailableprofilesof saturateonPII-Single,whilethelargestgainsfrom
20AIresearcherswithmanuallyannotatedPIIen- reasoningappearonthehigh-entropyPII-Distract
tities and human-written queries. Evaluation on subset;open-sourcemodelsmatchproprietarysys-
4998

Model Detect. Q-Rel. Q-Unrel. aboutsensitiveinformation. Thisgapinassessment
GPT-5 0.871 0.733 0.840 methodologylimitsourunderstandingofmodels’
DeepSeek-V3.2 0.856 0.765 0.852 reasoningcapabilitiesinreal-worldprivacyprotec-
|     | DeepSeek-R1 |     | 0.876 | 0.745 | 0.850 |     |     |     |     |     |     |
| --- | ----------- | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- |
tionscenarios.
PII-Benchdoesnotevaluaterobustnesstoinfer-
| Table9: |     | RecentLLMsonPII-Single. |     |     | Detect.: | Strict-F1 |     |     |     |     |     |
| ------- | --- | ----------------------- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- |
enceattacks,whereanadversaryrecoversamasked
| onPIIDetectionusingtheNaive(zero-shot)prompt. |     |     |     |     |     | Q-  |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
entitybycombiningthestill-visiblecontext(forex-
| Rel. | andQ-Unrel.: |     | bestF1acrosspromptingstrategies, |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
excludingtheNaivew/Choiceoracle. Fullresultsin ample, inferring an employer from an unmasked
AppendixH.
|     |     |     |     |     |     |     | jobtitletogetherwithanearbylocationcue). |              |        |      | Such        |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | ------------ | ------ | ---- | ----------- |
|     |     |     |     |     |     |     | attacks target                           | the residual | signal | left | after mask- |
ingandarethereforecomplementarytothequery-
tems,withDeepSeek-R1onparwithGPT-5across
|                          |     |     |     |                   |     |     | awaremaskingproblemwestudy. |     |     | ExtendingPII- |     |
| ------------------------ | --- | --- | --- | ----------------- | --- | --- | --------------------------- | --- | --- | ------------- | --- |
| everyPIIDetectionsubset. |     |     |     | Thetwoquery-aware |     |     |                             |     |     |               |     |
Benchwithadversarialinferenceprobesisanatural
| tasksremainconsiderablyharder: |     |     |     |     | thestrongestsys- |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
directionforfollow-upwork.
temtrailsthehumanbaselineonQuery-RelatedPII
Detectionbyroughly18F1points,indicatingthat
EthicalConcerns
relevancejudgementratherthanentitydetectionis
thedominantbottleneck.
Throughoutthedevelopmentandimplementation
ofPII-Bench,ethicalconsiderationshaveremained
5 Conclusion
|     |     |     |     |     |     |     | our paramount | priority. | To ensure | the | evaluation |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --------- | --- | ---------- |
ThispaperintroducesPII-Bench,acomprehensive datasetitselfdoesnotcompromiseprivacy,wehave
evaluationframeworkcomprising2,842testsam- implemented rigorous data synthesis and review
plesacross7PIItypeswith55fine-grainedsubcate- protocols,withallsampledataundergoingmultiple
gories,andproposesaquery-unrelatedPIImasking roundsofscrutinybyprofessionalsecurityteams
strategy to balance privacy protection with LLM toguaranteetheabsenceofrealpersonalinforma-
utility. Ourempiricalevaluationrevealsthatwhile tion. Duringthedatagenerationprocess,wehave
advancedLLMsdemonstratestrongperformance carefullyengineeredouralgorithmstoensureequi-
inbasicPIIdetection,theyexhibitsubstantiallimi- tablerepresentationacrossdifferentdemographic
tationsinquery-relevanceassessment. Small-scale groups,establishingcomprehensivehumanreview
modelsshowconsiderablylargerperformancegaps mechanismstoverifythatgenerateddataremains
across all evaluation tasks. These findings estab- freefrombiasanddiscriminatorycontent.
lishfoundationalbenchmarksandexposecritical
| challengesinprivacy-awarePIIhandling. |     |     |     |     |     |     | Acknowledgments                          |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
| Limitations                           |     |     |     |     |     |     | ThisworkwassupportedbytheNationalNatural |     |     |     |     |
ScienceFoundationofChina(No.72595845).
DespitePII-Bench’scontributionstoprivacypro-
| tection       |     | evaluation, | several                      | limitations |     | merit ac- |     |     |     |     |     |
| ------------- | --- | ----------- | ---------------------------- | ----------- | --- | --------- | --- | --- | --- | --- | --- |
| knowledgment. |     |             | Whilethecurrentdatasetencom- |             |     |           |     |     |     |     |     |
References
| passes | common |     | privacy | scenarios, | it requires | ex- |     |     |     |     |     |
| ------ | ------ | --- | ------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
pansionintospecializeddomainssuchasmedical JoshAchiam,StevenAdler,SandhiniAgarwal,Lama
|                                  |     |     |     |     |              |     | Ahmad, | Ilge Akkaya, | Florencia | Leoni | Aleman, |
| -------------------------------- | --- | --- | --- | --- | ------------ | --- | ------ | ------------ | --------- | ----- | ------- |
| recordsandfinancialtransactions. |     |     |     |     | Ourautomated |     |        |              |           |       |         |
DiogoAlmeida,JankoAltenschmidt,SamAltman,
synthesismethodologymitigatesthislimitationby ShyamalAnadkat,etal.2023. Gpt-4technicalreport.
enablingflexibledatasetexpansionacrossdomains, arXivpreprintarXiv:2303.08774.
languages,andculturalcontexts,supportingcontin-
|     |     |     |     |     |     |     | Anthropic. | 2024. Claude | 3.5 sonnet. |     | https://www. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ----------- | --- | ------------ |
uousrefinementofPIIcategoriestomeetevolving
anthropic.com/news/claude-3-5-sonnet.
| application |           | requirements. |          | The          | evaluation | frame-     |                       |     |                    |     |           |
| ----------- | --------- | ------------- | -------- | ------------ | ---------- | ---------- | --------------------- | --- | ------------------ | --- | --------- |
| work        | primarily |               | assesses | the accuracy |            | of PII en- |                       |     |                    |     |           |
|             |           |               |          |              |            |            | Dimitris Asimopoulos, |     | Ilias Siniosoglou, |     | Vasileios |
tity detection and query relevance determination, Argyriou, Thomai Karamitsou, Eleftherios Foun-
toukidis,SotiriosKGoudos,IoannisDMoscholios,
butlackssystematicevaluationofmodels’reason-
KonstantinosEPsannis,andPanagiotisSarigiannidis.
| ing | processes. | Specifically, |     | it does | not | fully cap- |     |     |     |     |     |
| --- | ---------- | ------------- | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
2024. Benchmarkingadvancedtextanonymisation
turehowmodelsinterpretqueries,deriveinforma-
|     |     |     |     |     |     |     | methods: | A comparative | study | on novel | and tradi- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ----- | -------- | ---------- |
tionrequirements,andmakerelevancejudgments tionalapproaches. arXivpreprintarXiv:2404.14465.
4999

David Biesner, Rajkumar Ramamurthy, Robin Sten- Qinbin Li, Junyuan Hong, Chulin Xie, Jeffrey Tan,
zel, Max Lübbering, Lars Hillebrand, Anna Ladi, Rachel Xin, Junyi Hou, Xavier Yin, Zhun Wang,
MarenPielka,RüdigerLoitz,ChristianBauckhage, DanHendrycks,ZhangyangWang,etal.2024. Llm-
and Rafet Sifa. 2022. Anonymization of german pbe:Assessingdataprivacyinlargelanguagemodels.
financialdocumentsusingneuralnetwork-basedlan- arXivpreprintarXiv:2408.12787.
guagemodelswithcontextualwordrepresentations.
|     |     |     |     |     |     | Aixin Liu, | Bei | Feng, | Bing | Xue, Bingxuan |     | Wang, |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ---- | ------------- | --- | ----- |
InternationalJournalofDataScienceandAnalytics,
| pages1–11. |     |     |     |     |     | BochaoWu,ChengdaLu,ChenggangZhao,Chengqi |        |        |       |       |        |       |
| ---------- | --- | --- | --- | --- | --- | ---------------------------------------- | ------ | ------ | ----- | ----- | ------ | ----- |
|            |     |     |     |     |     | Deng,                                    | Chenyu | Zhang, | Chong | Ruan, | et al. | 2024. |
Sébastien Bubeck, Varun Chandrasekaran, Ronen El- Deepseek-v3 technical report. arXiv preprint
arXiv:2412.19437.
| dan, Johannes |     | Gehrke,  | Eric    | Horvitz, | Ece Kamar,  |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| Peter Lee,    | Yin | Tat Lee, | Yuanzhi | Li,      | Scott Lund- |     |     |     |     |     |     |     |
YangLiu,YuanshunYao,Jean-FrancoisTon,Xiaoying
| berg,etal.2023. |     | Sparksofartificialgeneralintelli- |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhang,RuochengGuoHaoCheng,YegorKlochkov,
| gence: Earlyexperimentswithgpt-4. |     |     |     | arXivpreprint |     |                                     |     |     |     |     |     |        |
| --------------------------------- | --- | --- | --- | ------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------ |
|                                   |     |     |     |               |     | MuhammadFaaizTaufiq,andHangLi.2023. |     |     |     |     |     | Trust- |
arXiv:2303.12712.
|           |         |     |       |         |            | worthyllms: |          | Asurveyandguidelineforevaluating |            |     |       |          |
| --------- | ------- | --- | ----- | ------- | ---------- | ----------- | -------- | -------------------------------- | ---------- | --- | ----- | -------- |
|           |         |     |       |         |            | large       | language | models’                          | alignment. |     | arXiv | preprint |
| Tao Chen, | Ruifeng | Xu, | Yulan | He, and | Xuan Wang. |             |          |                                  |            |     |       |          |
arXiv:2308.05374.
| 2017. Improving                          |     | sentiment |     | analysis | via sentence |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| typeclassificationusingbilstm-crfandcnn. |     |           |     |          | Expert       |     |     |     |     |     |     |     |
NilsLukas,AhmedSalem,RobertSim,ShrutiTople,
SystemswithApplications,72:221–230.
|     |     |     |     |     |     | Lukas | Wutschitz, | and | Santiago | Zanella-Béguelin. |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | -------- | ----------------- | --- | --- |
2023. Analyzingleakageofpersonallyidentifiable
LouiseDeleger,KatalinMolnar,GuerganaSavova,Fei
|     |     |     |     |     |     | informationinlanguagemodels. |     |     |     | In2023IEEESym- |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | -------------- | --- | --- |
Xia,ToddLingren,QiLi,KeithMarsolo,AnilJegga, posiumonSecurityandPrivacy(SP),pages346–363.
| Megan Kaiser, |     | Laura | Stoutenborough, |     | et al. 2013. |     |     |     |     |     |     |     |
| ------------- | --- | ----- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
IEEE.
Large-scaleevaluationofautomatedclinicalnotede-
identificationanditsimpactoninformationextrac- StephenMeisenbacherandFlorianMatthes.2024. Just
tion. JournaloftheAmericanMedicalInformatics
|     |     |     |     |     |     | rewrite | it again: | A post-processing |     | method |     | for en- |
| --- | --- | --- | --- | --- | --- | ------- | --------- | ----------------- | --- | ------ | --- | ------- |
Association,20(1):84–94.
hancedsemanticsimilarityandprivacypreservation
|                         |     |     |                        |            |         | ofdifferentiallyprivaterewrittentext. |     |     |     |     | arXivpreprint |     |
| ----------------------- | --- | --- | ---------------------- | ---------- | ------- | ------------------------------------- | --- | --- | --- | --- | ------------- | --- |
| Franck Dernoncourt,     |     | Ji  | Young                  | Lee, Ozlem | Uzuner, | arXiv:2405.19831.                     |     |     |     |     |               |     |
| andPeterSzolovits.2017. |     |     | De-identificationofpa- |            |         |                                       |     |     |     |     |               |     |
tientnoteswithrecurrentneuralnetworks. Journal Multi-LingualityMulti-FunctionalityMulti-Granularity.
of the American Medical Informatics Association, 2024. M3-embedding: Multi-linguality, multi-
24(3):596–606. functionality, multi-granularity text embeddings
throughself-knowledgedistillation.
JosepDomingo-Ferrer,DavidSánchez,andJordiSoria-
|              |     |          |                |     |         | Yuta Nakamura, |     | Shouhei | Hanaoka, |     | Yukihiro | No- |
| ------------ | --- | -------- | -------------- | --- | ------- | -------------- | --- | ------- | -------- | --- | -------- | --- |
| Comas. 2022. |     | Database | anonymization: |     | privacy |                |     |         |          |     |          |     |
mura,NaotoHayashi,OsamuAbe,ShuntaroYada,
| models, | data utility, |     | and microaggregation-based |     |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inter-modelconnections. SpringerNature. Shoko Wakamiya, and Eiji Aramaki. 2020. Kart:
|     |     |     |     |     |     | Privacy | leakage | framework |     | of language |     | models |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --------- | --- | ----------- | --- | ------ |
MM Douglass, GD Cliffford, Andrew Reisner, pre-trained with clinical records. arXiv preprint
arXiv:2101.00036.
| WJ Long,       | GB        | Moody, | and RG        | Mark.   | 2005. De- |              |     |              |     |                     |     |     |
| -------------- | --------- | ------ | ------------- | ------- | --------- | ------------ | --- | ------------ | --- | ------------------- | --- | --- |
| identification | algorithm |        | for free-text | nursing | notes.    |              |     |              |     |                     |     |     |
|                |           |        |               |         |           | OpenAI.2024. |     | Hellogpt-4o. |     | https://openai.com/ |     |     |
InComputersinCardiology,2005,pages331–334.
index/hello-gpt-4o.
IEEE.
AnthiPapadopoulou,YunhaoYu,PierreLison,andLilja
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,
|     |     |     |     |     |     | Øvrelid.2022. |     | Neuraltextsanitizationwithexplicit |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------------------- | --- | --- | --- | --- |
AbhishekKadian,AhmadAl-Dahle,AieshaLetman,
|     |     |     |     |     |     | measuresofprivacyrisk. |     |     | InProceedingsofthe2nd |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --------------------- | --- | --- | --- |
Akhil Mathur, Alan Schelten, Amy Yang, Angela ConferenceoftheAsia-PacificChapteroftheAsso-
| Fan,etal.2024. |     | Thellama3herdofmodels. |     |     | arXiv |     |     |     |     |     |     |     |
| -------------- | --- | ---------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ciationforComputationalLinguisticsandthe12th
preprintarXiv:2407.21783.
InternationalJointConferenceonNaturalLanguage
|     |     |     |     |     |     | Processing(Volume1: |     |     | LongPapers),pages217–229. |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------------- | --- | --- | --- |
MarkElliot,ElaineMackey,KieronO’Hara,andCar-
| oline Tudor. | 2016. | The | anonymisation |     | decision- |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
FatemehKhodaParast,ChandniSindhav,SeemaNikam,
makingframework. UKAN. Hadiseh Izadi Yekta, Kenneth B Kent, and Saqib
|     |     |     |     |     |     | Hakak. | 2022. | Cloud | computing | security: |     | A sur- |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ----- | --------- | --------- | --- | ------ |
ZhihengHuang, WeiXu, andKaiYu.2015. Bidirec- veyofservice-basedmodels. Computers&Security,
| tionallstm-crfmodelsforsequencetagging. |     |     |     |     | arXiv | 114:102580. |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
preprintarXiv:1508.01991.
|     |     |     |     |     |     | Ildikó Pilán, |     | Pierre Lison, | Lilja | Øvrelid, | Anthi | Pa- |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | ----- | -------- | ----- | --- |
AlistairEWJohnson,LucasBulgarelli,andTomJPol- padopoulou,DavidSánchez,andMontserratBatet.
lard. 2020. Deidentification of free-text medical 2022. The text anonymization benchmark (tab):
recordsusingpre-trainedbidirectionaltransformers. A dedicated corpus and evaluation framework for
In Proceedings of the ACM Conference on Health, text anonymization. Computational Linguistics,
| Inference,andLearning,pages214–221. |     |     |     |     |     | 48(4):1053–1101. |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
5000

PatrickRuch,RobertHBaud,Anne-MarieRassinoux, Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex
PierretteBouillon,andGilbertRobert.2000. Medi- Smola. 2022. Automatic chain of thought prompt-
caldocumentanonymizationwithasemanticlexicon. ing in large language models. arXiv preprint
| InProceedingsoftheAMIASymposium,page729. |     |     |     |     |     | arXiv:2210.03493. |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
AmericanMedicalInformaticsAssociation.
A DetailsaboutPII
ZhiliShen,ZihangXi,YingHe,WeiTong,JingyuHua,
| and Sheng | Zhong.                                 | 2024. | The | fire thief | is also the |                   |     |     |     |
| --------- | -------------------------------------- | ----- | --- | ---------- | ----------- | ----------------- | --- | --- | --- |
| keeper:   | Balancingusabilityandprivacyinprompts. |       |     |            |             | A.1 PIIDefinition |     |     |     |
arXivpreprintarXiv:2406.14318. In this section, we follow previous work by cate-
gorizingPersonallyIdentifiableInformation(PII)
| Shreya Singhal, |     | Andres | Felipe | Zambrano, | Maciej |     |     |     |     |
| --------------- | --- | ------ | ------ | --------- | ------ | --- | --- | --- | --- |
Pankiewicz,XinerLiu,ChelseaPorter,andRyanS into the following two categories(Elliot et al.,
Baker.2024. De-identifyingstudentpersonallyiden- 2016,Domingo-Ferrer et al., 2022,Papadopoulou
| tifyinginformationwithgpt-4. |     |     |     | InProceedingsofthe |     | etal.,2022): |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------ | --- | ------------ | --- | --- | --- |
17thInternationalConferenceonEducationalData
Mining,pages559–565.
|     |     |     |     |     |     | • Direct | identifiers: | Information | that can |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ----------- | -------- |
Xiaofei Sun, Xiaoya Li, Jiwei Li, Fei Wu, Shangwei uniquely identify an individual within a
Guo,TianweiZhang,andGuoyinWang.2023. Text dataset(e.g. name, social security number,
classification via large language models. Preprint, emailaddress,etc).
arXiv:2305.08377.
Xiongtao Sun, Gan Liu, Zhipeng He, Hui Li, and • Quasi identifiers: Information that cannot
uniquelyidentifyanindividualontheirown
| Xiaoguang | Li. | 2024. | Deprompt: | Desensitization |     |     |     |     |     |
| --------- | --- | ----- | --------- | --------------- | --- | --- | --- | --- | --- |
andevaluationofpersonalidentifiableinformation butcandosowhencombinedwithotherquasi-
| in large | language | model | prompts. | arXiv | preprint |                  |                            |     |     |
| -------- | -------- | ----- | -------- | ----- | -------- | ---------------- | -------------------------- | --- | --- |
|          |          |       |          |       |          | identifiers(e.g. | age,gender,occupation,etc. |     |     |
arXiv:2408.08930.
Becauseoftheirhighsensitivityorthepotential
LeiWang,WanyuXu,YihuaiLan,ZhiqiangHu,Yunshi
Lan,RoyKa-WeiLee,andEe-PengLim.2023. Plan- toindirectlyidentifyanindividual,bothdirectand
and-solveprompting: Improvingzero-shotchain-of- quasi-identifiers are governed by strict legal and
| thoughtreasoningbylargelanguagemodels. |     |     |     |     | arXiv |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
privacystandardstoensurepersonalprivacy.
preprintarXiv:2305.04091.
A.2 PIITypes
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,
EdChi,SharanNarang,AakankshaChowdhery,and
UnlikePapadopoulouetal.’s(2022)classification,
| DennyZhou.2022. |     | Self-consistencyimproveschain |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
of thought reasoning in language models. arXiv weexcludetheMISCcategoryduetoitsambigu-
preprintarXiv:2203.11171. ousdefinitionandunclearboundaries. Ourtaxon-
omycomprisessevencategories:
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
|     |     |     |     |     |     | PER: Refers | to individuals’ | names, | including |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------ | --------- |
Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
etal.2022. Chain-of-thoughtpromptingelicitsrea- fullnames,aliases,andsocialmediausernames.
| soninginlargelanguagemodels. |     |     |     | Advancesinneural |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
CODE:Encompassesidentifyingnumbersand
informationprocessingsystems,35:24824–24837. codeslikesocialsecuritynumbers,phonenumbers,
passportnumbers,emailaddresses,etc.
IpKinAnthonyWong,QiLilithLian,andDanniSun.
2023. Autonomoustraveldecision-making: Anearly LOC: Covers geographical locations such as
| glimpse | into chatgpt |     | and generative | ai. | Journal of |     |     |     |     |
| ------- | ------------ | --- | -------------- | --- | ---------- | --- | --- | --- | --- |
homeorworkaddresses,cities,countries,etc.
HospitalityandTourismManagement,56:253–263. ORG:Pertainstothenamesofentitieslikecom-
panies,schools,publicinstitutions,etc.
AnYang,BaosongYang,BeichenZhang,BinyuanHui,
BoZheng,BowenYu,ChengyuanLi,DayihengLiu, DEM:Representsdemographicinformationin-
| Fei Huang, | Haoran | Wei, | et al. | 2024a. | Qwen2. 5 |     |     |     |     |
| ---------- | ------ | ---- | ------ | ------ | -------- | --- | --- | --- | --- |
cludingage,gender,nationality,occupation,educa-
| technicalreport. |     | arXivpreprintarXiv:2412.15115. |     |     |     | tionlevel,etc. |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | -------------- | --- | --- | --- |
DATETIME:Indicatesspecificdates,times,or
| Songhua Yang, | Hanjie |     | Zhao, Senbin | Zhu, | Guangyu |     |     |     |     |
| ------------- | ------ | --- | ------------ | ---- | ------- | --- | --- | --- | --- |
Zhou,HongfeiXu,YuxiangJia,andHongyingZan. durations, such as birthdates, appointment times,
| 2024b. | Zhongjing: | Enhancingthechinesemedical |     |     |     |     |     |     |     |
| ------ | ---------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
etc.
capabilitiesoflargelanguagemodelthroughexpert
|                                          |     |     |     |     |        | QUANTITY:         | Refers  | to significant | numerical |
| ---------------------------------------- | --- | --- | --- | --- | ------ | ----------------- | ------- | -------------- | --------- |
| feedbackandreal-worldmulti-turndialogue. |     |     |     |     | InPro- |                   |         |                |           |
|                                          |     |     |     |     |        | data like monthly | income, | expenditures,  | loan      |
ceedingsoftheAAAIConferenceonArtificialIntelli-
| gence,volume38,pages19368–19376. |     |     |     |     |     | amount,creditscore,etc. |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
5001

A.3 StatisticsofPIITypes Counts of PII Types in Different Datasets
|     |     |     |     |     |     |     | 3000 |     |     |     | Datasets |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | -------- |
PII_single_final
PII_multi_final
Figure 5 and Table 10 present the distribution of 2500 PII_hard
PII_distract
| PII types | across | our | datasets: |     | PII-single | (1,214 |     |     |     |     |     |
| --------- | ------ | --- | --------- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
2000
samples),PII-multi(1,228samples),PII-hard(200
stnuoC
| samples),andPII-distract(200samples). |     |     |     |     |     |     | 1500 |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
1000
| • TypeFrequencies:                        |     |          | Organization(ORG)and |     |           |      |     |         |      |                   |         |
| ----------------------------------------- | --- | -------- | -------------------- | --- | --------- | ---- | --- | ------- | ---- | ----------------- | ------- |
| Code-basedidentifiers(CODE)constitutesig- |     |          |                      |     |           |      | 500 |         |      |                   |         |
| nificant                                  |     | portions | across               | all | datasets, | with |     |         |      |                   |         |
|                                           |     |          |                      |     |           |      | 0   | PER DEM | CODE | DATETIME QUANTITY | ORG LOC |
17.09%and15.74%inPII-single,and13.47%
and 15.31% in PII-multi, respectively. This Figure 5: Distribution of PII types across different
datasetsinPII-Bench.
| distribution |     | reflects     |     | the prevalence |             | of insti- |     |     |     |     |     |
| ------------ | --- | ------------ | --- | -------------- | ----------- | --------- | --- | --- | --- | --- | --- |
| tutional     |     | affiliations | and | digital        | identifiers | in        |     |     |     |     |     |
real-worldscenarios.
|     |     |     |     |     |     |     | 2. Contact | Information: |     | Creating syntactically |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ---------------------- | --- |
correctemailaddresses,phonenumbers,and
| • Dataset |     | Composition: |     | PII-multi |     | contains |     |     |     |     |     |
| --------- | --- | ------------ | --- | --------- | --- | -------- | --- | --- | --- | --- | --- |
IPaddresses.
16,136PIIentitiesacrossallcategories,main-
taining balanced proportions ranging from 3. FinancialData: Producingproperlyformatted
| 13.47%to15.77%formosttypes. |     |     |     |     |     | PII-single |                    |     |     |                     |     |
| --------------------------- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | ------------------- | --- |
|                             |     |     |     |     |     |            | creditcardnumbers, |     |     | bankaccountnumbers, |     |
follows a similar pattern with 9,303 entities, andothernumericalidentifierswithappropri-
| demonstratingconsistentcoverageacrossdif- |     |     |     |     |     |     | atecheckdigits. |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
ferentPIIcategories.
|                                         |     |      |       |               |     |         | 4. Temporal                              |     | Information: | Generating | dates, |
| --------------------------------------- | --- | ---- | ----- | ------------- | --- | ------- | ---------------------------------------- | --- | ------------ | ---------- | ------ |
| •                                       |     |      | Sets: | PII-distract, |     | despite |                                          |     |              |            |        |
| Specialized                             |     | Test |       |               |     |         | times,anddurationswithinreasonableranges |     |              |            |        |
| comprisingonly200samples,contains10,211 |     |      |       |               |     |         | andformats.                              |     |              |            |        |
PIIentitiesduetoitsmulti-descriptiondesign.
| PII-hard                                 |     | maintains | balanced |     | type | coverage |      |            |             |                 |              |
| ---------------------------------------- | --- | --------- | -------- | --- | ---- | -------- | ---- | ---------- | ----------- | --------------- | ------------ |
|                                          |     |           |          |     |      |          |      | PII_single | PII_multi   | PII_hard        | PII_distract |
| with1,834entities,withproportionsvarying |     |           |          |     |      |          | Type |            |             |                 |              |
|                                          |     |           |          |     |      |          |      | #          | % #         | % # %           | # %          |
|                                          |     |           |          |     |      |          | PER  | 1,214      | 13.05 2,456 | 15.22 286 15.59 | 1,449 14.19  |
from12.10%to16.58%.
|     |     |     |     |     |     |     | DEM  | 1,220 | 13.12 2,450 | 15.18 286 15.59 | 1,467 14.37 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ----------- | --------------- | ----------- |
|     |     |     |     |     |     |     | CODE | 1,464 | 15.74 2,470 | 15.31 222 12.10 | 1,605 15.72 |
|     |     |     |     |     |     |     | ORG  | 1,590 | 17.09 2,544 | 13.47 251 13.69 | 1,673 16.38 |
B PIIEntityGenerationMethods
|     |     |     |     |     |     |     | LOC      | 1,053 | 11.32 1,516 | 15.77 304 16.58 | 1,008 9.87  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----------- | --------------- | ----------- |
|     |     |     |     |     |     |     | DATETIME | 1,368 | 14.70 2,526 | 15.65 251 13.69 | 1,559 15.27 |
|     |     |     |     |     |     |     | QUANTITY | 1,394 | 14.98 2,174 | 9.40 234 12.76  | 1,450 14.20 |
ThegenerationofPIIentitiesrequirescarefulcon- 9,303 100 16,136 100 1,834 100 10,211 100
Total
siderationofbothstructuralconstraintsandseman-
tic plausibility. We employ two complementary Table10: DetailedstatisticsofPIItypesacrossdatasets.
Foreachdataset,wereportboththeabsolutecount(#)
| approachesforentitygeneration: |     |     |     |     | rule-basedgener- |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
andrelativepercentage(%)ofeachPIItype.
ationforstructuredPIItypesandlanguagemodel-
| based generation |     | for | context-dependent |     |     | informa- |     |     |     |     |     |
| ---------------- | --- | --- | ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
tion.
B.2 LanguageModel-basedGeneration
B.1 Rule-basedGeneration For PII types requiring contextual understanding
andreal-worldknowledge,weleveragelargelan-
| For PII | types | with | well-defined |     | formats | or enu- |     |     |     |     |     |
| ------- | ----- | ---- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- |
guagemodelsthroughcarefullydesignedprompts.
| merable | value | sets, | we implement |     | deterministic |     |     |     |     |     |     |
| ------- | ----- | ----- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
Thisapproachisessentialforgenerating:
| generation | methods. |     | These | methods |     | encompass |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ------- | --- | --------- | --- | --- | --- | --- | --- |
bothcustomrule-basedalgorithmsandtheFaker
|     |     |     |     |     |     |     | 1. Location |     | Information: | Coherent | and geo- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | -------- | -------- |
library’s standardized functions. The rule-based graphically accurate addresses, landmarks,
| approachisparticularlyeffectivefor: |     |     |     |     |     |     | andregionaldescriptions. |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
1. IdentificationNumbers: Generatingvalidfor- 2. OrganizationalEntities: Plausiblenamesfor
mats for social security numbers, passport educationalinstitutions,companies,andother
numbers,andemployeeIDswhilemaintain- organizations that reflect real-world naming
| ingregionalcompliance. |     |     |     |     |     |     | conventions. |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
5002

3. DemographicAttributes: Culturallyappropri- sampledentities;(2)modifyonlytheentityvalues
ateandconsistentdemographicinformation, whilepreservingtheirPIItypeandcategorylabels;
including ethnicity, nationality, and educa- (3) maximize entity retention to maintain dataset
tionalbackground. richness. For instance, given a conflict between
|     |     |     |     |     |     |     |     | “Age: 22years”and“WorkExperience: |     |     |     | 15years |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ------- | --- |
B.3 EntityCategoriesandGeneration asSeniorEngineer”,theoptimizationadjuststhe
|     | Methods |     |     |     |     |     |     | work experience | to  | “2 years | as Junior | Engineer” |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------- | --------- | --- |
Table11presentsacomprehensivemappingofPII rather than removing the entity entirely, thereby
preservingboththePIItype(DEM)andtheentity
| typestotheirrespectivegenerationmethods. |     |     |     |     |     |     | The |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tablesystematicallycategorizes55distinctPIIen- category(WorkExperience).
| titiesacrosssevenmaincategories: |        |       |     |             | PersonalIden- |         |     |                                          |     |     |     |     |     |
| -------------------------------- | ------ | ----- | --- | ----------- | ------------- | ------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
|                                  |        |       |     |             |               |         |     | C.2 Multi-SubjectConsistencyOptimization |     |     |     |     |     |
| tifiers                          | (PER), | Codes |     | and Numbers |               | (CODE), | Lo- |                                          |     |     |     |     |     |
cation Information (LOC), Organizational Affili- Multi-subject optimization extends the single-
ations(ORG),DemographicInformation(DEM), subjectprocessbyintroducingrelationship-aware
TemporalData(DATETIME),andQuantitativeVal- constraints. Consistencyrulesareenforcedbased
| ues(QUANTITY). |     |     |     |     |     |     |     | onthreerelationshipcategories: |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
C ConsistencyOptimizationDetails
|     |     |     |     |     |     |     |     | • Intersectionrelationships(e.g.,colleagues, |          |      |       |          |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | -------- | ---- | ----- | -------- | --- |
|     |     |     |     |     |     |     |     | classmates):                                 | Subjects | must | share | critical | at- |
Theconsistencyoptimizationprocessiscriticalfor
|     |     |     |     |     |     |     |     | tributes | suchas | organizationname, |     | work | lo- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------------- | --- | ---- | --- |
ensuringthatrandomlysampledPIIentitiesform
|                                        |     |      |           |     |          |          |     | cation for         | colleagues, | or                      | educational |              | institu- |
| -------------------------------------- | --- | ---- | --------- | --- | -------- | -------- | --- | ------------------ | ----------- | ----------------------- | ----------- | ------------ | -------- |
| logicallycoherentandrealisticprofiles. |     |      |           |     |          | Weemploy |     |                    |             |                         |             |              |          |
|                                        |     |      |           |     |          |          |     | tionforclassmates. |             | Theoptimizationverifies |             |              |          |
| GPT-4-0806                             |     | with | carefully |     | designed | prompts  | to  |                    |             |                         |             |              |          |
|                                        |     |      |           |     |          |          |     | attribute          | alignment   | and                     | adjusts     | inconsistent |          |
identifyandresolveconflictswhilepreservingthe
entitiesaccordingly.
diversityandcoverageofPIItypes.
|     |     |     |     |     |     |     |     | • Hierarchical |     | relationships | (e.g., |     | parent- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | ------ | --- | ------- |
C.1 Single-SubjectConsistencyOptimization
|     |                |     |               |     |     |              |     | child,supervisor-subordinate): |     |     | Structuralcon- |     |     |
| --- | -------------- | --- | ------------- | --- | --- | ------------ | --- | ------------------------------ | --- | --- | -------------- | --- | --- |
| For | single-subject |     | descriptions, |     | the | optimization |     |                                |     |     |                |     |     |
straintsareenforcedsuchasagedifferences
| process | addresses |     | intra-subject |     | conflicts | arising |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(parentatleast18-20yearsolderthanchild),
| fromincompatibleentitycombinations. |     |     |     |     |     | Common |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
authoritylevels(supervisorholdinghigherpo-
conflictpatternsinclude:
sitionthansubordinate),andderivedattributes
|     |            |     |                  |     |     |            |     | (children | inheriting | nationality |     | or ethnicity |     |
| --- | ---------- | --- | ---------------- | --- | --- | ---------- | --- | --------- | ---------- | ----------- | --- | ------------ | --- |
|     | • Temporal |     | inconsistencies: |     | Age | incompati- |     |           |            |             |     |              |     |
fromparentswhenculturallyappropriate).
blewithworkexperienceduration,education
level,orcareerstage(e.g.,a23-year-oldwith
|     |     |     |     |     |     |     |     | • Non-intersection |     | relationships: |     | Subjects |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------------- | --- | -------- | --- |
15yearsofworkexperience).
maintainindependententitysetswithnoen-
forceddependencies,thoughinternalconsis-
|     | • Professionalmismatches: |     |     |     | Occupationincon- |     |     |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tencywithineachsubject’sprofileisstillveri-
|     | sistent                                 | with | education | background |     | or  | salary |       |     |     |     |     |     |
| --- | --------------------------------------- | ---- | --------- | ---------- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- |
|     | range(e.g.,ahighschoolgraduateworkingas |      |           |            |     |     |        | fied. |     |     |     |     |     |
alicensedphysician).
Themulti-subjectprompt(Figure11)provides
• Geographiccontradictions: Worklocation relationshipcontextandrequiresthemodeltoout-
distantfromresidentialaddresswithoutsup- putseparate,coordinatedentitysetsforeachsub-
porting evidence (e.g., daily commute span- ject. Thisrelationship-awareapproachensuresthat
ningdifferentcontinents). multi-subjectdescriptionsreflectrealisticinterper-
sonaldynamicsandmaintainnarrativecoherence
|     | • Financialimplausibility: |     |     |     | Income,expenses, |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
acrossprofiles.
andsavingsthatviolatebasiceconomiccon-
straints (e.g., monthly expenses exceeding D QueryScenarioDesignDetails
monthlyincomebyordersofmagnitude).
Thescenariodesignphasebridgesthegapbetween
The optimization prompt (Figure 10) instructs abstractentityselectionandnaturaluserqueriesby
themodelto: (1)identifylogicalconflictsamong groundingqueriesinrealisticapplicationcontexts.
5003

| PIIType | EntityCategory    | GenerationApproach | FormatConstraints     |
| ------- | ----------------- | ------------------ | --------------------- |
|         | FullName          | Rule-based         | [FirstName][LastName] |
|         | SocialMediaHandle | Rule-based         | [@][a-zA-Z0-9]5,15    |
PER
|          | Nickname               | LLM-based  | -                     |
| -------- | ---------------------- | ---------- | --------------------- |
|          | SocialSecurityNumber   | Rule-based | XXX-XX-XXXX           |
|          | Driver’sLicense        | Rule-based | [A-Z][0-9]8           |
|          | BankAccount            | Rule-based | [0-9]10,12            |
|          | CreditCard             | Rule-based | [0-9]16               |
|          | PhoneNumber            | Rule-based | +[0-9]1,3-[0-9]10     |
|          | IPAddress              | Rule-based | IPv4/IPv6format       |
| CODE     | EmailAddress           | Rule-based | [user]@[domain].[tld] |
|          | PasswordHash           | Rule-based | SHA-256               |
|          | PassportNumber         | Rule-based | [A-Z][0-9]8           |
|          | TaxID                  | Rule-based | [0-9]9                |
|          | EmployeeID             | Rule-based | [A-Z]2[0-9]6          |
|          | StudentID              | Rule-based | [0-9]8                |
|          | StreetAddress          | LLM-based  | -                     |
| LOC      | City/Region            | LLM-based  | -                     |
|          | Landmark               | LLM-based  | -                     |
|          | CompanyName            | LLM-based  | -                     |
|          | EducationalInstitution | LLM-based  | -                     |
| ORG      | GovernmentAgency       | LLM-based  | -                     |
|          | NGO                    | LLM-based  | -                     |
|          | HealthcareFacility     | LLM-based  | -                     |
|          | Occupation             | Rule-based | Predefinedlist        |
|          | Age                    | Rule-based | [0-9]1,3              |
|          | Gender                 | Rule-based | Binary/Non-binary     |
|          | Height                 | Rule-based | [0-9]3cm/[0-9]’[0-9]" |
|          | Weight                 | Rule-based | [0-9]2,3kg/lbs        |
|          | BloodType              | Rule-based | A/B/O[+-]             |
|          | SexualOrientation      | Rule-based | Predefinedlist        |
|          | Nationality            | LLM-based  | -                     |
| DEM      | Ethnicity              | LLM-based  | -                     |
|          | Race                   | LLM-based  | -                     |
|          | ReligiousBelief        | LLM-based  | -                     |
|          | PoliticalAffiliation   | LLM-based  | -                     |
|          | EducationLevel         | LLM-based  | -                     |
|          | AcademicDegree         | LLM-based  | -                     |
|          | PhysicalFeatures       | LLM-based  | -                     |
|          | MedicalCondition       | LLM-based  | -                     |
|          | DisabilityStatus       | LLM-based  | -                     |
|          | Date                   | Rule-based | YYYY-MM-DD            |
| DATETIME | Time                   | Rule-based | HH:MM:SS              |
|          | Duration               | Rule-based | [0-9]+[dhms]          |
|          | MonthlyIncome          | Rule-based | [Currency][0-9]+      |
|          | MonthlyExpenses        | Rule-based | [Currency][0-9]+      |
|          | AccountBalance         | Rule-based | [Currency][0-9]+      |
|          | LoanAmount             | Rule-based | [Currency][0-9]+      |
|          | AnnualBonus            | Rule-based | [Currency][0-9]+      |
|          | CreditLimit            | Rule-based | [Currency][0-9]+      |
QUANTITY
|     | SocialSecurityPayment | Rule-based | [Currency][0-9]+ |
| --- | --------------------- | ---------- | ---------------- |
|     | TaxPayment            | Rule-based | [Currency][0-9]+ |
|     | DebtRatio             | Rule-based | [0-9]1,2.[0-9]2% |
|     | InvestmentReturn      | Rule-based | [0-9]1,2.[0-9]2% |
|     | ROI                   | Rule-based | [0-9]1,2.[0-9]2% |
|     | CreditScore           | Rule-based | [300-850]        |
Table11: ComprehensivecategorizationofPIIentitiesandtheirgenerationmethods. Rule-basedgenerationfollows
specificformatconstraints,whileLLM-basedgenerationproducescontextuallyappropriatecontentwithoutrigid
formattingrequirements.
5004

Thisprocessisessentialforevaluatingwhetherpri- This rigorous scenario design process ensures
vacyprotectionsystemscanidentifyquery-relevant thatPII-Benchqueriesreflectauthenticinformation
PIIinauthenticusagescenarios. needsacrossdiversedomains,providingarealistic
testbedforevaluatingquery-awareprivacyprotec-
D.1 Domain-SpecificScenarioGeneration
tionsystems.
| Given | a set | of selected | entities | , we | employ | a   |     |     |     |     |     |     |     |
| ----- | ----- | ----------- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
E q
structuredpromptingstrategytogeneratediverse
|                   |     |     |                          |     |     |     | E HumanEvaluationDetails |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------------------ | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| scenariocontexts. |     |     | ThepromptinstructstheLLM |     |     |     |                          |     |     |     |     |     |     |
to:
ThehumanevaluationofPII-Benchwasconducted
|     |                         |     |     |                  |     |     | with 25                     | graduate | students | specializing |                   | in  | data se- |
| --- | ----------------------- | --- | --- | ---------------- | --- | --- | --------------------------- | -------- | -------- | ------------ | ----------------- | --- | -------- |
| 1.  | Analyzeentitysemantics: |     |     | Determinethethe- |     |     |                             |          |          |              |                   |     |          |
|     |                         |     |     |                  |     |     | curityandprivacyprotection. |          |          |              | Allevaluatorswere |     |          |
maticdomainimpliedbytheselectedentities
|     |     |     |     |     |     |     | pursuing | their | Master’s | or  | Ph.D. degrees |     | with at |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | --- | ------------- | --- | ------- |
(e.g.,educationandworkexperiencesuggest
leasttwoyearsofresearchexperienceinprivacy-
|     | career-related |     | scenarios; medical |     | conditions |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
preservingmachinelearningordataprotectionsys-
|     | and medications |     | suggest healthcare |     | scenar- |     |       |                |     |         |           |     |       |
| --- | --------------- | --- | ------------------ | --- | ------- | --- | ----- | -------------- | --- | ------- | --------- | --- | ----- |
|     |                 |     |                    |     |         |     | tems. | The evaluation |     | process | consisted | of  | three |
ios).
|     |     |     |     |     |     |     | phases: | preparation,evaluation,andvalidation. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------- | --- | --- | --- | --- | --- |
2. Generatescenariocandidates: Proposemul- During the preparation phase, participants at-
tiplescenariotypesthatnaturallyrequireall tendeda4-hourtrainingsessioncoveringPIItax-
selectedentities,ensuringthematicdiversity onomy,recognitionguidelines,andquery-related
acrossthedataset. Examplescenariosinclude detectioncriteria. Thesessionincludedhands-on
careerplanning,medicalconsultation,finan- practicewithrepresentativecasesfromeachdataset
cialadvisory,legalcounseling,academicmen- component. Participantsthencompletedaqualifi-
toring,andhousingapplications.
cationtestfeaturing20diverseinstances,requiring
90%agreementwithexpertassessmentstoproceed
3. Ensureentitynecessity: Verifythateachse- totheformalevaluation.
lectedentityismeaningfullyincorporatedinto
|     |     |     |     |     |     |     | During | the | evaluation | phase, | participants |     | used |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | ------ | ------------ | --- | ---- |
thescenarioratherthansuperficiallyincluded,
|     |         |                |            |     |         |      | our specialized |     | platform | designed |            | for systematic |         |
| --- | ------- | -------------- | ---------- | --- | ------- | ---- | --------------- | --- | -------- | -------- | ---------- | -------------- | ------- |
|     | so that | query-relevant | PII labels |     | reflect | gen- |                 |     |          |          |            |                |         |
|     |         |                |            |     |         |      | PII assessment. |     | To       | maintain | consistent |                | perfor- |
uineinformationdependencies.
mance,welimitedevaluationsessionstotwohours
anddistributedinstancesacrossatwo-weekperiod.
| The    | scenario | generation   | prompt   | is  | provided     | in  |              |     |               |     |         |            |     |
| ------ | -------- | ------------ | -------- | --- | ------------ | --- | ------------ | --- | ------------- | --- | ------- | ---------- | --- |
|        |          |              |          |     |              |     | The platform |     | automatically |     | tracked | assessment |     |
| Figure | 12.      | By requiring | coverage | of  | all selected |     |              |     |               |     |         |            |     |
timeandaccuracymetricswhileenforcingoureval-
entitieswhilemaintainingscenariodiversity,this
|     |     |     |     |     |     |     | uation | protocol: | participants |     | first | performed | PII |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------------ | --- | ----- | --------- | --- |
approachproducesqueriesthatrealisticallyreflect
detectionbymarkingentityspans,linkingthemto
specializeduserinformationneedsacrossdomains.
subjects,andassigningPIItypes,beforeproceed-
ingtoquery-relateddetection.
D.2 ScenarioValidationandFiltering
|     |     |     |     |     |     |     | Our | validation | process | incorporated |     | both | auto- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------ | --- | ---- | ----- |
Generatedscenariosundergovalidationtoensure
|     |     |     |     |     |     |     | mated | and manual | checks |     | to ensure | assessment |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------ | --- | --------- | ---------- | --- |
qualityanddiversity:
|     |                    |     |                       |     |     |     | quality.                              | Theplatformautomaticallyverifiedassess- |     |     |     |     |       |
| --- | ------------------ | --- | --------------------- | --- | --- | --- | ------------------------------------- | --------------------------------------- | --- | --- | --- | --- | ----- |
|     |                    |     |                       |     |     |     | mentcompletenessandformatconsistency. |                                         |     |     |     |     | Cases |
| •   | Completenesscheck: |     | Verifythatallentities |     |     |     |                                       |                                         |     |     |     |     |       |
withsubstantialdisagreement(Fleiss’kappa<0.6)
|     | in  | are semantically | incorporated |     | into | the |     |     |     |     |     |     |     |
| --- | --- | ---------------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
q
|     | E   |     |     |     |     |     | underwent | expert | review | by  | two authors | with | ex- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------ | --- | ----------- | ---- | --- |
scenariocontext.
tensiveexperienceinprivacy-preservingsystems.
Evaluatorsreceiveddetailedfeedbackontheirper-
| •   | Realism | assessment: | Confirm | that | the | sce- |     |     |     |     |     |     |     |
| --- | ------- | ----------- | ------- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
formanceandparticipatedindiscussionsessionsto
nariorepresentsplausiblereal-worldinterac-
resolvesystematicdiscrepancies.
tionswithAIsystems.
Compensationwasstructuredtoencourageboth
• Diversity enforcement: Track scenario dis- accuracyandefficiency,withabaserateof$30per
tributionandrejectover-representedscenario hourandperformancebonusesbasedonagreement
|     | typestomaintainbalanceddomaincoverage. |     |     |     |     |     | withotherevaluators. |     |     |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
5005

1
F ExperimentDetails
F1 = F1 (p ,g )
strict strict i j
max( , )
F.1 EvaluationMetrics P G (pi,g Xj) ∈ M ∗
(10)
Theevaluationframeworkemploysdistinctmetrics
P , R , andF1 arecomputedanalo-
span span span
forPIIdetectionandquery-relateddetectiontasks.
gously.
For PII detection, let = p ,...,p denote
P { 1 m } For query-related detection, given a predicted
thepredictedsubjectsetand = g ,...,g de-
G { 1 n } entityset p andgroundtruthset g ,wecompute:
notethegroundtruthsubjectset. Eachsubjectp E E
i
or g contains a set of entity-type pairs (e,t) ,
j p g
{ } P = |E ∩E | (11)
whereerepresentstheentityspanandtrepresents query
p
|E |
itsPIItype.
Foreachsubjectpair(p i ,g j ),wecomputethree R = |E p ∩E g | (12)
query
typesofevaluationmetrics:
g
|E |
1. Strict Matching: Both entity spans and their
2 P R
query query
typesmustmatchexactly: F1 query = · · (13)
P +R
query query
E E
P (p ,g ) = |
pi
∩
gj|
(1)
ForbothPIIdetectionandquery-relateddetec-
strict i j
|
E pi| tiontasks,weadditionallyemployRouge-Lbased
fuzzymatchingtohandlepartialmatchesbetween
E E
R (p ,g ) = | pi ∩ gj| (2) entity spans. Instead of using exact set intersec-
strict i j
E
|
gj| tion,theRouge-Lscoreisusedtomeasuretextual
2 P (p ,g ) R (p ,g ) similaritybetweenentities:
strict i j strict i j
F1 (p ,g ) = · ·
strict i j
P (p ,g )+R (p ,g )
strict i j strict i j 1
(3) P = max Rouge-L(e ,e ) (14)
fuzzy p g
whereE pi andE gj arethesetsofentity-typepairs. |E p | e Xp
∈E
p eg ∈E g
2. Entity-onlyMatching: Onlyentityspansneed
1
tomatch: R = max Rouge-L(e ,e )
fuzzy p g
g ep p
P (p ,g ) = |
S pi
∩
S gj|
(4)
|E | e Xg ∈E g ∈E
(15)
ent i j
| S pi| F1 = 2 · P fuzzy · R fuzzy (16)
fuzzy
P +R
S S fuzzy fuzzy
R (p ,g ) = |
pi
∩
gj|
(5)
ent i j
|
S gj| whereRouge-L(e p ,e g )computesthelongestcom-
monsubsequence-basedF-scorebetweenpredicted
2 P (p ,g ) R (p ,g )
ent i j ent i j
F1 ent (p i ,g j ) = · · entitye p andgroundtruthentitye g .
P (p ,g )+R (p ,g )
ent i j ent i j
(6)
F.2 Privacy-UtilityTradeoffMetrics
whereS andS arethesetsofentityspans.
pi gj
Wedevelopacomprehensiveevaluationframework
TheoptimalsubjectmatchingM isdetermined
∗
to quantify the tradeoff between privacy protec-
bymaximizingthestrictF1score:
tionandqueryutilityacrossdifferentPIImasking
strategies.
M ∗ = max F1 strict (p i ,g j ) (7)
M
∈M(pi, X gj) ∈ M F.2.1 PrivacyProtectionMetric
where denotesallpossibleone-to-onemappings Let = e 1 ,...,e n denotethesetofPIIentitiesin
betwee M npredictedandgroundtruthsubjects. theo E rigin { altextT o } ,andT m representthemasked
Thefinalrecognitionscoresarecomputedover text. TheprivacyscoreP measurestheproportion
theoptimalmatchingpairs: ofPIIentitiessuccessfullyprotected:
1 C(e,T )
P strict = P strict (p i ,g j ) (8) P = 1 e ∈E m (17)
− C(e,T )
|P| (pi,g Xj) ∈ M ∗ Pe ∈E o
where C(e,T) couPnts occurrences of entity e
1
R = R (p ,g ) (9) in text T. A score of P = 1 indicates complete
strict strict i j
protection,whileP = 0indicatesnoprotection.
|G| (pi,g Xj)
∈
M
∗
5006

F.2.2 UtilityPreservationMetrics deployment-ready models and larger proprietary
To measure utility preservation, we employ two systems. The 0.5B and 1.5B models exhibit ex-
tremelylimitedcapabilitiesacrossalltasks(with
complementaryapproaches:
|          |            |     |     |         |            |     | F1 scores | generally |     | below | 0.2), rendering | them |
| -------- | ---------- | --- | --- | ------- | ---------- | --- | --------- | --------- | --- | ----- | --------------- | ---- |
| Semantic | Similarity |     | We  | compute | embedding- |     |           |           |     |       |                 |      |
practicallyunusableforreal-worldPIIprotection.
basedsimilaritybetweenresponsesgeneratedfrom While the 3B model shows modest potential (F1
| masked | prompts | (R  | ) and | unmasked |     | prompts |                                                |     |     |     |     |     |
| ------ | ------- | --- | ----- | -------- | --- | ------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|        |         |     | m     |          |     |         | scoresapproaching0.6onsimplerdatasets),itsper- |     |     |     |     |     |
(R ):
| o   |     |     |     |     |     |     | formance | remains | substantially |     | inferior | to larger |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------------- | --- | -------- | --------- |
models,particularlyonchallengingscenarios(e.g.,
|     |     | U = | cos(v | ,v    | )   | (18) |                         |     |     |                         |     |     |
| --- | --- | --- | ----- | ----- | --- | ---- | ----------------------- | --- | --- | ----------------------- | --- | --- |
|     |     | s   |       | Rm Ro |     |      | PII-Hard,PII-Distract). |     |     | Thesefindingsunderscore |     |     |
where v is the text embedding generated by the tension between privacy goals and model ca-
R
BGE-M3 (Multi-Granularity, 2024), and cos( , ) pabilities: whilesmalleron-devicemodelswould
· ·
bepreferablefromaprivacyperspective,theycur-
| computes | cosine | similarity. |     | This | metric | captures |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- |
semanticpreservationindependentofexactword- rently lack the sophistication needed for reliable
| ing.                   |     |     |     |                 |     |     | PIImanagement. |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
| LLM-as-JudgeEvaluation |     |     |     | WeemployClaude- |     |     |                |     |     |     |     |     |
F.4 SupplementaryResultsonPII-Real
3.7-Sonnettoassessresponsequalitythroughdirect
Dataset
comparison:
ToempiricallyvalidatePII-Bench’sabilitytocap-
|     |     | Judge(R1 |     | ,R2 |      |      |                                               |              |     |         |          |           |
| --- | --- | -------- | --- | --- | ---- | ---- | --------------------------------------------- | ------------ | --- | ------- | -------- | --------- |
|     | U   | =        |     |     | ,R ) | (19) | turereal-worldprivacychallenges,weconstructed |              |     |         |          |           |
|     |     | l        |     | m m | o    |      |                                               |              |     |         |          |           |
|     |     |          |     |     |      |      | PII-Real,                                     | a validation |     | dataset | based on | authentic |
R1 R2
| where                              |     | and | represent |     | responses | from      |                          |     |     |     |     |     |
| ---------------------------------- | --- | --- | --------- | --- | --------- | --------- | ------------------------ | --- | --- | --- | --- | --- |
|                                    | m   |     | m         |     |           |           | biographicalinformation. |     |     |     |     |     |
| twodifferentmaskingstrategies,andR |     |     |           |     |           | istheref- |                          |     |     |     |     |     |
o
| erenceresponsefromunmaskedtext. |     |     |     |     | Thejudgeas- |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
F.4.1 DatasetConstruction
| signsnumericalratingsr |     |     |     | [1,10]toeachmasked |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
∈
|     |     |     |     |     |     |     | We selected |     | 20 prominent |     | AI researchers | from |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | -------------- | ---- |
responsebasedonhowwellitpreservesthequery
ranking1
intentcomparedtothereference. Tomitigatepo- the AMiner AI2000 and manually cu-
ratedtheirprofessionalprofilesfrompubliclyavail-
sitionbias,werandomlyalternatethepresentation
ablesourcesincludingconferencewebsites,insti-
orderofresponses.
|     |     |     |     |     |     |     | tutional | pages, | and | academic | publications. | Each |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | -------- | ------------- | ---- |
F.2.3 BalancedMetric profileunderwentexpertannotationbytheauthors
To quantify the overall effectiveness of masking followingourestablishedPIItaxonomy,ensuring
strategies, we compute a balanced score B that consistencywithPII-Benchguidelines.
| combines | privacy | protection |     | and | utility | preserva- |     |     |     |     |     |     |
| -------- | ------- | ---------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
UnlikePII-Bench’sautomatedquerygeneration,
tion:
|     |     |     |     |     |     |     | PII-Real | features | human-written |     | queries | crafted |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | --- | ------- | ------- |
bydomainexpertstoreflectauthenticinformation
|     |     | B = αP | +(1 | α)U |     |      |                                             |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |        |     |     |     | (20) | needs. Wedesignedqueriesspanningcareerplan- |     |     |     |     |     |
−
where α [0,1] is a weighting parameter that ning, research collaboration, academic advising,
|     | ∈   |     |     |     |     |     | and startup | leadership |     | scenarios | for each | profile. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------- | -------- | -------- |
determinestherelativeimportanceofprivacyver-
Theresultingdatasetcomprises100instanceswith
| susutility. | Inourexperiments,weuseα |     |     |     |     | = 0.5to |     |     |     |     |     |     |
| ----------- | ----------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
assignequalimportancetobothaspects. manually annotated PII entities, providing an au-
thentictestbedforvalidatingsyntheticdataquality.
| The | complete | prompt |     | template | for | LLM-as- |        |     |         |            |              |     |
| --- | -------- | ------ | --- | -------- | --- | ------- | ------ | --- | ------- | ---------- | ------------ | --- |
|     |          |        |     |          |     |         | Tables | 18, | 19, and | 20 present | experimental | re- |
JudgeevaluationisprovidedinFigure20.
sultsacrossthreeevaluationtasks.
F.3 AdditionalExperimentswithSmaller
| LanguageModels |                  |     |                 |        |     |            | F.4.2         | ConsistencyAnalysis |            |         |                  |     |
| -------------- | ---------------- | --- | --------------- | ------ | --- | ---------- | ------------- | ------------------- | ---------- | ------- | ---------------- | --- |
| We have        | conducted        |     | a comprehensive |        |     | evaluation |               |                     |            |         |                  |     |
|                |                  |     |                 |        |     |            | We quantified |                     | alignment  | between | PII-Single       | and |
| on smaller,    | deployment-ready |     |                 | models |     | (0.5B-3B   |               |                     |            |         |                  |     |
|                |                  |     |                 |        |     |            | PII-Real      | using               | Spearman’s |         | rank correlation | co- |
parameters)toassesstheirviabilityforon-device efficient (ρ) and Performance Consistency Score
| PIIprotection. |     |           |     |     |     |             | (PCS). |     |     |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
| As shown       |     | in Tables | 13, | 14, | and | 12, our re- |        |     |     |     |     |     |
sultsrevealasignificantperformancegapbetween 1https://www.aminer.cn/ai2000
5007

|     |     | PII-Single |     |     | PII-Multi |     | PII-Hard | PII-Distract |     |
| --- | --- | ---------- | --- | --- | --------- | --- | -------- | ------------ | --- |
BaselineModels Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F Strict-F1 Ent-F1 RougeL-F
Qwen2.5-0.5B 0.002 0.0029 0.002 0.0013 0.0042 0.0013 0.0034 0.0042 0.0034 0.009 0.0207 0.009
Qwen2.5-1.5B 0.1846 0.2069 0.1865 0.1057 0.1794 0.1071 0.1474 0.1976 0.1502 0.0728 0.1549 0.0733
Qwen2.5-3B 0.5929 0.6289 0.5962 0.6189 0.7067 0.6212 0.5202 0.5921 0.5237 0.3717 0.6293 0.3731
|     |     | Table12: | PerformanceofbaselinemodelsunderthePIIDetectiontask. |     |     |     |     |     |     |
| --- | --- | -------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Qwen2.5-0.5B Qwen2.5-1.5B Qwen2.5-3B Task Spearman’sρ P-value
| Method | F1  | RougeL-F | F1 RougeL-F | F1  | RougeL-F |              |     |        |        |
| ------ | --- | -------- | ----------- | --- | -------- | ------------ | --- | ------ | ------ |
|        |     |          |             |     |          | PIIDetection |     | 0.9880 | <0.001 |
BasicMethod
|                  |        |               |        |        |        | Query-RelatedDetection |     | 0.9982 | <0.001 |
| ---------------- | ------ | ------------- | ------ | ------ | ------ | ---------------------- | --- | ------ | ------ |
| Naive            | 0.0041 | 0.0041 0.2131 | 0.2185 | 0.1691 | 0.1699 |                        |     |        |        |
| AdvancedMethod   |        |               |        |        |        | Query-UnrelatedMasking |     | 0.9982 | <0.001 |
| Self-CoT         | 0.009  | 0.0095 0.2002 | 0.2051 | 0.2884 | 0.2909 |                        |     |        |        |
| Auto-CoT(3-shot) | 0.0258 | 0.0268 0.2383 | 0.2466 | 0.381  | 0.384  |                        |     |        |        |
Self-Consistency 0.0018 0.0018 0.1057 0.1088 0.2694 0.2774 Table 15: Spearman’s rank correlation between PII-
| PS-CoT | 0.0088 | 0.009 0.1887 | 0.1959 | 0.293 | 0.2956 |     |     |     |     |
| ------ | ------ | ------------ | ------ | ----- | ------ | --- | --- | --- | --- |
SingleandPII-Realdatasetsacrossevaluationtasks.
w/PIIDetection
| Naivew/Choice | 0.3978 | 0.3986 0.4357 | 0.4357 | 0.542 | 0.5437 |     |     |     |     |
| ------------- | ------ | ------------- | ------ | ----- | ------ | --- | --- | --- | --- |
Table 13: Performance comparison on the Query- Performance Consistency Tables 16 and 17
RelatedPIIDetectiontask(PII-singledataset). present PCS values quantifying absolute perfor-
|     |     |     |     |     |     | mancealignment. | ForPIIdetection(Table16),all |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | ---------------------------- | --- | --- |
Qwen2.5-0.5B Qwen2.5-1.5B Qwen2.5-3B modelsachievePCSvaluesexceeding0.967,with
| Method | F1  | RougeL-F | F1 RougeL-F | F1  | RougeL-F |                          |     |                     |     |
| ------ | --- | -------- | ----------- | --- | -------- | ------------------------ | --- | ------------------- | --- |
|        |     |          |             |     |          | anoverallaverageof0.980. |     | Forquery-relatedde- |     |
BasicMethodw/PIIDetection
Naive 0.0016 0.0025 0.0912 0.1018 0.3257 0.3321 tectionandmaskingtasks(Table17),PCSvalues
AdvancedMethodw/PIIDetection
consistentlyexceed0.947acrossallmodel-strategy
| Self-CoT         | 0.0016 | 0.0029 0.0846 | 0.0945 | 0.3764 | 0.3841 |               |           |              |           |
| ---------------- | ------ | ------------- | ------ | ------ | ------ | ------------- | --------- | ------------ | --------- |
|                  |        |               |        |        |        | combinations, | averaging | 0.966. These | high con- |
| Auto-CoT(3-shot) | 0.0019 | 0.0032 0.0927 | 0.1038 | 0.4247 | 0.4327 |               |           |              |           |
| Self-Consistency | 0.0016 | 0.0029 0.0907 | 0.1020 | 0.3414 | 0.3486 |               |           |              |           |
sistencyscoresconfirmthatsyntheticsingle-entity
| PS-CoT | 0.0016 | 0.0025 0.0920 | 0.1033 | 0.3765 | 0.3840 |     |     |     |     |
| ------ | ------ | ------------- | ------ | ------ | ------ | --- | --- | --- | --- |
w/PIIDetection scenariosaccuratelycapturethechallengespresent
Naivew/Choice 0.0011 0.0017 0.0722 0.0800 0.3918 0.3994 inreal-worldprivacyprotectiontasks.
| Table 14: | Performance | comparison |     | on  | the Query- |     |     |     |     |
| --------- | ----------- | ---------- | --- | --- | ---------- | --- | --- | --- | --- |
Unrelated PII Masking task (PII-single and PII-multi Model Strict-F1 Ent-F1 RougeL-F Average
datasets).
|     |     |     |     |     |     | GPT4o      | 0.979 | 0.979 0.979 | 0.979 |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | ----- |
|     |     |     |     |     |     | Claude3.5  | 0.967 | 0.978 0.970 | 0.972 |
|     |     |     |     |     |     | DeepSeekV3 | 0.978 | 0.979 0.978 | 0.978 |
PerformanceConsistencyScore PCSmeasures Llama3.1 0.978 0.984 0.978 0.980
absolute performance alignment between two Qwen2.5 0.980 0.988 0.980 0.982
|           |             |       |     |            |      | Llama3.1-SLM | 0.982 | 0.984 0.982 | 0.982 |
| --------- | ----------- | ----- | --- | ---------- | ---- | ------------ | ----- | ----------- | ----- |
| datasets. | For a given | model | and | evaluation | met- |              |       |             |       |
|           |             |       |     |            |      | Qwen2.5-SLM  | 0.986 | 0.988 0.986 | 0.987 |
ric,PCSisdefinedas:
|     |     |        |     |      |     | OverallAverage | 0.979 | 0.983 0.979 | 0.980 |
| --- | --- | ------ | --- | ---- | --- | -------------- | ----- | ----------- | ----- |
|     |     | F1     |     | F1   |     |                |       |             |       |
|     |     | single |     | real |     |                |       |             |       |
PCS = 1 | − | (21) Table16: PerformanceConsistencyScoresforPIIde-
|     |     | max(F1 |        | ,F1  | )   |     |     |     |     |
| --- | --- | ------ | ------ | ---- | --- | --- | --- | --- | --- |
|     | −   |        | single | real |     |     |     |     |     |
tectiontaskacrossdifferentmetrics.
| where F1 | represents |     | the | F1 score | on PII- |     |     |     |     |
| -------- | ---------- | --- | --- | -------- | ------- | --- | --- | --- | --- |
single
| SingledatasetandF1 |     |     | representstheF1score |     |     |     |     |     |     |
| ------------------ | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
real
onPII-Realdataset. APCSvalueof1indicatesper- F.4.3 RepresentativeExamplefromPII-Real
fectperformanceconsistency,whilelowervalues Figure 6 presents a representative instance from
| indicate | greater deviation |     | between | synthetic | and |              |                       |     |            |
| -------- | ----------------- | --- | ------- | --------- | --- | ------------ | --------------------- | --- | ---------- |
|          |                   |     |         |           |     | the PII-Real | dataset, illustrating | the | comparable |
real-worldscenarios.
|     |     |     |     |     |     | complexityandstructuretosyntheticsamples. |     |     | This |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | ---- |
exampleisderivedfromareal-worldbiographical
| RankingConsistency |     |     | Table15presentsSpear- |     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
profile.2
| man’s ρ       | values across | all         | evaluation | tasks.       | The  |     |     |     |     |
| ------------- | ------------- | ----------- | ---------- | ------------ | ---- | --- | --- | --- | --- |
| exceptionally | high          | correlation |            | coefficients | (ρ > |     |     |     |     |
0.988, p < 0.001) demonstrate that model rank- F.5 AdditionalResults
ingsremainconsistentbetweensyntheticandreal-
Table21comparesdifferentpromptingstrategies
| worlddatasets,indicatingPII-Benchreliablypre- |     |     |     |     |     | onPII-multidataset. |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
dictsrelativemodelperformanceinauthenticpri-
| vacyscenarios. |     |     |     |     |     | 2Originalsource:https://kimiyoung.github.io |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
5008

Model Task Naive Self-CoT Auto-CoT Self-Consistency PS-CoT Naivew/Choice Average
|     | Query-Related | 0.966 0.962 | 0.955 | 0.966 | 0.952 | 0.976 | 0.963 |
| --- | ------------- | ----------- | ----- | ----- | ----- | ----- | ----- |
GPT4o
|     | Masking       | 0.969 0.972 | 0.973 | 0.970 | 0.976 | 0.979 | 0.973 |
| --- | ------------- | ----------- | ----- | ----- | ----- | ----- | ----- |
|     | Query-Related | 0.972 0.969 | 0.967 | 0.960 | 0.966 | 0.972 | 0.968 |
Llama3.1
|     | Masking       | 0.976 0.977 | 0.973 | 0.970 | 0.966 | 0.967 | 0.972 |
| --- | ------------- | ----------- | ----- | ----- | ----- | ----- | ----- |
|     | Query-Related | 0.976 0.965 | 0.974 | 0.969 | 0.972 | 0.980 | 0.973 |
Qwen2.5
|     | Masking       | 0.971 0.972 | 0.972 | 0.967 | 0.969 | 0.973 | 0.971 |
| --- | ------------- | ----------- | ----- | ----- | ----- | ----- | ----- |
|     | Query-Related | 0.954 0.956 | 0.953 | 0.948 | 0.951 | 0.967 | 0.955 |
Llama3.1-SLM
|     | Masking       | 0.963 0.969 | 0.968 | 0.965 | 0.964 | 0.962 | 0.965 |
| --- | ------------- | ----------- | ----- | ----- | ----- | ----- | ----- |
|     | Query-Related | 0.960 0.957 | 0.951 | 0.947 | 0.962 | 0.973 | 0.958 |
Qwen2.5-SLM
|                | Masking | 0.968 0.963 | 0.961 | 0.957 | 0.969 | 0.972 | 0.965 |
| -------------- | ------- | ----------- | ----- | ----- | ----- | ----- | ----- |
| OverallAverage |         | 0.968 0.966 | 0.965 | 0.962 | 0.965 | 0.972 | 0.966 |
Table17: PerformanceConsistencyScoresforquery-relateddetectionandmaskingtasksbypromptingstrategy.
UserDescription:
“Hi,I’mZhilinYang.IamworkingonastartupandIamtheCEOofMoonshotAI.In2019,IobtainedmyPhDdegreefrom
CarnegieMellonUniversity,advisedbyRuslanSalakhutdinovandWilliamW.Cohen.Priortothat,in2015,Ireceivedmy
bachelor’sdegreefromTsinghuaUniversity,advisedbyJieTang. IworkedatMetaAIwithJasonWeston,andGoogle
BrainwithQuocV.Le.”
Query:
“Inmycurrentrole,we’reearlyandjugglinghiringwithfirstproductbets.Whatminimalweeklyrhythmanddecisionrules
keepusfastwithoutcreatingchaos?”
PIIEntities(Total:16):
• PER:ZhilinYang,RuslanSalakhutdinov,WilliamW.Cohen,JieTang,JasonWeston,QuocV.Le
• DEM:CEO,PhDdegree,bachelor’sdegree
• CODE:(none)
• ORG:MoonshotAI,CarnegieMellonUniversity,TsinghuaUniversity,MetaAI,GoogleBrain
• DATETIME:2019,2015
• LOC:(none)
• QUANTITY:(none)
Query-RelatedPII:CEO,MoonshotAI
Figure 6: Example from PII-Real dataset showing a real-world biographical profile with comprehensive PII
annotations. Thequeryspecificallytargetscareer-relatedinformation,requiringidentificationofoccupationand
organizationalaffiliationwhileprotectingotherpersonaldetails.
5009

Model Strict-F1 Ent-F1 RougeL-F • Subject Association: Entities are linked to
theircorrespondingsubjectsusingalphabeti-
API-basedLargeLanguageModel
calidentifiers(e.g.,A,B)tomaintainrelation-
| GPT4o |     | 0.912 | 0.934 |     | 0.914 |     |     |     |     |     |     |     |
| ----- | --- | ----- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
shipclarityinmulti-subjectscenarios.
| Claude3.5  |     | 0.887 | 0.911 |     | 0.889 |     |                     |     |     |                           |     |     |
| ---------- | --- | ----- | ----- | --- | ----- | --- | ------------------- | --- | --- | ------------------------- | --- | --- |
| DeepSeekV3 |     | 0.923 | 0.941 |     | 0.925 |     |                     |     |     |                           |     |     |
|            |     |       |       |     |       |     | • SpanVerification: |     |     | Theinterfacedisplaysstart |     |     |
Open-sourceLargeLanguageModel
andendpositionsforeachentityspan,ensur-
| Llama3.1 |     | 0.901 | 0.928 |     | 0.903 |     | ingpreciseboundarydetection.           |     |     |     |     |     |
| -------- | --- | ----- | ----- | --- | ----- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
| Qwen2.5  |     | 0.884 | 0.919 |     | 0.887 |     |                                        |     |     |     |     |     |
|          |     |       |       |     |       |     | G.2 Query-RelatedPIIDetectionInterface |     |     |     |     |     |
Open-sourceSmallLanguageModel
Llama3.1-SLM 0.762 0.813 0.766 Figure8illustratestheinterfaceforquery-related
|             |     |       |       |     |       |     | PII detection, |     | which | builds | upon the | recognition |
| ----------- | --- | ----- | ----- | --- | ----- | --- | -------------- | --- | ----- | ------ | -------- | ----------- |
| Qwen2.5-SLM |     | 0.798 | 0.856 |     | 0.803 |     |                |     |       |        |          |             |
resultstoassesscontextualrelevance:
Table18: PerformanceofbaselinemodelsonPIIdetec-
tiontask(PII-Realdataset). • Query Context: The interface presents both
theuserdescriptionandtheassociatedquery,
providingcompletecontextforrelevanceas-
F.6 PromptDetails
sessment.
| This section                        | presents     |     | the prompts | used          | through- |       |                    |     |     |                            |     |     |
| ----------------------------------- | ------------ | --- | ----------- | ------------- | -------- | ----- | ------------------ | --- | --- | -------------------------- | --- | --- |
| out our                             | experiments. |     | For the     | PII detection |          | task, |                    |     |     |                            |     |     |
|                                     |              |     |             |               |          |       | • EntitySelection: |     |     | AnnotatorsidentifyPIIenti- |     |     |
| weemploythetemplateshowninFigure13. |              |     |             |               |          | For   |                    |     |     |                            |     |     |
tiescrucialforaddressingthequery,withthe
| query-related | PII      | detection, | we          | design | and    | eval- |           |     |              |     |                |          |
| ------------- | -------- | ---------- | ----------- | ------ | ------ | ----- | --------- | --- | ------------ | --- | -------------- | -------- |
|               |          |            |             |        |        |       | interface |     | highlighting |     | pre-identified | entities |
| uate six      | distinct | prompting  | strategies. |        | Figure | 14    |           |     |              |     |                |          |
fromtherecognitionphase.
| displays  | the Naive | prompts, | Figure   |        | 15 presents |         |           |               |     |     |              |        |
| --------- | --------- | -------- | -------- | ------ | ----------- | ------- | --------- | ------------- | --- | --- | ------------ | ------ |
| the Naive | w/ Choice |          | prompts, | Figure |             | 16 fea- |           |               |     |     |              |        |
|           |           |          |          |        |             |         | • Subject | Verification: |     |     | For selected | query- |
turestheSelf-CoTprompts,Figure17revealsthe
relatedentities,annotatorsmustverifythesub-
Auto-CoT prompts, Figure 18 exhibits the Self- jectassociationstoensureconsistencyacross
|             | prompts,and |     | Figure | 19  | displays | the |        |     |     |     |     |     |
| ----------- | ----------- | --- | ------ | --- | -------- | --- | ------ | --- | --- | --- | --- | --- |
| Consistency |             |     |        |     |          |     | tasks. |     |     |     |     |     |
PS-CoTprompts.
|     |     |     |     |     |     |     | • RelevanceValidation: |     |     |     | Theinterfaceincludes |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | -------------------- | --- |
G PIIAnnotationSystem
areviewmechanismtoconfirmthatselected
Wedevelopedaspecializedweb-basedannotation entitiesarebothnecessaryandsufficientfor
queryresolution.
platformtofacilitatethesystematicevaluationof
PIIdetectionandquery-relateddetectioncapabil-
ities. Theplatformimplementsatwo-stageanno- G.3 Query-UnrelatedPIIMasking
Visualization
tationprocess,ensuringcomprehensivecoverage
| of both | fundamental | PII | entity | identification |     | and |             |     |               |     |            |         |
| ------- | ----------- | --- | ------ | -------------- | --- | --- | ----------- | --- | ------------- | --- | ---------- | ------- |
|         |             |     |        |                |     |     | To validate | the | effectiveness |     | of privacy | protec- |
contextualrelevanceassessment.
|     |     |     |     |     |     |     | tion while | maintaining |     | query | relevance, | we im- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----- | ---------- | ------ |
plementedamaskingvisualizationinterface(Fig-
G.1 PIIDetectionInterface
ure9):
| As shown | in Figure | 7,  | the PII | detection | interface |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
enables annotators to identify and categorize PII • OriginalContext: Displaysthecompleteuser
| entitieswithinuserdescriptions. |     |     |     | Theinterfacepro- |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
descriptionwithallPIIentitieshighlighted.
videsthefollowingkeyfunctionalities:
|          |            |            |            |          |           |     | • Masked      | View: |     | Shows     | the description    | with     |
| -------- | ---------- | ---------- | ---------- | -------- | --------- | --- | ------------- | ----- | --- | --------- | ------------------ | -------- |
| • Entity | Detection: |            | Annotators | can      | highlight |     |               |       |     |           |                    |          |
|          |            |            |            |          |           |     | non-relevant  |       | PII | entities  | replaced           | by their |
| text     | spans      | containing | PII        | entities | directly  | in  |               |       |     |           |                    |          |
|          |            |            |            |          |           |     | corresponding |       |     | type tags | (e.g., <Nickname>, |          |
theuserdescription.
<PhoneNumber>).
| • TypeClassification: |     |     | Eachidentifiedentityis |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assigned a specific PII type (e.g., PER for • Key Information Display: Preserves query-
personnames,ORGfororganizations,LOC relatedPIIentitieswhilemaintainingreadabil-
| forlocations). |     |     |     |     |     |     | ityandsemanticcoherence. |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
5010

GPT4o Llama3.1 Qwen2.5 Llama3.1-SLM Qwen2.5-SLM
Method
F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F
BasicMethod
Naive 0.652 0.654 0.648 0.651 0.635 0.638 0.346 0.348 0.427 0.429
AdvancedMethod
Self-CoT 0.738 0.741 0.712 0.714 0.694 0.697 0.408 0.411 0.418 0.421
Auto-CoT 0.691 0.693 0.724 0.728 0.729 0.732 0.451 0.454 0.389 0.392
Self-Consistency 0.745 0.747 0.656 0.659 0.671 0.674 0.327 0.331 0.338 0.342
PS-CoT 0.683 0.685 0.673 0.676 0.689 0.691 0.368 0.372 0.468 0.471
w/ExtraInformation
Naivew/Choice 0.861 0.861 0.782 0.784 0.847 0.849 0.538 0.541 0.791 0.793
Table19: PerformancecomparisononQuery-RelatedPIIDetectiontask(PII-Realdataset).
GPT4o Llama3.1 Qwen2.5 Llama3.1-SLM Qwen2.5-SLM
Method
F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F
BasicMethod
Naive 0.743 0.745 0.738 0.742 0.721 0.725 0.436 0.441 0.558 0.593
AdvancedMethod
Self-CoT 0.782 0.785 0.768 0.771 0.751 0.754 0.547 0.551 0.561 0.596
Auto-CoT 0.771 0.773 0.781 0.784 0.782 0.785 0.589 0.593 0.562 0.597
Self-Consistency 0.794 0.796 0.732 0.736 0.734 0.738 0.508 0.513 0.512 0.548
PS-CoT 0.758 0.761 0.745 0.748 0.753 0.756 0.498 0.503 0.578 0.614
w/ExtraInformation
Naivew/Choice 0.838 0.841 0.796 0.799 0.812 0.815 0.478 0.483 0.689 0.725
Table20: PerformancecomparisononQuery-UnrelatedPIIMaskingtask(PII-Realdataset).
GPT4o Llama3.1 Qwen2.5 Llama3.1-SLM Qwen2.5-SLM
Method
F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F
BasicMethod
Naive 0.600 0.602 0.611 0.614 0.596 0.603 0.240 0.333 0.405 0.413
AdvancedMethod
Self-CoT 0.675 0.681 0.638 0.643 0.626 0.632 0.354 0.362 0.392 0.397
Auto-CoT(3-shot) 0.629 0.640 0.650 0.662 0.657 0.665 0.393 0.402 0.391 0.394
Self-Consistency 0.685 0.692 0.602 0.605 0.614 0.620 0.263 0.269 0.288 0.293
PS-CoT 0.618 0.620 0.624 0.631 0.636 0.643 0.291 0.300 0.431 0.436
w/ExtraInformation
Naivew/Choice 0.846 0.846 0.775 0.775 0.804 0.804 0.387 0.388 0.743 0.743
Table21: PerformancecomparisonontheQuery-RelatedPIIDetectiontask(PII-multidataset).
5011

| G.4 AnnotationGuidelines |     |     |     |     |     |     | Model |     | Single | Multi | Hard | Distract |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | ---- | -------- | --- |
Toensureannotationconsistencyandquality,we GPT-5 0.871 0.884 0.840 0.832
|     |     |     |     |     |     |     | DeepSeek-V3.2 |     | 0.856 | 0.838 | 0.779 | 0.719 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ----- | ----- | ----- | --- |
establishedcomprehensiveguidelinesforeachtask.
|     |     |     |     |     |     |     | DeepSeek-R1 |     | 0.876 | 0.879 | 0.835 | 0.826 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ----- | ----- | ----- | --- |
Table24summarizesthecoreannotationinstruc- Qwen3-30B-Instruct 0.793 0.781 0.745 0.510
tionsprovidedtoannotatorsacrossthethreetasks. Qwen3-30B-Thinking 0.805 0.798 0.781 0.625
|     |     |     |     |     |     |     | Qwen3-8B(No-Think) |     | 0.771 | 0.684 | 0.667 | 0.485 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | ----- | ----- | ----- | --- |
|     |     |     |     |     |     |     | Qwen3-8B(Think)    |     | 0.740 | 0.684 | 0.679 | 0.571 |     |
G.5 QualityControlandInter-Annotator
Agreement
|     |     |     |     |     |     |     | Table23: | Strict-F1onthePIIDetectiontaskusingthe |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------------------------------- | --- | --- | --- | --- | --- |
To maintain high annotation quality, we imple- Naive (zero-shot) prompt, across the four PII-Bench
mentedarigorousqualitycontrolprotocol. Each subsets. Withineachfamily,thenon-reasoningvariant
sample was independently annotated by multiple precedes its reasoning counterpart; best per subset in
bold.
| annotators, | with   | disagreements |         | resolved |         | through |     |     |     |     |     |     |     |
| ----------- | ------ | ------------- | ------- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| majority    | voting | or expert     | review. |          | Regular | review  |     |     |     |     |     |     |     |
sessions were conducted to discuss challenging (1)Reasoninghelpsmostincomplexdetection
| cases and | update                             | guidelines |     | based | on  | annotator |           |        |        |            |     |           |     |
| --------- | ---------------------------------- | ---------- | --- | ----- | --- | --------- | --------- | ------ | ------ | ---------- | --- | --------- | --- |
|           |                                    |            |     |       |     |           | settings. | On the | easier | PII-Single | and | PII-Multi |     |
| feedback. | Forqualityassurance,werandomlysam- |            |     |       |     |           |           |        |        |            |     |           |     |
subsets,basicdetectionisclosetosaturationacross
pled10%oftheannotationsforexpertreview. allsevensystems,soreasoningcapabilityprovides
|                |     |     |              |     |     |          | littleadditionalbenefit. |              |     | Thepicturechangesonthe |       |        |     |
| -------------- | --- | --- | ------------ | --- | --- | -------- | ------------------------ | ------------ | --- | ---------------------- | ----- | ------ | --- |
| AnnotationTask |     |     | Agreement(%) |     |     | Fleiss’κ |                          |              |     |                        |       |        |     |
|                |     |     |              |     |     |          | high-entropy             | PII-Distract |     | subset,                | where | Qwen3- |     |
PIIDetection 95.1 0.912 30B-ThinkingimprovesoverQwen3-30B-Instruct
Query-RelatedDetection 91.5 0.873 by11.5Strict-F1points(0.625vs.0.510,a22.5%
|          |                                         |     |     |     |     |     | relative gain),      | with | a comparable               |     | gap | for the | 8B  |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | -------------------- | ---- | -------------------------- | --- | --- | ------- | --- |
| Table22: | Inter-annotatoragreementforPIIdetection |     |     |     |     |     |                      |      |                            |     |     |         |     |
|          |                                         |     |     |     |     |     | pair(0.571vs.0.485). |      | Thisindicatesthatreasoning |     |     |         |     |
andquery-relateddetectiontasks.
|     |     |     |     |     |     |     | becomes | beneficial | only | when | detection | itself | is  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ---- | ---- | --------- | ------ | --- |
non-trivial.
Table22presentstheinter-annotatoragreement
resultsforthetwoprimaryannotationtasks,mea- (2)Open-sourcereasoningreachesproprietary
|             |      |          |     |           |     |           | parity. | On PII-Single |     | detection, | DeepSeek-R1 |     |     |
| ----------- | ---- | -------- | --- | --------- | --- | --------- | ------- | ------------- | --- | ---------- | ----------- | --- | --- |
| sured using | both | observed |     | agreement |     | rates and |         |               |     |            |             |     |     |
(0.876)slightlysurpassesGPT-5(0.871),andthe
| Fleiss’ | kappa. | We obtain |     | kappa | values | of 0.912 |     |     |     |     |     |     |     |
| ------- | ------ | --------- | --- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
twomodelstrackeachotherwithinaboutoneF1
forPIIdetectionand0.873forquery-relateddetec-
pointoneveryotherPIIDetectionsubset.
tionacrossallannotators.
(3)Thequery-awaretasksremainconsiderably
H EvaluationofReasoning-Capable harder. No evaluated model exceeds 0.77 F1 on
| Models |     |     |     |     |     |     | Query-RelatedPIIDetection,whichstilltrailsthe |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
0.951humanbaselinebymorethan18F1points.
| We evaluate |     | seven | recent | LLMs | that | pair rea- |     |     |     |     |     |     |     |
| ----------- | --- | ----- | ------ | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
ReasoningoffersnoconsistentliftonPII-Singlefor
| soning          | and non-reasoning |       |        | variants: | the          | propri- |             |                                 |     |     |     |     |     |
| --------------- | ----------------- | ----- | ------ | --------- | ------------ | ------- | ----------- | ------------------------------- | --- | --- | --- | --- | --- |
|                 |                   |       |        |           |              |         | thesetasks: | thenon-reasoningDeepSeek-V3.2is |     |     |     |     |     |
| etary reasoning |                   | model | GPT-5, |           | the DeepSeek |         |             |                                 |     |     |     |     |     |
marginallyaheadofDeepSeek-R1(0.765vs.0.745
| pair (non-reasoning |     |     | DeepSeek-V3.2 |       | and    | reason- |                   |     |       |     |          |           |     |
| ------------------- | --- | --- | ------------- | ----- | ------ | ------- | ----------------- | --- | ----- | --- | -------- | --------- | --- |
|                     |     |     |               |       |        |         | on Query-Related, |     | 0.852 | vs. | 0.850 on | Masking). |     |
| ing DeepSeek-R1),   |     |     | and two       | Qwen3 | scales | with    |                   |     |       |     |          |           |     |
On-devicevariantsaddasecondgap,withthebest
| matched | Instruct | and | Thinking | variants |     | (Qwen3- |     |     |     |     |     |     |     |
| ------- | -------- | --- | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Qwen3-8BtrailingDeepSeek-R1by14.5F1points
| 30B-Instruct,  |     | Qwen3-30B-Thinking, |     |           |     | Qwen3- |                              |           |            |     |                 |        |     |
| -------------- | --- | ------------------- | --- | --------- | --- | ------ | ---------------------------- | --------- | ---------- | --- | --------------- | ------ | --- |
|                |     |                     |     |           |     |        | onQuery-RelatedPIIDetection. |           |            |     | Relevancejudge- |        |     |
| 8B (No-Think), |     | Qwen3-8B            |     | (Think)). |     | Open-  |                              |           |            |     |                 |        |     |
|                |     |                     |     |           |     |        | ment and                     | on-device | deployment |     | thus            | emerge | as  |
sourcemodelsareservedlocallyviavLLM;API-
thetwoprincipalchallengesforfuturequery-aware
| based models |     | are accessed |     | through | their | official |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
privacysystems.
| endpoints.                     | Alldecodingsettingsfollowthemain |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| experiments(temperature0,top-k |                                  |     |     |     | 1). |     |     |     |     |     |     |     |     |
Tables23,25and26reportStrict-F1onPIIDe-
tectionacrossallfoursubsets,andF1/RougeL-F
onPII-SingleforQuery-RelatedPIIDetectionand
Query-UnrelatedPIIMaskingundersixprompting
| strategies. | We  | summarise |     | the results | along | three |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
axes.
5012

Task AnnotationGuidelines
PIIDetection •VerifywhetherallPIIentitiesintheuserdescriptionarecorrectlyidentified.
•ClicktheCorrectbuttonifallentitiesareproperlydetected.
•AnnotatemissingPIIentitiesbyselectingtextspansandassigningtype,tag,and
subjectidentifiers.
•Assignthenextavailableletter(A,B,C)forentitiesbelongingtonewsubject
groups.
•Selectminimalspanscontainingonlytheessentialtextrepresentingeachentity.
Query-RelatedPIIDetection •IdentifyPIIentitiescrucialforaddressingthequeryfromtheprovidedoptions.
•Verifyorcorrectthesubjectassociation(A,B,C,etc.)foreachselectedentity.
•Ensurethatselectedentitiesarebothnecessaryandsufficientforqueryresolution.
•Usethereviewmechanismtovalidateyourselectionbeforesubmission.
Query-UnrelatedPIIMasking •Reviewthemaskeduserdescriptionwherequery-unrelatedPIIentitiesarereplaced
withtypetags.
•Verifythatquery-relatedentitiesarepreservedintheiroriginalform.
•Confirmthatmaskedentitiesarereplacedwithappropriatetags(e.g.,<Nickname>,
<PhoneNumber>).
•Evaluatewhetherthemaskedtextmaintainssemanticcoherenceandreadability.
•Assessthebalancebetweenprivacyprotectionandqueryutilitypreservation.
Table24:ComprehensiveannotationguidelinesforthethreetasksinPII-Bench.Eachtaskfollowsspecificprotocols
toensureconsistencyandqualityacrossannotators.
GPT-5 DeepSeek-V3.2 DeepSeek-R1 Qwen3-30B-Ins. Qwen3-30B-Thk. Qwen3-8B(NT) Qwen3-8B(T)
Method
F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F
Naive 0.700 0.704 0.735 0.737 0.715 0.718 0.545 0.550 0.612 0.617 0.362 0.363 0.494 0.498
Self-CoT 0.733 0.740 0.765 0.767 0.745 0.749 0.632 0.638 0.698 0.703 0.524 0.525 0.534 0.537
Auto-CoT 0.697 0.710 0.746 0.754 0.710 0.718 0.692 0.696 0.741 0.746 0.538 0.540 0.600 0.608
Self-Consistency 0.722 0.725 0.741 0.745 0.735 0.738 0.631 0.635 0.689 0.693 0.501 0.502 0.529 0.532
PS-CoT 0.725 0.729 0.754 0.756 0.739 0.742 0.606 0.612 0.675 0.680 0.443 0.444 0.552 0.554
Naivew/Choice 0.872 0.872 0.857 0.857 0.879 0.879 0.816 0.816 0.845 0.845 0.638 0.638 0.643 0.643
Table25: Query-RelatedPIIDetectiononPII-Singleunderthesixpromptingstrategiesdefinedin§F.6. Withineach
family,thenon-reasoningvariantprecedesitsreasoningcounterpart;bestF1permodelacrossthefivenon-oracle
strategiesinbold. “Naivew/Choice”providesthegoldPIIcandidatesetandservesasanoracleupperbound.
GPT-5 DeepSeek-V3.2 DeepSeek-R1 Qwen3-30B-Ins. Qwen3-30B-Thk. Qwen3-8B(NT) Qwen3-8B(T)
Method
F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F F1 RougeL-F
Naive 0.832 0.835 0.831 0.833 0.841 0.844 0.683 0.687 0.765 0.770 0.517 0.522 0.628 0.633
Self-CoT 0.840 0.843 0.852 0.854 0.850 0.853 0.794 0.797 0.845 0.849 0.641 0.646 0.705 0.710
Auto-CoT 0.836 0.839 0.850 0.852 0.847 0.850 0.815 0.818 0.852 0.856 0.656 0.661 0.720 0.725
Self-Consistency 0.824 0.827 0.831 0.833 0.835 0.838 0.768 0.771 0.825 0.829 0.621 0.626 0.692 0.697
PS-CoT 0.834 0.836 0.846 0.848 0.844 0.847 0.772 0.775 0.831 0.835 0.593 0.597 0.665 0.670
Naivew/Choice 0.854 0.856 0.861 0.862 0.862 0.864 0.805 0.808 0.841 0.845 0.607 0.613 0.698 0.703
Table26:Query-UnrelatedPIIMaskingonPII-Singleunderthesixpromptingstrategiesdefinedin§F.6.Withineach
family,thenon-reasoningvariantprecedesitsreasoningcounterpart;bestF1permodelacrossthefivenon-oracle
strategiesinbold. “Naivew/Choice”providesthegoldPIIcandidatesetandservesasanoracleupperbound.
5013

PPIII DI etection Task
IInnppuutt HHiigghhlliigghhtteedd
EEnntttt eeeexrxr(( t UtU:: ssBBe aearrc ckkggrrDDoo eeususncncdrrdii ppttiioonn)) DDeetteecctteedd EEnnttiittiieess
LLaannccee iiss aa ddeeddiiccaatteedd rreesseeaarrcchheerr aatt tthhee GGlloobbaall HHeeaalltthh RReesseeaarrcchh CCeenntteerr,, llooccaatteedd oonn tthhee 88tthh FFlloooorr,, NNoo.. 220000,, GGeeoorrggee SSttrreeeett,, SSyyddnneeyy.. LLaannccee PPEERR iiss aa ddeeddiiccaatteedd rreesseeaarrcchheerr aatt tthhee GGlloobbaall HHeeaalltthh RReesseeaarrcchh CCeenntteerr OORRGG,, llooccaatteedd oonn tthhee
KKnnoowwnn ffoorr hhiiss mmeettiiccuulloouuss wwoorrkk eetthhiicc,, LLaannccee oo  eenn ffiinnddss hhiimmsseellff eennggrroosssseedd iinn hhiiss pprroojjeeccttss wweellll ppaasstt tthhee uussuuaall wwoorrkkiinngg hhoouurrss.. DDeessppiittee 88tthh FFlloooorr,, NNoo.. 220000,, GGeeoorrggee SSttrreeeett,, SSyyddnneeyy LLOOCC.. KKnnoowwnn ffoorr hhiiss mmeettiiccuulloouuss wwoorrkk eetthhiicc,, LLaannccee PPEERR oo  eenn ffiinnddss hhiimmsseellff eennggrroosssseedd iinn
hhiiss pprrooffeessssiioonnaall ssuucccceessss,, LLaannccee mmaannaaggeess aa ppeerrssoonnaall cchhaalllleennggee——hhyyppeerrtteennssiioonn,, wwhhiicchh hhee ddiilliiggeennttllyy mmoonniittoorrss.. EEvveerryy ddaayy aatt pprreecciisseellyy hhiiss pprroojjeeccttss wweellll ppaasstt tthhee uussuuaall wwoorrkkiinngg hhoouurrss.. DDeessppiittee hhiiss pprrooffeessssiioonnaall ssuucccceessss,, LLaannccee PPEERR mmaannaaggeess aa ppeerrssoonnaall cchhaalllleennggee——
33::1144 PPMM,, hhee ttaakkeess aa mmoommeenntt ttoo cchheecckk hhiiss bblloooodd pprreessssuurree,, eennssuurriinngg hhee ssttaayyss oonn ttoopp ooff hhiiss hheeaalltthh.. OOuuttssiiddee ooff wwoorrkk,, LLaannccee iiss kknnoowwnn ffoorr hhyyppeerrtteennssiioonn DDEEMM,, wwhhiicchh hhee ddiilliiggeennttllyy mmoonniittoorrss.. EEvveerryy ddaayy aatt pprreecciisseellyy 33::1144 PPMM DDAATTEETTIIMMEE,, hhee ttaakkeess aa mmoommeenntt ttoo cchheecckk hhiiss bblloooodd
hhiiss aapppprrooaacchhaabbllee nnaattuurree aanndd iiss aallwwaayyss jjuusstt aa pphhoonnee ccaallll aawwaayy aatt 1144559933774422114477,, rreeaaddyy ttoo lleenndd aann eeaarr oorr sshhaarree hhiiss iinnssiigghhttss oonn gglloobbaall pprreessssuurree,, eennssuurriinngg hhee ssttaayyss oonn ttoopp ooff hhiiss hheeaalltthh.. OOuuttssiiddee ooff wwoorrkk,, LLaannccee PPEERR iiss kknnoowwnn ffoorr hhiiss aapppprrooaacchhaabbllee nnaattuurree aanndd iiss aallwwaayyss jjuusstt aa
hheeaalltthh iissssuueess.. pphhoonnee ccaallll aawwaayy aatt 1144559933774422114477 CCOODDEE,, rreeaaddyy ttoo lleenndd aann eeaarr oorr sshhaarree hhiiss iinnssiigghhttss oonn gglloobbaall hheeaalltthh iissssuueess..
DDeetteecctteedd PPIIII EEnnttiittiieess
EEnnttiittyy TTyyppee TTaagg SSttaarrtt EEnnddSSuubbjjeecctt
00 LLaannccee PPEERR NNiicckknnaammee 00 55AA
11 GGlloobbaall HHeeaalltthh RReesseeaarrcchh CCeenntteerr OORRGG NNoonn--GGoovveerrnnmmeennttaall OOrrggaanniizzaattiioonn NNaammee 3399 6688AA
22 88tthh FFlloooorr,, NNoo.. 220000,, GGeeoorrggee SSttrreeeett,, SSyyddnneeyy LLOOCC WWoorrkk oorr HHoommee DDeettaaiilleedd AAddddrreessss 8855 112266AA
33 LLaannccee PPEERR NNiicckknnaammee 116655 117700AA
44 LLaannccee PPEERR NNiicckknnaammee 228866 229911AA
55 hhyyppeerrtteennssiioonn DDEEMM HHeeaalltthh SSttaattuuss 332211 333333AA
66 33::1144 PPMM DDAATTEETTIIMMEE SSppeecciiffiicc TTiimmee 338888 339955AA
77 LLaannccee PPEERR NNiicckknnaammee 550011 550066AA
88 1144559933774422114477 CCOODDEE PPhhoonnee NNuummbbeerrss 558844 559955AA
🎯🎯 TTaasskk DDeeffiinniittiioonn
🔍🔍 PPlleeaassee cchheecckk iiff aallll PPIIII eennttiittiieess iinn tthhee uusseerr ddeessccrriippttiioonn aarree ccoorrrreeccttllyy iiddeennttiiffiieedd..
✅✅ IIff ccoorrrreecctt,, cclliicckk tthhee ✓✓ CCoorrrreecctt bbuuttttoonn.. 📝📝 OOtthheerrwwiissee,, aannnnoottaattee aannyy mmiissssiinngg PPIIII eennttiittiieess..
✓✓ CCoorrrreecctt ✗✗IInnccoorrrreecctt
HHuummaann AAnnnnoottaattiioonn
✨✨ PPlleeaassee aadddd aannyy mmiissssiinngg PPIIII eennttiittiieess.. FFoorr eeaacchh eennttiittyy,, sseelleecctt iittss ttyyppee,, ttaagg,, aanndd ssuubbjjeecctt ggrroouupp.. IIff tthhee eennttiittyy bbeelloonnggss ttoo aa nneeww ssuubbjjeecctt ggrroouupp,, sseelleecctt tthhee nneexxtt aavvaaiillaabbllee lleetttteerr..
EEnnttiittyy ttyyppee:: SSuubbjjeecctt::
PPEERR AA
EEnnttiittyy ttaagg:: AAdddd nneeww eennttiittyy::
NNaammee
Figure7: WebDemoforthePIIDetectionTask
Query-Related PII Detection Task
UUsseerr DDeessccrriippttiioonn
HHeelllloo,, II''mm lloonnggjjiiee PPEERR,, aa 6677kkgg DDEEMM aaddvvooccaattee ffoorr gglloobbaall hhaarrmmoonnyy wwoorrkkiinngg wwiitthh tthhee WWoorrlldd PPeeaaccee OOrrggaanniizzaattiioonn OORRGG.. II oo  eenn ffiinndd mmyysseellff rreefflleeccttiinngg oonn lliiffee''ss jjoouurrnneeyy wwhhiillee eennjjooyyiinngg tthhee bbrreeaatthhttaakkiinngg vviieewwss ffrroomm TTaabbllee MMoouunnttaaiinn iinn CCaappee TToowwnn LLOOCC.. MMyy eevveenniinnggss aarree uussuuaallllyy
ssppeenntt aatt 88::4400 PPMM DDAATTEETTIIMMEE,, ccoonntteemmppllaattiinngg tthhee 5500 yyeeaarrss DDAATTEETTIIMMEE ooff pprrooggrreessss iinn ppeeaaccee iinniittiiaattiivveess.. YYoouu ccaann rreeaacchh mmee aatt xxiiaaqqiiuu@@eexxaammppllee..nneett CCOODDEE oorr ccaallll mmee aatt 1188118800998899441111 CCOODDEE.. MMyy ccrreeddiitt ssccoorree iiss 7766..55//110000 QQUUAANNTTIITTYY,, aanndd II ffrreeqquueennttllyy ccoollllaabboorraattee wwiitthh
SSyyddnneeyy PPrriinnccee HHoossppiittaall OORRGG oonn hheeaalltthh--rreellaatteedd pprroojjeeccttss.. MMyy ddaauugghhtteerr,, ddeennggnnaa PPEERR,, iiss aa ddiissttiinngguuiisshheedd DDooccttoorr ooff CClliinniiccaall MMeeddiicciinnee DDEEMM wwhhoo hhaass ddeeddiiccaatteedd 2233 yyeeaarrss DDAATTEETTIIMMEE ttoo tthhee TTrraannssnnaattiioonnaall HHeeaalltthh AAssssoocciiaattiioonn OORRGG iinn tthhee UUnniitteedd KKiinnggddoomm LLOOCC.. SShhee rreessiiddeess
aatt 55tthh FFlloooorr,, NNoo.. 6655,, LLaabboorr WWeesstt RRooaadd,, TTiiaannxxiinn DDiissttrriicctt,, CChhaannggsshhaa LLOOCC,, aanndd iiss ccuurrrreennttllyy mmaannaaggiinngg aa llooaann ooff €€227744330044..3333 QQUUAANNTTIITTYY.. HHeerr eexxppeerrttiissee iiss ffuurrtthheerr hhoonneedd aatt MMoossccooww FFiirrsstt HHoossppiittaall OORRGG,, aanndd sshhee ccoollllaabboorraatteess wwiitthh CCaassiioo OORRGG oonn hheeaalltthh tteecchhnnoollooggyy pprroojjeeccttss.. SShhee
oo  eenn vviissiittss KKrriisshhnnaa FFoorrtt LLOOCC ttoo uunnwwiinndd aanndd ggaatthheerr iinnssppiirraattiioonn ffoorr hheerr wwoorrkk..
SScceennee:: TTeecchhnnoollooggiiccaall IInnnnoovvaattiioonnss iinn PPeeaacceekkeeeeppiinngg
QQuueerryy TTeexxtt:: ::
IInn wwhhaatt wwaayyss ccaann mmyy eexxtteennssiivvee eexxppeerriieennccee iinn ffoosstteerriinngg gglloobbaall hhaarrmmoonnyy,, ccoommbbiinneedd wwiitthh hheerr ccoollllaabboorraattiioonnss iinn hheeaalltthh tteecchhnnoollooggyy,,
ccoonnttrriibbuuttee ttoo iinnnnoovvaattiivvee ssoolluuttiioonnss iinn ppeeaacceekkeeeeppiinngg eeffffoorrttss?? HHooww mmiigghhtt oouurr rreessppeeccttiivvee oorrggaanniizzaattiioonnaall aaffffiilliiaattiioonnss eennhhaannccee tthhee
iinntteeggrraattiioonn ooff ccuuttttiinngg--eeddggee ttoooollss iinn tthhiiss ffiieelldd??
KKeeyy PPIIII IInnffoorrmmaattiioonn
TThhee kkeeyy PPIIII iiss:: 2233 yyeeaarrss || CCaassiioo || 7766..55//110000 || WWoorrlldd PPeeaaccee OOrrggaanniizzaattiioonn || TTrraannssnnaattiioonnaall HHeeaalltthh AAssssoocciiaattiioonn
HHuummaann AAnnnnoottaattiioonn
TTaasskk DDeeffiinniittiioonn:: SSeelleecctt tthhee mmoosstt rreellaatteedd PPIIII ttoo tthhee qquueerryy ffrroomm tthhee ffoolllloowwiinngg ooppttiioonnss..
PPlleeaassee vveerriiffyy oorr ccoorrrreecctt yyoouurr sseelleeccttiioonn bbaasseedd oonn tthhee ccoorrrreecctt aannsswweerr::
2233 yyeeaarrss CCaassiioo 7766..55//110000 WWoorrlldd PPeeaaccee OOrrgg…… TTrraannssnnaattiioonnaall HH……
TTaasskk DDeeffiinniittiioonn:: FFoorr eeaacchh sseelleecctteedd PPIIII,, pplleeaassee iiddeennttiiffyy aanndd aannnnoottaattee iittss ssuubbjjeecctt((ss))..
EEnnttiittyy:: 2233 yyeeaarrss EEnnttiittyy:: CCaassiioo
BB BB
EEnnttiittyy:: 7766..55//110000 EEnnttiittyy:: WWoorrlldd PPeeaaccee OOrrggaanniizzaattiioonn
AA AA
EEnnttiittyy:: TTrraannssnnaattiioonnaall HHeeaalltthh AAssssoocciiaattiioonn
BB
RReevviieeww SSuubbmmiitt
Figure8: WebDemofortheQuery-RelatedPIIDetectionTask
5014

Query-Unrelated PII   Masking  Method
🎯🎯  AAddaappttiivvee  PPIIII  MMaasskk  MMeetthhoodd  iinntteelllliiggeennttllyy  pprrootteeccttss  uusseerr  pprriivvaaccyy  wwhhiillee  mmaaiinnttaaiinniinngg  qquueerryy  rreelleevvaannccee..
OOrriiggiinnaall  UUsseerr  DDeessccrriippttiioonn
LLaannccee PPEERR  iiss  aa  ddeeddiiccaatteedd  rreesseeaarrcchheerr  aatt  tthhee  GGlloobbaall  HHeeaalltthh  RReesseeaarrcchh  CCeenntteerr OORRGG,,  llooccaatteedd  oonn  tthhee  88tthh  FFlloooorr,,  NNoo..  220000,,  GGeeoorrggee  SSttrreeeett,,  SSyyddnneeyy LLOOCC..  KKnnoowwnn  ffoorr  hhiiss  mmeettiiccuulloouuss  wwoorrkk  eetthhiicc,,  LLaannccee PPEERR  oo  eenn  ffiinnddss  hhiimmsseellff  eennggrroosssseedd  iinn  hhiiss  pprroojjeeccttss  wweellll  ppaasstt  tthhee  uussuuaall  wwoorrkkiinngg
hhoouurrss..  DDeessppiittee  hhiiss  pprrooffeessssiioonnaall  ssuucccceessss,,  LLaannccee PPEERR  mmaannaaggeess  aa  ppeerrssoonnaall  cchhaalllleennggee——hhyyppeerrtteennssiioonn DDEEMM,,  wwhhiicchh  hhee  ddiilliiggeennttllyy  mmoonniittoorrss..  EEvveerryy  ddaayy  aatt  pprreecciisseellyy  33::1144  PPMM DDAATTEETTIIMMEE,,  hhee  ttaakkeess  aa  mmoommeenntt  ttoo  cchheecckk  hhiiss  bblloooodd  pprreessssuurree,,  eennssuurriinngg  hhee  ssttaayyss  oonn  ttoopp  ooff  hhiiss  hheeaalltthh..
| OOuuttssiiddee  ooff  wwoorrkk,,  LLaannccee PPEERR  iiss  kknnoowwnn  ffoorr  hhiiss  aapppprrooaacchhaabbllee  nnaattuurree  aanndd  iiss  aallwwaayyss  jjuusstt  aa  pphhoonnee  ccaallll  aawwaayy  aatt  1144559933774422114477 | CCOODDEE,,  rreeaaddyy  ttoo  lleenndd  aann  eeaarr  oorr  sshhaarree  hhiiss  iinnssiigghhttss  oonn  gglloobbaall  hheeaalltthh  iissssuueess.. |     |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
QQuueerryy
| QQuueerryy  TTeexxtt:: |     | 中中⽂⽂翻翻译译:: |     |
| ---------------------- | --- | ---------- | --- |
GGiivveenn  mmyy  rroouuttiinnee  hheeaalltthh  cchheecckk  iinn  tthhee  aa  eerrnnoooonn  aanndd  mmyy  ccoommmmiittmmeenntt  ttoo  mmyy  ccuurrrreenntt  ooffffiiccee,,  hhooww  ccaann  II  eeffffiicciieennttllyy  sscchheedduullee  aa  mmeeddiiccaall   考考虑虑到到我我下下午午的的例例⾏⾏健健康康检检查查和和我我对对⽬⽬前前办办公公室室的的承承诺诺，，我我如如何何在在不不⼲⼲扰扰我我在在所所属属组组织织职职责责的的情情况况下下有有效效地地安安排排医医疗疗咨咨询询？？
ccoonnssuullttaattiioonn  wwiitthhoouutt  ddiissrruuppttiinngg  mmyy  rreessppoonnssiibbiilliittiieess  aatt  tthhee  oorrggaanniizzaattiioonn  II  aamm  ppaarrtt  ooff??
KKeeyy  PPIIII  IInnffoorrmmaattiioonn
KKeeyy  PPIIII::  88tthh  FFlloooorr,,  NNoo..  220000,,  GGeeoorrggee  SSttrreeeett,,  SSyyddnneeyy  ||  HHyyppeerrtteennssiioonn  ||  GGlloobbaall  HHeeaalltthh  RReesseeaarrcchh  CCeenntteerr  ||  33::1144  PPMM
MMaasskkeedd  UUsseerr  DDeessccrriippttiioonn
🔒🔒  NNoonn--eesssseennttiiaall  PPIIII  eennttiittiieess  aarree  mmaasskkeedd  wwiitthh  tthheeiirr  ccoorrrreessppoonnddiinngg  ttaaggss  aanndd  ✨✨  oonnllyy  qquueerryy--rreelleevvaanntt  PPIIII  iinnffoorrmmaattiioonn  iiss  pprreesseerrvveedd
<<NNiicckknnaammee>> PPEERR  iiss  aa  ddeeddiiccaatteedd  rreesseeaarrcchheerr  aatt  tthhee  GGlloobbaall  HHeeaalltthh  RReesseeaarrcchh  CCeenntteerr OORRGG,,  llooccaatteedd  oonn  tthhee  88tthh  FFlloooorr,,  NNoo..  220000,,  GGeeoorrggee  SSttrreeeett,,  SSyyddnneeyy LLOOCC..  KKnnoowwnn  ffoorr  hhiiss  mmeettiiccuulloouuss  wwoorrkk  eetthhiicc,,  <<NNiicckknnaammee>> PPEERR  oo  eenn  ffiinnddss  hhiimmsseellff  eennggrroosssseedd  iinn  hhiiss  pprroojjeeccttss  wweellll  ppaasstt  tthhee
uussuuaall  wwoorrkkiinngg  hhoouurrss..  DDeessppiittee  hhiiss  pprrooffeessssiioonnaall  ssuucccceessss,,  <<NNiicckknnaammee>> PPEERR  mmaannaaggeess  aa  ppeerrssoonnaall  cchhaalllleennggee——hhyyppeerrtteennssiioonn,,  wwhhiicchh  hhee  ddiilliiggeennttllyy  mmoonniittoorrss..  EEvveerryy  ddaayy  aatt  pprreecciisseellyy  33::1144  PPMM DDAATTEETTIIMMEE,,  hhee  ttaakkeess  aa  mmoommeenntt  ttoo  cchheecckk  hhiiss  bblloooodd  pprreessssuurree,,  eennssuurriinngg  hhee  ssttaayyss  oonn  ttoopp  ooff  hhiiss
| hheeaalltthh..  OOuuttssiiddee  ooff  wwoorrkk,,  <<NNiicckknnaammee>> | PPEERR  iiss  kknnoowwnn  ffoorr  hhiiss  aapppprrooaacchhaabbllee  nnaattuurree  aanndd  iiss  aallwwaayyss  jjuusstt  aa  pphhoonnee  ccaallll  aawwaayy  aatt  <<PPhhoonnee  NNuummbbeerrss>> | CCOODDEE,,  rreeaaddyy  ttoo  lleenndd  aann  eeaarr  oorr  sshhaarree  hhiiss  iinnssiigghhttss  oonn  gglloobbaall  hheeaalltthh  iissssuueess.. |          |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| SSeelleecctt  EEnnggiinnee::                                           |                                                                                                                                                                                                  | MMaaxx  TTookkeennss                                                                                                                               |          |
| ggllmm--44--ffllaasshh                                                 |                                                                                                                                                                                                  | 551122                                                                                                                                             |          |
| AAPPII  KKeeyy::                                                       |                                                                                                                                                                                                  | TTeemmppeerraattuurree                                                                                                                             | 11..0000 |
00..0000 22..0000
TToopp  PP
00..8800
00..0000 11..0000
Figure9: WebDemofortheQuery-UnrelatedPIIMaskingMethod
5015

ConsistencyOptimizationPromptofSingleSubject
Youareacharacterfeatureselectortaskedwithidentifyingandrefininglogicallyconsistentfeature
combinations. Iwillprovideyouwithcharacterfeatures. Yourroleistoidentifyanyfeaturesthat
haveobviouslogicalconflictsorinconsistencies,andmodifythemtocreateacoherentsetwhile
preservingtheircoreclassifications.
Requirements:
1. Theselectedcharacterfeaturesmustbelogicallyconsistentwithreal-worldexpectations,with
noobviousconflicts.
2. When resolving conflicts, modify only the feature entities while keeping their PII types and
classificationsunchanged.
3. ModifiedfeatureentitiesmustremainwithinthesamePIItypeandclassificationcategoriesas
theiroriginals.
4. Aimtomaintainasmanyfeaturesaspossible,ideallymatchingtheoriginalcountorcomingas
closeasfeasible.
Commonconflictpatternstoidentifyandresolve:
-Temporalinconsistencies: Ageincompatiblewithworkexperienceduration,educationlevel,or
careerstage(e.g.,a23-year-oldwith15yearsofworkexperienceshouldbeadjustedto2yearsas
Juniorposition).
-Professionalmismatches: Occupationinconsistentwitheducationbackgroundorsalaryrange
(e.g.,ahighschoolgraduateworkingasalicensedphysician).
-Geographiccontradictions: Worklocationdistantfromresidentialaddresswithoutsupporting
evidence(e.g.,dailycommutespanningdifferentcontinents).
-Financialimplausibility: Income,expenses,andsavingsthatviolatebasiceconomicconstraints
(e.g.,monthlyexpensesexceedingmonthlyincomebyordersofmagnitude).
##CharacterFeatures
<PIIType><EntityCategory><PIIEntity>
{usr_features}
Pleaseprovideyouroutputinthefollowingformat:
-Under"##Reason:",explainyourselectionandmodificationprocess,specificallyaddressingany
conflictpatternsidentifiedabove
-Under"##FinalFeatures:",listthefinalselectedfeaturesasJSONobjectsintheformat{{"label":
xxx,"tag": yyy,"entity": zzz}}withnoadditionalcontentorlinebreakswherexxxisthePIItype,
yyyistheentitycategory,andzzzisthePIIentity.
##Reason: [Explainyourselectionandmodificationprocess]
##FinalFeatures: [{{"label": xxx,"tag": yyy,"entity": zzz}},{{"label":xxx,"tag": yyy,"entity":
zzz}},...]"""
Figure10: PromptofConsistencyOptimizationforSingle-Subject
5016

ConsistencyOptimizationPromptofMultiSubject
You are a character feature selector tasked with identifying and refining logically consistent
featurecombinations. Iwillprovideyouwithcharacterfeaturesfordifferentsubjectsandtheir
relationships. Yourroleistoidentifyconflictsandmodifyfeaturestoalignwiththerelationship
whilepreservingPIItypesandcategories.
Requirements:
1. Selectedfeaturesmustbelogicallyconsistentandalignwiththerelationshipbetweensubjects.
2. Applyrelationship-awareconstraints:
-Intersectionrelationships(colleagues,classmates): Subjectssharecriticalattributes(e.g.,same
organization,institution).
-Hierarchicalrelationships(parent-child,supervisor-subordinate): Enforceagedifferences(parent
18yearsolder),authoritylevels,andderivedattributeswhenappropriate.
≥
- Non-intersection relationships (strangers): Maintain independent profiles, but ensure internal
consistencyforeachsubject.
3. Whenmodifying: KeepPIItypeandcategoryunchanged,onlyadjustentityvalues.
4. Maximizefeatureretention: Aimtopreservetheoriginalcount.
##SubjectAFeatures
<PIIType><EntityCategory><PIIEntity>
{usr_features_a}
##SubjectBFeatures
<PIIType><EntityCategory><PIIEntity>
{usr_features_b}
##RelationshipBetweenSubjects
{rel}
Pleaseprovideyouroutputinthefollowingformat:
-Under"##Reason:",explainyourselectionandmodificationprocess,addressinghowrelationship
constraintsareenforced.
-Under"##FinalFeaturesA:"and"##FinalFeaturesB:",listthefinalselectedfeaturesasJSON
objectsintheformat{{"label": xxx,"tag": yyy,"entity": zzz}}.
##Reason: [Explainyourselectionandmodificationprocess]
##FinalFeaturesA:[{{"label":xxx,"tag": yyy,"entity": zzz}},{{"label":xxx,"tag": yyy,"entity":
zzz}},...]
##FinalFeaturesB:[{{"label":xxx,"tag": yyy,"entity": zzz}},{{"label":xxx,"tag": yyy,"entity":
zzz}},...]
Figure11: PromptofConsistencyOptimizationforMulti-Subject
5017

QueryScenarioGenerationPrompt
YouarearealuserinteractingwithanAIchatbot. BasedonALLtheselectedentitiesprovided,
generate a diverse set of everyday conversation scenarios where you might engage with the
chatbot.
Requirements:
1. EachgeneratedscenariomustberelevanttoALLtheselectedentities
2. Thescenariosshouldbediverseandcoverdifferentdomainssuchas:
-Careerplanningandprofessionaldevelopment
-Medicalconsultationandhealthcaremanagement
-Financialplanningandadvisory
-Legaladviceandcompliance
-Academicmentoringandeducation
-Housingandrealestateapplications
-Personallifemanagement
3. Avoidrepeatingsimilarscenariotypes
4. Ensureeachscenarionaturallyrequiresallselectedentitiestoaddressuserneeds
5. OutputthescenarionamesasaPythonlist
##SelectedEntities
{select_ents}
Pleaseprovideyouroutputinthefollowingformat:
- Under "## Reason:", explain your analysis of the entities and how each proposed scenario
naturallyincorporatesallofthem
-Under"##Result:",outputaJSONobjectcontainingthelistofscenarionames
##Reason: [Explainyourthoughtprocessandentityanalysis]
##Result: {{"scene": [scenario1,scenario2,scenario3]}}
Figure12: PromptforQueryScenarioGeneration
5018

PIIDetectionPrompt
Please identify the PII entities and their corresponding PII types for each distinct individual
mentionedintheconversationtranscript,includingbothspeakersandreferencedindividuals.
ThePIItypesaredefinedasfollows:
{pii_definition}
PIItypesinclude: ["PER","CODE","LOC","ORG","DEM","DATETIME","QUANTITY"]
##TaskDescription:
Yourtaskisto:
1. IdentifyALLdistinctindividualsmentionedinthetext,including:
-Primaryspeakers(markedwith[PER_X])
-Individualsmentionedwithinothers’statements
-Referencedcolleagues,familymembers,orassociates
2. Foreachidentifiedindividual,extracttheirassociatedPIIentities,ensuring:
-Eachentityisinitssmallestviabletextspan
-Entitiesarecorrectlycategorizedbytype
-Cross-referencedinformationisattributedtothecorrectindividual
##ImportantRules:
1. Treateachindividualasaseparatesubject,evenifmentionedwithinanotherperson’sstatement
2. Includebothexplicitlynamedindividualsandthosereferencedthroughrelationships
3. Maintainclearboundariesbetweendifferentindividuals’information
4. Extractexactentityspanswithoutadditionalcontext
5. Preservespecialcharactersincodesandquantities
6. Handlebothdirectmentionsandindirectreferences
##Givenconversationtranscript:
{user_desc}
##RequiredOutputFormat:
Foreachidentifiedindividual(bothspeakersandmentionedpersons),output:
Subject{{N}}{{ent1: type1,ent2: type2,...}}
##Example:
Inputtext: "[PER_1]: I’mAlex,workingatGoogle. MyfriendBob,whois25yearsold,worksat
Apple."
Expectedoutput:
Subject{{1}}{{"Alex": "PER","Google": "ORG"}}
Subject{{2}}{{"Bob": "PER","25years": "DATETIME","Apple": "ORG"}}
Beginanalysisnow:
Figure13: PromptusedforthePIIDetectiontask
5019

BasicQuery-RelatedPIIDetectionPrompt
Please identify highly relevant PII (Personally Identifiable Information) entities from the
backgrounddescriptionPIIentitiesthatdirectlyaddressorrelatetotheuser’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
###Backgrounddescription:
{desc}
###Query:
{query}
Youroutputwillcontainthefollowingformat:
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure14: PromptofNaiveMethod
5020

Choice-BasedQuery-RelatedPIIDetectionPrompt
Fromthefollowingoptions,PleaseidentifyhighlyrelevantPII(PersonallyIdentifiableInforma-
tion) entities from the background description PII entities that directly address or relate to the
user’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
-Selectonlyfromtheprovidedoptions
###Backgrounddescription:
{desc}
###Query:
{query}
##Options:
{choices}
Youroutputwillcontainthefollowingformat:
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure15: PromptofNaive/wChoiceMethod
5021

Chain-of-ThoughtQuery-RelatedPIIDetectionPrompt
Please identify highly relevant PII (Personally Identifiable Information) entities from the
backgrounddescriptionPIIentitiesthatdirectlyaddressorrelatetotheuser’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
###Backgrounddescription:
{desc}
###Query:
{query}
Youroutputwillcontainthefollowingformat:
###Thought: ExplainyourreasoningstepbystepforselectingtherelevantPIIentities.
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Thought: xxx
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure16: PromptofSelf-CoTMethod
5022

AutoChain-of-ThoughtQuery-RelatedPIIDetectionPromptwithExamples
Please identify highly relevant PII (Personally Identifiable Information) entities from the
backgrounddescriptionPIIentitiesthatdirectlyaddressorrelatetotheuser’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
###Backgrounddescription:
{desc}
###Query:
{query}
Youwillbegiven3examplestohelpyouunderstandthetask.
Example1:
## Background: "Hello, I’m Sarah. I work at Microsoft as a junior developer with 2 years of
experience. IliveinSeattle."
##Query: "WhatskillsshouldIfocusondevelopinginmyearlytechcareerataleadingsoftware
companytoadvancefrommyentry-levelprogrammingrole?"
##Answer: ["Microsoft","juniordeveloper"]
[Additionalexamplesomittedforbrevity]
Youroutputwillcontainthefollowingformat:
###Thought: ExplainyourreasoningstepbystepforselectingtherelevantPIIentities.
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Thought: xxx
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure17: PromptofAuto-CoTMethod
5023

Self-ConsistencyQuery-RelatedPIIDetectionPrompt
Please identify highly relevant PII (Personally Identifiable Information) entities from the
backgrounddescriptionPIIentitiesthatdirectlyaddressorrelatetotheuser’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
###Backgrounddescription:
{desc}
###Query:
{query}
Youroutputwillcontainthefollowingformat:
###Thought: Generate5completelydifferentperspectivesofyourreflectionsforselectingthe
relevantPIIentities.
###Summary: Outputasummaryofallyourthinking.
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Thought:
1. xxxxxx
2. xxxxxx
3. xxxxxx
4. xxxxxx
5. xxxxxx
###Summary:
xxxxx
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure18: PromptofSelf-ConsistencyMethod
5024

Plan-and-SolveQuery-RelatedPIIDetectionPrompt
Please identify highly relevant PII (Personally Identifiable Information) entities from the
backgrounddescriptionthatdirectlyaddressorrelatetotheuser’squery.
Rules:
-Extractentitiesintheirsmallestpossiblespan
-Excludeallpersonnames
-Focusonlyonentitiescrucialforansweringthequery
-Returnentitiesexactlyastheyappearinthetext
###Backgrounddescription:
{desc}
###Query:
{query}
Youroutputwillcontainthefollowingformat:
###Thought: PleasestartwithageneralplanforselectingtherelevantPIIentities,andthenthink
step-by-stephowtosolveitbasedontheplan.
###Answer: ListtherelevantPIIentities,eachenclosedindoublequotes(""). Returnonlythelist
withoutexplanation. Example: ["key_pii_1",...,"key_pii_n"]
Please have your output follow the format below: (if there is only one entity, please out-
put["key_pii_1"]):
###Thought: xxx
###Answer: ["key_pii_1",...,"key_pii_n"]
Figure19: PromptofPlanandSolveCoTMethod
5025

LLMJudgeEvaluationPrompt
Iwantyoutoactasaneutraljudgeevaluatingresponsestoauserquery. Yourtaskistodetermine
whichresponsesbetteraddresstheuser’sintent.
UserQuery: {query}
ReferenceResponse(frompromptwithallinformation):
{original_response}
ResponseA(frompromptwithallPIImasked):
{masked_response}
ResponseB(frompromptwithquery-unrelatedPIImasked):
{adaptive_response}
Please evaluate which responses better satisfy the user’s intent and need, ignoring the
presence of personally identifiable information (PII). Focus only on how well each response
answersthequery.
Rateeachresponseonascaleof1-10where10isperfect:
1. ResponseArating(1-10):
2. ResponseBrating(1-10):
Thenprovideafinaljudgmentcomparingeachmaskedresponsetothereferenceresponsewith
oneoftheseoptions:
ForResponseA:
-ReferenceismuchbetterthanResponseA
-ReferenceisslightlybetterthanResponseA
-ReferenceandResponseAareequallygood
-ResponseAisslightlybetterthanReference
-ResponseAismuchbetterthanReference
ForResponseB:
-ReferenceismuchbetterthanResponseB
-ReferenceisslightlybetterthanResponseB
-ReferenceandResponseBareequallygood
-ResponseBisslightlybetterthanReference
-ResponseBismuchbetterthanReference
Provideyourfinaljudgmentsas:
JUDGMENTA:[yourchoice]
JUDGMENTB:[yourchoice]
Figure20: PromptofLLM-as-Judge
5026