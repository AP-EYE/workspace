> 원본: Thunder-DeID_2506.15266v3.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.3, 8 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
Thunder-DeID: Accurate and Efficient De-identification Framework
|     |     |     | for | Korean | Court | Judgments |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- |
SungeunHahm*1 HeejinKim*1 GyuseongLee*1 HyunjiM.Park1 JaejinLee1,2
1GraduateSchoolofDataScience,Dept.ofDataScience,SeoulNationalUniversity
2CollegeofEngineering,Dept.ofComputerScienceandEngineering,SeoulNationalUniversity
|     | {isungeuni, |     | kheejin, | ksnannaya, |     | mhj233,                                       | jaejin}@snu.ac.kr |     |     |     |     |     |
| --- | ----------- | --- | -------- | ---------- | --- | --------------------------------------------- | ----------------- | --- | --- | --- | --- | --- |
|     | Abstract    |     |          |            |     | identificationprocedureisnotcapableofhandling |                   |     |     |     |     |     |
courtjudgmentsatscale.
5202 tcO 61  ]LC.sc[  3v66251.6052:viXra Toensureabalancebetweenopenaccesstojus- Wewanttoaddressthefollowingthreeproblems
ticeandpersonaldataprotection,theSouthKo-
|     |     |     |     |     |     | of the current |     | state of | the de-identification |     |     | proce- |
| --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------------------- | --- | --- | ------ |
reanjudiciarymandatesthede-identificationof
|     |     |     |     |     |     | dure in South |     | Korea. | First, | over-reliance |     | on the |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------ | ------------- | --- | ------ |
courtjudgmentsbeforetheycanbepubliclydis-
manualmethodhasbeenamajorbottleneck,caus-
closed.However,thecurrentde-identification
processisinadequateforhandlingcourtjudg- ingadministrativestrainanddelayingpublication
|     |     |     |     |     |     | of judgments. |     | Public | accessibility |     | of judgments |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------------- | --- | ------------ | --- |
mentsatscalewhileadheringtostrictlegalre-
quirements.Additionally,thelegaldefinitions has been significantly low in South Korea, and
andcategorizationsofpersonalidentifiersare thestagnantde-identificationprocedureisoneof
| vague | and not well-suited |     | for technical | solu- |     |     |     |     |     |     |     |     |
| ----- | ------------------- | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thereasons(NationalCourtAdministrationofKo-
tions.Totacklethesechallenges,wepropose
rea,2025).Second,theautomaticde-identification
ade-identificationframeworkcalledThunder-
tool’sperformanceissurprisinglylow.From2019
| DeID, | which aligns | with | relevant | laws | and |          |       |         |          |        |     |         |
| ----- | ------------ | ---- | -------- | ---- | --- | -------- | ----- | ------- | -------- | ------ | --- | ------- |
|       |              |      |          |      |     | to 2025, | their | overall | accuracy | merely |     | spans 8 |
practices.Specifically,we(i)constructandre-
|     |     |     |     |     |     | to 15% (National |     | Assembly |     | of Korea, | 2019; | Na- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | --- | --------- | ----- | --- |
leasethefirstKoreanlegaldatasetcontaining
annotated judgments along with correspond- tional Court Administration of Korea, 2025). Fi-
ing lists of entity mentions, (ii) introduce a nally,whileexistinglawlaysoutthescopeofde-
| systematic | categorization |     | of Personally | Iden- |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
identification,howpersonalidentifiersarecatego-
tifiableInformation(PII),and(iii)developan rizedanddefinedforadministrativepracticeatthe
end-to-enddeepneuralnetwork(DNN)-based
courtisvagueandespeciallyunsuitabletobeused
de-identificationpipeline.Ourexperimentalre-
forautomatedtechnicalsolutions.
sultsdemonstratethatourmodelachievesstate-
|     |     |     |     |     |     | To overcome |     | the above |     | problems, | this | paper |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | --- | --------- | ---- | ----- |
of-the-artperformanceinthede-identification
| ofcourtjudgments. |     |     |     |     |     | proposesThunder-DeID,aDNN-andNER-based |       |          |     |     |           |       |
| ----------------- | --- | --- | --- | --- | --- | -------------------------------------- | ----- | -------- | --- | --- | --------- | ----- |
|                   |     |     |     |     |     | framework,                             | which | improves |     | the | accuracy, | effi- |
1 Introduction ciency, and consistency of de-identifying court
judgments.Unlikeaprompt-basedapproachusing
| Generally, | court proceedings |     | are open | and | acces- |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
alargelanguagemodel(LLM),whichoftenalters
sibletothepublic.Itisoneofthekeydemocratic
theoriginalsentencestructureintheprocessofdei-
principles enshrined in the constitutions of many dentificationtask(e.g.,“총3명(atotalofthreepeo-
countries,includingSouthKorea1.SouthKoreais
ple)”alteredto“총명수1(atotalofoneperson)”),
oneofthecountrieswithmorestringentconditions
|     |     |     |     |     |     | the token-level |     | classification |     | method | of Thunder- |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | --- | ------ | ----------- | --- |
thatcoverabroaderrangeofpersonalidentifiersto DeIDeliminatessuchrisksofsentenceandcontext
beanonymizedinthecourtsetting.
|        |                 |     |       |            |     | distortion(seeAppendix |     |     | A).Moreover,duetopri- |     |     |     |
| ------ | --------------- | --- | ----- | ---------- | --- | ---------------------- | --- | --- | --------------------- | --- | --- | --- |
| Before | the publication | of  | court | decisions, | the |                        |     |     |                       |     |     |     |
vacyandinformationsecurityconcerns,theuseof
| Korean National | Court | Administration |     | uses | both |     |     |     |     |     |     |     |
| --------------- | ----- | -------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
API-basedLLMservices,suchasChatGPT,isre-
manual and automated de-identification meth- strictedinmanyofthekeygovernmentinstitutions
| ods throughout | four stages |          | of processing |     | and re- |          |                                       |         |      |            |     |     |
| -------------- | ----------- | -------- | ------------- | --- | ------- | -------- | ------------------------------------- | ------- | ---- | ---------- | --- | --- |
|                |             |          |               |     |         | inKorea  | (NationalIntelligenceService,2023).To |         |      |            |     |     |
| view (Judicial | Policy      | Research | Institute     |     | of Ko-  |          |                                       |         |      |            |     |     |
|                |             |          |               |     |         | create a | trainable                             | dataset | from | anonymized |     | and |
rea, 2021). However, the current state of the de- unannotated court judgment data, we first manu-
allylabel6,700civil,criminal,andadministrative
*Equalcontribution.
1ConstitutionofSouthKorea,Art.109 law cases that cover a broad spectrum of scenar-

Publicly Available  AnnotatedJudgment PII Scheme & Replacement List Reconstructed realistic judgment
De-identified Judgments
PII
|      |     |             |     |                             | ... 피고인  |     |     |     |     |                              | ... 피고인  |     |     |
| ---- | --- | ----------- | --- | --------------------------- | -------- | --- | --- | --- | --- | ---------------------------- | -------- | --- | --- |
| Data |     |             |     | <<<내국인이름>>>A<<</내국인이름>>>는s  |          |     |     |     |     |                              |          |     |     |
|      |     | ... 피고인 A는  |     |                             |          |     |     |     |     | <<<내국인이름>>>김철수<<</내국인이름>>>는  |          |     |     |
preparation B 은행에서... <<<은행>>>B<<</은행>>> 은행에서... <<<은행>>>신한<<</은행>>> 은행에서...
|     |                             |     |                |                                                                                    |     |     | 내국인이름 |       | 은행    |     |     |     |     |
| --- | --------------------------- | --- | -------------- | ---------------------------------------------------------------------------------- | --- | --- | ----- | ----- | ----- | --- | --- | --- | --- |
|     |                             |     |                |                                                                                    |     |     | •     | 김 철 수 | • 신 한 |     |     |     |     |
|     | “Defendant A was at B bank” |     |                | *내국인이름: Korean names                                                               |     |     |       |       | 우 리   |     |     |     |     |
|     |                             |     |                | *은행: Banks                                                                         |     |     | •     | 홍 길 동 | •     |     |     |     |     |
|     |                             |     | Tokenized text | [피, 고인, <<<내국인이름>>>,  김,   철수, <<</내국인이름>>>, 는,  <<<은행>>>, 신,한, <<</은행>>>, 은행, 에서] |     |     |       |       |       |     |     |     |     |
Tokenization
D
|     |     |     | Token ID sequence | [2700, 5,                            3445,  723,                             622,                 1618,7386,  |             |            |                         |     |               |     | 4602,  135] |     |     |
| --- | --- | --- | ----------------- | ------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | ----------------------- | --- | ------------- | --- | ----------- | --- | --- |
|     |     |     | Ground truth      |                                                                                                               | [  O,    O, | K o r ea n | ,  K   o  r ea n ,      | O,  | Banks, Banks, |     | O,      O ] |     |     |
|     |     |     |                   |                                                                                                               |             | n a m e s  | n a m e s               |     |               |     |             |     |     |
Training [2700, 5, 3445, 723 , 622, 1618,7386, 4602,  135] Sㄴ Thun d e r -D eID  [O,    O,K o r ea n ,  K   o  r ea n ,  O   ,Banks, Banks,O,  O  ]
|     |     |     |     |     |     |     | M   | o d e l |     | n a m e s n a | m e s |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | ----- | --- | --- |
Figure1:OverviewofThunder-DeID.
2 RelatedWork
iosincivil,criminal,andadministrativelaw.From
theseannotations,whichidentified48,306named
|     |     |     |     |     |     |     | Among | others, | there | are many | de-identification |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ----- | -------- | ----------------- | --- | --- |
entities,weestablishahierarchicalcategorization
|     |     |     |     |     |     |     | studies | in  | health information. |     | In  | the USA, | de- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------------- | --- | --- | -------- | --- |
schemeforPIIthatalignswithrelevantlawsand
identificationinthemedicalfieldisguidedbythe
| practices | and | is suitable |     | for model | training. | For |        |           |             |     |     |                |     |
| --------- | --- | ----------- | --- | --------- | --------- | --- | ------ | --------- | ----------- | --- | --- | -------------- | --- |
|           |     |             |     |           |           |     | Health | Insurance | Portability |     | and | Accountability |     |
eachofthe729labelsinthePIIscheme,wecurate
|                 |     |      |           |          |     |           | Act   | (HIPAA)   | (U.S.  | Department |         | of Health | and      |
| --------------- | --- | ---- | --------- | -------- | --- | --------- | ----- | --------- | ------ | ---------- | ------- | --------- | -------- |
| a corresponding |     | list | of entity | mentions |     | to gener- |       |           |        |            |         |           |          |
|                 |     |      |           |          |     |           | Human | Services, | 1996), | which      | defines |           | two main |
atemodeltrainingdata,asillustratedinFigure1.
strategiesforcompliance:theSafeHarbormethod
Furthermore,wedesignade-identificationpipeline
|     |     |     |     |     |     |     | and | Expert | Determination |     | (Meystre | et  | al., 2010; |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | -------- | --- | ---------- |
fortheDNN-basedlanguagemodel,incorporating
|               |     |           |      |           |     |        | Emelyanov, |     | 2021). The | Safe | Harbor | method | re- |
| ------------- | --- | --------- | ---- | --------- | --- | ------ | ---------- | --- | ---------- | ---- | ------ | ------ | --- |
| a specialized |     | tokenizer | that | leverages | the | unique |            |     |            |      |        |        |     |
quirestheremovalof18identifierscalledPersonal
characteristicsoftheKoreanlanguage.
|     |     |     |     |     |     |     | Health        | Information |        | (PHI).           | Alternatively, |     | Expert     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ------ | ---------------- | -------------- | --- | ---------- |
|     |     |     |     |     |     |     | Determination |             | relies | on a statistical |                | or  | scientific |
Theapproachusedinthispapermayoffervalu- methodtoensureminimalre-identificationrisk.In
ableinsightsforotherjurisdictionslookingtoeffi-
|     |     |     |     |     |     |     | Europe, | the | General | Data Protection |     | Regulation |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --------------- | --- | ---------- | --- |
cientlyanonymizelargevolumesofcourtdecisions.
(GDPR)(EuropeanParliamentandCouncil,2016)
Thecontributionsofthispaperaresummarizedas
guidesthede-identificationofpersonalinformation
| follows: |     |     |     |     |     |     | inmedicaldata.Inthispaper,weproposeathree- |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
tieredPIIschemeforthede-identificationofcourt
| • We  | have | created | a two-part |           | dataset | that con- | judgment.                 |     |     |     |                   |     |     |
| ----- | ---- | ------- | ---------- | --------- | ------- | --------- | ------------------------- | --- | --- | --- | ----------------- | --- | --- |
| sists | of   | 6,700   | labeled    | judgments | from    | three     |                           |     |     |     |                   |     |     |
|       |      |         |            |           |         |           | Medicalde-identification. |     |     |     | Researchinmedical |     |     |
kindsofcases:civil,criminal,andadministra-
de-identificationhasevolvedthroughthreemajor
tivecasesandalistofactualentitymentionsto
technicalapproaches.Earlyeffortsprimarilyrelied
replacethelabels.Thelabeledjudgmentsare
|         |     |      |          |           |            |     | onrule-basedsystems |     |     | (Uzuneretal.,2007).With |     |     |     |
| ------- | --- | ---- | -------- | --------- | ---------- | --- | ------------------- | --- | --- | ----------------------- | --- | --- | --- |
| created |     | from | publicly | available | anonymized |     |                     |     |     |                         |     |     |     |
theadvancementofdeeplearning,learning-based
courtjudgments.
|       |         |     |                |          |               |           | de-identification |       | approaches,   |          | such       | as     | BiLSTM- |
| ----- | ------- | --- | -------------- | -------- | ------------- | --------- | ----------------- | ----- | ------------- | -------- | ---------- | ------ | ------- |
| • We  | propose |     | a three-tiered |          | PII framework |           |                   |       |               |          |            |        |         |
|       |         |     |                |          |               |           | CRF               | (Liu  | et al., 2017) | and      | BERT-based |        | NER     |
| based | on      | an  | inductive      | analysis |               | of 48,306 |                   |       |               |          |            |        |         |
|       |         |     |                |          |               |           | models            | (Berg | et al.,       | 2020; An | et al.,    | 2025), | were    |
namedentitiesidentifiedinourdataset.
introduced.Largelanguagemodels(LLMs)have
• Weproposeatokenizerthatintegratesamor-
beenrecentlyexploredforde-identificationinzero-
phologicalanalyzer,Mecab-ko,withBytePair
|          |     |       |     |          |            |      | shotorfew-shotsettings |     |     | (Liuetal.,2023;Altalla’ |     |     |     |
| -------- | --- | ----- | --- | -------- | ---------- | ---- | ---------------------- | --- | --- | ----------------------- | --- | --- | --- |
| Encoding |     | (BPE) | to  | leverage | the unique | fea- |                        |     |     |                         |     |     |     |
etal.,2025).However,practicaldeploymentisvery
turesoftheKoreanlanguage.Usingthistok-
limitedbecauseHIPAAregulationscanbeviolated.
enizer,wealsoproposeamethodforgenerat-
ingtrainingdatafromourlabeleddatasetand De-identification of court judgments. In re-
replacementlist.
|     |     |     |     |     |     |     | cent | years, | there has | been growing |     | interest | in au- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --------- | ------------ | --- | -------- | ------ |
• We evaluate Thunder-DeID and it achieves tomatingthede-identificationofcourtjudgments
the highest performance among existing de- based on NER. Many countries have launched
identificationmodelsforcourtjudgments.
|     |     |     |     |     |     |     | government-led |     | initiatives | to  | adopt | technical | so- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ----- | --------- | --- |

|     |     | Domain | Casetype |                         |     | Documents | Entities  |     |
| --- | --- | ------ | -------- | ----------------------- | --- | --------- | --------- | --- |
|     |     |        |          | Compensationfordamage   |     |           | 901 9,223 |     |
|     |     |        |          | Securitydepositdisputes |     |           | 696 5,187 |     |
Civil
|     |     |                |     | Paymentofpurchaseprice   |     |     | 557 4,983    |     |
| --- | --- | -------------- | --- | ------------------------ | --- | --- | ------------ | --- |
|     |     |                |     | Eviction                 |     |     | 846 6,816    |     |
|     |     |                |     | Subtotal                 |     |     | 3,000 26,209 |     |
|     |     |                |     | Bodilyinjury             |     |     | 600 2,562    |     |
|     |     |                |     | Violence                 |     |     | 600 2,583    |     |
|     |     | Criminal       |     | Sexualmisconduct         |     |     | 600 2,732    |     |
|     |     |                |     | Propertytheft&deception  |     |     | 600 4,376    |     |
|     |     |                |     | Drunkdriving             |     |     | 600 2,354    |     |
|     |     |                |     | Subtotal                 |     |     | 3,000 14,607 |     |
|     |     | Administrative |     | Administrativelitigation |     |     | 700 7,490    |     |
|     |     |                |     | Subtotal                 |     |     | 700 7,490    |     |
|     |     | Total          |     |                          |     |     | 6,700 48,306 |     |
Table1:Numberofdocumentsandentitiesforeachcasetypeinthedataset.
lutionstotackleproblemswiththelabor-intensive in South Korea. First, since de-identification of
de-identification procedure. The manual process- courtjudgmentspriortopublicationisalegalobli-
ing has been highlighted as delaying public dis- gationofjudicialinstitutions2,andonlythefully
closureandpublicationofjudgmentsinItalyand anonymized judgments are available for external
Uruguay (Salierno et al., 2024; Garat and Won- use,weneedamethodtogeneratedatasetsusing
sever,2022).InIndia,themostpopulouscountry anonymizedandunannotateddata.
in the world, such a turn to automation is essen- Second,therearelegalrulestodefinecategories
anonymized3.
tial due to the overwhelming volume of court de- of personal identifiers to be How-
cisions (Kalamkar et al., 2022). In Switzerland, ever,theyarenotdetailedenoughtocovervarious
automation has been introduced to assist court attributes related to the persons involved in pro-
officials and legal experts in the anonymization ceedings. They merely provide a direct identifier
process (Niklaus et al., 2023). These NER-based categoryandabroadquasi-identifiercategorythat
methods report Precision, Recall, and F1-scores includesanyotherinformationthatcanidentifythe
| of 96.43%, | 95.86%, | 96.14% | for Arabic | (Mous- | individual. |     |     |     |
| ---------- | ------- | ------ | ---------- | ------ | ----------- | --- | --- | --- |
saoui et al., 2023), 92.26%, 92.57%, 92.40% for Finally,sincetheSouthKoreanjudiciaryheavily
German, French, and Italian texts (Switzerland), relies on manual de-identification, which is time-
89.92%,90.50%,91.90%forSpanish(Uruguay), consuming (National Assembly of Korea, 2019;
92.00%, 90.20%, 91.10% for Indian texts, and NationalCourtAdministrationofKorea,2025),a
85.00%,92.46%,88.60%forItaliantexts(Italy). largevolumeofcourtrulingsthatcanimmediately
beusedasalegalcorpusfortrainingisnotavail-
Havingasubstantialpost-processingapproach
| is critical | in de-identifying |     | court | judgments. | able. |     |     |     |
| ----------- | ----------------- | --- | ----- | ---------- | ----- | --- | --- | --- |
Forinstance,over-anonymizationorunprincipled
3.1 DataCollection
| anonymization | may | undermine | the readability | of  |     |     |     |     |
| ------------- | --- | --------- | --------------- | --- | --- | --- | --- | --- |
rulings when publicly disclosed (Judicial Policy Weinitiallycompile6,700anonymizedcourtdeci-
Research Institute of Korea, 2023). The majority sionsfromadatasetprovidedbyKoreanMinistry
|     |     |     |     |     | ofGovernmentLegislation4,AI-hub5 |     |     | andHwang |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- | -------- |
ofpreviousstudies(Oksanenetal.,2022;Niklaus
|     |     |     |     |     | et al. | (2022)6. | After removing | duplicates across |
| --- | --- | --- | --- | --- | ------ | -------- | -------------- | ----------------- |
etal.,2023;Saliernoetal.,2024)focusonhowto
detectpersonalidentifiersincourtjudgmentsusing differentsources,thefinaldatasetcomprises3,000
civil,3,000criminal,and700administrativecases.
NER,andlessattentionhasbeenpaidtodiscussing
Ourdatasetencompassesawiderangeofcivil,
howtheidentifiedentitiesshouldbehandledinthe
post-processingstage.AlthoughtheUruguaystudy criminal,andadministrativescenarios,assumma-
brieflyaddressesthisissue,broaderdiscussionand rizedinTable1.Bydoingthis,ourdatasetisbet-
systematicapproachesremainlimited. 2Korean Criminal Procedure Act, Art. 59-3; Korean Civil
ProcedureAct,Art.163-2
3Korean
| 3 Methods |     |     |     |     |     | Supreme | Court Regulation | No. 2809 and Judicial |
| --------- | --- | --- | --- | --- | --- | ------- | ---------------- | --------------------- |
RuleNo.1778
4https://www.moleg.go.kr/
Therearethreechallengesuniquetoconstructing
5https://www.aihub.or.kr/
datasetsforthede-identificationofcourtjudgments 6ThedatasetisreleasedundertheCCBY-NC4.0license.

tersuitedforidentifyingvarioustypesofdomain- identifiersinvolved,individualscanberepresented
specificpersonalidentifiersincourtjudgements. with English letters (e.g., A and B) or combina-
Wefocusoncollectingjudgmentsrenderedby tionsofletters(e.g.,ABB,AAB).Thecompletere-
courts of first instance. A significant portion of movalofcertaindirectidentifiers,suchasresident
thesejudgmentsinKoreaisdedicatedtoexamin- registration numbers, is mandatory. For example,
ing and clarifying facts, which is different from thetext"...피고인홍길동(561231-1234567)..."
the approach taken in common law countries. At ("... defendant Hong Gildong (561231-1234567)
thislevel,thecourtsprioritizefact-findingandre- ...") would be anonymized to "... 피고인 A (주
solvingdisputedfactsbasedontheinvestigations 민등록번호1)..."("...defendantA(residentreg-
andevidencepresentedincourt.Consequently,the istration number 1) ..."), where 561231-1234567
collectedjudgmentscontainnumerousdirectand is a specific resident registration number. In this
quasi-identifiersrelatedtomultipleindividualsin- case,"피고인A(주민등록번호1)"representsthe
volvedintheproceedings. anonymized information obtained from the judg-
mentwithinthecollectedcorpusandisnotlabeled
3.2 AnnotationScheme
or annotated. The resident registration number is
We need a systematic annotation scheme for the designated as 1 to differentiate between multiple
annonymizedcourtjudgmentstoensurethatdata individualspresentinthejudgment.
labelingisconsistent,reliable,andusefulforour Annotators manually identify the placehold-
DNN-basedde-identificationprocess.Thelabeling ers A and 1, labeling them to indicate the spe-
process following the annotation scheme should cific types of entities they represent as follows:
be consistent across annotators and reproducible. "... ≪내국인이름≫A≪/내국인이름≫(≪주
Theschemeshouldalsospeeduptrainingfornew 민등록번호≫B≪/주민등록번호≫)...,"where
annotators and helps maintain quality over large "내국인이름" refers to Korean names, and "주민
datasets. 등록번호" refers to a resident registration num-
Without legal rules defining all relevant cate- ber.≪내국인이름≫and≪/내국인이름≫are
goriesofpersonalidentifiers,wedevelopananno- markers and they point the beginning and end of
tation scheme in four phases. First, human anno- theentitymention,respectively."내국인이름"isa
tatorsidentifyplaceholders(i.e.,theanonymized labeltorepresentthecategoryoftheentitymention
sectionsinthejudgment)intheprovidedtextand inourPIIscheme(seeAppendix B).
labelthemusingasetofentitycategoriesweini- Inanadjudicationsetting,locationalinformation,
tially prepared based on an analysis of existing suchastheresidentialaddressesofthepartiesin-
laws and practices. Second, while reviewing the volvedinacaseandtheaddressofthecrimescene,
labelingresultsforconsistencyamongdifferentan- isessentialforconfirmingthecourt’sjurisdiction.
notators,weestablishanewannotationschemefor Itisstandardpracticetoprovidetheexactaddress;
PIIwithathree-tieredhierarchicalstructurethat however,underKoreanJudicialRuleNo.1778,spe-
classifiesarangeofentitytypes.Third,annotators cificlower-leveldetailsoftheaddress,likedistricts
makeadjustmentsandcorrectionsaccordingtothe andstreets,mustbemasked.Atfirstglance,thead-
annotationscheme.Finally,weresolveanyissues dressofalocationorthenameofaplacemaynot
whereannotatorsmaydisagreeorhavedoubts. seemlikeidentifyinginformation.However,their
directassociationwithspecificcriminalactivities
3.3 PlaceholderDetectionandLabeling
can help identify the individuals involved in the
We have seventeen annotators who are fluent in case.Therefore,inaccordancewithexistinglaws
KoreanandpossessagoodunderstandingofNLP. andpractices,lower-leveladdresscomponentsand
Theyhavecompletedaninitialtrainingsessionthat the names of all incident-related places must be
providedguidelinesontwomainaspects:thekey de-identified.Similarly,contextualattributessuch
features of the task, which include a multi-stage as the date of an event may also be considered
processwedesignedforthisproject,andtherules quasi-identifiersandshouldbemasked.Formore
regardingthescopeandmethodofanonymization examplesofmaskingandlabeling,pleaseseeAp-
asappliedincourtpractice. pendixC.
KoreanJudicialRuleNo.1778establishesprin- Annotators identified and labeled a total of
ciplestoguidecourtofficialsinusingvariousde- 48,306 named entities across 6,700 court judg-
identificationmethods.Dependingonthetypeof ments. Table 1 shows the number of documents

and identified entities for the crime categories in
Personally Identifiable Information (PII)
thecollectedjudgments.
First tier
Direct-identifiers Quasi-identifiers Second tier
3.4 PIICategories Third tier
인명 사건관계인이력
Asdiscussedearlier,existinglawbroadlydefines (Names) (Work and criminal backgrounds)
thescopeofde-identification.Asidefromcleardi- 연령정보 사건관련숫자정보
(Age and date of birth) (Incident-related numerical information)
rectidentifiers,quasi-identifiersoftenrequiremore 사건관련장소
이메일주소
(Incident-related locations)
than just a textual assessment of the relevant at- (Email addresses)
지리정보
tributes that can make an individual identifiable. 주민등록번호 (Geographicinformation)
(Resident registration number)
조직
Thescopecanbeasextensiveas"anyotherinfor- (Organizations)
mationidentifyingthepersonsinvolvedinthecase 기관및시설
(Institutions and facilities)
and third parties"7. Since it is nearly impossible
사업체
(Corporate entities)
to list all privacy-sensitive identifiers in writing,
온ㆍ오프라인방송 상품일반
courtofficialsareinstructedtousediscretionand (Streaming and broadcasting service) (Consumer products)
analyzethespecificcontextanditsconnectionto (Online p 플 la 랫 tfo 폼 rm 일 s 반 in general) (Media an 방 d 송 te 통 lec 신 o 서 m 비 mu 스 nications)
theindividualsinvolvedinthecase. 전자상거래 금융서비스
(E-commerce) (Financial products and services)
Duringtheinitialreviewoflabeling,wefound … 사회문화
(Culture and society)
that many of the identified entities, specifically,
소셜미디어
theinformationanonymizedinthecollectedjudg- (Social media) URL
ments, do not consistently fit within the prede-
Figure2:Thethree-tieredcategorizationschemeforPII
finedcategoriesofidentifiers.Therearechalleng-
inthedomainoflawandadjudication.
ing cases where the same type of entity may be
evaluateddifferentlyacrossmultiplejudgments.
Forexample,asageneralrule,namesofgovern-
organizations,eachmemberresponsiblefordiffer-
mentinstitutionsandpublicauthorities(suchasthe
entaspectsofthecriminalactivities.Additionally,
SeoulPoliceAgencyandtheSeoulCorrectionalIn-
intrialsinvolvingaccomplicestoacrime,itiscru-
stitution)arenotsubjecttode-identification.How-
cial to anonymize identifiable information about
ever,iftheseorganizationsareassociatedwiththe
various third parties, such as witnesses, apprais-
locationwhereacrimewascommitted,exceptions
ers, and forensic experts, to mitigate the risk of
may apply. This contextual interpretation of the
retaliation.
casecanleadtovaryingoutcomes.
Foranotherexample,considerthefollowingde-
Whiletheannotatorsmadeadjustmentsandcor-
identifiedjudgmenttext:"...피고인F와피해자G
rectionsinaccordancewiththeannotationscheme,
는H교도소I팀소속의교정공무원으로..."("...
we resolved any issues where the annotators dis-
defendant F and victim G were prison officers at
agreedorhaduncertainties.
teamIofHcorrectionalinstitution...").Inactual
de-identificationpractice,thenameofthecorrec-
After reviewing all the named entities in the
tionalinstitution("교도소")isanonymizedbecause
judgments,wedevelopedourownPIIannotation
itidentifiestheworkplacewhereboththedefendant
scheme that classifies various entity types into
andvictimwerecolleagues.Ifthisinformationis
two main categories: direct identifiers and quasi-
notanonymizedinpublicdisclosures,itcouldin-
identifiers.Thisschemeincludes16subcategories
creasethechancesofidentifyingthetwoindividu-
and 80 granular categories. Figure 2 illustrates
alsduetoitsdirectconnectiontothecircumstances
the hierarchy of the categories. Each of the third-
surroundingthecrimecommitted.
tier categories is associated with labels for anno-
Adifferentchallengeinannotationariseswhen
tation.Usingthisscheme,weannotatedtheiden-
there are many individuals involved, and the spe-
tifiednamedentitieswithatotalof729labels.To
cific roles each person plays in the case are not
the best of our knowledge, this is the first PII an-
clearlydefinedduringtheanonymizationprocess.
notation scheme specifically designed for the de-
Thisisparticularlyevidentincasesoffraud,where
identificationofcourtjudgmentsinKorea.Further
alargegroupofvictimsisoftentargetedbyillegal
detailsontheannotationschemeanditscategories
7KoreanJudicialRuleNo.1778,Art.4 areprovidedinAppendixD.

|     |     |     | Defining a Unique Pair of Entity Tags |     |     |     |     | Mapping Special Token IDs    |     |     |     |     |
| --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
|     |     |     | <<<내국인이름>>> : <<</내국인이름>>>            |     |     |     |     | <<<128003>>> : <<</128004>>> |     |     |     |     |
Preprocessing
<<<은행>>> : <<</은행>>>
<<<128005>>> : <<</128006>>>
*내국인이름: Korean names, 은행: Banks
|     |     |     | Annotated text | “피고인<<<내국인이름>>>L<<</내국인이름>>>이” |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
*Defendant L
|     |     |     |     |      |     |        | Tokenizing |     | List of entity mentions |       |     |     |
| --- | --- | --- | --- | ---- | --- | ------ | ---------- | --- | ----------------------- | ----- | --- | --- |
|     |     |     |     | 2700 | 5   | 128003 | 89 128004  | 39  |                         | 내국인이름 |     |     |
Training
|     | DataGeneration |                |     |      |     |              |                  | [562, 358] |     | • 홍길동 |     |     |
| --- | -------------- | -------------- | --- | ---- | --- | ------------ | ---------------- | ---------- | --- | ----- | --- | --- |
|     |                |                |     |      |     |              | Replacing        |            |     | • 김철수 |     |     |
|     |                |                |     | 2700 | 5   | 128003       | 562   358 128004 | 39         |     |       |     |     |
|     |                | Label sequence |     | [O,  | O,  | Koreannames, | Korean names,    | O]         |     |       |     |     |
Figure3:Tokenizationandtrainingdatageneration.
| 3.5 | ReplacementLists |     |     |     |     |     | 3.6 TrainingDataGeneration |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
To improve the size and diversity of our training When we train our language model, we generate
data,wecreateanextensivelistofentitymentions trainingdatafromtheannotateddataset.Inthispro-
usingtwodifferentmethods:manualcurationand cess,wereplacethelabelsinthedatasetwithactual
rule-basedgeneration. entity mentions in the replacement list. Each la-
beledcourtjudgmentisaugmentedmultipletimes
| Manualcuration. |     |     | Weselectivelychoosereliable |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Ntimes)throughentitymentionreplacementsto
andverifiedinformation(entitymentions)sourced
maximizetheamountoftrainingdata.
fromtheKoreangovernment’slicensingdatabases8
|     |     |     |     |     |     |     | For model | training, | documents |     | are converted |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | --- | ------------- | --- |
andpublicdataportals9.Wegenerateentitymen-
intotokenizedinputsequences(referredtoasX)
tions for the majority of labels—691 out of 729. andcorrespondinglabelsequences(referredtoas
| Our | goal | is to compile |     | an average | of  | at least 100 |                   |     |      |          |            |     |
| --- | ---- | ------------- | --- | ---------- | --- | ------------ | ----------------- | --- | ---- | -------- | ---------- | --- |
|     |      |               |     |            |     |              | Y). Our tokenizer | has | been | extended | to include |     |
itemsforeachlabel.
|     |         |         |          |     |                 |     | 1,458 special | tokens that | represent |     | 729 different |     |
| --- | ------- | ------- | -------- | --- | --------------- | --- | ------------- | ----------- | --------- | --- | ------------- | --- |
|     | We also | conduct | searches | on  | domain-specific |     |               |             |           |     |               |     |
entities(labels).Thisextensionisprioritizedtoen-
websitestocollectentitynamesrelatedtospecial-
|     |     |     |     |     |     |     | sure that | proper nouns | do  | not merge | with | other |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --------- | ---- | ----- |
izedlocations.Forexample,wegatherlistsofexhi-
particles.Eachjudgmentdocumentistransformed
bitionhallsandconventionsfromtheCoexCenter,
intoatokensequence,wheresubsequencesmarked
obtain names of ships and vessels from the Ko- withthestarttoken≪,placeholdertokens,andthe
reaSeafarer’sWelfare&EmploymentCenter,and
|         |       |     |              |     |           |      | end token | ≫ (e.g., "≪name≫A≪/name≫" |     |     |     |     |
| ------- | ----- | --- | ------------ | --- | --------- | ---- | --------- | ------------------------- | --- | --- | --- | --- |
| collect | names | of  | junk dealers | and | recycling | com- |           |                           |     |     |     |     |
aftertokenization)arereplacedwithactualentity
panies from the Korea Waste Recycling Institute. mentiontokensequences("홍길동"aftertokeniza-
Additionally,weperformgeneralwebsearchesto
|     |     |     |     |     |     |     | tion). Tokens | within | these | subsequences |     | are as- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ----- | ------------ | --- | ------- |
supplementtheseresults,ensuringabroadanddi-
|     |     |     |     |     |     |     | signedtherelevantlabelinY |     |     | (e.g.,"name")forde- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ------------------- | --- | --- |
versesetofentitymentionsthataccuratelyreflect
identification,whiletokensinothersubsequences
real-worldusage. receivean"O"(outside)labelinY toindicatethat
theydonotrequirede-identification.
| Rule-based |     | generation. |     | The | second | strategy |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
usesrule-basedgenerationtocreateentitymentions
3.7 Tokenization
involvingpersonalidentifiersinstandardizedand
Wedevelopacustomtokenizertrainedonasubset
structuredformats.Simplerulesareemployedto
ofonemillionsentencessampledfromourcorpus
generateentitiessuchasKoreannames,addresses
|     |     |     |     |     |     |     | to effectively | segment | sensitive | entities, | such | as  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --------- | --------- | ---- | --- |
inKorea,andnumericalidentifiers,whichinclude
namesandorganizations.Ourtokenizerintegrates
residentregistrationnumbers,phonenumbers,and
adictionary-basedmorphologicalanalyzer,Mecab-
bankaccountnumbers.
|     |     |     |     |     |     |     | ko10, with | Byte Pair | Encoding | (BPE) | (Sennrich |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | -------- | ----- | --------- | --- |
8https://www.localdata.go.kr/main.do
9https://www.data.go.kr/ 10https://github.com/hephaex/mecab-ko

| etal.,2016). |          |     |     |        |         |         | inthesequence[2700,5,128003,82,128004,39], |          |     |             |             |     |
| ------------ | -------- | --- | --- | ------ | ------- | ------- | ------------------------------------------ | -------- | --- | ----------- | ----------- | --- |
|              |          |     |     |        |         |         | the segment                                | [128003, |     | 82, 128004] | is replaced | by  |
| We choose    | Mecab-ko |     | due | to its | ability | to han- |                                            |          |     |             |             |     |
dletheKoreanlanguage’sagglutinativemorphol- a token sequence [562, 358], which represents a
ogy.Itsegmentstextintomorphemesusingapre- name"홍길동"inthereplacementlist.Thisresults
intheupdatedsequence:[2700,5,562,358,39].
| defined | dictionary, | accurately |     | distinguishing |     | be- |     |     |     |     |     |     |
| ------- | ----------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tweennouns,particles,affixes,andadjectives.Stud- Subsequently, a corresponding label sequence
ies have demonstrated Mecab-ko’s effectiveness is generated based on the indices of the replaced
forrecognizingdomain-specifictermsandproper tokens,ensuring thattheposition andtypeof the
nounsinKoreanNLPtasks(Parketal.,2020;Cho labeledentityareretained(i.e.,marking"홍길동"
etal.,2021;Jeonetal.,2023). as a Korean names). For instance, the token se-
UnlikeEnglish,wherepropernounslike"홍길 quence [2700, 5, 562, 358, 39] generates the la-
동" remain unsegmented, Korean attaches nomi- belsequence[O,O,Koreannames,Koreannames,
nativeparticles,suchas"-이"and"-을,"tonouns O],where"O"represents"Outside".Thislabelse-
(e.g., "홍길동이"). Mecab-ko’s dictionary-based quence serves as the ground truth for supervised
segmentationseparates"홍길동이"into"홍길동" learning.Finally,themodifiedtokensequenceand
itsassociatedlabelsequenceformatrainingdata
| and "-이", | ensuring | that | only | the target | entity | ("  |     |     |     |     |     |     |
| --------- | -------- | ---- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
홍길동") is de-identified while the particles re- instanceinthedataset(Figure3).
mainintact.Thisapproachhelpsthede-identified
|     |     |     |     |     |     |     | 3.8 DataAugmentation |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
textflowsmoothlyandnaturally.Inaddition,such
| precision | is essential, | given | that | the | original | (i.e., |        |             |              |     |             |        |
| --------- | ------------- | ----- | ---- | --- | -------- | ------ | ------ | ----------- | ------------ | --- | ----------- | ------ |
|           |               |       |      |     |          |        | Due to | the limited | availability |     | of publicly | acces- |
unanonymized and unannotated) court decisions siblecourtjudgments,therewillinevitablybein-
lackclearboundariesforallentities. stances where new entity types arise that the ex-
While using a morphological analyzer like istingPIIlabelscannotrepresent.Toaddressthis
| Mecab-ko | is powerful, |     | its fixed | dictionary |     | may |             |     |         |       |               |        |
| -------- | ------------ | --- | --------- | ---------- | --- | --- | ----------- | --- | ------- | ----- | ------------- | ------ |
|          |              |     |           |            |     |     | limitation, | we  | prepare | a set | of additional | labels |
not be able to capture rare legal terms or proper usingLLM-assistedaugmentation.
nouns,leadingtoout-of-vocabulary(OOV)issues. We begin by selecting specific granular cate-
Toovercomethislimitation,wechoseBPE,which gories that have significantly fewer labels com-
buildsavocabularythroughfrequentcharacterpair
paredtoothers.Next,weemployalargelanguage
merges and represents unseen terms as subword model(LLM),suchasChatGPT(OpenAI,2022),
| units.       |            |     |     |           |     |        | togenerateadditionallabelsandcreatecorrespond- |           |           |        |               |            |
| ------------ | ---------- | --- | --- | --------- | --- | ------ | ---------------------------------------------- | --------- | --------- | ------ | ------------- | ---------- |
|              |            |     |     |           |     |        | ing lists                                      | of entity | mentions. |        | For instance, | "socio-    |
| Tokenization | algorithm. |     | The | tokenizer |     | recog- |                                                |           |           |        |               |            |
|              |            |     |     |           |     |        | cultural                                       | event"    | is one    | of the | granular      | categories |
nizesspecialtokensandassignsuniquetokenIDs
|                 |     |        |        |        |     |       | under "Culture |         | and Society" |        | in the proposed | PII  |
| --------------- | --- | ------ | ------ | ------ | --- | ----- | -------------- | ------- | ------------ | ------ | --------------- | ---- |
| to thebeginning |     | andend | marker | tokens | of  | anen- |                |         |              |        |                 |      |
|                 |     |        |        |        |     |       | scheme         | (Figure | 2). If,      | during | the annotation  | pro- |
titymention.Forinstance,considerFigure3.We
|               |     |         |       |          |            |      | cess, we        | identify | only   | a few    | labels    | within the |
| ------------- | --- | ------- | ----- | -------- | ---------- | ---- | --------------- | -------- | ------ | -------- | --------- | ---------- |
| assign 128003 | to  | ≪내국인이름≫ |       |          | and 128004 |      |                 |          |        |          |           |            |
|               |     |         |       |          |            |      | "socio-cultural |          | event" | granular | category, | we can     |
| to ≪/내국인이름≫.  |     |         | Given | an input | text       | from |                 |          |        |          |           |            |
instructtheLLMtogeneratemorelabelsforthis
theannotateddataset,suchas"피고인≪내국인
category.Subsequently,wemanuallycreateseveral
| 이름≫L≪/내국인이름≫이...", |     |     |     |     | the text | is to- |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
entitymentionsforeachadditionallabelgenerated
| kenized | into a | sequence: | [2700, | 5,  | 128003, | 82, |     |     |     |     |     |     |
| ------- | ------ | --------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
bytheLLM.
| 128004, | 39], where | L   | (token | ID 82) | serves | as a |     |     |     |     |     |     |
| ------- | ---------- | --- | ------ | ------ | ------ | ---- | --- | --- | --- | --- | --- | --- |
placeholderforalabeledentity.Here,내국인이름
|           |        |        |     |      |     |        | 4 Experiments |     |     |     |     |     |
| --------- | ------ | ------ | --- | ---- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
| refers to | Korean | names, | and | "피고인 | L이" | refers |               |     |     |     |     |     |
to"DefendantL". This section evaluates Thunder-DeID and the ex-
perimentalmethodology.
Next,thetokensequenceisscannedtoidentify
startmarkertokens(e.g.,128003)andtheircorre-
|          |            |        |     |        |          |      | 4.1 ExperimentalSetup |     |     |     |     |     |
| -------- | ---------- | ------ | --- | ------ | -------- | ---- | --------------------- | --- | --- | --- | --- | --- |
| sponding | end marker | tokens |     | (e.g., | 128004), | thus |                       |     |     |     |     |     |
detectingtherangeoftokensbetweenthem.This Training datasets. Besides our annotation
rangeincludestheplaceholder(e.g.,[128003,82, dataset, we collect a bilingual corpus of approx-
128004]).Theplaceholderwithinthisrangeisthen imately76.7GB,comprisingKoreanandEnglish
replacedwithoneoftheentitymentionsselected textsfrompubliclyavailableWebsources.Thiscor-
fromthepre-definedreplacementlist.Forexample, pusisusedfortokenizertrainingandpre-training

|             |     |     |         |           | SingleReplacement   |        |        |     |           | Per-EpochReplacement |        |         |     |
| ----------- | --- | --- | ------- | --------- | ------------------- | ------ | ------ | --- | --------- | -------------------- | ------ | ------- | --- |
| Model       |     |     | #Params |           | (BinaryToken-Level) |        |        |     |           | (BinaryToken-Level)  |        |         |     |
|             |     |     |         | Precision |                     | Recall | F1     |     | Precision |                      | Recall | MicroF1 |     |
| Polyglot-ko |     |     | 1.3B    | 0.9774    |                     | 0.9570 | 0.9669 |     | 0.9710    |                      | 0.9695 | 0.9701  |     |
| Exaone      |     |     | 2.4B    | 0.9774    |                     | 0.9542 | 0.9656 |     | 0.9688    |                      | 0.9666 | 0.9677  |     |
Thunder-DeID-360M 360M 0.9767 0.9264 0.9509 0.9628 0.9679 0.9654
Thunder-DeID-800M 800M 0.9786 0.9767 0.9776 0.9757 0.9826 0.9791
Thunder-DeID-1.5B 1.5B 0.9855 0.9683 0.9769 0.9755 0.9862 0.9808
(a)Binarytoken-level(Precision,Recall,andF1)
|             |     |     |         |           | SingleReplacement |               |        |     |           | Per-EpochReplacement |        |         |     |
| ----------- | --- | --- | ------- | --------- | ----------------- | ------------- | ------ | --- | --------- | -------------------- | ------ | ------- | --- |
| Model       |     |     | #Params |           |                   | (Token-Level) |        |     |           | (Token-Level)        |        |         |     |
|             |     |     |         | Precision |                   | Recall        | F1     |     | Precision |                      | Recall | MicroF1 |     |
| Polyglot-ko |     |     | 1.3B    | 0.8816    |                   | 0.8631        | 0.8723 |     | 0.8772    |                      | 0.8758 | 0.8765  |     |
| Exaone      |     |     | 2.4B    | 0.8785    |                   | 0.8576        | 0.8679 |     | 0.8762    |                      | 0.8742 | 0.8752  |     |
Thunder-DeID-360M 360M 0.8895 0.8438 0.8660 0.8848 0.8895 0.8871
Thunder-DeID-800M 800M 0.9099 0.9082 0.9090 0.9073 0.9137 0.9105
Thunder-DeID-1.5B 1.5B 0.9091 0.8933 0.9011 0.9021 0.9120 0.9071
(b)Token-level(Precision,Recall,andMicroF1)
Table2:Performancecomparisonunderdifferentdatagenerationsettings.Eachsub-tablereportsPrecision,Recall,
and F1 on the test set for the indicated evaluation granularity (Binary token-level vs Token-level). Values are
averagedoverthreerandomseeds(1200,1203,1205).Thebestperformanceresultsarehighlightedinbold.
forourlanguagemodel.Wealsogenerateadataset accommodate longer contexts. Unlike the origi-
forNER-basedde-identificationusingthemethod nalDeBERTa-v3,whichusespost-LayerNorm,we
describedinsubsection3.6.Thedatasetisdivided adoptpre-LayerNorm(Xiongetal.,2020)because
into 80% training (2,400, 2,401, and 560 docu- post-LayerNormfailedtoconvergeforlargermod-
ments), 10% validation (300, 298, and 70 docu- els,whereaspre-LayerNormconvergedreliablyun-
ments),and10%test(300,301,and70documents), derthesamesettings.Formoredetails,pleasesee
forcivil,criminal,andadministrativecases,respec- TableE.1inAppendixE.
|     |     |     |     |     |     |     | Fine-tuningthemodels. |     |     |     | Thunder-DeIDmodels |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------ | --- | --- |
tively.
|                     |     |     |                    |     |     |     | and the | baseline | models | were | fine-tuned |     | on our |
| ------------------- | --- | --- | ------------------ | --- | --- | --- | ------- | -------- | ------ | ---- | ---------- | --- | ------ |
| Languagemodelsused. |     |     | WetrainDeBERTa-v3- |     |     |     |         |          |        |      |            |     |        |
dataset,whichconsistsof5,361trainingdocuments
| based models | (He | et  | al., 2023), | Thunder-DeID, |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2,400,2,401and560),668validationdocuments
with370M,800M,and1.5Bparametersforthede-
(300,298,70)and671testdocuments(300,301,
identificationofKoreancourtjudgmentsthrough
70)forcivil,criminal,andadministrativecases,re-
| token classification. |     | These | models |     | are compared |     |     |     |     |     |     |     |     |
| --------------------- | --- | ----- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
spectively.WeemploybothPer-EpochandSingle
againstKorean-specializedlanguagemodelbase-
EntityReplacementmethodstoassesstheeffectsof
| lines, namely | Polyglot-Ko |     | (Ko | et  | al., 2023) | and |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
datavariation.Thetraininguseasequencelength
EXAONE-3.5(Anetal.,2024),toassesstheirper-
of2,048tokensoverthecourseof30epochs.For
| formance | on our | proposed | dataset. |     | For | detailed |          |          |              |     |        |       |        |
| -------- | ------ | -------- | -------- | --- | --- | -------- | -------- | -------- | ------------ | --- | ------ | ----- | ------ |
|          |        |          |          |     |     |          | detailed | training | information, |     | please | refer | to Ta- |
informationonthearchitecturesandtrainingcon-
|     |     |     |     |     |     |     | ble E.1 | in Appendix |     | E, and | for | the results, | see |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ------ | --- | ------------ | --- |
figurations,pleaserefertoTableE.1inAppendixE.
Table2.
Pre-training the models. Thunder-DeID mod- Evaluationmetrics. Weusethreemetrics—pre-
els are pre-trained from scratch using subsets of cision,recall,andF1-score—toassesstheperfor-
ourbilingualcorpus,whichincludesbothEnglish manceofourmodelonthede-identificationtask.
and Korean, containing 60 billion tokens for the Each metric is evaluated under two settings: bi-
1.5 billion parameter model, 30 billion tokens narytoken-level(Dernoncourtetal.,2016;Yueand
for the 800 million parameter model, and 14 bil- Zhou,2020;Saliernoetal.,2024;Kimetal.,2024)
lion tokens for the 370 million parameter model. andtoken-level(Dernoncourtetal.,2016;Yueand
Trainingbeginswithasequencelengthof512to- Zhou, 2020; Kim et al., 2024). The binary token-
kens, which is later extended to 2048 tokens to level setting measures the model’s ability to cor-

rectlyclassifytokensthatrequirede-identification tween the two models is minimal and could di-
andthosethatdonot,withoutconsideringthetype minish with additional data for rare labels or the
of entity. For the details of the two settings and applicationofstrongerregularization.
metricdefinitions,pleaseseeAppendixF. Thunder-DeIDdemonstratesweaknessesiniden-
|     |     |     |     |     |     | tifying | low-frequency |     | labels | that | seldom | appear |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------ | ---- | ------ | ------ |
4.2 Experimentalresult
|     |     |     |     |     |     | in the training |     | corpus. | For example, |     | it frequently |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | ------------ | --- | ------------- | --- |
Table2showstheperformanceofourmodelscom-
|          |     |                    |     |         |      | misclassifies | “뷔페        |      | (buffet | restaurant)”—which |     |        |
| -------- | --- | ------------------ | --- | ------- | ---- | ------------- | ---------- | ---- | ------- | ------------------ | --- | ------ |
| pared to | two | Korean-specialized |     | Decoder | mod- |               |            | “외식업 |         |                    |     |        |
|          |     |                    |     |         |      | should        | fall under |      |         | (eating            | and | drink- |
els, Polyglot-ko (1.3B) and Exaone (2.4B), un- ing places)”—as “기계설비회사 (machinery and
der two data generation settings: Single Replace- equipmentcompany)”withinthe“제조업(manu-
mentandPer-EpochEntityReplacement.Thunder-
|     |     |     |     |     |     | facturing)” | category. |     | As our | annotators | reviewed |     |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------ | ---------- | -------- | --- |
DeID models consistently outperform the base- the fully anonymized court judgments, we noted
lines in both binary token-level and token-level someexceptionalcaseswhereitwaschallenging
| micro F1 | scores. |     | Our largest | model | Thunder- |     |     |     |     |     |     |     |
| -------- | ------- | --- | ----------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
toaccuratelydeterminetheexacttypeofentity,de-
| DeID-1.5B | achieves |     | a binary | token-level | F1 of |     |     |     |     |     |     |     |
| --------- | -------- | --- | -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
spitecarefulcontextualanalysis.Theseinstances
0.9808 and 800M model achieves a token-level alsoresultedinmisclassifications,suchaslabeling
F1of0.9105underthePer-EpochEntityReplace- “불특정제품명(unspecifiedproductname)”under
mentsetting,establishingastate-of-the-art(SOTA)
“상품일반(generalproducts)”as“불특정회사명
benchmarkforNER-basedde-identificationofKo- (unspecifiedcompany)”under“기업일반(compa-
reancourtjudgments.Notably,evenoursmallest niesandbusinessesingeneral).”
modelThunder-DeID-370M(0.8871)outperforms
|                  |     |          |     |            |          | Thunder-DeID |        | significantly |     | outperforms |        | the    |
| ---------------- | --- | -------- | --- | ---------- | -------- | ------------ | ------ | ------------- | --- | ----------- | ------ | ------ |
| both Polyglot-ko |     | (0.8765) |     | and Exaone | (0.8752) |              |        |               |     |             |        |        |
|                  |     |          |     |            |          | rule-based   | system | currently     |     | used        | by the | Korean |
inthetoken-levelmicroF1metric.Foradetailed NationalCourtAdministration,whichreportedly
breakdown of performance by case type, please achievesanoverallaccuracyof8to15% (National
refertoAppendixH.
AssemblyofKorea,2019;NationalCourtAdmin-
The high binary token-level F1 score for istration of Korea, 2025). These results position
Thunder-DeID under Per-Epoch Entity Replace- Thunder-DeIDasanewandeffectiveframework
mentdemonstratesthatthemodelisproficientin for Named Entity Recognition (NER)-based de-
identifyingwhichtokensneedtobede-identified.
identificationofcourtjudgments.
Additionally,thehightoken-levelmicroF1score
5 Conclusion
indicatesthatThunder-DeIDeffectivelyclassifies
the entity types of these de-identifiable tokens. In this paper, we propose a DNN-based solu-
Giventhatthemodelisrequiredtoclassifyasmany tion,referredtoasThunder-DeID,forNERaimed
as 729 distinct labels, achieving a token-level F1 at improving the efficiency and consistency of
score exceeding 0.91 is a strong indicator of its de-identifying court judgments. We address the
robustmulti-classclassificationperformance. complex challenges currently faced in the de-
The Per-Epoch Entity Replacement technique identificationprocesswithintheKoreanjudiciary.
OurworkincludesthedevelopmentofthefirstKo-
| significantly | outperforms |     | Single | Replacement | in  |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
allmodels,includingPolyglot-koandExaone.This reanlegaldataset,whichcontains6,700judgments
consistent improvement highlights the quality of fromcivil,criminal,andadministrativecases,en-
our dataset, its annotation scheme, and the corre- compassingatotalof48,306labelednamedenti-
|     |     |     |     |     |     | ties. We | also introduce |     | a three-tiered |     | annotation |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | -------------- | --- | ---------- | --- |
spondinglistofentitymentionsforrealisticvalue
generation.Frequententityreplacementsenhance schemeforPII,whichsystematicallycategorizes
datadiversitywhilemaintaininghigh-qualityaug- awidevarietyofpersonalidentifiers.Furthermore,
weprovideacomprehensivelistofentitymentions
mentationandeffectivegeneralization.
thatcanbeusedtoreplacethe729token-levella-
The800Mmodeldemonstratesaslightlyhigher
token-level micro F1 score under the per-epoch belsfoundinthetrainingdataset.Inaddition,we
setting compared to the 1.5B model. In our data- outlineatokenizationmethodforthetrainingdata
generatedfromthesereplacements.Ourexperimen-
| limited | scenario, | the | 800M | model may | be better |     |     |     |     |     |     |     |
| ------- | --------- | --- | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
suited to the dataset size, allowing it to general- talresultsshowthatThunder-DeIDachievesstate-
izeslightlybetter.Incontrast,the1.5Bmodelmay of-the-art performance in the de-identification of
courtjudgments.
| overfit to | rare | labels. | However, | the difference | be- |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |

Limitations
formationwasusedatanystageofthisresearch.
Althoughthedatasetisfullyanonymizedandall
| Our study | has | some limitations. |     | First, | original |     |     |     |     |     |     |
| --------- | --- | ----------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
sourcesarepubliclyavailable,weensuredthatour
(unanonymized)courtjudgmentsarenotaccessible
dataprocessingprocedures—includingthecreation
duetolegalrestrictions.Asmentionedearlier,we
ofreplacementlists—adheredtotheprinciplesof
| only have | access | to fully  | anonymized |          | judgments |            |          |             |     |            |     |
| --------- | ------ | --------- | ---------- | -------- | --------- | ---------- | -------- | ----------- | --- | ---------- | --- |
|           |        |           |            |          |           | the Korean | Personal | Information |     | Protection | Act |
| that have | been   | processed | and        | reviewed | by court  |            |          |             |     |            |     |
(PIPA).
officialsbeforebeingmadepublic.Thislimitation
| prevents | us from | evaluating | our | model’s | perfor- |     |     |     |     |     |     |
| -------- | ------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Acknowledgements
manceinreal-worldsettings.Toaddressthisissue
andmakeourmodelmoreapplicabletoactualde- Wethanktheanonymousreviewersandthemeta-
identificationpracticeswithintheKoreanjudiciary,
|     |     |     |     |     |     | reviewer | for | their valuable |     | feedback | on this pa- |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | -------- | ----------- |
weplantodevelopamorestrategicmethodofdata
|     |     |     |     |     |     | per. We | also | sincerely | thank | Gyeongje | Cho, |
| --- | --- | --- | --- | --- | --- | ------- | ---- | --------- | ----- | -------- | ---- |
augmentation for future research. This includes HyeonggeunJeon,SungmokJung,DayeonKang,
creatingsyntheticdatathatcloselyresemblescourt Jia Kang, Minsu Kim, Sangho Kim, Jongmin
judgments.Bypursuingthisdirection,weaimto
Kim,DongyoungLee,JoonhakLee,ChangjinLee,
increasethesizeanddiversityofourtrainingdata,
|     |     |     |     |     |     | Jongyeon | Park, | Yoonhee | Park, | Seho | Pyo, Jiheon |
| --- | --- | --- | --- | --- | --- | -------- | ----- | ------- | ----- | ---- | ----------- |
allowingformorerobusttestingofourmodel. Seok,YeonkyoungSo,andYoungjunSonfortheir
Second,ourmodelwasspecificallytrainedusing
dedicatedworkasannotators.
judgmentsfromthefieldofcivil,criminal,andad-
|     |     |     |     |     |     | This | work | was partially |     | supported | by the Na- |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ------------- | --- | --------- | ---------- |
ministrativelawandprocedure.De-identification
tionalResearchFoundationofKorea(NRF)under
in the legal domain is highly context-sensitive, Grant No. RS-2023-00222663 (Center for Opti-
| which means |     | the model’s | performance |     | may de- |     |     |     |     |     |     |
| ----------- | --- | ----------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
mizingHyperscaleAIModelsandPlatforms),and
| crease when | applied | to  | court | decisions | involving |                  |     |                 |     |                |     |
| ----------- | ------- | --- | ----- | --------- | --------- | ---------------- | --- | --------------- | --- | -------------- | --- |
|             |         |     |       |           |           | by the Institute |     | for Information |     | and Communica- |     |
differenttypesoflegaldisputes.However,wean- tionsTechnologyPromotion(IITP)underGrantNo.
| ticipate | that our | model | will still | perform | reason- |     |     |     |     |     |     |
| -------- | -------- | ----- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
2018-0-00581(CUDAProgrammingEnvironment
ablywell,astherearesharedcharacteristicsregard-
|     |     |     |     |     |     | for FPGA | Clusters) | and | No. | RS-2025-02304554 |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- | ---------------- | --- |
ingdirectidentifiersacrossvarioustypesofcourt
(EfficientandScalableFrameworkforAIHetero-
judgments.Additionally,ourdatasetencompasses geneousClusterSystems),allfundedbytheMin-
awiderangeofentitytypes.Thus,oursystemhas
istryofScienceandICT(MSIT)ofKorea.Itwas
importantimplicationsevenforcourtjudgmentsin
|     |     |     |     |     |     | also partially |     | supported | by  | the Korea | Health In- |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | --------- | ---------- |
entirelydifferentareasoflaw.Furtherresearchis dustryDevelopmentInstitute(KHIDI)underGrant
necessarytoevaluatethemodel’sperformancein
No.RS-2025-25454559(FrailtyRiskAssessment
theseotherareasandtoexplorehowtheproposed
|     |     |     |     |     |     | and Intervention |     | Leveraging |     | Multimodal | Intelli- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | ---------- | -------- |
methodcanbeadaptedandenhancedforeffective
genceforNetworkedDeploymentinCommunity
de-identificationtasksacrossdiverselegalcontexts. Care),fundedbytheMinistryofHealthandWel-
|     |     |     |     |     |     | fare (MOHW) |     | of Korea. | Additional | support | was |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | ------- | --- |
EthicsStatement
|           |           |      |     |            |          | provided  | by the   | BK21   | Plus      | Program     | for Innova- |
| --------- | --------- | ---- | --- | ---------- | -------- | --------- | -------- | ------ | --------- | ----------- | ----------- |
|           |           |      |     |            |          | tive Data | Science  | Talent | Education | (Department |             |
| All court | judgments | used | in  | this study | were ob- |           |          |        |           |             |             |
|           |           |      |     |            |          | of Data   | Science, | Seoul  | National  | University, | No.         |
tainedfrompubliclyavailableanonymizeddatasets,
includingthosereleasedbytheKoreanMinistryof 5199990914569) and the BK21 FOUR Program
Government, AI-hub11 and published by Hwang for Intelligent Computing (Department of Com-
puterScienceandEngineering,SeoulNationalUni-
| et al. (2022), |     | none of which | contain |     | any PII. To |     |     |     |     |     |     |
| -------------- | --- | ------------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
supportdatareconstructionandmodeltraining,re- versity,No.4199990214639),bothfundedbythe
placement lists were compiled exclusively from MinistryofEducation(MOE)ofKorea.Thiswork
wasalsopartiallysupportedbytheArtificialIntel-
open-accesssources,includinggovernmentlicens-
ingdatabases12,publicdataportals13,andofficial ligence Industrial Convergence Cluster Develop-
institutionalwebsites14.Noprivateorsensitivein- ment Project, funded by the MSIT and Gwangju
|     |     |     |     |     |     | Metropolitan |     | City. Research |     | facilities | were pro- |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | ---------- | --------- |
11https://www.aihub.or.kr/
|     |     |     |     |     |     | vided by | the | Institute | of Computer |     | Technology |
| --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ----------- | --- | ---------- |
12https://www.localdata.go.kr/main.do
(ICT)atSeoulNationalUniversity.
13https://www.data.go.kr/
14https://data.seoul.go.kr/

References
|     |     |     |     |     |     | Judicial | Policy Research | Institute |     | of Korea. 2021. | A   |
| --- | --- | --- | --- | --- | --- | -------- | --------------- | --------- | --- | --------------- | --- |
studyonpersonaldataprotectionincriminaltrialpro-
| Bayan Altalla’, | Sameera     |     | Abdalla, | Ahmad | Altamimi,   |          |                                        |     |     |     |     |
| --------------- | ----------- | --- | -------- | ----- | ----------- | -------- | -------------------------------------- | --- | --- | --- | --- |
|                 |             |     |          |       |             | cedures. | Technicalreport,JudicialPolicyResearch |     |     |     |     |
| Layla           | Bitar, Amal | Al  | Omari,   | Ramiz | Kardan, and |          |                                        |     |     |     |     |
Institute.
| IyadSultan.2025. |     | Evaluatinggptmodelsforclinical |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notede-identification. ScientificReports,15(1):3852. JudicialPolicyResearchInstituteofKorea.2023. Con-
temporarymeaningsandlimitationsoftheprinciple
JiyongAn,JiyunKim,LeonardSunwoo,Hyunyoung
ofopenjustice.
| Baek,SooyoungYoo,andSeunggeunLee.2025. |     |     |     |     | De- |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
identificationofclinicalnoteswithpseudo-labeling
PrathameshKalamkar,AsthaAgarwal,AmanTiwari,
usingregularexpressionrulesandpre-trainedbert.
|             |     |             |     |          |         | Smita | Gupta, Saurabh | Karn, | and | Vivek Raghavan. |     |
| ----------- | --- | ----------- | --- | -------- | ------- | ----- | -------------- | ----- | --- | --------------- | --- |
| BMC Medical |     | Informatics | and | Decision | Making, |       |                |       |     |                 |     |
2022. Namedentityrecognitioninindiancourtjudg-
| 25(1):82. |     |     |     |     |     | ments. | arXivpreprintarXiv:2211.03442. |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ------ | ------------------------------ | --- | --- | --- | --- |
Soyoung An, Kyunghoon Bae, Eunbi Choi, Kibong Woojin Kim, Sungeun Hahm, and Jaejin Lee. 2024.
Choi,StanleyJungkyuChoi,SeokheeHong,Junwon
|     |     |     |     |     |     | Generalizing | clinical | de-identification |     | models | by  |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | ----------------- | --- | ------ | --- |
Hwang,HyojinJeon,GerrardJeongwonJo,Hyunjik
|               |                                 |     |     |     |     | privacy-safedataaugmentationusinggpt-4. |     |     |     | InPro- |     |
| ------------- | ------------------------------- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ------ | --- |
| Jo,etal.2024. | Exaone3.5:Seriesoflargelanguage |     |     |     |     |                                         |     |     |     |        |     |
ceedingsofthe2024ConferenceonEmpiricalMeth-
| models | for real-world |     | use cases. | arXiv | e-prints, |     |     |     |     |     |     |
| ------ | -------------- | --- | ---------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
odsinNaturalLanguageProcessing,pages21204–
| pagesarXiv–2412. |     |     |     |     |     | 21218. |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
HannaBerg,AronHenriksson,andHerculesDalianis.
|     |     |     |     |     |     | Hyunwoong | Ko, Kichang | Yang, |     | Minho Ryu, | Taeky- |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | ----- | --- | ---------- | ------ |
2020. Theimpactofde-identificationondownstream
|                                       |     |     |     |     |            | oon Choi,                  | Seungmu | Yang, | Jiwung | Hyun, Sungho     |     |
| ------------------------------------- | --- | --- | --- | --- | ---------- | -------------------------- | ------- | ----- | ------ | ---------------- | --- |
| namedentityrecognitioninclinicaltext. |     |     |     |     | InProceed- |                            |         |       |        |                  |     |
|                                       |     |     |     |     |            | Park,andKyubyongPark.2023. |         |       |        | Atechnicalreport |     |
ingsofthe11thInternationalWorkshoponHealth
forpolyglot-ko:Open-sourcelarge-scalekoreanlan-
TextMiningandInformationAnalysis,pages1–11.
guagemodels.
DanbiCho,HyunyoungLee,andSeungshikKang.2021.
ZengjianLiu,BuzhouTang,XiaolongWang,andQing-
Anempiricalstudyofkoreansentencerepresentation
|                           |     |     |                    |     |     | caiChen.2017. |     | De-identificationofclinicalnotes |     |     |     |
| ------------------------- | --- | --- | ------------------ | --- | --- | ------------- | --- | -------------------------------- | --- | --- | --- |
| withvarioustokenizations. |     |     | Electronics,10(7). |     |     |               |     |                                  |     |     |     |
viarecurrentneuralnetworkandconditionalrandom
FranckDernoncourt,JiYoungLee,OzlemUzuner,and field. Journal of biomedical informatics, 75:S34–
S42.
| Peter Szolovits. |     | 2016. | De-identification |     | of patient |     |     |     |     |     |     |
| ---------------- | --- | ----- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
noteswithrecurrentneuralnetworks.
|                                      |            |       |         |     |               | Zhengliang | Liu, Xiaowei    | Yu,  | Lu        | Zhang, Zihao    | Wu,   |
| ------------------------------------ | ---------- | ----- | ------- | --- | ------------- | ---------- | --------------- | ---- | --------- | --------------- | ----- |
|                                      |            |       |         |     |               | Chao       | Cao, Haixing    | Dai, | Lin Zhao, | Wei Liu,        | Ding- |
| Yaroslav                             | Emelyanov. | 2021. | Towards |     | task-agnostic |            |                 |      |           |                 |       |
|                                      |            |       |         |     |               | gang       | Shen, Quanzheng | Li,  | et al.    | 2023. Deid-gpt: |       |
| privacy-andutility-preservingmodels. |            |       |         |     | InProceed-    |            |                 |      |           |                 |       |
ingsoftheInternationalConferenceonRecentAd- Zero-shot medical text de-identification by gpt-4.
vances in Natural Language Processing (RANLP arXivpreprintarXiv:2303.11032.
2021),pages394–401.
|     |     |     |     |     |     | Ilya Loshchilov | and | Frank | Hutter. | 2019. Decoupled |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ------- | --------------- | --- |
EuropeanParliamentandCouncil.2016. GeneralData weightdecayregularization.
| ProtectionRegulation(EU)2016/679,Recital35. |     |     |     |     | ht  |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
StephaneMMeystre,FJeffreyFriedlin,BrettRSouth,
tps://eur-lex.europa.eu/eli/reg/2016/679/
|              |         |     |              |     |              | ShuyingShen,andMatthewHSamore.2010. |     |     |     |     | Au- |
| ------------ | ------- | --- | ------------ | --- | ------------ | ----------------------------------- | --- | --- | --- | --- | --- |
| oj. Official | Journal | of  | the European |     | Union, L119, |                                     |     |     |     |     |     |
tomaticde-identificationoftextualdocumentsinthe
pp.1–88.
electronichealthrecord:areviewofrecentresearch.
DiegoGaratandDinaWonsever.2022. Automaticcura- BMCmedicalresearchmethodology,10:1–16.
tionofcourtdocuments:Anonymizingpersonaldata.
Information,13(1):27. PauliusMicikevicius,SharanNarang,JonahAlben,Gre-
goryDiamos,ErichElsen,DavidGarcia,BorisGins-
PengchengHe,JianfengGao,andWeizhuChen.2023. burg, Michael Houston, Oleksii Kuchaiev, Ganesh
Debertav3:Improvingdebertausingelectra-stylepre- Venkatesh, et al. 2017. Mixed precision training.
trainingwithgradient-disentangledembeddingshar- arXivpreprintarXiv:1710.03740.
ing.
|     |     |     |     |     |     | Taoufiq | El Moussaoui, | Loqman |     | Chakir, and Jaouad |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | ------ | --- | ------------------ | --- |
Wonseok Hwang, Dongjun Lee, Kyoungyeon Cho, Boumhidi.2023. Preservingprivacyinarabicjudg-
HanuhlLee,andMinjoonSeo.2022. Amulti-task ments:Ai-poweredanonymizationforenhancedlegal
benchmarkforkoreanlegallanguageunderstanding dataprivacy. IEEEAccess,11:117851–117864.
| andjudgementprediction. |     |     | AdvancesinNeuralInfor- |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mationProcessingSystems,35:32537–32551. National Assembly of Korea. 2019. Debate for pro-
|              |          |       |           |     |          | motingopenpublicationofcourtjudgments. |     |     |     | Online. |     |
| ------------ | -------- | ----- | --------- | --- | -------- | -------------------------------------- | --- | --- | --- | ------- | --- |
| Taehee Jeon, | Bongseok | Yang, | Changhwan |     | Kim, and |                                        |     |     |     |         |     |
PDFfilechecked,p.39.
| Yoonseob | Lim. | 2023. | Improving | korean | nlp tasks |     |     |     |     |     |     |
| -------- | ---- | ----- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
with linguistically informed subword tokenization NationalCourtAdministrationofKorea.2025. National
and sub-character decomposition. arXiv preprint courtadministrationofkorea,finalreport:Informa-
arXiv:2311.03928. tionstrategyplan(isp)fordevelopmentofaimodels

tosupporttrials(2025). Technicalreport,National XiangYueandShuangZhou.2020. PHICON:Improv-
CourtAdministrationofKorea. ing generalization of clinical text de-identification
modelsviadataaugmentation. InProceedingsofthe
NationalIntelligenceService.2023. Securityguidelines 3rdClinicalNaturalLanguageProcessingWorkshop,
https://ww
forusinggenerativeaisuchaschatgpt. pages 209–214, Online. Association for Computa-
w.ncsc.go.kr:4018/main/cop/bbs/selectBoar tionalLinguistics.
dArticle.do?bbsId=InstructionGuide_main&
nttId=54340&pageIndex=1.
JoelNiklaus,RobinMamié,MatthiasStürmer,Daniel
| Brunner,      | and Marcel | Gygli. 2023. |         | Automatic  |
| ------------- | ---------- | ------------ | ------- | ---------- |
| anonymization | of swiss   | federal      | supreme | court rul- |
ings. arXivpreprintarXiv:2310.04632.
| Arttu Oksanen,                                   | Eero Hyvönen, | Minna       | Tamper,      | Jouni       |
| ------------------------------------------------ | ------------- | ----------- | ------------ | ----------- |
| Tuominen,                                        | Henna Ylimaa, | Katja       | Löytynoja,   | Matti       |
| Kokkonen,andAkiHietanen.2022.                    |               |             | Ananonymiza- |             |
| tion tool                                        | for open data | publication | of           | legal docu- |
| ments. InInternationalWorkshoponArtificialIntel- |               |             |              |             |
ligenceTechnologiesforLegalDocuments/Interna-
tionalWorkshoponKnowledgeGraphSummariza-
tion,pages12–21.CEUR-WS.org.
| OpenAI.2022.       | Introducingchatgpt.  |     | https://openai |     |
| ------------------ | -------------------- | --- | -------------- | --- |
| .com/blog/chatgpt. | Accessed:2025-01-02. |     |                |     |
KyubyongPark,JoohongLee,SeongboJang,andDa-
| woonJung.2020.                      | Anempiricalstudyoftokenization |     |     |            |
| ----------------------------------- | ------------------------------ | --- | --- | ---------- |
| strategiesforvariousKoreanNLPtasks. |                                |     |     | InProceed- |
ingsofthe1stConferenceoftheAsia-PacificChap-
teroftheAssociationforComputationalLinguistics
andthe10thInternationalJointConferenceonNat-
uralLanguageProcessing,pages133–142,Suzhou,
China.AssociationforComputationalLinguistics.
| Giulio Salierno, | Rosamaria         | Bertè,   | Luca Attias, | Carla     |
| ---------------- | ----------------- | -------- | ------------ | --------- |
| Morrone,         | Dario Pettazzoni, | and      | Daniela      | Battisti. |
| 2024. Giusberto: | A legal           | language | model        | for per-  |
sonaldatade-identificationinitaliancourtofauditors
| decisions.     | arXivpreprintarXiv:2406.15032. |     |           |        |
| -------------- | ------------------------------ | --- | --------- | ------ |
| Rico Sennrich, | Barry Haddow,                  | and | Alexandra | Birch. |
2016. Neuralmachinetranslationofrarewordswith
| subword | units. In Proceedings |                   | of the 54th | Annual |
| ------- | --------------------- | ----------------- | ----------- | ------ |
| Meeting | of the Association    | for Computational |             | Lin-   |
guistics(Volume1:LongPapers),pages1715–1725,
Berlin,Germany.AssociationforComputationalLin-
guistics.
U.S.DepartmentofHealthandHumanServices.1996.
| HIPAAforProfessionals:Laws&Regulations. |     |     |     | ht  |
| --------------------------------------- | --- | --- | --- | --- |
tps://www.hhs.gov/hipaa/for-professiona
ls/privacy/laws-regulations/index.html.
Accessed:2025-05-19.
| Özlem Uzuner,   | Yuan Luo,                      | and Peter | Szolovits.   | 2007. |
| --------------- | ------------------------------ | --------- | ------------ | ----- |
| Evaluating      | the state-of-the-art           |           | in automatic | de-   |
| identification. | JournaloftheAmericanMedicalIn- |           |              |       |
formaticsAssociation,14(5):550–563.
| Ruibin Xiong, | Yunchang | Yang, Di | He, | Kai Zheng, |
| ------------- | -------- | -------- | --- | ---------- |
ShuxinZheng,ChenXing,HuishuaiZhang,Yanyan
| Lan,LiweiWang,andTie-YanLiu.2020. |     |     |     | Onlayer |
| --------------------------------- | --- | --- | --- | ------- |
normalizationinthetransformerarchitecture.

Appendix
• Lastly,distortionoffactsoccurred.Forexam-
|     |     |     |     |     |     | ple, | specific | numbers | in  | the judgment |     | were |
| --- | --- | --- | --- | --- | --- | ---- | -------- | ------- | --- | ------------ | --- | ---- |
A IssuesinPrompt-based
alteredduringde-identification“총3명(ato-
De-identification
talofthreepeople)”wasalteredto“총명수1
(atotalofoneperson)”.
Weidentifythefollowingfivecategoriesofprob-
lemsfrequentlyappearingintheGPT-assistedde-
identification dicussed in Section 1. These cases Moreover,duetoprivacyandinformationsecu-
rityconcerns,theuseofAPI-basedLLMservices
| represent | the ways | in which | prompting-based |     |     |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anonymizationcanleadtocompromisetextualin- such as ChatGPT is restricted in Korean govern-
tegrityofpublicrecordsandunderminelegalpreci- mentinstitutions.Domesticregulations(issuedby
theNationalIntelligenceServiceandtheMinistry
sionrequiredforsettlingdisputeseffectively.
oftheInteriorandSafety)requirepublicofficials
| • First,  | rewriting | and paraphrasing |          | frequently |     |        |            |             |     |     |         |      |
| --------- | --------- | ---------------- | -------- | ---------- | --- | ------ | ---------- | ----------- | --- | --- | ------- | ---- |
|           |           |                  |          |            |     | across | government | departments |     | to  | refrain | from |
| occurred. | For       | example,         | the verb | “입금하였      |     |        |            |             |     |     |         |      |
puttinginanysensitiveinternaldataandpersonal
다(deposited)”waschangedto“송금하였다
informationwhileusingsuchservices.
| (wiretransferred).” |       | Whilebothcandescribe |     |           |     |               |     |     |     |     |     |     |
| ------------------- | ----- | -------------------- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| sending             | money | to someone,          |     | the forms | and |               |     |     |     |     |     |     |
|                     |       |                      |     |           |     | B DataSamples |     |     |     |     |     |     |
implicationsofthesebehaviorsaredifferently
conceivedinlegalandfinancialcontexts. Since it is a legal obligation of the courts to
anonymizejudgmentspriortopublicdisclosures,
• Second,wealsofoundcasesofpartialomis-
thereisnowaytoaccessunannoymizedjudgments
| sion when |     | GPT removed, | for | instance, | the |             |      |        |           |     |       |         |
| --------- | --- | ------------ | --- | --------- | --- | ----------- | ---- | ------ | --------- | --- | ----- | ------- |
|           |     |              |     |           |     | which could | have | served | as ground |     | truth | for our |
phrase“제때(ontime)”fromtheoriginaltext.
research.Aftercollectingfullyanonymizedjudg-
Theoriginalphrase“그대금을제때변제하
|     |     |     |     |     |     | ments, | we manually |     | annotate | the whole |     | corpus |
| --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | -------- | --------- | --- | ------ |
여”(“byrepayingtheamountontime”)was
|           |     |            |     |      |        | based on | the | three-tiered | categorization |     | scheme |     |
| --------- | --- | ---------- | --- | ---- | ------ | -------- | --- | ------------ | -------------- | --- | ------ | --- |
| shortened | to  | “대금을 변제하여” |     | (“by | repay- |          |     |              |                |     |        |     |
classifyingarangeofpersonalidentifiers.(SeeSec-
ingtheamount”)inGPT-4’soutput.Theomis-
|     |     |     |     |     |     | tion 3.3) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
sionof“제때”(“ontime”)removesanimpor-
Togiveourreadersthegistofthecollectionand
| tant indication |     | of timely | payment, |     | which is |     |     |     |     |     |     |     |
| --------------- | --- | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
annotationprocess,AppendixCpresentsoneofthe
oftencriticalindeterminingwhetherthelegal
examplesofthecourtjudgmentinitiallycompiled
obligationwasproperlymet.
fordataconstructionasinFigureB.1.Nexttothis
• Third,(unsolicited)summarizationoftheorig-
anonymizedcourtjudgment,theannotatedversion
inaltextresultedinthelossofdetailedfacts ofthatsamejudgmentappears.
andstrategiesconcerningthecrimescommit-
ted. Unlike the original text, it merely pro- C MaskingandLabelingExamples
| vides | a brief | summary | of the | factual | back- |          |               |     |             |     |           |     |
| ----- | ------- | ------- | ------ | ------- | ----- | -------- | ------------- | --- | ----------- | --- | --------- | --- |
|       |         |         |        |         |       | Appendix | B illustrates |     | the example |     | discussed | in  |
groundsofthecase.Forinstance,aftergoing
throughGPT-assistedde-identification,three Section3.3inmoredetail.
sentencescontainingimportantdetailsabout
|     |     |     |     |     |     | Example | with | a functional |     | descriptor. |     | Loca- |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ------------ | --- | ----------- | --- | ----- |
defendant’sintentionandplantodefraudvic-
|         |     |           |        |        |      | tionalinformationinthesentence“... |     |     |      |      | 나리식당 |        |
| ------- | --- | --------- | ------ | ------ | ---- | ---------------------------------- | --- | --- | ---- | ---- | ---- | ------ |
| tim and | the | amount of | damage | caused | were |                                    |     |     |      |      |      |        |
|         |     |           |        |        |      | 에서 근무하는                            |     | 피고인 | 홍길동은 | ...” | can  | be de- |
vaguelysummarizedandreducedtoasingle
|           |       |           |      |        |          |            |           | 식당에       |        | 근무하는        | 피고인  |        |
| --------- | ----- | --------- | ---- | ------ | -------- | ---------- | --------- | --------- | ------ | ----------- | ---- | ------ |
|           |       |           |      |        |          | identified | as        | “... A    |        |             |      | B      |
| sentence, | “피고인은 | 이를        | 개인   | 용도로    | 사용       |            |           |           |        |             |      |        |
|           |       |           |      |        |          | 는 ...”.    | According | to        | Korean | Judicial    | Rule | No.    |
| 하였다       | (The  | defendant | used | it for | personal |            |           |           |        |             |      |        |
|           |       |           |      |        |          | 1778, “나리  | 식당”       | qualifies | as     | identifying |      | infor- |
purposes)”.
mationduetoitscontextualspecificity.Whilethe
|     |     |     |     |     |     | generic | term | “식당” | (diner) | remains | intact | as a |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ---- | ------- | ------- | ------ | ---- |
• Fourth,inthecaseswheremultipleindividuals
andinstitutionsareinvolvedinthelitigation, non-identifying functional descriptor, the unique
weoftenidentifiedentitycollapse:anumber component“나리”isreplacedwiththeplaceholder
“A”.Similarly,thename“홍길동”isreplacedwith
ofdifferententitieswereanonymizedwiththe
sameletter(e.g.,광주은행(GwangjuBank), “B”.Theresultingsentenceislabeledas:
| 우정사업본부(KoreaPost),부산은행(Busan |     |     |     |     |     | “... ≪식당≫A≪/식당≫식당에근무하는 |                   |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | ---------------------- | ----------------- | --- | --- | --- | --- | --- |
| Bank)→A,A,A).                |     |     |     |     |     |                        | ≪내국인이름≫B≪/내국인이름≫는 |     |     |     |     |     |
피고인

Anexampleof anonymizedcourtjudgment
initiallycollectedfordataconstruction
이 총책인 중국 산둥성 칭다오시에 있는 금융기관 사칭 보이스피싱 조직(이하 '이 사건 보이스피싱 조직'이라 한다)의
구성원은 (가명 AA), (가명 AB)이 중간관리자급 팀장으로, 피고인(가명 AC) 및 (가명 AD), (가명 AE 또는 AF), (가명
AG), (가명 AH), (가명 AI), (가명 AJ), (가명 AK), (가명 AL), (가명 AM), (가명 AN) 등이 보이스피싱 콜센터 상
담원으로 있었다.
피고인과 이 사건 보이스피싱 조직의 조직원들은 중국 산둥성 칭다오시에 있는 아파트, 아파트 등지에 보이스피싱 콜
센터 사무실과 조직원들의 숙소를 차려두고 불특정 다수의 대한민국 사람들을 상대로 전화하여 AO, AP, AQ의 직원이라
고 말하면서 금융기관을 사칭하여 '기존의 대출금을 상환하면 저금리 대환대출을 해주겠다'고 속이고 금원을 대포 계좌
로 교부받기로 공모하였다.
이에 따라 AR은 총책으로서 중국 산둥성칭다오시에 콜센터 사무실과 콜센터 상담원 숙소를 임차하여 사무실에 컴퓨터,
전화기, 책상 등을 구비하는 한편, 보이스피싱 대상자에게 연락하기 위한 DB(데이터베이스) 자료, 피해자들로부터 피해
금원을 송금받을 대포통장을 구해오고 피해금원이 대포통장을 통해 보이스피싱 조직의 수익금 계좌로 입금되면 조직원들
의 맡은 업무와 실적에 따라 팀장인 AA을 통해 보이스피싱 조직원들에게 수익금을 분배하는 역할, AB은 콜센터 팀장으
로서 상담원들의 업무와 숙식을 관리·감독하면서 콜센터 1차 상담원 업무를 담당할 신규 조직원을 섭외하여 위 조직에
가담하게 하고 총책 로부터 받은 보이스피싱 대상자들의 DB 자료를 콜센터 상담원들에게 나누어준 다음 콜센터 상담원
들에게 보이스피싱 대상자에게 연락하도록 독려하고 1차 상담원들이 보이스피싱 대상자들을 속여 위 콜센터 2차 상담
전화번호로 전화가 걸려오면 '기존 대출금을 상환해야 한다'고 말하면서 대포통장 계좌를 불러주어 대포통장 계좌로 대
출금 명목으로 피해금을 입금하게 하고 로부터 정산받은 보이스피싱 수익금을 콜센터 상담원들에게 분배하는 역할, 피고
인 및 AC 등은 콜센터 상담원으로서 평일 아침 콜센터 사무실로 출근하여 등으로부터 받은 DB 자료를 토대로 보이스
피싱 대상자들에게 전화하여 AS AT 등 금융기관 직원을 사칭하면서 '기존의 대출금을 상환하면 저금리 대환대출을 해
주겠다'고 거짓말하고 2차 상담원에게 연결해주거나 '신용보증기금 보증서 및 신용 등급 향상을 위한 조회 건수 삭제
비용이 든다'고 말하여 이에 속은 피해자로 하여금 대포통장 계좌로 금원을 이체하도록 하는 등의 역할을 각각 분담하
였다.
위와 같은 공모 내용과 역할 분담에 따라 이 사건 보이스피싱 조직원인 는 2017. 12. 27. 오전경 중국 산둥성 칭다오
이하 불상지에 있는 보이스피싱 콜센터 사무실에서, 발신번호 AU 번호로 피해자 에게 전화하여 'AV대리'를 사칭하면서
'기존에 있던 대출금을 상환하면 저금리로 대출해주겠다'고 거짓말을 하였다.
그러나 피고인 및 이 사건 보이스피싱 조직원들은 직원이 아니었고 피해자로부터 금원을 송금받으면 이를 일정한 비율
에 따라 서로 나누어가질 생각이었다. 그럼에도 불구하고 피고인들 및 이 사건 보이스피싱 조직원들은 피해자로부터
2017. 12. 29.경 대포통장 계좌인 AW명의 우체국 계좌(계좌번호 :계좌번호 1 생략 )로 5,530,000원, 2018. 1. 3.경
대포통장 계좌인 명의 조합 계좌(계좌번호 : 계좌번호 2 생략)로 1,000,000원씩 3회에 걸쳐 3,000,000원을 무통장송
금 또는 계좌이체 송금받는 등 8,530,000원을 송금받은 것을 비롯하여 그 때부터 2018. 1. 31.경까지 별지 범죄일람표
기재와 같이 총 16명으로부터 합계 95,311,339원을 송금받았다.
이로써 피고인은 이 사건 보이스피싱 조직원들과 공모하여 피해자들을 기망하여 재물을 교부받았다.
The judgment data annotated pursuant to
the three-tiered categorization scheme of PII
이 총책인 중국 산둥성 칭다오시에 있는 금융기관 사칭 보이스피싱 조직(이하 '이 사건 보이스피싱 조직'이라 한다)
의 구성원은 (가명 <<<내국인이름>>>AA<<</내국인이름>>>), (가명 <<<내국인이름>>>AB<<</내국인이름>>>)이 중간
관리자급 팀장으로, 피고인(가명 <<<내국인이름>>>AC<<</내
국인이름>>>) 및 (가명 <<<내국인이름>>>AD<<</내국인이름>>>), (가명 <<<내국인이름>>>AE<<</내국인이름>>> 또
는 <<<내국인이름>>>AF<<</내국인이름>>>), (가명 <<<내국인이름>>>AG<<</내국인이름>>>), (가명 <<<내국인이
름>>>AH<<</내국인이름>>>), (가명 <<<내국인이름>>>AI<<</내국인이름>>>), (가명 <<<내국인이름>>>AJ<<</내국
인이름>>>), (가명 <<<내국인이름>>>AK<<</내국인이름>>>), (가명 <<<내국인이름>>>AL<<</내국인이름>>>), (가
명 <<<내국인이름>>>AM<<</내국인이름>>>), (가명 <<<내국인이름>>>AN<<</내국인이름>>>) 등이 보이스피싱 콜센
터 상담원으로 있었다.
피고인과 이 사건 보이스피싱 조직의 조직원들은 중국 산둥성 칭다오시에 있는 아파트, 아파트 등지에 보이스피싱
콜센터 사무실과 조직원들의 숙소를 차려두고 불특정 다수의 대한민국 사람들을 상대로 전화하여 <<<은
행>>>AO<<</은행>>>, <<<은행>>>AP<<</은행>>>, <<<은행>>>AQ<<</은행>>>의 직원이라고 말하면서 금융기관을 사
칭하여 '기존의 대출금을 상환하면 저금리 대환대출을 해주겠다'고 속이고 금원을 대포 계좌로 교부받기로 공모하
였다.
이에 따라 <<<내국인이름>>>AR<<</내국인이름>>>은 총책으로서 중국 산둥성칭다오시에 콜센터 사무실과 콜센터 상
담원 숙소를 임차하여 사무실에 컴퓨터, 전화기, 책상 등을 구비하는 한편, 보이스피싱 대상자에게 연락하기 위한
DB(데이터베이스) 자료, 피해자들로부터 피해금원을 송금받을 대포통장을 구해오고 피해금원이 대포통장을 통해 보
이스피싱 조직의 수익금 계좌로 입금되면 조직원들의 맡은 업무와 실적에 따라 팀장인 <<<내국인이름>>>AA<<</내
국인이름>>>을 통해 보이스피싱 조직원들에게 수익금을 분배하는 역할, <<<내국인이름>>>AB<<</내국인이름>>>은
콜센터 팀장으로서 상담원들의 업무와 숙식을 관리·감독하면서 콜센터 1차 상담원 업무를 담당할 신규 조직원을 섭
외하여 위 조직에 가담하게 하고 총책 로부터 받은 보이스피싱 대상자들의 DB 자료를 콜센터 상담원들에게 나누어
준 다음 콜센터 상담원들에게 보이스피싱 대상자에게 연락하도록 독려하고 1차 상담원들이 보이스피싱 대상자들을
속여 위 콜센터 2차 상담 전화번호로 전화가 걸려오면 '기존 대출금을 상환해야 한다'고 말하면서 대포통장 계좌를
불러주어 대포통장 계좌로 대출금 명목으로 피해금을 입금하게 하고 로부터 정산받은 보이스피싱 수익금을 콜센터
상담원들에게 분배하는 역할, 피고인 및 <<<내국인이름>>>AC<<</내국인이름>>> 등은 콜센터 상담원으로서 평일
아침 콜센터 사무실로 출근하여 등으로부터 받은 DB 자료를 토대로 보이스피싱 대상자들에게 전화하여 <<<은
행>>>AS<<</은행>>> <<<은행>>>AT<<</은행>>> 등 금융기관 직원을 사칭하면서 '기존의 대출금을 상환하면 저금
리 대환대출을 해주겠다'고 거짓말하고 2차 상담원에게 연결해주거나 '신용보증기금 보증서 및 신용 등급 향상을
위한 조회 건수 삭제 비용이 든다'고 말하여 이에 속은 피해자로 하여금 대포통장 계좌로 금원을 이체하도록 하는
등의 역할을 각각 분담하였다.
위와 같은 공모 내용과 역할 분담에 따라 이 사건 보이스피싱 조직원인 는 2017. 12. 27. 오전경 중국 산둥성 칭
다오 이하 불상지에 있는 보이스피싱 콜센터 사무실에서, 발신번호 <<<전화번호>>>AU<<</전화번호>>> 번호로 피해
자 에게 전화하여 '<<<내국인이름>>>AV<<</내국인이름>>>대리'를 사칭하면서 '기존에 있던 대출금을 상환하면 저
금리로 대출해주겠다'고 거짓말을 하였다.
그러나 피고인 및 이 사건 보이스피싱 조직원들은 직원이 아니었고 피해자로부터 금원을 송금받으면 이를 일정한
비율에 따라 서로 나누어가질 생각이었다. 그럼에도 불구하고 피고인들 및 이 사건 보이스피싱 조직원들은 피해자
로부터 2017. 12. 29.경 대포통장 계좌인 <<<내국인이름>>>AW<<</내국인이름>>>명의 <<<은행>>>우체국<<</은
행>>> 계좌(계좌번호 :<<<계좌번호>>>계좌번호 1 생략 <<</계좌번호>>>)로 5,530,000원, 2018. 1. 3.경 대포통
장 계좌인 명의 조합 계좌(계좌번호 : <<<계좌번호>>>계좌번호 2 생략<<</계좌번호>>>)로 1,000,000원씩 3회에
걸쳐 3,000,000원을 무통장송금 또는 계좌이체 송금받는 등 8,530,000원을 송금받은 것을 비롯하여 그 때부터
2018. 1. 31.경까지 별지 범죄일람표 기재와 같이 총 16명으로부터 합계 95,311,339원을 송금받았다.
이로써 피고인은 이 사건 보이스피싱 조직원들과 공모하여 피해자들을 기망하여 재물을 교부받았다.
FigureB.1:Examplesofcourtjudgmentdatabeforeandafterannotation.

식당
...”, where the label refers to a place for D.1.2 연령정보(AgeandDateofBirth)
eatinganddrinking.
나이(age),출생연도(yearofbirth),생년월일(date
ofbirth)
| Example | without | a functional |     | descriptor. | In  |     |     |     |     |     |     |     |
| ------- | ------- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
constrast,someplacenamesdonotcontainanex- D.1.3 이메일주소(EmailAddress)
plicitfunctionaldescriptor.Forexample,thesen- 이메일주소(emailaddress)
| tence "... | 피해자 | 김철수를 | 기다리며 | 맥도날드에 |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
서 음식을 주문하고 ..." ("... ordered food at Mc- D.1.4 주민등록번호(ResidentRegistration
| Donald’swhilewaitingforthevictimKimChulsoo |     |     |     |     |     |     | Number) |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
toarrive...")canbeanonymizedto"...피해자D를
|     |     |     |     |     |     | D.2 | 기타(사건관계인이나제3자를특정할수 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
기다리며E에서음식을주문하고..."("...ordered
있는)정보(Quasi-identifiers)
foodatEwhilewaitingforthevictimDtoarrive
|     |     |     |     |     |     | D.2.1 | 사건관계인이력(WorkandCriminal |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----------------------- | --- | --- | --- | --- | --- |
...").Inthiscase,"맥도날드"("McDonald’s")does
backgroundsofthepersonsinvolvedin
nothaveafunctionaldescriptor,socourtofficials
thecase)
| are instructed | to  | replace | the entire | word | with a |                        |     |     |     |          |     |     |
| -------------- | --- | ------- | ---------- | ---- | ------ | ---------------------- | --- | --- | --- | -------- | --- | --- |
|                |     |         |            |      |        | 범죄경력(Criminalrecords): |     |     |     | 죄(crime) |     |     |
placeholder,E.Therefore,"...피해자D를기다리
며E에서음식을주문하고..."inthede-identified
|     |     |     |     |     |     | D.2.2 | 사건관련숫자정보(Incident-related |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------------------------- | --- | --- | --- | --- | --- |
judgmentwillbelabeledbytheannotatorsasfol-
numericalinformation)
|            |     | ≪내국인 | 이름≫D≪/내국인 |     |     |      |          |         |     |          |     |         |
| ---------- | --- | ---- | --------- | --- | --- | ---- | -------- | ------- | --- | -------- | --- | ------- |
| lows: "... | 피해자 |      |           |     |     |      |          |         |     |          |     |         |
|            |     |      |           |     |     | 고유번호 | (Various | Numbers |     | Uniquely |     | Identi- |
이름≫를기다리며≪식당≫E≪식당≫에서
|     |     |     |     |     |     | fyingSpecificIndividualsandObjects): |     |     |     |     |     | 계좌  |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
음식을주문하고...."
|     |     |     |     |     |     | 번호 (bank |     | account number), |     | 관리번호 | (manage- |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------------- | --- | ---- | -------- | --- |
mentnumber),금괴일련번호(goldbarserialnum-
D PersonallyIdentifiableInformation
ber),사건번호(casenumber),선박번호(IMOship
(PII)Categorization
|     |     |     |     |     |     | number), | 비트코인개인지갑 |     | (bitcoin |     | wallet), | 수   |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | --- | -------- | --- |
AppendixBprovidesacompleteoverviewofthe 표번호(checknumber),카드번호(cardnumber),
어선(fishingvesselnumber),어음번호(billnum-
three-tieredcategorizationschemeclassifyingper-
ber),범죄경력등조회회보서(criminalrecordcer-
sonalidentifiersinthedomainoflawandadjudi-
|     |     |     |     |     |     | tificate), | 차량번호 | (vehicle | registration |     | number), |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | -------- | ------------ | --- | -------- | --- |
cation,asdetailedinSection3.4.Undertwomain
|     |     |     |     |     |     | 특허번호 |     |     | 휴대폰번호 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ----- | --- | --- | --- |
categories,16subcategories,and80granularcat- (patent number), (mobile
|     |     |     |     |     |     | phone | number), | 군번 (military |     | service | number), |     |
| --- | --- | --- | --- | --- | --- | ----- | -------- | ------------ | --- | ------- | -------- | --- |
egories,wepresentatotalof729labelsalphabet-
면허번호(licensenumber),훈장번호(decoration
| ically ordered          |     | in Korean | along with | the English |     |                                    |     |     |     |     |     |     |
| ----------------------- | --- | --------- | ---------- | ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
| translationofeachlabel. |     |           |            |             |     | number),전화번호(phonenumber),내선번호(ex- |     |     |     |     |     |     |
tensionnumber),수험번호(examinationnumber),
사건관계인특정정보(Directidentifiers) 보훈번호 (veterans registration number), 보증번
D.1
|     |     |     |     |     |     | 호 (guarantee |     | number), | 고시번호 | (official |     | notice |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---- | --------- | --- | ------ |
인명(Names)
| D.1.1                   |     |     |     |       |     |               | 비밀번호 |                  |     |          | 등기번호      |     |
| ----------------------- | --- | --- | --- | ----- | --- | ------------- | ---- | ---------------- | --- | -------- | --------- | --- |
|                         |     |     |     |       |     | number),      |      | (password        |     | / PIN),  |           |     |
| 내국인이름(Koreannames):     |     |     |     |       |     | (registration |      | number), 사업자등록번호 |     |          | (business |     |
|                         |     |     |     |       |     | registration  |      | number), 접수번호    |     | (receipt | number),  |     |
| 외국인이름(Non-Koreannames): |     |     |     | 몽골인이름 |     |               |      |                  |     |          |           |     |
민원번호(civilcomplaintnumber),경매번호(auc-
(Mongolian names), 베트남이름 (Vietnamese tionnumber),채권번호(bondnumber),일련번호
|     | 세례명 |     |     | 영어이름 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
names), (baptismal names), (serialnumber),법인등록번호(corporateregistra-
| (English | names), | 일본인이름 | (Japanese | names), |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionnumber)
| 중국인이름      | (Chinese | names), |     | 캄보디아이름        |     |       |     |          |          |     |             |     |
| ---------- | -------- | ------- | --- | ------------- | --- | ----- | --- | -------- | -------- | --- | ----------- | --- |
|            |          |         |     |               |     | 장소 관련 | 번호  | (Numbers | Assigned |     | to Specific |     |
| (Cambodian | names),  | 태국인이름   |     | (Thai names), |     |       |     |          |          |     |             |     |
필리핀이름 (Filipino names), 러시아권이름 Places): 골프장코스(golfcourse),구역(zone),
라인(line),지하철칸(subwaycompartment),항공
(Russiannames),법명(Dharmanames)
편(flightnumber)번(number),호선(linenumber),
|     |     |     |     |     |     | 호실(room | number), | 호(unit | number), |     | 출구번호 |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | -------- | --- | ---- | --- |
아이디•닉네임 (IDs and Nicknames): 가수 (exitnumber),동(buildingnumber),층(floor),노선
(aliases),닉네임(nicknames),대화명(usernames), 번호(routenumber),레일(railnumber),승강장번
별명 (nicknames), 블로그 (blogs), 아이디 (IDs), 호(platformnumber),열차번호(trainnumber),탑
| 법호(Dharmanickname) |     |     |     |     |     | 승장번호(boardingplatformnumber),번호(num- |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |

ber), 광역버스(express bus number), 단지 (hous- river/stream), 행정구 (Gu: district-level adminis-
ing complex), 로트 (lot), 블록 (block), 실(room), trative unit), 행정군 (Gun: county-level adminis-
번지(lotaddressnumber) trative unit), 행정동 (Dong: neighborhood-level
|       |     |     |        |                  |     | administrative |     | unit), 행정리 | (Ri: | village-level |     | ad- |
| ----- | --- | --- | ------ | ---------------- | --- | -------------- | --- | ---------- | ---- | ------------- | --- | --- |
| 기타 사건 | 관련  | 숫자  | (Other | Incident-related |     |                |     |            |      |               |     |     |
ministrativeunit),행정면(Myeon:township-level
| Numbers): |     | 기수 (class | number), |     | 명수(number |     |     |     |     |     |     |     |
| --------- | --- | --------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
administrativeunit),행정시(Si:city-leveladmin-
ofpeople),연도(year),날짜(date)
|     |     |     |     |     |     | istrative | unit), | 행정읍 | (Eup: | town-level | adminis- |     |
| --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ----- | ---------- | -------- | --- |
D.2.3 사건관련장소(Incident-relatedsites trative unit), 행정도 (Do: province-level admin-
|     |     |     |     |     |     | istrative | unit), | 베트남전관련지명 |     | (Vietnam |     | War |
| --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | --- | -------- | --- | --- |
andlocations)
|       |     |           |          |     |       | related      | place   | names), | 지사및지청명 |     | (branch   | and |
| ----- | --- | --------- | -------- | --- | ----- | ------------ | ------- | ------- | ------ | --- | --------- | --- |
| 시설 내부 | 공간  | (Interior | Spaces): |     | 건물내장소 |              |         |         |        |     |           |     |
|       |     |           |          |     |       | local office | names), | 특정지역범위명 |        |     | (specific | re- |
(aplaceinthebuilding),공공기관내장소(aplace
|               |     |               |       |     |             | gional | boundary | names), | 고지  | (highland/hill), |     | 국   |
| ------------- | --- | ------------- | ----- | --- | ----------- | ------ | -------- | ------- | --- | ---------------- | --- | --- |
| in the public |     | institution), | 공원내장소 |     | (a place in |        |          |         |     |                  |     |     |
가명(countryname),고개(mountainpass),섬이
thepark),광장(square),소분류장(smallclassifica-
|     |     |     |     |     |     | 름 (island | name), | 전투지역(combat |     |     | zone), | 해변  |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ----------- | --- | --- | ------ | --- |
tionyard),사무실(office),교도소내장소(aplace
(beach),호수(lake),하천(river/stream),
inthecorrectionfacility),구치소내장소(aplacein
thedetentioncenter),대학교내장소(aplaceinthe
|     |     |     |     |     |     | 도로명(RoadsandStreets): |     |     |     | 골목(alley),교차 |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------------ | --- | --- |
university),문(gate),물류센터레일(railsatlogis-
|     |     |     |     |     |     | 로               |     | 길         |     | 도로      | 인터체 |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ------- | --- | --- |
|     |     |     |     |     |     | (intersection), |     | (street), |     | (road), |     |     |
ticscenter),법원내장소(aplaceinthecourthouse),
인지(interchange),로터리(rotary)
병원내장소(aplaceinthehospital),생활관(res-
| idential | hall),아파트내장소 |     | (a  | placein | the apart- |              |     |                       |     |     |     |     |
| -------- | ------------ | --- | --- | ------- | ---------- | ------------ | --- | --------------------- | --- | --- | --- | --- |
|          |              |     |     |         |            | 구간(Sections) |     | 도로구간(roadsection),철도구 |     |     |     |     |
ment),기숙사(dormitory),군부대내장소(aplace
간(railwaysection)
inthemilitaryfacility)
D.2.5 조직(Organizations)
| 교통 (Transport |         | Infrastructure): |     |      | 버스공영차      |       |            |     |              |     |     |     |
| ------------- | ------- | ---------------- | --- | ---- | ---------- | ----- | ---------- | --- | ------------ | --- | --- | --- |
| 고지 (bus       | garage) | 버스정류장            |     | (bus | stop), 요금소 |       |            |     |              |     |     |     |
|               |         |                  |     |      |            | 친목•문화 | (Community |     | Gatherings): |     | 단체명 |     |
(tollgate)
|     |     |     |     |     |     | (uncategorized |     | gatherings), | 독서토론모임 |     |     | (book |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | ------ | --- | --- | ----- |
|     |     |     |     |     |     | 동호회            |     |              |        |     | 모임  |       |
건설(ConstructionSites): 공사장(construction club), (uncategorized clubs), (social
|     |     |     |     |     |     | gatherings), |     | 봉사단체 | (volunteer | group), | 산악회 |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ---------- | ------- | --- | --- |
yard),현장(site),야적장(storageyard)공사현장
|     |     |     |     |     |     | (hikers | club), | 연합회 | (uncategorized |     | coalitions), |     |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --- | -------------- | --- | ------------ | --- |
(constructionsite)
체육회(sportsclub)
| 산림•하천(ForestandWater): |     |     |     | 둘레길(perime- |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ter trail), 등산로 (hiking path), 산책로 (walking 사회•종교 단체(Social and Religious Groups):
| trail),약수터(mineralspring) |     |         |             |     |              | 노회             |     | 사회복지법인 |            |                |         |     |
| ------------------------- | --- | ------- | ----------- | --- | ------------ | -------------- | --- | ------ | ---------- | -------------- | ------- | --- |
|                           |     |         |             |     |              | (presbytery),  |     |        |            | (social        | welfare |     |
|                           |     |         |             |     |              | organization), |     | 종교단체   | (religious | organization), |         |     |
| 해양 (Places                |     | related | to Maritime |     | Activities): |                |     |        |            |                |         |     |
종중(classassociation)
선박명(shipname),여객선(passengershipname),
군함명(warshipname)
정치•경제단체및협의체(VariousAssociations
지리정보(Geographicinformation) of Like-minded People in Politics, Commerce
D.2.4
|               |     |       |     |          |       | andLabor): |     | 공제조합(mutualaidassociation), |     |     |     |     |
| ------------- | --- | ----- | --- | -------- | ----- | ---------- | --- | --------------------------- | --- | --- | --- | --- |
| 주소 (Address): |     | 도아래주소 |     | (address | under |            |     |                             |     |     |     |     |
노동조합(laborunion),선거캠프(electioncamp),
province)구아래주소(addressunderdistrict/Gu)
|     |     |     |     |     |     | 재개발정비조합 |     | (redevelopment |     | partnership), |     | 재   |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------------- | --- | ------------- | --- | --- |
군아래주소(addressundercounty/Gun)읍아래주
|     |     |     |     |     |     | 건축정비조합 |     | (reconstruction |     | partnership), |     | 정당  |
| --- | --- | --- | --- | --- | --- | ------ | --- | --------------- | --- | ------------- | --- | --- |
소(addressundertown/Eup)동아래주소(address
(politicalparty),조합(uncategorizedpartnerships),
시아래주소
| under neighborhood/Dong) |     |     |     |     | (address |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
지역주택조합(localhousingassociation),협동조
undercity/Si)주소(address)임야(forestland)토
합(cooperativeassociation),협의회(uncategorized
지(land)필지(parcel/lot)국외주소(overseasad-
councils),협회(uncategorizedassociations),상인
dress)
|     |     |     |     |     |     | 회 (merchant |     | association), | 사단법인 |     | (non-profit |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | ---- | --- | ----------- | --- |
지역명 (Geographic units): 마을 (village), 산 corporation),의료법인(medicalcorporation),위
(mountain), 선거구 (coinstituency), 선거단위 원회(committee),재단법인(foundation),학교법
(electoral district), 외국도시 (foreign city), 지 인 (educational foundation), 의료재단 (medical
구 (district), 해안지역명 (coastal area name), foundation),어촌계(fishermen’sassociation),총
| 해수욕장 | (bathing | beach), |     | 국외하천 | (overseas | 회(generalassembly) |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | ---- | --------- | ------------------ | --- | --- | --- | --- | --- | --- |

국방•치안 (Specific Units in Military and Law terminal), 선착장 (dock), 육교 (pedestrian over-
Enforcement Agencies): 국정원비밀조직 (se- pass), 저수지 (resorvoir), 지하차도 (underpass),
cret agency under the National Intelligence Ser- 지하철역 (subway station), 태양광발전소 (solar
vice), 대대 (battalion), 헌병대 (military police), power plant), 터널 (tunnel), 항구 (port), 교량
사단(division),여단(brigade),소대(platoon),연 (bridge),비행장(airfield),검사및검문소(inspec-
대(regiment),중대(company),사령부(headquar- tionandcheckpoint),상하수도시설(watersupply
ters),해군전단(navalsquadron),본부(headquar- and sewage facilities), 변전소 (substation), 원자
ters),해군함대(navalfleet) 력본부(nuclearheadquarters),부두(pier/wharf),
기차역(trainstation)
| 조직 내 | 세부부서 | (Specific |     | Units | and Depart- |     |     |     |     |     |     |     |
| ---- | ---- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ments in the Organizations): 단과대학 (col- 사회복지시설 (Social Security and Welfare
|     |     |     |     |     |     |     |     | 복지시설 |     |     |     | 요양원 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
lege),반(kindergartenclass),부서(departments), Facilities): (welfare facility),
지회(branches),팀(teams),학과(collegemajors), (nursing home), 육아원 (child care center), 장애
교통공사내부서(departmentwithintransportation 인이용시설 (facility for person with disabilities),
| corporation) |     |     |     |     |     |     | 재가장기요양기관(home-basedlong-termcarein- |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
stitution)
| 조직 내 | 업무•권한 |     | 등(Job | levels | and | duties |     |     |     |     |     |     |
| ---- | ----- | --- | ----- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
within organizations) 직급 (job level), 회원등 주민편의시설 (Residential Convenience Facili-
농어촌근린시설
급(membershiplevel),군계급(militaryrank),직 ties): 공원 (park), (rural com-
무(jobduty),보직(officialpost) munity facility), 마을회관 (community center),
|                        |          |                 |     |     |      |     | 주민쉼터             | (community    | rest | area), | 경로당 | (senior |
| ---------------------- | -------- | --------------- | --- | --- | ---- | --- | ---------------- | ------------- | ---- | ------ | --- | ------- |
| 불법 단체                  | (Illegal | Organizations): |     |     | 범죄조직 |     |                  |               |      |        |     |         |
|                        |          |                 |     |     |      |     | center), 유원지     | (recreational |      | area), | 놀이터 | (play-  |
| (criminalorganization) |          |                 |     |     |      |     | ground),마당(yard) |               |      |        |     |         |
기관및시설(Institutionsand
| D.2.6 |     |     |     |     |     |     | 스포츠시설 | (Sports | Facilities) |     | 경기장 | (sta- |
| ----- | --- | --- | --- | --- | --- | --- | ----- | ------- | ----------- | --- | --- | ----- |
Facilities):
dium),야구장(baseballstadium)
| 정부기관        | 및   | 지방자치단체 | (Public          |     | Administra- |     |      |              |     |             |     |      |
| ----------- | --- | ------ | ---------------- | --- | ----------- | --- | ---- | ------------ | --- | ----------- | --- | ---- |
|             |     |        |                  |     |             |     | 주거시설 | (Residential |     | Buildings): |     | 고급주택 |
| tive Bodies | and | Local  | Municipalities): |     |             | 공사  |      |              |     |             |     |      |
(luxuryresidence),맨션(low-riseapartment),빌라
| 및공단 | (public | institution), | 시청  | (city | hall), | 우체  |     |     |     |     |     |     |
| --- | ------- | ------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
아파트
|         |          |        |     |            |     |      | (multiplex | housing), |     | (apartment), |     | 오피스 |
| ------- | -------- | ------ | --- | ---------- | --- | ---- | ---------- | --------- | --- | ------------ | --- | --- |
| 국 (post | office), | 행정복지센터 |     | (community |     | ser- |            |           |     |              |     |     |
텔(studioapartment),주택(single-familyhome),
vicecenter),중앙행정기관(centraladministrative
타운하우스(townhouse)
| agency), | 해양및산림등관리기관 |     |     | (maritime |     | and |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
forestry management agency), 교육청 (office of 의료기관(HealthcareInstitutions): 내과(inter-
education), 등기소 (registry office), 세무서 (tax nalmedicineclinic),병원(hospitals),산부인과의
office)
|                    |     |        |                    |           |     |        | 원 (OB-GYN     | clinic),        | 성형외과 |            | (plastic       | surgery), |
| ------------------ | --- | ------ | ------------------ | --------- | --- | ------ | ------------- | --------------- | ---- | ---------- | -------------- | --------- |
|                    |     |        |                    |           |     |        | 신경외과          | (neurosurgery), |      | 안과         | (ophthalmalmic |           |
| 군사(MilitaryBases): |     |        | 군부대(militarycamp), |           |     |        |               |                 |      |            |                |           |
|                    |     |        |                    |           |     |        | clinic), 요양병원 | (nursing        |      | hospital), |                | 의원 (local |
| 미군부대               | (US | Army), | 훈련소                | (military |     | train- |               |                 |      |            |                |           |
clinic),정신병원(mentalhospital),정형외과(or-
군정비및관리시설
| ing center), |     |     |     | (military |     | mainte- |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
thopedicsclinic),치과(dentistry),치과의원(den-
nanceandmanagementfacility),군소속교육기관
talclinic),의료원(medicalcenter),보건소(public
(military-affiliatededucationalinstitution)
healthcenter),재활원(rehabilitationcenter),이비
| 치안 및 | 교정  |           |     |              |     |        | 인후과(ENTclinic),피부과(dermatologyclinic) |     |     |     |     |     |
| ---- | --- | --------- | --- | ------------ | --- | ------ | ------------------------------------- | --- | --- | --- | --- | --- |
|      |     | (Policing | and | Correctional |     | Facil- |                                       |     |     |     |     |     |
ities): 경찰서 (police office), 경찰청 (national 한방병원(Koreanmedicinehospital),한의원(ori-
entalmedicineclinic)
policeagency),구치소(detentioncenter),지구대
| (police | substation), | 치안센터 |     | (community |     | police |      |              |     |                |     |     |
| ------- | ------------ | ---- | --- | ---------- | --- | ------ | ---- | ------------ | --- | -------------- | --- | --- |
|         |              |      |     |            |     |        | 교육기관 | (Educational |     | Institutions): |     | 고등학 |
center),파출소(policesubstation)
|     |     |     |     |     |     |     | 교             | 대학교 |     |               |     | 어린이집 |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------------- | --- | ---- |
|     |     |     |     |     |     |     | (highschool), |     |     | (university), |     |      |
(daycarecenter),연수원(trainingcenter),유치원
소방및재난(AgenciesforFireSafetyandDis-
(kindergarten),중학교(middleschool),직업능력
| asterResponse): |     | 소방서(firestation),안전센터 |     |     |     |     |        |             |     |          |          |     |
| --------------- | --- | --------------------- | --- | --- | --- | --- | ------ | ----------- | --- | -------- | -------- | --- |
| (safetycenter)  |     |                       |     |     |     |     | 개발훈련시설 | (vocational |     | training | center), | 초등  |
학교(elementaryschool),국외중고등학교(over-
사회기반시설 (Public Infrastructure): 공항 seas middle and high school), 국외대학교 (over-
(airport), 발전소 (power plant), 버스터미널 (bus seasuniversity),사관학교(militaryacademy),전

문학교(vocationalschool),중고등학교(secondary 골프용품판매점 (golf equipment store), 과일가
| school) |     |     |     |     | 게 (fruit | shop), | 귀금속점 |     | (jewelry | store), | 꽃가게 |     |
| ------- | --- | --- | --- | --- | -------- | ------ | ---- | --- | -------- | ------- | --- | --- |
(flowershop),농산물판매업(agriculturalproduct
| 문화•예술 | (Art and | Cultural | Facilities): | 도서  |     |     |     |     |     |     |     |     |
| ----- | -------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sales),대리점(distributor),떡집(ricecakeshop),
관(library),문화시설(culturecenter),미술관(art
마트(grocerystore),문구점(stationerystore),반
museum),전시장(exhibitionhall),청소년수련관
찬가게(sidedishshop),백화점(departmentstore),
(youthtrainingcenter),박물관(museum)
|     |     |     |     |     | 빵집  | (bakery), | 상품권판매업체 |     |     | (gift | certificate |     |
| --- | --- | --- | --- | --- | --- | --------- | ------- | --- | --- | ----- | ----------- | --- |
종교시설(PlaceofWorship): 교회(church),사 vendor), 생활용품매장 (household goods store),
|     |     |     |     |     | 석유대체연료판매업체 |     |     |     | (alternative |     | fuel retailer), |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ------------ | --- | --------------- | --- |
찰(temple)
|     |     |     |     |     | 슈퍼마켓 |     | (supermarket), |     | 스포츠용품점 |     | (sporting |     |
| --- | --- | --- | --- | --- | ---- | --- | -------------- | --- | ------ | --- | --------- | --- |
상업시설(CommercialBuildingsandFacilities):
|     |     |     |     |     | goods | store), | 스포츠의류 |     | (sportswear), |     | 식품유 |     |
| --- | --- | --- | --- | --- | ----- | ------- | ----- | --- | ------------- | --- | --- | --- |
빌딩(building),상가(shoppingplaza),시장(mar- 통업 (food distribution business), 신발판매업체
ket), 아울렛 (outlet), 장례식장 (funeral home), (shoe store), 악기회사 (musical instrument com-
전기차충전소(EVchargingstation),중고차매매 pany), 안경점 (optical shop), 반려동물분양업체
| 단지 (used | car sales | complex), | 지하상가 | (under- |      |        | 약국  |             |     | 오디오샵 |     |        |
| -------- | --------- | --------- | ---- | ------- | ---- | ------ | --- | ----------- | --- | ---- | --- | ------ |
|          |           |           |      |         | (pet | shop), |     | (pharmacy), |     |      |     | (audio |
groundshoppingcenter),휴게소(restarea),예식 equipmentstore),옷가게(clothingstore),원단공
장(weddinghall),매표소(ticketbooth),놀이시설 급업체 (fabric supplier), 유압벨브판매업체 (hy-
(amusementfacility),건물(building),모델하우스
|     |     |     |     |     | draulic | valve | vendor), |     | 유통업 | (distribution |     | busi- |
| --- | --- | --- | --- | --- | ------- | ----- | -------- | --- | --- | ------------- | --- | ----- |
(showhouse),자동차매매단지(carsalescomplex) ness),의류매장(apparelstore),자동차대리점(car
|     |     |     |     |     | dealership), |     | 자동차백화점 |     | (auto | megastore), |     | 자   |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | ----- | ----------- | --- | --- |
연구개발기관(ResearchandDevelopmentInsti-
동차판매점(carsalesshop),전자제품매장(elec-
| tutions): | 연구소 (research |     | institute), | 주행시험 |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
tronicsstore),정육점(butchershop),제과점(pas-
장(drivingtestcenter)
tryshop),주유소(gasstation),중고도서매매업체
산업•물류(IndustrialDevelopmentandLogistic (usedbookstore),중고차매매업체(usedcardeal-
Complex): 공단(publiccorporation),물류단지 ership)카드단말기판매업체(creditcardterminal
distributor),캠핑업체(campingserviceprovider),
(logisticscomplex),산업단지(industrialcomplex)
|     |     |     |     |     | 컴퓨터판매업체 |     | (computer |     | retailer), |     | 타이어판매 |     |
| --- | --- | --- | --- | --- | ------- | --- | --------- | --- | ---------- | --- | ----- | --- |
복합단지및개발지구(IndustrialDevelopment
|                                |     |     |              |     | 업체                              | (tire        | shop), | 페인트판매업  |         | (paint   | supplier), |        |
| ------------------------------ | --- | --- | ------------ | --- | ------------------------------- | ------------ | ------ | ------- | ------- | -------- | ---------- | ------ |
| andLogisticComplex):           |     |     | 친환경복합단지(eco- |     | 편의점                             |              |        |         |         | 화원       |            |        |
|                                |     |     |              |     |                                 | (convenience |        | store), |         | (flower  |            | shop), |
| friendlycomplex)               |     |     |              |     | 화학약품판매업(chemicalsupplier),휴대전화판 |              |        |         |         |          |            |        |
|                                |     |     |              |     | 매업체                             | (mobile      | phone  |         | store), | 휴대폰케이스매장 |            |        |
| 금융관련공공기관(financialregulators): |     |     |              | 금융  |                                 |              |        |         |         |          |            |        |
(mobileaccessoriesshop),보청기판매점(hearing
기관(financialservicesagency),은행(bank),저
|     |     |     |     |     | aid | store), | 자전거판매업 |     | (bicycle | shop), | 기계도 |     |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --- | -------- | ------ | --- | --- |
축은행(savingsbank)
소매업(machinerywholesaleandretailbusiness)
D.2.7 사업체(Corporateentities) 수산물유통업 (seafood distribution business), 매
장(store),매점(shop)
| 외식업(EatingandDrinkingPlaces): |     |     |     | 가요주 |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
점(karaokepub),고깃집(KoreanBBQrestaurant), 금융•세무(FinancialInstitutions,Insuranceand
노래주점 (singing bar), 다방 (traditional Korean Other Financial Intermediaries): , 금융회사
cafe),동남아음식점(SoutheastAsianrestaurant),
|       |             |        |      |          | (financial |     | company), | 대부업 |     | (loan | business), | 보   |
| ----- | ----------- | ------ | ---- | -------- | ---------- | --- | --------- | --- | --- | ----- | ---------- | --- |
| 라이브카페 | (live music | cafe), | 레스토랑 | (restau- |            |     |           |     |     |       |            |     |
험사(insuarancecompany),신탁회사(trustcom-
rant), 바 (bar), 분식점 (snack bar), 뷔페 (buffet pany),전당포(pawnshop),증권사(securitiescom-
restaurant),애견카페(petcafe),일식당(Japanese pany), 카드회사 (credit card company), 투자회
| restaurant), | 주점 (pub), | 중식당 | (Chinese | restau- |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
사(investmentfrim),해외은행(foreignbank),해
rant),치킨집(friedchickenrestaurant),푸드트럭 외증권사(foreignsecuritiescompany),세무법인
(foodtruck),한식당(Koreanrestaurant),해외식당 (tax corporation), 회계법인 (accounting corpora-
(internationalrestaurant),횟집(sashimirestaurant),
tion),감정평가법인(appraisalcorporation),집합
키즈카페(kidscafe),카페(cafe)
투자기구(collectiveinvestmentscheme),감정평
가사사무소(appraisaloffice),세무사사무소(tax
| 도•소매 | 및 유통 (Wholesale |     | and Retail | Trade): |     |     |     |     |     |     |     |     |
| ---- | --------------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
accountantoffice)
가게(shop),가구매장(furniturestore),가스업체
(gassupplycompany),가전제품판매업(homeap- 법무 (Law Practice): 법률사무소 (law office),
pliance store), 고물업체 (scrap metal business), 법무법인 (law firm), 노무법인 (labor law firm),

법무사사무소(judicialscriveneroffice) manufacturing),철판제조업(steelplatemanufac-
|     |     |     |     |     |     |     | turing), | 철판가공업 |     | (sheet | metal | processing), | 플   |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | ------ | ----- | ------------ | --- |
부동산중개및임대매매(RealEstateBusiness):
라스틱가공업(plasticprocessingcompany),화장
공인중개사(realestateagent),부동산매매임대회
품회사(cosmeticscompany),중공업회사(heavy
사(realestatesalesandrentalcompany),부동산
industrycompany),세라믹제조업(ceramicsman-
| 분양사무실 |     | (real | estate | sales office), | 분양대행사 |     |              |     |       |          |     |               |     |
| ----- | --- | ----- | ------ | -------------- | ----- | --- | ------------ | --- | ----- | -------- | --- | ------------- | --- |
|       |     |       |        |                |       |     | ufacturing), |     | 침장제조업 | (bedding |     | manufacturing |     |
(realestatemarketingagency),중개법인(broker-
|                 |     |     |     |     |     |     | company), |     | 화학공업사 | (chemical |      | industry    | com- |
| --------------- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | --------- | ---- | ----------- | ---- |
| agecorporation) |     |     |     |     |     |     |           |     |       |           | 제약회사 |             |      |
|                 |     |     |     |     |     |     | pany),    | 정미소 | (rice | mill),    |      | (pharmaceu- |      |
ticalcompany),제철소(steelmill)
정보통신업(InformationandCommunications):
| 방송국                                  |     | (broadcasting | station), |     | 신문 (newspaper), |     |        |     |     |                         |     |            |     |
| ------------------------------------ | --- | ------------- | --------- | --- | --------------- | --- | ------ | --- | --- | ----------------------- | --- | ---------- | --- |
|                                      |     |               |           |     |                 |     | 농축물수산업 |     | 및   | 임업 (Agriculture,        |     | Fisheries, |     |
| 언론사(mediacompany),출판사(publishingcom- |     |               |           |     |                 |     |        |     |     | 농장(farm),축산농장(livestock |     |            |     |
andForestry):
pany),통신사(telecommunicationscompany),전
|     |     |     |     |     |     |     | farm), | 어업회사 |     | (fishery | company), | 과수원 | (or- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | -------- | --------- | --- | ---- |
화국(telephoneoffice),방송(broadcasting),
chard)
| 건설  |                 |     |     | 건설업체 |               |     |                             |     |     |     |     |     |     |
| --- | --------------- | --- | --- | ---- | ------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
|     | (Construction): |     |     |      | (construction |     | 광업및각종자원채굴•채취(MiningandQuar- |     |     |     |     |     |     |
company),부동산개발업(realestatedevelopment
|     |     |     |     |     |     |     | rying): | 금광채굴업(goldmining),광업소(min- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | --- |
business),토공사(civilengineeringcompany),토
ingcompany)
목업(civilengineeringbusiness),재개발업체(re-
development company), 조경업체 (landscaping 숙박업 (Lodging and Accommodation): 고시
| company) |     |     |     |     |     |     | 원(gosiwon:asmallsingle-roomaccommodation), |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
리조트(resort),모텔(motel),무인텔(unmanned
| 운수업 |                 | (Transportation): |           |     | 택배및운송회 |       |         | 산장  |           |         |     | 여관     | 콘도  |
| --- | --------------- | ----------------- | --------- | --- | ------ | ----- | ------- | --- | --------- | ------- | --- | ------ | --- |
|     |                 |                   |           |     |        |       | motel), |     | (mountain | lodge), |     | (inn), |     |
| 사   | (transportation |                   | company), |     | 택시회사   | (taxi |         |     |           |         |     |        |     |
(condominiumresort),펜션(pension),호텔(hotel),
| company), |     | 여객운송회사 |     | (passenger |     | transport |        |     |        |         |      |     |          |
| --------- | --- | ------ | --- | ---------- | --- | --------- | ------ | --- | ------ | ------- | ---- | --- | -------- |
|           |     |        |     |            |     |           | 게스트하우스 |     | (guest | house), | 숙박시설 |     | (lodging |
company),이삿짐센터(movingcompany)
facility)
| 물류  | (Logistics |     | and Distribution): |     | 물류센터 |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
오락및스포츠(Recreation,LeisureandSports):
(logisticscenter),물류창고(logisticswarehouse),
극단(theatertroupe),PC방(internetcafé),게임장
| 물류회사(logisticscompany) |     |     |     |     |     |     | (arcade),골프연습장(golfpracticerange),골프장 |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
(golfclub),낚시터(fishingspot),노래방(karaoke
| 제조업 |     | (Manufacturing): |     | 가구공장 | (furniture |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
room),당구장(billiardhall),볼링장(bowlingal-
| factory), |     | 건설자재회사 |     | (building | materials | com- |     |     |     |     |     |     |     |
| --------- | --- | ------ | --- | --------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ley),수영장(swimmingpool),승마장(equestrian
pany),공장(factory),금속제조업(metalmanufac-
center),실내낚시터(indoorfishingcafe),영화관
turing),기계설비회사(machineryandequipment
(movietheater),오락실(arcade),온천(hotspring),
| company), |     | 목공소 | (woodworking |     | shop), | 미용기 |     |     |     |     |     |     |     |
| --------- | --- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
워터파크(waterpark),캠핑장(campground),풀
| 기업체 |     | (beauty | equipment | company), | 보일러회 |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |         |           |           |      |     | 장   |     | 헬스장 |     |     | 기원  |     |
사(boilermanufacturer),복합기업체(multifunc- (pool), (fitness center), (baduk
|     |     |     |     |     |     |     | club), | 당구장 | (billiard | hall), | 수족관 | (aquarium), |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | ------ | --- | ----------- | --- |
tionprintermanufacturer),봉제업체(sewingcom-
야구연습장(battingcage),스키장(skiresort),수
pany),비료회사(fertilizercompany),석재가공업
체(stoneprocessingcompany),선박제조업(ship- 상레저업(waterleisurebusiness)
buildingcompany),식품가공업(foodprocessing
|           |     |           |     |           |      |     | 미용•욕탕•신체관리 |     |     | 서비스      | (Beauty | and | Body    |
| --------- | --- | --------- | --- | --------- | ---- | --- | ---------- | --- | --- | -------- | ------- | --- | ------- |
| company), |     | 식품업체(food |     | company), | 식품회사 |     |            |     |     |          |         |     |         |
|           |     |           |     |           |      |     | Care):     | 마사지 |     | (massage | shop),  | 목욕탕 | (public |
(foodcompany),육류업체(meatprocessingcom-
|     |     |     |     |     |     |     | bathhouse), |     | 미용실 | (hair | salon), | 사우나 | (sauna), |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ----- | ------- | --- | -------- |
pany),음료회사(beveragecompany),의료기기회
|     |     |     |     |     |     |     | 안마시술소 |     | (massage | parlor), | 안마원 | (therapeu- |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | -------- | --- | ---------- | --- |
사(medicaldevicecompany),의류브랜드(cloth-
ticmassageclinic),왁싱샵(waxingshop),이발소
| ing | brand), | 이동식주택 |     | (mobile | home | manufac- |     |     |     |     |     |     |     |
| --- | ------- | ----- | --- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
(barbershop),찜질방(Koreanspa),피어싱(pierc-
자동차부품생산업체
turer), (auto parts manufac- ingstudio),반려동물미용샵(petgroomingshop),
turer),자동차회사(automobilecompany),전기배
네일샵(nailsalon)
터리업체(batterymanufacturer),전자전기제조업
(electroniccomponentmanufacturing),조선회사 유흥업 (Adult entertainment): 나이트클럽
(shipbuildingcompany),주류회사(alcoholicbev- (nightclub), 노래빠 (karaoke bar), 단란주점
erage company), 질소발생기제조업체 (nitrogen (karaokeloungewithhostservices),룸살롱(high-
generatormanufacturer),철골제조업(steelframe endadultentertainmentvenuewithprivaterooms),

업소(adultentertainmentvenue),카지노(casino), D.2.8 상품일반(ConsumerProducts)
| 클럽 (club), | 호스트바 |     | (host | bar), 무도장 | (dance |                                         |        |     |                    |     |
| ---------- | ---- | --- | ----- | --------- | ------ | --------------------------------------- | ------ | --- | ------------------ | --- |
|            |      |     |       |           |        | 식•의약품                                   | (Foods | and | Medical Products): | 식   |
| hall)      |      |     |       |           |        | 품(food),음료(beverage),의약품(pharmaceutical |        |     |                    |     |
product),피자(pizza)
서비스일반(OtherServiceSectors): 건물임대 공산품(IndustrialProducts): 가전제품(home
관리회사(buildingmanagementcompany),광고
|                 |     |           |     |        |       | appliance), | 공작기계 | (machine | tool), | 마스크팩 |
| --------------- | --- | --------- | --- | ------ | ----- | ----------- | ---- | -------- | ------ | ---- |
| 회사 (advertising |     | company), |     | 대리운전회사 | (des- |             |      |          |        |      |
(sheetmask),발전기(generator),악기모델명(in-
| ignated driver | service |     | company), | 동물병원 | (vet- |          |       |        |         |         |
| -------------- | ------- | --- | --------- | ---- | ----- | -------- | ----- | ------ | ------- | ------- |
|                |         |     |           |      |       | strument | model | name), | 임플란트제품명 | (dental |
erinary clinic), 방역회사 (pest control company), implantproduct),작업용차량(workvehicle),차량
| 배달대행업체 | (delivery |     | agency), | 상담소 | (coun- |     |     |     |     |     |
| ------ | --------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- |
종류(vehicletype),철강제품(steelproduct),의료
selingcenter),상조회사(funeralserviceagency),
기기(medicaldevice),교구(teachingaid),미용제
선박임대판매업(shiprentalandsalescompany), 품(cosmeticproduct),불특정제품명(unspecified
| 세차장 |     | 세탁소 |     |     | 소개소 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(car wash), (laundry), (la- product name), 농약 (pesticide), 비료 (fertilizer),
| bor dispatch | agency), |     | 스튜디오 | (studio), | 여행사 |     |     |     |     |     |
| ------------ | -------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
항공기(aircraft)
| (travel agency), |     | 오토바이수리점 |     | (motorcycle | re- |                   |     |     |           |     |
| ---------------- | --- | ------- | --- | ----------- | --- | ----------------- | --- | --- | --------- | --- |
|                  |     |         |     |             |     | 출판물(Publications) |     |     | 서적(books) |     |
pairshop),요가학원(yogastudio),용역회사(out-
| sourcing | service | company), |     | 운전면허학원 | (driv- |     |     |     |     |     |
| -------- | ------- | --------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
정보통신상품(ComputerEquipmentandSoft-
ingschool),유학알선업체(studyabroadagency),
|     |     |     |     |     |     | ware): | 소프트웨어(software) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | --- | --- |
인터넷설치업체(internetinstallationservice),인
| 테리어 (interior |           | design | service), | 자동차임대업 |      | D.2.9 | 방송통신서비스(Mediaand    |     |     |     |
| ------------- | --------- | ------ | --------- | ------ | ---- | ----- | ------------------- | --- | --- | --- |
| 체 (car rental | company), |        | 재직정보제공업체  |        | (em- |       | Telecommunications) |     |     |     |
ploymentverificationcompany),전자제품렌탈업 온•오프라인 방송 (Streaming and Broadcast-
(electronicsrentalbusiness),정비공업사(autore-
|     |     |     |     |     |     | ingservice): |     | 방송마일리지(streamingdonation |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------------ | --- | --- |
pairshop),주차장(parkinglot),주차장관리회사
points),방송프로그램(broadcastingprogram),방
(parkinglotmanagementcompany),철거업체(de- 송플랫폼(streamingplatform)
molitioncompany),철학관(fortunetellinghouse),
청소대행업체 (cleaning service company), 컨설 플랫폼일반(OnlineplatformsinGeneral): 구
인사이트(jobsearchsite),번역사이트(translation
팅(consultingfirm),태권도장(Taekwondogym),
site),사이트(uncategorizedwebsites),어플(appli-
| 택시면허매매중개업 |     |     | (taxi license | brokerage), | 파   |     |     |     |     |     |
| --------- | --- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
티룸(partyroom),학원(privateacademy),기업행 cation),포털(portalsite),보이스피싱어플리케이
사대행업체 (event management company), 화실 션(voicephisingapplication)
(artstudio),점집(fortunetellinghouse),운전면허
|     |     |     |     |     |     | 전자상거래(E-commerce): |     |     | 미술품경매사이트 |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | -------- | --- |
시험장(driver’slicensetestcenter),보안경비회사
(artauctionsite),배달어플리케이션(deliveryap-
(securitymanagementcompany),폐기물처리업체
plication),쇼핑몰(onlineshoppingmall),중고거
(wastedisposalcompany),금속분석업(metalanal-
래사이트(secondhandmarketplacewebsite)
ysisbusiness),산후조리원(postnatalcarecenter),
| 결혼준비대행업 |     |          |          |     | 건        | 소셜미디어 |     | (Social Media): | SNS | (social net- |
| ------- | --- | -------- | -------- | --- | -------- | ----- | --- | --------------- | --- | ------------ |
|         |     | (wedding | planning |     | agency), |       |     |                 |     |              |
축사사무소 (architectural office), 사진관 (photo workingservice),밴드(groupcommunicationap-
studio),음원서비스(musicstreamingservice) plication), 소개팅어플리케이션 (dating applica-
tion),인터넷동성사이트(LGBTdatingapp),채팅
어플리케이션(chattingapplication),커뮤니티사
| 기업 일반 | (Companies |     | and | Businesses | in Gen- |     |     |     |     |     |
| ----- | ---------- | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- |
이트(onlinecommunitysite),국외메신저(foreign
eral): IT회사(ITcompany),불특정회사명(un-
messagingapplication),온라인게시판명(nameof
specifiedcompany),무역회사(tradingcompany),
onlinebulletinboard),온라인게시글명(titleofon-
유한공사(limitedcompany),유한회사(limitedli-
|                   |     |      |     |                |     | line | post), 온라인대화방명 |     | (name of | online chat |
| ----------------- | --- | ---- | --- | -------------- | --- | ---- | -------------- | --- | -------- | ----------- |
|                   |     | 주식회사 |     |                | 지점  |      |                |     |          |             |
| ability company), |     |      |     | (corporation), |     |      |                |     |          |             |
room)
| (branch office), |     | 지주회사 | (holding | company), | 국   |     |     |     |     |     |
| ---------------- | --- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- |
외기업(foreigncompany),상사회사(tradingcom- 게임 (Online Games): 게임마일리지 (game
pany), 합자회사 (limited partnership company), mileage),게임서버(gameserver),게임아이템(in-
합명회사 (general partnership company), 농업회 gameitem),게임아이템거래카페(itemtradingfo-
사법인 (agricultural corporation), 영농조합법인 rum),모바일게임(mobilegame),온라인게임(on-
(agriculturalcooperativecorporation) linegame),인터넷도박(onlinegambling)

D.2.10 금융서비스(FinancialProductsand model has 370 million parameters, a hidden di-
|          | Services) |     |              |     |           | mensionof1024,24transformerlayers,16atten- |     |              |     |      |            |     |
| -------- | --------- | --- | ------------ | --- | --------- | ------------------------------------------ | --- | ------------ | --- | ---- | ---------- | --- |
|          |           |     |              |     |           | tion heads,                                | and | a vocabulary |     | size | of 32,000. | The |
| 투자•보험•대출 |           | 서비스 | (Investment, |     | Insurance |                                            |     |              |     |      |            |     |
and Personal Loan Services): 골프보험 (golf 800Mmodelhas800millionparameters,ahidden
dimensionof1280,36transformerlayers,20atten-
| insurance), | 금융투자상품 |       | (financial |      | investment |             |     |              |         |             |            |          |
| ----------- | ------ | ----- | ---------- | ---- | ---------- | ----------- | --- | ------------ | ------- | ----------- | ---------- | -------- |
|             |        |       |            |      |            | tion heads, | and | a vocabulary |         | size        | of 32,000. | The      |
| product),   | 대출상품   | (loan | product),  | 보험상품 | (in-       |             |     |              |         |             |            |          |
|             |        |       |            |      |            | 1.5B model  | has | 1.5          | billion | parameters, |            | a hidden |
suranceplan)
|     |     |     |     |     |     | dimension | of  | 2048, | 24 transformer |     | layers, | 32 at- |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----- | -------------- | --- | ------- | ------ |
가상자산(VirtualAssets): 가상화폐(cryptocur- tention heads, and a vocabulary size of 128,000.
rency), 가상화폐거래프로그램 (crypto trading The smaller vocabulary size for the 370M and
가상화폐거래소
platform), (cryptocurrency ex- 800Mmodelspreventstheembeddingmatrixfrom
| change) |     |     |     |     |     | becoming | disproportionately |     |     | large | relative | to the |
| ------- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | ----- | -------- | ------ |
transformerlayerstoensurebalancedmodelarchi-
| D.2.11 | 사회•문화(CultureandSociety) |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tecture.
국가유산(NationalHeritageandOtherCultural
| Features): | 중요무형문화재(intangiblecultural |     |     |     |     | E.2 Training |     |     |     |     |     |     |
| ---------- | -------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
heritage)
|     |     |     |     |     |     | Pre-training. |     | Thunder-DeID |     |     | models | are pre- |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --- | ------ | -------- |
trainedfromscratchonthebilingualcorpusfrom
예술(FineArts,VisualArts,PerformingArts):
Section4.1,whichyields60billiontokens(22bil-
공연(performance),영화(film)
|     |     |     |     |     |     | lion Korean, | 38  | billion | English) |     | when | tokenized |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | -------- | --- | ---- | --------- |
| 교육  | 학술  |     |     |     |     |              |     |         |          |     |      |           |
및 (Education Programs and Aca- with our custom tokenizer. The 370M model is
demicCurriculum): 교과목(curriculum) pre-trainedona14billiontokensubset(7billion
|       |                 |     |     |          |     | Korean,        | 7 billion | English) |         | sampled | from | the cor- |
| ----- | --------------- | --- | --- | -------- | --- | -------------- | --------- | -------- | ------- | ------- | ---- | -------- |
| 각종 행사 | (Socio-cultural |     |     | Events): | 공청회 |                |           |          |         |         |      |          |
|       |                 |     |     |          |     | pus, conducted |           | over     | 2 hours | using   | 32   | NVIDIA   |
낚시대회
(public hearing), (fishing competition), H10080GBGPUs.The800Mmodelispre-trained
| 등산행사 | (hiking | event), | 임플란트세미나 |     | (im- |         |         |       |        |     |         |         |
| ---- | ------- | ------- | ------- | --- | ---- | ------- | ------- | ----- | ------ | --- | ------- | ------- |
|      |         |         |         |     |      | on a 30 | billion | token | subset | (15 | billion | Korean, |
plantseminar),사회공헌•자선행사(charityevent),
15billionEnglish)sampledfromthecorpus,con-
축제(festival),행사(uncategorizedevents)
ductedover9hoursusing32NVIDIAH10080GB
|             |     |                      |     |     |     | GPUs. | The 1.5B | model | is  | pre-trained | on  | the full |
| ----------- | --- | -------------------- | --- | --- | --- | ----- | -------- | ----- | --- | ----------- | --- | -------- |
| 스포츠(Sports) |     | 운동종목(sportscategory) |     |     |     |       |          |       |     |             |     |          |
60billiontokens(22billionKorean,38billionEn-
각종과업(VariousProjects) 공사(construction glish),conductedover19hoursusing32NVIDIA
work),사업(project),용역(servicecontract) H100 80GB GPUs. For the 370M model, initial
|        |     |     |     |     |     | pre-training  | uses | a       | global  | batch    | size of | 2048, a  |
| ------ | --- | --- | --- | --- | --- | ------------- | ---- | ------- | ------- | -------- | ------- | -------- |
| D.2.12 | URL |     |     |     |     |               |      |         |         |          |         |          |
|        |     |     |     |     |     | peak learning |      | rate of | 7.5e-5, | a masked |         | language |
modeling(MLM)probabilityof0.15,andamaxi-
URL: URL
mumsequencelengthof512,withtheDeepSpeed
E ModelandTraining framework under ZeRO Stage 0 (DDP). For the
|              |          |     |            |         |        | 800M    | and 1.5B | models, |          | the same | configuration |           |
| ------------ | -------- | --- | ---------- | ------- | ------ | ------- | -------- | ------- | -------- | -------- | ------------- | --------- |
| This section | provides |     | additional | details | on our |         |          |         |          |          |               |           |
|              |          |     |            |         |        | is used | but with | a peak  | learning |          | rate of       | 5e-5. All |
modelarchitecture,andtrainingproceduresintro-
modelsareoptimizedusingAdamW(Loshchilov
| duced in | the main | paper | (Section | 4). | We first de- |                               |     |     |     |     |                |     |
| -------- | -------- | ----- | -------- | --- | ------------ | ----------------------------- | --- | --- | --- | --- | -------------- | --- |
|          |          |       |          |     |              | andHutter,2019)optimizerwithβ |     |     |     |     | = (0.9,0.999). |     |
scribeThunder-DeIDmodelfamilydevelopedfor
Alearningrateschedulewithawarm-upphasefor
Koreancourtjudgmentde-identification.Wethen
|     |     |     |     |     |     | the first | 10% | of training |     | steps and | cosine | decay |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | --- | --------- | ------ | ----- |
outlinethepre-trainingandfine-tuningstrategies
fortheremainderisappliedacrossallmodels.To
appliedtobothourmodelsandthebaselines.
handlelongerinputs,eachmodelundergoesaddi-
tionaltrainingon2milliontokenswithamaximum
E.1 Modelconfiguration
sequencelengthof2048,usingthesamelearning
| Model. | We introduce |     | Thunder-DeID, |     | a family |                |     |            |     |          |       |        |
| ------ | ------------ | --- | ------------- | --- | -------- | -------------- | --- | ---------- | --- | -------- | ----- | ------ |
|        |              |     |               |     |          | rate schedule. |     | All models |     | use FP16 | mixed | preci- |
ofmodelsbasedontheDeBERTa-v3architecture, sion(Micikeviciusetal.,2017)training.
designedforde-identificationthroughtokenclassi-
fication.Thunder-DeIDfamilyincludesthreemod- Fine-Tuning. Wefine-tuneThunder-DeIDmod-
els: 370M, 800M and 1.5B models. The 370M elsandthebaselinemodelsonthetokenclassifica-

tiontaskusingthedataset(Section4.1).Weemploy truepositives(TP),falsepositives(FP),andfalse
twodataaugmentationsettings:Per-EpochEntity negatives (FN). TP is the number of tokens cor-
Replacement,whereentitymentionsineachdocu- rectlypredictedasatargetlabel.FPisthenumber
mentarereplacedwithnewsamplesfromaprede- of tokens incorrectly predicted as a target label
finedlistateveryepochtoincreasedatadiversity, whentheybelongtoanotherlabel.FNisthenum-
andSingleReplacement,whereentitymentionsare beroftokensbelongingtoatargetlabelbutincor-
replacedonceandremainfixedthroughouttraining. rectly predicted as another label. Precision is the
At each epoch under Per-Epoch Entity Replace- proportionofcorrectlypredictedtokensamongall
ment, the model sees a different variant of every tokens predicted as the target label, and recall is
document,andthefulltrainingcompletesover30 theproportionofcorrectlypredictedtokensamong
epochstocovertheentireaugmentedset.Thevali- alltokenstrulybelongingtothetargetlabel.These
| dationsetremainsunchangedtoensureconsistent |     |     | aredefinedas: |     |     |     |
| ------------------------------------------- | --- | --- | ------------- | --- | --- | --- |
evaluation.Forthe370Mmodel,wesettheglobal
TP
batch size to 32, the peak learning rate to 5e-5. Precision =
TP+FP
Forthe800Mmodel,1.5Bmodel,Polyglot-Koand
TP
| Exaone-3.5,thesameconfigurationisusedbutwith |     |     |     | Recall | =   |     |
| -------------------------------------------- | --- | --- | --- | ------ | --- | --- |
TP+FN
apeaklearningrateof2e-5.Allmodelsaretrained
|                |              |        | BinaryToken-LevelF1. |     | BinaryToken-LevelF1 |     |
| -------------- | ------------ | ------ | -------------------- | --- | ------------------- | --- |
| with a maximum | input length | capped | at 2048 to-          |     |                     |     |
kens(themodellimit).Inputslongerthanthislimit evaluatesthemodel’sabilitytoclassifytokensre-
aretruncatedfromtheend(head-only,tailtrunca- quiringde-identificationfromthosethatdonotre-
gardlessofentitytype.Highscoresensureaccurate
tion),soverylongcourtrulings—especiallycivil
detectionofalltokensrequiringde-identification
andadministrativecases—maynotbefullycovered
by the model input. We apply FP16 mixed preci- like“홍길동”(HongGildong)whileexcludingoth-
erslike“이”(i).Thismetriciscriticalbecausemiss-
sionacrossallmodelsandoptimizethesemodels
ingevenonetokenthatrequiresde-identification
| usingAdamWoptimizerwithβ |     | = (0.9,0.999). |     |     |     |     |
| ------------------------ | --- | -------------- | --- | --- | --- | --- |
canimmediatelyleadtoincreaseidentifiabilityof
F EvaluationMetrics thepersonandthuscompromiseprivacy.Bytreat-
ingallentitytypesasasingleclass,itprovidesa
Thissectiondetailstheevaluationmetricsusedto simple yet robust baseline widely adopted in de-
assessmodelperformanceinthede-identification identification research (Dernoncourt et al., 2016;
of Korean court judgments, as discussed in the Yue and Zhou, 2020; Salierno et al., 2024; Kim
mainpaper(Section4).WedescribeBinaryToken- etal.,2024).Thebinarytoken-levelF1scoreinour
Level F1 and Token-Level Micro F1, including experimentiscalculatedasfollows:
theirmathematicaldefinitionsandsignificancefor
| resultanalysis. |     |     |     |                 | TPbin |     |
| --------------- | --- | --- | --- | --------------- | ----- | --- |
|                 |     |     |     | BinaryPrecision | =     |     |
TPbin +FPbin
| Backgrounds. | In token | classification | for de- |              | TPbin |     |
| ------------ | -------- | -------------- | ------- | ------------ | ----- | --- |
|              |          |                |         | BinaryRecall | =     |     |
+FNbin
| identification,modelperformanceismeasuredwith |     |     |     |     | TPbin |     |
| --------------------------------------------- | --- | --- | --- | --- | ----- | --- |
Aspect Thunder-DeID-370M Thunder-DeID-800M Thunder-DeID-1.5B Polyglot-Ko EXAONE-3.5
| Parameters        |     | 370M   | 800M   | 1.5B    | 1.3B   | 2.4B    |
| ----------------- | --- | ------ | ------ | ------- | ------ | ------- |
| HiddenDimension   |     | 1024   | 1280   | 2048    | 2048   | 2560    |
| TransformerLayers |     | 24     | 36     | 24      | 24     | 30      |
| AttentionHeads    |     | 16     | 20     | 32      | 16     | 32      |
| VocabularySize    |     | 32,000 | 32,000 | 128,000 | 30,080 | 102,400 |
Pre-trainCorpus 14B(7BKo/7BEn) 30B(15BKo/15BEn) 60B(22BKo/38BEn) - -
Pre-trainHardware 32×NVIDIAH10080GB 32×NVIDIAH10080GB 32×NVIDIAH10080GB - -
| Pre-trainDuration     |     | 2hours   | 9hours   | 19hours  | -   | -   |
| --------------------- | --- | -------- | -------- | -------- | --- | --- |
| Pre-trainLearningRate |     | 7.5e-5   | 7.5e-5   | 7.5e-5   | -   | -   |
| Pre-trainBatchSize    |     | 2048     | 2048     | 2048     | -   | -   |
| Pre-trainSeqLength    |     | 512→2048 | 512→2048 | 512→2048 | -   | -   |
Pre-trainAdamWBetas β=(0.9,0.98) β=(0.9,0.98) β=(0.9,0.98) - -
| Pre-trainAdamWWeightDecay |     | 0.01 | 0.01 | 0.01 | -   | -   |
| ------------------------- | --- | ---- | ---- | ---- | --- | --- |
Fine-tuningHardware 8×NVIDIAH10080GB 8×NVIDIAH10080GB 8×NVIDIAH10080GB 8×NVIDIAH10080GB 8×NVIDIAH10080GB
| Fine-tuningLearningRate |     | 5e-5 | 2e-5 | 2e-5 | 2e-5 | 2e-5 |
| ----------------------- | --- | ---- | ---- | ---- | ---- | ---- |
| Fine-tuningBatchSize    |     | 32   | 32   | 32   | 32   | 32   |
| Fine-tuningSeqLength    |     | 2048 | 2048 | 2048 | 2048 | 2048 |
Fine-tuningAdamWBetas β=(0.9,0.98) β=(0.9,0.98) β=(0.9,0.98) β=(0.9,0.98) β=(0.9,0.98)
| Fine-tuningAdamWWeightDecay |     | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| --------------------------- | --- | ---- | ---- | ---- | ---- | ---- |
TableE.1:ComparisonofThunder-DeIDmodelsandbaselineKoreanmodels,ExaoneandPolyglot-ko.

|                   |     |      | BinaryPrecision·BinaryRecall |     |     |     |             |     | MicroPrecision·MicroRecall |     |     |     |
| ----------------- | --- | ---- | ---------------------------- | --- | --- | --- | ----------- | --- | -------------------------- | --- | --- | --- |
| BinaryToken-Level |     | = 2· |                              |     |     |     | Token-Level | =   | 2·                         |     |     |     |
| F1                |     |      |                              |     |     |     | MicroF1     |     |                            |     |     |     |
|                   |     |      | BinaryPrecision+BinaryRecall |     |     |     |             |     | MicroPrecision+MicroRecall |     |     |     |
wherethepositiveclassisanynon-“Outside”la- whereC isthesetofentitytypes(labelsexclud-
|                                    |     |     |     |     |     |       | ingthe“Outside”),andforeachentitytypec |     |     |     |     | ∈ C, |
| ---------------------------------- | --- | --- | --- | --- | --- | ----- | -------------------------------------- | --- | --- | --- | --- | ---- |
| bel(e.g.,name,phonenumber).Here,TP |     |     |     |     |     | isthe |                                        |     |     |     |     |      |
bin
|                                              |     |     |     |     |     |     | TP ,FP | ,andFN | arethetruepositives,falseposi- |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------------------------------ | --- | --- | --- |
| numberoftokenstrulynon-“Outside”andcorrectly |     |     |     |     |     |     | c      | c      | c                              |     |     |     |
predictedasnon-“Outside”,FP isthenumberof tives,andfalsenegativesrespectively.
bin
tokensactually“Outside”butincorrectlypredicted
G Annotators
| as non-“Outside”, |     | and | FN bin | is the | number | of to- |     |     |     |     |     |     |
| ----------------- | --- | --- | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- |
kenstrulynon-“Outside”butincorrectlypredicted
Theauthorsparticipatedintheannotationprocess
| as“Outside”.        |     |     |     |                    |     |     | for 20 hours | per      | week       | over a period | of 4   | weeks. |
| ------------------- | --- | --- | --- | ------------------ | --- | --- | ------------ | -------- | ---------- | ------------- | ------ | ------ |
|                     |     |     |     |                    |     |     | Seventeen    | external | annotators | contributed   |        | to the |
| Token-LevelMicroF1. |     |     |     | Token-LevelMicroF1 |     |     |              |          |            |               |        |        |
|                     |     |     |     |                    |     |     | task for     | 12 hours | per        | week over 4   | weeks. | These  |
measureshowwellthemodelclassifiestokensinto
|     |     |     |     |     |     |     | annotators | were | compensated | at a | rate of 10,000 |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | ---- | -------------- | --- |
specificentitytypessuchasnameofthepersonand
|     |     |     |     |     |     |     | KRW per | hour, | amounting | to a total | payment | of  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | ---------- | ------- | --- |
phonenumbers.Itexcludesthe“Outside”labeland
|     |     |     |     |     |     |     | 480,000 | KRW per | person. | We consider | this | com- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ----------- | ---- | ---- |
calculatesperformanceusingaggregatedprecision
pensationappropriategiventhelocalstandardsof
andrecallforeachentitytype.Highscoresindicate
livingandthescopeofthework.
correctidentificationandlabelingoftokensrequir-
ingde-identification,suchasclassifying“홍길동” H PerformancebyCaseType
(HongGildong)asanameofthepersonratherthan
Wereportcase-typeprecision,recall,binarytoken-
acorporateentity.
levelF1,andtoken-levelmicroF1undertwodata
Accurateclassificationofentitytypesisessen-
regimes:SingleReplacementandPer-EpochEntity
tialforproperde-identificationofcourtjudgments.
Thisgetsimportanceinthepost-processingstage Replacementdiscussedin 4.2.
Seethetablesbelowfordetailedresults:binary
becausewithoutpreciseentitytypeprediction,the
|            |       |            |     |           |             |     | token-level | in Table | H.1 | (Single) | and Table | H.2 |
| ---------- | ----- | ---------- | --- | --------- | ----------- | --- | ----------- | -------- | --- | -------- | --------- | --- |
| identified | parts | containing |     | sensitive | information |     |             |          |     |          |           |     |
cannotbeproperlyreplacedwithcontextuallycon- (Per-Epoch),andtoken-levelinTableH.3(Single)
andTableH.4(Per-Epoch).AlltablesreportPreci-
| gruent | phrases. | Inaccurate |     | classification |     | can re- |     |     |     |     |     |     |
| ------ | -------- | ---------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
sionandRecall;F1isbinaryforbinarytoken-level
sultinawkwardorincorrectreplacementsinpost-
andmicro-averagedfortoken-level.Allvaluesare
| processing | and | ultimately |     | lead to | undermine | the |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
averagedoverthreeruns(seeds1200,1203,1205)
readabilityoftheanonymizedtext.
foreachcasetype.
| For example,      |     | account | numbers  |      | must    | be accu- |     |     |     |     |     |     |
| ----------------- | --- | ------- | -------- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- |
| rately identified |     | and     | replaced | with | phrases | like     |     |     |     |     |     |     |
I License
“계좌번호1생략”(Accountnumber1omitted)dur-
ingpost-processing.Ifclassifiedasdifferententity
typesuchasaphonenumber,themisclassifiedac-
countnumbermightbeincorrectlyreplacedwith
| a phrase  | like “전화번호 |      | 1 생략” | (Phone        |     | number 1   |     |     |     |     |     |     |
| --------- | ---------- | ---- | ----- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| omitted). | If the     | same | case  | is classified |     | as a busi- |     |     |     |     |     |     |
nessentity,itmightbereplacedwith“A”,andthe
| post-processing |         | result   | is not     | compatible |     | with the |     |     |     |     |     |     |
| --------------- | ------- | -------- | ---------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| current         | law and | practice | concerning |            | the | methods  |     |     |     |     |     |     |
ofanonymization(JudicialRuleNo.1778).
| The | token-level | F1  | score | in our | experiment | is  |     |     |     |     |     |     |
| --- | ----------- | --- | ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
calculatedasfollows:
(cid:80)
|                |     |     |          |     | TP c |     |     |     |     |     |     |     |
| -------------- | --- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|                |     | =   |          | c∈C |      |     |     |     |     |     |     |     |
| MicroPrecision |     |     | (cid:80) |     |      |     |     |     |     |     |     |     |
|                |     |     |          | (TP | +FP  | )   |     |     |     |     |     |     |
|                |     |     | c∈C      |     | c    | c   |     |     |     |     |     |     |
(cid:80)
TP
|     |             |     |          | c∈C | c   |     |     |     |     |     |     |     |
| --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | MicroRecall | =   | (cid:80) |     |     |     |     |     |     |     |     |     |
|     |             |     |          | (TP | +FN | )   |     |     |     |     |     |     |
|     |             |     | c∈C      |     | c   | c   |     |     |     |     |     |     |

SingleReplacement
| Domain | Casetype | Model             | (BinaryToken-Level) |        |        |
| ------ | -------- | ----------------- | ------------------- | ------ | ------ |
|        |          |                   | P                   | R      | F1     |
|        |          | Polyglot-ko(1.3B) | 0.9843              | 0.9589 | 0.9714 |
|        |          | Exaone(2.4B)      | 0.9818              | 0.9462 | 0.9637 |
Compensation
|     |     | Thunder-DeID-360M | 0.9718 | 0.9303 | 0.9506 |
| --- | --- | ----------------- | ------ | ------ | ------ |
fordamage
|       |          | Thunder-DeID-800M | 0.9870 | 0.9774 | 0.9822 |
| ----- | -------- | ----------------- | ------ | ------ | ------ |
|       |          | Thunder-DeID-1.5B | 0.9954 | 0.9663 | 0.9806 |
|       |          | Polyglot-ko(1.3B) | 0.9700 | 0.9336 | 0.9514 |
|       |          | Exaone(2.4B)      | 0.9681 | 0.9529 | 0.9604 |
|       | Eviction | Thunder-DeID-360M | 0.9672 | 0.9070 | 0.9361 |
|       |          | Thunder-DeID-800M | 0.9763 | 0.9506 | 0.9632 |
| Civil |          | Thunder-DeID-1.5B | 0.9709 | 0.9632 | 0.9671 |
|       |          | Polyglot-ko(1.3B) | 0.9727 | 0.9520 | 0.9623 |
|       |          | Exaone(2.4B)      | 0.9812 | 0.9594 | 0.9701 |
Purchase-price
|     |     | Thunder-DeID-360M | 0.9713 | 0.9148 | 0.9421 |
| --- | --- | ----------------- | ------ | ------ | ------ |
ofasale
|     |     | Thunder-DeID-800M | 0.9851 | 0.9628 | 0.9738 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9854 | 0.9600 | 0.9725 |
|     |     | Polyglot-ko(1.3B) | 0.9865 | 0.9726 | 0.9795 |
|     |     | Exaone(2.4B)      | 0.9826 | 0.9614 | 0.9719 |
Securitydeposit
|     |     | Thunder-DeID-360M | 0.9816 | 0.9317 | 0.9559 |
| --- | --- | ----------------- | ------ | ------ | ------ |
disputes
|          |              | Thunder-DeID-800M | 0.9865 | 0.9684 | 0.9773 |
| -------- | ------------ | ----------------- | ------ | ------ | ------ |
|          |              | Thunder-DeID-1.5B | 0.9881 | 0.9695 | 0.9787 |
|          |              | Polyglot-ko(1.3B) | 0.9826 | 0.9588 | 0.9706 |
|          |              | Exaone(2.4B)      | 0.9724 | 0.9718 | 0.9720 |
|          | Bodilyinjury | Thunder-DeID-360M | 0.9886 | 0.9623 | 0.9752 |
|          |              | Thunder-DeID-800M | 0.9905 | 0.9800 | 0.9852 |
|          |              | Thunder-DeID-1.5B | 0.9884 | 0.9806 | 0.9845 |
|          |              | Polyglot-ko(1.3B) | 0.9728 | 0.9508 | 0.9616 |
|          |              | Exaone(2.4B)      | 0.9831 | 0.9473 | 0.9649 |
|          | Drunkdriving | Thunder-DeID-360M | 0.9714 | 0.9164 | 0.9430 |
|          |              | Thunder-DeID-800M | 0.9733 | 0.9488 | 0.9608 |
|          |              | Thunder-DeID-1.5B | 0.9817 | 0.9508 | 0.9660 |
|          |              | Polyglot-ko(1.3B) | 0.9775 | 0.9659 | 0.9717 |
| Criminal |              | Exaone(2.4B)      | 0.9707 | 0.9601 | 0.9654 |
Propertytheft
|     |     | Thunder-DeID-360M | 0.9845 | 0.9418 | 0.9627 |
| --- | --- | ----------------- | ------ | ------ | ------ |
anddeception
|     |                  | Thunder-DeID-800M | 0.9718 | 0.9806 | 0.9762 |
| --- | ---------------- | ----------------- | ------ | ------ | ------ |
|     |                  | Thunder-DeID-1.5B | 0.9911 | 0.9766 | 0.9838 |
|     |                  | Polyglot-ko(1.3B) | 0.9837 | 0.9690 | 0.9763 |
|     |                  | Exaone(2.4B)      | 0.9837 | 0.9561 | 0.9697 |
|     | Sexualmisconduct | Thunder-DeID-360M | 0.9803 | 0.9260 | 0.9524 |
|     |                  | Thunder-DeID-800M | 0.9872 | 0.9705 | 0.9788 |
|     |                  | Thunder-DeID-1.5B | 0.9881 | 0.9650 | 0.9764 |
|     |                  | Polyglot-ko(1.3B) | 0.9758 | 0.9644 | 0.9701 |
|     |                  | Exaone(2.4B)      | 0.9702 | 0.9701 | 0.9701 |
|     | Violence         | Thunder-DeID-360M | 0.9664 | 0.9316 | 0.9486 |
|     |                  | Thunder-DeID-800M | 0.9749 | 0.9778 | 0.9763 |
|     |                  | Thunder-DeID-1.5B | 0.9740 | 0.9809 | 0.9774 |
|     |                  | Polyglot-ko(1.3B) | 0.9641 | 0.9321 | 0.9478 |
|     |                  | Exaone(2.4B)      | 0.9743 | 0.9383 | 0.9559 |
Administrative
| Administrative |     | Thunder-DeID-360M | 0.9814 | 0.9254 | 0.9526 |
| -------------- | --- | ----------------- | ------ | ------ | ------ |
litigation
|     |     | Thunder-DeID-800M | 0.9877 | 0.9555 | 0.9713 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9842 | 0.9811 | 0.9827 |
TableH.1:Binarytoken-levelmetrics(Precision,Recall,andF1)fortheSingleReplacementsetting,reportedby
casetypeandmodel(parametersshowninparentheses).

Per-EpochReplacement
| Domain | Casetype | Model             | (BinaryToken-Level) |        |        |
| ------ | -------- | ----------------- | ------------------- | ------ | ------ |
|        |          |                   | P                   | R      | F1     |
|        |          | Polyglot-ko(1.3B) | 0.9779              | 0.9687 | 0.9732 |
|        |          | Exaone(2.4B)      | 0.9770              | 0.9591 | 0.9679 |
Compensation
|     |     | Thunder-DeID-360M | 0.9611 | 0.9763 | 0.9686 |
| --- | --- | ----------------- | ------ | ------ | ------ |
fordamage
|       |          | Thunder-DeID-800M | 0.9796 | 0.9889 | 0.9842 |
| ----- | -------- | ----------------- | ------ | ------ | ------ |
|       |          | Thunder-DeID-1.5B | 0.9796 | 0.9891 | 0.9843 |
|       |          | Polyglot-ko(1.3B) | 0.9644 | 0.9639 | 0.9641 |
|       |          | Exaone(2.4B)      | 0.9635 | 0.9597 | 0.9616 |
|       | Eviction | Thunder-DeID-360M | 0.9482 | 0.9566 | 0.9524 |
|       |          | Thunder-DeID-800M | 0.9615 | 0.9711 | 0.9663 |
| Civil |          | Thunder-DeID-1.5B | 0.9569 | 0.9803 | 0.9685 |
|       |          | Polyglot-ko(1.3B) | 0.9630 | 0.9650 | 0.9640 |
|       |          | Exaone(2.4B)      | 0.9679 | 0.9714 | 0.9696 |
Paymentof
|     |     | Thunder-DeID-360M | 0.9463 | 0.9667 | 0.9564 |
| --- | --- | ----------------- | ------ | ------ | ------ |
purchaseprice
|     |     | Thunder-DeID-800M | 0.9712 | 0.9822 | 0.9766 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9748 | 0.9851 | 0.9799 |
|     |     | Polyglot-ko(1.3B) | 0.9770 | 0.9732 | 0.9751 |
|     |     | Exaone(2.4B)      | 0.9732 | 0.9736 | 0.9734 |
Securitydeposit
|     |     | Thunder-DeID-360M | 0.9714 | 0.9661 | 0.9687 |
| --- | --- | ----------------- | ------ | ------ | ------ |
disputes
|          |              | Thunder-DeID-800M | 0.9795 | 0.9864 | 0.9829 |
| -------- | ------------ | ----------------- | ------ | ------ | ------ |
|          |              | Thunder-DeID-1.5B | 0.9807 | 0.9878 | 0.9842 |
|          |              | Polyglot-ko(1.3B) | 0.9777 | 0.9746 | 0.9761 |
|          |              | Exaone(2.4B)      | 0.9697 | 0.9803 | 0.9749 |
|          | Bodilyinjury | Thunder-DeID-360M | 0.9811 | 0.9820 | 0.9815 |
|          |              | Thunder-DeID-800M | 0.9875 | 0.9870 | 0.9872 |
|          |              | Thunder-DeID-1.5B | 0.9868 | 0.9898 | 0.9883 |
|          |              | Polyglot-ko(1.3B) | 0.9667 | 0.9645 | 0.9656 |
|          |              | Exaone(2.4B)      | 0.9726 | 0.9685 | 0.9705 |
|          | Drunkdriving | Thunder-DeID-360M | 0.9612 | 0.9572 | 0.9592 |
|          |              | Thunder-DeID-800M | 0.9592 | 0.9795 | 0.9692 |
|          |              | Thunder-DeID-1.5B | 0.9660 | 0.9739 | 0.9699 |
|          |              | Polyglot-ko(1.3B) | 0.9754 | 0.9776 | 0.9765 |
| Criminal |              | Exaone(2.4B)      | 0.9651 | 0.9702 | 0.9676 |
Propertytheft
|     |     | Thunder-DeID-360M | 0.9739 | 0.9767 | 0.9753 |
| --- | --- | ----------------- | ------ | ------ | ------ |
anddeception
|     |                  | Thunder-DeID-800M | 0.9843 | 0.9840 | 0.9841 |
| --- | ---------------- | ----------------- | ------ | ------ | ------ |
|     |                  | Thunder-DeID-1.5B | 0.9850 | 0.9895 | 0.9873 |
|     |                  | Polyglot-ko(1.3B) | 0.9788 | 0.9744 | 0.9766 |
|     |                  | Exaone(2.4B)      | 0.9770 | 0.9638 | 0.9705 |
|     | Sexualmisconduct | Thunder-DeID-360M | 0.9667 | 0.9698 | 0.9682 |
|     |                  | Thunder-DeID-800M | 0.9814 | 0.9840 | 0.9827 |
|     |                  | Thunder-DeID-1.5B | 0.9786 | 0.9851 | 0.9818 |
|     |                  | Polyglot-ko(1.3B) | 0.9679 | 0.9736 | 0.9707 |
|     |                  | Exaone(2.4B)      | 0.9610 | 0.9754 | 0.9681 |
|     | Violence         | Thunder-DeID-360M | 0.9599 | 0.9745 | 0.9672 |
|     |                  | Thunder-DeID-800M | 0.9706 | 0.9874 | 0.9789 |
|     |                  | Thunder-DeID-1.5B | 0.9724 | 0.9942 | 0.9831 |
|     |                  | Polyglot-ko(1.3B) | 0.9603 | 0.9564 | 0.9583 |
|     |                  | Exaone(2.4B)      | 0.9589 | 0.9605 | 0.9597 |
Administrative
| Administrative |     | Thunder-DeID-360M | 0.9666 | 0.9623 | 0.9644 |
| -------------- | --- | ----------------- | ------ | ------ | ------ |
litigation
|     |     | Thunder-DeID-800M | 0.9802 | 0.9814 | 0.9808 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9739 | 0.9898 | 0.9818 |
TableH.2:Binarytoken-levelmetrics(Precision,Recall,andF1)forthePer-EpochReplacementsetting,reported
bycasetypeandmodel(parametersshowninparentheses).

SingleReplacement
| Domain | Casetype | Model             |        | (Token-Level) |         |
| ------ | -------- | ----------------- | ------ | ------------- | ------- |
|        |          |                   | P      | R             | MicroF1 |
|        |          | Polyglot-ko(1.3B) | 0.8793 | 0.8566        | 0.8677  |
|        |          | Exaone(2.4B)      | 0.8285 | 0.7988        | 0.8134  |
Compensation
|     |     | Thunder-DeID-360M | 0.7518 | 0.7195 | 0.7352 |
| --- | --- | ----------------- | ------ | ------ | ------ |
fordamage
|       |          | Thunder-DeID-800M | 0.7949 | 0.7872 | 0.7910 |
| ----- | -------- | ----------------- | ------ | ------ | ------ |
|       |          | Thunder-DeID-1.5B | 0.8280 | 0.8037 | 0.8156 |
|       |          | Polyglot-ko(1.3B) | 0.8936 | 0.8602 | 0.8766 |
|       |          | Exaone(2.4B)      | 0.9108 | 0.8965 | 0.9036 |
|       | Eviction | Thunder-DeID-360M | 0.8963 | 0.8405 | 0.8675 |
|       |          | Thunder-DeID-800M | 0.9234 | 0.8989 | 0.9109 |
| Civil |          | Thunder-DeID-1.5B | 0.8985 | 0.8913 | 0.8949 |
|       |          | Polyglot-ko(1.3B) | 0.8386 | 0.8207 | 0.8296 |
|       |          | Exaone(2.4B)      | 0.8189 | 0.8000 | 0.8092 |
Paymentof
|     |     | Thunder-DeID-360M | 0.8619 | 0.8118 | 0.8361 |
| --- | --- | ----------------- | ------ | ------ | ------ |
purchaseprice
|     |     | Thunder-DeID-800M | 0.9057 | 0.8854 | 0.8954 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9094 | 0.8859 | 0.8975 |
|     |     | Polyglot-ko(1.3B) | 0.8991 | 0.8864 | 0.8927 |
|     |     | Exaone(2.4B)      | 0.8959 | 0.8766 | 0.8861 |
Securitydeposit
|     |     | Thunder-DeID-360M | 0.9312 | 0.8839 | 0.9069 |
| --- | --- | ----------------- | ------ | ------ | ------ |
disputes
|          |              | Thunder-DeID-800M | 0.9411 | 0.9239 | 0.9324 |
| -------- | ------------ | ----------------- | ------ | ------ | ------ |
|          |              | Thunder-DeID-1.5B | 0.9440 | 0.9261 | 0.9349 |
|          |              | Polyglot-ko(1.3B) | 0.8852 | 0.8639 | 0.8744 |
|          |              | Exaone(2.4B)      | 0.8962 | 0.8956 | 0.8958 |
|          | Bodilyinjury | Thunder-DeID-360M | 0.9344 | 0.9096 | 0.9218 |
|          |              | Thunder-DeID-800M | 0.9479 | 0.9378 | 0.9428 |
|          |              | Thunder-DeID-1.5B | 0.9433 | 0.9360 | 0.9396 |
|          |              | Polyglot-ko(1.3B) | 0.8644 | 0.8448 | 0.8545 |
|          |              | Exaone(2.4B)      | 0.9047 | 0.8718 | 0.8879 |
|          | Drunkdriving | Thunder-DeID-360M | 0.8784 | 0.8286 | 0.8527 |
|          |              | Thunder-DeID-800M | 0.9097 | 0.8867 | 0.8980 |
|          |              | Thunder-DeID-1.5B | 0.9078 | 0.8790 | 0.8931 |
|          |              | Polyglot-ko(1.3B) | 0.9040 | 0.8933 | 0.8987 |
| Criminal |              | Exaone(2.4B)      | 0.9039 | 0.8940 | 0.8989 |
Propertytheft
|     |     | Thunder-DeID-360M | 0.9385 | 0.8978 | 0.9177 |
| --- | --- | ----------------- | ------ | ------ | ------ |
anddeception
|     |                  | Thunder-DeID-800M | 0.9456 | 0.9286 | 0.9370 |
| --- | ---------------- | ----------------- | ------ | ------ | ------ |
|     |                  | Thunder-DeID-1.5B | 0.9322 | 0.9186 | 0.9253 |
|     |                  | Polyglot-ko(1.3B) | 0.8900 | 0.8767 | 0.8833 |
|     |                  | Exaone(2.4B)      | 0.8505 | 0.8265 | 0.8383 |
|     | Sexualmisconduct | Thunder-DeID-360M | 0.8879 | 0.8387 | 0.8626 |
|     |                  | Thunder-DeID-800M | 0.8958 | 0.8807 | 0.8882 |
|     |                  | Thunder-DeID-1.5B | 0.8941 | 0.8731 | 0.8834 |
|     |                  | Polyglot-ko(1.3B) | 0.8704 | 0.8602 | 0.8653 |
|     |                  | Exaone(2.4B)      | 0.8828 | 0.8826 | 0.8827 |
|     | Violence         | Thunder-DeID-360M | 0.9036 | 0.8711 | 0.8871 |
|     |                  | Thunder-DeID-800M | 0.9203 | 0.9231 | 0.9217 |
|     |                  | Thunder-DeID-1.5B | 0.9138 | 0.9205 | 0.9171 |
|     |                  | Polyglot-ko(1.3B) | 0.8661 | 0.8373 | 0.8515 |
|     |                  | Exaone(2.4B)      | 0.8999 | 0.8666 | 0.8829 |
Administrative
| Administrative |     | Thunder-DeID-360M | 0.9246 | 0.8718 | 0.8974 |
| -------------- | --- | ----------------- | ------ | ------ | ------ |
litigation
|     |     | Thunder-DeID-800M | 0.9481 | 0.9172 | 0.9324 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9363 | 0.9334 | 0.9349 |
TableH.3:Token-levelmetrics(Precision,Recall,andMicroF1)fortheSingleReplacementsetting,reportedby
casetypeandmodel(parametersshowninparentheses).

Per-EpochReplacement
| Domain | Casetype | Model             |        | (Token-Level) |         |
| ------ | -------- | ----------------- | ------ | ------------- | ------- |
|        |          |                   | P      | R             | MicroF1 |
|        |          | Polyglot-ko(1.3B) | 0.8774 | 0.8688        | 0.8730  |
|        |          | Exaone(2.4B)      | 0.8525 | 0.8372        | 0.8448  |
Compensation
|     |     | Thunder-DeID-360M | 0.7435 | 0.7553 | 0.7493 |
| --- | --- | ----------------- | ------ | ------ | ------ |
fordamage
|       |          | Thunder-DeID-800M | 0.8121 | 0.8197 | 0.8159 |
| ----- | -------- | ----------------- | ------ | ------ | ------ |
|       |          | Thunder-DeID-1.5B | 0.8141 | 0.8220 | 0.8179 |
|       |          | Polyglot-ko(1.3B) | 0.8878 | 0.8874 | 0.8875 |
|       |          | Exaone(2.4B)      | 0.9007 | 0.8971 | 0.8989 |
|       | Eviction | Thunder-DeID-360M | 0.8939 | 0.9019 | 0.8979 |
|       |          | Thunder-DeID-800M | 0.9035 | 0.9125 | 0.9080 |
| Civil |          | Thunder-DeID-1.5B | 0.8967 | 0.9186 | 0.9075 |
|       |          | Polyglot-ko(1.3B) | 0.8322 | 0.8339 | 0.8330 |
|       |          | Exaone(2.4B)      | 0.8460 | 0.8490 | 0.8474 |
Paymentof
|     |     | Thunder-DeID-360M | 0.8646 | 0.8833 | 0.8738 |
| --- | --- | ----------------- | ------ | ------ | ------ |
purchaseprice
|     |     | Thunder-DeID-800M | 0.8902 | 0.9002 | 0.8952 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.8933 | 0.9029 | 0.8981 |
|     |     | Polyglot-ko(1.3B) | 0.8958 | 0.8923 | 0.8940 |
|     |     | Exaone(2.4B)      | 0.8833 | 0.8838 | 0.8835 |
Securitydeposit
|     |     | Thunder-DeID-360M | 0.9268 | 0.9218 | 0.9243 |
| --- | --- | ----------------- | ------ | ------ | ------ |
disputes
|          |              | Thunder-DeID-800M | 0.9430 | 0.9497 | 0.9463 |
| -------- | ------------ | ----------------- | ------ | ------ | ------ |
|          |              | Thunder-DeID-1.5B | 0.9469 | 0.9538 | 0.9503 |
|          |              | Polyglot-ko(1.3B) | 0.8792 | 0.8765 | 0.8778 |
|          |              | Exaone(2.4B)      | 0.8857 | 0.8953 | 0.8904 |
|          | Bodilyinjury | Thunder-DeID-360M | 0.9306 | 0.9314 | 0.9310 |
|          |              | Thunder-DeID-800M | 0.9519 | 0.9515 | 0.9517 |
|          |              | Thunder-DeID-1.5B | 0.9518 | 0.9546 | 0.9532 |
|          |              | Polyglot-ko(1.3B) | 0.8697 | 0.8678 | 0.8688 |
|          |              | Exaone(2.4B)      | 0.8932 | 0.8894 | 0.8913 |
|          | Drunkdriving | Thunder-DeID-360M | 0.8869 | 0.8832 | 0.8851 |
|          |              | Thunder-DeID-800M | 0.9045 | 0.9238 | 0.9140 |
|          |              | Thunder-DeID-1.5B | 0.9158 | 0.9231 | 0.9194 |
|          |              | Polyglot-ko(1.3B) | 0.9097 | 0.9117 | 0.9107 |
| Criminal |              | Exaone(2.4B)      | 0.8964 | 0.9010 | 0.8987 |
Propertytheft
|     |     | Thunder-DeID-360M | 0.9212 | 0.9238 | 0.9225 |
| --- | --- | ----------------- | ------ | ------ | ------ |
anddeception
|     |                  | Thunder-DeID-800M | 0.9399 | 0.9396 | 0.9397 |
| --- | ---------------- | ----------------- | ------ | ------ | ------ |
|     |                  | Thunder-DeID-1.5B | 0.9204 | 0.9246 | 0.9225 |
|     |                  | Polyglot-ko(1.3B) | 0.8799 | 0.8759 | 0.877  |
|     |                  | Exaone(2.4B)      | 0.8556 | 0.8441 | 0.8498 |
|     | Sexualmisconduct | Thunder-DeID-360M | 0.8888 | 0.8916 | 0.8902 |
|     |                  | Thunder-DeID-800M | 0.9021 | 0.9045 | 0.9033 |
|     |                  | Thunder-DeID-1.5B | 0.8768 | 0.8827 | 0.8797 |
|     |                  | Polyglot-ko(1.3B) | 0.8617 | 0.8669 | 0.8643 |
|     |                  | Exaone(2.4B)      | 0.8679 | 0.8810 | 0.8744 |
|     | Violence         | Thunder-DeID-360M | 0.8981 | 0.9118 | 0.9049 |
|     |                  | Thunder-DeID-800M | 0.9043 | 0.9200 | 0.9120 |
|     |                  | Thunder-DeID-1.5B | 0.9209 | 0.9416 | 0.9311 |
|     |                  | Polyglot-ko(1.3B) | 0.8691 | 0.8654 | 0.8672 |
|     |                  | Exaone(2.4B)      | 0.8913 | 0.8928 | 0.8920 |
Administrative
| Administrative |     | Thunder-DeID-360M | 0.9138 | 0.9097 | 0.9118 |
| -------------- | --- | ----------------- | ------ | ------ | ------ |
litigation
|     |     | Thunder-DeID-800M | 0.9372 | 0.9384 | 0.9377 |
| --- | --- | ----------------- | ------ | ------ | ------ |
|     |     | Thunder-DeID-1.5B | 0.9297 | 0.9448 | 0.9372 |
TableH.4:Token-levelmetrics(Precision,Recall,andMicroF1)forthePer-EpochReplacementsetting,reported
bycasetypeandmodel(parametersshowninparentheses).
