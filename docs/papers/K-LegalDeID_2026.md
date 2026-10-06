> 원본: K-LegalDeID_2026.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.7-8 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
| K-LegalDeID: |     |                   | A   | Benchmark |             | Dataset   | and   | KLUEBERT-CRF |           |     |     | for |     |
| ------------ | --- | ----------------- | --- | --------- | ----------- | --------- | ----- | ------------ | --------- | --- | --- | --- | --- |
|              |     | De-identification |     |           |             | in Korean | Court |              | Judgments |     |     |     |     |
|              |     | WooseokChoi       |     |           | HyungbinKim |           |       | YonDohnChung |           |     |     |     |     |
DepartmentofComputerScienceandEngineering,KoreaUniversity
|     |     | {woosukqw, |     | hyungbinkim, |     |     | ydchung}@korea.ac.kr                           |     |             |                  |     |     |      |
| --- | --- | ---------- | --- | ------------ | --- | --- | ---------------------------------------------- | --- | ----------- | ---------------- | --- | --- | ---- |
|     |     | Abstract   |     |              |     |     | researchandlegaleducation,andfacilitateseffec- |     |             |                  |     |     |      |
|     |     |            |     |              |     |     | tive monitoring                                |     | of judicial | decision-making. |     |     | Fur- |
The Korean legal system mandates public thermore, the disclosure of judgments helps pre-
| access to          | court | judgments |            | to ensure        | judi- |     |                 |     |           |          |        |          |         |
| ------------------ | ----- | --------- | ---------- | ---------------- | ----- | --- | --------------- | --- | --------- | -------- | ------ | -------- | ------- |
|                    |       |           |            |                  |       |     | vent corruption |     | and abuse | of power | within |          | the ju- |
| cial transparency. |       | However,  |            | this requirement |       |     |                 |     |           |          |        |          |         |
|                    |       |           |            |                  |       |     | dicial system,  |     | promotes  | equal    | access | to legal | in-     |
| conflicts          | with  | privacy   | protection | obligations      |       |     |                 |     |           |          |        |          |         |
formationregardlessofsocialoreconomicstatus,
| due to the | prevalence |     | of Personally |     | Identi- |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
fiable Information (PII) in legal documents. and contributes to the development of legal tech-
To address this challenge, we introduce K- nology by supplying essential data for AI-based
LegalDeID, a large-scale benchmark dataset legalservicesandresearch.
and an efficient KLUEBERT-CRF model for However, several challenges impede the effec-
| de-identification |     | for Korean |     | court judgments. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiveimplementationofjudgmentdisclosureinKo-
| Our primary | contribution |     | is  | a new large-scale |     |     |            |            |     |              |        |     |        |
| ----------- | ------------ | --- | --- | ----------------- | --- | --- | ---------- | ---------- | --- | ------------ | ------ | --- | ------ |
|             |              |     |     |                   |     |     | rean legal | documents. |     | First, there | exists | an  | inher- |
benchmarkdatasetspanning39legaldomains,
|          |         |              |     |           |        |     | ent conflict | between |     | the constitutional |     | mandate |     |
| -------- | ------- | ------------ | --- | --------- | ------ | --- | ------------ | ------- | --- | ------------------ | --- | ------- | --- |
| with its | quality | is validated |     | by a high | inter- |     |              |         |     |                    |     |         |     |
fortransparencyandtheobligationtoprotectPer-
annotatoragreement(IAA)withFleiss’Kappa
of 0.7352. Our results demonstrate that a sonally Identifiable Information (PII), including
lightweight KLUEBERT-CRF model, when names, resident registration numbers, addresses,
trained on our dataset, achieves state-of-the- and other personal identifiers for not only parties
artperformancewithanentity-levelmicroF1
butalsowitnesses,victims,andvariousstakehold-
| scoreof0.9923.Ourend-to-endframeworkof- |     |                     |     |     |           |     | ers.      |      |                   |     |           |     |      |
| --------------------------------------- | --- | ------------------- | --- | --- | --------- | --- | --------- | ---- | ----------------- | --- | --------- | --- | ---- |
| fers a practical                        |     | and computationally |     |     | efficient |     |           |      |                   |     |           |     |      |
|                                         |     |                     |     |     |           |     | Secondly, | most | de-identification |     | processes |     | rely |
solutionforreal-worldlegalsystems.
|     |     |     |     |     |     |     | on manual | methods, | which | introduce |     | significant |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | --------- | --- | ----------- | --- |
1 Introduction bottlenecks. Manual masking typically requires
|     |     |     |     |     |     |     | approximately |     | two weeks | per | document | and | sub- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | -------- | --- | ---- |
The Korean legal system has established a funda- stantial human resources, severely limiting the
mental principle that court proceedings and judg- scope and speed of judgment disclosure. Despite
ments must be transparent to ensure public trust existing guidelines for personal information pro-
andaccountability.Article109oftheKoreanCon- tection,manualprocessingmayyieldinconsistent
stitution mandates that ‘the trial and judgment of results that vary in quality across cases and per-
courtsshallbeopentothepublic,’withanexcep- sonnel. Only about 1.6 million judgment docu-
tion allowing trials to be closed only if openness ments, approximately 5.97% of the total (Admin-
mightharmnationalsecurity,publicorder,orgood istration,2019),haveundergonede-identification,
morals. The objective of this constitutional provi- highlighting the limited extent of automated or
sion is to guarantee transparency in judicial pro- systematicanonymizationtodate.
ceedings, thereby maintaining public trust in the Korean courts have attempted to address these
judiciary while simultaneously safeguarding the challenges through automated systems, including
rightsofthepartiesinvolvedinlitigation. an‘intelligentjudgmentde-identificationsystem.’
Thenecessityofdisclosingcourtjudgmentsex- However, this system performs poorly, achieving
tends beyond mere constitutional compliance to onlyaround8%accuracyinidentifyingandmask-
encompassbroadersocietalbenefits.Publicaccess ingPII(Administration,2025).Thelimitedeffec-
tothesedocumentsenablescitizenstounderstand tivenessof currentautomation stemsfrom several
legalprinciplesandprecedents,supportsacademic key technical challenges: the unique characteris-
2308
Proceedingsofthe19thConferenceoftheEuropeanChapteroftheAssociationforComputationalLinguistics
Volume1:LongPapers,pages2308–2325
March24-29,2026©2026AssociationforComputationalLinguistics

tics of Korean legal documents, linguistic chal- de-identification in the legal domain. By analyz-
lenges such as agglutinative morphology and ir- ingexistingapproaches,weidentifythecriticalre-
regular spacing, and a severe shortage of high- searchgapsthatourworkaimstoaddress.
qualitytrainingdata.
2.1 De-identificationinGeneralDomains
| To overcome | these | challenges, |     | we propose | an  |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
enhanced framework that combines KLUEBERT Automated de-identification is a well-established
with a Conditional Random Field (CRF) layer, research area, driven by privacy regulations such
significantly improving PII detection and mask- as HIPAA in healthcare and GDPR in Europe.
ing in Korean legal documents. To this end, we Early approaches were predominantly rule-based,
introducetwonewdatasets—onecomprisingcase relyingonregularexpressionsandspecializeddic-
documents from 39 legal categories and another tionaries to detect explicit identifiers (Sweeney,
comprising multi-turn conversations from Korean 2002;Guptaetal.,2004).
SNS—and establish a unified 11-label PII anno- With the development of deep learning, re-
tation scheme. Our method addresses the limita- search shifted towards sequence labeling models
tions of existing systems by resolving ambigui- using contextual embeddings (Dernoncourt et al.,
ties in masking guidelines, and implementing an 2017), and fine-tuning large pre-trained language
end-to-end framework that ensures consistent en- models became the de facto standard for Named
tity anonymization while maintaining document Entity Recognition (NER) (Lee et al., 2020; Bog-
coherenceandlegalrelevance. danov et al., 2024). More recently, the paradigm
Thispaperprovidesevidenceforthevalueofof- has evolved towards Large Language Models
fering de-identified legal documents and supports (LLMs), exploring generative approaches via in-
furtherresearchinrelateddomains.Themaincon- structiontuningorzero-shotpromptingtoaddress
tributionsofthispaperareasfollows: data scarcity and generalization challenges (May-
hewetal.,2024;Wangetal.,2025).
| • We introduce |                       | the     | first large-scale, |              | high- |          |         |               |     |            |             |             |
| -------------- | --------------------- | ------- | ------------------ | ------------ | ----- | -------- | ------- | ------------- | --- | ---------- | ----------- | ----------- |
|                |                       |         |                    |              |       | Despite  | these   | advances,     |     | it remains |             | challenging |
| quality        | benchmark             | dataset |                    | specifically | de-   |          |         |               |     |            |             |             |
|                |                       |         |                    |              |       | to apply | general | methodologies |     |            | to specific | do-         |
| signed         | for de-identification |         |                    | for Korean   | court |          |         |               |     |            |             |             |
mains(Szawernaetal.,2024;Larsonetal.,2024).
judgments,comprising46,973annotatedsen-
|     |     |     |     |     |     | While these | approaches |     | are | effective | in  | achieving |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | --------- | --- | --------- |
tencesfrom2,000casesacross39diversele-
|            |     |     |     |     |     | their specific | objectives, |     | they | are     | not          | directly ap- |
| ---------- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ---- | ------- | ------------ | ------------ |
| galfields. |     |     |     |     |     | plicable       | to domains  |     | that | require | fine-grained | se-          |
manticdistinctionsandhigh-qualitygroundtruth.
| • The dataset’s |       | integrity | is         | validated  | by a |     |     |     |     |     |     |     |
| --------------- | ----- | --------- | ---------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Fleiss’         | Kappa | score     | of 0.7352, | indicating |      |     |     |     |     |     |     |     |
2.2 De-identificationinLegalDomain
substantialinter-annotatoragreementanden-
|     |     |     |     |     |     | Research | on de-identification |     |     | in  | the legal | domain |
| --- | --- | --- | --- | --- | --- | -------- | -------------------- | --- | --- | --- | --------- | ------ |
suringconsistent,trustworthylabeling.
|     |     |     |     |     |     | is still | underexplored, |     | despite | presenting |     | unique |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | ---------- | --- | ------ |
• We introduce an enhanced model architec- challenges posed by complex sentence structures,
ture,KLUEBERT-CRF,specificallydesigned specialized terminology in documents like court
| to handle | Korean | language |     | and | legal text | judgments. |     |     |     |     |     |     |
| --------- | ------ | -------- | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
complexities such as agglutinative morphol- Sincefewstudieshaveaddressedthesedomain-
|     |     |     |     |     |     | specific | characteristics, |     | high-quality |     |     | benchmark |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------------ | --- | --- | --------- |
ogyandintricatesentencestructures.
|              |        |                   |     |           |           | datasets       | required |        | to train | and  | evaluate      | de- |
| ------------ | ------ | ----------------- | --- | --------- | --------- | -------------- | -------- | ------ | -------- | ---- | ------------- | --- |
| • We present | an     | end-to-end        |     | framework | that      |                |          |        |          |      |               |     |
|              |        |                   |     |           |           | identification |          | models | are      | also | non-existent. | Al- |
| spans the    | entire | de-identification |     |           | pipeline, |                |          |        |          |      |               |     |
thoughsomestudiesutilizeLLMstogeneratesyn-
| demonstrating |     | a practical |     | pathway | for |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
theticlegaltextdataset(Savkinetal.,2025),these
| deploying | automated, |     | high-accuracy |     | de- |            |          |     |              |     |            |         |
| --------- | ---------- | --- | ------------- | --- | --- | ---------- | -------- | --- | ------------ | --- | ---------- | ------- |
|           |            |     |               |     |     | approaches | struggle |     | to replicate |     | the strict | formal- |
identificationforreal-worldenvironments.
|     |     |     |     |     |     | ism and | structural | integrity |     | of  | court | judgments. |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | --- | ----- | ---------- |
Thislackofbothdomain-specificmethodsandre-
2 RelatedWork
|     |     |     |     |     |     | liable datasets |     | indicates | the | need | for a | systematic |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ---- | ----- | ---------- |
Inthissection,wereviewpriorresearchintwokey approach to build a legal-domain benchmark and
areas relevant to our work: (1) the broader con- todesigneffectivede-identificationmodels.
text of de-identification across various domains, InthecontextofKoreanlegaldocuments,these
and(2)specificchallengesandmethodologiesfor challenges are compounded by the agglutina-
2309

tive nature of the Korean language, which intro- bothusabilityandprocessingspeed.
duces morphological ambiguity and inconsistent
3.2 ConditionalRandomField.
spacing, making accurate tokenization and entity
boundarydetectionparticularlydifficult.Thunder- A Conditional Random Field (CRF) is a popular
DeID(Hahmetal.,2025)isaframeworkdesigned methodforsequencelabelingtasks.Itlearnsanin-
specifically for Korean court judgments. It pro- dependentper-positionclassifierthatmapseachx
vides a dataset for detecting PII in Korean legal toy ,whereyisalabelvector,y = y ,y ,...,y .
s 0 1 T
documents.WhileThunder-DeIDrepresentsasig- The CRF models the conditional probability dis-
nificant step forward, its scope has two notable tribution p(y x) directly. This modeling approach
|
limitations.First,itsdatasetisspecificallyfocused ensuresthatdependenciesinvolvingonlyvariables
on three types of criminal cases, including sexual in x do not affect the conditional model, allow-
assault, assault, and fraud. Second, its annotation ingforamuchsimplerstructurecomparedtojoint
scheme does not employ a BIO (Beginning, In- models(Suttonetal.,2012).
side, Outside) tagging, which poses challenges in
4 ProposedMethod
delineatingtheboundariesofconsecutivelyoccur-
ring entities. This highlights the need for a more
4.1 Datasets
comprehensive dataset that covers a wider range
Ourtrainingandtestdataarederivedfromacom-
oflegaldomainsandanannotationapproachsuit-
bination of three distinct sources. The datasets
ableforrobustentityboundarydetection.
used are a multi-turn SNS conversation dataset,
OurPosition.Basedonthelimitationsinprior
our newly curated Court Judgment Dataset, and
research, our work addresses the critical lack of a
publicly available Thunder-DeID Dataset (Hahm
comprehensivebenchmarkbyintroducingalarge-
etal.,2025).Thisintegrationyieldsacomprehen-
scale, high-quality dataset covering a wide spec-
sive PII dataset of approximately one million in-
trumofKoreanlegalcategories.Weemphasizethe
stances.
dataset’sreliability,validatedthroughrigorousan-
A key challenge is that court judgments must
notationprotocolsandhighinter-annotatoragree-
bede-identifiedbeforepublicrelease,asmandated
ment. Our approach prioritizes the creation of a
by Supreme Court Regulations 1. To address this,
foundationalpublicresourceandintroducesanef-
wedevelopapipelinetoprocessthesedocuments
fective and practical solution for de-identification
into a usable format. In addition, we collect and
withintheKoreanlegalsystem.
processtheSNSconversationdatasetusingadata
generation logic to further enhance our training
3 Preliminaries
data. The following subsections detail our data
3.1 KLUEBERT-NER. collection process, the masking rules applied, the
synthetic data generator, and the specific adjust-
KLUEBERT is a pre-trained BERT model for the
mentsmadeforeachdataset.
Korean language (Park et al., 2021), distributed
under the CC BY-NC-SA 4.0 License. KLUE- 4.1.1 DataCollection
BERT is designed to perform eight Korean natu-
Wecollectatotalof3,246,886utterances,includ-
ral language understanding tasks, including topic
inganSNSmulti-turnconversationdataset,2,000
classification, semantic textual similarity, natural
case court judgments, and 4,500 sentences from
language inference, named entity recognition, re-
theThunder-DeIDDataset.Thecombineddataset
lation extraction, dependency parsing, machine
consistsof1,091,998instances,whichare908,422
reading comprehension, and dialogue state track-
of SNS, 138,576 of Court Judgement, and 45,000
ing. It employs a morpheme-based subword tok-
ofThunder-DeIDDataset.
enization scheme which first tokenizes raw text
SNS Dataset This is the ‘Korean SNS Multi-
into morphemes using a morphological analyzer,
turn Conversation Data’ published on AI Hub1,
followed by applying Byte Pair Encoding (BPE)
consistingofconversationdatabuiltaround9con-
(Sennrich et al., 2015). After building the vocab-
versation topics involving 2 or 3 participants in
ulary,KLUEBERTusesonlytheBPEmodeldur-
ing inference, allowing word sequences to be to-
1ThisresearchusedSNSMulti-turnConversationdatasets
from ‘The Open AI Dataset Project (AI-Hub, S. Korea)’.
kenized to reflect morphemes without requiring a
This data information can be accessed through ‘AI-Hub
morphological analyzer. This approach improves (www.aihub.or.kr)’.
2310

multi-turn interactions. The topics are Health and Hub use their own distinct PII masking schemes,
Food&Beverage,EconomyandSociety,Science weimplementastandardizedprocesstotransform
and Technology, Culture, Lifestyle, and Leisure, allcollecteddatatoconformtoournewannotation
| Beauty | and Fashion, |     | Sports | and | E-sports, | Travel | framework. |     |     |     |     |     |     |
| ------ | ------------ | --- | ------ | --- | --------- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
and Attractions, Politics, and Content preference. We prepare an initial annotation scheme us-
| Politics | accounts | for | 1.84%, | Economy   |        | and Soci- |            |            |               |      |      |              |     |
| -------- | -------- | --- | ------ | --------- | ------ | --------- | ---------- | ---------- | ------------- | ---- | ---- | ------------ | --- |
|          |          |     |        |           |        |           | ing entity | categories |               | that | meet | the document |     |
| ety for  | 21.68%,  | and | the    | remaining | topics | each      |            |            |               |      |      |              |     |
|          |          |     |        |           |        |           | ‘Standards | for        | Anonymization |      | for  | Viewing      | and |
comprise approximately 10%. Speaker composi- Copying Court Judgments’, while also being
| tion ratios | are | 90.96% | for | two-person |     | conversa- |        |         |     |               |     |            |     |
| ----------- | --- | ------ | --- | ---------- | --- | --------- | ------ | ------- | --- | ------------- | --- | ---------- | --- |
|             |     |        |     |            |     |           | deemed | capable | of  | appropriately |     | segmenting | the |
tionsand9.04%forthree-personconversations.
|     |     |     |     |     |     |     | types of | PII within | the | content | of  | the court | judg- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------- | --- | --------- | ----- |
Court Judgment Dataset We collect court ment data. In addition, through multiclass preci-
judgment publicly available on the Ministry of sion, recall, and F1 score analysis, we merge en-
| Government |     | Legislation’s |     | National | Law | Informa- |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
titycategoriesthatexhibitedhighconfusion,such
tion Center by legal field. We collect a total of as school and department, company and business
2,000 cases, with 50 cases each collected from division, and URL and web-mail. Finally, we es-
39 of the 44 classified legal fields (except for tablish a BIO annotation scheme comprising 11
| civil law, | which | had | 100 | cases). | To broadly | en- |          |      |             |     |       |          |      |
| ---------- | ----- | --- | --- | ------- | ---------- | --- | -------- | ---- | ----------- | --- | ----- | -------- | ---- |
|            |       |     |     |         |            |     | types of | PII, | as follows: |     | name, | address, | num- |
compass characteristics of case content—such as ber, bank name, account number, security code,
crime scenarios and frequently occurring case school,company,URL,email,ID.Thisentitycat-
| types that | may | vary | by legal | field—we |     | collected |                 |     |      |              |     |          |        |
| ---------- | --- | ---- | -------- | -------- | --- | --------- | --------------- | --- | ---- | ------------ | --- | -------- | ------ |
|            |     |      |          |          |     |           | egory functions |     | as a | placeholder, |     | and data | corre- |
a mix of lower court and Supreme Court cases sponding to each category is inserted by the syn-
| across      | all fields | except    |        | those                  | with fewer  | than | theticdatagenerator. |     |     |     |     |     |     |
| ----------- | ---------- | --------- | ------ | ---------------------- | ----------- | ---- | -------------------- | --- | --- | --- | --- | --- | --- |
| 50 publicly | available  |           | cases: | Part                   | 2 (National | As-  |                      |     |     |     |     |     |     |
| sembly),    | Part       | 12 (Civil |        | Defense·Firefighting), |             |      |                      |     |     |     |     |     |     |
4.1.3 SyntheticDataGenerator
| Part 22 | (Tobacco·Ginseng), |     |     | Part | 29  | (Industrial |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
TogenerateappropriatedataforeachPIIcategory,
| standards·measurements) |     |     |     | and | Part 44 | (Foreign |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Affairs). For precedents with overlapping case a dedicated generator is required for each cate-
gory.ConsideringthatthedataconsistsofKorean
| numbers, | the | final | version | from | the lower | court |                |     |        |       |            |     |         |
| -------- | --- | ----- | ------- | ---- | --------- | ----- | -------------- | --- | ------ | ----- | ---------- | --- | ------- |
|          |     |       |         |      |           |       | court judgment |     | texts, | these | generators | are | created |
wasselectedtomaintainconsistency.
|              |     |         |     |       |     |            | based on | Korean | statistical |     | data. Datasets |     | for sur- |
| ------------ | --- | ------- | --- | ----- | --- | ---------- | -------- | ------ | ----------- | --- | -------------- | --- | -------- |
| Thunder-DeID |     | Dataset |     | (Hahm | et  | al., 2025) |          |        |             |     |                |     |          |
Thunder-DeID Dataset, created by the Graduate name, given name, address, school, department,
company,workdepartment,URL,andbankname
SchoolofDataScienceatSeoulNationalUniver-
|          |          |     |     |                   |     |        | are constructed |     | using | information |     | collected | from |
| -------- | -------- | --- | --- | ----------------- | --- | ------ | --------------- | --- | ----- | ----------- | --- | --------- | ---- |
| sity, is | designed | for | the | de-identification |     | within |                 |     |       |             |     |           |      |
Korean court judgment available under the CC sourcessuchasStatisticsKorea.Additionally,data
|          |     |          |     |             |     |           | generation | logic | is  | implemented |     | for each | of the |
| -------- | --- | -------- | --- | ----------- | --- | --------- | ---------- | ----- | --- | ----------- | --- | -------- | ------ |
| BY-NC-SA | 4.0 | License. |     | It consists | of  | a labeled |            |       |     |             |     |          |        |
following:ID,email,phonenumber,accountnum-
| court judgment |     | dataset | and | a named |     | entity list |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
dataset. The Thunder-DeID Dataset comprises a ber, and security code. This logic ensures that the
total of 4,500 sentences, with 1,500 sentences for generateddataconformstoformatsusedinKorea
whilemaintainingrandomness.
eachofthethreecasetypes:sexualassault,assault
|     |     |     |     |     |     |     | The | data generation |     | process | is  | performed | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | --------- | --- |
andfraud.Thisdatasetprovides27,402annotated
PIIentitieslabeledwith595uniqueplaceholders. showninFigure1.Structuralalignmentisfirstap-
|     |     |     |     |     |     |     | plied to | the SNS | Dataset | via | category | specializa- |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | --- | -------- | ----------- | --- |
4.1.2 DataMaskingRule
tionandtotheThunder-DeIDDatasetviacategory
To ensure both regulatory compliance and anno- aggregation,ensuringtheysharethesameannota-
tation consistency, we develop a unified annota- tionschemeastheCourtJudgmentDataset.When
tion scheme for de-identification. A primary re- a PII placeholder (#@(\w+)#) is detected in each
quirementisadherencetotheSupremeCourtAd- dataset, contextually appropriate synthetic data is
ministrative Office’s ‘Standards for Anonymiza- inserted using the generator corresponding to that
Judgment’2.
tion for Viewing and Copying Be- PII category. Then, the PII category type and its
causedatasetssuchasSNSconversationsfromAI
|     |     |     |     |     |     |     | start and | end | indices | are added | to  | the label | infor- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --------- | --- | --------- | ------ |
mation.ThisdataisthenalignedandBIO-labeled
2SupremeCourtTrialRegulationNo.1778revisedonAu-
| gust9,2021. |     |     |     |     |     |     | atthetokenlevelusingtheKLUEBERTtokenizer. |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
2311

SNS
|     |     |     |                                | Category Specialization |     |     | {                                   |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------ | ----------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Raw text: 내 #@Financial#로 송금해줘 |                         |     |     | sentence: “내 3521521412176로 송금해줘“,  |     |     |     |     |     |     |
spans: [{label: “Account_number”, start: 2, end: 14}]
}
Specialized Text: 내 #@Account_number#로 송금해줘
Court
Judgement
{
Structure Integration  Raw text: 피고는 #@Company#와 사이에 체결된 ... sentence: “피고는 주식회사 스트롱시프트와 사이에 체결된…”,
spans: [{label: “Company”, start: 4, end: 14}]
| & Data Generation |     |     |     |     |     |     | }   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thunder
|     |     |     |                                                   | Category Aggregation |     |     | {                                     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------------------------- | -------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Raw text: 피고인은 전북 부안군  <<<Administrative_town>>>B |                      |     |     | sentence: “피고인은 전북 부안군 부발읍 10에 있는..”, |     |     |     |     |     |     |
<<</ Administrative_town>>>에 있는...
spans: [{label: “Address”, start: 12, end: 17}]
}
Aggregated text: 피고인은 전북 부안군 #@Address#에 있는...
|              |             |     |       |      | External Data  | Synthetic PII |         |         |         |      |      |     |     |
| ------------ | ----------- | --- | ----- | ---- | -------------- | ------------- | ------- | ------- | ------- | ---- | ---- | --- | --- |
|              |             |     |       |      | Source         | Generator     |         |         |         |      |      |     |     |
|              | Token ID :  |     | 0     | 8305 | 2259 13545     | 3791          | 2498    | 2067    | 5126    | 2522 | 3734 |     |     |
| BIO labeling | Token :     |     |       |      |                |               |         |         |         |      |      | ... |     |
|              |             |     | [CLS] | 피고   | ##는 주식회사       | ##스트          | ##롱     | ##시     | ##프트    | ##와  | 사이   |     |     |
|              | Label :     |     | O     | O    | O B-           | I-            | I-      | I-      | I-      | O    | O    |     |     |
|              |             |     |       |      | Company        | Company       | Company | Company | Company |      |      |     |     |
Figure1:DataGenerationandBIOlabeling
4.1.4 SNSPIIDataset ditionally, this integration is necessary because
|         |            |         |     |     |           | Thunder-DeID |     |     | uses a | custom | tokenizer | (Mecab- |     |
| ------- | ---------- | ------- | --- | --- | --------- | ------------ | --- | --- | ------ | ------ | --------- | ------- | --- |
| The SNS | multi-turn | dataset | has | its | own anno- |              |     |     |        |        |           |         |     |
tations, which we transform into a format com- ko + BPE) and a simple tagging scheme, whereas
|         |          |         |     |        |            | our | approach |     | uses the | KLUEBERT |     | wordpiece |     |
| ------- | -------- | ------- | --- | ------ | ---------- | --- | -------- | --- | -------- | -------- | --- | --------- | --- |
| patible | with our | scheme. | We  | retain | categories |     |          |     |          |          |     |           |     |
tokenizerandaBIOannotationscheme.
| that directly | matched | our | method, | such | as names |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
and phone numbers. For categories with broader We align the tokens to match the differences
scopes—likefinance,affiliation,andaccount—we with our tokenizer and restructured the labels of
|     |     |     |     |     |     | each | dataset | to  | the BIO | format, |     | making | them |
| --- | --- | --- | --- | --- | --- | ---- | ------- | --- | ------- | ------- | --- | ------ | ---- |
subdividethemintoourmoregranularlabels.This
subdivision is processed in batches using Ope- compatible for integration into our dataset. Fi-
nAI’s GPT-4o-mini. After filtering out sentences nally, a total of 4,500 sentence-level instances are
|     |     |     |     |     |     | constructed, |     | containing |     | 27,402 | PII | entities | in the |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------ | --- | -------- | ------ |
thatlackedPII,wecollectthecorrectlyprocessed
|            |               |     |           |     |             | dataset. |     | However, | the | resulting | 4,500 | sentence- |     |
| ---------- | ------------- | --- | --------- | --- | ----------- | -------- | --- | -------- | --- | --------- | ----- | --------- | --- |
| data along | with existing |     | data that | did | not require |          |     |          |     |           |       |           |     |
subdivision.Thisprocessyieldsatotalof908,422 level instances were significantly fewer than the
sentence-level instances, containing 970,129 PII other two datasets. To address this data imbal-
ance,weexpandedthedatasetto45,000instances
entities.
|     |     |     |     |     |     | through |     | data augmentation |     | using | placeholder |     | re- |
| --- | --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | ----- | ----------- | --- | --- |
4.1.5 Thunder-DeIDDataset
placement.IncontrasttoCourtJudgementdataset,
The Thunder-DeID Dataset presents several inte- theentitydistributionisconcentratedinthreespe-
grationchallenges,asitusedadifferentannotation cific fields (57.5%, 21.6%, and 20.9%, respec-
schemeandtokenizer. tively). About the details about data augmenta-
Therefore, a pre-processing step is re- tionofThunder-DeIDDataset,pleaserefertoAp-
| quired        | to integrate | it   | into                    | our dataset. | The     | pendixE. |                         |     |     |     |     |     |     |
| ------------- | ------------ | ---- | ----------------------- | ------------ | ------- | -------- | ----------------------- | --- | --- | --- | --- | --- | --- |
| Thunder-DeID  | Dataset      |      | placeholders            |              | are {0: |          |                         |     |     |     |     |     |     |
|               |              |      |                         |              |         | 4.1.6    | CourtJudgmentPIIDataset |     |     |     |     |     |     |
| ‘IT_company’, | 1:           | ‘O’, | 2: ‘internet_café’,..., |              | 594:    |          |                         |     |     |     |     |     |     |
‘mobile_phone_case_store’}. We classify its 595 We create the Court Judgment PII Dataset by
placeholder types according to our 11 categories collecting court judgments published by the Na-
and match them using a custom ‘Thunder-To- tional Law Information Center and processing
Ours’ mapping rule (e.g., ‘IT_company’ them according to our annotation scheme. Dur-
→
‘company’, ‘internet_café’ ‘address’, ..., ing this process, eight annotators follow annota-
→
‘mobile_phone_case_store’ ‘address’). Ad- tion guidelines based on the Court Administra-
→
2312

tionOffice’sanonymizationstandardsandprovide entity-levelmicroF1scoreisimprovedby2.98%.
mutual feedback to improve the agreement be- Additionally, after training evaluation, we con-
tween annotators. To measure this inter-annotator duct an analysis of cases where the model in-
agreement (IAA), we calculate the Fleiss’ Kappa correctly tokenized and resulted in incorrect BIO
score (Landis and Koch, 1977). This metric sta- labeling. We select 26 pieces of vocabulary that
tistically measures the agreement among three or could potentially be PII from tokens that caused
moreevaluatorsoncategoricaldata.Themeasured errors in approximately 5% of cases (600 out of
Fleiss’Kappascoreis0.7352,indicatingsubstan- 11,653).Thesepiecesofvocabularyareduplicates
| tial agreement |     | according | to  | the standard | interpre- |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
inthetokenizer’svocabularyduetoincorrecttok-
tation of the scale. This high level of consistency enizationinthesamecases.Weaddthesetermsas
among annotators signify the reliability and qual- properlytokenizedunitstothemodel’svocabulary
ity of the data labeling. Finally, we construct a andfine-tunedourmodelaccordingly.
dataset of 138,576 sentence-level instances from Our KLUEBERT-CRF model, with approx-
2,000 court judgments, containing 51,245 PII en- imately 110 million parameters, features a
tities. The distribution of these entities across the lightweight structure compared to other models
| 39 law | fields | is more | balanced | and | covers | more |              |         |          |     |                 |     |
| ------ | ------ | ------- | -------- | --- | ------ | ---- | ------------ | ------- | -------- | --- | --------------- | --- |
|        |        |         |          |     |        |      | in the legal | domain. | Compared |     | to Thunder-DeID |     |
diversefieldscomparedtothepriorwork.Forde- model(360Mparameters),itssmallersizeapprox-
tailed statistics and distribution figures, please re- imately 68% offers practical advantages in mem-
fertoFigure3inAppendixH. oryusageduringdeploymentincourtsystems.
4.2 KLUEBERT-CRF
|     |     |     |     |     |     |     | 4.3 End-to-EndMaskingFramework |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
The de-identification for court judgment can be For each PII symbol, synthetic data is inserted
| defined | as a | Named | Entity | Recognition |     | (NER) |     |     |     |     |     |     |
| ------- | ---- | ----- | ------ | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- |
basedonstatisticaldatatoconstructaPIIdataset,
| task that | accurately | detects |     | entity boundaries |     | by  |         |              |     |       |            |     |
| --------- | ---------- | ------- | --- | ----------------- | --- | --- | ------- | ------------ | --- | ----- | ---------- | --- |
|           |            |         |     |                   |     |     | and the | KLUEBERT-CRF |     | model | is trained | us- |
understandingthecontextofentiresentences.Ko- ingthisdataset.Whenacourtjudgmentdocument
rean, being an agglutinative language, has am- is provided into the model, it identifies entities
| biguous | word | boundaries, |     | and legal | documents |     |            |           |      |       |               |     |
| ------- | ---- | ----------- | --- | --------- | --------- | --- | ---------- | --------- | ---- | ----- | ------------- | --- |
|         |      |             |     |           |           |     | within the | documents | that | could | be identified | as  |
feature complex syntactic structures composed of PII. PII with specific patterns (e.g., resident reg-
long sentences and specialized terminology. To istration numbers, vehicle registration numbers)
| effectively | handle | these | domain | characteristics, |     |     |           |           |           |     |               |     |
| ----------- | ------ | ----- | ------ | ---------------- | --- | --- | --------- | --------- | --------- | --- | ------------- | --- |
|             |        |       |        |                  |     |     | undergoes | secondary | filtering |     | using regular | ex- |
weadaptKLUEBERT—apre-trainedtransformer
|     |     |     |     |     |     |     | pressions | to detect | PII within |     | the document. | The |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | ------------- | --- |
encoder model trained on Korean corpora (Park detected PII is then masked in accordance with
| et al., 2021)—as |           | our | baseline.       | However, | KLUE-   |        |                     |              |              |             |               |      |
| ---------------- | --------- | --- | --------------- | -------- | ------- | ------ | ------------------- | ------------ | ------------ | ----------- | ------------- | ---- |
|                  |           |     |                 |          |         |        | court anonymization |              | regulations. |             | Specifically, | to   |
| BERT alone       | struggles |     | to sufficiently |          | reflect | inter- |                     |              |              |             |               |      |
|                  |           |     |                 |          |         |        | preserve            | the semantic |              | consistency | of the        | doc- |
token dependencies, leading to errors such as im- ument, identical PII entities appearing multiple
possible tag transitions (e.g., ‘I-’ tag following timeswithinthesamedocumentarereplacedwith
| ‘O’) or | inconsistent |     | labeling | of the | same | entity. |     |     |     |     |     |     |
| ------- | ------------ | --- | -------- | ------ | ---- | ------- | --- | --- | --- | --- | --- | --- |
thesameuniquemaskingsymbol.Finally,thede-
Consequently, even with high token-level micro identifiedcourtjudgmentdocumentisprovided.
| F1 scores, | a single | misplaced |     | boundary | degrades |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
theEntity-levelMicroF1score.
|     |     |     |     |     |     |     | 5 Experiments |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
Toaddressthisissue,weaddaConditionalRan-
|     |     |     |     |     |     |     | 5.1 ExperimentSetting |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
domField(CRF)layer(Zhengetal.,2015)ontop
of the final hidden layer. CRF learns not only the Dataset. We use our PII dataset described in sec-
classificationprobabilityofeachtokenbutalsothe tion4.1fortrainingandtest.Toensureafaireval-
transitionprobabilitybetweenadjacentlabels,en- uation and prevent data leakage for the Thunder-
suringtheconsistencyoftheentiresequence.Fur- DeID dataset which is performed augmentation,
thermore,byemployingglobaldecodingusingthe we split the dataset based on the unique identi-
Viterbialgorithm,weexcludelogicallyimpossible fiers of the original source sentences. The dataset
label sequences in the BIO tagging scheme (e.g., isdividedinto70%train,20%validation,and10%
| ‘B-name’ | followed | by  | ‘I-address’), |     | reducing | er- | test. |     |     |     |     |     |
| -------- | -------- | --- | ------------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- |
rorssuchasincorrectboundaries(‘O’followedby ModelsandBaselines.Wefine-tunefivemodels,
‘I-’tag)andinconsistentlabeling.Asaresult,the KLUEBERT (baseline), KLUEBERT-CRF, with
2313

|     |     |     | #of | Token |     | Token | Entity | Entity |     | Overlap | Intermediate |
| --- | --- | --- | --- | ----- | --- | ----- | ------ | ------ | --- | ------- | ------------ |
Model
|              |     | parameters |      | BinaryF1 |     | MicroF1 | BinaryF1 | MicroF1 |     | F1     | F1     |
| ------------ | --- | ---------- | ---- | -------- | --- | ------- | -------- | ------- | --- | ------ | ------ |
| KLUEBERT     |     |            | 110M | 0.9942   |     | 0.9906  | 0.9509   | 0.9451  |     | 0.9753 | 0.9739 |
| Kanana-1.5   |     |            | 2.1B | 0.5354   |     | 0.2889  | 0.4504   | 0.2495  |     | 0.3148 | 0.3112 |
| Qwen-2.5     |     |            | 1.5B | 0.6931   |     | 0.5863  | 0.5425   | 0.5233  |     | 0.6531 | 0.6074 |
| Thunder-DeID |     |            | 360M | 0.9970   |     | 0.9929  | 0.9614   | 0.9608  |     | 0.9850 | 0.9844 |
KLUEBERT-CRF(Ours) 110M 0.9989 0.9988 0.9925 0.9923 0.9952 0.9951
Table 1: Performance comparison on the combined dataset (3 Datasets). Our model, KLUEBERT-CRF, demon-
stratessuperiorperformanceacrossallmetrics.
110M parameters, Kanana-1.5-2.1b (Team et al., The token-level F1 scores demonstrate that in-
2025), a bilingual LLM, Qwen-2.5-1.5b (Team, corporatingaCRFlayerstructuretoKLUEBERT
2024), a multilingual LLM, and the Thunder- and expanding the tokenizer with legal domain-
DeID (Hahm et al., 2025), encoder-only model specific vocabulary improves PII token classifica-
initiallyfine-tunedthroughThunder-DeIDdataset. tion performance relative to the baseline KLUE-
Formoredetails,pleaserefertoAppendixI. BERT model. Furthermore, examining the entity-
Evaluation Metrics. We use six metrics to eval- level, overlap, and intermediate F1 scores reveals
uate the performance of the models includ- that clearly distinguishing each PII entity and
ing token-level binary F1, token-level micro F1, identifying boundaries between entities demon-
entity-levelbinaryF1,entity-levelmicroF1(same stratesimprovedperformance.
| as strict | F1) (Dernoncourt | et  | al., 2017; | Takahashi |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
et al., 2022), overlap F1, and intermediate F1 5.3 RobustnesstoUnseenData
(Segura-Bedmaretal.,2013). Wefurtherinvestigatethequalityofourproposed
ThebinaryF1metricsmeasurethemodel’sabil- datasetbyassessingitsabilitytogeneralizetoun-
ity to correctly classify whether tokens or entities seen data. To this end, we evaluated our model,
containPII,withoutconsideringthespecifictypes trained on Court Judgment and SNS datasets (ex-
of PII. In contrast, the micro F1 metrics measure cluding Thunder-DeID), on the Thunder-DeID
|     |     |     |     |     |     | test | set. We compare |     | its performance |     | against the |
| --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | --------------- | --- | ----------- |
themodel’sabilitytocorrectlyclassifythespecific
typesofPIIthattokensorentitiesrepresent. Thunder-DeID model, which serves as a refer-
Thesemetricsareappliedatboththetokenand encebenchmarkforexpectedperformancehaving
entity levels. In the case of entity-level F1 met- been trained on its native Thunder-DeID dataset.
rics,themicroF1deemsapredictioncorrectonly Achieving performance comparable to this native
when both the exact boundary span and the spe- baseline demonstrates that the diversity and qual-
cific entity type match the ground truth, whereas ityofourdatasetenablemodelstoberobusteven
onspecialized,previouslyunseenlegaltexts.
| the binary | F1 evaluates | whether | the | exact | bound- |     |     |     |     |     |     |
| ---------- | ------------ | ------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- |
aryspanmatchesandtheentityiscorrectlyclassi- Table 2 presents the performance degradation
| fiedasPII. |     |     |     |     |     | when | tested on | Thunder | test | dataset. | This perfor- |
| ---------- | --- | --- | --- | --- | --- | ---- | --------- | ------- | ---- | -------- | ------------ |
TheoverlapF1considersamatchvalidifthere mance gap is natural as the baseline (Thunder-
is any boundary overlap with a ground-truth en- DeID)wastrainedonitsdataset.Furthermore,this
tityofthesametype,whereastheintermediateF1 gap is also attributable to the interpretations and
requiresatleast50%tokenoverlapforamatch. applicationsofthemaskingguidelines.Whileboth
|     |     |     |     |     |     | our | method and | the Thunder-DeID |     |     | aim to follow |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --- | --- | ------------- |
5.2 MainResult the official guidelines3, our approach employs a
Table 1 shows the performance of our models different annotation scheme and data processing
compared to other three models, KLUEBERT, methodology. Despite these constraints, the fact
Thunder-DeID (360M), Kanana-1.5, and Qwen- thatourmodelmaintainsperformancecomparable
2.5. We train each model on a combined training to the native baseline validates the robustness and
set consisting of three datasets and evaluate them generalization capability of our proposed dataset
onunseendata.Ascoreof‘-’indicatesavalueless
| on a test   | set that also | includes  | all          | three | datasets. |     |     |     |     |     |     |
| ----------- | ------------- | --------- | ------------ | ----- | --------- | --- | --- | --- | --- | --- | --- |
| The results | show that     | our model | consistently |       | out-      |     |     |     |     |     |     |
3SupremeCourtTrialRegulationNo.1778revisedonAu-
| performstheothermodelsinallmetricsweused. |     |     |     |     |     | gust9,2021. |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
2314

OnlyThunder-DeIDDataset
Model
|              |     |     | #of        |          | Token | Token   | Entity   |         | Entity | Overlap |     | Intermediate |
| ------------ | --- | --- | ---------- | -------- | ----- | ------- | -------- | ------- | ------ | ------- | --- | ------------ |
|              |     |     | parameters | BinaryF1 |       | MicroF1 | BinaryF1 | MicroF1 |        | F1      |     | F1           |
| Thunder-DeID |     |     | 360M       |          |       | 0.9223  | -        |         | -      | 0.3682  |     | 0.3682       |
0.9472
KLUEBERT-CRF(Ours) 110M 0.9268 0.9299 0.4201 0.3658 0.4484 0.4421
Table2:PerformanceofourmodelsontheThunder-DeIDtestsetafterbeingtrainedexclusivelyonourproposed
dataset.Theperformancedropisduetothedifferingmaskingguidelinesbetweenthetwodatasets.
|     |     |     | #of |     | Token | Token | Entity |     | Entity | Overlap |     | Intermediate |
| --- | --- | --- | --- | --- | ----- | ----- | ------ | --- | ------ | ------- | --- | ------------ |
Model
|              |     |     | parameters | BinaryF1 |        | MicroF1 | BinaryF1 | MicroF1 |        | F1     |     | F1     |
| ------------ | --- | --- | ---------- | -------- | ------ | ------- | -------- | ------- | ------ | ------ | --- | ------ |
| KLUEBERT     |     |     | 110M       |          | 0.9916 | 0.9861  | 0.9509   |         | 0.9451 | 0.9753 |     | 0.9739 |
| Kanana-1.5   |     |     | 2.1B       |          | 0.2870 | 0.0803  | 0.0556   |         | 0.0192 | 0.1436 |     | 0.1432 |
| Qwen-2.5     |     |     | 1.5B       |          | 0.4826 | 0.3328  | 0.2636   |         | 0.1997 | 0.4020 |     | 0.3900 |
| Thunder-DeID |     |     | 360M       |          | 0.9982 | 0.9979  | 0.9052   |         | 0.8934 | 0.9062 |     | 0.9044 |
KLUEBERT-CRF(Ours) 110M 0.9998 0.9997 0.9935 0.9928 0.9946 0.9946
Table3:PerformancecomparisonontheThunder-DeIDdatasetonly.Ourmodelshowsrobustperformance,out-
performingtheoriginalThunder-DeIDmodelonitsowndata.
| than0.01,duetolowentityrecognitioncapability. |     |     |     |     |     | 6   | Discussion |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
5.4 ComparativeAnalysis A key contribution of our work is the introduc-
|            |                    |     |        |         |         | tion      | of a high-quality |     | benchmark |          | dataset, | which      |
| ---------- | ------------------ | --- | ------ | ------- | ------- | --------- | ----------------- | --- | --------- | -------- | -------- | ---------- |
| To further | analyze            | the | impact | of our  | diverse |           |                   |     |           |          |          |            |
|            |                    |     |        |         |         | addresses | a critical        |     | data      | scarcity | issue    | in the Ko- |
| dataset    | and to demonstrate |     | the    | model’s | gener-  |           |                   |     |           |          |          |            |
reanlegaltechlandscape.Byenablingresearchers
| alization     | capability, | we          | train our   | KLUEBERT- |     |                   |               |           |         |             |          |           |
| ------------- | ----------- | ----------- | ----------- | --------- | --- | ----------------- | ------------- | --------- | ------- | ----------- | -------- | --------- |
|               |             |             |             |           |     | and               | practitioners | to        | develop | and         | validate | robust    |
| CRF model     | on          | the full    | combined    | dataset,  |     | and               |               |           |         |             |          |           |
|               |             |             |             |           |     | de-identification |               | models,   |         | our dataset | can      | help au-  |
| then evaluate | the         | performance | exclusively |           | on  | the               |               |           |         |             |          |           |
|               |             |             |             |           |     | tomate            | a process     | currently |         | dominated   |          | by manual |
Thunder-DeIDtestdataset.Afterthat,wecompare
|            |               |     |                 |     |      | labor. | This automation     |     | is  | necessary | for        | increasing |
| ---------- | ------------- | --- | --------------- | --- | ---- | ------ | ------------------- | --- | --- | --------- | ---------- | ---------- |
| it against | other models. |     | More individual |     | test | re-    |                     |     |     |           |            |            |
|            |               |     |                 |     |      | the    | public availability |     | of  | court     | judgments, | which      |
sultsareinAppendixD.
willenhancejudicialtransparency.
| As shown | in Table      | 3,  | our model, | when     | trained |      |     |     |     |     |     |     |
| -------- | ------------- | --- | ---------- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- |
| on the   | comprehensive |     | combined   | dataset, |         | sig- |     |     |     |     |     |     |
7 Conclusion
| nificantly | outperforms |     | the native | Thunder-DeID |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
model on its own test data. This result demon- In this paper, we propose a BERT-based frame-
strates two key points. First, it confirms that the work to address the challenge of automated de-
identificationforKoreancourtjudgments,balanc-
| performance | drop | observed | in the | robustness |     | test |     |     |     |     |     |     |
| ----------- | ---- | -------- | ------ | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- |
was indeed due to the domain shift and differing ing judicial transparency with privacy protection.
annotation schemes, not a fundamental limitation Ourprimarycontributionisthecreationofalarge-
|                 |         |     |               |     |         | scale | PII dataset | of  | approximately |     | one | million in- |
| --------------- | ------- | --- | ------------- | --- | ------- | ----- | ----------- | --- | ------------- | --- | --- | ----------- |
| of our dataset. | Second, |     | it highlights | the | benefit | of    |             |     |               |     |     |             |
trainingonamorediverseandlarger-scaledataset. stances, constructed by combining a new, com-
Byincorporatingdatafromvariouslegalfieldsand prehensive Korean legal document dataset with
conversational contexts, our model learns a more SNS conversation dataset and the Thunder-DeID
dataset.Thelegaldataset,spanning39legalfields,
| generalized | representation |     | of PII, | enabling |     | it to |     |     |     |     |     |     |
| ----------- | -------------- | --- | ------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- |
achievesuperiorperformanceevenonspecialized, demonstrates high quality and reliability, vali-
narrowlyfocuseddatasets. dated by a Fleiss’ Kappa score of 0.7352 for
IAA.Experimentalresultsshowthatourproposed
5.5 QualitativeAnalysis KLUEBERT-CRF model, trained on this diverse
The confusion matrices in Appendix C demon- dataset,achievesstate-of-the-artperformance,set-
strate the model’s robust classification capabil- tinganewbenchmarkforde-identificationforKo-
ities, indicating consistent accuracy across all reanlegaldocuments.
datasetswithminimalinter-classconfusion.
2315

| Limitations |     |     |     |     |     |     | References                |     |     |                       |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --------------------- | --- | --- | --- |
|             |     |     |     |     |     |     | CourtAdministration.2019. |     |     | Nationalassemblyofko- |     |     |     |
SupremeCourtRegulation
rea.
AccordingtoSupremeCourtregulations,wecan-
|            |     |          |      |                  |     |           | Court Administration. |           | 2025.     | National |        | court | adminis- |
| ---------- | --- | -------- | ---- | ---------------- | --- | --------- | --------------------- | --------- | --------- | -------- | ------ | ----- | -------- |
| not access | the | original |      | (non-anonymized) |     | court     |                       |           |           |          |        |       |          |
|            |     |          |      |                  |     |           | tration               | of korea. | Technical |          | Report | ISP-, | Court of |
| judgments. | To  | address  | this | limitation,      |     | human an- | Korea,Seoul.          |           |           |          |        |       |          |
notatorsprocessedanonymizedcourtjudgmentby
annotatingPIIentitiesandinsertingsyntheticdata Sergei Bogdanov, Alexandre Constantin, Timothée
|     |     |     |     |     |     |     | Bernard, | Benoit | Crabbé, | and | Etienne | P   | Bernard. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | --- | ------- | --- | -------- |
intothemaskedplaceholdersbyoursyntheticdata
|     |     |     |     |     |     |     | 2024. | Nuner: | Entity | recognition |     | encoder | pre- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ------ | ----------- | --- | ------- | ---- |
generator.However,thissyntheticdatacannotper-
|     |     |     |     |     |     |     | training | via llm-annotated |     | data. | In  | Proceedings | of  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | ----- | --- | ----------- | --- |
fectly replicate the characteristics of actual origi- the2024ConferenceonEmpiricalMethodsinNat-
nal court judgments. Furthermore, without access uralLanguageProcessing,pages11829–11841.
| to the original  |     | court       | judgments, |     | we cannot  | con-     |                     |            |       |                   |      |       |         |
| ---------------- | --- | ----------- | ---------- | --- | ---------- | -------- | ------------------- | ---------- | ----- | ----------------- | ---- | ----- | ------- |
|                  |     |             |            |     |            |          | Franck Dernoncourt, |            | Ji    | Young             | Lee, | Ozlem | Uzuner, |
| duct comparative |     | experiments |            |     | to analyze | the dif- |                     |            |       |                   |      |       |         |
|                  |     |             |            |     |            |          | and Peter           | Szolovits. | 2017. | De-identification |      |       | of pa-  |
ferences between the original and our processed tient notes with recurrent neural networks. Journal
|                  |            |     |              |     |                |              | of the         | American | Medical      | Informatics |          | Association, |       |
| ---------------- | ---------- | --- | ------------ | --- | -------------- | ------------ | -------------- | -------- | ------------ | ----------- | -------- | ------------ | ----- |
| court judgments. |            | To  | minimize     |     | these          | limitations, |                |          |              |             |          |              |       |
| we plan          | to analyze |     | dependencies |     | between        | PII en-      | 24(3):596–606. |          |              |             |          |              |       |
| tities and       | refine     | our | synthetic    |     | data generator | to           |                |          |              |             |          |              |       |
|                  |            |     |              |     |                |              | Vipin Gupta,   | Ian      | C MacMillan, |             | and Gita | Surie.       | 2004. |
achievegreaterprecision. Entrepreneurialleadership:developingandmeasur-
|     |     |     |     |     |     |     | ing a cross-cultural |     | construct. |     | Journal | of  | business |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------- | --- | ------- | --- | -------- |
venturing,19(2):241–260.
GeneralizabilityandResourcesAdaptation.
| While the | proposed |     | data | processing | pipeline | and |         |       |        |               |     |      |        |
| --------- | -------- | --- | ---- | ---------- | -------- | --- | ------- | ----- | ------ | ------------- | --- | ---- | ------ |
|           |          |     |      |            |          |     | Sungeun | Hahm, | Heejin | Kim, Gyuseong |     | Lee, | Hyunji |
model architecture are fundamentally language- Park,andJaejinLee.2025. Thunder-deid:Accurate
andefficientde-identificationframeworkforkorean
| agnostic, | the | current | implementation |     |     | utilizes re- |                 |     |                                |     |     |     |     |
| --------- | --- | ------- | -------------- | --- | --- | ------------ | --------------- | --- | ------------------------------ | --- | --- | --- | --- |
|           |     |         |                |     |     |              | courtjudgments. |     | arXivpreprintarXiv:2506.15266. |     |     |     |     |
sourcesspecializedfortheKoreanlanguage,such
as KSS for sentence segmentation and KLUE- J Richard Landis and Gary G Koch. 1977. The mea-
BERT for embedding. Therefore, extending this surementofobserveragreementforcategoricaldata.
biometrics,pages159–174.
| framework  | to      | other | languages        |     | does | not require |                |     |                |     |       |          |     |
| ---------- | ------- | ----- | ---------------- | --- | ---- | ----------- | -------------- | --- | -------------- | --- | ----- | -------- | --- |
| structural | changes |       | but necessitates |     | the  | substitu-   |                |     |                |     |       |          |     |
|            |         |       |                  |     |      |             | Stefan Larson, |     | Nicole Cornehl |     | Lima, | Santiago | Pe- |
tion of these language-specific components with droza Diaz, Amogh Manoj Joshi, Siddharth Betala,
|            |       |          |     |         |        |           | Jamiu | Tunde | Suleiman, | Yash | Mathur, | Kaushal | Ku- |
| ---------- | ----- | -------- | --- | ------- | ------ | --------- | ----- | ----- | --------- | ---- | ------- | ------- | --- |
| equivalent | tools | suitable |     | for the | target | language. |       |       |           |      |         |         |     |
Forexample,itispossibletoreplacetoolslikethe mar Prajapati, Ramla Alakraa, Junjie Shen, and 1
|        |          |           |     |       |      |           | others.2024. |          | De-identificationofsensitivepersonal |      |           |             |     |
| ------ | -------- | --------- | --- | ----- | ---- | --------- | ------------ | -------- | ------------------------------------ | ---- | --------- | ----------- | --- |
| Korean | sentence | segmenter |     | (KSS) | with | multilin- |              |          |                                      |      |           |             |     |
|        |          |           |     |       |      |           | data in      | datasets | derived                              | from | iit-cdip. | In Proceed- |     |
gual tools (e.g., spaCy, NLTK) and swap KLUE- ings of the 2024 Conference on Empirical Meth-
odsinNaturalLanguageProcessing,pages21494–
| BERT    | with   | language-specific |     |        | encoders       | suitable |        |     |     |     |     |     |     |
| ------- | ------ | ----------------- | --- | ------ | -------------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
| for the | target | language          |     | (e.g., | UmBERTo(Parisi |          | 21505. |     |     |     |     |     |     |
etal.,2020)forItalian,RoBERTa(Liuetal.,2019)
|     |     |     |     |     |     |     | Jinhyuk | Lee, | Wonjin | Yoon, | Sungdong |     | Kim, |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------ | ----- | -------- | --- | ---- |
forEnglish,CamemBERT(Martinetal.,2020)for Donghyeon Kim, Sunkyu Kim, Chan Ho So, and
| French). |     |     |     |     |     |     | JaewooKang.2020. |     | Biobert:apre-trainedbiomed-     |     |       |                |     |
| -------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------------- | --- | ----- | -------------- | --- |
|          |     |     |     |     |     |     | ical language    |     | representation                  |     | model | for biomedical |     |
|          |     |     |     |     |     |     | textmining.      |     | Bioinformatics,36(4):1234–1240. |     |       |                |     |
Acknowledgments
YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
This work was supported in part by the Institute dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
of Information & Communications Technology Luke Zettlemoyer, and Veselin Stoyanov. 2019.
|          |              |                               |            |     |          |            | Roberta:      | A robustly                     | optimized |         | bert  | pretraining | ap-     |
| -------- | ------------ | ----------------------------- | ---------- | --- | -------- | ---------- | ------------- | ------------------------------ | --------- | ------- | ----- | ----------- | ------- |
| Planning | & Evaluation |                               | (IITP)-ICT |     | Creative | Con-       |               |                                |           |         |       |             |         |
|          |              |                               |            |     |          |            | proach.       | arXivpreprintarXiv:1907.11692. |           |         |       |             |         |
| silience | Program      | grant                         | funded     |     | by the   | Korea gov- |               |                                |           |         |       |             |         |
| ernment  | (MSIT)       | (IITP-2025-RS-2020-II201819); |            |     |          |            |               |                                |           |         |       |             |         |
|          |              |                               |            |     |          |            | Louis Martin, | Benjamin                       |           | Muller, | Pedro | Ortiz       | Suarez, |
and in part by the Basic Science Research Pro- Yoann Dupont, Laurent Romary, Éric Villemonte
|              |       |              |     |              |     |            | de La | Clergerie, | Djamé | Seddah,      | and      | Benoît | Sagot. |
| ------------ | ----- | ------------ | --- | ------------ | --- | ---------- | ----- | ---------- | ----- | ------------ | -------- | ------ | ------ |
| gram through |       | the National |     | Research     |     | Foundation |       |            |       |              |          |        |        |
|              |       |              |     |              |     |            | 2020. | Camembert: | a     | tasty french | language |        | model. |
| of Korea     | (NRF) | funded       | by  | the Ministry |     | of Educa-  |       |            |       |              |          |        |        |
InProceedingsofthe58thannualmeetingoftheas-
tion(RS-2021-NR060143)
sociationforcomputationallinguistics,pages7203–
7219.
2316

Stephen Mayhew, Terra Blevins, Shuheng Liu, Marek Kanana LLM Team and 1 others. 2025. Kanana:
Šuppa,HilaGonen,JosephMarvinImperial,BörjeF Compute-efficientbilinguallanguagemodels. arXiv
preprintarXiv:2502.18934.
Karlsson,PeiqinLin,NikolaLjubešic´,LesterJames
| Miranda, | and 1 | others. | 2024. | Universal |     | ner: A |            |       |          |         |     |            |
| -------- | ----- | ------- | ----- | --------- | --- | ------ | ---------- | ----- | -------- | ------- | --- | ---------- |
|          |       |         |       |           |     |        | Qwen Team. | 2024. | Qwen2.5: | A party | of  | foundation |
gold-standardmultilingualnamedentityrecognition
models.
| benchmark. | In        | Proceedings | of      | the 2024 | Confer- |       |             |     |         |             |     |         |
| ---------- | --------- | ----------- | ------- | -------- | ------- | ----- | ----------- | --- | ------- | ----------- | --- | ------- |
| ence of    | the North | American    | Chapter |          | of the  | Asso- |             |     |         |             |     |         |
|            |           |             |         |          |         |       | Shuhe Wang, |     | Xiaofei | Sun, Xiaoya | Li, | Rongbin |
ciationforComputationalLinguistics:HumanLan-
|     |     |     |     |     |     |     | Ouyang, | Fei | Wu, Tianwei | Zhang, | Jiwei | Li, Guoyin |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ------ | ----- | ---------- |
guageTechnologies(Volume1:LongPapers),pages
|     |     |     |     |     |     |     | Wang, | and Chen | Guo. | 2025. Gpt-ner: |     | Named en- |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---- | -------------- | --- | --------- |
4322–4337.
|     |     |     |     |     |     |     | tityrecognitionvialargelanguagemodels. |     |     |     |     | InFind- |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ------- |
ingsoftheassociationforcomputationallinguistics:
| Loreto Parisi, | Simone | Francia, | and | Paolo | Magnani. |     |     |     |     |     |     |     |
| -------------- | ------ | -------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
NAACL2025,pages4257–4275.
| 2020. Umberto:        |     | an italian | language            | model |     | trained |              |     |        |             |     |            |
| --------------------- | --- | ---------- | ------------------- | ----- | --- | ------- | ------------ | --- | ------ | ----------- | --- | ---------- |
| withwholewordmasking. |     |            | https://github.com/ |       |     |         |              |     |        |             |     |            |
|                       |     |            |                     |       |     |         | Shuai Zheng, |     | Sadeep | Jayasumana, |     | Bernardino |
musixmatchresearch/umberto.
|     |     |     |     |     |     |     | Romera-Paredes, |     | Vibhav       | Vineet, | Zhizhong | Su,         |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | ------- | -------- | ----------- |
|     |     |     |     |     |     |     | Dalong          | Du, | Chang Huang, | and     | Philip   | H. S. Torr. |
SungjoonPark,JihyungMoon,SungdongKim,WonIk
|     |     |     |     |     |     |     | 2015. | Conditionalrandomfieldsasrecurrentneural |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------------------------------------- | --- | --- | --- | --- |
Cho,JiyoonHan,JangwonPark,ChisungSong,Jun-
|            |          |     |               |     |     |       | networks. | In  | 2015 IEEE | International |     | Conference |
| ---------- | -------- | --- | ------------- | --- | --- | ----- | --------- | --- | --------- | ------------- | --- | ---------- |
| seong Kim, | Yongsook |     | Song, Taehwan |     | Oh, | and 1 |           |     |           |               |     |            |
onComputerVision(ICCV).IEEE.
| others.2021.   | Klue:Koreanlanguageunderstanding |        |     |        |            |     |     |     |     |     |     |     |
| -------------- | -------------------------------- | ------ | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| evaluation.    | arXivpreprintarXiv:2105.09680.   |        |     |        |            |     |     |     |     |     |     |     |
| Maksim Savkin, | Timur                            | Ionov, | and | Vasily | Konovalov. |     |     |     |     |     |     |     |
2025. Spy:Enhancingprivacywithsyntheticpiide-
| tection | dataset.       | In Proceedings |              | of the | 2025    | Con- |     |     |     |     |     |     |
| ------- | -------------- | -------------- | ------------ | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- |
| ference | of the Nations | of             | the Americas |        | Chapter | of   |     |     |     |     |     |     |
theAssociationforComputationalLinguistics:Hu-
manLanguageTechnologies(Volume4:StudentRe-
searchWorkshop),pages236–246.
| Isabel Segura-Bedmar, |       | Paloma       | Martínez, |      | and        | María |     |     |     |     |     |     |
| --------------------- | ----- | ------------ | --------- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| Herrero-Zazo.         | 2013. | Semeval-2013 |           | task | 9: Extrac- |       |     |     |     |     |     |     |
tionofdrug-druginteractionsfrombiomedicaltexts
| (ddiextraction | 2013). | In            | Second | Joint     | Conference |       |     |     |     |     |     |     |
| -------------- | ------ | ------------- | ------ | --------- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| on Lexical     | and    | Computational |        | Semantics | (*         | SEM), |     |     |     |     |     |     |
Volume2:ProceedingsoftheSeventhInternational
WorkshoponSemanticEvaluation(SemEval2013),
pages341–350.
| Rico Sennrich, | Barry | Haddow, | and | Alexandra |     | Birch. |     |     |     |     |     |     |
| -------------- | ----- | ------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
2015. Neuralmachinetranslationofrarewordswith
| subwordunits.   |        | arXivpreprintarXiv:1508.07909. |           |     |     |         |     |     |     |     |     |     |
| --------------- | ------ | ------------------------------ | --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
| Charles Sutton, | Andrew |                                | McCallum, | and | 1   | others. |     |     |     |     |     |     |
2012. Anintroductiontoconditionalrandomfields.
| Foundations | and | Trends® | in  | Machine | Learning, |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
4(4):267–373.
| Latanya Sweeney. |           | 2002.         | k-anonymity:    |         | A model  | for    |     |     |     |     |     |     |
| ---------------- | --------- | ------------- | --------------- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
| protecting       | privacy.  | International |                 | journal |          | of un- |     |     |     |     |     |     |
| certainty,       | fuzziness | and           | knowledge-based |         | systems, |        |     |     |     |     |     |     |
10(05):557–570.
MariaIrenaSzawerna,SimonDobnik,RicardoMuñoz
Sánchez,ThereseLindströmTiedemann,andElena
| Volodina.                        | 2024. | Detecting        | personal | identifiable  |     | in- |     |     |     |     |     |     |
| -------------------------------- | ----- | ---------------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| formationinswedishlearneressays. |       |                  |          | InProceedings |     |     |     |     |     |     |     |     |
| of the Workshop                  |       | on Computational |          | Approaches    |     | to  |     |     |     |     |     |     |
| Language                         | Data  | Pseudonymization |          | (CALD-pseudo  |     |     |     |     |     |     |     |     |
2024),pages54–63.
KanaeTakahashi,KoujiYamamoto,AyaKuchiba,and
| Tatsuki        | Koyama. | 2022.   | Confidence     |     | interval | for     |     |     |     |     |     |     |
| -------------- | ------- | ------- | -------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
| micro-averaged |         | f 1 and | macro-averaged |     | f 1      | scores. |     |     |     |     |     |     |
AppliedIntelligence,52(5):4961–4972.
2317

|     | Appendix |     |     |     | A.2 ExampleofPromptResponseon |     |     |     |     |
| --- | -------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
GPT-4o-mini
{
A PromptonCategorySpecialization
"id":"batch_req_68354c936464-8190bba6-
40c370e198e2",
| A.1 SchemeofPromptonGPT-4o-mini |     |     |     |     | "custom_id":"request-18", |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
"response":{
(a)OriginalPrompt(Korean)
...
| {                |     |     |      |     | "body":{ |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | -------- | --- | --- | --- | --- |
| "role":"system", |     |     |      |     | ...      |     |     |     |     |
| "content":       | "너는 | 주어진 | 대화에서 | 마   |          |     |     |     |     |
"choices":[{
| 스킹된 위치의 | 가명정보 | 문자열을 | 생성하 |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
"index":0,
| 는 AI assistant야. | 마스킹된 | 원래    | 단어는 | 구   | "message":{ |     |     |     |     |
| ---------------- | ---- | ----- | --- | --- | ----------- | --- | --- | --- | --- |
| 체적인 정보입니다.       |      | 전체 대화 | 맥락을 | 고려  |             |     |     |     |     |
"role":"assistant",
하여자연스러운가명정보를단일단어로생
"content":"'department'",
| 성하세요." |     |     |     |     | "refusal":null, |     |     |     |     |
| ------ | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
| },     |     |     |     |     | },              |     |     |     |     |
{
...
"role":"user",
}],
| "content": |     |     |     |     | ... |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
"T1:카드사에전화를해봐
}
T1:지금
},
| T2:홈페이지에적혀있었어요 |     |     |     |     | "error":null |     |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
T2:영업점직접방문
}
T3:저나해봐
| T3:안풀린건지 |     |     |     |     | B PromptonKanana-1.5 |     |     |     |     |
| -------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
T4:고객번호.#@소속#"
| }   |     |     |     |     | B.1 SchemeofPromptonKanana-1.5 |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
(a)OriginalPrompt(Korean)
(b)TranslatedPrompt(English)
|     |     |     |     |     | ### | 지시: | 주어진 문장에서 |     | 모든 개인 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- |
{
|     |     |     |     |     | 식별 정보(PII)를 |     | 찾아서, | 각 PII의 | 종류, |
| --- | --- | --- | --- | --- | ----------- | --- | ---- | ------ | --- |
"role":"system",
|     |     |     |     |     | 시작 인덱스, |     | 끝 인덱스를 | JSON | 형식으로 |
| --- | --- | --- | --- | --- | ------- | --- | ------ | ---- | ---- |
"content":"YouareanAIassistantthatgene-
추출하세요.
ratespseudonymizedinformationstringsfor
maskedpositionsinagivenconversation.
###입력:
| Theoriginalmaskedwordsrepresentspecific |     |     |     |     |     | {}  |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
information.Generatethepseudonymized
###답변:
| informationasanaturalsingleword, |     |     |     |     |     | {}  |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consideringtheentireconversationcontext." (b)TranslatedPrompt(English)
| },             |     |     |     |     | ### Instruction:      |      | Find        | all personally | identi-    |
| -------------- | --- | --- | --- | --- | --------------------- | ---- | ----------- | -------------- | ---------- |
| {              |     |     |     |     | fiable information    |      | (PII)       | in the given   | sentence   |
| "role":"user", |     |     |     |     | and extract           | each | PII’s type, | start          | index, and |
| "content":     |     |     |     |     | endindexinJSONformat. |      |             |                |            |
"T1:Callthecreditcardcompany.
| T1:Now |     |     |     |     | ###Input: |     |     |     |     |
| ------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
{}
T2:Itwaswrittenonthewebsite.
| T2:Visitabranchinperson |     |     |     |     | ###Response: |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
{}
T3:Givethemacall
T3:Tocheckwhetherthesuspensionhas B.2 ExampleofPromptResponseon
| beenliftedyet.                    |     |     |     |     | Kanana-1.5                |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
| T4:CustomerNumber.#@affiliation#" |     |     |     |     | (a)OriginalPrompt(Korean) |     |     |     |     |
}
2318

| ###    | 지시:      | 주어진 | 문장에서 |      | 모든   | 개인  |                          |             |                |                |
| ------ | -------- | --- | ---- | ---- | ---- | --- | ------------------------ | ----------- | -------------- | -------------- |
| 식별     | 정보(PII)를 |     | 찾아서, | 각    | PII의 | 종류, |                          |             |                |                |
| 시작     | 인덱스,     | 끝   | 인덱스를 | JSON | 형식으로 |     |                          |             |                |                |
| 추출하세요. |          |     |      |      |      |     |                          |             |                |     
    |
|        |          |     |      |      |      |     |  O B N F          |         |           |                |
    
   
|     |     |     |     |     |     |     |  T D I P P M         |         |           |    
    |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | ----------- | -------------- | ------------ |
   
   
   
   
### 입력: 공소사실의 요지. 피고인은  D P N Q B O Z                             
   
   
| 경기도               | 이천시 | 부발읍 |     | 10에서 | ’주식회사더 |     |                        |                       |                |                   |
| ----------------- | --- | --- | --- | ---- | ------ | --- | ---------------------- | --------------------- | -------------- | ----------------- |
|                   |     |     |     |      |        |     |  B E E S F T T       |              |           |   
           |
| 블에스메디칼’을운영하는사람이다. |     |     |     |      |        |     |  Q  I P  O  F          |                       |                |                   |
|                   |     |     |     |      |        |     |  O V  N  C  F  S     |                |           |                   |
|                   |     |     |     |      |        |     |  M F C B -  F V S 5   |                       |                |   
           |
|                   |     |     |     |      |        |     |  6 3 -               |               |           |      $ P V O U |
### 답변: [ "label": address, "start":  B  O  D  V  D  N  P V  C  O  F  U  S                         
|     |     | {   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
23, "end": 29 , "label": company, "start":  C B O L                        
} {
| 33,"end":44 |     | ]   |     |     |     |     |  T F D V S J U Z |             |                    |     |
| ----------- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ------------------ | --- |
|             |     |     |     |     |     |     |  D P E F       |         |             |     |
}
|     |     |     |     |     |     |     |  F  N B J M     |         |             |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------- | ------------------ | --- |
(b)TranslatedPrompt(English)
|     |     |     |     |     |     |     |  * %                               |                                 |                                             |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ----------------------------------- | --------------------------------------------------- | --- |
|     |     |     |     |     |     |     |  O B N F  T D I P P M  D P N Q B O Z |  B E E S F T T  P O  F  6 3 -  V O  |  U  C B O L  T F D V  S  J U  Z  F F  N B J M  * % |     |
|     |     |     |     |     |     |     |                                      |  Q  V  I N  C  F S  B D  D  V  P  N |  C  F S  D  P  E                                    |     |
 O  O
 1 S F E J D U F E  - B C F M
| ### | Instruction: |     | Find | all personally |     | identi- |     |     |     |     |
| --- | ------------ | --- | ---- | -------------- | --- | ------- | --- | --- | --- | --- |
(a)Inthecaseoftrainonthreedatasetandtestonthree
| fiable | information |     | (PII) | in the given | sentence |     |     |     |     |     |
| ------ | ----------- | --- | ----- | ------------ | -------- | --- | --- | --- | --- | --- |
dataset.
| and extract |     | each | PII’s type, | start | index, | and |                      |               |                |     |
| ----------- | --- | ---- | ----------- | ----- | ------ | --- | -------------------- | ------------- | -------------- | --- |
|             |     |      |             |       |        |     |  O B N F        |          |           |     |
  
   
endindexinJSONformat.
|       |        |           |     |            |           |         |  T D I P P M         |                   |                 |            |
| ----- | ------ | --------- | --- | ---------- | --------- | ------- | ------------------------ | ----------------------- | -------------------- | ---------- |
|       |        |           |     |            |           |         |  D P N Q B O Z         |                   |                |            |
| ###   | Input: | Summary   |     | of         | the       | Indict- |                          |                         |                      |   
    |
|       |        |           |     |            |           |         |  B E E S F T T       |               |                |         |
| ment. | The    | defendant | is  | the person | operating |         |                          |                         |                      |            |
|       |        |           |     |            |           |         |  Q I P O F             |                     |              |            |
 O V N C F S
| ‘DoubleSMedicalCorporation’at10Bubal- |     |     |     |     |     |     |  M F C B -  F V S 5 |             |                |                   |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | -------------- | ----------------- |
|                                       |     |     |     |     |     |     |  6 3 -             |         |           |      $ P V O U |
eup,Icheon-si,Gyeonggi-do.
|     |           |     |            |          |     |          |  B D D P V O U  O V N C F S     |         |           |     |
| --- | --------- | --- | ---------- | -------- | --- | -------- | --------------------------------- | ----------- | -------------- | --- |
|     |           |     |            |          |     |          |  C B O L                        |         |           |     |
| ### | Response: |     | [ "label": | address, |     | "start": |                                   |             |                |     |
|     |           |     | {          |          |     |          |  T F D V S J U Z                  |             |                |     |
23, "end": 29 , "label": company, "start":  D P E F                        
|             |     | }   | {   |     |     |     |  F  N B J M                       |                           |                                            |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ----------------------------- | ----------------------------------------------- | --- |
| 33,"end":44 |     | ]   |     |     |     |     |                                      |                               |                                                 |     |
|             |     | }   |     |     |     |     |  * %                               |                           |                                            |     |
|             |     |     |     |     |     |     |  O B N F  T D I P P M  D P N Q B O Z |  B E E S F T T  P O  F  6 3 - |  V O  U  C B O L  S  J U  Z  F F  N B J M  * % |     |
|             |     |     |     |     |     |     |                                      |  Q  I  N  C  F S  B D  D  P   |  N  C  F S  T F D V  D  P  E                    |     |
 O  V  O  V
| C QualitativeAnalysis |     |     |     |     |     |     |     |  1 S F E J D U F E  - B C F M |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- |
(b)Inthecaseoftrainontwodatasetandtestonthe
leftdataset(Thunder-DeID).
| Confusion | matrix |     | of KLUEBERT-CRF |     |     | on the |     |     |     |     |
| --------- | ------ | --- | --------------- | --- | --- | ------ | --- | --- | --- | --- |
   
   
main result, the robustness result and the abla-  O B N F                              
   
|            |         |     |      |         |      |           |  T D I P P M       |         |           |    
    |
| ---------- | ------- | --- | ---- | ------- | ---- | --------- | ---------------------- | ----------- | -------------- | ------------ |
| tion study | result. | The | main | results | were | tested on |                        |             |                |              |
  
   
a mixed dataset comprising all three datasets for  D P N Q B O Z                          
boththetrainandtestdatasets.Therobustnessre-  B E E S F T T                          
  
   
 Q I P O F
sults were tested on a mixed dataset of the two  O V N C F S                             
 M F C B -  F V S 5
datasets excluding the Thunder-DeID Dataset for  6 3 -                          $ P V O U
   
the train dataset, and the Thunder-DeID Dataset  B D D P V O U  O V N C F S                         
forthetestdataset.Theablationstudyresultswere  C B O L                        
 T F D V S J U Z
testedonallthreedatasetsforthetraindatasetand  D P E F                         
theThunder-DeIDDatasetforthetestdataset.  F  N B J M                       
Intheconfusionmatrixforfigure2a,2b,and2c,  * %                        
|     |     |     |     |     |     |     |  O B N F  T D I P P M  D P N Q B O Z |  B E E S F T T  P O  F  6 3 - |  V O  U  C B O L  S  J U  Z  F F  N B J M  * % |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ----------------------------- | ----------------------------------------------- | --- |
respectively,theverticalaxisrepresentstheactual  Q  I  N  C  F S  B D  D  P  N  C  F S  T F D V  D  P  E
 O  V  O  V
 1 S F E J D U F E  - B C F M
| labels, | and the | horizontal | axis | represents |     | the pre- |     |     |     |     |
| ------- | ------- | ---------- | ---- | ---------- | --- | -------- | --- | --- | --- | --- |
(c)Inthecaseoftrainonthreedatasetandtestonthe
| dicted | labels. | Therefore, | the | numbers |     | on the di- |     |     |     |     |
| ------ | ------- | ---------- | --- | ------- | --- | ---------- | --- | --- | --- | --- |
Thunder-DeIDdataset.
agonalindicatecaseswherethepredictionsmatch
Figure2:Perclassanalysis.
theactuallabels,whiletheothernumbersindicate
| cases where  | the  | predictions |            | do not | match | the ac-    |     |     |     |     |
| ------------ | ---- | ----------- | ---------- | ------ | ----- | ---------- | --- | --- | --- | --- |
| tual labels. | This | helps       | to analyze |        | how   | each label |     |     |     |     |
tendstobeincorrectlyclassifiedintootherlabels.
2319

|     |     |     |     | #of | Token |     | Token | Entity |     | Entity | Overlap |     | Intermediate |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ------ | --- | ------ | ------- | --- | ------------ |
Model
|              |     |     | parameters |     | BinaryF1 |     | MicroF1 | BinaryF1 | MicroF1 |        | F1     |     | F1     |
| ------------ | --- | --- | ---------- | --- | -------- | --- | ------- | -------- | ------- | ------ | ------ | --- | ------ |
| KLUEBERT     |     |     | 110M       |     | 0.9946   |     | 0.9924  | 0.8208   |         | 0.8110 | 0.9109 |     | 0.9015 |
| Thunder-DeID |     |     | 360M       |     | 0.9964   |     | 0.9952  | 0.9297   |         | 0.9255 |        |     |        |
|              |     |     |            |     |          |     |         |          |         |        | 0.9561 |     | 0.9552 |
KLUEBERT-CRF(Ours) 110M 0.9981 0.9981 0.9447 0.9438 0.9536 0.9518
Table4:Performancecomparisonontheindividualdataset(CourtJudgementPIIDataset).
|     |     |     |     | #of | Token |     | Token | Entity |     | Entity | Overlap |     | Intermediate |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ------ | --- | ------ | ------- | --- | ------------ |
Model
|              |     |     | parameters |     | BinaryF1 |     | MicroF1 | BinaryF1 | MicroF1 |        | F1     |     | F1     |
| ------------ | --- | --- | ---------- | --- | -------- | --- | ------- | -------- | ------- | ------ | ------ | --- | ------ |
| KLUEBERT     |     |     | 110M       |     | 0.9961   |     | 0.9928  | 0.9813   |         | 0.9810 | 0.9926 |     | 0.9922 |
| Thunder-DeID |     |     | 360M       |     | 0.9964   |     | 0.9871  | 0.9645   |         | 0.9643 | 0.9882 |     | 0.9877 |
KLUEBERT-CRF(Ours) 110M 0.9988 0.9986 0.9945 0.9945 0.9973 0.9972
Table5:Performancecomparisonontheindividualdataset(SNSPIIDataset).
|     |     |     |     | #of | Token |     | Token | Entity |     | Entity | Overlap |     | Intermediate |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ------ | --- | ------ | ------- | --- | ------------ |
Model
|              |     |     | parameters |     | BinaryF1 |     | MicroF1 | BinaryF1 | MicroF1 |        | F1     |     | F1     |
| ------------ | --- | --- | ---------- | --- | -------- | --- | ------- | -------- | ------- | ------ | ------ | --- | ------ |
| KLUEBERT     |     |     | 110M       |     | 0.9916   |     | 0.9861  | 0.8047   |         | 0.7679 | 0.8903 |     | 0.8848 |
| Thunder-DeID |     |     | 360M       |     | 0.9982   |     | 0.9979  | 0.9052   |         | 0.8934 | 0.9062 |     | 0.9044 |
KLUEBERT-CRF(Ours) 110M 0.9998 0.9997 0.9935 0.9928 0.9946 0.9946
Table6:Performancecomparisonontheindividualdataset(Thunder-DeIDDataset).
D ExperimentResultsforIndividual to enhance the diversity of this relatively smaller
| Dataset |     |     |     |     |     |     | dataset. | So,        | we conducted |             | an comparative |        | anal-  |
| ------- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------ | ----------- | -------------- | ------ | ------ |
|         |     |     |     |     |     |     | ysis     | to analyze | the          | performance |                | change | on the |
We conducted a detailed performance breakdown Thunder-DeID dataset with and without this aug-
| for each | individual | dataset | to  | ensure | transparency |     |            |     |                  |     |         |     |           |
| -------- | ---------- | ------- | --- | ------ | ------------ | --- | ---------- | --- | ---------------- | --- | ------- | --- | --------- |
|          |            |         |     |        |              |     | mentation. |     | The experimental |     | results | are | currently |
andreproducibility.Table4,5,and6showthein-
showninTable7,8,9,and10.
dividualtestresultsfortheCourtJudgment,SNS, As demonstrated in these tables, applying data
andThunder-DeIDdatasets,respectively.
|     |     |     |     |     |     |     | augmentation |               | generally | yields   | consistent |              | perfor- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --------- | -------- | ---------- | ------------ | ------- |
|     |     |     |     |     |     |     | mance        | improvements. |           | However, |            | an exception | is      |
E Performancecomparisonofdata
|              |     |     |     |     |     |     | observed                                   | in        | the individual |            | test on       | the Court | Judg- |
| ------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --------- | -------------- | ---------- | ------------- | --------- | ----- |
| augmentation |     |     |     |     |     |     | mentPIIDataset(Table8),wheretheperformance |           |                |            |               |           |       |
|              |     |     |     |     |     |     | slightly                                   | decreases |                | after data | augmentation. |           | This  |
Wewouldliketoclarifyourdataprocessingstrat-
|               |        |                 |     |       |             |         | specific | gap          | is attributable |     | to the  | interpretations |     |
| ------------- | ------ | --------------- | --- | ----- | ----------- | ------- | -------- | ------------ | --------------- | --- | ------- | --------------- | --- |
| egy regarding |        | "augmentation." |     | For   | our primary |         |          |              |                 |     |         |                 |     |
|               |        |                 |     |       |             |         | and      | applications | of              | the | masking | guidelines      | be- |
| datasets      | (Court | Judgment        | and | SNS), | we          | did not |          |              |                 |     |         |                 |     |
tweenCourtJudgementPIIDatasetandThunder-
| apply data | augmentation |     | (i.e., | generating |     | multi- |      |          |       |      |     |        |         |
| ---------- | ------------ | --- | ------ | ---------- | --- | ------ | ---- | -------- | ----- | ---- | --- | ------ | ------- |
|            |              |     |        |            |     |        | DeID | Dataset. | While | both | our | method | and the |
plesyntheticvariationsforasingleinstancetoin-
|                |        |          |        |              |             |       | Thunder-DeID |     | aim      | to follow | the | official  | guide-  |
| -------------- | ------ | -------- | ------ | ------------ | ----------- | ----- | ------------ | --- | -------- | --------- | --- | --------- | ------- |
| crease dataset | size). | Instead, |        | we performed |             | a 1:1 |              |     |          |           |     |           |         |
|                |        |          |        |              |             |       | lines4,      | our | approach | employs   | a   | different | annota- |
| replacement,   | where  | each     | masked |              | placeholder | in    |              |     |          |           |     |           |         |
tionschemeanddataprocessingmethodology.
thesourcetextwasreplacedwithasinglecontex-
tuallyappropriatesyntheticentitytoconstructthe
|          |            |          |     |     |        |         | F   | KSS |     |     |     |     |     |
| -------- | ---------- | -------- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
| training | data. This | approach |     | was | chosen | to pre- |     |     |     |     |     |     |     |
vent the model from overfitting to specific sen- KSS is a Korean string processing suite that pro-
tence structures, which can occur with excessive vides various functions for processing Korean
strings.Weusedthistosegmenttheannotatedcase
augmentation.
|          |                   |                  |     |               |          |        | court | judgement | data | from | the case | level | to the |
| -------- | ----------------- | ---------------- | --- | ------------- | -------- | ------ | ----- | --------- | ---- | ---- | -------- | ----- | ------ |
| However, | for               | the Thunder-DeID |     |               | dataset, | we     |       |           |      |      |          |       |        |
| applied  | data augmentation |                  |     | by generating |          | multi- |       |           |      |      |          |       |        |
4SupremeCourtTrialRegulationNo.1778revisedonAu-
| ple synthetic | variations |     | for | the PII | placeholders |     | gust9,2021. |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | ------- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- |
2320

|     |     | #of |     | Token | Token | Entity |     | Entity | Overlap | Intermediate |     |
| --- | --- | --- | --- | ----- | ----- | ------ | --- | ------ | ------- | ------------ | --- |
Model
|     |     | parameters | BinaryF1 |     | MicroF1 | BinaryF1 |     | MicroF1 | F1  |     | F1  |
| --- | --- | ---------- | -------- | --- | ------- | -------- | --- | ------- | --- | --- | --- |
KLUEBERT-CRF
|     |     | 110M |     | 0.9977 | 0.9970 | 0.9836 |     | 0.9808 | 0.9892 |     | 0.9887 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/oaugmentation
KLUEBERT-CRF
110M
| w/augmentation |     |     |     | 0.9989 | 0.9988 | 0.9925 |     | 0.9923 | 0.9952 |     | 0.9951 |
| -------------- | --- | --- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
Table7:PerformancecomparisonofdataaugmentationonCombinedDataset.
|     |     | #of |     | Token | Token | Entity |     | Entity | Overlap | Intermediate |     |
| --- | --- | --- | --- | ----- | ----- | ------ | --- | ------ | ------- | ------------ | --- |
Model
|     |     | parameters | BinaryF1 |     | MicroF1 | BinaryF1 |     | MicroF1 | F1  |     | F1  |
| --- | --- | ---------- | -------- | --- | ------- | -------- | --- | ------- | --- | --- | --- |
KLUEBERT-CRF
|     |     | 110M |     | 0.9986 | 0.9985 | 0.9711 |     | 0.9703 | 0.9792 |     | 0.9771 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/oaugmentation
KLUEBERT-CRF
|     |     | 110M |     | 0.9981 | 0.9981 | 0.9447 |     | 0.9438 | 0.9536 |     | 0.9518 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/augmentation
Table8:PerformancecomparisonofdataaugmentationonCourtJudgementPIIDataset.
|     |     | #of |     | Token | Token | Entity |     | Entity | Overlap | Intermediate |     |
| --- | --- | --- | --- | ----- | ----- | ------ | --- | ------ | ------- | ------------ | --- |
Model
|     |     | parameters | BinaryF1 |     | MicroF1 | BinaryF1 |     | MicroF1 | F1  |     | F1  |
| --- | --- | ---------- | -------- | --- | ------- | -------- | --- | ------- | --- | --- | --- |
KLUEBERT-CRF
|     |     | 110M |     | 0.9987 | 0.9985 | 0.9943 |     | 0.9943 | 0.9971 |     | 0.9971 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/oaugmentation
KLUEBERT-CRF
|     |     | 110M |     | 0.9988 | 0.9986 | 0.9945 |     | 0.9945 | 0.9973 |     | 0.9972 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/augmentation
Table9:PerformancecomparisonofdataaugmentationonSNSPIIDataset.
|     |     | #of |     | Token | Token | Entity |     | Entity | Overlap | Intermediate |     |
| --- | --- | --- | --- | ----- | ----- | ------ | --- | ------ | ------- | ------------ | --- |
Model
|     |     | parameters | BinaryF1 |     | MicroF1 | BinaryF1 |     | MicroF1 | F1  |     | F1  |
| --- | --- | ---------- | -------- | --- | ------- | -------- | --- | ------- | --- | --- | --- |
KLUEBERT-CRF
|     |     | 110M |     | 0.9955 | 0.9934 | 0.9231 |     | 0.9031 | 0.9451 |     | 0.9422 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/oaugmentation
KLUEBERT-CRF
|     |     | 110M |     | 0.9998 | 0.9997 | 0.9935 |     | 0.9928 | 0.9946 |     | 0.9946 |
| --- | --- | ---- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ |
w/augmentation
Table10:PerformancecomparisonofdataaugmentationonThunder-DeIDDataset.
sentencelevel.Theparametersettingsforthesen- fore employment to estimate the time require-
tencesegmentationfunctionusedareasfollows. ments, and the pay was set based on this assess-
|                 |     |     |     |     |     | ment. Annotators |     | received | 1,000 | KRW | per court |
| --------------- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ----- | --- | --------- |
| split_sentences |     | (   |     |     |     |                  |     |          |       |     |           |
judgmentcase.Consideringtheiraverageworking
| text :       | str , |     |          |     |     |              |         |     |             |        |             |
| ------------ | ----- | --- | -------- | --- | --- | ------------ | ------- | --- | ----------- | ------ | ----------- |
|              |       |     |          |     |     | hours, their | pay     | was | higher than | the    | legal mini- |
| backend:     | str   | =   | "mecab"  | ,   |     |              |         |     |             |        |             |
|              |       |     |          |     |     | mum wage     | (10,030 | KRW | per         | hour), | so we con-  |
| num_workers: |       | str | = "auto" |     | ,   |              |         |     |             |        |             |
sideritappropriate.
| strip : | bool   | = True | ,   |       |     |     |     |     |     |     |     |
| ------- | ------ | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| ignores | : List | [      | ] = | None, |     |     |     |     |     |     |     |
str
)
|     |     |     |     |     |     | H DistributionDetails |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
G Annotators
Eight annotators, including the author, con- WeprovidethespecificdistributionofPIIentities
tributed to the annotation process over 2 weeks. across each legal domain. Figure 3a presents the
We informed the annotators that the processed PIIentitydistributionacrossthe39legaldomains
data would be used for court judgment de- in our court judgment dataset. Figure 3b presents
identification. To determine appropriate compen- the entity distribution across the three types of
sation,theauthorcompletedpreliminarytasksbe- courtcasesintheThunder-DeIDdataset.
2321

 	 C 
  % J T U S J C V U J P O  P G  1 * *  & O U J U J F T  J O  U I F  5 I V O E F S  % F * %  % B U B T F U
 	 B 
  % J T U S J C V U J P O  P G  1 * *  & O U J U J F T  J O  U I F  $ P V S U  + V E H F N F O U  % B U B T F U
|     |  1                                                                      |  B  S  U          $  P  O  T  U  J  U  V  U  J  P  O                                                             |     |     |    
          	                                                |  
                                 |                           |     |     |
| --- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --- | --- | ----------------------------------------------------------------------- | ---------------------------------- | ------------------------- | --- | --- |
|     |  1  B  S  U          &  M  F  D  U  J  P  O                         |  T        1  P  M  J  U  J  D  B  M    1  B  S  U  J  F  T                                                       |     |     |                                                                         |                                    |   
      	     
 |     |     |
|     |  1  1  B  B  S  S  U  U                  /  (  B  F  U  O  J  P |  F  O  S  B  B  M  M      "  1  V  E  C  N  M  J  J  D  O    J  0  T  U  G  S  G  B  J  D  U  J  J  B  P  M  O  T |     |     |    
            	  
                  	  
          
 |                                    |                           |     |     |
|     |  1  B  S  U                                                           |      $  P  V  S  U  T        +  V  E  J  D  J  B  S  Z                                                          |     |     |                                                                         |    
          	         
 |                           |     |     |
 1  B  S  U          -  F  H  B  M  1    "  B  G  S  G  U  B      J  S    T    $      J    W  +  V  J  M    T  -  U  B  J  D  X  F    
          	          
   
     	      
  '  S  B  V  E    
     	      

|            |  1  B  S  U        1                                                                                 |    B  -  S  P  U    D    B    M      $  (  S  P  J  N  W  F  J  O  S  O  B  N  M    -  F  B  O  X  U          |     |                                                          |                                                                         |    
          
      	             	        
      
 |                                                   |                                                                   |                                      |
| ---------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
|            |                                                                                                          |  1  B  S  U            1  P  M  J  D  F                                                                         |     |                                                          |    
          	                                                |  
                                                                     |                                                   |                                                                   |                                      |
|            |  1  B  S  U            1  .  B  J  S  M  U  J  U                                                    |      B  S    Z        4  .  F  S  J  M  W  J  U  J  D  B  F  S  Z    "    "  E  G  N  G  B  J  J  O  S  T   |     |          	                                          |        
    
                                                     |      	          
                                                |                                                   |                                                                   |                                      |
|            |  1  B  S  U                                                                                         |  1  B  U  S  J  P  U  T        7  F  U  F  S  B  O  T                                                             |     |          	          
                            |                                                                         |                                                                        |                                                   |                                                                   |                                      |
|            |  1  B  1  S  B  U  S      U              &      E  $  V  V                                     |  D  M  U  B  V  U  J  S  P  F  O            1    "  V  C  D  B  M  J  D  E    F  *  O  N  G  P  J  B         |     |      	         
                              |    	          
                                                    |                                                                        |                                                   |                                                                   |                                      |
|            |  1  B  S  U            4  D  J                                                                      |  F  O  D  F        5  F  D  I  O  P  M  P  H  Z                                                                   |     |                                                         |        	          
                                              |                                                                        |                                                   |                                                                   |                                      |
|            |  1  B  S  U    1    B    S    U      '                                                             |    J  O    B      O  %  D  P  F  N      F    T  &  U  D  J  D  P    O  5  B  P  Y  N  F  Z  T                |     |                                                      |  	          
                                                       |    
                                                              |  	          
                                 |                                                                   |                                      |
|            |  1  B  S  U                                                                                           |      $  V  T  U  P  N  T        5  B  S  J  G  G  T                                                             |     |          	          
                            |    
          	          
                                     |                                                                        |                                                   |  * O E F D F O U  B  D  U    C Z   D  P  N  Q  V  M T  J  P  O |    
         	           
 |
|            |  1  B  S  U            1  $                                                                         |  B  V  S  S  U  S      F  O    D      Z  "      H  S    '  J  D  J  O  V  B  M  U  O  V  D  S  F  F          |     |          	                                         |      
                                                                |                                                                        |                                                   |                                                                   |                                      |
|            |                                                                                                          |  1  1  B  B  S  U  S    U                  -    J  '  W  P  F  S  T  F  U  T  P  U  D  S  L  Z             |     |          	                  	    
       |  
                                                                      |                                                                        |                                                   |                                                                   |                                      |
|            |                                                                                                          |  1  B  S  U            '  J  T  I  F  S  J  F  T                                                                |     |                                                          |    
          	                                                   |        
                                                            |                                                   |                                                                   |                                      |
|  1 B S U  |          1  $  B  P  S  N  U      N    F      S  $  D  P  F  N  
    5  N  S  B  F  E  S  F  D |  
  F    &  
    O  5  S  F  B  S  E  H  F  Z              *  *  O  O  E  E  V  V  T  T  U  U  S  S  Z  Z    |     |                                                          |    
        
          	        	                
  
 |                                                                        |                                                   |                                                                   |                                      |
|            |  1  B  S  U            &  O                                                                         |  F  S  H  Z    6  T  F        .  J  O  J  O  H                                                                   |     |                                                          |          	          
                                           |                                                                        |                                                   |                                                                   |                                      |
|            |  1  B  S  U            /  B  U  J  P  O  B  1  M    B  -  B  S  U  O      E                      |      %      F  &  W  M  F      D    U  S    6  J  D  S  J  U  C  Z  B      O      (  "  G  B  G  T      |     |                                                          |                                                                         |    
          	                                                   |          
          
    	         
 |                                                                   |                                      |
|            |  1  B  S  U            )  P  V  T  J  O  H  
    $  P                                              |  O  T  U  S  V  D  U  J  P  O        3  P  B  E  T                                                                |     |                                                          |                                                                         |                                                                        |    
          	          
               |                                                                   |                                      |
|            |  1  B  S  1  U    B    S    U          8      B    1  U  V  F  S  C  
  M    J  -  D  B       |    )  O  E  F  B      M  U    I  $    P    O    .  T  U  S  F  V  E  D  J  D  U  J  J  P  O  O  F             |     |                                                          |    
          	          
                                     |    
                                                                 |        	          
                        |                                                                   |                                      |
|            |  1  B  S  1  U  B      S    U                                                                         |          1    I      B  4  S  P  N  D  J  B  B  D  M    Z  8    "  F  G  M  G  G  B  B  J  S  S  F  T       |     |                                                          |    
          	          
    
          	               |        
                                                            |                                                   |  $  S  J  N  F   P  G   W  J P  M F  O  D  F                    |   
          	           
 |
|            |  1  B                                                                                                    |  S  U            &  O  W  J  S  P  O  N  F  O  U                                                                |     |                                                          |    
          	                                                 |    
                                                                  |                                                   |                                                                   |                                      |
|            |  1  B  S  U            5  S  B  O  T  Q                                                             |  P  S  U  B  U  1  J  P  B  O  S  U              5    P    -  V  B  S  C  J  T  P  N  S                      |     |                                                        |      	          
    
                                         |      	          
                                                |                                                   |                                                                   |                                      |
|            |  1  B  S  U            .  B  S  J  U  J  N  F                                                       |    "  G  G  B  J  S  T        4  I  J  Q  Q  J  O  H                                                             |     |                                                          |    
          	                                                   |        
                                                            |                                                   |                                                                   |                                      |
|            |  1  B  S  U            *  O  G  P  S  N  B  U  J  P  O                                             |      $  P  N  N  V  O  J  D  B  U  J  P  O  T                                                                      |     |                                                         |        	          
                                              |                                                                        |                                                   |                                                                   |                                      |
            / V N C F S  P G   &   O  U J U J F T                             / V N C  F  S    P G  & O U J U J F T                       
(a)TheentrydistributioninourCourtJudgmentdataset. (b)TheentrydistributionintheThunder-DeIDdataset.
Figure3:DistributionofPIIentitiesintheCourtJudgmentandThunder-DeIDdatasets.
I Fine-tuning
| We  | fine-tune |     | KLUEBERT-CRF, |     |     | KLUEBERT, |     |     |     |
| --- | --------- | --- | ------------- | --- | --- | --------- | --- | --- | --- |
Thunder-DeID,Kanana-1.5,andQwen-2.5onPII
| Entity |        | Recognition |     | task | using          | the dataset | split      |     |     |
| ------ | ------ | ----------- | --- | ---- | -------------- | ----------- | ---------- | --- | --- |
| for    | train, | validation, |     | and  | test described |             | in section |     |     |
4.1.Wefullyfine-tuneKLUEBERT-CRF,KLUE-
BERT,andThunder-DeIDandweLoRAfine-tune
| Kanana-1.5 |       | and         | Qwen-2.5, |                | setting | hyperparame- |          |     |     |
| ---------- | ----- | ----------- | --------- | -------------- | ------- | ------------ | -------- | --- | --- |
| ters       | while | considering |           | hardware       |         | capacity.    | More     |     |     |
| details    |       | about       | model     | specifications |         | and          | hyperpa- |     |     |
rameteraredescribedinTable11
J AnnotatedDataSample
| In  | this | section, | we  | present | the | Figure | 4 and 5 |     |     |
| --- | ---- | -------- | --- | ------- | --- | ------ | ------- | --- | --- |
thesampleofbothpubliclyavailableanonymized
| court   | judgement |        | and         | the | court | judgement | an-    |     |     |
| ------- | --------- | ------ | ----------- | --- | ----- | --------- | ------ | --- | --- |
| notated |           | by our | annotators. |     | We    | convert   | PII to |     |     |
uniquesymbolsinourannotationscheme.Theat-
| tached     |            | court | judgment    | is   | an excerpt |            | from "2014 |     |     |
| ---------- | ---------- | ----- | ----------- | ---- | ---------- | ---------- | ---------- | --- | --- |
| 가합38116".  |            |       | In publicly |      | available  | anonymized |            |     |     |
| court      | judgments, |       | words       | that | would      | be         | PII if not |     |     |
| anonymized |            | were  | replaced    |      | with       | symbols    | accord-    |     |     |
ingtotheannotationscheme.
2322

KLUEBERT-CRF
| Aspect |     | KLUEBERT | Thunder-DeID | Kanana-1.5 | Qwen-2.5 |
| ------ | --- | -------- | ------------ | ---------- | -------- |
(ours)
ModelSpecification
| #ofParameters   | 110M   | 110M   | 360M   | 2.1B    | 1.5B    |
| --------------- | ------ | ------ | ------ | ------- | ------- |
| HiddenDimension | 768    | 768    | 1,024  | 1,792   | 1,536   |
| Hiddenlayers    | 12     | 12     | 24     | 32      | 28      |
| AttentionHead   | 12     | 12     | 16     | 24      | 14      |
| VocabularySize  | 32,026 | 32,000 | 32,000 | 128,259 | 151,936 |
Fine-tuning
| Hardware         | 2xRTX8000 | 2xRTX8000 | 2xRTX8000 | 2xRTX8000 | 2xRTX8000 |
| ---------------- | --------- | --------- | --------- | --------- | --------- |
| Duration         | 24hours   | 24hours   | 24hours   | 3days     | 4days     |
| LearningRate     | 3e-5      | 3e-5      | 3e-5      | 2e-5      | 3e-5      |
| BatchSize        | 32        | 32        | 8         | 4         | 16        |
| SeqLength        | 512       | 512       | 512       | 512       | 512       |
| AdamWWeightDecay | 0.02      | 0.01      | 0.01      | 0.01      | 0.01      |
AdamWBetas β=(0.9,0.999) β=(0.9,0.999) β=(0.9,0.999) β=(0.9,0.999) β=(0.9,0.999)
LoRAtuning
| LoRAr             | -   | -   | -   | 16            | 8             |
| ----------------- | --- | --- | --- | ------------- | ------------- |
| LoRAAlpha         | -   | -   | -   | 32            | 16            |
| LoRADropout       | -   | -   | -   | 0.05          | 0.05          |
|                   |     |     |     | q,v,k,o,gate, | q,v,k,o,gate, |
| LoRATargetModules | -   | -   | -   |               |               |
|                   |     |     |     | up,down_proj  | up,down_proj  |
Table11:Detailedreportofusedmodels.
2323

An example of publicly available anonymized court judgement
【판시사항】
갑 외국법인이 인터넷을 기반으로 하여 전 세계적으로 제공하는 검색, 이메일 등의 서비스에 가입한 을 등이 갑 법인을 상대로 정보통신망 이용
촉진 및 정보보호 등에 관한 법률 제30조 제2항, 제4항에 따라 갑 법인이 을 등의 개인정보 및 서비스 이용 내역을 제3자에게 제공한 현황의
공개 등을 구한 사안에서, 을 등과 갑 법인 사이의 서비스 이용에 관한 법률관계에는 서비스 약관상 준거법 합의가 있더라도 정보통신망 이용촉
진 및 정보보호 등에 관한 법률상 이용자의 권리보호에 관한 규정들이 적용되고, 갑 법인은 법령에 의하여 비공개 의무가 부과된 사항을 제외하
고 을 등의 개인정보 및 서비스 이용 내역을 제3자에게 제공하였는지와 그 내용을 공개할 의무가 있다고 한 사례
【판결요지】
갑 외국법인이 인터넷을 기반으로 하여 전 세계적으로 제공하는 검색, 이메일 등의 서비스에 가입한 을 등이 갑 법인을 상대로 정보통신망 이용
촉진 및 정보보호 등에 관한 법률(이하 ‘정보통신망법’이라 한다) 제30조 제2항, 제4항에 따라 갑 법인이 을 등의 개인정보 및 서비스 이용 내
역을 제3자에게 제공한 현황의 공개 등을 구한 사안에서, 정보통신망법 제30조에서 정한 정보통신서비스 이용자의 권리는 국제사법 제27조 제1
항의 ‘준거법 선택에 의하더라도 박탈할 수 없는 소비자에게 부여되는 보호에 관한 강행규정’에 해당하고, 당사자가 준거법으로 외국법을 적용하
는 것에 대한 합의를 하였더라도 이용자가 정보통신망법에 근거한 권리를 행사할 수 없도록 하는 것은 우리나라 강행규정에 의하여 소비자에게
부여되는 보호를 박탈하는 것으로서 그 범위 내에서는 외국법을 준거법으로 하는 합의의 효력을 인정할 수 없으므로, 을 등과 갑 법인 사이의 서
비스 이용에 관한 법률관계에는 서비스 약관상 준거법 합의가 있더라도 정보통신망법상 이용자의 권리보호에 관한 규정들이 적용되고, 다만 정보
통신망법 제30조 제4항이 정보통신서비스 제공자에게 어떤 경우이든지 예외 없이 개인정보를 제3자에게 제공한 현황을 공개하도록 하는 의무를
부담시키고 있다고 보기 어려우므로, 갑 법인은 법령에 의하여 비공개 의무가 부과된 사항을 제외하고 을 등의 개인정보 및 서비스 이용 내역을
제3자에게 제공하였는지와 그 내용을 공개할 의무가 있다고 한 사례.
An example court judgment annotated according to our annotation scheme
【판시사항】
#@company#이 인터넷을 기반으로 하여 전 세계적으로 제공하는 검색, 이메일 등의 서비스에 가입한 #@name# 등이 #@com-
pany#을 상대로 정보통신망 이용촉진 및 정보보호 등에 관한 법률 제30조 제2항, 제4항에 따라 #@company#이 #@name# 등의 개
인정보 및 서비스 이용 내역을 제3자에게 제공한 현황의 공개 등을 구한 사안에서, #@name# 등과 #@company# 사이의 서비스 이용에
관한 법률관계에는 서비스 약관상 준거법 합의가 있더라도 정보통신망 이용촉진 및 정보보호 등에 관한 법률상 이용자의 권리보호에 관한 규정들
이 적용되고, #@company#은 법령에 의하여 비공개 의무가 부과된 사항을 제외하고 #@name# 등의 개인정보 및 서비스 이용 내역을
제3자에게 제공하였는지와 그 내용을 공개할 의무가 있다고 한 사례
【판결요지】
#@company#이 인터넷을 기반으로 하여 전 세계적으로 제공하는 검색, 이메일 등의 서비스에 가입한 #@name# 등이 #@co-
mpany#을 상대로 정보통신망 이용촉진 및 정보보호 등에 관한 법률(이하 ‘정보통신망법’이라 한다) 제30조 제2항, 제4항에 따라
#@company#이 #@name# 등의 개인정보 및 서비스 이용 내역을 제3자에게 제공한 현황의 공개 등을 구한 사안에서, 정보통신망법 제
30조에서 정한 정보통신서비스 이용자의 권리는 국제사법 제27조 제1항의 ‘준거법 선택에 의하더라도 박탈할 수 없는 소비자에게 부여되는 보
호에 관한 강행규정’에 해당하고, 당사자가 준거법으로 외국법을 적용하는 것에 대한 합의를 하였더라도 이용자가 정보통신망법에 근거한 권리를
행사할 수 없도록 하는 것은 우리나라 강행규정에 의하여 소비자에게 부여되는 보호를 박탈하는 것으로서 그 범위 내에서는 외국법을 준거법으로
하는 합의의 효력을 인정할 수 없으므로, #@name# 등과 #@company# 사이의 서비스 이용에 관한 법률관계에는 서비스 약관상 준거법
합의가 있더라도 정보통신망법상 이용자의 권리보호에 관한 규정들이 적용되고, 다만 정보통신망법 제30조 제4항이 정보통신서비스 제공자에게
어떤 경우이든지 예외 없이 개인정보를 제3자에게 제공한 현황을 공개하도록 하는 의무를 부담시키고 있다고 보기 어려우므로, #@com-
pany#은 법령에 의하여 비공개 의무가 부과된 사항을 제외하고 #@name# 등의 개인정보 및 서비스 이용 내역을 제3자에게 제공하였는지
와 그 내용을 공개할 의무가 있다고 한 사례.
Figure4:Asampledataofannonymizedcourtjudgementandcourtjudgementannotatedaccordingtoourannota-
tionscheme.
2324

An example of publicly available anonymized court judgement (translated in English)
【Holding】
In a case where Party B, who subscribed to services such as search and email provided globally by Foreign Corporation A via the internet, requested
disclosure of the status of Party A's provision of Party B's personal information and service usage records to third parties pursuant to Article 30(2) and
(4) of the Act on Promotion of Information and Communications Network Utilization and Information Protection, etc., Even if the legal relationship
between Party B and the Corporation A regarding service use contains a governing law agreement in the service terms, the provisions protecting user
rights under the Act on Promotion of Information and Communications Network Utilization and Information Protection apply. The Corporation A has an
obligation to disclose whether it provided Party B's personal information and service usage details to third parties, and the content of such disclosure,
except for matters subject to a non-disclosure obligation imposed by law.
【Abstract】
Party A, a foreign corporation, provides search, email, and other services globally via the internet. Party B and others, who subscribed to these services,
requested Party A to disclose the status of providing their personal information and service usage details to third parties pursuant to Article 30,
Paragraphs 2 and 4 of the Act on Promotion of Information and Communications Network Utilization and Information Protection, etc. (hereinafter
referred to as the “Information and Communications Network Act”). In this case, the rights of users of information and communications services
stipulated in Article 30 of the Act constitute a mandatory provision concerning the protection granted to consumers that cannot be deprived even by
choice of law under Article 27(1) of the International Private Law Act. Therefore, even if the parties agreed to apply foreign law as the governing law,
preventing users from exercising their rights under the Information and Communications Network Act would deprive consumers of the protection
afforded by Korea's mandatory provisions. Consequently, within that scope, the validity of an agreement designating foreign law as the governing law
cannot be recognized. Therefore, even if there is an agreement on the governing law in the service terms between Party B and Company A regarding the
legal relationship concerning the use of the service, the provisions of the Information and Communications Network Act concerning the protection of
the user's rights apply. However, it is difficult to interpret Article 30(4) of the Information and Communications Network Act as imposing an obligation
on information and communications service providers to disclose the status of personal information provided to third parties in all cases without
exception. Therefore, there is a case where Company A was found to have an obligation to disclose whether it provided the personal information and
service usage details of Party B and others to third parties, and the content thereof, except for matters subject to a non-disclosure obligation imposed
by law.
An example court judgment annotated according to our annotation scheme (translated in English)
【Holding】
In a case where #@name#, who subscribed to services such as search and email provided globally by #@company# via the internet, requested
disclosure of the status of #@company#'s provision of #@name# 's personal information and service usage records to third parties pursuant to
Article 30(2) and (4) of the Act on Promotion of Information and Communications Network Utilization and Information Protection, etc., Even if the legal
relationship between Party #@name# and the #@company# regarding service use contains a governing law agreement in the service terms, the
provisions protecting user rights under the Act on Promotion of Information and Communications Network Utilization and Information Protection apply.
#@company# has an obligation to disclose whether it provided #@name#'s personal information and service usage details to third parties, and the
content of such disclosure, except for matters subject to a non-disclosure obligation imposed by law.
【Abstract】
#@company#, a foreign corporation, provides search, email, and other services globally via the internet. #@name# and others, who subscribed to
these services, requested #@company# to disclose the status of providing their personal information and service usage details to third parties
pursuant to Article 30, Paragraphs 2 and 4 of the Act on Promotion of Information and Communications Network Utilization and Information
Protection, etc. (hereinafter referred to as the “Information and Communications Network Act”). In this case, the rights of users of information and
communications services stipulated in Article 30 of the Act constitute a mandatory provision concerning the protection granted to consumers that
cannot be deprived even by choice of law under Article 27(1) of the International Private Law Act. Therefore, even if the parties agreed to apply foreign
law as the governing law, preventing users from exercising their rights under the Information and Communications Network Act would deprive
consumers of the protection afforded by Korea's mandatory provisions. Consequently, within that scope, the validity of an agreement designating
foreign law as the governing law cannot be recognized. Therefore, even if there is an agreement on the governing law in the service terms between
#@name# and #@company# regarding the legal relationship concerning the use of the service, the provisions of the Information and
Communications Network Act concerning the protection of the user's rights apply. However, it is difficult to interpret Article 30(4) of the Information
and Communications Network Act as imposing an obligation on information and communications service providers to disclose the status of personal
information provided to third parties in all cases without exception. Therefore, there is a case where #@company# was found to have an obligation to
disclose whether it provided the personal information and service usage details of #@name# and others to third parties, and the content thereof,
except for matters subject to a non-disclosure obligation imposed by law.
Figure5:Atranslatedsampledataofannonymizedcourtjudgementandcourtjudgementannotatedaccordingto
ourannotationscheme.
2325
