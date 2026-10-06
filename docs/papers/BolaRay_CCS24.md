> 원본: BolaRay_CCS24.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.10-13 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
Detecting Broken Object-Level Authorization Vulnerabilities in
Database-Backed Applications
YonghengHuang ChenghangShi JieLu∗
SKLP,InstituteofComputing SKLP,InstituteofComputing SKLP,InstituteofComputing
Technology,CAS Technology,CAS Technology,CAS
UniversityofChineseAcademyof UniversityofChineseAcademyof Beijing,China
Sciences Sciences lujie@ict.ac.cn
Beijing,China Beijing,China
huangyongheng20s@ict.ac.cn shichenghang21s@ict.ac.cn
HaofengLi HainingMeng LianLi∗
SKLP,InstituteofComputing SKLP,InstituteofComputing SKLP,InstituteofComputing
Technology,CAS Technology,CAS Technology,CAS
Beijing,China UniversityofChineseAcademyof UniversityofChineseAcademyof
lihaofeng@ict.ac.cn Sciences Sciences
Beijing,China ZhongguancunLaboratory
menghaining@ict.ac.cn Beijing,China
lianli@ict.ac.cn
Abstract ACMReferenceFormat:
Brokenobject-levelauthorization(BOLA)vulnerabilitiesareamong Yongheng Huang, Chenghang Shi, Jie Lu, Haofeng Li, Haining Meng,
andLianLi.2024.DetectingBrokenObject-LevelAuthorizationVulnera-
themostcriticalsecurityrisksfacingdatabase-backedapplications.
bilitiesinDatabase-BackedApplications.InProceedingsofthe2024ACM
However,thereisstillasignificantgapinoursystematicunder-
SIGSACConferenceonComputerandCommunicationsSecurity(CCS’24),
standingofthesevulnerabilities.Tobridgethisgap,weconducted October14–18,2024,SaltLakeCity,UT,USA.ACM,NewYork,NY,USA,
anin-depthstudyof101real-worldBOLAvulnerabilitiesfromopen- 15pages.https://doi.org/10.1145/3658644.3690227
sourceapplications.Ourstudyrevealedthefourmostcommon
object-levelauthorizationmodelsindatabase-backedapplication.
Theinsightsgainedfromourstudyinspiredthedevelopment
1 Introduction
ofanewtoolcalledBolaRay.Thistoolemploysacombinationof
SQLandstaticanalysistoautomaticallyinferthedistincttypesof This(BOLA)hasbeenthemostcommonandimpactfulattackon
object-levelauthorizationmodels,andsubsequentlyverifywhether APIs.
existingimplementationsenforceappropriatechecksforthesemod- —TheOpenWebApplicationSecurityProject(OWASP)[33]
els.WeevaluatedBolaRayusing25populardatabase-backedappli-
cations,whichledtotheidentificationof 193truevulnerabilities, Database-backedapplicationsutilizeadatabasetomanagedata,
including178vulnerabilitiesthathaveneverbeenreportedbefore, oftenaccompaniedbyafront-endtointeractwiththeuserand
performdatabaseoperationsupontheuser’srequests.Suchap-
at a false positive rate of 21.86%. We reported all newly identi-
fiedvulnerabilitiestothecorrespondingmaintainers.Todate,155 plicationsarewidelyadoptedacrossvariousindustries,including
vulnerabilitieshavebeenconfirmed,with52CVEIDsgranted. contentmanagementsystems,e-commercewebsites,andhospital
managementplatforms.However,giventhevastamountsofsen-
CCSConcepts sitivedatamanagedbytheseapplications,theyhavealsobecome
primetargetsforcybersecurityattacks.
•Securityandprivacy→Softwareandapplicationsecurity.
A variety of vulnerabilities, such as SQL injection [35] and
Keywords XSS[36],canbeexploitedtocompromisedatabase-backedappli-
cationsandstealsensitivedata.Amongthem,brokenobject-level
BrokenObject-LevelAuthorization;Database-BackedApplications authorization(BOLA)vulnerabilities,alsoknownasinsecuredi-
rectobjectreference(IDOR)[4],havegainedthetoppositioninthe
∗Correspondingauthor
OWASPAPITop10rankings[34]duetotheircommonoccurrence
andhighrisk.Notably,manywidely-usedapplications,suchasPay-
ThisworkislicensedunderaCreativeCommonsAttribution
International4.0License. Pal,Twitter,andTikTok,havesufferedfromBOLAvulnerabilities,
asreportedinHackerOne[39].
CCS ’24, October 14–18, 2024, Salt Lake City, UT, USA Figure1illustratesCVE-2022-31295,aBOLAvulnerabilityinthe
© 2024 Copyright held by the owner/author(s). applicationOdfs-1.0(OnlineDiscussionForumSite).Asthename
ACM ISBN 979-8-4007-0636-3/24/10
suggests,thisapplicationallowsuserstocreatepostswhichare
https://doi.org/10.1145/3658644.3690227
storedintheposttable—adatabasetableutilizingidasitsprimary
2934

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
|           |           |     |     |               | b o u n t y p | la t f o r m H u n t | r [ 4 8 ] . T o t h e b | e s t o f o u r k n o | w l e d g e , t h is i s |
| --------- | --------- | --- | --- | ------------- | ------------- | -------------------- | ----------------------- | --------------------- | ------------------------ |
| h t       |           |     |     | p o s t       |               |                      |                         |                       |                          |
| t p : / / | v u l n e |     |     | i d us e ri d | con t ent     |                      |                         |                       |                          |
h t t p : / / v r a b l e . c o m / t h e fi r st i n - d e p t h s t u d y o f B O L A v u ln e r a b i l i ti e s . D u r in g o u r s t u d y ,
|     | u l n e r a b l e . d e l p o s t . | p h |     | 1 1 | · · · |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
c o m / d e l p o p ? i d = 1 2 2 · · · w e h a v e o b t a i n e d t w o i n t e r e s t i n g fi n d i n g s , w h i c h c a n r e s p e c t i v e l y
| Attacker | 1 s t . | p h p ? i d = |     |     |     |     |     |     |     |
| -------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
2 h e l p t o a d d r e s s t h e t w o c h a l l e n g e s m e n t i o n e d a b o v e .
3 Da ta b a s e
http://vulnerable.com/delpost.php?id=2 A u t o m a t ic a l ly in f e r r in g a u t h o r i z a t i o n m o d e l s . W e o bs er v e
|     |     |                         |     | u s e r    | tha t th e r | ea r e f o u rd is t in | c t k in d s o f o b | j e c t - le ve la u t h | o r i za tio n m o d - |
| --- | --- | ----------------------- | --- | ---------- | ------------ | ----------------------- | -------------------- | ------------------------ | ---------------------- |
|     |     | if($role == "poster") { |     | id n a m e | role         |                         |                      |                          |                        |
2Server
query("DELETE FROM  1 Attacker poster elsinreal-worldapplications.Amongthesemodels,onlytheown-
| Victim |     | p ostWHEREid='$id'"); |     | 2 Victim | poster                                                   |     |     |     |     |
| ------ | --- | --------------------- | --- | -------- | -------------------------------------------------------- | --- | --- | --- | --- |
|        |     | }                     |     |          | ershipmodelhasbeenstudiedbefore[28,30],withtheotherthree |     |     |     |     |
Figure1:TheBOLAvulnerabilityCVE-2022-31295 modelsremainingunexploredintheliterature.Furthermore,we
observethatallobject-levelauthorizationmodelscanbederived
key.TheURL"http://vulnerable.com?delpost.php?id=1"re- fromrelationsacrossdatabasetables.Forinstance,inFigure1,the
queststhedeletionofapostwhoseidequals1. columnuseridoftheposttableistheforeignkeyreferencingthe
| The authorization |     | model of | this application | should | be fine- |     |     |     |     |
| ----------------- | --- | -------- | ---------------- | ------ | -------- | --- | --- | --- | --- |
primarykey(Columnid)oftheusertable.
grainedattheobjectlevel:onlythecreatorofapostshouldhave
Inlightofthis,weproposetoinferobject-levelauthorization
| thenecessarypermissionto |     | deleteit. | However,due | tothelack |     |     |     |     |     |
| ------------------------ | --- | --------- | ----------- | --------- | --- | --- | --- | --- | --- |
modelsbyreasoningaboutrelationsbetweendifferentdatabase
ofobject-levelauthorizationchecks,anattackercandeleteother tables.Insimplecases,relationsbetweendistinctdatabasetablesare
users’postsatwill.Letusanalyzesuchanattack. 1 Theattacker directlydeclaredasforeignkeysinthedatabaseschema.However,
attemptstodeleteapostbelongingtothevictimbytamperingwith
suchrelationsareoftennotexplicitlyspecifiedintheschema,but
| theidfrom1to2. | 2 Themodifiedrequestissenttotheapplication |     |     |     |     |     |     |     |     |
| -------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
areinsteadimplicitlyimplementedinthesourcecode.Hence,to
| server,whichprocessesitintoaSQLstatement. |     |     |     | Thedatabase |                                                          |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | ----------- | -------------------------------------------------------- | --- | --- | --- | --- |
|                                           |     |     |     | 3           | addressthischallenge,wehavedesignedasetofrigorousrulesto |     |     |     |     |
executestheSQLstatementtoperformthedeletionoperation,al- deduceimplicitforeignkeyreferencesbyexaminingthecomplex
beitundesirably.Inthisexample,itisnoteworthythatdespitethe interactionbetweenprogramcodeanddatabasequeries.
server’svalidationoftheattacker’sroleasaposterwithDELETE EfficientlydetectingBOLAvulnerabilities.Weobservethat
privileges,itfailstofurtherverifywhethertheattackerisindeed allstudiedBOLAvulnerabilitiesareduetomissingobject-levelau-
thecreatoroftheposttobedeleted.
|     |     |     |     |     | thorizationchecks. | Thus,insteadofanalyzingwhethertheautho- |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --------------------------------------- | --- | --- | --- |
1.1 Challenges rizationmodelforeachobjectaccessisconsistentlyenforcedor
not(whichoftenrequiresextensiveconstraintsolvingofpathcon-
TodetectBOLAvulnerabilities,itisvitaltounderstandtheunderly-
ingobject-levelauthorizationmodel,whichdeterminestheappropri- ditions),wefocusonthecommoncaseswhereaccessestosensitive
objectslackobject-levelauthorizations.Forinstance,inFigure1,an
atepolicyforaccessinganobject.Forinstance,Figure1illustrates
accesstoobjectpostneedstobecheckedagainstboththeobject
thatapostobjectcanonlybedeletedbyitscreator.However,it
itselfanditscreator,user.Thisapproximationleadstoanefficient
ischallenging,ifnotimpossible,topreciselyinferobject-levelau-
yetpreciseapproachtohuntBOLAvulnerabilities,whichaddresses
thorizationmodelsandefficientlydetectBOLAvulnerabilitiesthat
challenge2.
violatethosemodels.Here,wesummarizetwomainchallenges:
Itiscrucialtounderstandthatmissingobject-levelauthorization
Challenge1:Howcanwepreciselyandautomaticallyinfer
checks
object-levelauthorizationmodels?Althoughtherehavebeen notonlyincludessimplecaseswherepermissionchecks
areentirelymissing,butalsoencompassescaseswithinconsistent
effortstoautomaticallyinfercoarse-grained,function-level[32]
orincompletechecksthatfailtoverifythecorrectcorresponding
| authorization | models | [15, 41, 43, | 44, 53], object-level | authoriza- |     |     |     |     |     |
| ------------- | ------ | ------------ | --------------------- | ---------- | --- | --- | --- | --- | --- |
object.Forinstance,asshowninFigure1,althoughrolepermissions
| tion models | are much | more intricate | and | require finer-grained, |     |     |     |     |     |
| ----------- | -------- | -------------- | --- | ---------------------- | --- | --- | --- | --- | --- |
application-specificsemantics.Thisrequirementposesasignifi- are checked, object-level authorization is missing. Additionally,
object-levelauthorizationchecksmayinvolvemultiplesub-checks.
| cant challenge | to automating | this | process. | As a result, | existing |     |     |     |     |
| -------------- | ------------- | ---- | -------- | ------------ | -------- | --- | --- | --- | --- |
Anymissingsub-checksleadstoincompleteauthorization,which
approachesareincapableofderivingcomplexobject-levelautho-
isalsoconsideredalackofobject-levelauthorizationchecks.We
rizationmodelsandoftenrelyonthemanualannotationofeach
willfurtherelaborateonthedetailsinSection3.3.
objectoperationwithauthorizationrules,whichistediousand
error-prone[13]. Puttingitalltogether,wehavedevisedanefficientyetprecise
Challenge2:Howcanweefficientlyandpreciselydetect static approach for detecting BOLA vulnerabilities in database-
BOLAvulnerabilities?TodetectBOLAvulnerabilities,weneed backedapplications.
toaccuratelycomputewhethereachobjectaccessischeckedprop-
erlyagainstitsauthorizationmodelsornot.Thisoftendemands 1.3 Contributions
| expensive | path-sensitive | analyses, | such as | model checking | and |     |     |     |     |
| --------- | -------------- | --------- | ------- | -------------- | --- | --- | --- | --- | --- |
WerealizeourapproachinanewtoolnamedBolaRayandevaluate
symbolicexecution[7,9,12–14,28,30],whicharedifficulttoscale
iton25populardatabase-backedapplications.BolaRaypreciselyin-
toreal-worldapplications.
fersobject-levelauthorizationmodelsinallevaluatedapplications,
1.2 Solutions
andreports193vulnerabilities,including178newvulnerabilities
To tackle these two challenges, it is imperative to gain a deep thathaveneverbeenfoundbefore,withonly54falsepositives.To
understanding of the real-world BOLA vulnerabilities. For this date,155newlyreportedvulnerabilitieshavebeenconfirmedand
purpose,thispaperconstructsacomprehensivedatasetconsisting 52ofthemhavebeenassignedCVEIDs.
of101BOLAvulnerabilitiesfromtheCVEdatabase[1]andthebug Thecontributionsofthispaperaresummarizedasfollows:
2935

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
• Weprovidethefirstin-depthstudyofBOLAvulnerabilities 3-9,toverifythattherequesterisamemberofthetarget
inreal-worlddatabase-backedapplications.Ourstudysheds forum.
lightonnewdetectiontechniquesforBOLAvulnerabilities • InFigure3(c),theAPIdelete_noticedeletesanoticeofa
withinsuchapplications. forumasrequestedbytheforummanager.Avulnerability
• Weintroduceanovelstaticanalysisapproachtoidentify manifestsiftheAPIdoesnotcheckwhethertherequester
BOLAvulnerabilitiesindatabase-backedapplications.Our isamemberoftheforumtowhichthedeletednoticebe-
analysisefficientlyuncoversobject-levelauthorizationmod- longs.Thisauthorizationruleisenforcedthroughlines4-9
elswithhighaccuracybystaticallyanalyzingtherelation- inFigure3(c)andlines1-9inFigure3(b),whichverifiesthe
shipsbetweendatabasetables. relationshipbetweenthetargetnoticeanditsparentforum,
• WehaveimplementedourapproachasatooldubbedBo- andthemembershipbetweentherequesterandtheforum,
laRay, and evaluated it using 25 real-world applications. respectively.
BolaRayaccuratelyreported193vulnerabilities,including • InFigure3(d),theAPIadd_commentenablesuserstocom-
178newcriticalBOLAvulnerabilities.Outofthese,155have mentonposts.ThevulnerabilitystemsfromtheAPI’sfailure
beenconfirmed,and52CVEIDshavebeengranted. toverifywhetherthepostisinanopenstatus.Thisissueis
• Tofacilitatefutureresearch,wehavereleasedthesource rectifiedinlines4-9ofFigure3(d).
codeof BolaRay,togetherwithallstudiedvulnerabilities,
EachvulnerabilityinFigure3necessitatesadistinctobject-level
athttps://github.com/BolaRay-d/BolaRay.
authorizationcheck.Thesechecksverifyvariousrelationsbetween
2 AnIllustrationExample
theaccessingobjectandtherequester,orbetweenrelatedobjects,
Figure2andFigure3depictanexampleofacontentmanagement eachcorrespondingtoadistinctauthorizationmodel.Todetect
applicationthatisusedthroughoutthispaper.Figure2presents suchvulnerabilities,weneedtopreciselyanalyzethefine-grained
the 7 tables in this application, where each table uses id as its authorizationmodelforeachobjectaccessandthenverifywhether
primarykey,andimplicitforeignkeyreferencesarehighlightedin theauthorizationmodelhasbeenproperlyimplemented.
yellow.Forinstance,forumidisanimplicitforeignkeyreferencing 3 EmpiricalStudy
forum::id–theprimarykeyidoftableforum.Recallthatthose
implicitforeignkeyreferencesneedtobederivedfromthesource TheUSPShackisaclassicexampleofabrokenauthorization
code.Relationshipsbetweendistincttables,derivedfromforeign vulnerability.UserAwasabletoauthenticatetotheAPIandthen
keyreferences,areconnectedbyarrows. pivotandaccessuserB’sand60millionotherpeople’sinformation.
Among the 7 tables, the user table manages registered user —DanBarahona,HeadofMarketingatBizDevatAPIsec[6]
accountsandtheprofiletablestorestheprofileforeachuser.The
Inthissection,wefirstpresentthevulnerabilitycollectionpro-
twotablessharetheidenticalprimarykey,meaningtheprofileof
cessforourempiricalstudy,thenconductacomprehensivestudy
ausercanbequeriedfromtheprofiletableusingtheirkey.The
on101BOLAvulnerabilities.Thisstudyaimstoanswerthefollow-
tableforummanagesforums,andausercanparticipateinnone
ingquestions:whatobject-levelauthorizationmodelsarepresent
ormanyforums,asindicatedintheuser_forumtable.Eachuser
inreal-worldapplications,andwhataretherootcausesofBOLA
isgrantedtherole"manager"or"poster"intheirparticipating
vulnerabilities?
forums,whereamanagercandeleteforumnoticesandapostercan
createnewpostsormanagetheirownposts.Forumnoticesand
3.1 VulnerabilityCollectionandAnalysis
postsarestoredinthenoticetableandposttable,respectively.
Finally,thecommenttablestorescommentsandausercancomment WeconductedanempiricalstudyonBOLAvulnerabilities,analyz-
onpostswhosestatusisopen. ingdatafromtheCVEdatabase[1]andHuntrplatform[48]follow-
Figure3illustratesfourBOLAvulnerabilities,eachwithdistinct ingpreviousvulnerabilitystudies[47,52].Afterfilteringforopen-
rootcauses,manifestingindifferentAPIs. sourceapplicationswithvalidpatches,weidentified101BOLA
• TheAPIclose_post(Figure3(a))allowsuserstosetthe vulnerabilitiesforin-depthanalysis.Threeauthorsindependently
statusofagivenposttoClose.Avulnerabilityarisesbe- examinedeachvulnerability,annotatingtheauthorizationmodel,
causethisAPIdoesnotcheckwhethertherequesteristhe rootcause,andfix.Anydisagreementswereresolvedthroughdis-
ownerofthetargetpost.Consequently,anattackercanclose cussionsinvolvingafourthauthor.Thisprocesswascompleted
anypostatwill.Thefix(line10)involvesaddinganobject- overtwomonths.Foradetailedmethodologyanddiscussionof
levelauthorizationcheckintheSQLstatementtoconfirm
studylimitations,pleaserefertoourappendix1.
ownershipofthetargetpost.
3.2 AuthorizationModels
• TheAPIupdate_forum(Figure3(b))allowsaforummanager
toupdatethetopicofaforum.Thecheckatline2ensures
Finding1:Therearefourtypesofobject-levelauthorization
thattherequesterholdsthemanagerrole.However,despite
models,allofwhichcanbederivedbyreasoningaboutrelation-
performingthisrolecheck,theAPIdoesnotvalidatewhether
shipsbetweentablesfromimplicitforeignkeyreferences.
therequesterisamemberofthetargetforum.Thisoversight
leadstoaBOLAvulnerability,enablingamanagertoupdate
thetopicofanyforum.Thisvulnerabilityisaddressedby
implementinganobject-levelauthorizationcheckinlines 1https://github.com/BolaRay-d/BolaRay/blob/main/appendix-study.pdf
2936

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
Table	“profile” Table	“user” Table	“user_forum” Table	“forum”
| id phone  | birth    |     | id  | name  | pass        | role   | id userid | forumid |     | id topic   |
| --------- | -------- | --- | --- | ----- | ----------- | ------ | --------- | ------- | --- | ---------- |
|           |          | 1:1 |     |       |             | 1:m    |           |         | n:1 |            |
| 0 8972694 | 1/3/2001 |     | 0   | John  | ***         | poster | 0 0       | 1       |     | 0 Security |
| 1 8793571 | 3/7/1999 |     | 1   | David | *** manager |        | 1 1       | 0       |     | 1 Network  |
m:n
|                 |     |     | 1:n |              |     |     |     |     |                | 1:n |
| --------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | -------------- | --- |
| Table	“comment” |     |     |     | Table	“post” |     |     | n:1 |     | Table	“notice” |     |
id postid content id userid forumid title content status id forumid content
n:1
| 0   | 0 Good  |     | 0   | 0   | 1   | Net WEB | Close |     | 0   | 0 Good  |
| --- | ------- | --- | --- | --- | --- | ------- | ----- | --- | --- | ------- |
| 1   | 1 Great |     | 1   | 1   | 0   | Sec CCS | Open  |     | 1   | 0 Great |
Figure2:Tablesandandtheirrelationshipsinacontentmanagementsystem.
1 $pid = escape($_POST["pid"]); 1 $fid = escape($_POST["fid"]); 1 // same as Lines 1-9 in (b) 1 $pid = escape($_POST["pid"]);
2 …… 2 if ($role != "manager") {……} 2 $nid = escape($_POST["nid"]); 2 $cont= escape($_POST["cont"]);
3 $curr_user = $_SESSION["uid"]; 3 + $row = query("SELECTuserid 3 …… 3 ……
4 $role = getRole($curr_user, ……); 4 + FROM user_forum WHERE 4 + $row2 = query("SELECT 4 + $row = query("SELECTstatus
5 if ($role != "poster") { 5 + forumid = '$fid'"); 5 + forumid FROM notice 5 + FROM post WHERE id = '$pid'");
6 die("Not poster"); 6 + if (!in_array($curr_user, 6 +WHERE id = '$nid'"); 7 + if ($row[0] == "Close") {
7 }else { 7 + $row)) { 7 + if ($row2[0] != $fid) { 8 +   die("Post closed");
8 query("UPDATE postSET status 8 +   die("Not member in forum"); 8 +   die("Notice not found"); 9 + }
| 9 ="Close" WHERE id='$pid' |     |     | 9 + } |     |     | 9 + } |     |     | 10 …… |     |
| -------------------------- | --- | --- | ----- | --- | --- | ----- | --- | --- | ----- | --- |
10 +AND userid='$curr_user' 10 … 10 …… 11 query("INSERT INTO comment
11 "); 11 query("UPDATE forum SET topic 11 query("DELETE FROM notice 12 (postid, content) VALUES
12 } 12 = …… WHERE id = '$fid'"); 12 WHERE id = '$nid'"); 13 ('$pid', '$cont')");
(a) close_post.php (b) update_forum.php (c) delete_notice.php (d) add_comment.php
Figure3:FourexamplesofBOLAvulnerabilitiesfromFigure2.Lines1-9ofthecodesnippetin(b)hasbeeninlinedinthecode
snippetin(c).
them(1:n).Consequently,apostcanonlybedeletedbyitsowner,
| USER | 1:1 OBJECT | USER |     | 1:n OBJECT |     |     |     |     |     |     |
| ---- | ---------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- |
asexemplifiedinFigure3(a).
(a)	Ownership	model
|     |     |     |     |     |     | 3.2.2 Membershipmodel. |     | Inthismodel,therelationshipbetween |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | ---------------------------------- | --- | --- |
1:m n:1 usersandobjectsismodeledasmany-to-many(m:n),indicating
| USER | JUNCTION |     |     | OBJECT |     |     |     |     |     |     |
| ---- | -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
that(1)anobjectcanbeaccessedbyaspecificgroupofusers,and
(b)	Membership	model
|     |     |     |     |     |     | (2) a user | can have access | to  | multiple | objects. The relationship |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | -------- | ------------------------- |
USER 1/m:n OBJECT_P 1:n OBJECT_C 1:n … betweenauserandaforuminFigure2issuchanexample:auser
canparticipateinmultipleforums,andconversely,aforumcan
|          | (c)	Hierarchical	model |     |     |          |     | accommodatemultipleusers.                               |     |     |     |     |
| -------- | ---------------------- | --- | --- | -------- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
|          |                        | Y   |     |          |     | Tocapturethismembershiprelationship,ajunctiontable(such |     |     |     |     |
| OBJECT_A |                        |     |     | OBJECT_B |     |                                                         |     |     |     |     |
STATUS
|     |     | N   |     |     |     | asuser_foruminFigure2)isoftenintroducedtojointheusertable |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
(d)	Status	model andtheobjecttabletogether,establishingtheconnectionsbetween
Figure4:Fourdifferentobject-levelauthorizationmodels.
usersandobjects.
Figure4illustratesthefourauthorizationmodelsindatabase- Thismodelisacombinationofanown-
3.2.3 Hierarchicalmodel.
backedapplications.Thefirstthreemodelsdepictdistinctrelation-
shipsbetweenauserandanobject.Thelastmodel,namedthestatus ership or membership model with one or multiple parent-child
relationshipsbetweenobjects,whereaparentobjectcanownmul-
model,relatesanobjecttothestatusofanotherobject,suggesting
tiplechildobjects.Forinstance,inFigure2,auserownstheirpost,
thenecessitytorecognizethestatuscolumnindetectingviolations
andapostownsallcommentsonitself.Thus,theownerofapost
ofthisspecificmodel.
alsoindirectlyownsallcommentsonthatpost.Consequently,only
theownerofthepostcanmanipulatecommentsonit.Another
| 3.2.1 Ownershipmodel. | Theownershipmodelisperhapsthemost |     |     |     |     |     |     |     |     |     |
| --------------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
exampleinvolvestheusertable,theforumtable,andthenotice
studiedauthorizationmodel,whereinauserdirectlyownsanobject
table:ausercanmanageforumnotices(childobjectsofaforum)
ascharacterizedbyadirectone-to-one(1:1)orone-to-many(1:n)
onlyifheorsheisamemberofthatforum.
relationshipbetweentheuserandtheobject,ormorespecifically,
betweenausertableandanobjecttable.Underthismodel,anobject 3.2.4 Statusmodel. Inthismodel,objectspossessstatuses,and
canonlybemanipulatedbyitsowner.Forinstance,inFigure2,a usersareonlypermittedtoexecuteactionsonobjectswhentheyare
userownstheirpersonalprofile(1:1)andmultiplepostscreatedby inspecificstates.Forinstance,inFigure2,afterapostisclosedby
2937

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
Table1:Therootcausesandfixstrategies.
DAL
Rootcauses Codefix SQLfix Total Applications Specifications
MissingOwnershipCheck 38 25 63(62.37%)
MissingMembershipCheck 7 0 7(6.93%)
Inferring Object-Level
MissingHierarchicalCheck 9 0 9(8.91%) Authorization Models Detecting BOLA Vulnerabilities
MissingStatusCheck 22 0 22(21.78%)
Total 76(75.24%) 25(24.75%) 101 Building Database Schemas Locating Sensitive Operations
Vulnerability
itsowner,otherusersarebarredfromcommentingonit.Another
Reports
commonscenarioinvolvesitemsbecomingunavailableforpurchase Analyzing Table Relationships Collecting Conditional Checks
oncetheyhavebeenremovedfromtheshelves.
Identifying Authorization Models Hunting BOLA Vulnerabilities
3.3 RootCauses andFixes
Finding2:Eachauthorizationmodelisaccompaniedbyitsown Figure5:OverviewofBolaRay.
setofauthorizationrules.Violatinganyoftheserulesleadstoa Forinstance,inCVE-2022-0574,theflawedapplicationpub-
BOLAvulnerability.Inourstudy,allBOLAvulnerabilitiesstem lify–apublishingplatform–onlyverifiesthatthepostis
frommissingobject-levelauthorizationchecks,whichcanbead-
commentablewhenaddingcommentsonit,withoutcheck-
dressedbyaddingchecksinthesourcecode(75.24%)orinSQL ingwhetherthepostisindraftstateornot.Toprecisely
statements(24.75%). detectsuchvulnerabilities,itisnecessarytoidentifyallre-
quiredstatuschecksforaspecificoperation,whichisquite
As shown in Table 1, all BOLA vulnerabilities are caused by challenging.Acautiousapproachistorequireallstatusesof
missingdistincttypesofobject-levelauthorizationchecks: anobjecttobechecked,whichensuressafetybutmayresult
• Missingownershipchecksarisesbecauseanapplicationfails infalsepositives.However,asshowcasedinSection5,we
didnotencoutersuchfalsepositivesinourexperiments.
toverifywhetherthecurrentuserisindeedtheownerof
theobjectbeingaccessed.Figure3(a)isanexamplewhere
Allstudiedvulnerabilitieswerefixedbyaddingextraobject-level
theownershipofthetargetpostisnotproperlychecked.
authorizationchecks:75.24%offixesintroducedextrachecksin
• Missingmembershipchecksiscausedbythelackofcheck
thesourcecode,and24.75%ofvulnerabilitieswereaddressedby
onwhetherarequesterbelongstothegroupauthorizedto
introducingextrachecksintheWHEREclausesofcorresponding
operateonaspecificobject.ThevulnerabilityinFigure3(b)
SQLstatements.Incode-basedfixes,datastoredindatabaseta-
issuchanexample,duetothefactthattheapplicationfails
blesareretrievedintoprogramvariablesviaSQLstatements,and
toconfirmiftherequesterisamemberofthetargetforum.
object-levelauthorizationisperformedbycheckingthosevariables
• Missinghierarchicalcheckscanbetriggeredbymissingown-
inconditionalstatements.Suchafixingstrategyissuitableforcom-
ership or membership checks, or by the lack of a check
plexauthorizationmodels,whichofteninvolvemultiplesub-checks,
againsttheparent-childrelationshipbetweendistinctob-
includingthehierarchicalmodel(Figure3(c))andthestatusmodel
jects.Thehierarchicalauthorizationmodelisoftenrealized
(Figure3(d)).Ontheotherhand,SQL-basedfixesdirectlypatchex-
throughmultiplesub-checkswhichrespectivelyverifyown-
istingSQLquerieswithadditionalpredicatesintheirWHEREclauses.
ershipormembershipofcorrespondingobjectsandthere-
Thisapproachisoftenfavoredinrelativelysimpleauthorization
lationshipbetweenparentobjectsandchildobjects.Any
models,suchastheownershipmodel(Figure3(a)).Conversely,to
missingsub-checkscanleadtoincompleteauthorization.
detectsuchvulnerabilities,weneedtoidentifytheauthorization
Forinstance,inFigure3(c),inadditiontoverifyingthemem-
modelforeachobjectaccessandfurtherverifywhethertheobject-
bershipbetweentherequesterandtheforum,theapplication
levelauthorizationchecksare properlyimplementedinboththe
needstofurtherensurethatthetargetnoticeisachildofthe
sourcecodeandSQLstatements.
targetforum.Thetwovulnerabilities,CVE-2021-4194and
Huntr-e6144554,aretriggeredinthesamefashion,i.e.,miss-
4 BolaRay
ingchecksforparent-childrelationships.Hence,toavoid
suchvulnerabilities,weneedtoensurethatallrequiredsub- Itisvitalthatwecheckallobjectsandthatwecheckthemforread,
checkshavebeenenforced. updateanddeleteactions.Weneedtocheckeveryfunctionalitythat
• Missingstatuschecksoccursbecausetheapplicationdoes
hasaccesstotheseobjects.
notverifythecurrentstatusofanobjectbeforeperforming
—StepanIlyin,Verifiedexpertfromwallarm[17]
specificoperations.ThisissueisexemplifiedinFigure3(d),
where,despitethetargetpostbeingclosed,theoversightin In light of our empirical study, we propose BolaRay, a new
checkingthetargetpost’sstatusenablesattackerstoleave BOLAvulnerabilitydetectiontool.AsdepictedinFigure5,thetool
commentsundesirably.Itisimportanttonotethatmultiple comprisestwoprimarymodules.Thefirstmoduleautomaticallyin-
statuschecksmayberequiredtosafelyperformanopera- fersobject-levelauthorizationmodelsinthreesteps.Subsequently,
tion.Inourstudy,fourvulnerabilities–CVE-2022-0170,CVE- thesecondmoduledetectsBOLAvulnerabilitiesbyverifyingthat
2022-0574,CVE-2022-0726,andCVE-2022-0727–arecaused thesetofchecksforanobjectaccessenforcestheauthorization
bycheckingonlyonestatusvariablewhileignoringothers. modelofthatobject.
2938

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
|      |             |     |         |         |        |     | Program | 𝑝   | ::= 𝑇;𝑠;𝑣            |     |         |                   |     |
| ---- | ----------- | --- | ------- | ------- | ------ | --- | ------- | --- | -------------------- | --- | ------- | ----------------- | --- |
|      | columns     |     | primary | foreign | unique |     |         |     |                      |     |         |                   |     |
| name |             |     |         |         |        |     |         | 𝑇   | ::= 𝑡 {𝑐;𝑐𝑝;(𝑐       |     | :𝑡);𝑐𝑢} |                   |     |
|      | name & type |     | key     | keys    | keys   |     | Tables  |     |                      | 𝑓   |         |                   |     |
|      |             |     |         |         |        |     |         | 𝑠   | 𝑙C :⟨𝑘,𝑡,𝑐,(𝑐,𝑣)⟩|𝑙C |     |         | :𝑣 ←⟨𝑘,𝑡,𝑐,(𝑐,𝑣)⟩ |     |
user [(id, int[4]), (name, char[20]), …] id [] [id] Statements ::=
|                                             |     |     |     |              |      |     | Keywords  | 𝑘   | ::= SELECT|DELETE|INSERT|UPDATE |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ------------ | ---- | --- | --------- | --- | ------------------------------- | --- | --- | --- | --- |
| profile [(id, int[4]), (phone, int[11]), …] |     |     | id  | [(id::user)] | [id] |     |           |     |                                 |     |     |     |     |
|                                             |     |     |     |              |      |     | Variables | 𝑣   | ::= 𝑥                           |     |     |     |     |
forum [(id, int[4], (topic, char[20]), …] id [] [id] C 𝑡 ::𝑐|(𝑡 ::𝑐,𝑡 ::𝑐)
|     |     |     |     |     |     |     | Checks |     | ::= |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
𝑡,𝑐,𝑥
| …   | …   |     | …   | …   |     | …   | Identifiers |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Locations   | 𝑙   |     |     |     |     |     |
Figure6:TheschemaofourexampleinFigure2.
Figure7:Domainsusedinformalism.
4.1 InferringObject-LevelAuthorizationModels
𝑙C:⟨−,𝑡,−,(𝑐,𝑣)⟩
[Key-value]
GuidedbyFinding1,weautomaticallyinferobject-levelautho- (𝑙,𝑡::𝑐,𝑣) ∈Binding
rizationmodelsinthreesteps:thefirststepconstructsadatabase
𝑙C:𝑣←−⟨SELECT,𝑡,𝑐,−⟩
schemafromtablecreationstatements;thesecond,alsothekey
|     |     |     |     |     |     |     |     | (𝑙,𝑡::𝑐,𝑣) | ∈Binding |     |     |     | [Select] |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- | -------- |
step,derivestablerelationshipsbyanalyzingimplicitforeignkey
| references; | and the third | step | infers authorization |     | models | from |               |     |                  |          |              |     |     |
| ----------- | ------------- | ---- | -------------------- | --- | ------ | ---- | ------------- | --- | ---------------- | -------- | ------------ | --- | --- |
|             |               |      |                      |     |        |      | (𝑙 ,𝑡 1::𝑐𝑝,𝑣 | ) ∈ | B i n d in g ( 𝑙 | , 𝑡 𝑐 ,  | 𝑣 ) ∈Binding |     |     |
|             |               |      |                      |     |        |      | 1             | 1   |                  | 2 2: : 2 | 2            |     |     |
thesetablerelationships. 𝑣 al ia se s t o 𝑣 𝑙 d o m i n a t e s 𝑙 [Connect]
|     |     |     |     |     |     |     |     | 1   | 2 1                   |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | (𝑡  | ,𝑡 2::𝑐 ) ∈ForeignKey |     |     |     |     |
4.1.1 Building Database Schemas. Given a database-backed ap- 1 2
Figure8:Rulesforforeignkeyanalysis.
plication,webuildthedatabaseschemabyconsideringalltable
creationstatementsinthisapplication.Tablecreationstatements oncolumn𝑐 oftable𝑡
2 2,itisastrongindicationoftheforeign
| specifythename,columns,andkeysofeachtable.Thesestate- |     |     |     |     |     |     | key(𝑡 ,𝑡 | 2::𝑐                                           |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|                                                       |     |     |     |     |     |     | 1        | 2 ).Toaddressthis,wedesignasetofrigorousrules, |     |     |     |     |     |
mentsmaybedeclared inSQLscripts (.sqlfiles)orincorporated whichwillbediscussedshortly,toderivethesetofforeignkeys.
intosourcecode,eitherasdirectquerystringsorthroughdatabase Forillustrativepurposes,Figure7presentsthedomainusedin
manipulationAPIsprovidedbytheunderlyingDataAccessLayer ourformalism.Aprogram𝑝 consistsofasetoftables𝑇,asetof
(DAL)framework.Section4.3willprovideadetailedexplanation statements𝑠,andasetofprogramvariables𝑣.Atable𝑡 consists
ofhowtablecreationstatementsandotherSQLstatementsare ofasetofcolumns𝑐,where𝑐 ∈𝑐isthecolumnforprimarykey;
𝑝
handled. (𝑐 :𝑡)isthesetofschema-declaredforeignkeys,wherecolumn
𝑓
The schema summarizes all tables managed by the database. 𝑐 ∈𝑐referstotheprimarykeyofanothertable;𝑐 denotestheset
|     |     |     |     |     |     |     | 𝑓   |     |     |     |     | 𝑢   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure6showstheschemaofourexampleinFigure2.Forsimplicity, ofuniquekeys𝑐 ∈𝑐.
𝑢
notalltablesaregiven.Eachtablehasauniquenameandconsists of𝑙𝐶 ⟨𝑘,𝑡,𝑐,(𝑐′,𝑣′)⟩
|                                                       |     |     |     |     |     |     | A SQL | statement𝑠       | takes    | the form |               | :   | or           |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | -------- | -------- | ------------- | --- | ------------ |
| ofasetofcolumnsintheformof<name,type>.Theprimarykeyis |     |     |     |     |     |     | 𝑙𝐶    |                  |          |          |               |     |              |
|                                                       |     |     |     |     |     |     | : 𝑣 ← | ⟨𝑘,𝑡,𝑐,(𝑐′,𝑣′)⟩, | denoting |          | the statement |     | at location𝑙 |
thecolumnuniquelyindexingthetable,foreignkeysdeclarethose appliesaqueryoperation𝑘totable𝑡 with𝑐asthetargetcolumn
columnsthatrefertotheprimarykeysofothertables,andunique (onlywhen𝑘 isaSELECToperation),and𝑣 holdingtheresulting
| keysarethosecolumnsthatcanonlycontainuniquevalues. |            |          |            |      |              |     |             |      | location𝑙 |         |      |        |              |
| -------------------------------------------------- | ---------- | -------- | ---------- | ---- | ------------ | --- | ----------- | ---- | --------- | ------- | ---- | ------ | ------------ |
|                                                    |            |          |            |      |              |     | value. Note | that | is        | guarded | by a | set of | checks C (to |
| Relationships                                      | explicitly | declared | as foreign | keys | are directly |     |             |      |           |         |      |        |              |
becomputedinSection4.3),whereeachcheckeithervalidatesa
encodedintheschema.Forinstance,inFigure6,theprimarykey
|     |     |     |     |     |     |     | column𝑡 | ::𝑐 orcomparestwocolumns(𝑡 |     |     | ::𝑐,𝑡 | ::𝑐).Finally,the |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | ----- | ---------------- | --- |
oftableprofileisalsoaforeignkeyreferringtothetableuser,
|            |                    |     |           |          |       |          | pair (𝑐′,𝑣′)    | relatescolumn𝑐′ |     | tovariable𝑣′,asillustratedinthe |     |     |     |
| ---------- | ------------------ | --- | --------- | -------- | ----- | -------- | --------------- | --------------- | --- | ------------------------------- | --- | --- | --- |
| reflecting | the 1-to-1 mapping |     | between a | user and | their | profile. | followingcases: |                 |     |                                 |     |     |     |
However,theforeignkeysforothertablesaresettoempty,and
| theirrelationshipsneedtobeinferredinthenextstep. |     |     |     |     |     |     |                                     |     |     |     |     |       | 𝑐′ 𝑣′",or |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ----- | --------- |
|                                                  |     |     |     |     |     |     | • Key-valuepairsinaWHEREclause:"... |     |     |     |     | WHERE | =         |
4.1.2 AnalyzingTableRelationships. Thecruxofdeducingtablere- "... WHERE 𝑐′ IN 𝑣′".
|     |     |     |     |     |     |     | • Key-valuepairsinanUPDATEoperation:"UPDATE |     |     |     |     |     | ... SET |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ------- |
lationshipsliesinpreciselyidentifyingimplicitforeignkeys,which
|     |     |     |     |     |     |     | 𝑐′  | = 𝑣′ ...". |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
arecolumnsthatrefertotheprimarykeysofothertables.Dueto
|     |     |     |     |     |     |     | • Key-valuepairsinanINSERToperation:"INSERT |     |     |     |     |     | INTO ... |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | -------- |
variousreasons[18],theseforeignkeysoftenarenotdeclaredinthe
|     |     |     |     |     |     |     | (𝑐′, |     | (𝑣′, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- |
schemabutinsteadimplementedinthesourcecode.Withoutloss ...) VALUES ...)".
ofgenerality,wehereafterassumethataforeignkeycontainsonly
|     |     |     |     |     |     |     | A SQL query | containing | multiple | such | pairs | is normalized | into |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | ---- | ----- | ------------- | ---- |
onecolumn.Ourformulationcanbeeasilyextendedtosupport
multiplestatements,oneforeachpair.Forexample,aSQLstatement
caseswithmultiplecolumnsconstitutingaforeignkey.
|                                 |          |                                      |                         |           |          |     | 𝑙:"UPDATE                                               | comment   | SET pid  | = $p      | WHERE    | status   | = $s"is  |
| ------------------------------- | -------- | ------------------------------------ | ----------------------- | --------- | -------- | --- | ------------------------------------------------------- | --------- | -------- | --------- | -------- | -------- | -------- |
|                                 | (Foreign | key).                                | A foreign               | key takes | the form | of  |                                                         |           |          |           |          |          |          |
| Definition                      | 1.       |                                      |                         |           |          |     | representedbytwostatements:𝑙                            |           |          |           |          |          |          |
|                                 |          |                                      |                         |           |          |     |                                                         |           |          | :⟨UPDATE, |          | comment, | -, (pid, |
| (𝑡 ,𝑡 2::𝑐2),wherecolumn𝑐       |          | oftable𝑡                             | referstotheprimarykeyof |           |          |     |                                                         |           |          |           |          |          |          |
| 1                               |          | 2                                    | 2                       |           |          |     | $p)⟩and𝑙                                                | :⟨UPDATE, | comment, | -,        | (status, | $s)⟩.    |          |
| table𝑡 .Thenotation𝑡            |          | ::𝑐isusedtodenotecolumn𝑐oftable𝑡,and |                         |           |          |     |                                                         |           |          |           |          |          |          |
| 1                               |          |                                      |                         |           |          |     | Forclarity,Figure7considersonlydatabasequerystatements. |           |          |           |          |          |          |
| itissimplywrittenas𝑐ifthetable𝑡 |          |                                      | isunderstood.           |           |          |     |                                                         |           |          |           |          |          |          |
Thosestatementsconcerningdataandcontrolflowsareprocessed
Identifyingimplicitforeignkeyscanbechallengingsincesuch inaseparateanalysis,tocomputedataandcontroldependencies,
informationliesinthecomplexinteractionbetweensourcecodeand asdetailedinSection4.3.Priortoexploringthespecificrulesfor
databaseoperations.Forinstance,ifavariableholdingaprimary determiningforeignkeys,letusfirstintroducethetwofollowing
| keyvalueoftable𝑡 | 1isusedinaWHEREclauseofasubsequentquery |     |     |     |     |     | sets: |     |     |     |     |     |     |
| ---------------- | --------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2939

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
(𝑡 1 ,𝑡 2::𝑐 2)∈ForeignKey (𝑡 3 ,𝑡 2::𝑐 ′)∈ForeignKey ourexampleinFigure2,similartothejunctiontableuser_forum,
|     | (𝑡 ,𝑡 3::−)∉F | o r e | i gn K e y    | ( 𝑡 ,𝑡 :: −    | 2 ) ∉ForeignKey |           |                                                      |     |     |     |     |     |     |     |
| --- | ------------- | ----- | ------------- | -------------- | --------------- | --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 1             |       |               | 3 1            |                 |           | thetablepostalsocontainstwoforeignkeysuserid:userand |     |     |     |     |     |     |     |
|     |               | ( 𝑡 2 | , − :: − ) ∉F | o r e ig n K e | y               | [M-N-Rel] |                                                      |     |     |     |     |     |     |     |
|     |               | (𝑡 ,𝑡 | 2::𝑐 ,𝑡 ,𝑡    | 2::𝑐 ′)∈MNR    |                 |           |                                                      |     |     |     |     |     |     |     |
Step1: 1 2 3 2 forumid:forum.However,thistableisnotconsideredajunction
𝑡 2∈JunctionTable
tablesinceitisalsoreferencedbytheforeignkeycomment:postid.
(𝑡 ,𝑡2::𝑐 ,𝑡 ,𝑡 𝑐 ′ ) ∈ M N R ( 𝑡 ,𝑡 𝑐 ,𝑡 ,𝑡 4::𝑐 ′)∈MNR T h e ru l e [ M - N - R e l - R ] r ecursivelydeducem:nrelationshipstohan-
|     | 1   | 2 3 2: : 2 |            | 3 4 ::         | 4 5 4 | [M-N-Rel-R] |          |                  |                |     |     |     |     |     |
| --- | --- | ---------- | ---------- | -------------- | ----- | ----------- | -------- | ---------------- | -------------- | --- | --- | --- | --- | --- |
|     |     | ( 𝑡 , 𝑡    | :: 𝑐 ,𝑡 ,𝑡 | 4: : 𝑐 ′ ) ∈ M | N R   |             | dl e m u | l ti p le - ta b | l e j o in s . |     |     |     |     |     |
|     |     | 1          | 2 2 5      | 4              |       |             |          |                  |                |     |     |     |     |     |
Therulesfor1:1([1-1-Rel])and1:n([1-N-Rel])relationships
(𝑡 1 ,𝑡 2::𝑐𝑢)∈F o r e i g n K e y 𝑡 2 ∉ JunctionTable a re s e l f-e x p la na to r y . T h e y ar e d is ti n gu i s h e d b a se d o n w h e th e r t h e
|     |     |     | ( 𝑡 , 𝑡 𝑐𝑢 | ) ∈O O R |     | [1-1-Rel] |     | 𝑡   | 𝑐   |     |     |     |     |     |
| --- | --- | --- | ---------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2 : : fo re i g n k e y 2 :: 2 i s u n i qu e .I t is i m p o r t a nt t o r ec a ll th a t a j u n c -
Step2: 2)∈ForeignKey tiontableissolelyintroducedtojointwoothertablesanditdoes
|     |     | (𝑡 1 ,𝑡 2::𝑐 |     | 𝑐 2∉𝑡 | 2::𝑐𝑢 |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡 2∉JunctionTable [1-N-Rel] notstoreactualobject;thus,alljunctiontablesareexcludedfrom
(𝑡 1 , 𝑡 2 :: 𝑐 2) ∈ ON R consideration(indicatedby𝑡 ∉ JunctionTable)whenderiving
|     | Figure9:Rules |     | f o r t a | b le re lationanalysis. |     |     |     |     |     | 2   |     |     |     |     |
| --- | ------------- | --- | --------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1:1and1:nrelationships.
Binding,asetoftriplesintheformof
|     | •   |     |     |     | (𝑙,𝑡 | ::𝑐,𝑣),which |                                       |     |     |     |                          |     |     |     |
| --- | --- | --- | --- | --- | ---- | ------------ | ------------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- |
|     |     |     |     |     |      |              | 4.1.3 IdentifyingAuthorizationModels. |     |     |     | Figure10outlinestherules |     |     |     |
meansthatprogramvariable𝑣mayholdvaluesfromcolumn
forinferringauthorizationmodels.Beforedivingintoitsdetails,
𝑡 ::𝑐duetothestatementatlocation𝑙.
wefirstintroducefouradditionalsetsUserTable,OwnerModel,
• ForeignKey,asetofforeignkeys(Definition1)intheform
MemberModel,andStatusModel,asexplainedbelow:
|     | (𝑡 ,𝑡 2::𝑐 |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 1 2        | ).  |     |     |     |     |     |     |     |     |     |     |     |     |
• UserTable,asetofusertables.
Figure8outlinestherulesfordeducingforeignkeys.Specifically, OwnerModel,asetoftuplesintheformof (𝑡 ,𝑡 𝑐
(𝑙,𝑡 ::𝑐,𝑣) Bindingifatleastoneofthefollowingconditions • 1 2 :: 2 ),
|       | ∈               |        |       |             |     |                |                                         |     |     |     |     |       | 2(OORor |     |
| ----- | --------------- | ------ | ----- | ----------- | --- | -------------- | --------------------------------------- | --- | --- | --- | --- | ----- | ------- | --- |
|       |                 |        |       | statement𝑙𝐶 |     |                | signifyinga1:1or1:nrelationshipbetween𝑡 |     |     |     |     | 1and𝑡 |         |     |
| holds | true: (1) there | exists | a SQL |             | :   | ⟨−,𝑡,−,(𝑐,𝑣)⟩, |                                         |     |     |     |     |       |         |     |
ONR),whichformsthefoundationofanownershipmodel.
wherethepair(𝑐,𝑣)relatescolumn𝑐tovariable𝑣([Key-value]),
|     |     |     |     |     |     |     | • MemberModel, |     |     | a set of tuples | in  | the form | of (𝑡 | ,𝑡 :: |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------------- | --- | -------- | ----- | ----- |
includingthreecasesasdiscussedabove.(2)𝑣receivesresultsfrom 1 2
|                                                 |     |       |     |     |     |     | 𝑐         | ,𝑡 ,𝑡 ′ ::𝑐 | ′),signifyingam:nrelationship(MNR)inthe |     |     |     |     |     |
| ----------------------------------------------- | --- | ----- | --- | --- | --- | --- | --------- | ----------- | --------------------------------------- | --- | --- | --- | --- | --- |
| column𝑐(oftable𝑡)viaSELECTstatements([Select]). |     |       |     |     |     |     |           | 2 3 2       | 2                                       |     |     |     |     |     |
|                                                 |     | 𝑡 , 𝑡 | 𝑐   |     |     |     | sameform. |             |                                         |     |     |     |     |     |
I n [ C o n n e c t ] , ( 1 2 : : 2 ) i s r e g a r d e d a s a f o r e i g n k e y i f t h e S t a t u s M o d e l (𝑡 , 𝑡 𝑐 , 𝑡 𝑐 ′
|     |     |     |     |     |     |     | •   |     | , a s | et o f t r i p l e | s lik e | 1 2 : : 2 | 1 : : | ), d e - |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------------ | ------- | --------- | ----- | -------- |
b i n d i n g v a r i a b l e 𝑣 1 o f 𝑡 1 : : 𝑐 𝑝 ( i .e . , ( 𝑙 1 , 𝑡 1 : : 𝑐 𝑝 , 𝑣 1 ) ∈ B i n d i n g ) 1
|     |     |     |     |     |     |     | n   | o t i n g a | 1: 1 o r 1 : n | r e la t i o n s h | ip b e t w | e e n 𝑡 a n | d 𝑡 , a | n d t h e |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------------ | ---------- | ----------- | ------- | --------- |
a l i a s e s t o t h e b i n d i n g v a r i a b l e 𝑣 o f 𝑡 : : 𝑐 ( i. e . , ( 𝑙 , 𝑡 : : 𝑐 , 𝑣 ) ∈ 1 2
|     |     |     |     | 2 2 | 2 2 | 2 2 2 | c   | o l u m n 𝑡 | : : 𝑐 ′ s i g | n i fi e s a s t a t | u s v a l u | e . |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----------- | ------------- | -------------------- | ----------- | --- | --- | --- |
B i n d i n g ) , i n d ic a t in g t h a t 𝑡 2 : : 𝑐 2 r e f e r s t o t h e p r i m a r y k e y o f 𝑡 . 1 1
1
Forsimplicity,wehavenotintroducedsetsforhierarchicalmodels,
Tofilterfalseforeignkeys,inspiredby[8],wealsorequirethat
whichbyconstruction,canbecomputedbyjoiningthesetOwn-
thetwoinvolvingstatementsneedtobeexecutedtogether.This
dominance relationship erModel or MemberModel with OOR and ONR.For detailed
| requirement | is approximated |     | by  | the |     | [3] |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
informationonhierarchicalmodels,pleaserefertoourappendix2.
| betweenthetwostatements,i.e.,𝑙 |     |     |     | 1dominates𝑙 | 2.  |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Next,Figure9computestablerelationshipsbasedondeduced The first two rules in Figure 10 are used to compute user
foreignkeys.Wefurtherdefinefoursets,OOR,ONR,MNRand tables.Asacommonpractice,thecurrentuserIDisstoredinthe
JunctionTable,asfollows: global session for future authorization purposes. Consider the
|     |                                     |     |     |     |     |              | following                                              | code | snippet | as an example: | after | a user | logs in, | the |
| --- | ----------------------------------- | --- | --- | --- | --- | ------------ | ------------------------------------------------------ | ---- | ------- | -------------- | ----- | ------ | -------- | --- |
|     | • OOR(ONR),asetofpairsintheformof(𝑡 |     |     |     | ,𝑡  | 2::𝑐 ),which |                                                        |      |         |                |       |        |          |     |
|     |                                     |     |     |     | 1   | 2            | userIDisstoredintheglobalvariable$_SESSION["uid"](line |      |         |                |       |        |          |     |
meansthatthereisa1:1(1:n)relationshipbetween𝑡
1and
|     |                                     |     |        |          |             |             | 4), which | is then | accessible | from anywhere |     | in the | source | code. |
| --- | ----------------------------------- | --- | ------ | -------- | ----------- | ----------- | --------- | ------- | ---------- | ------------- | --- | ------ | ------ | ----- |
|     | 𝑡 2,and𝑐 2isaforeignkeyreferringto𝑡 |     |        |          | 1.          |             |           |         |            |               |     |        |        |       |
|     | • JunctionTable,                    | a   | set of | junction | tables used | to join two |           |         |            |               |     |        |        |       |
1 $row= query("SELECT idFROM userWHERE name='$name'
tablestogether,asutilizedinam:nrelationship.
AND pass='$pass'");
|     | • MNR,asetoftuplesintheformof(𝑡          |     |     |     | ,𝑡 ::𝑐 | ,𝑡 ,𝑡 ′ ::𝑐 ′), |                     |                      |     |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | ------ | --------------- | ------------------- | -------------------- | --- | --- | --- | --- | --- | --- |
|     |                                          |     |     |     | 1 2    | 2 3 2 2         | 2 if ($row == null) |                      |     |     |     |     |     |     |
|     | denotingthem:nrelationshipbetweentables𝑡 |     |     |     |        | 1and𝑡           |                     |                      |     |     |     |     |     |     |
|     |                                          |     |     |     |        | 3:the           | 3                   | die("Invalid user"); |     |     |     |     |     |     |
twotablesarejoinedthroughoneormorejunctiontables, 4 $_SESSION["uid"] = $row[0];
|     | 𝑡 ,...,𝑡 ′ ,with𝑡 |     | ::𝑐 and𝑡 | ′ ::𝑐 | ′ being theforeignkeys |     |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | -------- | ----- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 2 2 2 2 2 Inlightofthisheuristic,therule[User-Table]constructsan
|     | referencing𝑡 | 1and𝑡 | 3,respectively.Inthesimpletwo-table |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | ----- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
initialsetofusertablesinUserTable.Wefurtherextendtheset
|     | joincase,𝑡 | 2and𝑡 ′ | arethesame. |     |     |     |                                                         |     |     |     |     |     |     |     |
| --- | ---------- | ------- | ----------- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |            | 2       |             |     |     |     | UserTablewithrule[User-Ext],whichalsoregardsthosetables |     |     |     |     |     |     |     |
TherulesinFigure9areprocessedthroughtwodistinctsteps.
asusertablesiftheyhavea1:1relationshipwithanexistinguser
Initially,therules[M-N-Rel]and[M-N-Rel-R]are exclusively table.Asaresult,inourexampleinFigure2,theprofiletableis
appliedtodeducem:nrelationshipsandtocalculatejunctiontables. alsoconsideredasausertable.
Subsequently,inthesecondstep,thesejunctiontablesfacilitatethe Thenexttworules,[Own-Model]and[Mem-Model],inferthe
applicationofthetworules[1-1-Rel]and[1-N-Rel]. ownershipmodelandmembershipmodel,respectively,whichare
In[M-N-Rel],them:nrelationshipbetween𝑡 and𝑡 iscon- self-explanatory.Therule[Stat-Model]reliesontherecognition
|     |     |     |     |     | 1   | 3   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cludedonlyifthefollowingconditionsaremet:1)𝑡 and𝑡 ofstatuscolumns.Weconsiderthatcolumn𝑡 ::𝑐isastatuscolumn
|     |     |     |     |     |            | 1 3 are |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | (𝑡  | ,𝑡  | ForeignKey |         |     |     |     |     |     |     |     |     |
not directly related, meaning 1 3 :: −) ∉ and ifallthefollowingconditionsaremet:
ForeignKey;and2)𝑡
| (𝑡 3 ,𝑡 | 1 :: −) ∉ |     |     | 2 isintroducedsolelytojoin |     |     |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡 and𝑡 together, indicated by (𝑡 ,− :: −) ∉ ForeignKey. In 2https://github.com/BolaRay-d/BolaRay/blob/main/appendix-hm.pdf
| 1   | 3   |     |     | 2   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2940

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
(−,𝑡::𝑐,𝑣) ∈Binding 𝑣aliasesto𝑣′ 𝑙C:⟨DELETE,𝑡 1 ,−,−⟩ 𝑡 1 ∈UserTable
|     | 𝑣′isstoredintheglobalsession |              |     |              |     |     |     |        | 𝑡 2::𝑐       |     |     |             |     |
| --- | ---------------------------- | ------------ | --- | ------------ | --- | --- | --- | ------ | ------------ | --- | --- | ----------- | --- |
|     |                              |              |     | [User-Table] |     |     |     |        | 2            | ∈ C |     | [Admin-Col] |     |
|     |                              | 𝑡 ∈UserTable |     |              |     |     |     | 𝑡 2::𝑐 | ∈AdminColumn |     |     |             |     |
2
|     | 𝑡 ∈UserT | a bl | e (𝑡 , 𝑡 :−) ∈OOR |            |     |     |     | 𝑙C ⟨ − , 𝑡 | ,− , − ⟩ | 𝑡 𝑐          | ∈ C |               |     |
| --- | -------- | ---- | ----------------- | ---------- | --- | --- | --- | ---------- | -------- | ------------ | --- | ------------- | --- |
|     | 1        |      | 1 2 :             |            |     |     |     | :          | 2        | 1 : : 1      |     |               |     |
|     |          | 𝑡 ∈  | Use r T a bl e    | [User-Ext] |     |     |     | 𝑡 : :𝑐     | ∈ A d m  | in C o l u m | n   |               |     |
|     |          | 2    |                   |            |     |     |     | 1 1        |          |              |     | [Admin-Check] |     |
𝑙C ∈SafeOp
|     | 𝑡 ∈UserTable | (𝑡           | ,𝑡 2::𝑐 ) ∈ (OOR∪ONR) |             |     |     |         |            |               |              |       |             |     |
| --- | ------------ | ------------ | --------------------- | ----------- | --- | --- | ------- | ---------- | ------------- | ------------ | ----- | ----------- | --- |
|     | 1            |              | 1 2                   | [Own-Model] |     |     |         |            |               |              |       |             |     |
|     |              | (𝑡 ,𝑡 2::𝑐   | ) ∈OwnerModel         |             |     |     |         | (𝑡 ,𝑡 2::𝑐 | ) ∈OwnerModel |              |       |             |     |
|     |              | 1 2          |                       |             |     |     |         | 1          | 2             |              |       |             |     |
|     |              |              |                       |             |     |     | 𝑙C:⟨−,𝑡 | ,−,−⟩      | (𝑡            | 1::𝑐𝑝,𝑡 2::𝑐 | ) ∈ C | [Own-Check] |     |
|     |              |              |                       |             |     |     |         | 2          |               |              | 2     |             |     |
|     |              | 𝑡 ∈UserTable |                       |             |     |     |         |            | 𝑙C ∈SafeOp    |              |       |             |     |
1
|     | (𝑡  | 1 ,𝑡 2::𝑐 2 ,𝑡 | 3 ,𝑡 ′::𝑐 ′) ∈MNR | [Mem-Model] |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 2
(𝑡 1 ,𝑡 2::𝑐 2 ,𝑡 3 ,𝑡 ′::𝑐 ′) ∈MemberModel (𝑡 1 ,𝑡 2::𝑐 2 ,𝑡 3 ,𝑡 ′::𝑐 ′) ∈MemberModel
|     |     | 2   | 2   |     |     |     |     | C   | 2 2      |           |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 𝑙   | :⟨ −,𝑡 3 | , − , − ⟩ |     |     |     |
(𝑡 ,𝑡 2::𝑐 (OOR∪ONR) (𝑡 1::𝑐𝑝,𝑡 2::𝑐 (𝑡 :𝑐 𝑝,𝑡 ′::𝑐 ′) [Mem-Check]
|     |       | 1 2                     | ) ∈             |              |     |     |     | 2 ) | ∈ C        | 3 : | ∈   | C   |     |
| --- | ----- | ----------------------- | --------------- | ------------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |       | 𝑡 1::𝑐 ′isastatuscolumn |                 |              |     |     |     |     | 𝑙C ∈SafeOp |     | 2 2 |     |     |
|     |       | 1                       |                 | [Stat-Model] |     |     |     |     |            |     |     |     |     |
|     | (𝑡 ,𝑡 | 2::𝑐 ,𝑡 1::𝑐            | ′) ∈StatusModel |              |     |     |     |     |            |     |     |     |     |
|     | 1     | 2                       | 1               |              |     |     |     |     |            |     |     |     |     |
Figure10:Rulesforauthorizationmodelinference. (𝑡 ,𝑡 2::𝑐 ,𝑡 1::𝑐 ′) ∈StatusModel
|     |                                                   |     |     |     |     |     |     | 1 2     | 1        |         |     |              |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | --- | ------------ | --- |
|     |                                                   |     |     |     |     |     |     | 𝑙C:⟨−,𝑡 | ,− ,− ⟩  | 𝑡 ::𝑐 ′ | ∈ C | [Stat-Check] |     |
|     | 𝑐holdsatypewithasmallrangeofvalues,suchasBOOLEAN, |     |     |     |     |     |     |         | 2        | 1 1     |     |              |     |
| (1) |                                                   |     |     |     |     |     |     |         | 𝑙 C ∈ Sa | feO p   |     |              |     |
TINYINT(1),orENUM.Thisconditionensuresthatthenum- Figure11:Rulesforcheckingsafetyofsensitiveoperations.
berofstatesrepresentedby𝑐isfiniteandenumerable.For
example,thestatuscolumnofthetablepostinFigure2 ofthefourauthorizationmodelsdiscussedpreviously.Wehaveob-
canonlyhavetwovalues:OpenorClose. servedthatverifyingwhetherthecurrentuserisanadministrator
𝑐 that𝑐 ofteninvolvesspecificcolumns,termedadmincolumns.Inthiscon-
| (2) | is modifiable, |     | which ensures | can be | dynamically |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ------------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
text,weinitiallyidentifythesetofadmincolumns,AdminColumn,
changedbytheapplication.
byapplyingthe[Admin-Col]rule.Specifically,westartbyidenti-
(3) 𝑐isusedtocontrolthevisibilityorbehaviorofdatapresented
fyingprivilegedoperationsthatrequireadministratorpermissions,
totheuserbythefrontend,asshowninline2inthecode
snippetbelow.Notethatthisconditionisspecifictoweb which,inourimplementation,arethoseDELETEoperationsona
usertable.Then,foraprivilegedoperation𝑙C
|     |     |     |     |     |     |     |     |     |     |     |     | :⟨DELETE,𝑡 | 1 ,−,−⟩, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- |
applicationsonly.
|     |     |     |     |     |     | where𝑡 |     | is a user | table, | any columns | involved | in its | condition |
| --- | --- | --- | --- | --- | --- | ------ | --- | --------- | ------ | ----------- | -------- | ------ | --------- |
1
|     |     |     |     |     |     | checks(i.e.,𝑡 |     | 2::𝑐 | ∈C)aredeemedadmincolumns. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ------------------------- | --- | --- | --- | --- |
2
1 $row=query("SELECT *FROM post WHERE id='$pid'AND   Subsequently,ifasensitiveoperation𝑙Cissecuredbyacondition
f or u m i d = '$ fi d '" ); checkthatinvolvesanadmincolumn(i.e.,𝑡 1::𝑐 ∈Cand𝑡 1::𝑐
|     |     |     |     |     |     |     |     |     |     |     |     | 1   | 1 ∈ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 if ( $ ro w [ sta tu s ]  = = "Open") { AdminColumn),itisdeemedsafewithoutfurtherconsultation
|     | 3 echo "<h1> $row[title]</h1>"; |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofourauthorizationmodels.Thisisestablishedbythe[Admin-
|     | 4 echo "<body> $row[content]</body>"; |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Check]rule.
|     | 5 …… |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenextthreerules,[Own-Check],[Mem-Check]and[Stat-
6
}
Check],enforceauthorizationrulesforthecorrespondingowner-
Finally,wewanttopointoutthatahierarchicalmodelinvolves
ship,membership,andstatusmodels,respectively.
| th re | e ( o r m o re | ) ta b le s | 𝑡 1, 𝑡 a n d 𝑡 , w he | re 𝑡 a n d 𝑡 co | n s tit u t ea n |     |     |     |     |     |     |     |     |
| ----- | -------------- | ----------- | --------------------- | --------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2 3 1 2 G iv e n ( 𝑡 , 𝑡 :: 𝑐 ) ∈ O w n e r M od e l, t he [ O w n- C h ec k ] r u le en -
| o w n | er s h ip o r | m e m b e | rs h ip m o d e l , a nd | 𝑡 a n d 𝑡 fo rm | o n e o r m u l- |     |     | 1 2 2 |     |     |     |     |     |
| ----- | ------------- | --------- | ------------------------ | --------------- | ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
2 3 sur es t h at e a c h s e n s iti ve o p er a t ion 𝑙 C o n ta b le 𝑡 (𝑙 C : ⟨− , 𝑡 ,− ,− ⟩)
|     |     |     |     |     |     |     |     |     |     |     |     | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiple 1:1 or 1:n relationships. Thus, we can reuse the two rules isguardedbyproperownershipchecks.Specifically,wedetermine
[Own-Model]and[Mem-Model]todeducehierarchicalmodels. whetherthetwocolumns𝑡 ::𝑐 and𝑡 ::𝑐
|     |     |     |     |     |     |     |     |     |     | 1 𝑝 | 2   | 2areinvolvedinthe |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
Forsimplicity,theserulesarenotgiveninFigure10.
|     |     |     |     |     |     | sameconditioncheckfor𝑙C,i.e., |     |     |     |     | (𝑡 :: 𝑐 | 𝑝 ,𝑡 :: 𝑐 ) ∈ | C.Forin- |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ------- | ------------- | -------- |
|     |     |     |     |     |     |                               |     |     |     |     | 1       | 2 2           |          |
stance,inFigure3(a),thisisindicatedbytheconditionatLine10,
4.2 DetectingBOLAVulnerabilities
|     |     |     |     |     |     | i.e.,userid |     | = $curr_user,whereuseridreferstothecolumn |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
Inthismodule,wefirstlocateallsensitivedatabasequerystate- post::useridand$curr_userreferstouser::id.
mentsandcalculatethesetofchecksCenforcedforeachquery The[Mem-Check]ruleissomewhatintricate:itrequiresthat
statement𝑙.Section4.3willdemonstratehowthetwostepsare twogroupsofforeignandprimarykeypairs–specifically,𝑡 1::𝑐 𝑝
performedindetail.HerewepresenttherulesfordetectingBOLA and 𝑡 :: 𝑐 2, along with 𝑡 :: 𝑐 𝑝 and 𝑡 ′ :: 𝑐 ′ – be involved
|     |     |     |     |     |     |     | 2   |     |     | 3   |     | 2 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vulnerabilitiesinFigure11.Forillustrativepurposes,wefirstintro- in two separate conditions checks, respectively. That is, (𝑡 ::
1
|     |     |     |     |     |     | 𝑐   | ,𝑡 𝑐 | ) ∈ C | (𝑡  | 𝑐 ,𝑡 ′ | 𝑐 ′) | ∈ C. |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ------ | ---- | ---- | --- |
ducethefollowingtwosets: 𝑝 2 :: 2 and 3 :: 𝑝 :: In our example in
|     |     |     |     |     |     |        |       |         |            | 2   | 2     |               |        |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | ---------- | --- | ----- | ------------- | ------ |
|     |     |     |     |     |     | Figure | 3(b), | the two | conditions | at  | lines | 5-7 – forumid | = $fid |
• AdminColumn,asetofadmincolumns,whichrepresent
|     |     |     |     |     |     | andin_array($curr_user, |     |     |     | $row)–implementtheauthoriza- |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
administratorsthatcanperformprivilegedoperations.
tionrulesofthemembershipmodel(user,user_forum::userid,
• SafeOp,asetofsafeoperations.
|     |     |     |     |     |     | forum, | user_forum::forumid) |     |     | for | the query | statement | at line |
| --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | --- | --------- | --------- | ------- |
TheAdminColumnsetisintroducedtomodelprivilegedusers forumid user_forum::forumid, $fid
|     |     |     |     |     |     | 11. | Here, |     | refers | to  |     |     | refers |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- | ------ |
suchassystemadministratorsofanapplication.Intuitively,system
toforum::id,$curr_userreferstouser::id,and$rowrefersto
administratorscanperformanyprivilegedoperations,irrespective user_forum::userid.
2941

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
1 DAL Specification manipulatingdata.TheDALspecificationsdetailhowtheseabstract
2 { APIsrelatetoSQLqueries,withourDALspecificationsdrawing
3 "name": "$wpdb->update", onexistingmethodology[42]forimplementation.
4 "op": "UPDATE", Figure12presentsasimplifiedDALspecificationexamplein
5 "table": {"name": "$0"}, JSONformat.ThespecificationdeclarestheAPIname(line3),its
6 "columns": {"name": "$1"}, correspondingSQLoperation(line4),aswellasAPIparameters
7 "where": {"name": "$2"} denotingthetargettable(line5),theoperatingcolumns(line6),
8 }
andtheconditionsfortheoperation(line7).Suchaconfiguration
Figure12:ADALspecificationexampleinthebenchmark enablesBolaRaytoreconstructSQLstatementsfrominvocations
SPManager-4.57. ofDALAPIs.Inthispaper,wehavemanuallywrittenDataAccess
Intherule[Stat-Check],wehave𝑡
1
::𝑐
1
′ ∈ C,ensuringthat L
p
a
e
y
r
e
m
r
e
(D
th
A
o
L
d
)
.
specificationsfor100APIs,withanaverageof13lines
thestatuscolumnisconsidered.Forexample,inFigure3(d),the
conditionatLine7checksthestatusofthepostbeforeaddinga ComputingAliases. Weleveragetheuse-defbaseddatadepen-
comment. dencyanalysisinTCheckertocomputealiases,wheretwovari-
Finally,thosesensitiveoperationsthatarenotintheSafeOp
ablesareconsideredasaliasesiftheydependonacommonvariable.
setarereportedasBOLAvulnerabilitiesviolatingcorresponding WeenhancedTChecker’sdependencyanalysiswiththreespecific
authorizationmodels.Itisnoteworthythatthetworules,[Own- extensions:1)Wehandleloopsintheformof‘foreach ($arr as
Check]and[Mem-Check],canbeeasilyextendedtovalidatethe $key⇒$value)’,commoninPHP,bylinking$arrtoboth$key
existenceofchecksforthehierarchicalauthorizationmodel.For and$valueinthedef-useanalysis,thustreating$arrasanalias
clarity,wedonotincorporatetheserulesinFigure11.Furthermore, forboth$keyand$value;2)Weintroducefunctionsummariesfor
Figure11illustratesthesimplecasewhereeachsensitiveoperation commonlibraryfunctions,includingarray_pushandcompact;3)
correspondstoasingleauthorizationmodel.Inreality,whenoper- Wedifferentiateaccessestothesamearraywithdistinctindexes,
atingontheposttableinFigure2,since(user, post::userid) e.g.,$row[0]and$row[1]. InBolaRay,aliasesareinstrumental
∈OwnerModel,andthetablesuser,forum,andposttogether
inassociatingavariablewithatablecolumn,whichalsoforms
constituteahierarchicalmembershipmodel,thestatementmust thefoundationtoinferimplicitforeignkeys([Connect]).InFig-
bevalidatedforeachmodelseparately. ure3(a),$curr_userreferstouser::idifitaliasesto𝑣′ and (𝑙,
user::id,𝑣′) ∈Binding.
4.3 Implementation
LocatingSensitiveOperations. Theoretically,alldatabasequery
WehavedevelopedBolaRayontopof TChecker[25],aninter-
statementsaresensitiveoperationsthatneedtobecheckedbyFig-
proceduralstaticanalysistoolforPHPapplications.Specifically,
ure11.However,thisoverlyconservativeapproachmayintroduce
TCheckerperformsinter-proceduraldata-flowanalysisonPHP
numerousfalsepositives.Specifically,wehavesummarizedthree
objectstoinfertheirtypesorvalues.Thisenablespreciseidentifica-
scenariosthatmaynotrequireobject-levelauthorizations:
tionofmethodcalltargets,facilitatingtheincrementalconstruction
• SELECTstatements.ItistoorestrictivetocheckeverySELECT
ofanprecisecallgraph,whichfurtherenhancesinter-procedural
statementsinceonlythosestatementsqueryingconfidential
data-flowanalysis.TCheckersupportscontext-sensitivitybutnot
informationrequireobject-levelauthorization.Revisiting
path-sensitivity,whichisalsonotrequiredbyBolaRay.Ourimple-
ourexampleinFigure2:ausercanreadpostscreatedby
mentationconsistsof12KlinesofGroovycode.Here,weelaborate
anotheruserfromtheposttablebutcannotqueryhisorher
ontheimplementationdetailsofthetechniquesusedinSection4.1
profileintheprofiletable.Howtoautomaticallydeduce
andSection4.2.
whetherthequeriedinformationisconfidentialornotisan
Parsing SQL Statements. We utilize regular expressions (e.g., interestingtopicworthyofseparateinvestigation.
CREATE TABLE.*, SELECT.*FROM.*, UPDATE.*SET.*, INSERT • INSERToperationsinhierarchicalmodels.InFigure2,due
INTO.*, DELETE FROM.*) to identify SQL statements (as direct totheabsenceofahierarchicalmembershipcheckinvolving
querystrings)withinthesourcecode.Subsequently,weleverage thethreetables–user,forum,andpost–ausercaninsert
existingresearchonloganalysis[49,54]torecursivelyanalyze apostintoanyforumregardlessoftheirmembershipinthat
variableswithinthesestatements,aimingtodistinguishstatictext forum.Wereportedthisissuetotheoriginaldeveloper,but
fromvariablesinSQLstatements.Afterthisinitialstep,weem- theydonotperceivethisasasecurityissue,consideringit
ployJsqlParser[19]toparseallSQLstatements,whichbuildsthe merelyafunctionalbug.Itremainsdebatablewhethersuch
schemaasshowninFigure6andnormalizeseachstatementinthe violationscouldleadtovulnerabilities.
formof⟨𝑘,𝑡,𝑐,(𝑐′,𝑣′)⟩,asdepictedinFigure7.AnySQLstatement • DELETEoperationsinStatusmodels.Typically,DELETEoper-
thatcannotbesuccessfullyparsedisdisregarded. ationsdonotconsidertheimpactonstatus.
Inconclusion,weconsiderdatabaseoperationnotfallinginto
DALSpecifications. BolaRayreliesonmanualinputDataAccess
theabovethreecategoriesassensitiveoperations.
Layer(DAL)specificationstohandleSQLstatementsencapsulated
indatabasemanipulatingframeworkAPIs.TheDAL,akintoan CollectingConditionalChecks. Thesetofchecks,C,guarding
ORM(Object-RelationalMapping)framework,istaskedwithdirect astatement𝑙 :< −,𝑡,−,(𝑐,𝑣) >includesconditionsintheWHERE
databaseinteractions,offeringanabstractAPIforqueryingand clauseofthestatement(i.e.,checksimpliedby (𝑐,𝑣))aswellas
2942

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
thoseinconditionalbranchesonwhich𝑙 iscontrol-dependent.We Theeffectivenessof BolaRayreliesontwokeyassumptions.
associateeachprogramvariable𝑣 inaconditionwithitscorre- First,wepresumethatmostfunctionalcode,specificallytheSQL
spondingtablecolumn(ifapplicable),andadditionalchecksinthe statements manipulating database tables, is correct. Otherwise,
WHEREclausesofthosestatementsbinding𝑣toaspecificcolumnare BolaRaywillfailtoreconstructcorrecttablerelationsandinfer
incorporated.Consequently,(𝑐,𝑣)impliesthat(𝑡 ::𝑐,𝑡′ ::𝑐′) ∈C authorizationmodelsbasedonthoserelations.Thisassumption
ifboth(𝑙,𝑡′ ::𝑐′,𝑣′) ∈Bindingand𝑣′aliasesto𝑣hold,indicating isreasonablebecauseanymalfunctionswouldlikelybereported
acomparisonbetweentwocolumns.Otherwise,𝑡 ::𝑐isincluded promptly.Second,weassumethatapplicationsadheretocommon
inC,validatingthecolumn𝑡 ::𝑐.Ultimately,thesetofchecksin programmingpracticesobservedinourstudy.BolaRayfollows
Ccompriseseachcheckthateithervalidatesasinglecolumnor thesepracticestoformulateaseriesofheuristic-basedrules.Ifan
comparestwocolumns. applicationdeviatesfromtothesepractices,itsBOLAvulnerabilities
Wefollowthestandardalgorithmthatcomputestheiterative maynotbedetectedbyBolaRay.
post-dominancefrontierof𝑙 asitscontroldependencies[10].Ac-
cordingtothestandarddefinition,𝑐isapost-dominancefrontier 5 Evaluation
of𝑙 if𝑙 post-dominatesoneofitssuccessorsbutnot𝑐itself.Inper-
We evaluated BolaRay using 25 open-source database-backed
formingsuchcontrolflowanalysis,wealsoconsiderthoseaborting PHP applications (see Table 2), which include 19 applications
statements (e.g., exit and die in PHP) as an exit node in their (fromrows3to21)thathavebeenwidelyevaluatedinprevious
correspondingcontrolflowgraphs. works[2,8,28,31,45]and6applications(fromrows22to27)from
ourempiricalstudy.Theseapplicationsspanvariousindustries,
4.4 Discussions containingdiversetablesandSQLstatements.Theexperiments
wereconductedonaMacBookProlaptopequippedwithan8-core
4.4.1 SoundnessandPrecision. Weemployaseriesofheuristic-
2.0GHzM1Proprocessor,16GBofmemory,andMacOSSonoma
basedrulestoinferobject-levelauthorizationmodels.Thoserules
14.4.1.
aresummarizedfromcommoncodingpractices,andalthoughthey
Ourevaluationaimstoanswerthefollowingresearchquestions:
workwellinpractice,theyareneithersoundnorcomplete.
• RQ1. How precise is BolaRay in identifying object-level
TheforeignkeyanalysisrulespresentedinFigure8accurately
authorizationmodels?
capturethesemanticsofforeignkeys,i.e.,tablecolumnsthatdi-
• RQ2.HoweffectiveisBolaRayindetectingBOLAvulnera-
rectlyorindirectlyrefertoprimarykeysofothertables(Defini-
bilities?
tion1).Theprecisionandsoundnessofforeignkeyanalysisare
• RQ3.HowefficientisBolaRay?
determinedbytheunderlyingaliasanalysis,whichmayproduce
• RQ4.HowdoesBolaRaycomparewithotherexistingap-
falsepositivesorfalsenegatives.However,ourexperiments,as
proach?
showninTable3,didnotrevealanyincorrectforeignkeys(nofalse
positives)oranymissingknownforeignkeys(nofalsenegatives).
5.1 IdentifyingAuthorizationModels
InFigure10,therule[User-Table]deducesusertablesbased
onthecommondesignpracticethatuserIDsmustbestoredin Accuratelyidentifyingauthorizationmodelsisessentialforthe
theglobalSESSIONvariable.Todistinguishfromothervaluesalso effectivenessofBolaRay.Table3outlinesthecountsofusertables,
storedinSESSION,wefurtherrequirethatusertablesmustcontain foreignkeys,tablerelations,statuscolumns,admincolumns,and
acolumnnamedwiththesubstring‘password’,‘passwd’,or‘pwd’. object-levelauthorizationmodelsinferredbyBolaRayforeach
This restriction results in no false positives in our experiments application.ToevaluateBolaRay’sprecision,wemanuallyexam-
(Table3).However,applicationsmaynotfollowthisdesign,leading inedthegeneratedreports.AsdepictedinTable3,BolaRaycor-
topotentialfalsenegatives. rectlyidentifies35usertables(Columns2-3)and1,151foreignkeys
Theheuristicsfordeterminingstatusandadmincolumnsare (Columns4-5,100ofwhichareexplicitlydeclaredintheschema,all
basedonobservationsinourstudiedapplications.Consequently, fromthebenchmarkRosariosis)withnofalsepositives.Wefurther
applicationsthatdeviatefromtheseobservationsmayexperience manuallycheckedeachtableandconfirmedthattherewereno
falsepositivesandfalsenegatives.Forinstance,developersmight knownfalsenegatives.ThisconfirmsthattherulesinFigure10
usearbitrarytypeslikeINTtorepresentastatus,whichviolatesthe andFigure8areeffectiveandpreciseinpracticalscenarios.Itis
firstconditionforidentifyingstatuscolumns.Additionally,applica- noteworthythattherule[Connect]bindsavariabletoatable
tionsmightpermitnon-adminrolestomanageusersorlackuser columnwiththenecessaryconditionthattheinvolvedstatements
managemententirely,leadingtofalsepositivesandfalsenegatives mustbeexecutedtogether.Thisfilteringstrategy,inspiredby[8],
inthediscoveryofadmincolumns,respectively.Suchfalsepositives didnotproducefalsenegativesinourexperimentswhileeffectively
andfalsenegativeswillbefurtherdiscussedinSection5.1. eliminating273falseforeignkeys.
Outofthe1,099inferredtablerelations(Columns6-11),only
4.4.2 ThreatModel. BolaRaydetectsthoseBOLAvulnerabilities onefalsem:nrelationinScarfwasreported(Column11).Thisfalse
that violate the four types of object-level authorization models positiveiscausedbythefactthatBolaRaymistakenlyclassified
outlinedinSection3.3.Thesefourauthorizationmodelsweredevel- anobjecttableasajunctiontable,resultinginafalsemany-to-
opedfromourempiricalstudyof101knownBOLAvulnerabilities. many relation. The identification of status columns exhibited a
Inpractice,othertypesofvulnerabilitypatternsmayexist,which lowerprecision,withafalsepositiverateof25%(Columns12-13).
arebeyondthedetectionof BolaRay. Thisdiscrepancyisattributedtothefactthatsomestatuscolumns
2943

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
Table2:StatisticsonEvaluationApplications.
| Application | SourceCode   | Database |          |               | #SQLQueries |        | Description |     |     |
| ----------- | ------------ | -------- | -------- | ------------- | ----------- | ------ | ----------- | --- | --- |
|             | #Files #LLOC | #Tables  | #Columns | SELECT INSERT | DELETE      | UPDATE | Total       |     |     |
Mybloggie-2.1.4 57 3,894 4 24 78 7 7 7 99 Contentmanagementsystem
| Scarf-1.0        | 19  | 840 7    | 37  | 50  | 7   | 6   | 12 75 Conferencesystem |     |     |
| ---------------- | --- | -------- | --- | --- | --- | --- | ---------------------- | --- | --- |
| Phpns-2.1.1alpha | 30  | 2,012 13 | 100 | 68  | 11  | 9   | 8 96 Newsplatform      |     |     |
Webid-1.2.2 239 16,304 57 367 415 83 72 197 767 Auctionplatform
SchoolMate-1.5.4 63 1,877 15 104 215 16 33 30 294 Schoolmanagementsystem
| PhpNews-1.3.0 | 20  | 3,488 6 | 37  | 61  | 39  | 5   | 13 118 Newsplatform |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | ------------------- | --- | --- |
Timeclock-1.04 63 12,373 8 35 257 20 7 22 306 Employmentmanagementsystem
HospitalMS-4.0 73 1,843 11 88 54 10 3 18 85 Hospitalmanagementsystem
DoctorApt-1.0.0 26 820 4 32 24 2 0 4 30 Doctormanagementsystem
Wheatblog-1.1 42 1,495 6 35 33 6 5 8 52 Contentmanagementsystem
| PHP7-Webchess | 30  | 3,307 7 | 48  | 63  | 14  | 12  | 20 109 Webgame |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | -------------- | --- | --- |
Hocms-1.0 38 1,386 7 52 35 9 4 12 60 Homecollectionmanagementsystem
Collabtive-3.1 74 18,152 20 141 139 20 43 35 237 Projectmanagementsystem
Oscommerce-2.4.2 436 25,287 51 358 374 465 190 124 1,153 Ecommerceplatform
Piwigo-14.4.0 681 120,653 39 221 335 12 31 55 433 Photomanagementsystem
PhpBB-3.3.12 1,219 71,781 70 605 856 14 145 298 1,313 Onlineforum
| SMF-2.1.4 | 329 | 87,394 73 | 525 | 745 | 24  | 229 219 | 1,217 Onlineforum |     |     |
| --------- | --- | --------- | --- | --- | --- | ------- | ----------------- | --- | --- |
Opencart-4.0.2.3 1,005 56,785 154 937 700 173 259 138 1,270 Ecommerceplatform
Zencart-2.0.1 1,312 63,107 110 896 746 319 102 103 1,270 Ecommerceplatform
Odfs-1.0 44 1,734 5 35 34 8 7 15 64 Onlinediscussionforumsystem
Admidio-4.1.12 241 20,659 38 366 352 40 69 79 540 Onlineusermanagementsystem
TeamPass-3.0.0.22 156 21,558 45 331 576 147 86 195 1,004 Collaborativepasswordsmanager
Rosariosis-8.9.4 374 36,437 92 937 1,010 29 92 88 1,219 Schoolmanagementsystem
SPManager-4.57 1,399 163,932 29 204 303 70 44 133 550 Wordpressprojectmanagementplugin
Openemr-7.0.0 795 95,373 255 3,351 1,413 162 72 262 1,909 Medicalpracticemanagementsystem
Total 8,765 832,491 1,126 9,866 8,936 1,707 1,532 2,095 14,270
Table3:NumberofTablesandRelations.
#User #Foreign #TableRelationships #Status #Admin #Ownership #Membership #Hierarchical #Status
Application Tables Keys 1:1 1:n m:n Columns Columns Models Models Models Models
TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP
| Mybloggie-2.1.4 | 1 0 | 3 0 0 0 | 3   | 0 0 0 | 0   | 0 1 0 | 2 0 0 | 0 1 | 0 0 0 |
| --------------- | --- | ------- | --- | ----- | --- | ----- | ----- | --- | ----- |
| Scarf-1.0       | 1 0 | 7 0 0 0 | 3   | 0 1 1 | 1   | 1 1 0 | 2 0 1 | 1 4 | 0 0 1 |
Phpns-2.1.1alpha 1 0 12 0 0 0 12 0 0 0 2 0 1 0 5 4 0 0 4 0 1 0
Webid-1.2.2 2 0 72 0 1 0 70 0 0 0 11 2 1 0 12 4 0 0 65 6 18 6
SchoolMate-1.5.4 1 0 26 0 3 0 17 0 2 0 0 0 1 0 6 2 1 0 6 0 0 0
| PhpNews-1.3.0   | 1 0 | 3 0 0 0  | 3   | 0 0 0 | 1   | 1 1 0 | 2 0 0 | 0 1 | 0 1 0 |
| --------------- | --- | -------- | --- | ----- | --- | ----- | ----- | --- | ----- |
| Timeclock-1.04  | 1 0 | 10 0 1 0 | 6   | 0 1 0 | 1   | 3 1 0 | 5 1 1 | 0 1 | 0 2 2 |
| HospitalMS-4.0  | 3 0 | 10 0 2 0 | 8   | 0 0 0 | 2   | 0 0 0 | 6 2 0 | 0 2 | 0 0 0 |
| DoctorApt-1.0.0 | 1 0 | 2 0 0 0  | 2   | 0 0 0 | 1   | 0 0 0 | 2 0 0 | 0 0 | 0 0 0 |
| Wheatblog-1.1   | 1 0 | 2 0 0 0  | 2   | 0 0 0 | 2   | 0 1 0 | 1 0 0 | 0 0 | 0 1 0 |
| PHP7-Webchess   | 1 0 | 9 0 0 0  | 9   | 0 0 0 | 0   | 2 0 0 | 4 0 0 | 0 8 | 0 0 3 |
| Hocms-1.0       | 1 0 | 5 0 0 0  | 5   | 0 0 0 | 6   | 0 0 0 | 1 0 0 | 0 0 | 0 3 0 |
Collabtive-3.1 1 0 33 0 0 0 21 0 6 0 2 0 1 0 5 1 3 1 21 1 8 1
Oscommerce-2.4.2 3 0 64 0 4 0 55 0 1 0 3 0 0 0 19 0 0 0 10 0 13 2
| Piwigo-14.4.0 | 1 0 | 34 0 1 0 | 29  | 0 1 0 | 1   | 0 0 0 | 10 0 1 | 0 1 | 0 0 0 |
| ------------- | --- | -------- | --- | ----- | --- | ----- | ------ | --- | ----- |
PhpBB-3.3.12 1 0 151 0 2 0 142 0 2 0 1 1 0 0 37 8 0 0 568 118 4 0
SMF-2.1.4 1 0 127 0 3 0 114 0 3 0 0 0 1 0 37 9 3 0 196 46 0 0
Opencart-4.0.2.3 2 0 91 0 1 0 87 0 1 0 0 0 1 0 15 1 0 0 0 0 0 0
Zencart-2.0.1 2 0 91 0 3 0 82 0 1 0 0 0 0 1 22 0 1 0 15 0 0 0
| Odfs-1.0 | 1 0 | 4 0 0 0 | 4   | 0 0 0 | 4   | 1 0 0 | 3 0 0 | 0 1 | 0 2 2 |
| -------- | --- | ------- | --- | ----- | --- | ----- | ----- | --- | ----- |
Admidio-4.1.12 1 0 39 0 0 0 39 0 0 0 1 0 1 0 18 3 0 0 8 0 2 0
TeamPass-3.0.0.22 1 0 106 0 0 0 102 0 2 0 4 0 2 1 15 4 0 0 135 7 32 0
Rosariosis-8.9.4 2 0 102 0 7 0 93 0 1 0 0 0 1 2 47 2 2 0 80 0 0 0
| SPManager-4.57 | 1 0 | 18 0 0 0 | 15  | 0 1 0 | 1   | 0 1 0 | 6 0 0 | 0 7 | 0 0 0 |
| -------------- | --- | -------- | --- | ----- | --- | ----- | ----- | --- | ----- |
Openemr-7.0.0 3 0 130 0 0 0 124 0 1 0 7 6 1 0 36 3 0 0 68 8 34 6
Total 35 0 1,151 0 28 0 1,047 0 24 1 51 17 17 4 318 44 13 2 1,202 186 121 23
Table4:Resultson15existingvulnerabilities.
areirrelevanttoauthorization,suchasthosecolumnscontrolling
thefrontenddisplaylanguage.Additionally,BolaRayaccurately CVE-2022-31295CVE-2022-31294CVE-2023-3063
inferred21admincolumns(Columns14-15),withonly4falseposi- CVE-2022-1551CVE-2023-3303CVE-2023-3304
Detected
tives,indicatingtheefficacyofthe[Admin-Col]ruleinFigure11. HUNTR-24ae402fCVE-2023-1463HUNTR-3bf6999c
Ultimately,BolaRayidentified1,909accuratemodelswithonly CVE-2023-2946CVE-2023-2945CVE-2023-2944
CVE-2023-2942CVE-2022-2824HUNTR-52da52b8
255falsepositives(Columns16-23).Itisnoteworthythatneither
5.2 Effectiveness
usertablesnor1:nrelationships,whichwereutilizedforinferring
ownershipmodels,yieldedfalsepositives.However,44ownership WeevaluatetheeffectivenessofBolaRayintermsofitsabilityto
modelsweremisreported(Column17).Thereasonforthesedis- detectexistingandnewvulnerabilities.
crepanciesisthattheseapplicationsdefinetheirownauthorization
| models, which | are inconsistent | with the ownership | models | we  |     |     |     |     |     |
| ------------- | ---------------- | ------------------ | ------ | --- | --- | --- | --- | --- | --- |
inferred.Thesefalsepositiveswerefurtherpropagatedtofalsehier- 5.2.1 ExistingVulnerabilities. Table4summarizestheresultsin
archicalmodels(Column21),stemmingfromincorrectownership detectingexistingvulnerabilitiesfromourstudy.Outofthe101
models.Thefalsepositivesrelatedtomembershipmodels(Column vulnerabilitiesexamined,31arePHPvulnerabilities.Afterexclud-
19)andstatusmodels(Column23)originatedfromincorrectm:n
ing16SELECT-relatedcases,weareleftwith15vulnerabilities
relationships(Column11)andincorrectstatuscolumns(Column forfurtheranalysis.BolaRaysuccessfullyidentifiedall15existing
13),respectively. BOLAvulnerabilitiesacrossthesixPHPapplicationsanalyzedin
ourstudy,achievingarecallrateof100%.
2944

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
Table5:BOLAvulnerabilitiesreportedbyBolaRay.MOC,MMC,MHC,andMSCdenotemissingownershipchecks,missing
membershipchecks,missinghierarchicalchecks,andmissingstatuschecks,respectively.
|             | #MOCs |     | #MMCs |     | #MHCs | #MSCs |     | #Total |
| ----------- | ----- | --- | ----- | --- | ----- | ----- | --- | ------ |
| Application |       |     |       |     |       |       |     | #CVEs  |
INSERT DELETE UPDATE INSERT DELETE UPDATE DELETE UPDATE INSERT UPDATE
TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP TP FP
Mybloggie-2.1.4 0 0 0 0 0 0 0 0 0 0 0 0 1 0 2 0 0 0 0 0 3 0 1
| Scarf-1.0 | 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 |
| --------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
Phpns-2.1.1alpha 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 3 0 3
|     | 0 1 | 7 0 8 | 9 0 0 | 0 0 0 | 0 3 0 | 0 0 17 | 3 0 0 | 35 13 8 |
| --- | --- | ----- | ----- | ----- | ----- | ------ | ----- | ------- |
Webid-1.2.2
SchoolMate-1.5.4 0 0 0 0 10 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 12 1 3
| PhpNews-1.3.0  | 0 0 | 0 0 0 | 1 0 0 | 0 0 0 | 0 1 0 | 1 0 1 | 0 0 0 | 3 1 3 |
| -------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Timeclock-1.04 | 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 4 | 0 0 0 | 4 0 1 |
| HospitalMS-4.0 | 0 1 | 2 0 4 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 6 1 4 |
DoctorApt-1.0.0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
| Wheatblog-1.1 | 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 1 | 0 0 0 | 1 0 1 |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| PHP7-Webchess | 0 0 | 1 0 7 | 0 0 0 | 0 0 0 | 0 1 0 | 0 0 0 | 4 0 0 | 9 4 3 |
| Hocms-1.0     | 0 0 | 1 0 2 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 5 | 0 0 0 | 8 0 2 |
Collabtive-3.1 0 1 3 0 3 0 1 0 3 0 8 0 2 0 3 0 8 0 1 0 32 1 13
Oscommerce-2.4.2 0 0 0 2 0 7 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 11 0
| Piwigo-14.4.0 | 0 0 | 0 0 1 | 1 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 1 1 0 |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| PhpBB-3.3.12  | 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 |
| SMF-2.1.4     | 0 0 | 1 0 1 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 2 0 2 |
Opencart-4.0.2.3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
| Zencart-2.0.1 | 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0  |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |
| Odfs-1.0      | 2 0 | 2 0 5 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 2 | 0 2 0 | 13 0 4 |
Admidio-4.1.12 0 0 2 6 2 5 0 0 0 0 0 0 0 0 0 0 1 0 0 0 5 11 0
TeamPass-3.0.0.22 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
Rosariosis-8.9.4 0 0 2 3 2 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 5 3 0
SPManager-4.57 8 0 0 0 9 0 4 0 0 0 5 0 0 0 0 0 0 0 0 0 26 0 3
Openemr-7.0.0 4 0 2 1 10 3 0 0 0 0 0 0 0 0 1 0 4 2 1 0 22 6 0
Total 14 4 23 12 67 27 5 0 3 0 13 0 10 0 9 1 45 10 4 0 193 54 52
5.2.2 NewVulnerabilities. Table5providesdetailsaboutvulnera- leadsto11falsepositives(Column23)reportedbyBolaRayfor
| bilitiesreportedbyBolaRay.Overall,BolaRayreportsatotalof |     |     |     | thisbenchmark. |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- |
247vulnerabilities,ofwhich193vulnerabilitieshavebeenmanu-
Column-levelAuthorization.
allyconfirmedasrealvulnerabilities,resultinginafalsepositive BolaRayenforcesobject-levelau-
rateof 21.86%(Columns22-23).Thistotalincludesthe15known thorization, while some applications require the authorization
modeltobemorefinely-grained,restrictingtospecificcolumns.
vulnerabilitiesmentionedintable4.Subsequently,wereportedthe
Theauctionsystem,Webid,issuchanapplication.BolaRaycor-
178newvulnerabilitiestotheircorrespondingmaintainers.Todate,
155vulnerabilitieshavebeenconfirmed,with52CVEIDsgranted. rectlyestablishedanownershiprelationshipbetweentheusertable
BolaRaydetectsatleastoneBOLAvulnerabilityin21appli- andtheauctiontable,whichstoresauctionitems.Consequently,
cations, except for Scarf, PhpBB, Opencart and Zencart. Upon BolaRayflaggedaMOCinscenarioswhenupdatestothecolumn
examiningScarf,itwasdiscoveredthatallsensitiveoperationsare auction::current_bidlackownershipverification.However,this
particularcolumnrecordsthecurrenthighestbidofauctionitems
restrictedtoadminusers,makingobject-levelauthorizationmodels
irrelevant.Nevertheless,byeffectivelyidentifyingtheadmincol- which,bydesign,couldbeupdatedbyanyuser,makingthisspecific
umnforScarf,asdetailedinTable3,BolaRayreportsnofalseBOLA columnuniversallychangeable.BolaRayreported9falsepositives
vulnerabilitiesinthisbenchmark.Theotherthreeapplicationsdid (Column7)duetothisdiscrepancy.
notrevealvulnerabilitiesbecausetheyhadalreadyimplemented
|     |     |     |     |     | LimitationsofTChecker. | TCheckerdoesnotsupportvariable |     |     |
| --- | --- | --- | --- | --- | ---------------------- | ------------------------------ | --- | --- |
properobject-levelauthorizationchecksforeachobject.
functions,whicharecommonlyusedforimplementingcallbacks
inPHP.Consequently,BolaRayreported11falsepositivesinOs-
| 5.2.3 FalsePositives. | BolaRayreports54falsepositivesatarate |     |     |     |     |     |     |     |
| --------------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
of 21.86%.Throughathoroughinvestigation,wesummarizethe commercebecauseitspermission-checkingAPIsareimplemented
commoncausesofthesefalsepositivesbelow: throughvariablefunctions.ThislimitationresultsinBolaRay’s
inabilitytoinfertheadmincolumninthisapplication.
| IncorrectStatusModel. | Thereare10falsemissingstatuschecks |     |     |     |     |     |     |     |
| --------------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
(MSCs) (Column 19), all caused by incorrectly inferred status 5.2.4 Case Studies. Here we investigate three intriguing new
columns,asdiscussedinTable3.Suchfalsepositivescanbead- BOLAvulnerabilitiesidentifiedbyBolaRay.
dressedbymanuallyannotatingrealstatuscolumns.
|     |     |     |     |     | CVE-2024-1693. | InSPManager,thereisanownershiprelation- |     |     |
| --- | --- | --- | --- | --- | -------------- | --------------------------------------- | --- | --- |
Application-levelAuthorization. shipbetweentheusertableandthesp_cu_projecttable.How-
BolaRaysimplifiesapplication-
admin
level access control policies with the role, and this sim- ever,theapplicationonlyverifiesownershipwhendeletingobjects
plificationleadsto14falsepositives. Forexample,inAdmidio, inthesp_cu_projecttable,whileitfailstodosoduringupdates
BolaRayaccuratelyderivesanownershiprelationshipbetween tothistable,allowingattackerstoarbitrarilyupdateotherusers’
usersandphotos,andconsequentlyreportedamissingownership sp_cu_project entries, thereby violating system integrity. It is
check(MOC)wheneditingphotos.Nevertheless,thisapplication importanttonotethat,duetothefrequentupdatesofnumerous
doesnotimplementobject-levelauthorizationandallowsanyuser APIs,developerscaneasilyoverlookobject-levelauthorizationfor
with the editPhotoRight permission to edit any photo at will. someAPIs.Thisoversightundergoestheneedforanautomated
Thisdiscrepancy,incontrasttothe[Own-Check]ruleinFigure11, toollikeBolaRaytosystematicallyscaneachAPI.
2945

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
| CVE-2024-23009. | TheCollabtiveapplicationcontainsamissing | 450 |     |     |     |     |     |     |     |     |
| --------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hierarchicalcheckvulnerability,whereinupondeletingaproject 400 Inferringauthorizationmodels
|     |     | 350 |     | DetectingBOLAvulnerabilities |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
folder,itonlyverifiesthemembershiprelationshipbetweenthe
| userandtheproject,neglectingtovalidatetheparent-childrela-  |     | 300 |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tionshipbetweentheprojectanditscontainingfolder.Asaresult,  |     | 250 |     |     |     |     |     |     |     |     |
| attackersmaydeleteanyprojectfolder.Suchmissinghierarchical  |     | 200 |     |     |     |     |     |     |     |     |
| checkvulnerabilitiesdemandmultiplesub-checks,allofwhichneed |     | 150 |     |     |     |     |     |     |     |     |
100
tobeenforcedtoensuresafety.
50
0
C V E - 20 2 4 - 3 2 1 6 6 . I n W e b i d , t h e a u c t i o n t a b l e , w h i c h s t o r e s a u c - . 4 . 0 h a .1 .4 . 0 .0 4 . 0 . 0 1.1 s s . 0 .1 . 2 . 0 .1 2 .4 .3 .1 . 0 1 2 2 2 .4 5 7 r-7.0.0
|     |     |     | Mybloggie-2 .1 f - 1 | lp 1 .2 1. 5 | -1 . 3 1 S -4 -1 | . 0 g - ebch e s - 1 | e- 3 2 .4 4 .4 -3.3 | 2 .1 0 .2 art-2.0 | s - 1 .1 . 0 . -8 . 9 | - 4. |
| --- | --- | --- | -------------------- | ------------ | ---------------- | -------------------- | ------------------- | ----------------- | --------------------- | ---- |
t i o n i t e m s , c o n t a i n s t w o s t a t u s co l u m n s : c l o s e d a n d s u s p e n d . a r 1a d - te - w s c k - M pt lo m iv e - -1 F - -4 . d f o- 4 3. 0 . is e r m
|     |     |     | S c . | 1 . e b i M a e | l o a l A | t b W o c b | t e r c g o B B | M a rt c | O d i s - o s a g | e   |
| --- | --- | --- | ----- | --------------- | --------- | ----------- | --------------- | -------- | ----------------- | --- |
T h e s e t w o c o l u m n s c o l la b o r a t i v e l y d e t e r m i n e w h e t h e r a n a u c t i o n s - 2 W l p N e c sp i t cto r h e a 7 - H ll a m w i h p S n c e n m i a s a r i a n e n
|     |     |     | p n | o o h i m | o W   | H P C o | m P i P | p e Z | d m P o s M O p |     |
| --- | --- | --- | --- | --------- | ----- | ------- | ------- | ----- | --------------- | --- |
|     |     |     | h   | c h P T   | H D o | P c     | o       | O     | A a R S P       |     |
it em c a n b e p u r c h a s e d o r n o t . H o w e v e r , W e b id o n l y c h e c k s t h e P S O s T e
closedcolumn,ignoringthesuspendcolumn.Asaresult,asus- Figure13:Analysistime(s)ofBolaRay
pendedauctionitemcanstillbepurchased. Toavoidsuchvul-
|     |     | Table | 6:  | Ownership | Models |     | and BOLA | vulnerabilities |     | re- |
| --- | --- | ----- | --- | --------- | ------ | --- | -------- | --------------- | --- | --- |
nerabilities,developersneedtocheckallrequiredstatusesfora
portedbyMace.
specificoperation.BolaRaydetectssuchvulnerabilitiesbyenforc-
|     |     |     |     | #Ownership |     |     | #MOCs |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | ----- | --- | --- | --- |
ingchecksonallstatuscolumnsofanobject,andthemissingcheck Application #CVEs
|     |     |     |     |     | Models | DELETE | UPDATE |     | Total |     |
| --- | --- | --- | --- | --- | ------ | ------ | ------ | --- | ----- | --- |
ofanystatuscolumnwillsignifyareport.Thisconservativestrat-
|     |     |     |     | TP  | FP  | TP  | FP TP | FP  | TP FP |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
egyguaranteessafety,andwedidnotencounteranyfalsepositives
|     |     | Mybloggie-2.1.4 |     | 2   |     | 0 0 | 2   | 0 2 | 0 4 | 0   |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
duetothisover-approximation.
|     |     | Scarf-1.0        |     | 1   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Phpns-2.1.1alpha |     | 5   |     | 4 0 | 0   | 1 0 | 1 0 | 1   |
|     |     | Webid-1.2.2      |     | 10  |     | 2 0 | 0   | 1 0 | 1 0 | 1   |
|     |     | SchoolMate-1.5.4 |     | 1   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
Allthenewvulnerabilitiesdetected PhpNews-1.3.0 2 0 0 0 0 1 0 1 0
5.2.5 ResponsibleDisclosure.
|     |     | Timeclock-1.04 |     | 2   |     | 1 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
byBolaRaycanleadtoseriousconsequences,includingdataloss, HospitalMS-4.0 4 2 2 0 3 0 5 0 4
|     |     | DoctorApt-1.0.0 |     | 1   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
datatampering,andsysteminstability.Recognizingthepotential Wheatblog-1.1 1 0 0 0 0 0 0 0 0
|     |     | PHP7-Webchess |     | 3   |     | 0 1 | 0   | 4 0 | 5 0 | 2   |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
risks,wetooktheresponsibilityofdisclosingallnewlyidentified
|     |     | Hocms-1.0 |     | 1   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
vulnerabilitiesin25database-backedapplications,withdetailed Collabtive-3.1 4 5 3 0 3 0 6 0 4
|     |     | Oscommerce-2.4.2 |     | 10  |     | 0 0 | 2   | 0 7 | 0 9 | 0   |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
reports.Wereachedouttothecorrespondingorganizationstore- Piwigo-14.4.0 2 0 0 0 1 0 1 0 0
|     |     | PhpBB-3.3.12 |     | 3   |     | 1 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
portthetotalnewvulnerabilitiesthroughtheirdedicatedemail SMF-2.1.4 1 0 0 0 0 0 0 0 0
|     |     | Opencart-4.0.2.3 |     | 3   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
addressesandsecurityvulnerabilityreportingforms.Adheringto Zencart-2.0.1 1 0 0 0 0 0 0 0 0
|     |     | Odfs-1.0 |     | 1   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
responsibledisclosurepractices,wewillrefrainfrompubliclyreleas- Admidio-4.1.12 0 0 0 0 0 0 0 0 0
inganyunresolvedvulnerabilitiesuntiltheyhavebeenaddressed TeamPass-3.0.0.22 11 4 0 0 0 0 0 0 0
|     |     | Rosariosis-8.9.4 |     | 2   |     | 0 0 | 0   | 0 0 | 0 0 | 0   |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
bydevelopers.Asofnow,155oftheidentifiedvulnerabilitieshave SPManager-4.57 2 0 0 0 0 0 0 0 0
|     |     | Openemr-7.0.0 |     | 10  |     | 0 1 | 0   | 5 0 | 6 0 | 0   |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
eitherbeenconfirmedorresolved,and52CVEidentifiershavebeen Total 83 19 7 4 18 10 25 14 12
| assignedtothesereports. |     | 5.4 | Comparison |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Mace[28]isthemostcloselyrelevantworktoBolaRay.Thistool
5.3 Efficiency
reliesonthemanualannotationofuservariablestoidentifyown-
ershiprelationships,wherethetargettableofanINSERTstatement
Figure13showcasesthetimesrequiredtoanalyzethe25applica-
isownedbytheinserteduservariable(ifitexists).Consequently,
tionslistedinTable2.Amongthem,SPManager(aWordPress
MacecheckswhetherthetargettablesofanyUPDATEorDELETE
plugin)standsoutfortakingthelongesttime,amountingto427.5
seconds.ThisunderscorestheefficiencyofBolaRayinconducting statementsenforceownershipchecksintheirWHEREclauses.Al-
thoughMaceisclosed-source,wereproducedthetoolforadirect
itsanalyses.ByintegratingthedatafromFigure13andTable2,
comparisonwithBolaRay.Insteadofmanuallyspecifyinguser
aclearpositivecorrelationemergesbetweentheoverallanalysis
variablesforMace,weusedtheuservariablesinferredbyBolaRay.
timeandthesizeofthecodebase.
TheresultsofthiscomparisonaresummarizedinTable6.Mace
Thisanalysistimecanbedividedintotwomaincomponents:
thetimedevotedtoinferringauthorizationmodelsandthetime correctlyidentified83trueownershipmodelsand25trueBOLA
vulnerabilitiesfor7applications,allofwhichwerealsodisclosed
allocatedtodetectingBOLAvulnerabilities.Notably,amajorityof
byBolaRay.However,Macemissedtherest235ownershipmodels
thetimeisconsumedbythemodelinferenceprocess.Itiscrucialto
and79MOCvulnerabilitiesreportedbyBolaRaybecauseitidenti-
emphasizethatthedurationofmodelinferenceisdirectlyrelatedto
fiesownershiprelationonlyfromINSERTstatements.Incontrast,
thenumberoftablesandSQLstatementsintheapplication,rather
thanitssheervolumeofcode.Forinstance,SPManager,despite BolaRayanalyzesaliasestogetherwithallformsofSQLstatements
toinfersuchrelationship.
havingalargercodebase,takeslesstimeinmodelinferencethan
Macereported19falseownershipmodelsand14falsevulnera-
Openemr,owingtoitsfewertablerelations.Thisobservationaligns
bilities,with15ofthefalseownershipmodelsand10ofthefalse
withourexpectations,astheprocessofmodelinferenceprimarily
|     |     | vulnerabilities |     | also | being | reported | by  | BolaRay. | The additional |     |
| --- | --- | --------------- | --- | ---- | ----- | -------- | --- | -------- | -------------- | --- |
involvesanalyzingSQLqueriestoinfertablerelationships.
2946

CCS’24,October14–18,2024,SaltLakeCity,UT,USA YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMengandLianLi
4falseownershipmodelsoccurredbecauseMacefailstorecog- itdistinctivelyinnovative.ThemostcloselyrelevantworktoBo-
nizejunctiontables,whichBolaRaycanhandle.Thisdifferencein laRayisMace[28],whichassumesthatanownershiprelation
capabilityleadstodiscrepanciesinanalyzingdatabasetablerela- existsbetweenauserandatableaslongastheINSERTstatement
tionships,furtheraffectingtheaccuracyofinferredauthorization ofatablecontainsauserID.UnlikeMace,ourapproachutilizesall
models.Moreover,Macereported4morefalsevulnerabilitiesthan typesofSQLstatementsandexpandstheconceptofownershipto
BolaRay.ThisbecauseMaceonlyverifieschecksintheWHERE includethreeadditionalauthorizationmodels.
clausesofSQLstatements,whereasBolaRayalsoconsiderschecks Dynamictools[20–22,27,38,40,46,55]forBOLAvulnerabil-
inconditionalbranches. itydetectionfocusonidentifyingtamperableIDsandvulnerabil-
itytriggers.Forexample,Authscope[55]analyzesuserrequests
5.5 LimitationsandFuturework toidentifytamperableIDsandexaminesresponsestodetermine
whethervulnerabilitiesaretriggered.Theeffectivenessofthese
Althougheffectiveinpractice,BolaRayhasthefollowinglimita-
effortsreliesontheabilitytotriggerasmanycodepathsaspossible
tions:
throughcomprehensiverequests.
• Manual DAL Specifications. Currently, BolaRay requires Anumberofdynamicdefenseapproacheshavebeenproposed
manualannotationofDALspecificationstodetailhowSQL topreventattacksthatexploitBOLAvulnerabilitiesatruntime.
queriesareencapsulatedinframeworkAPIs.Onaverage,we FlowWatcher [29] detects violations of object-level authoriza-
needtowrite13linesofspecificationsperAPI.Although tion models at the HTTP proxy level. Conversely, SafeD [11],
thisisaone-timeeffort,itisconsideredabarriertoadopting CLAMP[37],andNemesis[26]focusonidentifyingtheseviola-
thetoolfornewapplications. tionswithintheSQLserverenvironment.Alloftheseworksrelyon
• Generalizability.BolaRaysupportsPHPapplications;how- manualdescriptionsofobject-levelauthorizationmodels.BolaRay
ever,theapproachissuitableforgeneraldatabase-backed can enhance these existing methods by automatically inferring
applications.Therulesdevelopedforinferringauthorization object-levelauthorizationmodels.
modelsandapplyingauthorizationchecks(Figure8toFig- Generalaccesscontrolvulnerabilitieshavebeenstudiedexten-
ure11)canbereadilyimplementedinamulti-languagecode sively in the literature. AutoISES [44] statically infers security
analysisenginelikeCodeQL,andappliedtoapplications specificationsofLinuxsystemsbyanalyzingthecorrelationbe-
writteninotherlanguages. tweendatastructureaccessesandsecuritychecks.PeX[53]detects
• SELECTStatements.BolaRaydoesnotconsiderSELECTstate- accessvulnerabilitiesintheLinuxkernelusingacraftedindirect
ments as sensitive operations, meaning it cannot detect callanalysistoassociatepermissioncheckswithprivilegedfunc-
BOLAvulnerabilitiescausingsensitiveinformationleakage. tions.ACHyb[15]enhancestheprecisionofPeXthroughcombined
Thislimitationisalsopresentinallexistingstaticdetection static-dynamicanalysis.Sunetal.[43]detectaccesscontrolvul-
tools[7,9,12–14,28,30]forBOLAvulnerabilities.Deter- nerabilitiesinwebapplicationsbyfirstconstructingasitemapfor
miningwhichdatashouldbeclassifiedassensitiveinan differentroles,thencheckingwhetheraccessesfromunprivileged
applicationisachallengingtopicworthyoffurtherinvesti- pagescansuccessfullyreachprivilegedpages.RoleCast[41]pro-
gation[28]. posesarole-specificconsistencyanalysistodetectinconsistent
• Incorrectobject-levelauthorizationchecks.WedevelopedBo- authorizationchecksinwebapplications.MPChecker[24]auto-
laRaybasedonthefindingthatallstudiedBOLAvulner- maticallyidentifiesprivilegedoperationsindistributedsystemsby
abilitieswerecausedbymissingobject-levelchecks.Thus, inferringuser-andsystem-relatedvariablesvialog-basedanalysis,
BolaRayisnotdesignedfordetectingthoseincorrectobject- thencheckswhethertheprivilegedoperationsareguardedbyper-
levelauthorizationchecksagainstawrongvariable,which missionchecks.Comparedtotheaboveworks,BolaRaytargets
arerareinpractice. themoregranularBOLAvulnerabilities.
Therehavebeennumerousempiricalstudiestargetingdiffer-
Inthefuture,weplantoovercomesomeofthelimitationsbyutiliz-
entissuesindatabase-backedapplications,includingperformance
inglargelanguagemodelstoautomaticallygenerateDALspecifica-
bugs[23,51]anddataconstraintbugs[5,16,50].Tothebestofour
tionsandidentifysensitivedataforhandlingSELECTstatements.
knowledge,thisisthefirstpapertoconductanin-depthstudyof
BOLAvulnerabilitiesinsuchsystems.
6 RelatedWork
There have been a number of static tools capable of identify-
7 Conclusion
ing BOLA vulnerabilities, including Waler [12], SPACE [30],
ANOVUL[13],Cancheck[7],UrFlow[9],andFINAD[14].These Weconductedthefirstin-depthstudyonBOLAvulnerabilitiesin
toolsrequirethemanualprovisionofauthorizationmodelsandthen database-backedapplicationsanddevelopedBolaRay,anoveltool
applyvariousstaticanalysistechniques,suchasmodelchecking fordetectingsuchvulnerabilities.ThekeyideabehindBolaRay
andsymbolicexecution,toidentifyflawsinauthorizationimple- istheuseofacombinedSQLandstaticanalysistoautomatically
mentation.Toexpresstheunderlyingauthorizationmodel,different inferobject-levelauthorizationmodels.OurevaluationofBolaRay
specificationswereproposed.Forinstance,Walerusesinvariant encompassed25populardatabase-backedapplications,revealing
variables, UrFlow employs SQL query constraints, and FINAD 178newcriticalvulnerabilities.Notably,155ofthesevulnerabilities
utilizesactivityflowgraphstoannotateauthorizationrules.Incon- havebeenconfirmed,and52ofthemaredocumentedwithCVE
trast,BolaRayautomaticallyinfersauthorizationmodels,making identifiers.
2947

DetectingBrokenObject-LevelAuthorizationVulnerabilitiesinDatabase-BackedApplications CCS’24,October14–18,2024,SaltLakeCity,UT,USA
Acknowledgement
[27] S.GhasemiM.A.Hadavi,A.Bagherdaei.2021. IDOT:Black-BoxDetectionof
AccessControlViolationsinWebApplications.ISeCure13,2(2021).
We thank all reviewers for their valuable feedback. This work
[28] MalihehMonshizadeh,PrasadNaldurg,andVNVenkatakrishnan.2014.Mace:
is supported by the National Key R&D Program of China Detectingprivilegeescalationvulnerabilitiesinwebapplications.InCCS14.
(2022YFB3103900), the National Natural Science Foundation of 690–701.
[29] DivyaMuthukumaran,DanO’Keeffe,ChristianPriebe,DavidEyers,BrianShand,
China(62402474,62132020and62202452),andtheChinaPostdoc- andPeterPietzuch.2015.FlowWatcher:Defendingagainstdatadisclosurevul-
toralScienceFoundation(2024M753295). nerabilitiesinwebapplications.InCCS15.603–615.
[30] JosephPNearandDanielJackson.2016.Findingsecuritybugsinwebapplications
References usingacatalogofaccesscontrolpatterns.InProceedingsofthe38thInternational
ConferenceonSoftwareEngineering.947–958.
[1] 2020.CommonVulnerabilitiesandExposures(CVE).https://cve.mitre.org/. [31] EricOlsson,BenjaminEriksson,AdamDoupé,andAndreiSabelfeld.[n.d.].
[2] AbeerAlhuzali,RigelGjomemo,BirhanuEshete,andVNVenkatakrishnan.2018. Spider-Scents:Grey-boxDatabase-awareWebScanningforStoredXSS.([n.d.]).
{NAVEX}:Preciseandscalableexploitgenerationfordynamicwebapplications. [32] owsap.2023.API1:2023BrokenObjectLevelAuthorization.https://owasp.org/
InUSENIXSecurity18.377–392. API-Security/editions/2023/en/0xa1-broken-object-level-authorization/.
[3] F.E.Allen.1970.Controlflowanalysis.ACMSigplanNotices5,7(1970),1–19. [33] owsap.2023.API5:2023BrokenFunctionLevelAuthorization.https://owasp.org/
[4] apisecurity.io. 2022. API1:2019 — Broken object level authorizati. API-Security/editions/2023/en/0xa5-broken-function-level-authorization/.
https://apisecurity.io/encyclopedia/content/owasp/api1-broken-object- [34] owsap.2023.OWASPTop10APISecurityRisks–2023.https://owasp.org/API-
level-authorization.htm. Security/editions/2023/en/0x11-t10/.
[5] PeterBailis,AlanFekete,MichaelJFranklin,AliGhodsi,JosephMHellerstein, [35] owsap.2024. SQLInjection. https://owasp.org/www-community/attacks/
andIonStoica.2015.Feralconcurrencycontrol:Anempiricalinvestigationof SQL_Injection.
modernapplicationintegrity.InSIGMOD15.1327–1342. [36] owsap.2024.XSS.https://owasp.org/www-community/attacks/xss/.
[6] DanBarahona.2022.WhatisBrokenObjectLevelAuthorization(BOLA)and [37] BryanParno,JonathanMMcCune,DanWendlandt,DavidGAndersen,and
HowtoFixIt.https://www.apisec.ai/blog/broken-object-level-authorization. AdrianPerrig.2009.CLAMP:Practicalpreventionoflarge-scaledataleaks.In
[7] IvanBocićandTevfikBultan.2016.Findingaccesscontrolbugsinwebapplica- 200930thIEEESymposiumonSecurityandPrivacy.IEEE,154–169.
tionswithCanCheck.InASE16.155–166. [38] IPutuAgusEkaPratamaandAlvinMaulanaRhusuli.2022.PenetrationTesting
[8] AnChen,JiHoLee,BasantaChaulagain,YonghwiKwon,andKyuHyungLee. onWebApplicationUsingInsecureDirectObjectReferences(IDOR)Method.In
2023.SynthDB:SynthesizingDatabaseviaProgramAnalysisforSecurityTesting 2022InternationalConferenceonICTforSmartSociety(ICISS).IEEE,01–07.
ofWebApplications..InNDSS. [39] reddelexc.2023. TopIDORreportsfromHackerOne. https://github.com/
[9] AdamChlipala.2010.StaticCheckingof{Dynamically-Varying}SecurityPoli- reddelexc/hackerone-reports/blob/master/tops_by_bug_type/TOPIDOR.md.
ciesin{Database-Backed}Applications.In9thUSENIXSymposiumonOperating [40] MarcRennhard,MalteKushnir,OlivierFavre,DamianoEsposito,andValentin
SystemsDesignandImplementation(OSDI10). Zahnd.2022.Automatingthedetectionofaccesscontrolvulnerabilitiesinweb
[10] RonCytron,JeanneFerrante,BarryKRosen,MarkNWegman,andFKenneth applications.SNComputerScience3,5(2022),376.
Zadeck.1991.Efficientlycomputingstaticsingleassignmentformandthecontrol [41] SooelSon,KathrynSMcKinley,andVitalyShmatikov.2011.Rolecast:finding
dependencegraph.TOPLAS13,4(1991),451–490. missingsecuritycheckswhenyoudonotknowwhatchecksare.InOOPSLA11.
[11] KevinEykholt,AtulPrakash,andBarzanMozafari.2017.EnsuringAuthorized 1069–1084.
UpdatesinMulti-user{Database-Backed}Applications.In26thUSENIXSecurity [42] HeSu,FengLi,LiliXu,WenboHu,YujieSun,QingSun,HuinaChao,andWei
Symposium(USENIXSecurity17).1445–1462. Huo.2023.Splendor:StaticDetectionofStoredXSSinModernWebApplications.
[12] ViktoriaFelmetsger,LudovicoCavedon,ChristopherKruegel,andGiovanniVi- InISSTA23.1043–1054.
gna.2010.Towardautomateddetectionoflogicvulnerabilitiesinwebapplications. [43] FangqiSun,LiangXu,andZhendongSu.2011.StaticDetectionofAccessControl
In19thUSENIXSecuritySymposium(USENIXSecurity10). VulnerabilitiesinWebApplications..InUSENIXSecuritySymposium,Vol.64.
[13] MahmoudGhorbanzadehandHamidRezaShahriari.2020.ANOVUL:Detection [44] LinTan,XiaolanZhang,XiaoMa,WeiweiXiong,andYuanyuanZhou.2008.Au-
oflogicvulnerabilitiesinannotatedprogramsviadataandcontrolflowanalysis. toISES:AutomaticallyInferringSecuritySpecificationandDetectingViolations..
IETInformationSecurity14,3(2020),352–364. InUSENIXSecuritySymposium.379–394.
[14] MahmoudGhorbanzadehandHamidRezaShahriari.2020.Detectingapplication [45] ErikTrickel,FabioPagani,ChangZhu,LukasDresel,GiovanniVigna,Christo-
logicvulnerabilitiesviafindingincompatibilitybetweenapplicationdesignand pherKruegel,RuoyuWang,TiffanyBao,YanShoshitaishvili,andAdamDoupé.
implementation.IETSoftware14,4(2020),377–388. 2023. Tossafaulttoyourwitcher:Applyinggrey-boxcoverage-guidedmuta-
[15] YangHu,WenxiWang,CasenHunger,RileyWood,SarfrazKhurshid,andMohit tionalfuzzingtodetectsqlandcommandinjectionvulnerabilities.In2023IEEE
Tiwari.2021.ACHyb:ahybridanalysisapproachtodetectkernelaccesscontrol symposiumonsecurityandprivacy(SP).IEEE,2658–2675.
vulnerabilities.InESEC/FSE21.316–327. [46] NisalMadhushanVithanageandNeeraJeyamohan.2016.WebGuardia-Aninte-
[16] HaochenHuang,BingyuShen,LiZhong,andYuanyuanZhou.2023. Protect- gratedpenetrationtestingsystemtodetectwebapplicationvulnerabilities.In
ingdataintegrityofwebapplicationswithdatabaseconstraintsinferredfrom WiSPNET16.IEEE,221–227.
applicationcode.InASPLOS23.632–645. [47] EnzeWang,JianjunChen,WeiXie,ChuhanWang,YifeiGao,ZhenhuaWang,
[17] StepanIlyin.2024. WhatisBrokenObjectLevelAuthorization? https:// HaixinDuan,YangLiu,andBaoshengWang.2024.WhereURLsBecomeWeapons:
www.wallarm.com/what/broken-object-level-authorization. AutomatedDiscoveryofSSRFVulnerabilitiesinWebApplications.InS&P24.
[18] LanJiangandFelixNaumann.2020. Holisticprimarykeyandforeignkey IEEEComputerSociety,216–216.
detection.JournalofIntelligentInformationSystems54(2020),439–461. [48] Theworld’sfirstbugbountylatformforAI/ML.2024.CommonVulnerabilities
[19] JSQLParser.2024.JavaSQLParser.https://jsqlparser.github.io/JSqlParser/. andExposures(CVE).https://huntr.com/.
[20] AjayKumarShrestha,PradipSinghMaharjan,andSantoshPaudel.2015.Identifi- [49] W.Xu,L.Huang,A.Fox,D.Patterson,andM.I.Jordan.2009.Detectinglarge-scale
cationandillustrationofinsecuredirectobjectreferencesandtheircountermea- systemproblemsbyminingconsolelogs.InSOSP09.117–132.
sures.InternationalJournalofComputerApplications114,18(2015),39–44. [50] JunwenYang,UtsavSethi,CongYan,AlvinCheung,andShanLu.2020.Manag-
[21] MalteKushnir,OlivierFavre,MarcRennhard,DamianoEsposito,andValentin ingdataconstraintsindatabase-backedwebapplications.InProceedingsofthe
Zahnd.2021.AutomatedblackboxdetectionofHTTPGETrequest-basedaccess ACM/IEEE42ndInternationalConferenceonSoftwareEngineering.1098–1109.
controlvulnerabilitiesinwebapplications.InICISSP2021.SciTePress,204–216. [51] JunwenYang,PranavSubramaniam,ShanLu,CongYan,andAlvinCheung.
[22] XiaoweiLi,XujieSi,andYuanXue.2014. Automatedblack-boxdetectionof 2018.Hownottostructureyourdatabase-backedwebapplications:astudyof
accesscontrolvulnerabilitiesinwebapplications.InCODASPY14.49–60. performancebugsinthewild.InICSE18.800–810.
[23] XiaoxuanLiu,ShuxianWang,MengzhuSun,SichengPan,GeLi,Siddharth [52] ChendongYu,YangXiao,JieLu,YuekangLi,YetingLi,LianLi,YifanDong,
Jha,CongYan,JunwenYang,ShanLu,andAlvinCheung.2023. Leveraging JianWang,JingyiShi,DefangBo,etal.[n.d.].FileHijackingVulnerability:The
ApplicationDataConstraintstoOptimizeDatabase-BackedWebApplications. ElephantintheRoom.([n.d.]).
Proc.VLDBEndow.16,6(feb2023),1208–1221. [53] TongZhang,WenboShen,DongyoonLee,ChangheeJung,AhmedMAzab,and
[24] JieLu,HaofengLi,ChenLiu,LianLi,andKunCheng.2022.Detectingmissing- RuowenWang.2019. Pex:Apermissioncheckanalysisframeworkforlinux
permission-checkvulnerabilitiesindistributedcloudsystems.InCCS22.2145– kernel.In28th${𝑈𝑆𝐸𝑁𝐼𝑋}$SecuritySymposium.1205–1220.
2158. [54] XuZhao,YongleZhang,DavidLion,MuhammadFaizanUllah,YuLuo,Ding
[25] ChanghuaLuo,PenghuiLi,andWeiMeng.2022.TChecker:Precisestaticinter- Yuan,andMichaelStumm.2014.lprof:Anon-intrusiverequestflowprofilerfor
proceduralanalysisfordetectingtaint-stylevulnerabilitiesinPHPapplications. distributedsystems.InOSDI14.629–644.
InCCS22.2175–2188. [55] ChaoshunZuo,QingchuanZhao,andZhiqiangLin.2017.Authscope:Towards
[26] N.ZeldovichM.Dalton,C.Kozyrakis.2009.Nemesis:Preventingauthentication automaticdiscoveryofvulnerableauthorizationsinonlineservices.InCCS17.
andaccesscontrolvulnerabilitiesinwebapplications.(2009). 799–813.
2948
