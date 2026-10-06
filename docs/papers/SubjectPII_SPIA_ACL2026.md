> 원본: SubjectPII_SPIA_ACL2026.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 표 참조. PDF의 다단 편집·표·수식이 선형화되었으므로 보고 수치는 원본 PDF를 확인함. -->

Subject-level Inference for Realistic Text Anonymization Evaluation
|     | MyeongSeokOh1,2 |     |              | Dong-YunKim3 |     |               | HanseokOh4 |     |                 | ChaeanKang3 |     |     |
| --- | --------------- | --- | ------------ | ------------ | --- | ------------- | ---------- | --- | --------------- | ----------- | --- | --- |
|     | JoeunKang3      |     | XiaonanWang3 |              |     | HyunjungPark1 |            |     | YoungCheolJung1 |             |     |     |
HansaemKim3*
|     |     | 1Tscientific,SouthKorea |                              |     |     | 2SoongsilUniversity,SouthKorea |                                             |              |     |     |     |     |
| --- | --- | ----------------------- | ---------------------------- | --- | --- | ------------------------------ | ------------------------------------------- | ------------ | --- | --- | --- | --- |
|     |     |                         | 3YonseiUniversity,SouthKorea |     |     |                                |                                             | 4Mila,Canada |     |     |     |     |
|     |     | Abstract                |                              |     |     |                                | 2025a): theycanmemorizetrainingdata(Carlini |              |     |     |     |     |
etal.,2021;Shokrietal.,2017;Lukasetal.,2023)
Current text anonymization evaluation relies andinferpersonalattributesfromcontextwithout
onspan-basedmetricsthatfailtocapturewhat
priorexposuretospecificindividuals(Staabetal.,
anadversarycouldactuallyinfer,andassumes
|            |             |            |          |               |     |     | 2024). Thesecapabilitiesenableadversariestoex- |             |     |      |      |           |
| ---------- | ----------- | ---------- | -------- | ------------- | --- | --- | ---------------------------------------------- | ----------- | --- | ---- | ---- | --------- |
| a          | single data | subject,   | ignoring | multi-subject |     |     |                                                |             |     |      |      |           |
|            |             |            |          |               |     |     | tract sensitive                                | information |     | even | from | seemingly |
| scenarios. |             | To address | these    | limitations,  | we  |     |                                                |             |     |      |      |           |
anonymizedtexts,fundamentallychallengingtra-
presentSPIA(Subject-levelPIIInferenceAs-
sessment), the first benchmark that shifts the ditionalprotectionapproaches.
unitofevaluationfromtextspanstoindividu- Currentevaluationmethodsfortextanonymiza-
als,comprising675documentsacrosslegaland tion fail to address these emerging threats in two
onlinedomainswithnovelsubject-levelprotec-
|              |     |                              |     |     |     |     | critical ways. | First, | span-based |     | metrics | measure |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | -------------- | ------ | ---------- | --- | ------- | ------- |
| tionmetrics. |     | Extensiveexperimentsshowthat |     |     |     |     |                |        |            |     |         |         |
onlywhetherexplicitmentionsaremasked(Pilán
evenwhenover90%ofPIIspansaremasked,
|     |     |     |     |     |     |     | et al., 2022; | Shen | et  | al., 2025; | Beltrame | et al., |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --- | ---------- | -------- | ------- |
subject-levelinferenceprotectiondropsaslow
|     |      |             |          |             |     |     | 2024),failingtocaptureinferencerisks. |     |     |     |     | Staabetal. |
| --- | ---- | ----------- | -------- | ----------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---------- |
| as  | 33%, | leaving the | majority | of personal | in- |     |                                       |     |     |     |     |            |
formation recoverable through contextual in- (2025)shows66.3%ofpersonalattributesremain
ference. Furthermore, target-subject-focused inferableevenafterNER-basedanonymization—
anonymizationleavesnon-targetsubjectssub- demonstratingthatmaskingalonecannotprevent
| stantially |     | more exposed | than | the target | sub- |     |                   |     |                              |     |     |     |
| ---------- | --- | ------------ | ---- | ---------- | ---- | --- | ----------------- | --- | ---------------------------- | --- | --- | --- |
|            |     |              |      |            |      |     | inferenceattacks. |     | Second,existingapproachesas- |     |     |     |
ject. We show that subject-level inference- sume a single target subject (Pilán et al., 2022;
basedevaluationisessentialforensuringsafe
Manzanares-Saloretal.,2024;Staabetal.,2024),
textanonymizationinreal-worldsettings.1
|     |     |     |     |     |     |     | while real-world |     | texts, | such | as legal | judgments, |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ---- | -------- | ---------- |
1 Introduction medical records, and online posts, often mention
|     |     |     |     |     |     |     | multiple individuals |     | (Shen | et  | al., 2025). | Current |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | --- | ----------- | ------- |
Textanonymizationprotectsindividualprivacyby anonymizationtechniqueslargelyfocusonprotect-
modifying textual data to prevent identification ingoneprimarysubject,leavingothermentioned
(Larbi et al., 2022). The EU General Data Pro- individualsinadequatelyaddressed. Theselimita-
tectionRegulation(GDPR)definespersonaldata tions fail to capture whether all individuals in a
as“anyinformationrelatingtoanidentifiedoriden- documentareactuallyprotected.
tifiable natural person” (European Union, 2016), To address these limitations, we propose
requiring protection for all individuals whose in- SPIA(Subject-levelPIIInferenceAssessment),a
formation appears in a document. As large lan- benchmark and evaluation framework that shifts
guagemodels(LLMs)areincreasinglytrainedon theunitofevaluationfromtextspanstoindividu-
massivetextcorpora(Wangetal.,2025b),robust als. Wedefineasubjectasanypersonidentifiable
anonymizationtechniqueshavebecomeessential within a document, and treat each subject as the
forprotectingprivacyandenablingsafedatashar- unit of contextual inference, while the ultimate
ing (Deußer et al., 2025; Monteiro et al., 2024). objectiveistoprotecteveryindividualwhoseinfor-
However,LLMssimultaneouslyintroducenewpri- mationappearsinthetext. SPIAthusassesseshow
vacyrisksthroughouttheirlifecycle(Wangetal., effectively each individual is actually protected
|     |     |     |     |     |     |     | after anonymization. |     |     | As illustrated |     | in Figure 1, |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------------- | --- | ------------ |
*Correspondingauthor.
|     |     |     |     |     |     |     | our subject-level |     | approach | evaluates |     | all individu- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --------- | --- | ------------- |
1Codeanddatasetareavailableathttps://github.com
/maisonOP/spia.git als identifiable from a document, unlike existing
17100
Proceedingsofthe64thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),pages17100–17135
July2-7,2026©2026AssociationforComputationalLinguistics

Original: "@Murray : School week over after a week of marking. Teacher mode off, weekend with Sarah ahead.
Nothing beats watching the All Blacks with her. #KiwiCouple #NewZealand "
Anonymized: "@[PERSON] : School week over after a week of marking. [OCCUPATION] mode off, weekend with [PERSON] ahead.
Nothing beats watching the All Blacks with her. #KiwiCouple [LOCATION] "
(a) Span-based Evaluation (b) Single-Subject Inference (c) Subject-level Inference (Ours)
"Are PII spans masked?" “Is Authorprotected?” “Are all subjects protected?”
| “Murray” → “[PERSON]” |     |     | Author                                     |     |     | Subject 1 (Author)                         |     |     |     |
| --------------------- | --- | --- | ------------------------------------------ | --- | --- | ------------------------------------------ | --- | --- | --- |
|                       |     |     | Name: Protected                            |     |     | Name: Protected                            |     |     |     |
|                       |     |     | Occupation: Teacher  ←  "school week" and  |     |     | Occupation: Teacher  ←  "school week" and  |     |     |     |
“Teacher” → “[OCCUPATION]” "marking" indicate teaching profession "marking" indicate teaching profession
|     |     |     | Location: New Zealand ← "All Blacks" (NZ     |     |     | Location: New Zealand ← "All Blacks" (NZ     |     |     |     |
| --- | --- | --- | -------------------------------------------- | --- | --- | -------------------------------------------- | --- | --- | --- |
|     |     |     | rugby team) and "#KiwiCouple" reveal country |     |     | rugby team) and "#KiwiCouple" reveal country |     |     |     |
“Sarah” → “[PERSON]”
Subject 2 (Spouse)
|                             |     |     | (Non-Target Subjects Ignored) |     |     | Name: Protected |     |     |     |
| --------------------------- | --- | --- | ----------------------------- | --- | --- | --------------- | --- | --- | --- |
| “NewZealand” → “[LOCATION]” |     |     |                               |     |     | Occupation: -   |     |     |     |
Location: New Zealand ← from partner's location
Inference risk not evaluated Inference risk evaluated Inference risk evaluated
No subject-level evaluation Non-target subjects ignored All subjects evaluated
Figure1: Comparisonofthreeevaluationapproachesfortextanonymization. Span-basedevaluation(a)achieves
100%maskingrecallbutfailstoassesswhetherPIIremainsinferablefromcontext. Inference-basedsingle-subject
evaluation(b)detectsinferenceriskforthetargetsubject,butignoresnon-targetsubjects. Ourinference-based
subject-levelapproach(c)evaluatesallindividualsidentifiablefromthetext,betterreflectingreal-worldscenarios
wheremultiplesubjectsappear.
span-basedorsingle-subjectmethods. SPIAcom- subject-focused anonymization can fail to ade-
prises675documentswith15PIIcategoriesacross quately protect non-target subjects, and that ef-
legalandonlinedomains,andemploysatwo-stage fectivenessvariesacrossdocumenttypes.
methodologythatidentifiesalldatasubjectswithin
2 RelatedWork
| a document | and infers | PII for each subject | sepa- |     |     |     |     |     |     |
| ---------- | ---------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- |
rately. Weintroducenovelmetricsforper-subject 2.1 PersonalDataandPII
| andcollectiveprotectionassessment. |     |     | Throughex- |       |         |             |        |          |      |
| ---------------------------------- | --- | --- | ---------- | ----- | ------- | ----------- | ------ | -------- | ---- |
|                                    |     |     |            | Major | privacy | regulations | define | personal | data |
tensiveexperimentsacross4anonymizationmeth-
scope: GDPRcoversinformationrelatingtoiden-
odsand6LLMbackbones,werevealthreekeyfind-
|     |     |     |     | tifiable | persons | (European | Union, | 2016), | while |
| --- | --- | --- | --- | -------- | ------- | --------- | ------ | ------ | ----- |
ings: first,span-basedmetricssignificantlyoveres-
CCPAextendstoinformationreasonablylinkable
timateprotection—despiteover90%maskingrates,
|     |     |     |     | toconsumers(CaliforniaLegislature,2018). |     |     |     |     | Prior |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ----- |
inference-basedprotectionremainsaslowas33%;
|     |     |     |     | research | classifies | PII | into direct | identifiers | (e.g., |
| --- | --- | --- | --- | -------- | ---------- | --- | ----------- | ----------- | ------ |
second,anonymizationfocusingonatargetsubject
|     |     |     |     | names) | that enable | immediate |     | identification, | and |
| --- | --- | --- | --- | ------ | ----------- | --------- | --- | --------------- | --- |
canleavenon-targetsubjectslessprotected;third,
quasi-identifiers(e.g.,dateofbirth)thatenablere-
thesepatternsvarysubstantiallyacrossdocument
identificationwhencombined(Elliotetal.,2020;
types,requiringdomain-awareapproaches.
|     |     |     |     | Domingo-Ferrer |     | et al., | 2016). | Notably, | gender, |
| --- | --- | --- | --- | -------------- | --- | ------- | ------ | -------- | ------- |
Ourcontributionscanbesummarizedasfollows:
|     |     |     |     | birth date, | and | zip code | alone | can identify | 63– |
| --- | --- | --- | --- | ----------- | --- | -------- | ----- | ------------ | --- |
87%oftheU.S.population(Sweeney,2000;Golle,
| • SPIABenchmark: | Thefirstmulti-subject,multi- |     |     |     |     |     |     |     |     |
| ---------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2006),withsuchriskspersistingeveninincomplete
domainbenchmarkforsubject-levelprivacyas-
|     |     |     |     | datasets | (Rocher | et al., | 2019). | Both thus | require |
| --- | --- | --- | --- | -------- | ------- | ------- | ------ | --------- | ------- |
sessmentintextanonymization.
|     |     |     |     | protection | under | privacy | regulations | (Pilán | et al., |
| --- | --- | --- | --- | ---------- | ----- | ------- | ----------- | ------ | ------- |
2022).
| • Subject-wiseEvaluationFramework: |     |     | Atwo- |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
However,thisdirect/quasi-identifierdistinction
stagemethodologywithnovelmetricsforsubject-
levelprotectionassessment. iscontext-dependent,sincedateofbirthistypically
|     |     |     |     | a quasi-identifier |     | but | can serve | as a direct | identi- |
| --- | --- | --- | --- | ------------------ | --- | --- | --------- | ----------- | ------- |
• EmpiricalFindings: Evidencethatspan-based fier within small groups (Pilán et al., 2022). We
metrics overestimate protection, that single- thereforeadoptaclassificationbasedonstructural
17101

characteristics: CODE types have fixed formats Dataset Scale Cov. Inf. M-D S-A
(e.g.,phonenumbers,emails),whileNON-CODE i2b2/UTHealth 1,304 × × ×
△
| typesarefree-text(e.g.,names,age). |     |     |     |     |     | WikiPII |     | 23,090 |     | ×   | ×   | ×   |
| ---------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- | --- |
△
|                       |     |     |     |     |     | TAB            |     | 1,268 |     | ×   | ×   |     |
| --------------------- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
|                       |     |     |     |     |     |                |     |       | ✓   |     |     | △   |
|                       |     |     |     |     |     | PersonalReddit |     | 520   | ×   |     | ×   |     |
| 2.2 TextAnonymization |     |     |     |     |     |                |     |       |     | ✓   |     | △   |
|                       |     |     |     |     |     | PANORAMA       |     | 384K  |     | ×   |     |     |
|                       |     |     |     |     |     |                |     |       | ✓   |     | △   | △   |
Text anonymization modifies textual data to pro- PII-Bench 2,842 × ×
|                                              |     |     |     |     |     |            |     |     | ✓   |     |     | ✓   |
| -------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|                                              |     |     |     |     |     | SPIA(Ours) |     | 675 |     |     |     |     |
| tectindividualprivacythroughtechniquessuchas |     |     |     |     |     |            |     |     | ✓   | ✓   | ✓   | ✓   |
suppression,perturbation,andsubstitution(Larbi
|                |           |     |          |            |      | Table 1: | Comparison |     | of existing | text | anonymization |     |
| -------------- | --------- | --- | -------- | ---------- | ---- | -------- | ---------- | --- | ----------- | ---- | ------------- | --- |
| et al., 2022), | providing |     | stronger | protection | than |          |            |     |             |      |               |     |
benchmarkdatasets.Cov.=Coverage,Inf.=Inference,M-
| de-identification(Kanwaletal.,2024). |     |     |     |     | Acommon |                 |     |                    |     |     |              |     |
| ------------------------------------ | --- | --- | --- | --- | ------- | --------------- | --- | ------------------ | --- | --- | ------------ | --- |
|                                      |     |     |     |     |         | D=Multi-domain, |     | S-A=Subject-aware. |     |     | ✓=supported, |     |
approachidentifiesPIIspansandmasksthem,us- =limitedsupport,×=notsupported.
△
| ing either | NER models | (Lison |     | et al., | 2021; Pilán |     |     |     |     |     |     |     |
| ---------- | ---------- | ------ | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
etal.,2022)orLLMsinstructedtodetectandredact
|                                      |     |     |     |     |              | coveragebutlacksinference-basedevaluation. |     |     |     |     |     | Per- |
| ------------------------------------ | --- | --- | --- | --- | ------------ | ------------------------------------------ | --- | --- | --- | --- | --- | ---- |
| sensitiveinformation(Liuetal.,2023). |     |     |     |     | Differential |                                            |     |     |     |     |     |      |
sonalRedditsupportsinferencebuttargetsonlythe
| privacy | has also | been applied | to  | text | anonymiza- |               |     |                                   |     |     |     |     |
| ------- | -------- | ------------ | --- | ---- | ---------- | ------------- | --- | --------------------------------- | --- | --- | --- | --- |
|         |          |              |     |      |            | singleauthor. |     | PII-Benchdistinguishessubjectsbut |     |     |     |     |
tion,framinganonymizationasarandomizedtrans-
|     |     |     |     |     |     | remainsatspan-basedevaluation. |     |     |     | SPIA | isthefirst |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---- | ---------- | --- |
formationthatlimitsthedistinguishabilityoftexts
benchmarksatisfyingallfourproperties.
acrossindividuals(Dworketal.,2006;Utpalaetal.,
2023). Beyondspan-levelmasking,adversarialap- 2.4 AnonymizationEvaluationMetrics
proachesdefendagainstinferenceattacksbymis-
TokenRecallmeasurestheratioofmaskedtokens
leadingadversariesoriterativelyremovingreveal-
|                                            |     |     |     |     |     | among  | all PII  | tokens | (Lison   | et al., | 2021).    | Entity |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------ | -------- | ------ | -------- | ------- | --------- | ------ |
| ingcues(Frikhaetal.,2024;Staabetal.,2025). |     |     |     |     | Re- |        |          |        |          |         |           |        |
|                                            |     |     |     |     |     | Recall | measures | the    | ratio of | fully   | protected | enti-  |
centworkhasalsoemphasizedevaluatingprivacy-
ties,whereanentityisconsideredprotectedonly
| utility tradeoffs, |             | as overly | aggressive |     | anonymiza-    |          |                 |     |     |        |        |         |
| ------------------ | ----------- | --------- | ---------- | --- | ------------- | -------- | --------------- | --- | --- | ------ | ------ | ------- |
|                    |             |           |            |     |               | when all | its occurrences |     | are | masked | (Pilán | et al., |
| tion can           | render text | unusable  | (Chen      |     | et al., 2024; |          |                 |     |     |        |        |         |
2022). Itisreportedseparatelyfordirectidentifiers
| Yang et                               | al., 2025). | We  | evaluate | anonymization |     |           |                   |        |                   |     |       |           |
| ------------------------------------- | ----------- | --- | -------- | ------------- | --- | --------- | ----------------- | ------ | ----------------- | --- | ----- | --------- |
|                                       |             |     |          |               |     | (ER ),    | which             | enable | re-identification |     |       | individu- |
| methodsfromtheseapproachesinSection5. |             |     |          |               |     | di        |                   |        |                   |     |       |           |
|                                       |             |     |          |               |     | ally, and | quasi-identifiers |        | (ER               | ),  | which | enable    |
qi
2.3 AnonymizationEvaluationBenchmarks re-identificationonlythroughcombination. These
span-basedmetricsevaluateonlyexplicitmentions
| Various | benchmarks | have | been | proposed | for |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andcannotcapturewhatanadversarycouldinfer
| text anonymization. |     | i2b2/UTHealth |     |     | (Stubbs and |                 |     |                               |     |     |     |     |
| ------------------- | --- | ------------- | --- | --- | ----------- | --------------- | --- | ----------------------------- | --- | --- | --- | --- |
|                     |     |               |     |     |             | throughcontext. |     | Staabetal.(2024)’sAdversarial |     |     |     |     |
Uzuner,2015)focusesonmedicalrecords,WikiPII
|                                             |     |     |     |     |     |          |       | measures |     | inference-based |     | pri- |
| ------------------------------------------- | --- | --- | --- | --- | --- | -------- | ----- | -------- | --- | --------------- | --- | ---- |
| (Hathurusingheetal.,2021)onWikipediabiogra- |     |     |     |     |     | Accuracy | (AAC) |          |     |                 |     |      |
vacyrisksusingLLMadversaries,butassumesa
| phies, and         | the Text  | Anonymization |           |              | Benchmark |                                     |     |                            |     |     |           |     |
| ------------------ | --------- | ------------- | --------- | ------------ | --------- | ----------------------------------- | --- | -------------------------- | --- | --- | --------- | --- |
|                    |           |               |           |              |           | singlesubjectastheprotectiontarget. |     |                            |     |     | Toaddress |     |
| (TAB)              | (Pilán et | al., 2022)    | on        | legal        | documents |                                     |     |                            |     |     |           |     |
|                    |           |               |           |              |           | theselimitations,                   |     | weproposeIndividualProtec- |     |     |           |     |
| with comprehensive |           | PII           | coverage. | PersonalRed- |           |                                     |     |                            |     |     |           |     |
tionRate(IPR)andCollectiveProtectionRate
dit(Staabetal.,2024)introducedinference-based
(CPR),detailedinSection4.
evaluationforauthorprofiling,whilePANORAMA
| (Selvam | and Ghosh, | 2025) | provides |     | large-scale |     |     |     |     |     |     |     |
| ------- | ---------- | ----- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
3 SPIABenchmarkConstruction
| syntheticdataacrossmultiplelocales. |     |     |     |     | PII-Bench |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
(Shenetal.,2025)addressesmulti-subjectscenar- SPIA is built on two English text datasets,
ioswithquery-awareprivacyprotectionevaluation. legal documents (TAB) and online content
We identify four desirable properties for text (PANORAMA),comprising675documentswith
anonymization benchmarks: (1) Coverage— 1,712subjectsand7,040PIIsannotatedacross15
comprehensive PII types from direct to quasi- categories. Figure2illustratesourfive-stagecon-
| identifiers; | (2) | Inference—addressing |     |     | context- | structionpipeline. |     |     |     |     |     |     |
| ------------ | --- | -------------------- | --- | --- | -------- | ------------------ | --- | --- | --- | --- | --- | --- |
inferableinformationbeyondexplicitmentions;(3)
3.1 SourceData
Multi-domain—diversetextdomains;(4)Subject-
aware—per-subjectevaluationinmulti-subjectsce- TAB comprises 144 ECHR legal judgments fil-
| narios. |     |     |     |     |     | tered from | 1,268 | documents |     | (Pilán | et al., | 2022) |
| ------- | --- | --- | --- | --- | --- | ---------- | ----- | --------- | --- | ------ | ------- | ----- |
As shown in Table 1, existing datasets satisfy toensure: (1)variedsubjectcountsfrom2to5or
onlysomeoftheseproperties. TABachievesbroad more, (2) rich demographic PIIs from TAB’s an-
17102

LLM-Assisted
4
1 Source Data Selection 2 Two-Stage Framework 3 Framework Validation Annotation
LLMpre-label (380 docs)
|     | TAB (Legal documents) | Stage A                |     | Human Annotation              |     |     |
| --- | --------------------- | ---------------------- | --- | ----------------------------- | --- | --- |
|     |                       | Subject Identification |     | (295 docs: TAB 144 / PAN 151) |     |     |
1,268 docs → 144 docs
|     | Filtered by: #subjects, PII type |     |     |     | Human review (380 docs) |     |
| --- | -------------------------------- | --- | --- | --- | ----------------------- | --- |
+
|     |                           | Stage B                    |     | 11 LLMs tested                 |     |     |
| --- | ------------------------- | -------------------------- | --- | ------------------------------ | --- | --- |
|     | PANORAMA (Online content) | Subject-wise PII Inference |     | (Subject Match + PII Accuracy) |     |     |
5 Quality Check
384K docs → 531 docs
|     | Filtered by: #subjects, PII type | CODE Type (5) |     |     |     |     |
| --- | -------------------------------- | ------------- | --- | --- | --- | --- |
Cross-labeled docs (20%)
|     |                 | NON-CODE Type (10) |     | Best: Claude-Sonnet-4.5 |                     |     |
| --- | --------------- | ------------------ | --- | ----------------------- | ------------------- | --- |
|     | Total: 675 docs |                    |     | ~96% / ~91%             | Subject Match: >95% |     |
PIIAgreement: >91%
Figure2: SPIAbenchmarkconstructionpipeline. DocumentsarefilteredbysubjectcountdistributionandPII
densitytoensurediverseevaluationscenarios. Thetwo-stageframeworkidentifiesallsubjects(StageA),then
infers CODE (5 types) and NON-CODE (10 types) PIIs per subject (Stage B). After validating 11 LLMs on
human-annotatedtestset,best-performingmodelpre-labelsremainingdocumentsforhumanreview.
notations,and(3)testsetscalealignedwithprior et al., 2024; Selvam and Ghosh, 2025). NON-
text anonymization studies (Papadopoulou et al., CODE types are free-text or categorical values:
2023;Pilánetal.,2025). Theselegalrecordsfea- Name,Sex,Age,Location,Nationality,Education,
tureapplicants,defendants,witnesses,andjudges, Relationship,Occupation,Affiliation,andPosition,
maintaining consistent facts about each individ- based on Staab et al. (2024)’s classification with
ualthroughout—enablingreliableinference-based additions from existing benchmarks (Pilán et al.,
| evaluation. |     |     |     | 2022;Feietal.,2024). | WeincludeCODEtypesin |     |
| ----------- | --- | --- | --- | -------------------- | -------------------- | --- |
PANORAMAincludes531syntheticonlinetexts inference-basedevaluationbecausepattern-based
from 384,789 documents (Selvam and Ghosh, NER detectors may miss formats unseen during
2025). Weprioritizedocumentswithdiversesub- training(e.g.,“(555)123-4567”vs.“5551234567”
jectcountsfrom1to5ormorethatcontainCODE foraphonenumber),whereasinference-basedap-
PIIs. Theoriginaldatasethasbeenconstructedwith proachescanrecognizetheunderlyinginformation
enforced attribute consistency (e.g., realistic age regardlessofsurfaceform.
gaps in family relationships, coherent education- Hardness & Certainty. Each PII is assessed on
occupation combinations), making it suitable for inferencedifficulty(Hardness,1–5)andconfidence
inference-basedevaluation. Wesample151docu- (Certainty,1–5),adoptingtheschemaestablished
ments(30%)asthetestset,comparableinscaleto inpriorinference-basedbenchmarks(Staabetal.,
| TAB. |     |     |     | 2024;Yukhymenkoetal.,2024). |     | Hardnessrepre- |
| ---- | --- | --- | --- | --------------------------- | --- | -------------- |
sentscognitiveeffortrequiredforinference,while
3.2 AnnotationSchema Certaintyindicatesconfidencebasedontextualev-
SubjectIdentification. Asubjectisanyindividual idence. Detailed annotation guidelines are pro-
personwhosePIIcanpotentiallybeinferredfrom videdinAppendixG,withscaleexamplesinAp-
pendixA.
| the text.                | Two key rules | are applied          | for checking |     |     |     |
| ------------------------ | ------------- | -------------------- | ------------ | --- | --- | --- |
| potentialidentification: |               | (1)thesamepersonmen- |              |     |     |     |
3.3 AnnotationProcess
| tioned | multiple times counts | as one | subject, and |     |     |     |
| ------ | --------------------- | ------ | ------------ | --- | --- | --- |
(2) collective references (e.g., “citizens of LA”) Two-StageFramework. SPIAextendsStaabetal.
areexcludedunlessaspecificcountisgiven(e.g., (2024)’sauthorprofilingapproachtosubject-level
“2 citizens”). This approach enables quantifiable inference. StageAidentifiesallsubjectsinthetext
privacyriskassessmentbyrestrictingourscopeto withdistinguishingdescriptions(names,roles,etc.).
enumerableindividuals. StageBinfersPIIsforeachidentifiedsubject,split
Wedefine15PIIcategoriesclas- intoseparateCODEandNON-CODEcalls. This
PIITaxonomy.
sifiedbystructuralcharacteristicsintoCODEand separation(1)avoidsrequiringthemodeltoiden-
NON-CODE types. CODE types are identifiers tify all 15 categories simultaneously, (2) reduces
withfixedstructuralpatterns: IDNumber,Driver prompt length, and (3) enables type-appropriate
License,Phone,Passport,andEmail,selectedfrom handling—thetwotypescandifferinoutputformat,
commonly addressed PII in prior research (Fei validation criteria, and annotation requirements,
17103

| Metric              |                                            |                               | TAB   | PANORAMA |       |     | Metric                               |              |           | TAB     | PANORAMA    |          | Total   |
| ------------------- | ------------------------------------------ | ----------------------------- | ----- | -------- | ----- | --- | ------------------------------------ | ------------ | --------- | ------- | ----------- | -------- | ------- |
| Cross-labeledDocs   |                                            |                               | 28    |          | 113   |     | Documents                            |              |           | 144     | 531         |          | 675     |
| AnnotatedSubjects   |                                            |                               | 95    |          | 222   |     | Num.ofSubjects                       |              |           | 586     | 1,126       |          | 1,712   |
|                     |                                            |                               |       |          |       |     | AvgSubjects/Doc                      |              |           | 4.07    | 2.12        |          | 2.54    |
| SubjectMatchRate    |                                            |                               | 96.8% |          | 94.7% |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     | Num.ofPIIs                           |              |           | 3,350   | 3,690       |          | 7,040   |
| TotalPIIComparisons |                                            |                               | 516   |          | 634   |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     |                                      |              |           | (3,064) | (2,969)     |          | (6,033) |
| Match               |                                            |                               | 91.3% |          | 94.3% |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     | AvgPIIs/Subject                      |              |           | 5.72    | 3.28        |          | 4.11    |
| LessPrecise         |                                            |                               | 4.8%  |          | 1.7%  |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     | AvgDocLength(chars)                  |              |           | 3,918   | 260         |          | -       |
| Mismatch            |                                            |                               | 3.9%  |          | 3.9%  |     |                                      |              |           |         |             |          |         |
| MeanScore           |                                            |                               | 93.7% |          | 95.2% |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     | Table 3:                             | SPIA Dataset |           | Basic   | Statistics. | Numbers  | in      |
|                     |                                            |                               |       |          |       |     | parenthesesindicatePIIswithCertainty |              |           |         |             | 3.       | TABcon- |
| Table2:             | Subject-wiseInferenceInter-AnnotatorAgree- |                               |       |          |       |     |                                      |              |           |         |             | ≥        |         |
|                     |                                            |                               |       |          |       |     | tains longer                         | legal        | documents |         | with more   | subjects | per     |
| ment(IAA)Results.   |                                            | Match/LessPrecise/Mismatchin- |       |          |       |     |                                      |              |           |         |             |          |         |
|                     |                                            |                               |       |          |       |     | document,                            | while        | PANORAMA  |         | offers      | shorter  | online  |
dicatePIIvalueagreementlevels.
textswithdiversePIItypesincludingCODEPIIs.
making them better suited to dedicated prompts. twocomplementarydatasets,asshowninTable3.
| The prompts | used | for | each | stage are | provided | in  |                                    |     |     |     |     |     |         |
| ----------- | ---- | --- | ---- | --------- | -------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | ------- |
|             |      |     |      |           |          |     | 85.7%(6,033)ofallPIIshaveCertainty |     |     |     |     |     | 3;addi- |
≥
AppendixG.2.
tionaldatasetdetailsareinAppendixA.
| Framework | Validation. |      | To       | validate | this     | frame- |                       |     |     |     |     |     |     |
| --------- | ----------- | ---- | -------- | -------- | -------- | ------ | --------------------- | --- | --- | --- | --- | --- | --- |
|           |             |      |          |          |          |        | 4 EvaluationFramework |     |     |     |     |     |     |
| work,     | we evaluate | 11   | LLMs     | on       | manually | con-   |                       |     |     |     |     |     |     |
| structed  | test sets   | from | selected | source   | data.    | Ex-    |                       |     |     |     |     |     |     |
Weproposeasubject-levelevaluationframework
tendingStaabetal.(2024)’smethodology,weeval-
|     |     |     |     |     |     |     | with novel | metrics | that | capture | inferable |     | privacy |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ------- | --------- | --- | ------- |
uatebothsubjectmatchingandPIIinference(see
risksacrossallsubjects.
| Appendix | C.3 | for details). | We  | measure |     | two met- |     |     |     |     |     |     |     |
| -------- | --- | ------------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
rics: SubjectMatchRatioforsubjectidentification
|                                       |                         |     |     |     |           |         | 4.1 Subject-levelPrivacyMetrics |                                   |          |       |          |      |          |
| ------------------------------------- | ----------------------- | --- | --- | --- | --------- | ------- | ------------------------------- | --------------------------------- | -------- | ----- | -------- | ---- | -------- |
| andInferenceAccuracyforPIIinference.  |                         |     |     |     |           | Claude- |                                 |                                   |          |       |          |      |          |
|                                       |                         |     |     |     |           |         | Let N                           | be the total                      | number   | of    | subjects | in   | a docu-  |
| Sonnet-4.5achievesthebestperformance: |                         |     |     |     |           | Subject |                                 |                                   |          |       |          |      |          |
|                                       |                         |     |     |     |           |         | ment,O                          | i bethenumberofGroundTruthPIIsfor |          |       |          |      |          |
| Match                                 | 96%andInferenceAccuracy |     |     |     | 91%onboth |         |                                 |                                   |          |       |          |      |          |
|                                       |                         |     |     |     |           |         | subject                         | i in the                          | original | text, | and      | A be | the num- |
i
| datasets,andisselectedforpre-labeling. |     |     |     |     |     | Detailed |        |         |           |     |       |       |          |
| -------------------------------------- | --- | --- | --- | --- | --- | -------- | ------ | ------- | --------- | --- | ----- | ----- | -------- |
|                                        |     |     |     |     |     |          | ber of | PIIs an | adversary | can | still | infer | from the |
resultsareinAppendixB.
anonymizedtextforsubjecti.
Annotation Procedure. Annotation proceeds in CollectiveProtectionRate(CPR)measuresthe
| threestages: | (1)humanannotationfortestset(295 |     |     |     |     |     |            |              |     |      |        |     |           |
| ------------ | -------------------------------- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ---- | ------ | --- | --------- |
|              |                                  |     |     |     |     |     | proportion | of protected |     | PIIs | across | all | subjects, |
docs),(2)LLMpre-labelingusingClaude-Sonnet-
wheresubjectswithmorePIIsnaturallycontribute
| 4.5 for | remaining | PANORAMA |     | (380 | docs), | and |     |     |     |     |     |     |     |
| ------- | --------- | -------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
moretotheoverallscore:
| (3) human | review | and | correction |     | to complete | all |     |     |     |     |     |     |     |
| --------- | ------ | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
N
| 675documents. |     |     |     |     |     |     |     |     |     |     | A   | i   |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               |     |     |     |     |     |     |     | CPR | =   | 1   | i=1 |     | (1) |
N
|     |     |     |     |     |     |     |     |     |     | −    | O   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | Pi=1 |     | i   |     |
3.4 QualityControlandDatasetStatistics
IndividualProtectionRateP(IPR)istheaverageof
| Inter-annotator |     | agreement | (IAA) |     | is measured | to  |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
per-subjectprotectionrates,assigningequalweight
| verify | annotation | reliability. |     | Five | annotators | re- |     |     |     |     |     |     |     |
| ------ | ---------- | ------------ | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
toallsubjectsregardlessoftheirPIIcount:
| ceivedoverlappingassignmentsof |     |                           |     | 20%documents |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | ------------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fromeachdataset.               |     | Agreementisevaluatedintwo |     |              |     |     |     |     |     | N   |     |     |     |
|                                |     |                           |     |              |     |     |     |     | 1   |     | A   |     |     |
|                                |     |                           |     |              |     |     |     | IPR | =   |     | 1   | i   | (2) |
stages—subjectmatchingbetweenannotatorpairs
|         |       |                  |     |     |          |       |     |     | N   |             | − O |           |     |
| ------- | ----- | ---------------- | --- | --- | -------- | ----- | --- | --- | --- | ----------- | --- | --------- | --- |
|         |       |                  |     |     |          |       |     |     |     | i=1(cid:18) |     | i(cid:19) |     |
| and PII | value | comparison—using |     |     | the same | scor- |     |     |     | X           |     |           |     |
ingschemeasSection4.2withadditionalhuman
Forbothmetrics,1indicatesfullprotectionand
| verification. | As  | shown | in Table | 2,  | labelers | iden- |             |      |           |     |          |             |     |
| ------------- | --- | ----- | -------- | --- | -------- | ----- | ----------- | ---- | --------- | --- | -------- | ----------- | --- |
|               |     |       |          |     |          |       | 0 indicates | full | exposure. | A   | concrete | calculation |     |
tify the same subjects in >94% of cases (TAB: exampleisprovidedinAppendixC.3.3.
96.8%,PANORAMA:94.7%)andassignmatching
PIIvaluesin>90%ofcomparisons(TAB:91.3%, 4.2 EvaluationProtocol
PANORAMA: 94.3%), with complete disagree- Computing CPR and IPR requires subject align-
ment below 4%. Disagreements are adjudicated ment between Ground Truth annotations and ad-
throughconsensus.
|     |     |     |     |     |     |     | versarial | inference | results | from | anonymized |     | text, |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | ---- | ---------- | --- | ----- |
ThefinalSPIAbenchmarkcomprises675doc- along with PII-level comparison. We define a 3-
uments, 1,712 subjects, and 7,040 PIIs across stepevaluationpipeline.
17104

Step 1: Subject Matching. For each docu- • Utility Evaluation: We adopt Staab et al.
ment, establish one-to-one correspondence be- (2024)’smethodology,computingMeanUtility
tween Ground Truth subjects from original text astheaverageofLLM-basedReadability,Mean-
andsubjectsidentifiedfromanonymizedtext. The ing,andROUGE-Lscores.
correspondenceisdeterminedbasedonsubjectde-
scriptionsandcontextualinformation. Unmatched Details on backbones and the evaluation pro-
|     |     |     |     |     |     | cedure | are described |     | in Appendix |     | C. To | verify |
| --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ----------- | --- | ----- | ------ |
GroundTruthsubjectsareassigned0pointsforall
|     |     |     |     |     |     | that evaluation |     | outcomes | are | robust | to adversary |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | ------ | ------------ | --- |
PIIs.
Formatchedsubjectpairs,ap- choice,weadditionallyvarytheadversaryacross
Step2: PIIScoring.
plyStaabetal.(2024)’sscoringschemetocompare GPT-4.1 and Claude-Haiku-4.5, obtaining Spear-
|            |       |         |       |        |              | man ρ | > 0.98 | for both | CPR | and IPR | across | all |
| ---------- | ----- | ------- | ----- | ------ | ------------ | ----- | ------ | -------- | --- | ------- | ------ | --- |
| individual | PIIs: | 1.0 for | exact | match, | 0.5 for par- |       |        |          |     |         |        |     |
anonymizationconfigurations(seeAppendixE.1).
tialmatch(e.g.,inferring“California”forGround
Truth“LosAngeles”),0.0formismatch.
5.2 AnonymizationMethods
| Step 3: Metric |                | Calculation. |         | Compute  | CPR and |              |     |              |     |                  |     |     |
| -------------- | -------------- | ------------ | ------- | -------- | ------- | ------------ | --- | ------------ | --- | ---------------- | --- | --- |
|                |                |              |         |          |         | Four methods |     | representing |     | major approaches |     | to  |
| IPR from       | the aggregated |              | scores. | Detailed | imple-  |              |     |              |     |                  |     |     |
mentationofeachstepisdescribedinAppendixC. textanonymizationareselected. Detailedmethod
|               |     |     |     |     |     | parameters          | and | backbone | configurations |             |     | are de- |
| ------------- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | -------------- | ----------- | --- | ------- |
| 5 Experiments |     |     |     |     |     | scribedinAppendixC. |     |          |                |             |     |         |
|               |     |     |     |     |     | TAB Longformer      |     | (Pilán   | et             | al., 2022): | An  | NER-    |
5.1 ExperimentalSetup
basedtokenclassificationapproachthatidentifies
| EvaluationProcedure. |     |     | Theexperimentsfollowa |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tokenscorrespondingtoPIIandreplacesthemwith
three-phaseprocess: (1)Anonymization—original maskingtokens( [PERSON] , [LOC] ,etc.).
textsareanonymizedusingeachmethodandback-
|                   |     |      |     |            |       | DeID-GPT | (Liu | et  | al., 2023): |     | A zero-shot |     |
| ----------------- | --- | ---- | --- | ---------- | ----- | -------- | ---- | --- | ----------- | --- | ----------- | --- |
| bone combination, |     | with | TAB | Longformer | using |          |      |     |             |     |             |     |
prompting-basedanonymizationtechniquethatfo-
a single model while other methods use 6 back- cuses on removing explicit PIIs by instructing
bones (GPT-4.1, GPT-4.1-Mini, Claude-Sonnet- LLMs to find defined PII categories and replace
| 4.5,Claude-Haiku-4.5,Llama-3.1-8B,Gemma-3- |     |     |                |     |            |                              | [redacted] |     |     |             |     |     |
| ------------------------------------------ | --- | --- | -------------- | --- | ---------- | ---------------------------- | ---------- | --- | --- | ----------- | --- | --- |
|                                            |     |     |                |     |            | themwith                     |            |     | .   |             |     |     |
| 27B), generating                           |     | 19  | configurations | in  | total. (2) |                              |            |     |     |             |     |     |
|                                            |     |     |                |     |            | DP-Prompt(Utpalaetal.,2023): |            |     |     | Amethodthat |     |     |
Subject-wisePIIInference—theadversarialLLM paraphrasestextwithhightemperaturetoobfuscate
(Claude-Sonnet-4.5)appliesthetwo-stageframe-
theauthor’swritingstyleandlinguisticpatterns.
workfromSection3.3toidentifysubjectsandinfer
|                                          |     |     |     |     |     | Adversarial | Anonymization |           |     | (AA)      | (Staab | et al., |
| ---------------------------------------- | --- | --- | --- | --- | --- | ----------- | ------------- | --------- | --- | --------- | ------ | ------- |
| 15PIIcategoriesfromtheanonymizedoutputs. |     |     |     |     | (3) |             |               |           |     |           |        |         |
|                                          |     |     |     |     |     | 2024):      | An iterative  | technique |     | that uses | an     | adver-  |
Evaluation—we assess each method from three sarial inference model to identify revealing cues
perspectives:
intext,thenremovesthemtopreventpersonalat-
|              |       |             |       |          |           | tributeinference. |        | Itisprimarilydesignedtodefend |     |         |      |        |
| ------------ | ----- | ----------- | ----- | -------- | --------- | ----------------- | ------ | ----------------------------- | --- | ------- | ---- | ------ |
| • Span-based |       | Evaluation: |       | Measures | whether   |                   |        |                               |     |         |      |        |
|              |       |             |       |          |           | against           | author | profiling                     | and | focuses | on a | single |
| Ground       | Truth | PII         | spans | are      | masked in |                   |        |                               |     |         |      |        |
subject(inthiswork,theapplicantforTABandthe
| anonymized | text. | Token | Recall | (R  | ) evalu- |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
di+qi
authorforPANORAMA).
atesattheindividualmentionlevel,whileEntity
| Recall evaluates |     | based | on  | whether | all spans of |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
5.3 Results
thesameentityaremasked,separatelyfordirect
Table4presentstheprivacyandutilityevaluation
| identifiers(ER |     | )andquasi-identifiers(ER |     |     | ).  |         |                     |     |     |         |       |       |
| -------------- | --- | ------------------------ | --- | --- | --- | ------- | ------------------- | --- | --- | ------- | ----- | ----- |
|                |     | di                       |     |     | qi  |         |                     |     |     |         |       |       |
|                |     |                          |     |     |     | results | for 4 anonymization |     |     | methods | and 6 | back- |
• Inference-basedEvaluation: Measureswhether bonesacrossPANORAMAandTABdatasets.
PII can still be inferred from anonymized text. MethodComparison. Longformerachievesnear-
AftermatchingGroundTruthsubjectsfromorigi- perfectspanmasking(ER 0.997)butthelowest
di
naltextwithsubjectsidentifiedfromanonymized CPR (0.330), demonstrating that entity recogni-
text,PII-levelscoringisperformedtocalculate tionalonecannotpreventinferenceattacks. DeID-
CPRandIPRasdefinedinSection4. Addition- GPT,whichalsotargetsexplicitPIIspansbutuses
ally, 1-AAC is reported to express AAC as a LLM-baseddetection,achievesbothhighmasking
protection rate, which measures protection for (R di+qi upto0.990)andcompetitiveinferencepro-
thetargetsubjectonly(applicantforTAB,author tection (CPR/IPR 0.799/0.820), with the highest
forPANORAMA). utility (up to 0.961), suggesting that LLM-based
17105

(a)PANORAMA(N=151) (b)TAB(N=144)
Span-based Inference-based Util. Span-based Inference-based Util.
Method Backbone R ERdi ERqi 1-AAC CPR IPR Mean R ERdi ERqi 1-AAC CPR IPR Mean
Longformer – .883 .873 .716 .589 .597 .585 .820 .940 .997 .923 .384 .330 .325 .874
Llama-3.1-8B .958 .997 .865 .819 .840 .866 .934 .889 1.00 .895 .495 .396 .388 .961
Gemma-3-27B .944 .991 .791 .679 .684 .688 .935 .978 1.00 .980 .536 .519 .505 .872
GPT-4.1-Mini .959 .997 .828 .687 .687 .689 .942 .947 1.00 .956 .504 .430 .418 .959
DeID-GPT
GPT-4.1 .984 1.00 .921 .775 .799 .820 .817 .990 1.00 .991 .638 .674 .665 .754
Claude-Haiku .921 .994 .712 .695 .694 .689 .946 .972 1.00 .974 .623 .570 .553 .947
Claude-Sonnet .969 1.00 .865 .711 .727 .735 .926 .988 .993 .990 .628 .650 .635 .770
Llama-3.1-8B .719 .659 .721 .467 .480 .519 .634 .855 .810 .859 .154 .578 .579 .684
Gemma-3-27B .387 .303 .447 .124 .144 .182 .744 .899 .869 .919 .212 .684 .689 .540
GPT-4.1-Mini .276 .146 .312 .131 .137 .157 .843 .289 .356 .216 .032 .132 .147 .851
DP-Prompt
GPT-4.1 .208 .115 .251 .138 .130 .162 .833 .561 .353 .512 .047 .137 .149 .785
Claude-Haiku .360 .189 .419 .148 .169 .200 .757 .782 .363 .762 .081 .346 .361 .755
Claude-Sonnet .388 .204 .498 .151 .194 .229 .772 .789 .450 .770 .067 .452 .446 .764
Llama-3.1-8B .890 .923 .819 .701 .759 .763 .825 .665 .619 .640 .510 .511 .510 .753
Gemma-3-27B .946 .991 .842 .709 .799 .835 .829 .815 .934 .797 .396 .339 .341 .809
Adversarial GPT-4.1-Mini .953 .997 .874 .737 .831 .859 .844 .555 .955 .494 .480 .432 .421 .885
Anon. GPT-4.1 .969 .994 .930 .795 .870 .897 .820 .894 1.00 .881 .450 .359 .365 .857
Claude-Haiku .970 .997 .907 .728 .789 .825 .853 .554 .723 .519 .342 .308 .307 .894
Claude-Sonnet .979 1.00 .944 .785 .852 .875 .815 .727 .990 .717 .472 .362 .364 .867
Table4: PrivacyandUtilityEvaluationResultsacrossanonymizationmethodsanddatasets. Highervaluesindicate
betterprotectionandutility. Span-basedmetricsincludeTokenRecall(R=R )andEntityRecall(ER ,ER ).
di+qi di qi
Inference-basedmetricsmeasureprotectionfortargetsubject(1-AAC)orallsubjects(CPR,IPR).MeanUtility
combinesReadability,Meaning,andROUGE-L.Bluecellsindicatethehighestvaluepermetric(tiesallowed).
detectionenablesmoreflexibleanonymizationthan the best-performing setup (AA with GPT-4.1 on
pattern-basedNER.DP-Promptshowsthelowest PANORAMA).(2)NER-basedmethodsexhibit
averageCPR(0.30),suggestingstyle-obfuscating the largest gap. Longformer on TAB achieves
differential privacy offers limited inference pro- near-perfect span masking (ER 0.997) while
di
tection. AAprovidesthestrongestinferencepro- CPRisonly0.330—two-thirdsofPIIsremaininfer-
tection (CPR/IPR 0.870/0.897) through iterative abledespitevirtuallycompletespanremoval. LLM-
adversarial refinement, but with moderate utility based methods generally show smaller gaps on
trade-off. TAB,suggestinginstruction-followingmodelsbet-
Backbone Comparison. GPT-4.1 leads in both teridentifycontextualcues. Theseresultsdemon-
span-basedandinference-basedprotection,while stratethatinference-basedmetricsareessentialfor
smallerbackbonemodelsshowcompetitiveresults capturingresidualprivacyrisks.
inspecificcases—Llama-3.1-8Bachievesthehigh-
est1-AAC(0.819)underDeID-GPT.However,this 6.2 Target-Subject-FocusedApproaches
reflects effective literal category-based masking UnderestimateMulti-SubjectPrivacy
on short PANORAMA texts rather than superior Risks
anonymizationcapability(seeAppendixE.5). For
On TAB (avg. 4.07 subjects per document), AA
utility,Claude-Haikuachievesstrongscores(upto
shows1-AAChigherthanCPRinmostconfigura-
0.947),whileGPT-4.1showslowerutilitydespite
tions (Figure 4). We draw two observations: (1)
itsstrongprivacyprotection,indicatingaprivacy-
Target-subject-focused anonymization creates
utilitytrade-off.
protection inequality. Across 5 of 6 backbones,
AA shows 1-AAC exceeding CPR, with up to 11
6 Analysis percentage points gap (Claude-Sonnet: 0.472 vs
0.362),indicatingthatnon-targetsubjectsreceive
6.1 HighSpanMaskingDoesNotGuarantee
substantiallylowerprotectionthanthedesignated
InferenceProtection
targetsubject. (2)Subject-agnosticmethodscan
AsshowninFigure3,span-basedmetricsarecon- achievebettercollectiveprotection. DeID-GPT
sistentlyhigherthaninference-basedmetricsacross with GPT-4.1 achieves CPR of 0.674, surpassing
all methods and backbones. We identify two key AA’s0.359withthesamebackbone. Thiscounter-
findings: (1)Thespan-inferencegapissubstan- intuitiveresultsuggeststhatiterativeoptimization
tial and universal. Across all 19 configurations, for the target subject may compromise collective
thegaprangesfrom0.10to0.61,presentevenin protection by preserving contextual information
17106

1.0
0.8
0.6
0.4
0.2
0.0
LF
AMARONAP
erocS
Longformer DeID-GPT DP-Prompt Adversarial Anonymization
1.0 1.0 1.0
0.8 0.8 0.8
0.6 0.6 0.6
0.4 0.4 0.4
0.2 0.2 0.2
0.0 0.0 0.0
Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5 Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5 Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5
1.0
0.8
0.6
0.4
0.2
0.0
LF
BAT erocS
Span-based Inference-based
Longformer DeID-GPT DP-Prompt Adversarial Anonymization
1.0 1.0 1.0
0.8 0.8 0.8
0.6 0.6 0.6
0.4 0.4 0.4
0.2 0.2 0.2
0.0 0.0 0.0
Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5 Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5 Llama-3.1 Gemma-3 GPT-4.1-Mini GPT-4.1 Haiku-4.5 Sonnet-4.5
Figure3: Per-backbonecomparisonofspan-basedandinference-basedmetricaveragesacrossfouranonymization
techniques(columns)andtwodatasets(rows). Span-basedmetricsconsistentlyexceedinference-basedmetrics
across all configurations, with larger gaps on TAB than PANORAMA. Longformer uses a single model; other
methodsshowresultsforsixLLMbackbones.
1.0
0.8
0.6
0.4
0.2
Llama-3.1-8B Gemma-3-27B GPT-4.1-Mini GPT-4.
C
1 laude-Haiku-4
C
.
l
5 aude-Sonnet-4.5
erocS
(a) PANORAMA
1.0
0.83 0.87 0.85
0.70 0.76 0.71 0.80 0.74 0.79 0.73 0.79 0.79 0.8
0.6
0.4
0.2
Llama-3.1-8B Gemma-3-27B GPT-4.1-Mini GPT-4.
C
1 laude-Haiku-4
C
.
l
5 aude-Sonnet-4.5
erocS
1-AAC (Single-subject) CPR (Multi-subject)
(b) TAB
0.510.51
0.48 0.43 0.45 0.47
0.40
0.34 0.36 0.34 0.36
0.31
Figure4: Comparisonofsingle-subject(1-AAC)andmulti-subject(CPR)metricsfortheAdversarialAnonymiza-
tiontechniqueacross6LLMbackbones. OnTAB,1-AACexceedsCPR,revealingthatnon-targetsubjectsare
inadequatelyprotected. OnPANORAMA,thepatternreverseswithCPRexceeding1-AAC.
aboutnon-targetsubjects. Theseresultshighlight three of four methods fail to protect higher-
theneedforanonymizationstrategiesthatexplicitly HardnessPIIs(levels4–5)aseffectivelyaslower-
protectallsubjectspresent. Hardness ones, while PANORAMA maintains
consistent protection across levels. See Ap-
6.3 AnonymizationEffectivenessVaries pendix E for further analysis. (2) The single-
SubstantiallyAcrossDomains subject vs multi-subject protection pattern re-
verses across domains. TAB shows 1-AAC
Comparing PANORAMA (avg. 260 chars) and
higherthanCPR,whilePANORAMAshowsCPR
TAB (avg. 3,918 chars), we observe domain-
exceeding 1-AAC by 5.8–9.4 percentage points.
dependentpatterns: (1)Thespan-inferencegap This reflects structural differences: TAB’s legal
varies by domain characteristics. The gap documents describe parties independently, while
is consistently larger on TAB (0.31–0.61) than
PANORAMA’sauthor-centriccontentinterweaves
PANORAMA(0.10–0.29),attributabletoTABcon-
subjects—anonymizing“MarriedlifewithLisa”to
taining exclusively NON-CODE PIIs (100% vs
“Lifewithothers”inherentlyprotectsrelatedindi-
81%) where removing inference cues is harder,
viduals. Thesefindingssuggestthatanonymization
combined with 15 longer documents provid-
effectiveness depends substantially on document
×
ing more inferential context. Moreover, on TAB,
17107

characteristics including length, PII distribution, InterdependenceofPIICategoriesandSubject
andnarrativestructure. Evaluation. Thisstudyuses15PIIcategoriesfrom
priorresearch(Staabetal.,2024;Pilánetal.,2022).
| 7 Conclusion |     |     |     |     |     |     | However, | reducing | PII       | categories | could | exclude |
| ------------ | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | ---------- | ----- | ------- |
|              |     |     |     |     |     |     | subjects | with no  | remaining | inferable  | PIIs; | future  |
WeintroduceSPIA,thefirstbenchmarkforsubject-
|               |     |            |     |      |                |     | work could | decouple | subject | identification |     | from |
| ------------- | --- | ---------- | --- | ---- | -------------- | --- | ---------- | -------- | ------- | -------------- | --- | ---- |
| level privacy |     | evaluation | in  | text | anonymization, |     |            |          |         |                |     |      |
PII-basedscoringtoaddressthis.
| comprising   | 675 | documents |          | with | 1,712   | subjects |           |     |                 |     |     |           |
| ------------ | --- | --------- | -------- | ---- | ------- | -------- | --------- | --- | --------------- | --- | --- | --------- |
|              |     |           |          |      |         |          | Ambiguity | in  | PII Attribution |     | to  | Subjects. |
| across legal | and | online    | domains. |      | Through | ex-      |           |     |                 |     |     |           |
Subject-levelevaluationrequiresattributingeach
| periments                             | with    | 4 anonymization |       |           | methods   | and 6 |                               |          |           |            |                  |             |
| ------------------------------------- | ------- | --------------- | ----- | --------- | --------- | ----- | ----------------------------- | -------- | --------- | ---------- | ---------------- | ----------- |
|                                       |         |                 |       |           |           |       | PII to a                      | specific | subject,  | which      | may be           | ambigu-     |
| LLMbackbones,wedrawthreemainfindings: |         |                 |       |           |           | (1)   |                               |          |           |            |                  |             |
|                                       |         |                 |       |           |           |       | ouswhencontextisinsufficient. |          |           |            | Carefulguideline |             |
| High span                             | masking | does            | not   | guarantee | inference |       |                               |          |           |            |                  |             |
|                                       |         |                 |       |           |           |       | design is                     | needed   | to ensure | consistent |                  | attribution |
| protection—even                       |         | with            | 99.7% | entity    | recall,   | two-  |                               |          |           |            |                  |             |
acrossannotatorsandmodels.
| thirdsofPIIsremaininferable.                  |     |     |     | (2)Single-subject- |     |     |           |        |      |       |        |         |
| --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --------- | ------ | ---- | ----- | ------ | ------- |
|                                               |     |     |     |                    |     |     |           |        | This | study | covers | two do- |
| focusedanonymizationcreatesprotectioninequal- |     |     |     |                    |     |     | Scope and | Scale. |      |       |        |         |
mains,legaldocuments(TAB)andonlinecontent
ity,leavingnon-targetsubjectsupto11percentage
|                      |     |     |                            |     |     |     | (PANORAMA), |     | across | diverse | cultural | contexts. |
| -------------------- | --- | --- | -------------------------- | --- | --- | --- | ----------- | --- | ------ | ------- | -------- | --------- |
| pointslessprotected. |     |     | (3)Anonymizationeffective- |     |     |     |             |     |        |         |          |           |
nessvariessubstantiallyacrossdomains,requiring However, the 675-document scale is constrained
|                                   |     |               |            |                     |            |        | by the high                              | cost  | of subject-level |           | annotation, | and  |
| --------------------------------- | --- | ------------- | ---------- | ------------------- | ---------- | ------ | ---------------------------------------- | ----- | ---------------- | --------- | ----------- | ---- |
| domain-awareevaluationapproaches. |     |               |            |                     | Thesefind- |        |                                          |       |                  |           |             |      |
|                                   |     |               |            |                     |            |        | only English                             | texts | are              | analyzed. | Different   | lan- |
| ings underscore                   |     | the necessity |            | of inference-based, |            |        |                                          |       |                  |           |             |      |
|                                   |     |               |            |                     |            |        | guagespresentuniquePIIinferencepathways: |       |                  |           |             | for  |
| multi-subject                     |     | evaluation    | frameworks |                     | that       | go be- |                                          |       |                  |           |             |      |
instance,pro-droplanguagessuchasKoreanand
| yond span-based |     | metrics.   |     | We envision   |     | SPIA as |                                 |     |     |     |               |     |
| --------------- | --- | ---------- | --- | ------------- | --- | ------- | ------------------------------- | --- | --- | --- | ------------- | --- |
|                 |     |            |     |               |     |         | Japanesefrequentlyomitsubjects, |     |     |     | increasingthe |     |
| a foundation    | for | developing |     | anonymization |     | tech-   |                                 |     |     |     |               |     |
difficultyofsubjectboundarydetection,whileEast
niquesthatensureequitableprivacyprotectionfor
allindividualsinadocument,andreleasethebench- Asianhonorificsystemsimplicitlyencodeageand
|     |     |     |     |     |     |     | socialrelationshipsbetweensubjects. |     |     |     | Beyondlan- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ---------- | --- |
markandevaluationframeworktosupportcontin-
guage,extendingtootherdomainswouldrequire
uedresearchinthisdirection.
|     |     |     |     |     |     |     | domain-specific |     | adaptation: | clinical   | notes | would |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ---------- | ----- | ----- |
|     |     |     |     |     |     |     | require mapping |     | to PHI      | categories | under | HIPAA |
Limitations
regulations,whileaudiotranscriptswouldnecessi-
| ExclusionofCollectiveReferences. |     |     |     |     | Ourannota- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
tatespeakerdiarizationasapreprocessingstepfor
tionfocusesonquantifiableindividuals,excluding subjectidentification.
collectivereferenceswithoutspecifiedcounts(e.g.,
“citizensofLA”).UnderGDPR(EuropeanUnion,
Reproducibility
2016),suchgroupmentionscanstillenableindivid-
ualidentificationwhencombinedwithadditional Toensurethereproducibilityofthisstudy,were-
leasethefollowingmaterials.
context(e.g.,insmallorganizations).
EqualTreatmentofPIIRisk. TheIPRandCPR CodeandExperimentScripts. Allcode, exper-
metrics proposed in this study treat all PII cat- iment scripts, and configuration files used in this
egories with equal weight. However, actual re- studyarepubliclyavailableatthefollowingrepos-
identificationriskvariesbyPIItype—forexample, itory: https://github.com/maisonOP/spia.g
it
aCPRof0.8carriessubstantiallydifferentriskif . Therepositoryincludes(1)implementationsof
theexposed20%consistsofdirectidentifiers(e.g., 4anonymizationtechniques,(2)subject-levelPII
inferencepipeline,(3)CPR/IPR/1-AACevaluation
| SSN, passport |     | numbers) | versus | quasi-identifiers |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(e.g., gender, age group). Furthermore, combi- scripts,and(4)utilityevaluationtools.
nations of quasi-identifiers (e.g., gender + age + Dataset. We release the SPIA benchmark
residence)canenablere-identificationevenwhen dataset, comprising TAB (144 documents) and
individualPIIsseembenign. Futureworkcouldde- PANORAMA (531 documents), along with per-
velopmetricsthatapplyriskweightsbyPIItypeor subject Ground Truth annotations. TAB is de-
modelcombinatorialre-identificationriskfroma rived from Pilán et al. (2022) (MIT License) and
k-anonymityperspective(Sweeney,2002). Forde- PANORAMAfromSelvamandGhosh(2025)(CC
ploymentscenarios,werecommendsupplementary BY 4.0 License), with original copyright notices
| analysisstratifiedbyPIIsensitivitytiers. |     |     |     |     |     |     | preserved. |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
17108

Backbone Version Control. For API-accessed theGovernmentoftheRepublicofKorea.
backbones,versioncontrolisnotfullycontrollable;
| we have | documented |     | the backbone |     | versions | and |     |     |     |     |     |     |
| ------- | ---------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
References
APIcallsettingsatthetimeofexperimentsinthe
Appendix. Open-source backbones (Llama 3.1, Anthropic.2025. IntroducingClaudeSonnet4.5.
Gemma3,Qwen3,GPT-OSS)arerunlocally.
|                                                |     |     |                       |     |     |     | Iz Beltagy,       | Matthew     | E. Peters,                   |     | and Arman | Cohan. |
| ---------------------------------------------- | --- | --- | --------------------- | --- | --- | --- | ----------------- | ----------- | ---------------------------- | --- | --------- | ------ |
| ExperimentalSettings.                          |     |     | Allhyperparametersfor |     |     |     |                   |             |                              |     |           |        |
|                                                |     |     |                       |     |     |     | 2020.             | Longformer: | Thelong-documenttransformer. |     |           |        |
| anonymizationtechniques,evaluationsettings,and |     |     |                       |     |     |     | arXiv:2004.05150. |             |                              |     |           |        |
prompttemplatesaredocumentedintheAppendix.
|     |     |     |     |     |     |     | MircoBeltrame, | MauroConti, |     | PierpaoloGuglielmin, |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | -------------------- | --- | --- |
Inparticular,methodsarereproducedasfaithfully
|     |     |     |     |     |     |     | Francesco | Marchiori, | and | Gabriele |     | Orazi. 2024. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | --- | ------------ |
aspossibletotheoriginalpapersettings,andmodi-
|     |     |     |     |     |     |     | RedactBuster: | Entitytyperecognitionfromredacted |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------------------- | --- | --- | --- | --- |
ficationsmadeinthisstudy(suchasapplyingthe documents. InComputerSecurity–ESORICS2024,
TAB8-categorysystem)areexplicitlydescribed. volume14983ofLectureNotesinComputerScience,
pages451–470.Springer.
EthicalConsiderations
|     |     |     |     |     |     |     | CaliforniaLegislature.2018. |     |     | Californiaconsumerpri- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ---------------------- | --- | --- |
vacyact(CCPA).
Bothdatasetsusedinthisstudyaredesignedwith
privacyprotectionconsiderations. Annotationwas Nicholas Carlini, Florian Tramer, Eric Wallace,
|           |     |         |         |                |     |     | Matthew | Jagielski,    | Ariel | Herbert-Voss, |      | Katherine |
| --------- | --- | ------- | ------- | -------------- | --- | --- | ------- | ------------- | ----- | ------------- | ---- | --------- |
| conducted | by  | privacy | experts | and university |     | re- |         |               |       |               |      |           |
|           |     |         |         |                |     |     | Lee,    | Adam Roberts, | Tom   | Brown,        | Dawn | Song, Úl- |
searchersfromconsortiuminstitutions,participat-
farErlingsson,AlinaOprea,andColinRaffel.2021.
ingaspartofagovernment-fundedresearchproject Extracting training data from large language mod-
withcompensationcoveredbytheprojectgrant. els. In Proceedings of the 30th USENIX Security
PANORAMAconsistsentirelyofsyntheticdata, Symposium,pages2633–2650.
withallprofilesandPIIsunrelatedtorealindividu-
|     |     |     |     |     |     |     | Yizhuo | Chen, Chun-Fu | Chen, | Hsiang |     | Hsu, Shao- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | ----- | ------ | --- | ---------- |
alsoractualrecords. Theentirepipelinefrompro- han Hu, Marco Pistoia, and Tarek F. Abdelzaher.
filegenerationtocontentgenerationiscomposed 2024. MaSS:Multi-attributeselectivesuppression
|     |     |     |     |     |     |     | for utility-preserving |     | data | transformation |     | from an |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ---- | -------------- | --- | ------- |
ofmodel-basedgenerationandconstraint-basedse-
|          |              |            |     |                 |     |     | information-theoreticperspective. |     |     |     | InProceedingsof |     |
| -------- | ------------ | ---------- | --- | --------------- | --- | --- | --------------------------------- | --- | --- | --- | --------------- | --- |
| lection, | structurally | preventing |     | the possibility |     | of  |                                   |     |     |     |                 |     |
the41stInternationalConferenceonMachineLearn-
| including | real | personal | information |     | (Selvam | and |     |     |     |     |     |     |
| --------- | ---- | -------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ing,volume235ofProceedingsofMachineLearning
Ghosh,2025). Therefore,itcanbesafelyusedin Research,pages6519–6538.PMLR.
environmentswherePIIresearchisneededbutuse
|     |     |     |     |     |     |     | Tobias Deußer, | Lorenz | Sparrenberg, |     | Armin | Berger, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | ------------ | --- | ----- | ------- |
ofactualpersonalinformationisprohibited.
MaxHahnbück,ChristianBauckhage,andRafetSifa.
TABisconstructedusingonlyjudgmentsforwhich 2025. Asurveyoncurrenttrendsandrecentadvances
InProceedingsoftheIEEE
the European Court of Human Rights (ECHR) intextanonymization.
InternationalConferenceonBigData.IEEE.
legallymandatespublicationandhasreceivedex-
| plicit consent |     | from applicants. |     | The | ECHR | sep- |     |     |     |     |     |     |
| -------------- | --- | ---------------- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
JosepDomingo-Ferrer,DavidSánchez,andJordiSoria-
aratelyde-identifiesorexcludesfrompublication Comas. 2016. Database Anonymization: Privacy
Models,DataUtility,andMicroaggregation-based
sensitivecasesorthoserequiringanonymizationbe-
|     |     |     |     |     |     |     | Inter-modelConnections. |     |     | SynthesisLecturesonIn- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------------------- | --- | --- |
forethepublicationstage,sodocumentsincluded formationSecurity,Privacy,andTrust.SpringerIn-
| in TAB | have | minimized | risk | of personal |     | infor- |     |     |     |     |     |     |
| ------ | ---- | --------- | ---- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
ternationalPublishing,Cham.
| mation | exposure. | Additionally, |     | the | TAB annota- |     |               |                |     |     |              |     |
| ------ | --------- | ------------- | --- | --- | ----------- | --- | ------------- | -------------- | --- | --- | ------------ | --- |
|        |           |               |     |     |             |     | CynthiaDwork, | FrankMcSherry, |     |     | KobbiNissim, | and |
tionprocessprovidedguidelinestobasemasking
|           |      |             |           |     |              |     | AdamSmith.2006.        |     | Calibratingnoisetosensitivity |     |     |     |
| --------- | ---- | ----------- | --------- | --- | ------------ | --- | ---------------------- | --- | ----------------------------- | --- | --- | --- |
| decisions | only | on publicly | inferable |     | information, |     |                        |     |                               |     |     |     |
|           |      |             |           |     |              |     | inprivatedataanalysis. |     | InTheoryofCryptography,       |     |     |     |
structurally preventing re-identification possibili- pages265–284,Berlin,Heidelberg.Springer.
tiesbasedonnon-publicinformation(Pilánetal.,
MarkElliot,ElaineMackey,andKieronO’Hara.2020.
2022).
|     |     |     |     |     |     |     | The Anonymisation |       | Decision-Making |     |     | Framework, |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | --------------- | --- | --- | ---------- |
|     |     |     |     |     |     |     | 2ndedition.       | UKAN. |                 |     |     |            |
Acknowledgments
|           |     |           |     |         |              |     | EuropeanUnion.2016. |     | Generaldataprotectionregula- |     |     |     |
| --------- | --- | --------- | --- | ------- | ------------ | --- | ------------------- | --- | ---------------------------- | --- | --- | --- |
| This work | was | supported | in  | part by | the Personal |     | tion(GDPR).         |     |                              |     |     |     |
InformationProtectionCommissionandtheKorea
LiFei,YejeeKang,SeoyoonPark,YeonjiJang,Jongkyu
Internet&SecurityAgency(KISA),Republicof
|     |     |     |     |     |     |     | Lee,andHansaemKim.2024. |     |     | KDPII:Anewkorean |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------------- | --- | --- |
Korea,underProject2780000030;andinpartby dialogicdatasetforthedeidentificationofpersonally
17109

identifiableinformation. IEEEAccess,12:135626– informationinlanguagemodels. In2023IEEESym-
| 135641. |     |     |     |     |     | posiumonSecurityandPrivacy(SP),pages346–363. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
IEEE.
AhmedFrikha,NassimWalha,KrishnaKanthNakka,
| Ricardo | Mendes,      | Xue | Jiang,                       | and Xuebing | Zhou. |                         |       |            |       |          |            |            |
| ------- | ------------ | --- | ---------------------------- | ----------- | ----- | ----------------------- | ----- | ---------- | ----- | -------- | ---------- | ---------- |
|         |              |     |                              |             |       | Benet Manzanares-Salor, |       |            | David | Sánchez, |            | and Pierre |
| 2024.   | IncogniText: |     | Privacy-enhancingconditional |             |       |                         |       |            |       |          |            |            |
|         |              |     |                              |             |       | Lison.                  | 2024. | Evaluating |       | the      | disclosure | risk of    |
textanonymizationviaLLM-basedprivateattribute anonymizeddocumentsviaamachinelearning-based
randomization. InNeurIPS2024WorkshoponSafe re-identificationattack. DataMiningandKnowledge
GenerativeAI.
Discovery,38(6):4040–4075.
| GemmaTeam.2025. |     | Gemma3technicalreport. |     |     | Com- |     |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
MarianaMonteiro,FilipeCorreia,PauloQueiroz,Rui
putingResearchRepository,arXiv:2503.19786.
Ramos,DinisTrigo,andGonçaloGonçalves.2024.
PhilippeGolle.2006. Revisitingtheuniquenessofsim- Patternsofdataanonymization. InProceedingsof
pledemographicsintheUSpopulation. InProceed- the29thEuropeanConferenceonPatternLanguages
ofPrograms,People,andPractices,EuroPLoP’24,
ingsofthe5thACMWorkshoponPrivacyinElec-
|     |     |     |     |     |     | pages | 1–9, New | York, | NY, | USA. | Association | for |
| --- | --- | --- | --- | --- | --- | ----- | -------- | ----- | --- | ---- | ----------- | --- |
tronicSociety,WPES’06,pages77–80,NewYork,
ComputingMachinery.
NY,USA.AssociationforComputingMachinery.
Aaron Grattafiori and 1 others. 2024. The Llama 3 OpenAI. 2025a. gpt-oss-120b & gpt-oss-20b
herd of models. Computing Research Repository, model card. Computing Research Repository,
| arXiv:2407.21783. |     |     |     |     |     | arXiv:2508.10925. |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
RajithaHathurusinghe,IsarNejadgholi,andMiodrag
|             |     |                                  |     |     |     | OpenAI.2025b. |     | IntroducingGPT-4.1intheAPI. |     |     |     |     |
| ----------- | --- | -------------------------------- | --- | --- | --- | ------------- | --- | --------------------------- | --- | --- | --- | --- |
| Bolic.2021. |     | Aprivacy-preservingapproachtoex- |     |     |     |               |     |                             |     |     |     |     |
tractionofpersonalinformationthroughautomatic Anthi Papadopoulou, Pierre Lison, Mark Anderson,
| annotation   | and      | federated | learning.  | In  | Proceedings  |                |     |              |        |                  |       |             |
| ------------ | -------- | --------- | ---------- | --- | ------------ | -------------- | --- | ------------ | ------ | ---------------- | ----- | ----------- |
|              |          |           |            |     |              | Lilja Øvrelid, |     | and          | Ildikó | Pilán.           | 2023. | Neural text |
| of the Third | Workshop |           | on Privacy | in  | Natural Lan- |                |     |              |        |                  |       |             |
|              |          |           |            |     |              | sanitization   |     | with privacy |        | risk indicators: |       | An em-      |
guageProcessing,pages36–45,Online.Association
|     |     |     |     |     |     | pirical | analysis. | Computing |     | Research |     | Repository, |
| --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | --- | -------- | --- | ----------- |
forComputationalLinguistics.
arXiv:2310.14312.
NeelKanwal,EmielA.M.Janssen,andKjerstiEngan.
|       |           |         |              |     |               | Ildikó Pilán, | Pierre | Lison, |     | Lilja | Øvrelid, | Anthi Pa- |
| ----- | --------- | ------- | ------------ | --- | ------------- | ------------- | ------ | ------ | --- | ----- | -------- | --------- |
| 2024. | Balancing | privacy | and progress |     | in artificial |               |        |        |     |       |          |           |
padopoulou,DavidSánchez,andMontserratBatet.
| intelligence:                   |     | Anonymization | in  | histopathology | for |             |          |               |                |     |           |        |
| ------------------------------- | --- | ------------- | --- | -------------- | --- | ----------- | -------- | ------------- | -------------- | --- | --------- | ------ |
|                                 |     |               |     |                |     | 2022.       | The text | anonymization |                |     | benchmark | (TAB): |
| biomedicalresearchandeducation. |     |               |     | InFrontiersof  |     |             |          |               |                |     |           |        |
|                                 |     |               |     |                |     | A dedicated |          | corpus        | and evaluation |     | framework | for    |
ArtificialIntelligence,Ethics,andMultidisciplinary
Applications, pages 417–429, Singapore. Springer text anonymization. Computational Linguistics,
| Nature. |     |     |     |     |     | 48(4):1053–1101. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Iyadh Ben Cheikh Larbi, Aljoscha Burchardt, and IldikóPilán,BenetManzanares-Salor,DavidSánchez,
Roland Roller. 2022. Which anonymization tech- and Pierre Lison. 2025. Truthful text sanitization
nique is best for which NLP task? – it depends. a guidedbyinferenceattacks. AppliedSoftComputing.
| systematicstudyonclinicaltextprocessing. |     |     |     |     | Comput- |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ingResearchRepository,arXiv:2209.00262. QwenTeam.2025. Qwen3technicalreport. Computing
ResearchRepository,arXiv:2505.09388.
| Pierre Lison, | Ildikó                | Pilán, | David | Sanchez,      | Montser- |             |        |            |     |     |                |     |
| ------------- | --------------------- | ------ | ----- | ------------- | -------- | ----------- | ------ | ---------- | --- | --- | -------------- | --- |
| ratBatet,     | andLiljaØvrelid.2021. |        |       | Anonymisation |          |             |        |            |     |     |                |     |
|               |                       |        |       |               |          | Luc Rocher, | Julien | Hendrickx, |     | and | Yves-Alexandre |     |
modelsfortextdata: Stateoftheart,challengesand de Montjoye. 2019. Estimating the success of re-
futuredirections. InProceedingsofthe59thAnnual identificationsinincompletedatasetsusinggenera-
| Meeting | of the | Association | for | Computational | Lin- |             |     |                                  |     |     |     |     |
| ------- | ------ | ----------- | --- | ------------- | ---- | ----------- | --- | -------------------------------- | --- | --- | --- | --- |
|         |        |             |     |               |      | tivemodels. |     | NatureCommunications,10(1):3069. |     |     |     |     |
guisticsandthe11thInternationalJointConference
| onNaturalLanguageProcessing(Volume1: |     |     |     |     | Long |        |        |     |         |     |        |       |
| ------------------------------------ | --- | --- | --- | --- | ---- | ------ | ------ | --- | ------- | --- | ------ | ----- |
|                                      |     |     |     |     |      | Sriram | Selvam | and | Anneswa |     | Ghosh. | 2025. |
Papers),pages4188–4203,Online.Associationfor
|     |     |     |     |     |     | PANORAMA: |     | A   | synthetic |     | PII-laced | dataset |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --------- | --- | --------- | ------- |
ComputationalLinguistics.
forstudyingsensitivedatamemorizationinLLMs.
ComputingResearchRepository,arXiv:2505.12238.
| Zhengliang | Liu, | Yue Huang, | Xiaowei | Yu, | Lu Zhang, |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ZihaoWu,ChaoCao,HaixingDai,LinZhao,Yiwei
HaoShen,ZhouhongGu,HaokaiHong,andWeiliHan.
Li,PengShu,FangZeng,LichaoSun,WeiLiu,Ding-
gang Shen, Quanzheng Li, Tianming Liu, Dajiang 2025. PII-Bench: Evaluating query-aware privacy
Zhu, and Xiang Li. 2023. DeID-GPT: Zero-shot protectionsystems. ComputingResearchRepository,
arXiv:2502.18545.
| medicaltextde-identificationbyGPT-4. |     |     |     |     | Computing |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ResearchRepository,arXiv:2303.11032.
RezaShokri,MarcoStronati,CongzhengSong,andVi-
NilsLukas,AhmedSalem,RobertSim,ShrutiTople, talyShmatikov.2017. Membershipinferenceattacks
Lukas Wutschitz, and Santiago Zanella-Béguelin. againstmachinelearningmodels. In2017IEEESym-
2023. Analyzingleakageofpersonallyidentifiable posiumonSecurityandPrivacy,pages3–18.
17110

RobinStaab,MarkVero,MislavBalunovic,andMar- Type Category PANORAMA TAB Total
| tinVechev.2024. |     | Beyondmemorization: |     |     | Violating |     |     |          |     |     |     |     |
| --------------- | --- | ------------------- | --- | --- | --------- | --- | --- | -------- | --- | --- | --- | --- |
|                 |     |                     |     |     |           |     |     | IDNumber |     | 95  | –   | 95  |
privacyviainferencewithlargelanguagemodels. In DriverLicense 75 – 75
The Twelfth International Conference on Learning CODE Phone 85 – 85
|     |     |     |     |     |     |     |     | Passport |     | 31  | –   | 31  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
Representations,pages33832–33878.
|     |     |     |     |     |     |     |     | Email |     | 90  | –   | 90    |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     |     | Name  |     | 691 | 366 | 1,057 |
RobinStaab,MarkVero,MislavBalunovic,andMar-
|                                              |       |                                  |        |     |              |     |          | Sex         |     | 556 | 392 | 948 |
| -------------------------------------------- | ----- | -------------------------------- | ------ | --- | ------------ | --- | -------- | ----------- | --- | --- | --- | --- |
| tin Vechev.                                  | 2025. | Language                         | models |     | are advanced |     |          |             |     |     |     |     |
|                                              |       |                                  |        |     |              |     |          | Age         |     | 159 | 153 | 312 |
|                                              |       |                                  |        |     |              |     |          | Location    |     | 452 | 510 | 962 |
| anonymizers.                                 |       | InTheThirteenthInternationalCon- |        |     |              |     |          |             |     |     |     |     |
|                                              |       |                                  |        |     |              |     |          | Nationality |     | 452 | 519 | 971 |
| ferenceonLearningRepresentations,pages98558– |       |                                  |        |     |              |     | NON-CODE |             |     |     |     |     |
|                                              |       |                                  |        |     |              |     |          | Education   |     | 101 | 294 | 395 |
98598.
|     |     |     |     |     |     |     |     | Relationship |     | 254 | 55  | 309 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | Occupation   |     | 441 | 453 | 894 |
AmberStubbsandÖzlemUzuner.2015. Annotating Affiliation 193 292 485
|     |     |     |     |     |     |     |     | Position |     | 15  | 316 | 331 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
longitudinalclinicalnarrativesforde-identification:
The2014i2b2/UTHealthcorpus. JournalofBiomed- Total 3,690 3,350 7,040
icalInformatics,58(Suppl):S20–S29.
|     |     |     |     |     |     |     | Table5: PIIcategoryfrequencydistributionacrossTAB |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
Latanya Sweeney. 2000. Simple demographics often andPANORAMAdatasets. TABisdominatedbyNON-
identify people uniquely. Health (San Francisco), CODEtypePIIs(Name,Location,Occupation),while
| 671. |     |     |     |     |     |     | PANORAMAincludesCODE-typePIIs(Email,Phone) |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
thatareabsentinTAB.
| LatanyaSweeney.2002.                          |     | k-anonymity:                       |     | Amodelforpro- |     |     |           |          |     |     |             |     |
| --------------------------------------------- | --- | ---------------------------------- | --- | ------------- | --- | --- | --------- | -------- | --- | --- | ----------- | --- |
| tectingprivacy.                               |     | InternationalJournalofUncertainty, |     |               |     |     |           |          |     |     |             |     |
| FuzzinessandKnowledge-BasedSystems,10(5):557– |     |                                    |     |               |     |     |           |          |     |     | SPIA(Total) |     |
|                                               |     |                                    |     |               |     |     | #Subjects | PANORAMA |     | TAB |             |     |
570.
|     |     |     |     |     |     |     | 1   | 175(33.0%) |     | -   | 175(25.9%) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- |
Saiteja Utpala, Sara Hooker, and Pin-Yu Chen. 2023. 2 233(43.9%) 22(15.3%) 255(37.8%)
|            |                |               |              |          |            |         | 3   | 58(10.9%) |     | 35(24.3%) |     | 93(13.8%) |
| ---------- | -------------- | ------------- | ------------ | -------- | ---------- | ------- | --- | --------- | --- | --------- | --- | --------- |
| Locally    | differentially | private       | document     |          | generation |         |     |           |     |           |     |           |
|            |                |               |              |          |            |         | 4   | 24(4.5%)  |     | 30(20.8%) |     | 54(8.0%)  |
| using zero | shot           | prompting.    | In           | Findings | of         | the As- |     |           |     |           |     |           |
|            |                |               |              |          |            |         | 5+  | 41(7.7%)  |     | 57(39.6%) |     | 98(14.5%) |
| sociation  | for            | Computational | Linguistics: |          | EMNLP      |         |     |           |     |           |     |           |
2023,pages8442–8457,Singapore.Associationfor Total 531 144 675
| ComputationalLinguistics. |     |     |     |     |     |     | Average                                        |     | 2.12 | 4.07 |     | 2.54 |
| ------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | ---- | ---- | --- | ---- |
|                           |     |     |     |     |     |     | Table6: DistributionofNumberofSubjectsperDocu- |     |      |      |     |      |
ShangWang,TianqingZhu,BoLiu,MingDing,Day-
ongYe,WanleiZhou,andPhilipYu.2025a. Unique ment. TABshowshighersubjectcountsduetomulti-
securityandprivacythreatsoflargelanguagemodel: party legal proceedings, while PANORAMA covers
| Acomprehensivesurvey. |     |     | ACMComputingSurveys, |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
singletomulti-subjectonlinetexts.
58(4):83:1–83:36.
| Xinyi Wang, | Antonis | Antoniades, |     | Yanai | Elazar, | Al- |     |     |     |     |     |     |
| ----------- | ------- | ----------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
fonsoAmayuelas,AlonAlbalak,KexunZhang,and A.1 PIICategoryDistribution
| William | Yang | Wang. 2025b. |     | Generalization |     | v.s. |     |     |     |     |     |     |
| ------- | ---- | ------------ | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
memorization: Tracing language models’ capabil- Table5showsthefrequencyofeachPIIcategory
| itiesbacktopretrainingdata. |     |     | ComputingResearch |     |     |     |        |               |     |           |     |          |
| --------------------------- | --- | --- | ----------------- | --- | --- | --- | ------ | ------------- | --- | --------- | --- | -------- |
|                             |     |     |                   |     |     |     | in TAB | and PANORAMA. |     | CODE-type |     | PIIs (ID |
Repository,arXiv:2407.14985.
Number,DriverLicense,Phone,Passport,Email)
TianyuYang,XiaodanZhu,andIrynaGurevych.2025. appearonlyinPANORAMA,whileNON-CODE-
Robustutility-preservingtextanonymizationbased typePIIsaredistributedacrossbothdatasetswith
| on large | language | models. | In  | Proceedings |     | of the |     |     |     |     |     |     |
| -------- | -------- | ------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
differentpatternsreflectingtheirdomaincharacter-
63rdAnnualMeetingoftheAssociationforCompu-
istics.
| tationalLinguistics(Volume1: |     |     |     | LongPapers),pages |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
28922–28941,Vienna,Austria.AssociationforCom-
putationalLinguistics.
|     |     |     |     |     |     |     | A.2 SubjectDistribution |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
HannaYukhymenko,RobinStaab,MarkVero,andMar-
| tin Vechev.         | 2024. | A synthetic                 |     | dataset | for personal |     |          |               |              |              |            |       |
| ------------------- | ----- | --------------------------- | --- | ------- | ------------ | --- | -------- | ------------- | ------------ | ------------ | ---------- | ----- |
|                     |       |                             |     |         |              |     | Table 6  | shows the     | distribution | of           | the number | of    |
| attributeinference. |       | AdvancesinNeuralInformation |     |         |              |     |          |               |              |              |            |       |
|                     |       |                             |     |         |              |     | subjects | per document. |              | In PANORAMA, |            | docu- |
ProcessingSystems,37:120735–120779.
mentswith1-2subjectsaccountfor76.9%,while
|     |     |     |     |     |     |     | in TAB, | documents | with | 5 or more | subjects | ac- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ---- | --------- | -------- | --- |
A DatasetStatistics
countfor39.6%,focusingonmulti-subjectscenar-
This appendix presents detailed statistics of the ios. The average number of subjects across the
| SPIAdatasetmentionedinSection3. |     |     |     |     |     |     | entireSPIAdatasetis2.54. |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
17111

#PIIs PANORAMA TAB SPIA(Total) • Level1: “Thecaseoriginatedinanapplication
1 159(14.1%) 10(1.7%) 169(9.9%) againsttheKingdomofSwedenlodgedwiththe
2 229(20.3%) 19(3.2%) 248(14.5%)
Court by a Swedish national, Mr Raja Arlewin
3 360(32.0%) 34(5.8%) 394(23.0%)
4 135(12.0%) 46(7.8%) 181(10.6%) (‘theapplicant’),on18March2010.” Name:
5 93(8.3%) 107(18.3%) 200(11.7%) →
RajaArlewin
6 88(7.8%) 190(32.4%) 278(16.2%)
7 45(4.0%) 107(18.3%) 152(8.9%)
8+ 17(1.5%) 73(12.4%) 90(5.3%) • Level2: “Theapplicantisbornin1970andlives
TotalSubjects 1,126 586 1,712 inStockholm.” Age: 54-55(calculatedfrom
Average 3.28 5.72 4.11 →
birthyear1970relativetoreferencedateSeptem-
ber1,2025)
Table 7: Distribution of Number of PIIs per Subject.
Mostsubjectshave2–6inferablePIIs,providingsuffi-
• Level 3: “Username: Ridhi, Location: Sam-
cientsignalforinference-basedevaluationwhilereflect-
balpur... Stopped by this modest cafe near my
ingrealisticprivacyexposurescenarios.
workplace.” Nationality: India(requiresrec-
→
ognizing“Ridhi”asanIndian-originnameand
A.3 PIIperSubject combiningitwiththelocationcontext)
Table 7 shows the distribution of PIIs per sub-
• Level 4: “The President of the Fourth Section
ject. TAB contains an average of 5.72 PIIs per
decided to communicate the application to the
subject, providing richer PII information than
Government.” Occupation: Judge(requires
PANORAMA (3.28). This is because legal doc- →
knowledgethatthePresidentoftheFourthSec-
umentsrecorddetailedpersonalinformationofthe
tionatECHRisajudge)
partiesinvolved.
• Level 5: “The applicant is represented by Mr
A.4 CertaintyandHardnessDistribution
MahmutAkdog˘an,alawyerpractisinginMersin.”
Figures5and6showthedistributionofCertainty Education: CollegeDegree(requiressearch-
→
andHardnesslevelsforallPIIs,respectively. Cer- ingTurkishbaradmissionrequirementsandsyn-
taintymeasurestheconfidencelevelforinferring thesizingthatlawyersmustholdalawdegree)
PII from text on a 5-point scale from 1 (very un-
certain)to5(verycertain). Hardnessmeasuresthe CertaintyLevelExamples
cognitivedifficultyrequiredtoinferthePIIona5-
• Level5: “...aSwedishnational,MrRajaArlewin
pointscalefrom1(veryeasy)to5(verydifficult).
(‘theapplicant’).” Name: RajaArlewin(the
→
nameisexplicitlystatedwithnoambiguity)
A.5 DocumentLengthDistribution
Figure 7 shows the document length distribution • Level 4: “He is self-employed and runs a
bydataset. PANORAMAconsistsofshortonline business.” Occupation: Business owner
→
content averaging 260 characters (99.6% within (strongly implied, though the specific business
500characters),whileTABconsistsoflonglegal typeisnotstated)
documents averaging 3,918 characters (64.6% in
the2,000–5,000characterrange). Thisdifference • Level3: “...MrJ.Södergren,alawyerpractising
reflectstheinherentcharacteristicsofthetwodo- inStockholm.” Nationality: Sweden(prac-
→
mains. ticesinStockholmsuggestsSwedishnationality,
butforeignlawyerscanalsopracticethere)
A.6 QualitativeExamples
• Level 2: “...with a job, a family and a fixed
This section presents qualitative examples for
abode.” Relationship: Married (having a
each Hardness level and Certainty level in the →
familysuggestsmarriage,butcouldrefertobe-
SPIAdataset. Hardnessscoresrangefrom1(very
ingasingleparent)
easy)to5(veryhard),whileCertaintyscoresrange
from 1 (very uncertain) to 5 (very certain). For • Level 1: “...the applicant and Eren Keskin.”
Hardnesslevels4-5,annotatorsarepermittedtouse Sex: Female (the name “Eren” is gender-
→
traditionalonlinesearchengines. SeeAppendixF ambiguousinTurkish;withoutanhonorific,in-
forthecompletegradingcriteria. ferenceishighlyuncertain)
HardnessLevelExamples
17112

3000
3000
2500
2500
2000
2000
tnuoC
| tnuoC |     |     |     |     | 1500 |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
1500
1000
1000
500
500
0
| 0   |     |     |     |     |     | 1   | 2   | 3              | 4   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
|     | 1   | 2 3 | 4   | 5   |     |     |     | Hardness Level |     |     |     |
Certainty Level
|          |                           |     |               |     | Figure6: | PIIHardnessdistribution. |     |     | MostPIIs(75.7%) |     |     |
| -------- | ------------------------- | --- | ------------- | --- | -------- | ------------------------ | --- | --- | --------------- | --- | --- |
| Figure5: | PIICertaintydistribution. |     | Themajorityof |     |          |                          |     |     |                 |     |     |
requirelowcognitiveefforttoinfer,suggestingthatad-
| PIIs(85.7%)haveCertainty |     |     | 3,meaningtheyhave |     |                                                  |     |     |     |     |     |     |
| ------------------------ | --- | --- | ----------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                          |     | ≥   |                   |     | versariescaneasilyinferPIIsfromthesetextswithout |     |     |     |     |     |     |
directorindirectevidenceinthetext.
sophisticatedreasoning.
| 35  |     |     |     | Mean: 257   |     |     |     |     |     |     | Mean: 3719   |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ------------ |
|     |     |     |     | Median: 266 |     |     |     |     |     |     | Median: 3360 |
12
30
10
25
| stnemucoD fo rebmuN |     |     |     |     | stnemucoD fo rebmuN |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
8
20
6
15
| 10    |             |                              |     |     | 4   |      |      |                              |      |     |       |
| ----- | ----------- | ---------------------------- | --- | --- | --- | ---- | ---- | ---------------------------- | ---- | --- | ----- |
| 5     |             |                              |     |     | 2   |      |      |                              |      |     |       |
| 0 100 | 200         | 300                          | 400 | 500 | 0   | 2000 | 4000 | 6000                         | 8000 |     | 10000 |
|       |             | Document Length (characters) |     |     |     |      |      | Document Length (characters) |      |     |       |
|       | (a)PANORAMA |                              |     |     |     |      |      | (b)TAB                       |      |     |       |
Figure7: Documentlengthdistribution. Forvisualizationclarity,afewoutliersareexcluded: onePANORAMA
documentexceeding1,500charactersandtwoTABdocumentsexceeding15,000characters.
Metric TAB PANORAMA Total with Staab et al. (2024, 2025), only labels with
| Documents |     | 144 | 151 | 295 | Certainty |     | 3areselectedforevaluation. |     |     |     |     |
| --------- | --- | --- | --- | --- | --------- | --- | -------------------------- | --- | --- | --- | --- |
≥
Num.ofSubjects 586 360 946 InferenceLLM.Weevaluate11LLMsattemper-
| AvgSubjects/Doc |     | 4.07 | 2.38 | 3.21 |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
3,350 1,201 4,551 ature 0.1 (Staab et al., 2024, 2025) to select the
Num.ofPIIs
|     |     | (3,064) | (943) | (4,007) |     |     |     |     |     |     |     |
| --- | --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
inferenceLLMforsubject-wisePIIextraction:
| AvgPIIs/Subject     |     | 5.72  | 3.34 | 4.81 |                |     |     |        |        |     |     |
| ------------------- | --- | ----- | ---- | ---- | -------------- | --- | --- | ------ | ------ | --- | --- |
| AvgDocLength(chars) |     | 3,918 | 265  | -    |                |     |     |        |        |     |     |
|                     |     |       |      |      | • Proprietary: |     |     | Claude | Sonnet |     | 4.5 |
claude-sonnet-4-5-20250929
Table 8: Test Set Basic Statistics. Numbers in ( ) and Claude
SPIA
|                                      |     |     |     |     | Haiku4.5( |     | claude-haiku-4-5-20251001 |     |     | )(An- |     |
| ------------------------------------ | --- | --- | --- | --- | --------- | --- | ------------------------- | --- | --- | ----- | --- |
| parenthesesindicatePIIswithCertainty |     |     |     | 3.  |           |     |                           |     |     |       |     |
≥
|     |     |     |     |     | thropic,2025);GPT-4.1( |     |     | gpt-4.1-2025-04-14 |     |     | )   |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | ------------------ | --- | --- | --- |
gpt-4.1-mini-2025-04-14
|     |     |     |     |     | andGPT-4.1mini( |     |     |     |     |     | )   |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
B DetailsofSubject-wiseInference
(OpenAI,2025b).
Validation
|     |     |     |     |     | • Open-source: |     |     | openai/gpt-oss-120b |     |     | and |
| --- | --- | --- | --- | --- | -------------- | --- | --- | ------------------- | --- | --- | --- |
Thisappendixpresentsdetailedexperimentalset-
|              |               |            |            |         | openai/gpt-oss-20b    |     |     | (OpenAI, |                 | 2025a); |     |
| ------------ | ------------- | ---------- | ---------- | ------- | --------------------- | --- | --- | -------- | --------------- | ------- | --- |
| tings        | and per-model | comparison | results    | for the |                       |     |     |          |                 |         |     |
|              |               |            |            |         | google/gemma-3-27b-it |     |     | and      | google/gemma-3- |         |     |
| subject-wise | inference     | framework  | validation | de-     |                       |     |     |          |                 |         |     |
4b-it(GemmaTeam,2025);meta-llama/Llama-
scribedinSection3.3.
|     |     |     |     |     | 3.1-70B-Instruct |     |     | and          | meta-llama/Llama- |             |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------ | ----------------- | ----------- | --- |
|     |     |     |     |     | 3.1-8B-Instruct  |     |     | (Grattafiori | et                | al., 2024); |     |
B.1 ExperimentalSetup
Qwen/Qwen3-14B(QwenTeam,2025).
| Evaluation | Dataset. | Manually | constructed | test |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
sets (TAB 144, PANORAMA 151) are used; de- EvaluatorLLM.GPT-4.1-Miniservesastheeval-
tailedstatisticsareprovidedinTable8. Consistent uatorLLMforsubjectalignmentandPIIcompari-
17113

| Model |     |     | SubjectMatch |     | PIIAcc. |     | Model |     |     | SubjectMatch |     | PIIAcc. |
| ----- | --- | --- | ------------ | --- | ------- | --- | ----- | --- | --- | ------------ | --- | ------- |
Claude-Sonnet-4.5 96.76% 91.12% Claude-Sonnet-4.5 96.66% 91.62%
| GPT-4.1          |     |     | 96.42% |     | 90.11% |     | GPT-OSS-120B     |     |             | 97.50% |     | 82.27% |
| ---------------- | --- | --- | ------ | --- | ------ | --- | ---------------- | --- | ----------- | ------ | --- | ------ |
| GPT-OSS-120B     |     |     | 94.20% |     | 88.82% |     | GPT-4.1          |     |             | 95.47% |     | 84.00% |
| Claude-Haiku-4.5 |     |     | 90.27% |     | 86.05% |     | Gemma-3-27B      |     |             | 95.28% |     | 74.58% |
| GPT-4.1-Mini     |     |     | 90.61% |     | 83.09% |     | GPT-4.1-Mini     |     |             | 92.50% |     | 76.08% |
| Llama-3.1-70B    |     |     | 88.91% |     | 66.83% |     | GPT-OSS-20B      |     |             | 91.39% |     | 72.88% |
| Gemma-3-27B      |     |     | 86.35% |     | 74.31% |     | Claude-Haiku-4.5 |     |             | 91.11% |     | 85.86% |
| GPT-OSS-20B      |     |     | 84.30% |     | 70.92% |     | Qwen-3-14B       |     |             | 85.00% |     | 63.68% |
| Qwen-3-14B       |     |     | 76.28% |     | 68.21% |     | Llama-3.1-70B    |     |             | 78.33% |     | 64.54% |
| Llama-3.1-8B     |     |     | 76.28% |     | 60.95% |     | Llama-3.1-8B     |     |             | 70.28% |     | 68.40% |
| Gemma-3-4B       |     |     | 67.92% |     | 51.31% |     | Gemma-3-4B       |     |             | 61.11% |     | 56.21% |
|                  |     |     | (a)TAB |     |        |     |                  |     | (b)PANORAMA |        |     |        |
Table 9: Subject-level Inference Performance. Subject Match=Subject Match Ratio, PII Acc.=PII Inference
Accuracy.
son,offeringfavorablecostandprocessingspeed. ficiently large models are required for accurate
subject-levelevaluation.
EvaluationMetrics.
• Subject Match Ratio: Matching success rate B.3 AnalysisbyPIICategory
betweengroundtruthsubjectsandLLM-inferred
Figure8showstheper-tagbreakdownofcorrectly
subjects
|     |     |     |     |     |     |     | inferredPIIsforeachmodel. |     |     |     | Humangroundtruth |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---------------- | --- |
representsthetotalPIIcountsinthegroundtruth,
| • InferenceAccuracy: |     |     | PIIinferenceaccuracyfor |     |     |     |             |      |      |     |        |              |
| -------------------- | --- | --- | ----------------------- | --- | --- | --- | ----------- | ---- | ---- | --- | ------ | ------------ |
|                      |     |     |                         |     |     |     | while other | bars | show | the | number | of PIIs each |
matchedsubjects(Top-1prediction)
|     |     |     |     |     |     |     | model correctly |          | inferred. | Figures | 9        | and 10 show |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | --------- | ------- | -------- | ----------- |
|     |     |     |     |     |     |     | the inference   | accuracy |           | by PII  | category | for each    |
B.2 ModelPerformanceOverview
model.
| Table 9   | shows                               | the subject-level |        | inference |          | perfor- |                             |     |     |     |     |     |
| --------- | ----------------------------------- | ----------------- | ------ | --------- | -------- | ------- | --------------------------- | --- | --- | --- | --- | --- |
| mance     | of 11 models                        |                   | on TAB | and       | PANORAMA |         |                             |     |     |     |     |     |
|           |                                     |                   |        |           |          |         | B.4 AnalysisbyHardnessLevel |     |     |     |     |     |
| datasets. | Claude-Sonnet-4.5achievesthehighest |                   |        |           |          |         |                             |     |     |     |     |     |
Figure11showstheinferenceaccuracybyHard-
| performance | on  | both | datasets | and is | therefore | se- |                                     |     |     |     |     |     |
| ----------- | --- | ---- | -------- | ------ | --------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|             |     |      |          |        |           |     | nesslevelforTABandPANORAMAdatasets. |     |     |     |     | A   |
lectedasthepre-labelingandanonymizationevalu-
decreasingtrendininferenceaccuracyisobserved
ationmodel.
asHardnessincreases,suggestingthatLLMinfer-
| Model | Scale and | Performance. |     | Overall, |     | larger |                  |     |          |     |                 |      |
| ----- | --------- | ------------ | --- | -------- | --- | ------ | ---------------- | --- | -------- | --- | --------------- | ---- |
|       |           |              |     |          |     |        | ence performance |     | degrades |     | for cognitively | more |
modelsshowhigherperformance,andproprietary
difficultPIIs.
| models     | outperform | open-source |             | models.     |     | Claude- |                     |     |     |     |     |     |
| ---------- | ---------- | ----------- | ----------- | ----------- | --- | ------- | ------------------- | --- | --- | --- | --- | --- |
| Sonnet-4.5 | achieves   |             | the highest | performance |     | on      |                     |     |     |     |     |     |
|            |            |             |             |             |     |         | C ExperimentDetails |     |     |     |     |     |
bothdatasetsandisselectedastheinferencemodel
| for subsequent |     | pre-labeling |     | and anonymization |     |     |               |     |           |     |          |            |
| -------------- | --- | ------------ | --- | ----------------- | --- | --- | ------------- | --- | --------- | --- | -------- | ---------- |
|                |     |              |     |                   |     |     | This appendix |     | describes | the | detailed | experimen- |
evaluation.
|         |                  |     |     |               |     |      | tal settings | and | evaluation |     | methodology | used in |
| ------- | ---------------- | --- | --- | ------------- | --- | ---- | ------------ | --- | ---------- | --- | ----------- | ------- |
| Dataset | Characteristics. |     |     | Both datasets |     | show |              |     |            |     |             |         |
Sections4and5.
| comparable | overall | performance. |     |     | TAB achieves |     |     |     |     |     |     |     |
| ---------- | ------- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
slightlyhigheraverageInferenceAccuracy(75.6% C.1 TestSetStatistics
| vs 74.6%), | while | PANORAMA |     | shows |     | slightly |     |     |     |     |     |     |
| ---------- | ----- | -------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
ThetestsetfromtheSPIAbenchmarkdescribed
| higher  | average    | Subject | Match     | Ratio           | (86.8% | vs  |                                |     |     |     |     |             |
| ------- | ---------- | ------- | --------- | --------------- | ------ | --- | ------------------------------ | --- | --- | --- | --- | ----------- |
|         |            |         |           |                 |        |     | inSection3isusedforevaluation. |     |     |     |     | Table8shows |
| 86.2%), | reflecting | the     | different | characteristics |        | of  |                                |     |     |     |     |             |
thebasicstatisticsofthetestset.
legaldocumentsversussocialmediatexts.
SubjectMatch
SubjectIdentificationCapability.
|     |     |     |     |     |     |     | C.2 HardwareandSoftware |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
RatioishigherthanInferenceAccuracyacrossall
models, suggesting that subject identification is ExperimentswereconductedonIntelXeonGold
relativelyeasierthanPIIinference. However,for 6448Y,221GBDDR5,NVIDIAH10080GBGPU
smaller models (8B and below), Subject Match environment. Python3.11+andCUDA12.2were
| Ratio also | drops | below | 85%, | indicating | that | suf- | used. |     |     |     |     |     |
| ---------- | ----- | ----- | ---- | ---------- | ---- | ---- | ----- | --- | --- | --- | --- | --- |
17114

3500
3000
2500
2000
1500
1000
500
0
Hu
ma
C
n laude-Sonnet-4.5 GPT-4.1 GPT-OSS-120B Claude-Haiku-4.5 GPT-4.1-Mini
Ge m
ma-3-27B GPT-OSS-20B Qwen-3-14B
Lla
ma-3-70B
Lla
ma-3-8B
Ge m
ma-3-4B
tnuoC
tcerroC
Nation. Position
Sex Affil.
Name Edu.
Loc. Age
Occup. Relation.
(a)TAB
1000
800
600
400
200
0
Hu
ma
C
n laude-Sonnet-4.5 GPT-4.1 GPT-OSS-120B Claude-Haiku-4.5
Ge m
ma-3-27B GPT-4.1-Mini GPT-OSS-20B
Lla
ma-3-8B
Lla
ma-3-70B Qwen-3-14B
Ge m
ma-3-4B
tnuoC
tcerroC
Name Email
Sex ID Num. Occup. Driver Lic.
Relation. Age
Nation. Edu.
Loc. Passport
Affil. Position
Phone
(b)PANORAMA
Figure 8: Per-tag inference accuracy counts. Each stacked bar shows the number of correctly inferred PIIs by
category.
C.3 Subject-levelInferenceEvaluation C.3.1 Subject-levelComparison
The adversarial LLM extracts subjects and PIIs
fromanonymizedtextusingthetwo-stageframe-
work(Section3.3): subjectidentificationfollowed
This section describes the detailed implementa- byPIIinferencefor15categories. Thepromptsare
tion of the 3-step evaluation pipeline defined in showninFigures24–26.
Section 4.2. Based on the validation results in One-to-one correspondence between Ground
AppendixB,Claude-Sonnet-4.5isselectedasthe Truthsubjects(annotatedonoriginaltext)andsub-
adversarialLLM,achievingthehighestInference jects identified from anonymized text is then es-
Accuracy (above 91%) and Subject Match Ra- tablished by the evaluator LLM based on subject
tio (above 96%) on both datasets. GPT-4.1-Mini descriptionsandthetextcontent. Anonymization
serves as the evaluator LLM, as used in frame- can remove explicit identifiers, so matching con-
work validation (Appendix B). Following prior sidersrolesandcontextualcuesinadditiontoex-
work(Staabetal.,2024,2025),onlyPIIswithCer- plicit mentions. Ground Truth subjects that fail
tainty 3areevaluated,usingthetop-1inference tomatchareassigned0.0pointsforallPIIs. The
≥
(themodel’ssinglebestguess)forcomparison. alignmentpromptformatchingsubjectsisshown
17115

|           | (a) Inference Accuracy for Claude-Sonnet-4.5 |         |           | (b) Inference Accuracy for GPT-4.1          |         |
| --------- | -------------------------------------------- | ------- | --------- | ------------------------------------------- | ------- |
| Name      |                                              |         | Name      |                                             |         |
| Sex       |                                              |         | Sex       |                                             |         |
| Age       |                                              |         | Age       |                                             |         |
| Loc.      |                                              |         | Loc.      |                                             |         |
| Nation.   |                                              |         | Nation.   |                                             |         |
| Edu.      |                                              |         | Edu.      |                                             |         |
| Relation. |                                              |         | Relation. |                                             |         |
| Occup.    |                                              |         | Occup.    |                                             |         |
| Affil.    |                                              |         | Affil.    |                                             |         |
| Position  |                                              |         | Position  |                                             |         |
| 0.0 0.2   | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2   | 0.4 0.6                                     | 0.8 1.0 |
|           | (c) Inference Accuracy for GPT-OSS-120B      |         |           | (d) Inference Accuracy for Claude-Haiku-4.5 |         |
| Name      |                                              |         | Name      |                                             |         |
| Sex       |                                              |         | Sex       |                                             |         |
| Age       |                                              |         | Age       |                                             |         |
| Loc.      |                                              |         | Loc.      |                                             |         |
| Nation.   |                                              |         | Nation.   |                                             |         |
| Edu.      |                                              |         | Edu.      |                                             |         |
| Relation. |                                              |         | Relation. |                                             |         |
| Occup.    |                                              |         | Occup.    |                                             |         |
| Affil.    |                                              |         | Affil.    |                                             |         |
| Position  |                                              |         | Position  |                                             |         |
| 0.0 0.2   | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2   | 0.4 0.6                                     | 0.8 1.0 |
|           | (e) Inference Accuracy for GPT-4.1-Mini      |         |           | (f) Inference Accuracy for Gemma-3-27B      |         |
| Name      |                                              |         | Name      |                                             |         |
| Sex       |                                              |         | Sex       |                                             |         |
| Age       |                                              |         | Age       |                                             |         |
| Loc.      |                                              |         | Loc.      |                                             |         |
| Nation.   |                                              |         | Nation.   |                                             |         |
| Edu.      |                                              |         | Edu.      |                                             |         |
| Relation. |                                              |         | Relation. |                                             |         |
| Occup.    |                                              |         | Occup.    |                                             |         |
| Affil.    |                                              |         | Affil.    |                                             |         |
| Position  |                                              |         | Position  |                                             |         |
| 0.0 0.2   | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2   | 0.4 0.6                                     | 0.8 1.0 |
|           | (g) Inference Accuracy for GPT-OSS-20B       |         |           | (h) Inference Accuracy for Qwen-3-14B       |         |
| Name      |                                              |         | Name      |                                             |         |
| Sex       |                                              |         | Sex       |                                             |         |
| Age       |                                              |         | Age       |                                             |         |
| Loc.      |                                              |         | Loc.      |                                             |         |
| Nation.   |                                              |         | Nation.   |                                             |         |
| Edu.      |                                              |         | Edu.      |                                             |         |
| Relation. |                                              |         | Relation. |                                             |         |
| Occup.    |                                              |         | Occup.    |                                             |         |
| Affil.    |                                              |         | Affil.    |                                             |         |
| Position  |                                              |         | Position  |                                             |         |
| 0.0 0.2   | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2   | 0.4 0.6                                     | 0.8 1.0 |
|           | (i) Inference Accuracy for Llama-3-70B       |         |           | (j) Inference Accuracy for Llama-3-8B       |         |
| Name      |                                              |         | Name      |                                             |         |
| Sex       |                                              |         | Sex       |                                             |         |
| Age       |                                              |         | Age       |                                             |         |
| Loc.      |                                              |         | Loc.      |                                             |         |
| Nation.   |                                              |         | Nation.   |                                             |         |
| Edu.      |                                              |         | Edu.      |                                             |         |
| Relation. |                                              |         | Relation. |                                             |         |
| Occup.    |                                              |         | Occup.    |                                             |         |
| Affil.    |                                              |         | Affil.    |                                             |         |
| Position  |                                              |         | Position  |                                             |         |
| 0.0 0.2   | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2   | 0.4 0.6                                     | 0.8 1.0 |
(k) Inference Accuracy for Gemma-3-4B
Name
Sex
Age
Loc.
Nation.
Edu.
Relation.
Occup.
Affil.
Position
| 0.0 0.2 | 0.4 0.6 | 0.8 1.0 |     |     |     |
| ------- | ------- | ------- | --- | --- | --- |
Figure9: InferenceaccuracybyPIIcategoryonTABdataset.
17116

|             | (a) Inference Accuracy for Claude-Sonnet-4.5 |         |             | (b) Inference Accuracy for Claude-Haiku-4.5 |         |
| ----------- | -------------------------------------------- | ------- | ----------- | ------------------------------------------- | ------- |
| ID Num.     |                                              |         | ID Num.     |                                             |         |
| Driver Lic. |                                              |         | Driver Lic. |                                             |         |
| Phone       |                                              |         | Phone       |                                             |         |
| Passport    |                                              |         | Passport    |                                             |         |
| Email       |                                              |         | Email       |                                             |         |
| Name        |                                              |         | Name        |                                             |         |
| Sex         |                                              |         | Sex         |                                             |         |
| Age         |                                              |         | Age         |                                             |         |
| Loc.        |                                              |         | Loc.        |                                             |         |
| Nation.     |                                              |         | Nation.     |                                             |         |
| Edu.        |                                              |         | Edu.        |                                             |         |
| Relation.   |                                              |         | Relation.   |                                             |         |
| Occup.      |                                              |         | Occup.      |                                             |         |
| Affil.      |                                              |         | Affil.      |                                             |         |
| Position    |                                              |         | Position    |                                             |         |
| 0.0 0.2     | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2     | 0.4 0.6                                     | 0.8 1.0 |
|             | (c) Inference Accuracy for GPT-4.1           |         |             | (d) Inference Accuracy for GPT-OSS-120B     |         |
| ID Num.     |                                              |         | ID Num.     |                                             |         |
| Driver Lic. |                                              |         | Driver Lic. |                                             |         |
| Phone       |                                              |         | Phone       |                                             |         |
| Passport    |                                              |         | Passport    |                                             |         |
| Email       |                                              |         | Email       |                                             |         |
| Name        |                                              |         | Name        |                                             |         |
| Sex         |                                              |         | Sex         |                                             |         |
| Age         |                                              |         | Age         |                                             |         |
| Loc.        |                                              |         | Loc.        |                                             |         |
| Nation.     |                                              |         | Nation.     |                                             |         |
| Edu.        |                                              |         | Edu.        |                                             |         |
| Relation.   |                                              |         | Relation.   |                                             |         |
| Occup.      |                                              |         | Occup.      |                                             |         |
| Affil.      |                                              |         | Affil.      |                                             |         |
| Position    |                                              |         | Position    |                                             |         |
| 0.0 0.2     | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2     | 0.4 0.6                                     | 0.8 1.0 |
|             | (e) Inference Accuracy for GPT-4.1-Mini      |         |             | (f) Inference Accuracy for Gemma-3-27B      |         |
| ID Num.     |                                              |         | ID Num.     |                                             |         |
| Driver Lic. |                                              |         | Driver Lic. |                                             |         |
| Phone       |                                              |         | Phone       |                                             |         |
| Passport    |                                              |         | Passport    |                                             |         |
| Email       |                                              |         | Email       |                                             |         |
| Name        |                                              |         | Name        |                                             |         |
| Sex         |                                              |         | Sex         |                                             |         |
| Age         |                                              |         | Age         |                                             |         |
| Loc.        |                                              |         | Loc.        |                                             |         |
| Nation.     |                                              |         | Nation.     |                                             |         |
| Edu.        |                                              |         | Edu.        |                                             |         |
| Relation.   |                                              |         | Relation.   |                                             |         |
| Occup.      |                                              |         | Occup.      |                                             |         |
| Affil.      |                                              |         | Affil.      |                                             |         |
| Position    |                                              |         | Position    |                                             |         |
| 0.0 0.2     | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2     | 0.4 0.6                                     | 0.8 1.0 |
|             | (g) Inference Accuracy for GPT-OSS-20B       |         |             | (h) Inference Accuracy for Llama-3-8B       |         |
| ID Num.     |                                              |         | ID Num.     |                                             |         |
| Driver Lic. |                                              |         | Driver Lic. |                                             |         |
| Phone       |                                              |         | Phone       |                                             |         |
| Passport    |                                              |         | Passport    |                                             |         |
| Email       |                                              |         | Email       |                                             |         |
| Name        |                                              |         | Name        |                                             |         |
| Sex         |                                              |         | Sex         |                                             |         |
| Age         |                                              |         | Age         |                                             |         |
| Loc.        |                                              |         | Loc.        |                                             |         |
| Nation.     |                                              |         | Nation.     |                                             |         |
| Edu.        |                                              |         | Edu.        |                                             |         |
| Relation.   |                                              |         | Relation.   |                                             |         |
| Occup.      |                                              |         | Occup.      |                                             |         |
| Affil.      |                                              |         | Affil.      |                                             |         |
| Position    |                                              |         | Position    |                                             |         |
| 0.0 0.2     | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2     | 0.4 0.6                                     | 0.8 1.0 |
|             | (i) Inference Accuracy for Llama-3-70B       |         |             | (j) Inference Accuracy for Qwen-3-14B       |         |
| ID Num.     |                                              |         | ID Num.     |                                             |         |
| Driver Lic. |                                              |         | Driver Lic. |                                             |         |
| Phone       |                                              |         | Phone       |                                             |         |
| Passport    |                                              |         | Passport    |                                             |         |
| Email       |                                              |         | Email       |                                             |         |
| Name        |                                              |         | Name        |                                             |         |
| Sex         |                                              |         | Sex         |                                             |         |
| Age         |                                              |         | Age         |                                             |         |
| Loc.        |                                              |         | Loc.        |                                             |         |
| Nation.     |                                              |         | Nation.     |                                             |         |
| Edu.        |                                              |         | Edu.        |                                             |         |
| Relation.   |                                              |         | Relation.   |                                             |         |
| Occup.      |                                              |         | Occup.      |                                             |         |
| Affil.      |                                              |         | Affil.      |                                             |         |
| Position    |                                              |         | Position    |                                             |         |
| 0.0 0.2     | 0.4 0.6                                      | 0.8 1.0 | 0.0 0.2     | 0.4 0.6                                     | 0.8 1.0 |
(k) Inference Accuracy for Gemma-3-4B
ID Num.
Driver Lic.
Phone
Passport
Email
Name
Sex
Age
Loc.
Nation.
Edu.
Relation.
Occup.
Affil.
Position
| 0.0 0.2   | 0.4 0.6                                          | 0.8 1.0 |     |     |     |
| --------- | ------------------------------------------------ | ------- | --- | --- | --- |
| Figure10: | InferenceaccuracybyPIIcategoryonPANORAMAdataset. |         |     |     |     |
17117

| 1.0 |     |     |     |     |     | H1 (Easy) |
| --- | --- | --- | --- | --- | --- | --------- |
H2
H3 (Medium)
H4
H5 (Hard)
0.8
ycaruccA
0.6
0.4
0.2
0.0
Claude-Sonnet-4.5 GPT-4.1 GPT-OSS-120B Claude-Haiku-4.5 GPT-4.1-Mini Gemma-3-27B GPT-OSS-20B Qwen-3-14B Llama-3-70B Llama-3-8B Gemma-3-4B
(a)TAB
| 1.0 |     |     |     |     |     | H1 (Easy) |
| --- | --- | --- | --- | --- | --- | --------- |
H2
H3 (Medium)
H4
H5 (Hard)
0.8
| ycaruccA 0.6 |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
0.4
0.2
0.0
Claude-Sonnet-4.5 Claude-Haiku-4.5 GPT-4.1 GPT-OSS-120B GPT-4.1-Mini Gemma-3-27B GPT-OSS-20B Llama-3-8B Llama-3-70B Qwen-3-14B Gemma-3-4B
(b)PANORAMA
Figure11: InferenceaccuracybyHardnesslevel.
| inFigure28. |     |     | matchingusesthealignmentpromptinFigure27. |     |     |     |
| ----------- | --- | --- | ----------------------------------------- | --- | --- | --- |
Thefollowingexampleillustratessubjectmatch- Human annotators verified the matching results
ing between Ground Truth and inference from tocalculateSubjectMatchRatioandvalidatethe
| anonymizedtext: |                 |               | matchingprocedure.        |     |     |     |
| --------------- | --------------- | ------------- | ------------------------- | --- | --- | --- |
| • Subject       | 0: Ground Truth | describes “Mr | Jan                       |     |     |     |
|                 |                 |               | C.3.2 PII-levelComparison |     |     |     |
Kowalski-Theapplicant,Polishnationalbornin
|                         |     |                 | For matched                             | subject pairs, | PII-level | comparison |
| ----------------------- | --- | --------------- | --------------------------------------- | -------------- | --------- | ---------- |
| 1934,livesinWarsaw,...” |     | Matchedwith“The |                                         |                |           |            |
|                         |     | →               | followsStaabetal.(2024)’sscoringscheme: |                |           |            |
applicant-Individualwholodgedtheapplication
| ...”        |                               |     | • Rule-basedcomparisonisfirstperformedbycat- |                  |             |            |
| ----------- | ----------------------------- | --- | -------------------------------------------- | ---------------- | ----------- | ---------- |
|             |                               |     | egory:                                       | free text (Name, | Occupation, | etc.) uses |
| • Subject1: | GroundTruthdescribes“MrStefan |     |                                              |                  |             |            |
|             |                               |     | Jaro-Winkler                                 | similarity       | (threshold  | 0.85), Age |
Nowak-AgentrepresentingthePolishGovern-
uses 5yearrangematching,Locationuseshi-
| ment,...” | Matchedwith“Agentrepresenting |     |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- | --- |
±
→ erarchicalmatching,andCODEtypesuseexact
theGovernment-Specificofficialdesignatedto
matchingafternormalization.
represent...”
For framework validation (Appendix B), infer- • Cases judged as mismatch (0.0 points) are re-
ence is performed on original text, and subject evaluatedforsemanticequivalenceusingtheeval-
17118

uatorLLM,whichassignsMatch(1.0),LessPre- it more sensitive to underprotected subjects like
cise(0.5),orMismatch(0.0). Thescoringprompt Subject2,whereasCPRweightsproportionallyto
| isshowninFigure29. |            |     |           |     |           |     | PIIcount. |     |     |     |     |     |     |
| ------------------ | ---------- | --- | --------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| • Human            | evaluation | is  | triggered |     | only when | the |           |     |     |     |     |     |     |
LLM evaluator fails to return a valid response C.4 TokenandEntityRecallEvaluation
duetoresponseerrorsorparsingexceptions;for
|     |     |     |     |     |     |     | The TAB | benchmark |     | (Pilán | et al., | 2022) | evalua- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------ | ------- | ----- | ------- |
frameworkvalidation,allmismatchcaseswere
tionmethodologyisappliedtomeasuretokenand
manuallyreviewedandevaluatedbyhumanan-
entity-levelmaskingperformance.
notators.
|     |     |     |     |     |     |     | Ground | Truth | Construction. |     | For | Token | Recall |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------- | --- | --- | ----- | ------ |
C.3.3 CPRandIPRCalculationExample andEntityRecallcalculation,entitygroundtruth
|     |     |     |     |     |     |     | based on | the TAB | 8-category |     | system | (PERSON, |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | ------ | -------- | --- |
Consideradocumentwith3GroundTruthsubjects
containingatotalof9PIIs. Afteranonymization, CODE,LOC,ORG,DEM,DATETIME,QUAN-
theadversarialLLMattemptstoidentifysubjects TITY, MISC) is used. The TAB dataset uses
andinfertheirPIIs. Subjectmatchingisperformed the original benchmark’s entity annotations as-is.
SincethePANORAMAdatasetdoesnothaveen-
| by comparing |     | Ground | Truth | subject | descriptions |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ----- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
with LLM-inferred subject descriptions via the tityannotations,separateentityannotationisper-
alignment prompt (Figure 28). Each inferred PII formedinthisstudyfollowingtheTABbenchmark
|         |        |               |     |         |           |      | guidelines; | the | annotation |     | procedure | and | quality |
| ------- | ------ | ------------- | --- | ------- | --------- | ---- | ----------- | --- | ---------- | --- | --------- | --- | ------- |
| is then | scored | as 1.0 (exact |     | match), | 0.5 (less | pre- |             |     |            |     |           |     |         |
cise),or0.0(mismatchornotinferred)viathePII verificationresultsaredescribedinAppendixD.
agreementevaluationprompt(Figure29): CategorySystemCompatibility. Theanonymiza-
tionexperimentstargetTAB’s8categories,while
| • Subject | 1   | (matched): | Originally |     | had | 4 PIIs |     |     |     |     |     |     |     |
| --------- | --- | ---------- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
inferenceevaluationtargetsSPIA’s15categories.
| (O =                        | 4).       | The adversary |       | matched          | this | subject |                                           |     |     |     |                  |     |     |
| --------------------------- | --------- | ------------- | ----- | ---------------- | ---- | ------- | ----------------------------------------- | --- | --- | --- | ---------------- | --- | --- |
| 1                           |           |               |       |                  |      |         | ThesesystemsarecompatiblebecauseTAB’scat- |     |     |     |                  |     |     |
| andinferred4PIIswithscores: |           |               |       | 1.0(exactmatch), |      |         |                                           |     |     |     |                  |     |     |
|                             |           |               |       |                  |      |         | egoriesencompassSPIA’s:                   |     |     |     | TAB’sDEMcategory |     |     |
| 0.5 (less                   | precise), | 0.5           | (less | precise),        | 0.0  | (mis-   |                                           |     |     |     |                  |     |     |
coversdemographicattributes(age,gender,occu-
| match). | TotalinferredA |     | =   | 2.0. |     |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
pation,education),andMISCcoversallotherper-
|           |     |               |            |         |      |         | sonal information. |         | As  | Pilán | et al.        | (2022) | defined |
| --------- | --- | ------------- | ---------- | ------- | ---- | ------- | ------------------ | ------- | --- | ----- | ------------- | ------ | ------- |
| • Subject | 2   | (matched):    | Originally |         | had  | 2 PIIs  |                    |         |     |       |               |        |         |
|           |     |               |            |         |      |         | annotation         | targets | as  | “all  | text elements | with   | re-     |
| (O 2 =    | 2). | The adversary |            | matched | this | subject |                    |         |     |       |               |        |         |
andinferred2PIIswithscores: 1.0(exactmatch), identificationrisk,”textanonymizedunderTAB’s
8categoriesshouldprotectinformationcorrespond-
| 0.5(lessprecise). |     | TotalinferredA |     |     | = 1.5. |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2
ingtoSPIA’s15categories.
| •                             |         |                | Originallyhad3PIIs |        |              |        |                   |            |          |                 |                 |            |        |
| ----------------------------- | ------- | -------------- | ------------------ | ------ | ------------ | ------ | ----------------- | ---------- | -------- | --------------- | --------------- | ---------- | ------ |
| Subject3(unmatched):          |         |                |                    |        |              |        |                   |            |          | For             | TAB Longformer, |            | en-    |
|                               |         |                |                    |        |              |        | Masking           | Detection. |          |                 |                 |            |        |
| (O =                          | 3). The | adversary      |                    | failed | to identify  | this   |                   |            |          |                 |                 |            |        |
| 3                             |         |                |                    |        |              |        | tity information  |            | is       | preserved       | during          | masking    |        |
| subjectfromtheanonymizedtext. |         |                |                    |        | PerStep1,all |        |                   |            |          |                 |                 |            |        |
|                               |         |                |                    |        |              |        | and is used       | directly;  |          | for DeID-GPT,   |                 | DP-Prompt, |        |
|                               |         |                | TotalinferredA     |        |              | = 0.0. |                   |            |          |                 |                 |            |        |
| PIIsareassigned0.0.           |         |                |                    |        | 3            |        |                   |            |          |                 |                 |            |        |
|                               |         |                |                    |        |              |        | and AA,           | we use     | span     | search—checking |                 | whether    |        |
|                               |         |                |                    |        |              |        | each ground-truth |            | entity’s |                 | text still      | exists     | in the |
| CPR measures                  |         | the proportion |                    | of     | protected    | PIIs   |                   |            |          |                 |                 |            |        |
anonymizedoutputtodeterminemasking.
| acrossallsubjects. |     | Theadversaryinferredatotal |       |        |              |     |                       |              |     |         |            |           |     |
| ------------------ | --- | -------------------------- | ----- | ------ | ------------ | --- | --------------------- | ------------ | --- | ------- | ---------- | --------- | --- |
| ofA +A             | +A  | = 2.0+1.5+0.0              |       |        | = 3.5PIIsout |     |                       |              |     |         |            |           |     |
| 1                  | 2   | 3                          |       |        |              |     |                       |              |     |         |            |           |     |
| ofO +O             | +O  | = 4+2+3                    |       | =      | 9GroundTruth |     |                       |              |     |         |            |           |     |
| 1                  | 2   | 3                          |       |        |              |     | C.5 UtilityEvaluation |              |     |         |            |           |     |
| PIIs. Thus,CPR     |     | = 1                        | 3.5/9 | 0.611. |              |     |                       |              |     |         |            |           |     |
|                    |     | −                          |       | ≈      |              |     |                       |              |     |         |            |           |     |
|                    |     |                            |       |        |              |     | Staab et              | al. (2024)’s |     | utility | evaluation | methodol- |     |
IPRaveragesper-subjectprotectionratesequally.
Each subject’s protection rate is: Subject 1: 1 ogy is applied to measure the degree of meaning
− preservationinanonymizedtext.
| 2.0/4 | = 0.50, | Subject | 2:  | 1   | 1.5/2 | = 0.25, |     |     |     |     |     |     |     |
| ----- | ------- | ------- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
−
Subject 3: 1 0.0/3 = 1.00. Thus, IPR = Metrics. Following Staab et al. (2024), we
−
(0.50+0.25+1.00)/3 0.583. useLLM-basedReadability(1–10)andMeaning
≈
The unmatched subject contributes 1.0 to IPR, preservation(1–10)scores,alongwithROUGE-L
reflectingcompleteprotectionwhentheadversary (longestcommonsubsequenceF1). Theintegrated
cannotidentifythesubject’sexistence. Inthisex- utility metric is calculated as MeanUtility =
ample,CPR(0.611)exceedsIPR(0.583)because (Readability + Meaning + ROUGE-L)/3, where
IPRassignsequalweighttoeachsubject,making LLMscoresarenormalizedto[0,1].
17119

| C.6 Single-subjectEvaluation(1-AAC) |     |     |     |     |     |     | describedinAppendixG.1. |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
Sincetheperformanceofanonymizationmeth-
Forcomparisonwithpriorwork(Staabetal.,2024),
odsheavilydependsonthebackboneused(Staab
| the single-subject |     | evaluation |     | metric | 1-AAC | (1  | -              |     |      |          |                |     |     |
| ------------------ | --- | ---------- | --- | ------ | ----- | --- | -------------- | --- | ---- | -------- | -------------- | --- | --- |
|                    |     |            |     |        |       |     | et al., 2024), | the | same | set of 6 | backbones—GPT- |     |     |
AdversarialAccuracy)isalsoreported.
|                |     |                                |     |     |     |     | 4.1, GPT-4.1-Mini, |     |     | Claude-Sonnet-4.5, |     | Claude- |     |
| -------------- | --- | ------------------------------ | --- | --- | --- | --- | ------------------ | --- | --- | ------------------ | --- | ------- | --- |
| TargetSubject. |     | Thetargetsubjectisdefinedasthe |     |     |     |     |                    |     |     |                    |     |         |     |
Haiku-4.5,Llama-3.1-8B,andGemma-3-27B—is
applicantforTABandtheauthorforPANORAMA.
|     |     |     |     |     |     |     | applied | to all | generative | methods | to  | isolate | and |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------- | ------- | --- | ------- | --- |
For1-AACcalculation,single-subjectgroundtruth
|         |            |             |     |     |            |      | evaluate | the effectiveness |     | of the | methodology |     | it- |
| ------- | ---------- | ----------- | --- | --- | ---------- | ---- | -------- | ----------------- | --- | ------ | ----------- | --- | --- |
| data is | separately | constructed |     | by  | extracting | only |          |                   |     |        |             |     |     |
self.
thetargetsubjectforeachdatasetfromtheoriginal
per-subjectgroundtruthdata.
|              |     |            |     |          |     |     | D AnnotationQualityforSpan-based |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | -------- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| Calculation. |     | Calculated |     | as 1-AAC |     | = 1 |                                  |     |     |     |     |     |     |
Evaluation
−
| S/  | A,whereS |     | isthesumofPIIscoressuc- |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThePANORAMAdatasetdoesnotincludeentity
cessfullyinferredfromanonymizedtextandAis
P P
thetotalnumberofGroundTruthPIIsfromoriginal annotationsinitsoriginalform. Therefore,weper-
formedseparateentityannotationforspan-based
text.
metrics(TokenRecall,EntityRecall)evaluationin
| C.7 MethodImplementationDetails |     |     |     |     |     |     | Section5. |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Fouranonymizationtechniquesarecomparedand D.1 AnnotationProcedure
evaluatedinthisstudy.
|     |     |     |     |     |     |     | Annotation | Guidelines. |     | We  | applied | the | TAB |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | ------- | --- | --- |
TAB Longformer. The Longformer-based NER benchmark (Pilán et al., 2022) annotation guide-
| model from | Pilán | et al. | (2022) | is  | used. Based | on  |          |          |     |                   |     |          |     |
| ---------- | ----- | ------ | ------ | --- | ----------- | --- | -------- | -------- | --- | ----------------- | --- | -------- | --- |
|            |       |        |        |     |             |     | lines to | annotate | 8   | entity categories |     | (PERSON, |     |
allenai/longformer-base-4096
(Beltagyetal.,
CODE,LOC,ORG,DEM,DATETIME,QUAN-
2020), a confidence threshold of 0.55 is applied TITY, MISC) and identifier types (DIRECT,
| following | the | original | paper’s | settings. |     | For fair |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
QUASI).
| evaluation, | the | model | is retrained |     | excluding | the |             |     |             |     |         |            |     |
| ----------- | --- | ----- | ------------ | --- | --------- | --- | ----------- | --- | ----------- | --- | ------- | ---------- | --- |
|             |     |       |              |     |           |     | Annotators. |     | Two experts | in  | privacy | protection |     |
TABtestset(N=144)usedinthisexperimentfrom
participatedintheannotationwork.
thetrainingdata.
|           |     |               |     |                 |     |     | Annotation                    | Tool. | We  | developed | a             | custom | web- |
| --------- | --- | ------------- | --- | --------------- | --- | --- | ----------------------------- | ----- | --- | --------- | ------------- | ------ | ---- |
| DeID-GPT. |     | The zero-shot |     | prompting-based |     |     |                               |       |     |           |               |        |      |
|           |     |               |     |                 |     |     | basedtoolforentityannotation. |       |     |           | Figure12shows |        |      |
anonymizationtechniquefromLiuetal.(2023)is
thetoolinterface.
applied. Theoriginalpaper’s18PIIcategoriesare Approximately20%(31
AnnotationProcedure.
| restructured                               | to   | the TAB | 8-category |        | system,       | and |                                          |            |           |                  |     |      |      |
| ------------------------------------------ | ---- | ------- | ---------- | ------ | ------------- | --- | ---------------------------------------- | ---------- | --------- | ---------------- | --- | ---- | ---- |
|                                            |      |         |            |        |               |     | documents)                               | of         | the total | 151 documents    |     | were | as-  |
| temperature                                | 0.05 | is used | to         | induce | deterministic |     |                                          |            |           |                  |     |      |      |
|                                            |      |         |            |        |               |     | signedtobothannotatorsforcross-labeling. |            |           |                  |     |      | The  |
| outputfollowingtheoriginalpaper’ssettings. |      |         |            |        |               | The |                                          |            |           |                  |     |      |      |
|                                            |      |         |            |        |               |     | average                                  | annotation | time      | is approximately |     | 2    | min- |
promptisdescribedinAppendixG.1. utes per document. After annotation completion,
Thedifferentialprivacy-basedpara-
| DP-Prompt. |     |     |     |     |     |     | disagreementsareresolvedthroughthird-partyre- |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
phrasingapproachfromUtpalaetal.(2023)isap-
view.
| plied. High | temperature |     | (1.5, | or  | 1.0 due | to An- |                              |     |     |     |     |     |     |
| ----------- | ----------- | --- | ----- | --- | ------- | ------ | ---------------------------- | --- | --- | --- | --- | --- | --- |
|             |             |     |       |     |         |        | D.2 Inter-AnnotatorAgreement |     |     |     |     |     |     |
thropicAPIlimitations)andtop_p1.0areusedfor
linguistic pattern obfuscation following the orig- To verify annotation quality, we measured inter-
inal paper’s settings. The prompt is described in annotatoragreementusingthesamespan-levelAv-
| AppendixG.1. |     |     |     |     |     |     | erageObservedAgreement(AOA)methodasPilán |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
AA.Thefeedback-guidediterativeanonymization et al. (2022). Table 10 compares the agreement
techniquefromStaabetal.(2024)isapplied. Fol- resultsforthe31overlappingdocuments(139enti-
lowingtheoriginalpaper’ssettings,promptlevel ties)withtheTABbenchmark.
3 (Chain-of-Thought) is used with 3 iterative re- The higher agreement for PANORAMA com-
finement rounds, and the original paper’s Reddit paredtoTABisattributedtotherelativelyshorter
authorattributesarerestructuredtoTAB’s8cate- textlength(average260vs. 3,918characters)and
gories. Foreachdataset,TABissetwith“applicant” fewerentitiesperdocument,resultinginloweran-
| asthetargetsubjectfor“legalcasedocument,”and |     |     |     |     |     |     | notationdifficulty. |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
PANORAMAissetwith“author”asthetargetsub- Note: TheTABdatasetusesentitylabelsfromthe
jectfor“textwrittenbyoneauthor.” Thepromptis originalbenchmarkas-is.
17120

Figure 12: Entity annotation tool interface. Annotators can select spans from text and specify entity type and
identifiertype.
| Metric |     | PANORAMA | TAB | AdversaryPair |     | CPRρ | IPRρ |
| ------ | --- | -------- | --- | ------------- | --- | ---- | ---- |
EntityTypeExactMatch 85.6% 75.0% Claude-Sonnet-4.5vs.GPT-4.1 .980 .981
EntityTypePartialMatch 86.3% 80.0% Claude-Sonnet-4.5vs.Claude-Haiku-4.5 .980 .980
IdentifierTypeExactMatch 79.9% 67.0% GPT-4.1vs.Claude-Haiku-4.5 .986 .981
| IdentifierTypePartialMatch |     | 81.3% | 71.0% |     |     |     |     |
| -------------------------- | --- | ----- | ----- | --- | --- | --- | --- |
Table11: SpearmanrankcorrelationofCPRandIPR
Table10: PANORAMAEntityAnnotationAgreement acrossadversarymodels(n=38,allp<10 26).
−
(vs. TABBenchmark).
E.2 PIIType-wiseAnalysis(CODEvs
E AdditionalResults
NON-CODE)
|     |     |     |     | We analyzed | protection rates | by categorizing | PII |
| --- | --- | --- | --- | ----------- | ---------------- | --------------- | --- |
Thisappendixpresentsadditionalanalysisresults
intoCODEandNON-CODEtypesbasedonmor-
mentionedinSection5.
|     |     |     |     | phologicalcharacteristics. |                   | SincetheTABdataset |     |
| --- | --- | --- | --- | -------------------------- | ----------------- | ------------------ | --- |
|     |     |     |     | does not                   | contain CODE-type | PIIs, we conducted |     |
E.1 Multi-AdversaryRobustnessAnalysis
analysisonlyonthePANORAMAdataset,which
| To verify | that the evaluation | is not biased | by the |     |     |     |     |
| --------- | ------------------- | ------------- | ------ | --- | --- | --- | --- |
includesCODEtypes.
choiceofasingleadversary,wevariedtheadver-
| saryacrosstwoadditionalmodels—GPT-4.1and |     |     |     | PIITypeDefinitions: |     |     |     |
| ---------------------------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
Claude-Haiku-4.5—alongsideClaude-Sonnet-4.5.
|     |     |     |     | •   | (5): ID Number, | Driver License, |     |
| --- | --- | --- | --- | --- | --------------- | --------------- | --- |
CODE types
Table11reportspairwiseSpearmanrankcorrela-
Phone,Passport,Email
| tions of CPR     | and IPR                     | across all anonymization |     |                      |     |                  |     |
| ---------------- | --------------------------- | ------------------------ | --- | -------------------- | --- | ---------------- | --- |
| configurations(n | = 38),andFigure13visualizes |                          |     |                      |     |                  |     |
|                  |                             |                          |     | • NON-CODEtypes(10): |     | Name,Sex,Age,Lo- |     |
CPRforallanonymizationmethod–backbonecom-
cation,Nationality,Education,Relationship,Oc-
binations across the three adversaries. All pairs cupation,Affiliation,Position
| yield ρ > | 0.98, indicating | that relative | rankings |     |     |     |     |
| --------- | ---------------- | ------------- | -------- | --- | --- | --- | --- |
amonganonymizationmethodsremainhighlycon- Figure14showstheprotectionrateanalysisre-
sistentregardlessofadversarychoice. Theabsolute sults by PII type. CODE-type PIIs achieve CPR
CPR/IPRgapsbetweenadversariesrangefrom1.3 1.0 in most techniques, while NON-CODE types
to 4.6 percentage points for representative high- showrelativelylowerprotectionrates. Thisdemon-
performingconfigurations. stratesthatNON-CODE-typePIIscanbeindirectly
17121

Multi-Adversary Comparison: CPR by Anonymization Method (3-way)
|                            |     | TAB |     |                      | PANORAMA |     |
| -------------------------- | --- | --- | --- | -------------------- | -------- | --- |
| gemma3-27b dp_prompt       |     |     |     | adversarial gpt-4-1  |          |     |
| deid_gpt                   |     |     |     | adversarial          |          |     |
| gpt-4-1                    |     |     |     | claude-sonnet-4-5    |          |     |
| claude-sonnet-4-5 deid_gpt |     |     |     | llama3-1-8b deid_gpt |          |     |
| dp_prompt                  |     |     |     | adversarial          |          |     |
| llama3-1-8b                |     |     |     | gpt-4-1-mini         |          |     |
| deid_gpt                   |     |     |     | adversarial          |          |     |
| claude-haiku-4-5           |     |     |     | gemma3-27b           |          |     |
| gemma3-27b deid_gpt        |     |     |     | deid_gpt gpt-4-1     |          |     |
| adversarial                |     |     |     | adversarial          |          |     |
| llama3-1-8b                |     |     |     | claude-haiku-4-5     |          |     |
| dp_prompt                  |     |     |     | adversarial          |          |     |
| claude-sonnet-4-5          |     |     |     | llama3-1-8b          |          |     |
enobkcaB + dohteM
| gpt-4-1-mini adversarial      |     |     |     | claude-sonnet-4-5 deid_gpt |     |     |
| ----------------------------- | --- | --- | --- | -------------------------- | --- | --- |
| deid_gpt                      |     |     |     | deid_gpt                   |     |     |
| gpt-4-1-mini                  |     |     |     | claude-haiku-4-5           |     |     |
| deid_gpt                      |     |     |     | deid_gpt                   |     |     |
| llama3-1-8b                   |     |     |     | gpt-4-1-mini               |     |     |
| claude-sonnet-4-5 adversarial |     |     |     | gemma3-27b deid_gpt        |     |     |
| adversarial                   |     |     |     | longformer                 |     |     |
| gpt-4-1                       |     |     |     | longformer                 |     |     |
| claude-haiku-4-5 dp_prompt    |     |     |     | llama3-1-8b dp_prompt      |     |     |
| adversarial                   |     |     |     | dp_prompt                  |     |     |
| gemma3-27b                    |     |     |     | claude-sonnet-4-5          |     |     |
| longformer                    |     |     |     | dp_prompt                  |     |     |
| longformer                    |     |     |     | claude-haiku-4-5           |     |     |
| claude-haiku-4-5 adversarial  |     |     |     | gemma3-27b dp_prompt       |     |     |
| dp_prompt                     |     |     |     | dp_prompt                  |     |     |
| gpt-4-1                       |     |     |     | gpt-4-1-mini               |     |     |
Ad v e r s a r y  M o d e l
| dp_prompt    |     |     |     | dp_ p ro m p t |     | C l a u d e - S on n e t -4.5 |
| ------------ | --- | --- | --- | -------------- | --- | ----------------------------- |
| gpt-4-1-mini |     |     |     | g p t -4 -1    |     |                               |
GPT-4.1
Claude-Haiku-4.5
| 0.0 | 0.2 | 0.4 | 0.6 0.8 | 1.0 0.0 0.2 | 0.4 0.6 | 0.8 1.0 |
| --- | --- | --- | ------- | ----------- | ------- | ------- |
|     |     | CPR |         |             | CPR     |         |
Figure 13: CPR by anonymization method and backbone across three adversary models. Within each dataset,
configurationsareorderedbytheirCPRunderClaude-Sonnet-4.5(ascending).
inferred from context and are not fully protected and hence the inferred education—remain infer-
byspanmaskingalone. able. PANORAMA, by contrast, encodes higher-
Hardnesscueswithin~260-characterpostsasex-
E.3 InferencebyHardnessLevelAfter
plicitpersonalcuessuchas“#ProfessorVibes”or
Anonymization
“flightsimulationlogs”;theseareidentifiedandre-
On original text, inference accuracy shows a de- movedinasinglesubstitution. Higher-Hardnessin-
creasing trend as hardness increases (Figure 11). ferabilityafteranonymizationthusdependsonhow
Afteranonymization,thistrendnolongerholdsuni- muchcontextualstructureispreservedduringthe
|                                              |     |     |             | process—substantially | more in long, | structurally |
| -------------------------------------------- | --- | --- | ----------- | --------------------- | ------------- | ------------ |
| formlyacrossdatasets(Figure15):              |     |     | onTAB,three |                       |               |              |
| offourmethodsleavehigher-hardnessPIIs(levels |     |     |             | richlegaltext.        |               |              |
4–5)as—ormore—inferablethanlower-hardness
E.4 Privacy-UtilityTrade-offAnalysis
ones,whereasonPANORAMAthesamemethods
holdortightenprotectionatHardnesslevels4–5. Figure 16 visualizes the trade-off between CPR
This divergence reflects how anonymization (privacy)andMeanUtilityacrossanonymization
| interacts with | each | domain’s | document struc- | techniques. |     |     |
| -------------- | ---- | -------- | --------------- | ----------- | --- | --- |
ture rather than the higher-Hardness categories PANORAMA. Adversarial Anonymization
alone. Anonymizers substitute identifier-like to- achieves the most balanced performance in both
kens(names,professionwords,placenames)with privacyandutility. DeID-GPTachieveshighutility
[redacted],butleaveintactcontextualdescriptors withcompetitiveinferenceprotection. DP-Prompt
such as “representing the applicant” or “Agent shows the lowest privacy protection, indicating
oftheGovernment”—becausethesearenotthem- that paraphrasing alone is insufficient for PII
| selves recognized | as  | PII. In TAB, | such phrases | protection. |     |     |
| ----------------- | --- | ------------ | ------------ | ----------- | --- | --- |
surviveinabundancewithin~4,000-characterlegal TAB. Due to the complexity of legal documents,
documents: evenafter“lawyer”isredacted,nearby both privacy protection and utility are generally
role descriptions let the underlying profession— lowerthanPANORAMA.DeID-GPTachievesthe
17122

1-AA (Code) 1-AA (Non-Code) CPR (Code) CPR (Non-Code)
TAB Longformer
DeID-GPT (Llama-3.1-8B)
DeID-GPT (Gemma-3-27B)
DeID-GPT (GPT-4.1-Mini)
DeID-GPT (GPT-4.1)
DeID-GPT (Claude-Haiku-4.5)
DeID-GPT (Claude-Sonnet-4.5)
DP-Prompt (Llama-3.1-8B)
DP-Prompt (Gemma-3-27B)
DP-Prompt (GPT-4.1-Mini)
DP-Prompt (GPT-4.1)
DP-Prompt (Claude-Haiku-4.5)
DP-Prompt (Claude-Sonnet-4.5)
AA (Llama-3.1-8B)
AA (Gemma-3-27B)
AA (GPT-4.1-Mini)
AA (GPT-4.1)
AA (Claude-Haiku-4.5)
AA (Claude-Sonnet-4.5)
0.0 0.2 0.4 0.6 0.8 1.0
Score
Figure14: PIItype-wiseprotectionrateanalysisonPANORAMAdataset. CODE-typePIIsachieveCPR1.0in
mosttechniques,whileNON-CODEtypesshowrelativelylowerprotectionrates.
highestprivacyprotection,thoughwithsomeutil- elsdeviatefromtheDeID-GPTpromptinopposite
ity loss depending on the backbone. DP-Prompt directions: Claude-Sonnetunder-maskscommon
showshighlyinconsistentresultsacrossbackbones. nouns that implicitly encode occupation or rela-
AdversarialAnonymizationshowsrelativelylower tionships(“students,” “patients,” role-ladenhash-
privacyprotectiononTAB. tags),treatingthedemographicattributescategory
Summary. The optimal technique varies by do- as limited to explicit identifiers, while GPT-4.1
main. Forshortonlinetexts(PANORAMA),Ad- over-masksidiomatictokensunrelatedtoactualPII,
versarial Anonymization is effective, while for depressingutilitywithoutimprovingCPR.Llama-
longer legal documents (TAB), DeID-GPT pro- 3.1-8B applies the 8-category list more literally,
videsbetterprivacyprotection. DP-Prompt’spara- whichonshorttextsalignswellwiththeCPRcri-
phrasingapproachfailstoprovidereliableprivacy terion.
protectioninbothdomains.
On TAB, the result reverses: Llama-3.1-8B’s
E.5 Backbone-specificAnonymization
CPR (.396) falls well below GPT-4.1 (.674) and
Behavior
Claude-Sonnet-4.5(.650)becauseLlamainconsis-
Llama-3.1-8B achieves the highest CPR under tentlymaskstheorganization-namecategoryfrom
DeID-GPT on PANORAMA despite its smaller the same prompt, leaving targets such as “Euro-
size(Section5). Inspectionofoutputsfromthree peanParliament”verbatim. Llama-3.1-8Balsoun-
backbones (Claude-Sonnet-4.5, GPT-4.1, Llama- derperforms on PANORAMA under Adversarial
3.1-8B)indicatesthatthisreflectshoweachmodel Anonymization (.759 vs. GPT-4.1 .870, Claude-
interprets the anonymization prompt rather than Sonnet-4.5 .852), where iterative reasoning is re-
modelcapability. quired instead of category-based deletion. The
OnshortPANORAMAtexts,thetwolargermod- high DeID-GPT/PANORAMA CPR is therefore
17123

|     |     |     |     | H1 (Easy) |     | H2  | H3 (Medium) | H4  | H5 (Hard) |     |
| --- | --- | --- | --- | --------- | --- | --- | ----------- | --- | --------- | --- |
|     |     |     |     | TAB       |     |     |             |     | PANORAMA  |     |
)noitcetorp regnorts = rewol( ycaruccA ecnerefnI
1.0
0.8
0.6
0.4
0.2
0.0
TAB Longformer DeID-GPT DP-Prompt AA TAB Longformer DeID-GPT DP-Prompt AA
Figure15: InferenceaccuracybyHardnesslevelafteranonymization,averagedacrossallbackbones. Loweris
strongerprotection. TABandPANORAMAdivergeatHardnesslevels4–5forthreeoffourmethods.
| anartifactofshorttextscombinedwithanexplicit |     |     |     |     |     |     | Position. |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
categoryprompt,notsuperioranonymizationcapa- Code-based categories (ID Number, Driver Li-
| bility. |     |     |     |     |     |     | cense,Phone,Passport,Email)shouldberecorded |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
withexactstringpatternsincludingdelimiters. Par-
F AnnotationGuidelines
tiallymaskedvalues(e.g.,“950-20-****”)should
notbeannotatedifthefullvaluecannotbeinferred.
| Annotators | are | presented | with | text | samples | and |     |     |     |     |
| ---------- | --- | --------- | ---- | ---- | ------- | --- | --- | --- | --- | --- |
asked to identify all individual subjects (people) • IDNumber(Free-text): Nationalidentification
| mentioned, | infer | PII | categories | for | each | subject, |     |     |     |     |
| ---------- | ----- | --- | ---------- | --- | ---- | -------- | --- | --- | --- | --- |
numbers(e.g.,USSSN,UKNINO,SpainNIF).
andrateeachinferencewithHardness(extraction
|     |     |     |     |     |     |     | • DriverLicense(Free-text): |     |     | Driver’slicensenum- |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------------------- |
difficulty)andCertainty(confidencelevel).
|           |       | Annotators |     | should | not | use lan- | ber. |     |     |     |
| --------- | ----- | ---------- | --- | ------ | --- | -------- | ---- | --- | --- | --- |
| Important | Note: |            |     |        |     |          |      |     |     |     |
guagemodelswhensearchingforinformationon-
|                   |     |        |         |          |     |       | • Phone(Free-text):   |     | Phonenumbersincludingmo- |     |
| ----------------- | --- | ------ | ------- | -------- | --- | ----- | --------------------- | --- | ------------------------ | --- |
| line. Traditional |     | search | engines | (Google, |     | Duck- |                       |     |                          |     |
|                   |     |        |         |          |     |       | bile,landline,andfax. |     | Includeinternationalpre- |     |
DuckGo,BingwithoutBingChat)arepermitted.
fixes(+1,+82,etc.).
| We developed |     | a   | custom | web-based |     | tool for |     |     |     |     |
| ------------ | --- | --- | ------ | --------- | --- | -------- | --- | --- | --- | --- |
subject-levelPIIannotation. Figure17showsthe • Passport(Free-text): Passportnumber.
toolinterface.
|         |                 |     |       |      |            |     | • Email       | (Free-text): | Personal | or organizational |
| ------- | --------------- | --- | ----- | ---- | ---------- | --- | ------------- | ------------ | -------- | ----------------- |
| Subject | Identification. |     | Count | each | individual |     | emailaddress. |              |          |                   |
personmentionedinthetextexactlyonce,regard-
|                               |     |     |     |     |               |     | • Name | (Free-text): | Record | the most complete |
| ----------------------------- | --- | --- | --- | --- | ------------- | --- | ------ | ------------ | ------ | ----------------- |
| lessofhowmanytimestheyappear. |     |     |     |     | Includespeak- |     |        |              |        |                   |
ersindialogues,referencedindividuals(colleagues, form available, prioritizing Full name over
First/LastnameoverNickname.
| family,      | acquaintances), |                                  | document |     | subjects, | and |                 |     |               |                 |
| ------------ | --------------- | -------------------------------- | -------- | --- | --------- | --- | --------------- | --- | ------------- | --------------- |
| postauthors. |                 | Excludecollectivementionswithout |          |     |           |     |                 |     |               |                 |
|              |                 |                                  |          |     |           |     | • Sex(2options: |     | Male,Female): | Inferfromnames, |
specificcount(e.g.,“citizensofLA”),butinclude
honorifics,orcontext.
collectivementionswithspecificnumbers(e.g.,“2
citizens”countsas2individuals). Excludeindivid- • Age(IntegerorRange): Recordexactage(e.g.,
ualswithnoinferablePII. 27)orarangeupto10years(e.g.,25–35). Ref-
erencedateisSeptember1,2025.
| PII Categories. |     | We  | annotate | 15  | PII categories |     |     |     |     |     |
| --------------- | --- | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- |
across two types: Code-based (5)—ID Number, • Location(4-levelstructuredfreetext): Current
DriverLicense,Phone,Passport,Email;andNon- residenceformattedaspremises/sub-city/city/
code(10)—Name,Sex,Age,Location,Nationality, country. Recordthemostspecificlevelavailable
Education, Relationship, Occupation, Affiliation, withallhigherlevels. E.g.,whenitisdeducible
17124

|                               |             | CPR Mean Utility |         |                               |         | CPR Mean Utility |         |
| ----------------------------- | ----------- | ---------------- | ------- | ----------------------------- | ------- | ---------------- | ------- |
| TAB Longformer                |             |                  |         | TAB Longformer                |         |                  |         |
| DeID-GPT (Llama-3.1-8B)       |             |                  |         | DeID-GPT (Llama-3.1-8B)       |         |                  |         |
| DeID-GPT (Gemma-3-27B)        |             |                  |         | DeID-GPT (Gemma-3-27B)        |         |                  |         |
| DeID-GPT (GPT-4.1-Mini)       |             |                  |         | DeID-GPT (GPT-4.1-Mini)       |         |                  |         |
| DeID-GPT (GPT-4.1)            |             |                  |         | DeID-GPT (GPT-4.1)            |         |                  |         |
| DeID-GPT (Claude-Haiku-4.5)   |             |                  |         | DeID-GPT (Claude-Haiku-4.5)   |         |                  |         |
| DeID-GPT (Claude-Sonnet-4.5)  |             |                  |         | DeID-GPT (Claude-Sonnet-4.5)  |         |                  |         |
| DP-Prompt (Llama-3.1-8B)      |             |                  |         | DP-Prompt (Llama-3.1-8B)      |         |                  |         |
| DP-Prompt (Gemma-3-27B)       |             |                  |         | DP-Prompt (Gemma-3-27B)       |         |                  |         |
| DP-Prompt (GPT-4.1-Mini)      |             |                  |         | DP-Prompt (GPT-4.1-Mini)      |         |                  |         |
| DP-Prompt (GPT-4.1)           |             |                  |         | DP-Prompt (GPT-4.1)           |         |                  |         |
| DP-Prompt (Claude-Haiku-4.5)  |             |                  |         | DP-Prompt (Claude-Haiku-4.5)  |         |                  |         |
| DP-Prompt (Claude-Sonnet-4.5) |             |                  |         | DP-Prompt (Claude-Sonnet-4.5) |         |                  |         |
| AA (Llama-3.1-8B)             |             |                  |         | AA (Llama-3.1-8B)             |         |                  |         |
| AA (Gemma-3-27B)              |             |                  |         | AA (Gemma-3-27B)              |         |                  |         |
| AA (GPT-4.1-Mini)             |             |                  |         | AA (GPT-4.1-Mini)             |         |                  |         |
| AA (GPT-4.1)                  |             |                  |         | AA (GPT-4.1)                  |         |                  |         |
| AA (Claude-Haiku-4.5)         |             |                  |         | AA (Claude-Haiku-4.5)         |         |                  |         |
| AA (Claude-Sonnet-4.5)        |             |                  |         | AA (Claude-Sonnet-4.5)        |         |                  |         |
|                               | 0.0 0.2     | 0.4 0.6          | 0.8 1.0 |                               | 0.0 0.2 | 0.4 0.6          | 0.8 1.0 |
|                               |             | Score            |         |                               |         | Score            |         |
|                               | (a)PANORAMA |                  |         |                               | (b)TAB  |                  |         |
Figure16: Privacy-UtilityTrade-offcomparingfouranonymizationmethodsacrosssixLLMbackbones.
that a user lives in San Francisco, it suffices to multiplephonenumbersoraffiliations). However,
writeSanFrancisco/U.S.A.asthecountrycan thesameinformationshouldnotbeannotatedwith
beinferredfromthecity. differentkeywords(e.g.,ifboth“MichaelJordan”
and“Jordan”appear,onlyannotatethemostcom-
| • Nationality(Free-text): |     | UseISOcountrynames |     | pleteform). |     |     |     |
| ------------------------- | --- | ------------------ | --- | ----------- | --- | --- | --- |
(e.g.,RepublicofKorea,UnitedStates).
HardnessratesthedifficultyofextractingPIIfrom
0to5,enablinganalysisofmodelperformanceby
| • Education(6options): |     | NoHighSchoolDiploma, |     |     |     |     |     |
| ---------------------- | --- | -------------------- | --- | --- | --- | --- | --- |
difficultylevelandquantificationofprivacyexpo-
| In High | School, High | School Diploma, | In Col- |     |     |     |     |
| ------- | ------------ | --------------- | ------- | --- | --- | --- | --- |
surerisk:
lege,CollegeDegree,PhD.
|                           |     |                    |     | • 0: Defaultvalue. | Noinferencemadeorcannot |     |     |
| ------------------------- | --- | ------------------ | --- | ------------------ | ----------------------- | --- | --- |
| • Relationship(5options): |     | Norelation,InRela- |     |                    |                         |     |     |
extractthecorrespondingPII.
| tion, Married, | Divorced, | Widowed. | Deceased |     |     |     |     |
| -------------- | --------- | -------- | -------- | --- | --- | --- | --- |
individualsshouldnothavetheirrelationshipsta- • 1: Effortlessextraction,explicitlywrittenintext.
| tusannotated. |     |     |     | E.g.,“Iam19yearsold.” |     |     |     |
| ------------- | --- | --- | --- | --------------------- | --- | --- | --- |
• 2: Straightforwardextractionwithoutstrongde-
| • Occupation | (Free-text): | Record | job title, not |     |     |     |     |
| ------------ | ------------ | ------ | -------------- | --- | --- | --- | --- |
position(e.g.,SalespersonnotSalesManager). ductivereasoning. E.g.,“MywifeandIarehav-
| UseUnemployed | ifapplicable. |         |               | ingoursecondchildinApril.” |            |          |           |
| ------------- | ------------- | ------- | ------------- | -------------------------- | ---------- | -------- | --------- |
|               |               |         |               | • 3: Requires              | additional | thinking | or common |
| • Affiliation | (Free-text):  | Current | organization, |                            |            |          |           |
recordedaswrittenintext. knowledge. E.g.,“Iremember5yearsagowhen
Iisfinishinghighschool”(Age20–23)or“Ilove
• Position(Free-text): Currentroleortitlewithin visitingSquarePark”(NewYork).
organization(e.g.,CEO,SeniorDeveloper).
|     |     |     |     | • 4: Requires | online search | for specific | informa- |
| --- | --- | --- | --- | ------------- | ------------- | ------------ | -------- |
HandlingDuplicates: ThesamePIIcategorymay tion. E.g.,“Iloveeatingiceatstonerode”(Loca-
be annotated multiple times for one subject (e.g., tion: Guelph/Ontario).
17125

Figure17: Subject-levelPIIannotationtoolinterface. Annotatorsidentifysubjectsfromthetextandinputinferred
valuesandHardness/Certaintyscoresfor15PIIcategoriespersubject.
• 5: Requires considerable effort with online G.1 TextAnonymizationPrompts
search,combiningmultiplepiecesofinformation.
|     |     |     |     |     |     | This section | presents |     | prompts | used | for | the four |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | ---- | --- | -------- |
E.g.,mentionsofspecificintersectionsrequiring
anonymizationmethodsevaluatedinSection5.
cross-referencingwithlocalcontext.
|                    |             |                          |     |      |        | DeID-GPT:Zero-shotRedactionPrompt. |             |     |           |                 |          | The |
| ------------------ | ----------- | ------------------------ | --- | ---- | ------ | ---------------------------------- | ----------- | --- | --------- | --------------- | -------- | --- |
| Hardness           | 3 indicates | extraction               |     | with | common |                                    |             |     |           |                 |          |     |
|                    | ≤           |                          |     |      |        | prompt                             | (Figure     | 18) | is used   | for             | DeID-GPT |     |
| knowledge;Hardness |             | 4requiresexternalsearch. |     |      |        |                                    |             |     |           |                 |          |     |
|                    |             | ≥                        |     |      |        | (Liu et                            | al., 2023), | a   | zero-shot | prompting-based |          |     |
Certaintyratesconfidenceintheinferencefrom0
anonymizationtechniquethatredactsexplicitPII
to5,servingasacriterionforassessingannotation
|     |     |     |     |     |     | spans. The | original | 18  | PII categories |     | are | restruc- |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | -------------- | --- | --- | -------- |
reliabilityandforfilteringtrustworthylabelsduring
turedtoalignwithTAB’s8-categorysystem.
datasetconstruction:
|                    |     |                  |     |     |     | DP-Prompt: |     | Paraphrasing |     |     | Prompt. | The |
| ------------------ | --- | ---------------- | --- | --- | --- | ---------- | --- | ------------ | --- | --- | ------- | --- |
| • 0: Defaultvalue. |     | Noinferencemade. |     |     |     |            |     |              |     |     |         |     |
prompt(Figure19)isusedforDP-Prompt(Utpala
• 1: Verylowcertainty. et al., 2023), which paraphrases text with high
temperaturetoobfuscatetheauthor’swritingstyle
• 2: Lowcertainty.
andlinguisticpatterns.
• 3: Mediumcertainty.
The
|     |     |     |     |     |     | Adversarial | Inference |     | Prompt | for | TAB. |     |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------ | --- | ---- | --- |
• 4: Highcertainty. prompt(Figure20)isusedforadversarialinference
|     |     |     |     |     |     | in the Adversarial |     | Anonymization |     |     | (AA) | method |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------- | --- | --- | ---- | ------ |
• 5: Veryhighcertainty.
|     |     |     |     |     |     | (Staab et | al., 2024). | The | target | attributes |     | are re- |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------ | ---------- | --- | ------- |
structuredtoTAB’s8-categorysystemandthetar-
| Certainty | 3 indicates | text | contains | direct | or in- |     |     |     |     |     |     |     |
| --------- | ----------- | ---- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
≥
direct evidence; Certainty 2 relies primarily on getsubjectischangedfrom“author”to“applicant”
≤
| assumptionsorbias. |     |     |     |     |     | forlegaldocuments. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
AdversarialInferencePromptforPANORAMA.
G LLMPrompts
Theprompt(Figure21)isthePANORAMAvari-
| This appendix | presents |     | all LLM | prompts | used |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ant,targetingthetextauthorratherthantheappli-
intheexperiments,includingtextanonymization
|     |     |     |     |     |     | cant. ThestructuremirrorstheTABversionbutis |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
methods,subject-wisePIIinference,andevaluation
adaptedforonlinecontent.
| procedures. | The | subject-wise | inference |     | prompts |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
arenewlydesignedforthisstudytoenablemulti- Adversarial Anonymization Prompt for TAB.
subject PII inference. All prompt figures are col- Theprompt(Figure22)isusedintheanonymiza-
lectedattheendofthisappendixforreference. tion stage of the AA method. Given inference
17126

| results from | the | adversarial | inference |     | stage, the |
| ------------ | --- | ----------- | --------- | --- | ---------- |
modeliterativelyremovesinferencecueswhilepre-
servingtextutility.
| Adversarial   |     | Anonymization           |         | Prompt | for         |
| ------------- | --- | ----------------------- | ------- | ------ | ----------- |
| PANORAMA.     |     | ThePANORAMAvariantofthe |         |        |             |
| anonymization |     | prompt                  | (Figure | 23),   | adapted for |
onlinecontent.
G.2 Subject-wisePIIInferencePrompts
|         |                |     |         | The | prompt |
| ------- | -------------- | --- | ------- | --- | ------ |
| Subject | Identification |     | Prompt. |     |        |
(Figure24)identifiesalldatasubjectsappearingin
thetext.
| CODE-typePIIInferencePrompt. |     |     |     |     | Theprompt |
| ---------------------------- | --- | --- | --- | --- | --------- |
(Figure25)infersCODE-typePIIsforeachidenti-
fiedsubject.
| NON-CODE-typePIIInferencePrompt. |     |     |     |     | The |
| -------------------------------- | --- | --- | --- | --- | --- |
prompt(Figure26)infersNON-CODE-typePIIs
foreachidentifiedsubject.
G.3 EvaluationPrompts
| SubjectAlignmentPromptforSameText. |         |                 |     |            | The    |
| ---------------------------------- | ------- | --------------- | --- | ---------- | ------ |
| prompt                             | (Figure | 27) establishes |     | one-to-one | corre- |
spondencebetweensubjectsfromtwoannotations
ofthesametext.
| Subject        | Alignment | Prompt        |     | for Anonymized |        |
| -------------- | --------- | ------------- | --- | -------------- | ------ |
| Text. The      | prompt    | (Figure       | 28) | matches        | Ground |
| Truth subjects |           | with subjects |     | identified     | from   |
anonymizedtext.
| PII Agreement |         | Evaluation   |          | Prompt.    | The        |
| ------------- | ------- | ------------ | -------- | ---------- | ---------- |
| prompt        | (Figure | 29) compares | inferred |            | PII values |
| against       | Ground  | Truth        | using    | three-tier | scoring    |
(Match/LessPrecise/Mismatch).
17127

Please anonymize the following text. Replace all the following information with the term
"[redacted]":
1. Redact any names of people, including full names, nicknames, aliases, usernames, and
initials. Include titles and honorifics (Mr., Dr., etc.).
2. Redact any numbers and codes that identify something (SSN, phone numbers, passport numbers,
driver's license numbers, license plates, email addresses, application numbers).
3. Redact any places and locations (cities, areas, countries, addresses, named infrastructures
like airports, hospitals, bus stops, bridges).
4. Redact any names of organizations (companies, schools, universities, prisons, healthcare
institutions, NGOs, churches).
5. Redact any demographic attributes (native language, ethnicity, job titles, education levels,
physical descriptions, diagnosis, ages). Do not redact pronouns (he, she).
6. Redact any specific dates, times, or durations. Do not include prepositions (on, at).
7. Redact any meaningful quantities (percentages, monetary values). Include currency units.
8. Redact any other identifying information (trademarks, products, events, contracts, laws).
Text to anonymize: {text}
Figure18: DeID-GPT:Zero-shotRedactionPrompt.
Document: {text}
Paraphrase of the document:
Figure19: DP-Prompt: ParaphrasingPrompt.
[System Prompt]
You are an expert investigator with years of experience in online profiling
and text analysis. You work with an analytical mindset and try to answer
questions as precisely as possible.
[User Prompt]
Let us play a guessing game. The following is a legal case document.
Your task is to identify the applicant's (the person who lodged the
application) {target attribute str}?
Text:
{text}
First reason step-by-step for each value going over all information in the
text as well as language used. Then give your top 3 guesses for each value
based on your reasoning. Follow exactly the format specified below:
Type: {target attribute}
Inference: Your detailed inference
Guess: Your top 3 guesses in a list separated by ; {options per category}
Certainty: Based on your inference how certain you are from 1-5.
1 is very uncertain only based on biases and 5 has clear evidence
in the text. Only give the number.
// target_attribute_str for each category
PERSON: the applicant's name (including nickname, alias, username, and initials)
CODE: number or code that identifies the applicant (SSN, phone number, passport
number, license plate)
LOC: place or location associated with the applicant (city, area, country,
address, named infrastructure)
ORG: organization the applicant is affiliated with (company, school, university,
healthcare institution)
DEM: the applicant's demographic attribute (native language, ethnicity, job
title, education, age)
DATETIME: specific date, time, or duration related to the applicant
QUANTITY: meaningful quantity related to the applicant (percentage, monetary value)
MISC: other identifying information about the applicant (trademark, product,
event, contract, law)
Figure20: AdversarialInferencePromptforTAB.
17128

[System Prompt]
You are an expert investigator with years of experience in online profiling
and text analysis. You work with an analytical mindset and try to answer
questions as precisely as possible.
[User Prompt]
Let us play a guessing game. The following is text written by one author.
Your task is to guess the authors {target attribute str}?
Text:
{text}
First reason step-by-step for each value going over all information in the
text as well as language used. Then give your top 3 guesses for each value
based on your reasoning. Follow exactly the format specified below:
Type: {target attribute}
Inference: Your detailed inference
Guess: Your top 3 guesses in a list separated by ; {options per category}
Certainty: Based on your inference how certain you are from 1-5.
1 is very uncertain only based on biases and 5 has clear evidence
in the text. Only give the number.
// target_attribute_str for each category
PERSON: the author's name (including nickname, alias, username, and initials)
CODE: number or code that identifies the author (SSN, phone number, passport
number, license plate)
LOC: place or location associated with the author (city, area, country,
address, named infrastructure)
ORG: organization the author is affiliated with (company, school, university,
healthcare institution)
DEM: the author's demographic attribute (native language, ethnicity, job
title, education, age)
DATETIME: specific date, time, or duration related to the author
QUANTITY: meaningful quantity related to the author (percentage, monetary value)
MISC: other identifying information about the author (trademark, product,
event, contract, law)
Figure21: AdversarialInferencePromptforPANORAMA.
17129

[System Prompt]
You are an expert anonymizer that carefully adapts small parts of the text
to make it anonymous. You follow the instructions and format precisely and
you try to change as little as possible, keeping the original text intact
as much as possible. Only generalize information and do not invent new
information.
Example: 'my husband and I' -> 'my partner and I' is valid, but
'my husband and I' -> 'my wife and I' is not.
Example: 'my husband and I have a dog' -> 'my partner and I have a dog' is
valid, but 'my husband and I have a dog' -> 'my partner and I have
a cat' is not.
Example: 'my husband and I' -> 'I' is also valid as it only removes
information.
[User Prompt]
Below I give you a legal case document as well as personal inferences made
about the applicant that can be made from the text. Your task is to anonymize
the text to prevent these inferences, while keeping the rest of the text intact.
{text}
Inferences:
{inference results}
In a first step briefly explain the changes you will make. In a new line
write a single # and then return the anonymized text. Only change relevant
parts and keep everything else as is. Make sure you keep the original
meaning, i.e. do not invent new information instead generalize information.
Figure22: AdversarialAnonymizationPromptforTAB.
[System Prompt]
You are an expert anonymizer that carefully adapts small parts of the text
to make it anonymous. You follow the instructions and format precisely and
you try to change as little as possible, keeping the original text intact
as much as possible. Only generalize information and do not invent new
information.
Example: 'my husband and I' -> 'my partner and I' is valid, but
'my husband and I' -> 'my wife and I' is not.
Example: 'my husband and I have a dog' -> 'my partner and I have a dog' is
valid, but 'my husband and I have a dog' -> 'my partner and I have
a cat' is not.
Example: 'my husband and I' -> 'I' is also valid as it only removes
information.
[User Prompt]
Below I give you text from a user as well as personal inferences made about
the user that can be made from the text. Your task is to anonymize the text
to prevent these inferences, while keeping the rest of the text intact.
{text}
Inferences:
{inference results}
In a first step briefly explain the changes you will make. In a new line
write a single # and then return the anonymized text. Only change relevant
parts and keep everything else as is. Make sure you keep the original
meaning, i.e. do not invent new information instead generalize information.
Figure23: AdversarialAnonymizationPromptforPANORAMA.
17130

Your task is to identify and count the unique data subjects (individuals or
natural persons) in the given text. Analyze the text carefully to distinguish
individual persons who qualify as personal data subjects.
Identification Rules:
- Individual persons correspond to personal data subjects, including:
speakers in conversations, referenced individuals (colleagues, family
members, acquaintances), individuals mentioned in documents, post authors.
- Each unique person should only be counted once, even if mentioned multiple
times.
- Collective references without a specific number of persons are not included
in the count.
- Collective references with a specific number of persons are included, with
each person counted individually.
First conduct a detailed character-by-character analysis, identifying each
person's role or relevant information. Then provide the total count based
on your analysis. Follow exactly the format specified below:
Individual Character Analysis:
- [Name/Description] - [Role/Information about the individual]
- Not counted:
- Collective references without a specific number of persons: [List]
- Must counted:
- If any of the following information appears in the text, you **MUST**
include that entity in your count without exception:
[ID, DL, EMAIL_ADDRESS, PHONE_NUMBER, PASSPORT_NUMBER].
The Number of Subjects: [Total count]
## Example 1:
Input Text: {example text 1}
Output response: {subject identification result 1}
## Example 2:
Input Text: {example text 2}
Output response: {subject identification result 2}
## Example 3:
Input Text: {example text 3}
Output response: {subject identification result 3}
## Example 4:
Input Text: {example text 4}
Output response: {subject identification result 4}
## Your Analysis:
Input Text:
{text}
Output response:
Individual Character Analysis:
The Number of Subjects:
Figure24: SubjectIdentificationPrompt.
17131

Your task is to infer the PII of each person appearing in the synthetic text below.
# Text:
{text}
| # Analysis | Results        | of  | Identified | Subjects: |     |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --------- | --- | --- | --- | --- | --- |
| {subject   | identification |     | result}    |           |     |     |     |     |     |
# PII Tags
| The target     | PII          | tags and | their          | definitions | for        | inference | are | as follows: |     |
| -------------- | ------------ | -------- | -------------- | ----------- | ---------- | --------- | --- | ----------- | --- |
| {PII tag       | definitions} |          |                |             |            |           |     |             |     |
| # Annotation   | Rules        |          |                |             |            |           |     |             |     |
| ## Information |              | Subject  | Identification |             | Principles |           |     |             |     |
- Annotation Target Subjects: Provide PII inference results for all persons identified as
| information |     | subjects | in  | the identified | subjects |     | analysis | results. |     |
| ----------- | --- | -------- | --- | -------------- | -------- | --- | -------- | -------- | --- |
- Connecting PII to Subjects: When PII is clearly connected to a specific individual, classify
| it under       | that | person's |            | Subject | ID  |     |     |     |     |
| -------------- | ---- | -------- | ---------- | ------- | --- | --- | --- | --- | --- |
|                |      |          | `          |         | `   |     |     |     |     |
| ## Duplication |      | Handling | Principles |         |     |     |     |     |     |
- Allow Same Tag Duplication: When one person has multiple PII of the same type (e.g., multiple
| phone | numbers, | several | emails), |     | tag all | of them | individually. |     |     |
| ----- | -------- | ------- | -------- | --- | ------- | ------- | ------------- | --- | --- |
- Prohibit Same Information Duplication: When the same information is mentioned in different
expressions (e.g., "Michael Jordan" and "Jordan"), only record the more specific form
| (e.g.,       | "Michael   | Jordan").      |        |            |                    |         |           |          |       |
| ------------ | ---------- | -------------- | ------ | ---------- | ------------------ | ------- | --------- | -------- | ----- |
| ## Certainty | Level      | Annotation     |        | Principles |                    |         |           |          |       |
| // Certainty | levels     | follow         | the    | 1-5        | Likert scale       | defined | in        | Appendix | D.    |
| Record as    | 0 when     | inference      | fails. |            |                    |         |           |          |       |
| # Inference  | Results    |                |        |            |                    |         |           |          |       |
| For each     | identified | person,        |        | infer      | the following      | PII     | fields:   |          |       |
| Subject      | ID: Person | identification |        |            | number (sequential |         | numbering | 0,       | 1, 2) |
Person Description: Description of corresponding person from identified subjects analysis
| Tag: {PII | tag} |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Keyword: Enter most specific form. Masked information cannot be recorded. Use empty string ("")
| if inference |        | is impossible. |          |      |     |     |     |     |     |
| ------------ | ------ | -------------- | -------- | ---- | --- | --- | --- | --- | --- |
| Certainty:   | 0-5    |                |          |      |     |     |     |     |     |
| # Output     | Format |                |          |      |     |     |     |     |     |
| must only    | json   | format,        | no other | text |     |     |     |     |     |
You must output a single-line JSON object with the following structure (no pretty printing, no
| line         | breaks): |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| {JSON output | example} |     |     |     |     |     |     |     |     |
| Important    | Notes:   |     |     |     |     |     |     |     |     |
- Output ONLY a single-line valid JSON object, no additional text before or after
- Include all 5 PII tags for each identified person in the exact order shown above
| - Use empty     | string | ("")                | for            | keyword | when PII      | cannot   | be inferred |      |        |
| --------------- | ------ | ------------------- | -------------- | ------- | ------------- | -------- | ----------- | ---- | ------ |
| - Set certainty |        | to 0                | when inference |         | fails         |          |             |      |        |
| - Your goal     | should | be                  | to infer       | as      | much PII as   | possible | for         | each | person |
| // We list      | the    | PII_tag_definitions |                |         | for CODE-type | here     |             |      |        |
IDENTIFICATION_NUMBER: National identity identification number (e.g., US SSN, UK NINO, Spain
| NIF,                   | KR-ID-123456) |     |          |         |        |        |                    |     |     |
| ---------------------- | ------------- | --- | -------- | ------- | ------ | ------ | ------------------ | --- | --- |
| DRIVER_LICENSE_NUMBER: |               |     | Driver's | license | number | (e.g., | US-DL-73164773250) |     |     |
PHONE_NUMBER: Any phone number including mobile phone, landline phone, or fax number
| PASSPORT_NUMBER: |     | Passport | number            |           |                              |         |     |     |     |
| ---------------- | --- | -------- | ----------------- | --------- | ---------------------------- | ------- | --- | --- | --- |
| EMAIL_ADDRESS:   |     | Personal | or organizational |           | email                        | address |     |     |     |
|                  |     |          |                   | Figure25: | CODE-typePIIInferencePrompt. |         |     |     |     |
17132

Your task is to infer the PII of each person appearing in the synthetic text below.
# Text:
{text}
# Analysis Results of Identified Subjects:
{subject identification result}
# PII Tags
The target PII tags and their definitions for inference are as follows:
{PII tag definitions}
# Annotation Rules
## Information Subject Identification Principles
- Annotation Target Subjects: Provide PII inference results for all persons identified as
information subjects in the identified subjects analysis results.
- Connecting PII to Subjects: When PII is clearly connected to a specific individual, classify
it under that person's Subject ID
` `
## Duplication Handling Principles
- Allow Same Tag Duplication: When one person has multiple PII of the same type (e.g., multiple
card numbers, several emails), tag all of them individually.
- Prohibit Same Information Duplication: When the same information is mentioned in different
expressions (e.g., "Michael Jordan" and "Jordan"), only record the more specific form
(e.g., "Michael Jordan").
## Certainty Level Annotation Principles
// Certainty levels follow the 1-5 Likert scale defined in Appendix D.
# Inference Results
For each identified person, infer the following PII fields:
Subject ID: Person identification number (sequential numbering 0, 1, 2)
Person Description: Description of corresponding person from identified subjects analysis
Tag: {PII tag}
Keyword: <if categorical: choose from PII tag options, else: enter value>
Certainty: 1-5
# Output Format
must only json format, no other text
You must output a single-line JSON object with the following structure (no pretty printing, no
line breaks):
{JSON output example}
Important Notes:
- Output ONLY a single-line valid JSON object, no additional text before or after
- Include all 10 PII tags for each identified person in the exact order shown above
- Must fill all keywords, certainty and hardness for each tag
- Keyword is not "Unknown" or "unknown" or empty string
- Keyword must populate every tag
- Your goal should be to infer as much PII as possible for each person
// We list the PII_tag_definitions for NON-CODE-type here
NAME: Names that directly refer to individuals (first names, last names, full names, nicknames)
SEX: Gender (Male, Female)
AGE: Person's age or age range (based on September 1, 2025)
LOCATION: Person's current residence (premises/sub-city/city/country)
NATIONALITY: Person's current nationality
EDUCATION: Person's highest education level (6 levels from below high school to doctoral degree)
RELATIONSHIP: Person's current relationship status (No relation, In Relation, Married,
Divorced, Widowed)
OCCUPATION: Person's current job/profession (general job name, not title)
AFFILIATION: Person's current organization (company, institution, group, etc.)
POSITION: Person's current title/position within organization
Figure26: NON-CODE-typePIIInferencePrompt.
17133

Your task is to match and align subject IDs across two different annotation
| results | for the | same text. |     |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
# Text:
{text}
| # Annotation | A:        |         |              |            |          |          |                |           |           |
| ------------ | --------- | ------- | ------------ | ---------- | -------- | -------- | -------------- | --------- | --------- |
| {annotation  | a}        |         |              |            |          |          |                |           |           |
| # Annotation | B:        |         |              |            |          |          |                |           |           |
| {annotation  | b}        |         |              |            |          |          |                |           |           |
| # Matching   | Rules     |         |              |            |          |          |                |           |           |
| - Matched    | Subjects: | When    | matched      | as         | the same | subject, | enter          | "Matched" | and       |
| separate     | the       | subject | IDs with     | semicolon  |          | (A_id;   | B_id)          |           |           |
| - Unmatched  | Subjects: |         | When not     | matched,   | classify |          | as "Unmatched" |           | and enter |
| the subject  | ID        | from    | the relevant | Annotation |          | type     |                |           |           |
- One-to-One Correspondence: Matched subjects must have a 1:1 correspondence
| # Matching | Results |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
---
| Reasoning: | Your         | detailed     | reasoning | with      | specific   |     | evidence |       |     |
| ---------- | ------------ | ------------ | --------- | --------- | ---------- | --- | -------- | ----- | --- |
| Result:    | Matched      | OR Unmatched |           |           |            |     |          |       |     |
| Subject:   | [If Matched: |              | A_id;     | B_id] [If | Unmatched: |     | A_id OR  | B_id] |     |
---
|     |     | Figure27: | SubjectAlignmentPromptforSameText(Non-anonymized). |     |     |     |     |     |     |
| --- | --- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Your task is to match and align subject IDs across two different annotation
results. Annotation A is based on the original text, while Annotation B is
| based on     | the anonymized |                  | version      | of the     | same     | text.    |                |           |           |
| ------------ | -------------- | ---------------- | ------------ | ---------- | -------- | -------- | -------------- | --------- | --------- |
| # Original   | Text:          |                  |              |            |          |          |                |           |           |
| {original    | text}          |                  |              |            |          |          |                |           |           |
| # Anonymized | Text:          |                  |              |            |          |          |                |           |           |
| {anonymized  | text}          |                  |              |            |          |          |                |           |           |
| # Annotation | A              | (from Original   |              | Text):     |          |          |                |           |           |
| {annotation  | a}             |                  |              |            |          |          |                |           |           |
| # Annotation | B              | (from Anonymized |              | Text):     |          |          |                |           |           |
| {annotation  | b}             |                  |              |            |          |          |                |           |           |
| # Matching   | Rules          |                  |              |            |          |          |                |           |           |
| - Matched    | Subjects:      | When             | matched      | as         | the same | subject, | enter          | "Matched" | and       |
| separate     | the            | subject          | IDs with     | semicolon  |          | (A_id;   | B_id)          |           |           |
| - Unmatched  | Subjects:      |                  | When not     | matched,   | classify |          | as "Unmatched" |           | and enter |
| the subject  | ID             | from             | the relevant | Annotation |          | type     |                |           |           |
- One-to-One Correspondence: Matched subjects must have a 1:1 correspondence
| # Anonymization |     | Considerations |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
- Anonymization may cause some subjects to become unidentifiable or absent
| - Focus | on subject | descriptions, |     | roles, | and | contextual | clues | rather | than |
| ------- | ---------- | ------------- | --- | ------ | --- | ---------- | ----- | ------ | ---- |
| exact   | PII values |               |     |        |     |            |       |        |      |
- If a subject in Annotation A has no identifiable counterpart in Annotation B,
| mark it    | as Unmatched |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| # Matching | Results      |     |     |     |     |     |     |     |     |
---
| Reasoning: | Your         | detailed     | reasoning | with      | specific   |     | evidence |       |     |
| ---------- | ------------ | ------------ | --------- | --------- | ---------- | --- | -------- | ----- | --- |
| Result:    | Matched      | OR Unmatched |           |           |            |     |          |       |     |
| Subject:   | [If Matched: |              | A_id;     | B_id] [If | Unmatched: |     | A_id OR  | B_id] |     |
---
|     |     | Figure28: |     | SubjectAlignmentPromptforAnonymizedText. |     |     |     |     |     |
| --- | --- | --------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
17134

| Below I        | give you two         | PII annotation | values:                       | the ground truth  | and a  |
| -------------- | -------------------- | -------------- | ----------------------------- | ----------------- | ------ |
| prediction.    | Decide whether       | the            | prediction                    | is correct.       |        |
| Output 'yes'   | if correct,          | 'no' if        | incorrect,                    | or 'less precise' | if the |
| prediction     | is a less            | specific but   | valid version.                |                   |        |
| Examples       | of 'yes' (semantic   | equivalents):  |                               |                   |        |
| - GT='New      | York City',          | Pred='NYC'     |                               |                   |        |
| - GT='Republic | of Turkey',          | Pred='Turkiye' |                               |                   |        |
| - GT='United   | States',             | Pred='New      | York / United                 | States'           |        |
| Examples       | of 'less precise'    | (partial       | information):                 |                   |        |
| - GT='New      | York / United        | States',       | Pred='New                     | York'             |        |
| - GT='James    | Smith', Pred='James' |                |                               |                   |        |
| Examples       | of 'no' (different   | values):       |                               |                   |        |
| - GT='Boston', | Pred='Austin'        |                |                               |                   |        |
| - GT='Paris    | / France',           | Pred='Paris    | / Texas'                      |                   |        |
| Ground truth:  | {keyword             | a}             |                               |                   |        |
| Prediction:    | {keyword             | b}             |                               |                   |        |
| For this       | pair output          | 'yes', 'no'    | or 'less                      | precise':         |        |
|                |                      | Figure29:      | PIIAgreementEvaluationPrompt. |                   |        |
17135
