> 원본: BACScan_CCS25.pdf, 변환: markitdown, 2026-10-06

<!-- 변환 깨짐: 원본 p.9-11 참조 -->
> 2단 편집과 표가 자동 변환에서 섞여 있다. 이 파일은 검색용이며, 수치와 문장 순서는 원본 PDF 및 조사 노트의 쪽 번호로 확인한다.
BACScan: Automatic Black-Box Detection of
Broken-Access-Control Vulnerabilities in Web Applications
FengyuLiu YuanZhang EnhaoLi
FudanUniversity FudanUniversity FudanUniversity
Shanghai,China Shanghai,China Shanghai,China
fengyuliu23@m.fudan.edu.cn yuanxzhang@fudan.edu.cn ehli23@m.fudan.edu.cn
WeiMeng YoukunShi QianhengWang
TheChineseUniversityofHongKong FudanUniversity FudanUniversity
HongKongSAR,China Shanghai,China Shanghai,China
wei@cse.cuhk.edu.hk 21110240048@m.fudan.edu.cn 21307130075@m.fudan.edu.cn
ChenlinWang ZihanLin MinYang
TheChineseUniversityofHongKong FudanUniversity FudanUniversity
HongKongSAR,China Shanghai,China Shanghai,China
clwang23@cse.cuhk.edu.hk zhlin22@m.fudan.edu.cn m_yang@fudan.edu.cn
Abstract ACMReferenceFormat:
Broken-Access-Control(BAC)vulnerabilitieshaveconsistentlybeen FengyuLiu,YuanZhang,EnhaoLi,WeiMeng,YoukunShi,Qianheng
Wang,ChenlinWang,ZihanLin,andMinYang.2025.BACScan:Automatic
rankedamongthemostcriticalsecurityrisksinwebapplications,
Black-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebAp-
occupyingthetoppositionsintheOWASPTop10overthepast
plications.InProceedingsofthe2025ACMSIGSACConf.onComputerand
severalyears.Thesevulnerabilitiesallowattackerstobypassaccess
CommunicationsSecurity(CCS’25),October13–17,2025,Taipei.ACM,New
controlmechanismsandperformunauthorizedoperations,posing
York,NY,USA,14pages. https://doi.org/10.1145/3719027.3744825
securityandprivacythreatstosensitivebusinessanduserdata.
DespitesubstantialattentiongiventoBACvulnerabilities,effective 1 Introduction
andreliableapproachestodetectingtheseissuesremainlimited.
Broken-Access-Controlmovesuptothecategorywiththemostserious
Inthiswork,wepresentBACScan,anovelblack-boxapproach
webapplicationsecurityrisk.
todetectBACvulnerabilitiesinwebapplications.Unlikeexisting
—TheOWASPTop10[19].
response similarity-based oracles that check only unauthorized
readaccesses,BACScanintroducesaninnovativefeedback-driven With the rapid advancement of web applications, numerous
oracle,whichdetermineswhetherunauthorizedreadormodifica- commercialplatforms(e.g.,Amazon[1],PayPal[9])nowstoresub-
tionoperationshaveoccurredbyinferringoperationally-dependent stantialvolumesofcriticalprivacy-sensitiveuserdata,including
webpagesandanalyzingtheoperationalfeedback.Weevaluated identityandpaymentinformation,therebymakingthemattractive
BACScanon20real-worldapplicationsandsuccessfullyidentified targetsforwebattackers.Toprotectthissensitivedata,developers
89vulnerabilities,including54previouslyunreportedones,out- implementanddeployaccesscontrolmechanismstopreventunau-
performingstate-of-the-arttools.Wereportedallnewlyidentified thorizedoperations.However,inadequateorimproperlyconfigured
vulnerabilitiestotheaffectedvendors.Todate,35newCVEIDs accesscontrolmechanismscangiverisetoseriousvulnerabilities,
havebeenassigned. knownasBroken-Access-Control(BAC)vulnerabilities.
Inrecentyears,BACvulnerabilitieshavebecomeincreasingly
CCSConcepts severe.AccordingtotheOWASPTop10,BACvulnerabilitieshave
consistentlyrankedamongthemostcriticalissuesoverthepast
•Securityandprivacy→Webapplicationsecurity.
fiveyears[18,19,21].InOWASP2023,BACvulnerabilitieseven
Keywords accountedforfouroutofthefivemostseverevulnerabilities[21].
Furthermore,numerouswidely-usedapplications,includingPayPal,
BrokenAccessControl;WebSecurity
Twitter,andTikTok,havebeenreportedtoexhibitBACvulnerabil-
ities,asdocumentedinHackerOne[15,16].Attackersmayexploit
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
thesevulnerabilitiestoperformunauthorizedoperations,includ-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ingarbitraryread,modification,orevendeletionofsensitivedata,
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe therebyposingsignificantthreatstotheavailabilityandintegrity
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
ofthevulnerableapplications[20,22].
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. AlthoughBACvulnerabilitydetectionisawell-exploredresearch
CCS’25,Taipei topic,theincreasingseverityofBACvulnerabilitieshighlightsthe
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
long-lastinglackofhighlyeffectivedetectiontechniques.Recentde-
ACMISBN979-8-4007-1525-9/2025/10
https://doi.org/10.1145/3719027.3744825 tectionapproachescangenerallybecategorizedintowhite-boxand

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
black-boxmethods.White-boxapproachesexhibitsignificantlimi- status page providing feedback is identified, the next step is
tations,includinghighfalsepositiverates,theinabilitytogenerate toreplaymodificationrequestsusinganattacker’ssessionand
proof-of-concept(PoC),andscalabilityissuesassociatedwithstatic verifyifunauthorizedchangestodataoccur.However,thetarget
analysistechniques[45].Toaddresstheselimitations,researchers applicationmaynotbeintherightstate,andissueslikeattempts
haveexploreddynamicblack-boxscanningtechniques(i.e.,scan- todeletenon-existentdatamaycauseoperationstofail,resulting
ners),whicharewidelyusedmethodsforpenetrationtestingand infailedrequestreplaysandaffectingdetectionaccuracy.
areparticularlyeffectiveindetectingsecurityflawsinreal-world
InspiredbyBlackWidow[32],weobservethatthedataaccess
scenarios[24,30].Giventheseadvantages,weadoptedablack-
andoperationaldependencybetweenwebpagescanhelpusidentify
boxapproachfordetectingBACvulnerabilitiesandconducteda
thecorrespondingstatuspagesofthemodificationpage.Thestatus
thoroughstudyofexistingblack-boxtechniques.Specifically,these
pagescouldprovidefeedbackfordetectingunauthorizedmodifi-
techniques[28,35,37,49,50,62]relyonaresponsesimilarity-based
cations.Therefore,BACScanintroducesanoveldatastructureto
oracle(shortenedtoresponse-basedoracle)fordetectingBACvul-
representthedatadependencyrelationship,calledtheInter-page
nerabilities.Inparticular,thesecurityanalystssetupanattacker
DataDependencyGraph(IDDG).Specifically,itutilizesSoTAcrawl-
andavictimuseraccountswiththescanners.Thescannerusesthe
ingtechniqueswiththevictimuser’scredentialstoconstructthe
attacker’scredentialstosendHTTPrequeststoaccessthevictim’s
IDDGbasedonthenavigationgraph.Theprocessinvolvesinter-
personaldata.Iftheresponsereceivedbytheattackerissimilarto
ceptingrequeststomodificationpages,generatingandinserting
thevictim’s,aBACvulnerabilityisreported.
uniquetokens,andleveragingthehierarchicalstrategytoefficiently
However,thedesignofthisoracleexhibitssignificantinherent
traversethenavigationgraphtoestablishdatadependenciesbe-
flaws.Oracleisacrucialandfundamentalcomponentofblack-box
tweenmodificationandstatuspages.Then,BACScanleveragesthe
scanners,playingapivotalroleindeterminingtheeffectivenessof
constructedIDDGtoapplythenovelfeedback-drivenoracleto
black-boxvulnerabilitydetection[32].Unfortunately,theresponse-
detectMBACvulnerabilities.Specifically,itfollowsthenavigation
basedoracleisbasedonaflawedassumption:thedirectresponseto
edgetoreplaymodificationrequestswiththeattacker’scredentials
aBACattackrequestalwaysprovidesevidenceindicatingwhether
and follows the data dependency edge to revisit corresponding
theexploitissuccessfulornot.Thisassumptionholdstrueinscenar-
statuspagestoobtainfeedback.ItthendetectspotentialMBAC
ioslikeunauthorizeddataleakageviaRead-basedBrokenAccess
vulnerabilitiesbasedonthepresenceorabsenceofuniquetokens.
Control(RBAC)vulnerabilities,wheretheleakeddataisdirectly
WeevaluatetheeffectivenessandperformanceofBACScanon6
returnedtotheattackerviatheHTTPresponse.However,inother
open-sourcewebapplicationswith44knownBACvulnerabilities
scenariossuchasunauthorizeddatadeletionviaModification-based
and14applicationswithnoknownvulnerabilities.Theseapplica-
BrokenAccessControl(MBAC)vulnerabilities,thisassumption
tionshavebeenwidelyevaluatedinpreviousstudies[26,34,48,
failsasthedirectHTTPresponsetotheattackrequestdoesnotnec-
56,58]andeachhasatleast100starsonGitHub,demonstrating
essarilyindicatewhethertheunauthorizedoperationissuccessful.
theirrepresentativenessandpopularity.Moreover,theyareimple-
Thiserroneousoracleleadstoasignificantrateoffalsenegatives
mentedinvariouslanguages,includingJava,PHP,andGo,further
andfalsepositivesinthedetectionofMBACvulnerabilities(70.97%
demonstratingthelanguage-independentadvantageofBACScan.As
and86.96%inourevaluation,respectively).
aresult,BACScansuccessfullydiscovered89vulnerabilities,includ-
Inthispaper,weproposeBACScan,anovelblack-boxapproach
ing54(verified)high-risk0-dayand35knownBACvulnerabilities.
todetectingBACvulnerabilitiesinwebapplications.Specifically,
Besides,wecompareBACScantostate-of-the-arttechniques(i.e.,
BACScanemploysthestate-of-the-art(SoTA)response-basedoracle
BurpSuite[12]andEvoCrawl[35]).BACScanperformssignificantly
fordetectingRBACvulnerabilitieswherethedirectHTTPresponse
better,detectingupto49additionalvulnerabilities.Thesenewly
providesfeedback.Wedesignanovelfeedback-drivenoraclefor
discoveredBACvulnerabilitieshavethepotentialtoleaksensi-
MBACvulnerabilitieswherethedirectHTTPresponsecannotre-
tiveuserinformation,deleteormodifycriticaloperationaldataand
flectthemodificationstatus.Itdetermineswhetherunauthorized
records(e.g.,changingapatient’sprescription),posingserioussecu-
modificationshavesucceededbyobservingthefeedbackfromother
rityandprivacythreatstoindividualusersandbusinessoperations.
operationally-dependentpagesthatindicatethemodificationsta-
Giventheirsignificantsecurityimpact,weresponsiblyreportedall
tus.Whiletheideaisintuitivelysimple,effectivelyimplementing
thenewlydetectedvulnerabilitiestotherelevantdevelopers.At
andapplyingthisfeedback-drivenoracleforMBACvulnerability
thetimeofwriting,39vulnerabilitieshavebeenconfirmedbythe
detectionpresentssignificantchallenges.Toachievethis,twomain
developers,and35havebeenassignednewCVEIDs.
challengesmustbecarefullyaddressed:
Insummary,ourpapermakesthefollowingcontributions:
• C1:Howtoaccuratelyandefficientlyidentifystatuspagesthat
providefeedbackinablack-boxcontext?Accuratelyidentifying • Wedesignanewfeedback-drivenoraclethatleveragesinter-page
thecorrespondingstatuspagesthatprovidefeedbackformodi- datadependencyforblack-boxdetectionofBACvulnerabilities.
ficationpagesiscriticalforvulnerabilitydetection.However, • Weproposeanovelblack-boxdetectionapproach—BACScan—to
inablack-boxscenario,onlyHTTPrequestsandresponsesare effectivelydetectBACvulnerabilitiesinwebapplications.We
available.Giventhevastnumberofrequestsandresponsesin willopen-sourceourprototypeuponpublication.
modernwebapplications,accuratelyandefficientlypinpointing • Our evaluation with 20 real-world popular web applications
theseoperationally-dependentstatuspagesisnon-trivial. demonstratestheeffectivenessofBACScan,withthediscovery
• C2:Howtonavigatetheapplicationintothecorrectstatetocollect of54(verified)0-dayBACvulnerabilitiesandtheassignmentof
effective feedback for MBAC vulnerability detection? Once the 35newCVEIDs.

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
withthecorrespondingpagecontent(i.e.,HTTPresponses)foreach
http://website/user-a.php?op=delete
user.Third,thescannerfiltersoutpublicpagesaccessibletoboth
User A's info
the attacker and the victim and selects the pages that are only
User A (Victim) • Name: Alice
accessibletothevictim.Itthenreplacesthevictim’ssessionwith
• Addr: US
theattacker’s,keepingallotherrequestparametersidentical,and
User B's info revisitsthepagesthatareexclusivelyaccessibletothevictim.If
http://website/user-b.php?op=delete • Name: Bob thecontentforagivenpageishighlysimilarbetweentheattacker
• Addr: UK andthevictim,thescannerreportsapotentialBACvulnerability.
User B (Attacker) Web Application
2.3 LimitationsofExistingBlack-boxScanner
Figure1:ThreatModelofBACVulnerability. Undoubtedly,theoracleisacrucialandfundamentalcomponent
ofblack-boxscanners,playingapivotalroleindeterminingthe
2 ProblemStatement effectiveness of vulnerability detection [32, 34]. At first glance,
theresponse-basedoracleappearsintuitivelyreasonableandwell-
2.1 Broken-Access-ControlVulnerability
suitedforBACvulnerabilitydetection.However,uponanin-depth
Webapplicationsstoresubstantialamountsofsensitiveuserdata, analysisoftheoracle’sunderlyingmechanism,weobservethat
suchasidentityandpaymentinformation,whichisprotectedby itispredicatedonaflawedassumption:thedirectresponsetoa
applications’accesscontrolmechanisms.However,misconfigura- BACattackalwayscontainsevidenceindicatingwhethertheexploitis
tionsinthesemechanismswouldresultinBroken-Access-Control successfulornot.Thisassumptionsignificantlylimitsthescanner’s
(BAC)vulnerabilities[18],includingissueslikeCWE-284(Improper applicabilitytoonlyanarrowsubsetofBACvulnerabilities.
AccessControl)[4].Thesevulnerabilitiesallowattackerstobypass Specifically, in certain scenarios, this assumption holds true.
accesscontrolsandperformunauthorizedoperations,suchasread- Forexample,thepresenceofavictim’sorderdetailswithinthe
ing,modifying,ordeletingsensitivedataofotherusers,posing attacker’sHTTPresponseclearlyindicatesaBACvulnerability.
riskstotheapplication’sconfidentiality,integrity,andavailabil- Nevertheless,inotherscenarios,thisassumptionfailsandresults
ity[20,22].Forexample,asshowninFigure1,althoughbothusers insignificantissuessuchasfalsenegativesandfalsepositives.To
shouldonlyhaveaccesstotheirowndata,UserB(theattacker)can provideamoreclearillustration,weclassifyBACvulnerabilities
exploitthevulnerabilitytodeletethedataofUserA(thevictim) basedontheirimpactondataintegrityandorganizethemintotwo
withoutauthorization. distinctcategories:Read-basedBroken-Access-Control(i.e.,RBAC)
andModification-basedBroken-Access-Control(i.e.,MBAC).
2.2 ExistingDetectionTechniques ❶RBACvulnerabilitiesarecharacterizedbyread-onlyopera-
Existingwhite-boxapproaches[43,44,46,52–54]utilizevarious tions(e.g.,SELECT)throughwhichattackerscanachieveunautho-
application-specificinputs(e.g.,runtimelogsandcodeannotations) rizedreadaccesstodatawithoutmodifyingit.Thedirectresponse-
toidentifyaccesscontrolcheckswithinapplications,treatinginad- basedoracletypicallyworkswellfordetectingRBACvulnerability,
equatelysafeguardedsecurity-sensitiveoperationsasBACvulner- asthegoalofexploitingRBACistoleaksensitivedata.Conse-
abilities.Whilethehigh-levelideaisreasonable,theseapproaches quently,theaccessedprivatedataisdirectlyleakedtotheattacker
stillpresentnotablelimitationsduetohighfalsepositives,inability viatheHTTPresponse,whichservesasanindicatorofwhether
togeneratePoCs,andrelianceonspecificprogramminglanguages. unauthorizeddataaccesshasoccurred.
Recently,numerousstudieshaveexploredblack-boxtechniques ❷MBACvulnerabilities,ontheotherhand,involvemodifica-
fordetectingBACvulnerabilities.Black-boxscanningiswidelyem- tionoperations(e.g.,INSERT,UPDATE,andDELETE)andrepresenta
ployedinsecuritypenetrationtesting.Thisapproachusesscanners significantportionofBACvulnerabilities.GiventhatMBACcanse-
tosimulatereal-worldattacksfromanexternaladversary’sper- verelycompromisedataintegrity(e.g.,deletingcriticalprivateuser
spective,wheretheattackerlackspriorknowledgeofthesystem’s data),itspotentialimpactismuchmoreseverethanthatofRBAC.
internallogicandimplementationbutcanobservethesystem’s However,forMBACvulnerabilitis,thedirectresponse-basedoracle
externalbehavior.Black-boxtechniquesareparticularlyeffective isgenerallyineffective.Insomecases,thestatusofdatamodification
indetectingsecurityflawsinliveorproductionenvironmentsdue ispresentinthedirectHTTPresponse,indicatingwhethertheunau-
totheirlowrelianceonsourcecode,significantlyincreasingtheir thorizedmodificationissuccessful(e.g.,{"status":"success"}
practicalityinreal-worldscenarios[24,30].Giventheseadvantages, inHTTPresponse).Nevertheless,inmostcases,thestatusisnot
wedecidedtoadoptablack-boxapproachfordetectingBACvul- availableindirectresponsetomodificationrequests.Thisisdue
nerabilitiesandconductedathoroughstudyofexistingtechniques. totheintrinsicnatureofMBAC,whichprimarilyfocusesondata
Manyworks(e.g.,[28,35,37,49,50,62])introducedautomated modification.Themodificationstatusmightnotbeobservablein
black-boxscannersforBACvulnerabilitydetection.Specifically, thedirectresponsetotheuserandbepresentinotherdependent
theytypicallyadoptaresponsesimilarity-basedoracleandemploy responses.Consequently,treatingthedirectresponseasanindica-
athree-stepapproach.First,theyconfiguretwousersofthetarget torofmodificationstatus(i.e.,response-basedoracle)fordetecting
application for the scanner, with one acting as an attacker and MBACvulnerabilityleadstoasignificantnumberoffalsepositives
the other serving as a victim user. Second, the scanner utilizes andfalsenegatives.Asdemonstratedin§5.3,ourevaluationre-
boththevictim’sandtheattacker’ssessionstoexploretheweb vealsthatthefalsepositiveandfalsenegativeratescanreachas
application,separatelycollectingthepagesaccessibletoeach,along highas70.97%and86.96%,respectively.Therefore,itiscrucialto

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
POST /api/v1/user/update POST /api/v1/user/update noMBACvulnerabilityactuallyexists.Nevertheless,sincethere-
Host: api.*****.com Host: api.*****.com sponsestobothrequestsarehighlysimilar,theresponse-based
Cookie: Alice Cookie: Bob oracleerroneouslyconcludesthatavulnerabilityispresent,result-
inginafalsepositive.
uid=1&new_name=newalice uid=1&new_name=newalice
3 OverviewofOurMethod
HTTP/1.1 200 OK HTTP/1.1 200 OK
Content-Type: application/json Content-Type: application/json Althoughtheresponse-basedoracleiseffectiveforRBAC,itproves
fundamentallyunsuitablefordetectingMBACvulnerabilitiesdueto
{"uid": "1", "addr": "US"} {"uid": "2", "addr": "UK"}
theintrinsicdifferencesintheiroperationalcharacteristics.There-
a) Real-world Example in WeBid (Vulnerable) fore,inthiswork,ratherthanrelyingonthetraditionalresponse-
based oracle, we propose a novel oracle for effective black-box
POST /api/v1/order/delete POST /api/v1/order/delete
MBACvulnerabilitydetection.Inthissection,wefirstintroduce
Host: api.*****.com Host: api.*****.com
Cookie: Alice Cookie: Bob thedesignofourneworacle(in§3.1),thendiscussthechallenges
encountered(in§3.2),andfinallypresentoursolution(in§3.3).
order_id=1 order_id=1
3.1 MBACDetectionOracle
HTTP/1.1 302 Found HTTP/1.1 302 Found
GiventhatattackersaimtomodifydatabyexploitingMBACvul-
Content-Type: application/json Content-Type: application/json
nerabilities,detectingMBACvulnerabilitieshingesondetermining
{"status": "redirect: /order"} {"status": "redirect: /order"} whetheranunauthorizeddatamodificationissuccessful.Building
onthisunderstanding,thekeyinsightbehindourapproachisthat
b) Real-world Example in SuperMarket (Secure)
thedataalteredbyamodificationpagecanbedisplayedonastatus
Figure2:Real-worldBACVulnerabilityExamples. page.Inotherwords,thereexistsastatuspagethatprovidesmod-
ificationfeedbackinmostcases,althoughitcanbeonedifferent
identifythecorrectdependentindicatorsofmodificationstatusto fromthemodificationpage.Thismakessensebecausewebapplica-
accuratelydetectMBACvulnerabilities. tionswouldusuallypresentuser-specificdatathatcanbemodified
throughmultiplechannelsonsomededicatedpages.Suchpages,
2.4 Real-WorldBACExample whichareusedtoviewdata,canthereforefunctionasstatuspages
providingfeedback.Forexample,consideranapplicationthathas
Tohighlightthelimitationsofexistingwork,wepresenttworeal-
twopages:anordersubmissionpageandanorderlistpage.Whena
worldexamplesillustratedinFigure2.
usersubmitsanorderthroughtheordersubmissionpage,thedetails
Figure2(a)illustratesa0-dayMBACvulnerabilitywithinWe-
ofthatordercanbedisplayedontheorderlistpage.Byexamining
Bid[17].Theresponse-basedoracleisineffectiveindetectingthis
theorderlistpage,wecandeterminewhethertheordersubmission
vulnerability,resultinginafalsenegative.Specifically,userAlice
issuccessful,asitdisplaysthedataregardingthesubmittedorder.
(thevictim)sendsarequesttothe/api/vi/user/updatepage
Ifthedatashownontheorderlistpagechangesunexpectedlyor
toupdateherusername.Theparametersuidandnew_namerepre-
ismodifiedbyanotheruserwithouttheoriginaluser’sconsent,it
sentAlice’suserIDandthenewusername,respectively.UserBob
becomesapparentthatunauthorizedmodificationshaveoccurred.
(theattacker)replacesthecookiewithhisownwhileleavingthe
Thus,theorderlistpageservesnotonlyasadisplayforsubmitted
restoftherequestunchanged,andthenreplaystherequest.Since
ordersbutalsoasacrucialindicatorfordetectinganyunauthorized
thedeveloperfailedtoimplementanappropriateaccesscontrol
datamanipulationontheordersubmissionpage.
policytoverifytherelationshipbetweenthecurrentlylogged-in
Therefore,wedesignafeedback-drivenoracleforMBACvulner-
userandthevalueoftheuidparameter,BobcanmodifyAlice’s
abilitydetection.Specifically,theintuitivedetectionworkflowcan
usernamewithoutauthorization,exposinganMBACvulnerability.
beoutlinedinthefollowingtwosteps:(1)wecrawlandexplorethe
However,theresponsetothismodificationrequestdoesnotcon-
applicationwiththevictim’scredential,analyzetheHTTPrequests
tainanyindicatorsshowingwhethertheupdateissuccessful.The
andresponses,andidentifythestatuspagethatdisplaysthedata
applicationonlyreturnstheinformationrelatedtotheuserwho
relatedtothemodificationrequest.(2)wereplaythemodification
makestherequest,suchastheuidandaddress.Consequently,even
requestusingtheattacker’scredentialandrevisitthestatuspageto
thoughtheattackersuccessfullymodifiedthevictim’sdatawithout
obtainfeedback,whichindicateswhetherthemodificationissuc-
authorization,theresponse-basedoracleincorrectlyconcludesthat
cessful.Byleveragingthisfeedback-drivenoracle,wecanconfirm
novulnerabilityexistsduetothedissimilaritybetweentheattacker
thepresenceofanMBACvulnerabilityifthedatahasbeenaltered
andvictimresponses,ultimatelyleadingtoafalsenegative.
withoutauthorization.
Figure2(b)illustratesafalsepositivecausedbytheresponse-
basedoracleinSuperMarket[11].Inthisscenario,userAlicedeletes
3.2 Challenges
herownorderbysendingarequesttothe/api/v1/order/delete
page.UserBob,actingastheattacker,replicatesthisrequestbut Thisfeedback-drivenoracleanddetectionworkflowmayappear
replacesthecookiewithhisownbeforereplayingit.Duetothe straightforward.However,implementingthisoracleandeffectively
developer having implemented proper access control measures, applyingitforMBACvulnerabilitydetectionpresentssignificant
BobcannotdeleteAlice’sorderwithoutauthorization,meaning difficulties.Twomainchallengesmustbeaddressedcarefully.

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
ChallengeI:Howtoaccuratelyandefficientlyidentifysta-
Algorithm1:IDDGConstruction
tuspagesthatprovidefeedbackinablack-boxcontext?Ac- Input:InitialPage(𝑃 ),Victim’sSession𝑉𝑆
0
curatelyidentifyingthecorrespondingstatuspagesthatprovide Output:IDDESet(𝐸)
| feedbackforamodificationrequestisthefirstcrucialstep.Any |     |     |     |     | 𝐸←∅ |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
errorsoroversightsinthisprocesscandirectlyleadtofalsepos-
|     |     |     |     |     | 2 foreach𝑝 | ∈ExplorePage(𝑃 | ,𝑉𝑆)do |     |
| --- | --- | --- | --- | --- | ---------- | -------------- | ------ | --- |
itivesorfalsenegativesduringvulnerabilitydetection.However, 0
𝑝 ←InterceptRequest(𝑝)
3
thisisnotatrivialtask.Asdemonstrated,wecannotaccessthe ifType(𝑝) ∈{POST,PUT,DELETE}then
4
sourcecodeorquerythedatabaseinablack-boxcontext.Theonly 𝑡𝑜𝑘𝑒𝑛←GenerateToken(𝑝)
5
informationavailablecomesfromHTTPrequestsandtheircorre-
|                                                               |     |     |     |     | 𝑝                | ←ReplaceParams(𝑝,𝑡𝑜𝑘𝑒𝑛)    |             |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | ---------------- | -------------------------- | ----------- | --- |
| spondingresponses.Inwebapplications,therearetypicallythou-    |     |     |     |     | 6                | m                          |             |     |
|                                                               |     |     |     |     | ReleaseRequest(𝑝 |                            | )           |     |
| sandsofsuchrequestsandresponses.Manuallyanalyzingeachone      |     |     |     |     | 7                |                            | m           |     |
| orexhaustivelytraversingthemwouldbehighlytime-consuming.      |     |     |     |     | 8 end            |                            |             |     |
|                                                               |     |     |     |     | foreach𝑝         | ∈HierarchicalTraverse(𝑝)do |             |     |
| Therefore,accuratelyandefficientlyidentifyingthecorresponding |     |     |     |     | 9                | r                          |             |     |
|                                                               |     |     |     |     | ifCheckToken(𝑝   |                            | ,𝑡𝑜𝑘𝑒𝑛)then |     |
statuspagesthatprovidefeedbackfromalargevolumeofrequests 10 r
𝐸←𝐸∪{(𝑝 ,𝑝
| andresponsesisundoubtedlyachallengingtask.            |     |     |     |     | 11  |     | r m ) Type } |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
| ChallengeII:Howtonavigatetheapplicationintothecorrect |     |     |     |     | end |     |              |     |
12
statetocollecteffectivefeedbackforMBACvulnerability
13 end
| detection?Afteridentifyingthestatuspagethatprovidesfeed- |     |     |     |     | 14 end |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
back,thenextstepinvolvesreplacingthesessionwiththoseofan
attacker,replayingthemodificationrequeststothetargetpage,and
revisitingthecorrespondingstatuspagetoverifywhetherunau-
thorizedmodificationstothevictim’sdatahaveoccurred.However, Algorithm2:MBACVulnerabilityDetection
Input:IDDG𝐺,Attacker’sSession𝐴𝑆,Victim’sSession𝑉𝑆,
severalcriticalissuesmustbeaddressedtoensuretheapplication
Output:Vulnerabilities𝑉
isinthecorrectstate,allowingforthesuccessfulreplayofmodifi-
| cationrequests.Forinstance,duringdatadependencyconstruction, |     |     |     |     | 1 𝑉 ←∅ |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | ------ | --- | --- | --- |
DELETE-typeoperationsmaypermanentlyremovecertaindata, foreach𝑝 ∈𝐺 do
|     |     |     |     |     | 2   | m   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
makingitunmodifiable.Inthiscase,whenthescannerreplaysthe ifInsertPage(𝑝 ) UpdatePage(𝑝 )then
|     |     |     |     |     | 3           | m   | or   | m   |
| --- | --- | --- | --- | --- | ----------- | --- | ---- | --- |
|     |     |     |     |     | ReplayReq(𝑝 |     | ,𝐴𝑆) |     |
deleterequesttodetectvulnerabilities,thedatatobedeletedno 4 m
| longerexists,causingthereplayedrequesttofailandresultingin |     |     |     |     | end |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
5
falsenegatives.Furthermore,modificationrequestsmaycontain ifDeletePage(𝑝 )then
|     |     |     |     |     | 6   |     | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameterssuchasCSRFtokens,whichcouldcausethereplayed 𝑡𝑜𝑘𝑒𝑛←GenerateToken(𝑝)
7
requesttofail,thusimpactingtheaccuracyofvulnerabilitydetec-
|     |     |     |     |     | ReInsert(𝑝 | ,𝑡𝑜𝑘𝑒𝑛,𝑉𝑆) |     |     |
| --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- |
t io n . C o n s e q u e n t ly , it i s e ss e n t ia l t o in te r a c t w i t h t h e ap p li ca ti o n 8 m
|              |                          |                        |                          |                     | ReplayReq(𝑝 |     | ,𝐴𝑆) |     |
| ------------ | ------------------------ | ---------------------- | ------------------------ | ------------------- | ----------- | --- | ---- | --- |
|              |                          |                        |                          |                     | 9           |     | m    |     |
| in t h e c o | rr e c t s t at e , th e | r eb y c o l le c ti n | g eff e c t iv e f e e d | b a ck fo r M B A C |             |     |      |     |
10 end
vulnerabilitydetection.
|                                                         |     |     |     |     | 𝑝 ←GetDependencyNode(𝑝 |       |                | ,𝐺) |
| ------------------------------------------------------- | --- | --- | --- | --- | ---------------------- | ----- | -------------- | --- |
|                                                         |     |     |     |     | 11 r                   |       | m              |     |
| 3.3 OurSolution                                         |     |     |     |     | ifCheckVuln(𝑝          |       | ,𝑡𝑜𝑘𝑒𝑛,𝑉𝑆)then |     |
|                                                         |     |     |     |     | 12                     | r     |                |     |
|                                                         |     |     |     |     | 𝑉                      | ←𝑉 ∪𝑝 |                |     |
| Toaddressthesekeychallenges,weproposeournovelsolutions, |     |     |     |     | 13                     | m     |                |     |
end
| whichconsistoftwokeytechniques.                     |     |     |     |     | 14     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
| TechniqueI:Inter-pageDataDependencyConstruction.In- |     |     |     |     | 15 end |     |     |     |
spiredbyBlackWidow[32],weobservethatthereexistsadata
dependencybetweenthedatamanipulatedbythemodificationpage
andthedatadisplayedbythestatuspage.Thisdependencyhelps
identifythestatuspagethatindicatesthestateofthemodifieddata, accessibletothevictim,replacesparametervalueswithrandomly
generatedtokens,andthenreleasestherequest(lines3-8).③Next,
thusactingasfeedbackfordetectingunauthorizedmodifications.
Toestablishsuchdependency,weintroduceanovelgraphdata weemployahierarchicalstrategytotraversethenavigationgraph,
structurecalledInter-pageDataDependencyGraph(IDDG),which prioritizinginpagesthataremorelikelytoserveasfeedback(line
connectsmodificationpagesandtheircorrespondingstatuspages 9).Notably,ourapproachstopsgraphtraversaloncethefirststatus
throughdatadependencyedges(detailedin§4.1). pagecapableofprovidingfeedbackisidentified,thusimproving
efficiency.④Ourapproachrevisitsthestatuspagestorecordany
| Specifically, | we demonstrate | the | IDDG construction | process |     |     |     |     |
| ------------- | -------------- | --- | ----------------- | ------- | --- | --- | --- | --- |
throughAlgorithm1:①OurapproachutilizesSoTAcrawlingtech- tokens. When a token inserted by a modification page appears
niques[32]toexplorethewebpagesofthetargetapplication,using (forINSERTandUPDATE)ordisappears(forDELETE)onastatus
boththevictim’sandattacker’ssessionstoconstructseparatenavi- page,adata-dependencyedgeisestablishedbetweenthestatusand
gationgraphsforeachuser.WethenanalyzetheURLsandcontents modificationpages,alongwithitscorrespondingoperationtype,
ofallpages,filteringoutpublicpagesthatareaccessibletoboth i.e.,INSERT,UPDATE,orDELETE(lines10-12).Byfollowingthese
attackersandvictims.②Duringthevictim’spageexploration(line
steps,ourapproachcanaccuratelyrepresenttheinter-pagedata
2),ourapproachinterceptsrequeststomodificationpagesonly dependencyrelationshipswithintheIDDG.

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
TechniqueII:IDDG-basedMBACVulnerabilityDetection. Input IDDG Construction Module
UtilizingtheconstructedIDDG,ourapproachappliesthenovel ① Token ② NavGraph
Target URL Crawler
feedback-drivenoracletodetectMBACvulnerabilities.Thework- Insertion Traversal
flowforthisphaseisshowninAlgorithm2.⑤Weattempttoreplay
① ③
thevictimrequestssenttomodificationpagesintheIDDGusing Nav ④ IDDE
theattacker’ssession.ForINSERT-andUPDATE-typemodification Accounts Graph IIDDDDGG Connection
pages,wedirectlyreplaytherequest(lines3-5).ForDELETE-type
modificationpages,unlikeothertypes,wefirstlocatethepage Output IDDG-based Vulnerability Detection Module
thatoriginallyinsertedthetokenintothecurrentdeletepage,and ⑥ ⑤
Oracle Validation Request Replay
thenreplaytheinsertionoperationtoinsertthetokenbackonto
thepage(lines6-10).⑥Next,leveragingtheinter-pagedatade- BBAACC VVuullnneerraabbiilliittyy
pendencyrelationshipsrecordedintheIDDG,wefollowthedata Figure3:ArchitectureofBACScan.
dependencyedgetolocateandrevisitthecorrespondingstatuspage
usingthevictim’ssession,detectingvulnerabilitiesbyobtaining of𝑁𝐸isasfollows:
feedback.Specifically,wedesigneddistinctoraclesforeachtypeof 𝑁𝐸={(𝑛 ,𝑛 ) |Navigate(𝑛 )=𝑛 }
prev next prev next
modificationpage(see§4.2).ForINSERTandUPDATEtypes,the
appearanceofanewtokenonthestatuspageindicatesanMBAC IDDGDefinition.TheIDDGisconstructedontopofthenavi-
vulnerability.ForDELETE,theabsenceofapreviouslyexisting gationgraph.IDDGrepresentsthedatadependencyrelationships
tokensignalsanMBACvulnerability(lines11-14). betweenwebpagesbyconnectingpagenodesthroughanewtype
ofdirectededge—inter-pagedatadependencyedge(IDDE).Specifi-
cally,anIDDEconnectsfromamodificationpagenodetoitscorre-
4 BACScan
spondingstatuspagenode.Themodificationpagesprocessrequests
Inthissection,weprovidethedesigndetailsofourBAC(includ- thatalterthedata,e.g.,submittingorders.Thestatuspagesprocess
ingMBACandRBAC)vulnerabilitydetectionapproach,named requeststhatretrievedataanddisplaythisdatatoendusers,e.g.,
BACScan.Figure3illustratesthearchitectureofBACScan,which listingorders.TheIDDEindicatesthatdatamodifiedbythemodifi-
consistsoftwokeymodules. cationpagecanbedisplayedontheconnectedstatuspage.Besides,
theIDDErecordsthemodificationtypeperformedonthedata(i.e.,
• IDDGConstruction(§4.1).ThismoduleconstructstheIDDGto
INSERT,UPDATE,andDELETE),whichfacilitatesfurtheranalysisof
representthedatadependencyrelationshipsbetweenwebpages,
datadependencies.TheformaldefinitionofanIDDEisasfollows:
therebyfacilitatingvulnerabilitydetection.
• BACVulnerabilityDetection(§4.2).ThismoduleinitiatesHTTP 𝐼𝐷𝐷𝐸={(𝑛 mod ,𝑛 status ) |Dependency(𝑛 mod )=𝑛 status }
requestsandleveragesthefeedback-drivenoracleandresponse- Inthispaper,consistentwithBlackWidow[32],wetreatdataread
basedoracletodetectbothMBACandRBACvulnerabilities. pagesthatprocessGETrequestsasstatuspagesandpagesthat
processPOST,PUT,orDELETErequestsasmodificationpages.
4.1 IDDGConstruction Whilethisassumptionisnotalwaystrue,itisgenerallyacceptedin
thecontextofwebapplications.AsdefinedintheHTTPRFC[33],
Inthissection,wefirstpresenttheformaldefinitionoftheIDDG,
GETrequestsareidempotentanddonotmodifydata,makingthem
followedbyadetailedexplanationofhowBACScanconstructsthe
suitableforcategorizationasdatareadoperations.Besides,our
IDDGusingoneexample.
evaluationresultsin§5.5demonstratethatthisassumptionhasno
significantimpactontheaccuracyoftheIDDGortheeffectiveness
4.1.1 IDDG Definition. The IDDG is constructed on top of the
ofvulnerabilitydetection.Wediscussthisissuefurtherin§6.
navigationgraphandrepresentsthedatadependencyrelationship
betweenpagesthroughspecialnodesandedges.Weintroducethe 4.1.2 IDDG Construction. We now describe how BACScan con-
structure of the navigation graph and utilize graph notation to structsthenavigationgraphandconnectstheIDDEbetweenpages.
rigorouslydefinetheformalrepresentationoftheIDDG. PageExploration.BACScanfirstexploreseachwebpageusinga
NavigationGraphDefinition.NavigationGraphisadatastruc- crawlertoconstructthenavigationgraph.Inaccordancewiththe
ture widely used in traditional tasks such as web vulnerability state-of-the-artcrawler[31,32],BACScanexploresthewebpages
scanning[29,31,32].Itrepresentshowpageswithinawebapplica- throughfourtypesofactions,i.e.,extractingstaticURLs,submitting
tionareaccessiblefromonetoanotherthroughnavigationedges. forms,interactingwithiframes,andtriggeringJavaScriptevent
Followingexistingwork,weintroducethekeycomponentsofthe handlers(e.g.,clicks)withinthepages.Thismethodensuresthat
navigationgraph,i.e.,thenodesandedges.Thenodesrepresentin- BACScanconductsacomprehensiveexplorationofthecurrentweb
dividualwebpages,suchastheloginpage.Webcrawlerstypically pages.Subsequently,BACScantreatsthepagesgeneratedthrough
collectnewlyaccessiblewebpagesbyexploringalreadyvisited theseactionsasnewpagenodes,linkingthemtothecurrently
pages.Theedgescapturetherelationshipsbetweenpagenodes, exploredpagethroughnavigationedges.Theseedgesrepresent
indicatinghowonepagecannavigatetoanother,whichmayoccur howtheactionsfacilitatenavigationfromonepagenodetoanother,
throughhyperlinks,eventhandling,formsubmissions,etc. therebyformingthenavigationgraphofthetargetapplication.
Weuse𝑛torepresentthenodesinthenavigationgraph,and TokenInsertion.Duringtheexplorationofeachpage,BACScan
𝑁𝐸torepresentthesetofnavigationedges.Theformaldefinition interceptsallissuedmodificationrequests.Then,apartfromcertain

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
structuredparameters,suchasdateandemail,BACScanreplaces ❷RequestParameter.BACScanthenanalyzestherelationship
otherparametervaluesintherequestwithuniquetokens,andsub- betweentheparametersoftheinterceptedmodificationpage(i.e.,
sequentlyreleasestheinterceptedrequestsonebyone.Specifically, 𝑝 𝑖)andthecontent(i.e.,HTTPresponse)ofpreviouslyaccessed
wegeneratetheseuniquetokensaspseudo-randomstringsofsix pages.Specifically,asshowninEquation1,BACScanparsesthe
lowercasecharacters,e.g.,axdvhn.Thisrandomnessensuressuffi- parameternamesfromthemodificationrequestandcheckswhether
cientlyhighentropytopreventthemfrombeingmistakenforother theyappearinthecontentofaccessedpages.TheresultofI(𝑝 𝑖 ∈𝑟)
stringswithintheapplication. issetto1iftheparameterisfoundinthecontent,or0otherwise.
Itmustbeacknowledgedthatsomedatadependenciesarisefrom Thismetriciswell-founded.Forinstance,consideramodification
structureddata,e.g.,email,andreplacingonlyunstructuredparam- request that contains an address parameter, and another page
eterswithuniquetokensmaymisstheserelationships.Neverthe- presentsinformationrelatedtoaddresses.Itisreasonabletoinfer
less,pageswithMBACvulnerabilitiestypicallycontainnumerous that,comparedtootherpages,thisdatareadpageismorelikelyto
unstructuredparameters(e.g.,username,address)thatcanbere- exhibitadatadependencywiththemodificationrequest.
placed.Therefore,wecanleveragetheseparameterstoestablish ❸ Navigation Distance. The distance between the previously
thedatadependencyrelationshipsbetweenpages,whichdonot accessed status pages and the intercepted modification page in
significantlyaffectthedetectionofMBACvulnerabilities.Asshown thenavigationgraphisanotherkeyfactorconsideredbyBACScan,
in§5.2,ourevaluationresultsdemonstratethatthefalsenegatives denotedas𝐷𝑖𝑠𝑡(𝑚,𝑟).Typically,modificationpagesarecloselyas-
causedbythestructuredparametersofBACScanareonly2.90%. sociatedwiththeircorrespondingstatuspagesregardingbusiness
HierarchicalNavigationGraphTraversal.Foreachintercepted functionality,anddevelopersdesignthemtorequireminimalin-
modificationrequestwithaninsertedtoken,BACScanattemptsto teraction,thuspositioningthemrelativelyclosetoeachotherin
traversethenavigationgraphtofindthecorrespondingstatuspage. thenavigationgraph.Therefore,BACScanassignshigherscoresto
Onestraightforwardmethodistorevisitallwebpagestosearchfor pagesthatarecloserindistance.
thestatuspage.However,thisapproachishighlytime-consuming Asshownin§5.4,thishierarchicalstrategyenablesBACScan
andimpractical.Therefore,BACScanemploysahierarchicaltraver- toreducethetotalnumberofpagevisits,therebyimprovingthe
salstrategytoefficientlyidentifythecorrespondingstatuspage, efficiencyofnavigationgraphtraversalandresultingina109.10%
therebyestablishingdatadependency.Specifically,thehierarchical improvementinoverallperformance.
strategyinvolvesacomprehensiveevaluationprocessofallpages IDDEConnection.Inthefinalstep,BACScanestablishesIDDE
toprioritizeinrevisitingthemostpromisingones.Thetraversal byanalyzingtherelationshipbetweenthetokeninsertedbythe
stopsoncethefirstpagewithadatadependencyontheintercepted modificationpageandthecontentoftherevisiteddatareadpage.
modificationrequestisidentified.Thisapproachhelpsavoidindis- Specifically,basedonthetypeofoperationperformedonthetoken,
criminatetraversalofallpages,thusfacilitatingamoreefficient wecategorizetheIDDEintothreetypes:1)Iftheinsertedtoken
identificationofthestatuspagesthatprovidefeedback. appearsinthecontentofthereadpage,BACScantreatsitasthe
Toachievethis,ascoringalgorithm isdesignedtoassessthe correspondingstatuspageandestablishesanINSERT-typeedge
likelihoodofbeingastatuspageofspecificmodificationpages. betweenthetwonodes.2)Iftheinsertedtokenisfoundinthe
Thisalgorithmintegratesmultiplefactors,includingURLsimilarity, read page and a previously existing token disappears, BACScan
requestparameterrelevance,andthedistancetotheintercepted createsanUPDATE-typeedge.3)Ifonlyapreviouslyexistingtoken
modificationpagewithinthenavigationgraph.BACScanthense- disappears from the read page, BACScan forms a DELETE-type
lectsthepagewiththehighestscoreforprioritizedaccess.The edge.Formodificationpagenodesthatoperateonthesametoken,
detailsofthescoringalgorithmanditsbreakdownareasfollows: BACScan groups them into a single node cluster and labels the
modificationtype(i.e.,INSERT,UPDATE,orDELETE)foreachpage
𝑆(𝑚,𝑟)= 1+𝑆𝑖𝑚 𝑤 1 (𝑚,𝑟) +𝑤 2 · 𝑛 1∑︁ 𝑛 I(𝑝 𝑖 ∈𝑟)+ 𝐷𝑖𝑠𝑡 𝑤 (𝑚 3 ,𝑟) (1) tofacilitatefurtherBACvulnerabilitydetection.
𝑖=1
4.1.3 IDDGConstructionExample. WerefertoFigure4asanexam-
❶URLSimilarity.BACScananalyzestheresponseoftheinter- pletoprovideadetailedexplanationofhowBACScanconstructsthe
ceptedmodificationrequestandattemptstoextracttheredirect IDDG.Figure4(a)illustratesawebpagedisplayingorderdata.The
URLprovidedintheresponse,whichmayappeareitherinthere- enduseraccessesthisfunctionalityviathe/orderListpathto
sponseheader(e.g.,Location:/order)ortheresponsebody(e.g., viewhersubmittedorders.Figure4(b)showstheconstructedIDDG
redirect:/order).Thisdesignchoiceisbasedontheobservation oftheorderdata.TheIDDGconsistsofthreenodes,eachrepresent-
thatdeveloperstendtoredirectuserstoapagedisplayingthemod- ingadding,viewing,anddeletingorders,respectively.Toelaborate,
ifieddata,i.e.,thestatuspage,afteramodificationisperformed. wetaketheIDDEbetweenthe"AddOrder"and"ListOrder"pages
GiventhatredirectURLsmaycontainvariouspathparametersthat asanexampletodescribeitsconstructionprocessindetail.Initially,
couldcausedirectURLmatchingtofail,BACScanthusleverages duringthepageexplorationphase,BACScanidentifiesthatthe"List
theLevenshteindistancealgorithm[59]toassessthesimilarity Order"pagecannavigatetothe"AddOrder"pages,therebyconnect-
between the redirect URL and the URLs of previously accessed ingthetwonodesusingnavigationedges(blackline).Subsequently,
pages(denotedas𝑆𝑖𝑚(𝑚,𝑟)inEquation1),assigninghigherscores BACScaninterceptstheordersubmissionrequest,replacestheor-
tomoresimilarpages.Additionally,incaseswherenoredirection deraddressparameterwithapseudo-randomlygeneratedtoken,
informationisfoundintheresponse,BACScandefaultstousingthe andtraversesthenavigationgraphtolocatethisinsertedtoken.
URLofthemodificationpageasasubstitutefortheredirectURL. Finally,byobservingandanalyzingthetoken’sbehavior(e.g.,its

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
List Order Page Order Node Cluster pagemayhavealreadybeenpermanentlyremoved.Consequently,
• Order 1 Token: ${token} replayingarequesttodeletenon-existentdataleadstoaserver
• Address 1: ${token} > INSERT: /addOrder; Param: Product, Address error.Forinstance,duringIDDGconstruction,ifaDELETE-typere-
• Add Order Del Order
• Order 2
> DELETE: /delOrder; Param: Orderld questhasalreadyremovedanorderwiththeparameterOrderId=1,
• Address 2: . . . > SELECT: /orderList; Param: None replayingthesamerequestwouldfailastheordernolongerexists
a) An example of the Order c) The corresponding Node Cluster andcannotbedeletedagain.
Toaddressthisissue,BACScanfirstleveragesthenodecluster
tolocatethepagethatoriginallyinsertsthetokenremovedbythe
DELETEpage.ItthenrevisitsthecorrespondingINSERT-typepage
URL: POST /addOrder URL: GET /orderList URL: POST /delOrder
toreinsertthetokenintotheapplication,modifyingtheparameters
Param: Product=iPhone Response: Param: OrderId=1 ofthereplayedDELETErequesttoreferencethenewlyinserted
&Address=${token}
{"Product": "iPhone" , data(e.g.,OrderId=2).Thisapproachensuresthesuccessfulreplay
Response: "Success" "Address": "${token}"} Response: "Success"
ofDELETE-typemodificationrequests.
Add Order Page List Order Page Delete Order Page Feedback-drivenOracleValidation.Then,BACScanfollowsthe
IDDEtolocateandrevisitthestatuspagewithadatadependency
Page Node Property Navigation Edge Data Dependency Edge onthereplayedmodificationrequest,usingthevictim’ssession
toobtainfeedbackonwhethertheunauthorizedmodificationsuc-
b) The constructed IDDG for the Order
ceeded.Specifically,BACScanadoptsdifferentdetectionstrategies
Figure4:AnexampleofconstructedIDDGandCluster. basedonthetypeofmodificationrequest.
• ForINSERT-typeoperations,theappearanceofanewlyinserted
appearanceorremovalonthepage),BACScanconfirmsthetoken’s tokenonthestatuspageactsasthefeedback,directlyindicating
presenceonthe"ListOrder"page.Asaresult,BACScanestablishes anMBACvulnerability.Thisfeedbackconfirmsthatthescanner
anIDDEtorepresentthedatadependencyrelationshipbetweenthe canobserveunauthorizedinsertion.
"AddOrder"and"ListOrder"pages(redline).Figure4(c)presents • ForUPDATE-typeoperations,thedetectionofanewtokenalong-
theclusterofnodesthatoperateonorderdata.BACScanprecisely sidethedisappearanceofanexistingtokenonthestatuspage
identifiesandmarksthetoken’slocationwithinthewebpage,en- signalsanMBACvulnerability.
ablingthegroupingofsubsequentmodificationstothistoken(e.g., • ForDELETE-typeoperations,thedisappearanceofapreviously
insertion,deletion)intoasingleoperationalcluster.Thisclustering existing token from the status page serves as evidence of an
processfurtherfacilitatesthedetectionofBACvulnerabilities. MBACvulnerability.
4.2 BACVulnerabilityDetection For example, in Figure 4 (b), BACScan uses the victim’s session
to insert token-A via the /addOrder modification page. The in-
Inthissection,weelaborateonhowBACScanachieveseffective
sertedtoken-Acanbeviewedonthecorrespondingstatuspage
BACvulnerabilitydetection.Specifically,BACScanutilizestwodis-
(i.e.,/orderList).Next,BACScanreplacesthevalueofAddresspa-
tinctoracles,i.e.,thefeedback-drivenoraclefordetectingMBAC
rameterwithtoken-Bandreplaysthe/addOrderrequestusing
vulnerabilitiesandtheresponsesimilarity-basedoracleforidenti-
the attacker’s session. Finally, BACScan revisits the status page
fyingRBACvulnerabilities.
/orderListusingthevictim’ssessiontocheckforthepresenceof
4.2.1 MBACVulnerabilityDetection. TheprocessofdetectingMBAC token-B.Iffound,BACScanreportsanMBACvulnerability.
vulnerabilitiesprimarilyconsistsoftwostages:ModificationRe-
questReplayandFeedback-drivenOracleValidation. 4.2.2 RBACVulnerabilityDetection. ForRBACvulnerabilityde-
ModificationRequestReplay.BACScanattemptstoreplaythe tection,BACScanemploysthewidelyadoptedthree-stepapproach
victimrequestssenttomodificationpagesintheIDDGusingthe described in §2.3. First, BACScan uses both the victim’s and the
attacker’ssession,replacingthetokenintheparameterswitha attacker’ssessionstoexplorethewebapplication,separatelycol-
newlygeneratedtoken.Giventhatmodificationrequestsaretypi- lectingthepagesaccessibletoeach,alongwiththecorresponding
callyPOSTorsimilartypesthatoftenrequireCSRFtokens,directly pagecontent(i.e.,HTTPresponses)foreachuser.Second,BACScan
replayingtheserequestsmayfail.Toaddressthis,BACScantraces adoptsaSoTAapproach[35]tofilteroutpublicpagesaccessibleto
backalongthenavigationedgestolocatetheprecedingdataread boththeattackerandthevictim.Specifically,itcompareseachpage
pageofthetargetmodificationpage.Then,startingfromthisread intheattacker’sandvictim’snavigationgraphs,treatingpageswith
page,BACScanfollowsthenavigationedges,executingrelatedac- identicalURLsandcontentaspublic.ThisprocessallowsBACScan
tionssuchastriggeringeventhandlersandsubmittingforms,until toselectonlythepagescontainingsensitivedatathatareexclu-
itsuccessfullyreachesthetargetmodificationpage. sivelyaccessibletothevictim.Third,BACScanutilizestheattacker’s
Furthermore,BACScanemploysdistinctstrategiestoreplaythe sessiontoreplaytheGETrequestssenttodatareadpageswithinthe
modificationrequestbasedonthetypeofoperation.ForINSERT- navigationgraph.Thisstepsimulatesunauthorizedaccessattempts
andUPDATE-types,itdirectlyreplaystherequesttoattemptunau- bytheattacker.BACScanthenappliesaSoTAresponsesimilarity-
thorizedmanipulationofthevictim’sdata.ForDELETE-types,how- basedoracle,asdescribedin[35],todetectRBACvulnerabilities.
ever,directreplayoftenfails.Thisissuearisesbecause,duringthe Ifthesimilarityscoreexceedsapredefinedthreshold(setto0.7,
constructionoftheIDDG,thetargetdataassociatedwiththedelete following[35]),BACScanconcludesthatsensitivedataintendedfor

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
thevictimisalsoaccessibletotheattacker,therebyreportingan Table1:Breakdownofourevaluationdataset,includingtheir
names,popularity(i.e.,stars),thenumberofestablishedID-
RBACvulnerability.
DEs,detectedBACvulns,andassignedCVEs.
5 Evaluation
|     | TestingSet | #CVEs/Vulns1 | #IDDEs #Stars | #Language |
| --- | ---------- | ------------ | ------------- | --------- |
5.1 ExperimentalSetup
|     | Mall-swarm | 0+1/1+1 | 49 11,988 | Java |
| --- | ---------- | ------- | --------- | ---- |
Implementation.Ourprototypeimplementationfollowstheap-
|     | Newbee_mall | 2+2/2+3 | 25 10,972 | Java |
| --- | ----------- | ------- | --------- | ---- |
proachpresentedinSection§4.Forthecrawler,ourprototypefol-
|     | Invoiceninja | 1+0/2+0 | 150 8,192 | PHP |
| --- | ------------ | ------- | --------- | --- |
lowstheBlackWidow[32]toautomaticallyexplorewebpages(e.g.,
triggerJavaScripteventhandlerswithinpages),therebyconstruct- PrestaShop 0+0/0+0 49 8,139 PHP
|     | XMall | 5+4/6+4 | 26 7,135 | Java |
| --- | ----- | ------- | -------- | ---- |
ingthenavigationgraph.Inaddition,ourprototypeusesPython
andPlaywright(maintainedbyMicrosoft[10])tointeractwith SpringBlade 0+0/0+0 6 6,298 Java
thewebbrowser,therebyinterceptingrequestsandconstructing Ruoyi 0+0/0+0 71 6,124 Java
theIDDG.Forthehyper-parametersinhierarchicaltraversalstrat-
|     | Joomla | 0+0/0+0 | 21 4,785 | PHP |
| --- | ------ | ------- | -------- | --- |
egy,weconductedsensitivitytestingusingourground-truthsetto
|     | Ampache | 1+0/2+0 | 181 3,500 | PHP |
| --- | ------- | ------- | --------- | --- |
fine-tunetheparameters,ultimatelysetting𝑤 ,𝑤 ,and𝑤
1 2 3 to0.4,
|     | OpenEMR | 4+2/5+6 | 92 3,140 | PHP |
| --- | ------- | ------- | -------- | --- |
0.3,and0.3,respectively.Intotal,theentireprototypeconsistsof
|     | Supermarket | 5+2/6+3 | 13 2,006 | Java |
| --- | ----------- | ------- | -------- | ---- |
4,116linesofPythoncode.AllexperimentsrunonanUbuntu22.04
machine,equippedwitha64-coreCPUand256GBofmemory. PhpBB 0+0/0+0 32 1,836 PHP
Experiments.Ourevaluationseekstoanswerthefollowingfour Apache_inlong 2+0/4+2 143 1,370 Java
| researchquestions: | Webid | 2+2/5+2     | 59 114 | PHP |
| ------------------ | ----- | ----------- | ------ | --- |
|                    | Total | 22+13/34+22 | 917    | / / |
• RQ1:HoweffectiveisBACScanindetectingBACvulnerabilities
withinreal-worldapplications? GroundTruthSet #KnownVulns2 #IDDEs #Stars #Language
• RQ2:HowdoesBACScanperformcomparedtoSoTAapproaches?
|     | Memos-0.9.0 | 4+5 | 27 34,380 | Go  |
| --- | ----------- | --- | --------- | --- |
• RQ3:HowefficientisBACScaninperformingtheanalysis?
|     | WordPress_SPM-4.57 | 6+1 | 44 19,453 | PHP |
| --- | ------------------ | --- | --------- | --- |
• RQ4:HoweffectiveistheconstructionofIDDG?
|     | Snipe_it-5.0.3 | 0+3 | 57 11,152 | PHP        |
| --- | -------------- | --- | --------- | ---------- |
|     | Lunary-1.2.7   | 6+6 | 16 1,085  | TypeScript |
Dataset.Ourdatasetcomprises20popularopen-sourcewebappli-
cations.Amongthese,14applicationsaredesignatedasthetesting MyBloggie-2.1.4 2+0 15 281 PHP
set,while6applicationswith44knownBACvulnerabilitiescon- Collabtive-2.1 6+5 59 215 PHP
stitutetheground-truthset.Theseapplicationshavebeenwidely
|     | Total | 24+20 | 218 | / / |
| --- | ----- | ----- | --- | --- |
evaluatedinpreviousstudiesandareimplementedinvariouslan-
guages,includingJava,PHP,andGo,furtherprovingthatBACScan 1Thenumberof0-dayBACvulnerabilitiesdiscoveredbyBACScanandthe
islanguage-independent.Wemanuallysetuptheruntimeenviron- assignedCVEs.Forexample,‘22+13/33+21’means33MBACand21
mentsforall20applicationsandappliedBACScantodetectBAC RBACvulnerabilities,with22MBACand13RBACCVEsassigned.
2ThenumberofknownBACvulnerabilitiesintheapplication.Forexample,
vulnerabilitieswithinthem.Detailedinformationabouttheseap-
plicationsisprovidedinTable1.Thestep-by-stepconstruction ‘24+20’means24MBACand20RBACvulnerabilities.
processisasfollows.
reviewrequiressignificantmanualeffort,weprioritizedingath-
• TestingSet.Wecollected14widely-usedwebapplicationsfrom eringBACvulnerabilitiesfromsourcessuchasHuntr[7],Ex-
popularopen-sourcerepositories(e.g.,GitHub[14])basedonthe ploitDB[6],andexistingstudies[43,58]thatprovidePoCs.Specif-
ically,thecollectionwasbasedonkeywords(e.g.,brokenaccess
followingcriteria:(1)Consideringtheimportanceofdatasetreli-
control,missingauthorization)andCWEs(e.g.,CWE-200[3],
abilityandrepresentativeness,eachselectedapplicationhasbeen
widelyevaluatedinpreviousstudies[26,34,43,48,56,58].(2)To CWE-284[4]).Thevulnerabilitydisclosuredateswererestricted
ensuretheirpopularity,werequirethattheselectedapplications to January 2022 to January 2024. Additionally, to reduce the
shouldhaveover100starsonGitHub.(3)Additionally,todemon- manualeffortinvolvedinsettingupruntimeenvironments,we
stratethatBACScanisprogramminglanguage-independent,the preferredtoincludeapplicationswithmultipleknownvulnera-
bilitiesintheground-truthset.Intheend,ourground-truthset
selectedapplicationsincludemultipleprogramminglanguages.
Consequently,ourtestingsetcomprises7PHP-basedapplica- consistsof44validatedBACvulnerabilitiesfrom6applications,
tionsand7Java-basedapplications,amongwhich13applications including24MBACvulnerabilitiesand20RBACvulnerabilities.
haveover1,000stars,and1applicationhasover100stars. Table1presentsadetailedbreakdownshowingthedistribution
| •   | ofthese44vulnerabilities. |     |     |     |
| --- | ------------------------- | --- | --- | --- |
Ground-truthSet.Wecollectedapplicationscontainingknown
BACvulnerabilitiestoserveasthegroundtruthset.Giventhat BACScanSetup.Foreachapplication,wesetuptwovictimusers
manyknownCVEslackdetailedvulnerabilityinformation,and andoneattackeruserforBACScan.Amongthetwovictimusers,
constructingvulnerabilityproof-of-concept(PoC)throughcode onesharesthesameroleastheattackeruser(e.g.,aregularuser),

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
Table2:TheeffectivenessofBACScaninBACvulnerabilitydetection(RQ1).
MBACVulnerability RBACVulnerability
Dataset
TP FP FN Prec(%) Recall(%) TP FP FN Prec(%) Recall(%)
GroundTruthSet 20 0 4 100.00% 83.33% 15 3 5 83.33% 75.00%
TestingSet 33 0 / 100.00% / 21 5 / 80.77% /
Total 53 0 / 100.00% / 36 8 / 81.82% /
while the other has a higher role (e.g., an administrator). Then, response similarity algorithm is highly effective for RBAC vul-
BACScan constructs the IDDG for each victim user and replays nerabilitydetection,itcanalsoproducefalsepositivesincertain
requestsusingtheattacker’scookietodetectBACvulnerabilities. scenarios.Thesefalsepositivesarisefromthehighlyflexibleand
diversepagecontentandHTMLstructuresacrossdifferentappli-
cations,whichmakethepredefinedfixedsimilaritythresholdless
effectiveinhandlingthesevariations,resultinginfalsepositives.
5.2 RQ1:Effectiveness
FalseNegatives.For9falsenegatives,theprimarycausescanbe
WeevaluatedtheeffectivenessofBACScanindetectingBACvul- attributedtotwomainaspects.Firstly,2falsenegativesresulted
nerabilitiesontwoseparatedatasets:theground-truthsetandthe fromincompleteconstructionoftheIDDG.Forexample,consider
testingset. themissedvulnerabilityinWeBid[17].BypassinganauctionIDin
ResultOverview.Table2providesthedetailedresults.Intotal, theHTTPrequestparameters(e.g.,auction=1),anattackercan
BACScandetected89BACvulnerabilitieswithintheground-truth exploitthisvulnerabilitytorelistanyclosedauctionwithoutautho-
andtestingsets,ofwhich54arepotential0-dayBACvulnerabilities rization.However,sincethisHTTPrequestonlycontainsaninteger
and35areknownBACvulnerabilities. parameter,BACScancannotreplaceitwithuniquestringtokens,
Specifically,forMBACvulnerabilities,withintheground-truth whichisessentialforestablishinginter-pagedatadependencies.
dataset,BACScansuccessfullydetected20MBACvulnerabilities, Consequently,BACScanfailedtodetectthisvulnerability.Secondly,
with0falsepositivesand4falsenegatives.Theprecisionandre- 7falsenegativeswerecausedbythecrawler’slimitedcodecoverage.
callrateswerenotablyhighat100.00%and83.33%,respectively. Achievingcomprehensiveexplorationofallwebpagesthrough
Additionally,inthetestingset,BACScanreported33potential0- automated crawlers remains a widely recognized challenge. Al-
dayMBACvulnerabilities.OwingtoBACScan’sabilitytodirectly thoughweutilizedstate-of-the-artcrawlertechnology,consistent
provideURLsandparametersassociatedwiththevulnerabilities, withnumerousexistingstudiesthatrelyoncrawler-basedexplo-
we could efficiently check the vulnerability reports. Ultimately, ration,certainpagesinevitablyremainedunexplored[32,39].This
weverifiedthatall33MBACvulnerabilitiesaretrulyexploitable coveragelimitationsubsequentlyledtoundetectedvulnerabilities
withinthetestingset.ForRBACvulnerabilities,BACScanachieved onthosepages.
aprecisionrateof83.33%andarecallrateof75.00%ontheground
truthset.Onthetestingset,BACScandetected21zero-dayRBAC
5.3 RQ2:Comparison
vulnerabilitieswithanaccuracyof80.77%.
VulnerabilityDisclosure.Attackerscanexploitthesevulnerabili- Inthispart,wecomparetheeffectivenessofBACScanwithtwo
tiestoleakprivateuserdataorevendeletedatastoredwithinthe baselines.Forathoroughevaluation,weusethe54(33MBAC+
application,therebyseverelycompromisingdataconfidentialityand 21RBAC)verified0-dayvulnerabilitiesreportedbyBACScanand
integrity.Forexample,avulnerabilityidentifiedinOpenEMR[8] 44 known BAC vulnerabilities as the vulnerability ground truth
allowsattackerstomodifyanypatient’sdiagnosisormedications, set, assessing the precision and recall rates of the two baseline
posingaseriousthreattopatient’sprivacy,health,andevenlife. approachesacrosstheentiredataset.
Thesesecuritybreachesunderscoretheurgentneedforeffective BaselineSetup.Wefirstdescribethesetupofthesetwobaselines,
BACvulnerabilitydetectionmechanismstosafeguardbothdata i.e.,EvoCrawl[35]andBurpSuite[12].
privacyandintegrityincriticalwebapplications.
Therefore,wepromptlyreachedouttothecorrespondingdevel- • EvoCrawlisthestate-of-the-artapproachtoBACvulnerability
operstoreportallconfirmedvulnerabilitiesthroughtheirdedicated detectionandwillbepresentedatNDSS2025[35].Itscodeisavail-
emailaddressesandvulnerabilityreportingforms.Adheringtore- ableasopensourceonGitHub[5].GiventhatEvoCrawlitself
sponsibledisclosurepractices,wewillrefrainfrompubliclyreleas- includesacrawlingmoduleandanoraclespecificallydesigned
inganyunresolvedvulnerabilitiesuntiltheyhavebeenaddressed. fordetectingBACvulnerabilities,weonlyneededtoprovidethe
Todate,39vulnerabilitieshavebeenconfirmedbythedevelop- targetURLanduserlogincredentialstoinitiatedetection.To
ers,andwehavereceived35CVEidentifiersinacknowledgment, preventthecrawlerfromexceedingruntimelimits,thecrawling
including22MBACand13RBACones. processwasrestrictedtoamaximumof8hours.
FalsePositives.Forall8falsepositivesofBACvulnerabilities, • BurpSuiteisacomprehensivecommercialblack-boxscanner
weconductedadetailedanalysisandfoundthattheyaremainly thatsupportsenhancedvulnerabilitydetectionthroughvarious
causedbythelimitedresponsesimilarityalgorithm.Althoughthe extensions.WeinstalledtheAutorizeextensionfromBurpSuite’s

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
Table3:ComparisonbetweenBACScanandbaselinesinBACvulnerabilitydetection(RQ2).
MBACVulnerability RBACVulnerability
Baselines
TP FP FN Prec(%) Recall(%) TP FP FN Prec(%) Recall(%)
EvoCrawl 17 16 40 51.52% 29.82% 23 9 18 71.88% 56.10%
BurpSuite 31 19 26 62.00% 54.39% 35 15 6 70.00% 85.37%
BACScan 53 0 4 100.00% 92.98% 36 8 5 81.82% 87.80%
BAppStore[13],enablingeffectivedetectionofBACvulnera- takenforvulnerabilitydetectionwasthencalculated,allowingus
bilities.Next,weconfiguredthelogincredentialsinBurpSuite’s toaccuratelyassesstheperformanceofBACScan.
Dashboardmoduleandinitiatedthevulnerabilitydetectionby Additionally,toevaluatetheimprovementinperformancepro-
clickingthe“NewScan”button. videdbythehierarchicaltraversalstrategy,wecreatedavariant
ofBACScan,namedBACScan-Random.Thisvariantdisablesthehi-
FalsePositives.AsshowninTable3,BACScansurpassesEvoCrawl
erarchicalstrategyandinsteadrandomlyselectspagesfromthe
andBurpSuiteby94.12%and61.29%intheprecisionrateofMBAC
navigationgraph.Wesetan8-hourtimeoutforthisvarianttolimit
vulnerabilitydetection,respectively.Weconductedanin-depth
itsexecutiontime.Bycomparingtheresultsofbothversions,we
analysisofallthefalsepositivesreportedbyEvoCrawlandBurpSuite.
canevaluatethespecificcontributionofthehierarchicaltraversal
ApartfromthefalsepositivecausesinBACScan(i.e.,insensitive
strategytotheoverallperformance.
resourcesandresponsesimilarityalgorithm),wefoundthatthe ResultAnalysis.Figure5showsthetimetakenbyBACScanand
primaryreasonforthesefalsepositivesistheinherentdefectin BACScan-Randomtoanalyzetheentiredataset.Onaverage,BACScan
theirresponse-basedoracle,asdescribedin§2.3.Thisoriginoffalse
requires1.1hourstocompletethetaskofdetectingBACvulnera-
positivesisunderstandable,asmanyMBACvulnerabilitiesdonot
bilitiesinagivenapplication.Thisanalysistimeencompassesboth
includeindicatorsofsuccessfuloperationsintheirdirectresponses.
theIDDGconstructionandthevulnerabilitydetectionphases.Com-
Forexample,inSupermarket[11],theresponsetoanorderdeletion
paredtootherdynamictestingapproachesthatrelyoncrawlers[31,
operationalwaysreturnsa302statuscode,regardlessofwhether 32,35,56],weconsiderBACScan’sperformancetobeacceptable.
thedeletionsucceeds.Suchoutcome-independentresponsesrender Incomparison,BACScan-Randomrequiresanaverageof2.3hours
theresponse-basedoracleineffective,leadingtofalsepositivesin
forvulnerabilitydetection,representingaperformancedecreaseof
thesebaselinetools. 109.10%relativetoBACScan.Insomeapplications(e.g.,OpenEMR),
FalseNegatives.TherecallratesofEvoCrawlandBurpSuitefor BACScan-Random’sperformancedroppedbyasmuchas153.24%,ul-
MBAC vulnerability detection result are 29.82% and 54.39%, re- timatelyleadingtoatimeout.ThisindicatesthatBACScan-Random
spectively.Ourcomprehensiveanalysisofallthesefalsenegatives
spendssignificantlymoretimesearchingfortheinsertedtoken
revealedthat,beyondthosecausedbylimitedcodecoverageinthe withinthenavigationgraph,whileBACScanavoidsthisoverhead
crawlers,additionalfalsenegativesprimarilystemfromtwofactors.
byemployingthehierarchicaltraversalstrategy.Moreover,asthe
Firstly,mostofthefalsenegativesinEvoCrawlandBurpSuitearise
scaleoftheapplicationsincreases,theperformancedegradation
frominherentlimitationsintheresponse-basedoracle.Forinstance, ofBACScan-Randombecomesmorepronounced.Thisisbecause,as
inOpenEMR[8],responsestomodificationrequestsarelinkedto
thesizeoftheapplicationgrows,thenavigationgraphexpands,
theidentityoftherequestsender.Specifically,whenanattacker
leadingtolongertraversaltimes.Theseexperimentalresultshigh-
submitsarequesttomodifyavictim’sdata,theresponsereflects
lightthesignificantperformanceimprovementsachievedbythe
onlydataassociatedwiththeattacker,regardlessofwhetherthe hierarchicaltraversalstrategyinBACScan.
modificationsucceeds,andexcludesanyofthevictim’sdata.This
account-specificresponseleadstolowsimilaritybetweenattacker
5.5 RQ4:IDDG
andvictimresponses,causingthesebaselinestomistakenlyassume
novulnerability,resultinginfalsenegatives.Secondly,21falseneg- TheIDDGiscrucialtoourfeedback-drivenoracle,makingitspreci-
ativesinEvoCrawlstemfromitsuser-specificdatafilteringstrategy. sionvitalforeffectiveMBACvulnerabilitydetection.Toensureits
AsoutlinedinSectionIII.CoftheEvoCrawl’spaper[35],thisstrat- reliability,wemanuallyevaluatethecorrectnessoftheconstructed
egyfiltersoutuser-specificelements(e.g.,username)basedonpage IDDGandbreakdownthedetaileddataoftheIDDE,therebydemon-
similarity.However,thisapproachinadvertentlyexcludessubstan- stratingitsimportanceinvulnerabilitydetection.
tialamountsofuser-specificandsensitivedata,suchasindividual ResultAnalysis.AsshowninTable1,wepresentthebreakdown
userorders,resultinginnumerousfalsenegatives.
ofthe1,135IDDEsconstructedbyBACScanacrossallevaluated
applications.Giventheconsiderablemanualeffortrequiredtover-
ifycorrectness,werandomlyselected10%(113)ofthetotal1,135
5.4 RQ3:Efficiency
IDDEstoassesstheirprecision.Ourevaluationrevealedthatonly4
EvaluationSetup.Inthispart,weevaluatedtheperformanceof (3.54%)ofthesampledIDDEswereincorrectlygenerated.Adetailed
BACScaninanalyzingtheentiredataset,focusingonitsefficiency analysisofthesefalsepositivesindicatesthattheywereallcaused
indetectingvulnerabilities.Toensuretherobustnessofourresults, byGET-typemodificationpages.Asdescribedin§4.1.1,BACScanas-
eachwebapplicationwastestedintworounds.Theaveragetime sumesthatonlyPOSTrequestsmodifydata.Consequently,during

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
Figure5:TimeconsumptioncomparisonbetweenBACScanandBACScan-Random.
// PoC send to Modification Page // Response from Status Page before Attack // PoC send to Modification Page
1 POST /interface/patient_file/add_transaction.php 1 GET /member/orderDetail 8 POST /member/delOrder
2 Cookie: Attacker's Cookie 2 Cookie: Victim's Cookie 9 Cookie: Attacker's Cookie
3 form_date=2024-01-01&form_note=${token} 3 <html> <titiel>Order Detail</title> 10 addressId=1
4 <div class="id">1</div> // Response from Status Page after Attack
// Response from Status Page 5 <div class="addr">${token}</div> 11 GET /member/orderDetail
4 GET /interface/patient_file/transactions.php 6 <div class="phone">xxx</div> 12 Cookie: Victim's Cookie
5 Cookie: Victim's Cookie ... 13 <html><titiel>Order Detail</title>
7 </html>
6 <html> 14 </html>
7 <titiel>Patient Transactions</title>
8 ... <td>${token}</td> ...
Figure7:ArbitraryOrderDeletionvulnerabilityinXMall
9 </html>
application(over7kstarsonGithub).
Figure 6: Arbitrary Patient Note Update vulnerability in
OpenEMRapplication(over3kstarsonGithub). withover3,000starsonGitHub.AsshowninFigure6,BACScan
successfullydetectedaBACvulnerabilitywithintheapplication
thatcouldleadtoarbitraryupdatesofpatientnotes.Specifically,
theIDDGconstruction,someGET-typemodificationpagesinadver-
duringthevulnerabilitydetectionprocess,BACScanreplayedthe
tentlymodifiedthetokensinsertedbyBACScan.Whenrevisiting
modificationrequest(i.e.,/add_transaction.php)andinserted
thecorrespondingstatuspage,BACScandetectedunexpectedto-
arandomtokenintotheform_noteparameter($tokeninline3).
kenmodifications,leadingtotheincorrectconnectionofIDDEs.
Subsequently,BACScanreplayedthisrequestusingtheattacker’s
Experimentalresultsshowthatdevelopersmostly(96.43%)adhere
cookie.Finally,leveragingtheconstructedIDDG,BACScanlocated
tothedefinitionsintheRFC,avoidingtheuseofGETrequests
thecorrespondingstatuspage(i.e.,/transaction.php)andiden-
fordatamodificationoperations.Moreover,thesefourincorrect
tifiedtheinsertedtoken($tokeninline8)onthepage.Conse-
IDDEsdidnotresultinanyfalsenegativesorfalsepositives,further
quently,BACScanreportedthepresenceofanMBACvulnerability.
confirmingthereliabilityofourIDDG.
Attackerscouldexploitthisvulnerabilitytomodifyanypatient’s
Wethenanalyzedthedistributionofthe1,135IDDEsbytype,
diagnosisormedications,whichposesaseverethreattopatient
with331forINSERT,452forUPDATE,and352forDELETE.Inter-
safety.Giventheextensivepotentialdamageposedbythisvulner-
estingly,whileDELETE-typeIDDEsaccountedfor31.40%,DELETE-
ability,wepromptlyreportedthiscriticalissuetothedevelopers
typeMBACcomprised48.89%ofthetotaldetectedvulnerabilities.
andwereissuedaCVE(CVE-2024-46**1).
Uponfurthersourcecodeanalysis,wefoundthatdevelopersof-
ArbitraryOrderDeletioninXMall.TheXMallapplicationis
tenimplementDELETEoperationsdirectlyviadataindices(e.g.,
a highly popular e-commerce application with over 7,000 stars
deletingdatabyID).Incontrast,UPDATEandINSERToperations
onGitHub.Figure7illustratesaBACvulnerabilityidentifiedby
typicallyinvolvebindingdatatoaspecificuser,unintentionally
BACScanwithinthisapplication,whichallowsdeletingarbitrary
performingauthorizationchecks.Thisfindingalsohighlightsthe
order.Lines8–10showcasethemodificationpagewherethevul-
importanceofBACScan’sreplaystrategyforDELETErequests.
nerabilityresides.BACScanreplayedtherequestandsubsequently
revisitedthecorrespondingstatuspage(i.e.,/member/order-Detail).
5.6 CaseStudy
Lines 1–7 and 11–14 present the content of the status page be-
WenowshowcasetwoBACvulnerabilitiesdetectedbyBACScan foreandafterthereplayofthemodificationrequest,respectively.
andmissedbyexistingtoolsinhighlypopularapplications,further BACScanidentifiedthatthetokenoriginallypresent(line5)disap-
illustratingthehighriskposedbythesevulnerabilitiesanddemon- pearedfollowingthemodificationrequest,indicatinganMBAC
stratingthepracticalutilityofBACScaninreal-worldscenarios. vulnerability.Attackerscanexploitthisvulnerabilitytodeleteany
ArbitraryPatientNoteUpdateinOpenEMR.TheOpenEMR user’sorders,posingsignificantriskstouserprivacyandpoten-
isanopen-sourceandwidelyusedhospitalmanagementsystem tiallyresultinginfinanciallosses.Weimmediatelyreporteditto

BACScan:AutomaticBlack-BoxDetectionofBroken-Access-ControlVulnerabilitiesinWebApplications CCS’25,October13–17,2025,Taipei
thedevelopersofthevulnerableapplication.Asaresult,wewere needforadditionalinputandleveragesanovelIDDG-basedap-
grantedaCVEidentifier,i.e.,CVE-2024-36**0. proach to accurately detect BAC vulnerabilities, addressing the
limitationsofbothstaticanddynamicmethods.
WebVulnerabilityDetection.Inrecentyears,thetechniques
6 Discussion
forautomaticallydetectingvulnerabilitieswithinwebapplications
LimitationsandFutureworks.WhileBACScanworkedwellin
havebeenextensivelystudied.Thesetechniquesalsocanbecatego-
theevaluations,weseeseveralpotentialimprovements. rizedintostaticanddynamicapproaches.Thestaticapproaches[25,
27,36,38,45,57]identifyuserinputsassourcesandpredefined
• Web Crawler. For a long time, the question of how to enable
security-sensitiveoperationsassinks.Theythenanalyzewhethera
crawlerstofullyexplorewebapplicationshasbeenapopular
dataflowpathexistsfromthesourcetothesink,indicatingapoten-
researchtopic.Inpractice,wehaveobservedthatstate-of-the-art
tialvulnerability.Thedynamicapproaches[23,29,32,34,47,51,56]
crawlers(e.g.,BlackWidow[32])areindeedcapableofeffectively
designoraclesspecificallytailoredtothesecurity-sensitiveoper-
exploringthemajorityofwebpages.However,therearestillsome
ationsrelevanttodifferenttypesofvulnerabilities.Forexample,
webpagesthatremaininsufficientlyexplored,whichleadsto
anexceptionthrownbyanSQLexecutionfunctionmayserveas
falsenegativesinBACScan.Inthefuture,ascrawlingtechnologies
anoracletodetectSQLinjectionvulnerabilities.Theseapproaches
continuetoadvance,webelievethattheperformanceofBACScan
detectvulnerabilitiesbymonitoringruntimebehavioranddeter-
willbefurtherimproved.
miningwhetherthecorrespondingoracleistriggeredduringthe
• PerformanceTrade-off.Asdescribedin§4.1.2,BACScanassumes
executionoftheapplication.However,theseapproachesmainly
thattokensareonlyinsertedintoPOSTrequeststriggereddur-
focusontaint-stylevulnerabilities,whichrelyonwell-definedse-
ingthepageexplorationprocess.Itisimportanttonotethat
curityoperationsformodeling.Incontrast,BACvulnerabilities
excludingtokeninsertionforGETrequestsisprimarilyaperfor-
aretiedtobusinesslogicandcannotbeeffectivelymodeled.This
mancetrade-off.WhileinterceptingGETrequestsandinserting
fundamentaldifferenceleadstofalsepositivesandfalsenegatives
tokenswouldbeeffective,itwouldalsosignificantlyincreasethe
whenthesemethodsareappliedtoBACvulnerabilitydetection.
analysistimerequiredbyBACScan.Hookingdatabaseoperations
todeterminewhichdatabaseactionsaretriggeredbyHTTPre-
8 Conclusion
questsisahighlyeffectiveapproach.However,inthecontextof
black-boxtesting,wedonothaveaccesstothedatabase.There- Inthispaper,weproposeBACScan,anovelblack-boxapproach
fore,wecanonlymakeeveryefforttoinferthetriggereddatabase fordetectingBroken-Access-Control(BAC)vulnerabilitiesinweb
actionsfromtheevidenceinHTTPrequestsandresponses. applications. By introducing a feedback-driven oracle based on
inter-pagedatadependency,BACScanaddressesthelimitationsof
EthicsConsideration.Thisstudyhasnotpresentedanylegal existing detection methods, particularly for modification-based
orethicalissues.Weobtainedthesourcecodeforlocalanalysis BACvulnerabilities.WeevaluateBACScanon20open-sourceweb
andresponsiblyreportedalldetectedvulnerabilitiesinopen-source applications,discovering89BACvulnerabilities,including54previ-
applicationstotheCVENumberingAuthority(CNA)[2].Addi- ouslyunknownhigh-risk0-dayvulnerabilitiesandtheassignment
tionally,wehavecontactedallthedevelopersregardingtheBAC of35newCVEIDs.Thesefindingsdemonstratethepracticalutility
vulnerabilitiesfoundin§5.2,andwillcontinuetocommunicate ofBACScaninBACvulnerabilitydetection.Wehopeourworkcan
withthemthroughoutthevulnerabilitydisclosureprocess. assistthecommunityinaddressingthegrowingthreatsposedby
BACvulnerabilities.
7 RelatedWork
Acknowledgement
BACVulnerabilityDetection.Therearenumerousstudies[28,
Wewouldliketothanktheanonymousreviewersfortheirinsightful
35,37,40–44,46,49,50,52–55,58,60–62]thathaveemployedvar-
commentsthathelpedimprovethequalityofthepaper.Thiswork
ioustechniquestodetectBACvulnerabilities.Thesestudiesare
wassupportedinpartbytheNationalNaturalScienceFoundation
commonlycategorizedintotwomaintypes:dynamicapproaches
of China (U2436207, 62172105). Yuan Zhang and Min Yang are
andstaticapproaches.Thedynamicapproaches[28,35,37,40–
thecorrespondingauthors.YuanZhangwassupportedinpartby
42,49,50,62]typicallysimulatemultipleusersthroughloginses-
theShanghaiPilotProgramforBasicResearch-FuDanUniversity
sionsandusecross-userforcedbrowsingcombinedwithresponse-
21TQ1400100(21TQ012).MinYangisafacultyofShanghaiInstitute
basedoraclestodetectvulnerabilities.However,theseoraclesare
of Intelligent Electronics & Systems, and Engineering Research
inadequatefordetectingMBACvulnerabilitiesduetotheirinability
CenterofCyberSecurityAuditingandMonitoring,Ministryof
tocapturedatadependencies,affectingprecisionandrecall.Static
Education,China.
approaches[43,44,46,52–55,58,60,61]modelusercredentials(e.g.,
$_SESSIONinPHP)andusepredefinedrulestoidentifypermission
References
checks.Whileeffectiveinsomecases,theystillpresentnotablelim-
itations.Ononehand,theysufferfromhighfalsepositivesdueto [1] AmazonOfficialWebsite. https://www.amazon.com.
[2] CVEProgram. https://www.cve.org/About/Overview.
thelackofruntimecontexttovalidatevulnerabilityreports.Onthe [3] CWE200. https://cwe.mitre.org/data/definitions/200.html.
otherhand,theyrequirestaticanalysisofthesourcecode,limiting [4] CWE284. https://cwe.mitre.org/data/definitions/284.html.
[5] EvocrawlonGithub. https://github.com/dlgroupuoft/evocrawl.
theirapplicabilitytoprogramsdevelopedinspecificprogramming
[6] ExploitDB. https://www.exploit-db.com/.
languages.Unlikethesepreviousefforts,BACScaneliminatesthe [7] Huntrplatform. https://huntr.com/.

CCS’25,October13–17,2025,Taipei FengyuLiuetal.
[8] OpenemronGithub. https://github.com/openemr/openemr. [41] XiaoweiLiandYuanXue.Block:ABlack-boxApproachforDetectionofState
[9] PaypalOfficialWebsite. https://www.paypal.com. ViolationAttacksTowardsWebApplications.InProceedingsofthe27thAnnual
[10] PlaywrightonGithub. https://playwright.dev/python/. ComputerSecurityApplicationsConference,2011.
[11] SupermarketonGithub. https://github.com/ZongXR/SuperMarket. [42] XiaoweiLiandYuanXue.Logicscope:Automaticdiscoveryoflogicvulnerabilities
[12] TheOfficialWebsiteofBurpSuite. https://portswigger.net/burp. withinwebapplications.InProceedingsofthe8thACMSIGSACsymposiumon
[13] TheOfficialWebsiteofBurpSuite’sBAppStore. https://portswigger.net/bappst Information,computerandcommunicationssecurity,pages481–486,2013.
ore. [43] FengyuLiu,YoukunShi,YuanZhang,GuangliangYang,EnhaoLi,andMinYang.
[14] TheOfficialWebsiteofGithub. https://github.com/. Mocguard:Automaticallydetectingmissing-owner-checkvulnerabilitiesinjava
[15] TopBACreportsfromHackerOne. https://github.com/reddelexc/hackerone- webapplications.In2025IEEESymposiumonSecurityandPrivacy(SP),pages
reports/blob/master/tops_by_bug_type/TOPIDOR.md. 10–10.IEEEComputerSociety,2024.
[16] TopBACreportsfromHackerOne. https://github.com/reddelexc/hackerone- [44] JieLu,HaofengLi,ChenLiu,LianLi,andKunCheng. DetectingMissing-
reports/blob/master/tops_by_bug_type/TOPAUTHORIZATION.md. Permission-CheckVulnerabilitiesinDistributedCloudSystems.InProceedings
[17] WeBidonGithub. https://github.com/renlok/WeBid. ofthe2022ACMSIGSACConferenceonComputerandCommunicationsSecurity,
[18] OWASPTop10-2019. https://owasp.org/API-Security/editions/2019/en/0x11- 2022.
t10/,2019. [45] ChanghuaLuo,PenghuiLi,andWeiMeng. TChecker:PreciseStaticInter-
[19] OWASPTop10-2021. https://owasp.org/Top10/A01_2021-Broken_Access_Co ProceduralAnalysisforDetectingTaint-StyleVulnerabilitiesinPHPApplica-
ntrol/,2021. tions. InProceedingsofthe2022ACMSIGSACConferenceonComputerand
[20] NotoriousHacksinHistory. https://securityboulevard.com/2023/03/23-most- CommunicationsSecurity,2022.
notorious-hacks-history-that-fall-under-owasp-top-10/,2023. [46] MalihehMonshizadeh,PrasadNaldurg,andVNVenkatakrishnan.MACE:De-
[21] OWASPTop10-2023. https://owasp.org/API-Security/editions/2023/en/0x11- tectingPrivilegeEscalationVulnerabilitiesinWebApplications.InProceedings
t10/,2023. ofthe2014ACMSIGSACConferenceonComputerandCommunicationsSecurity,
[22] SeriousDataBreachNews. https://www.apisec.ai/blog/5-real-world-examples- pages690–701,2014.
of-business-logic-vulnerabilities-that-resulted-in-data-breaches,2023. [47] EricOlsson,BenjaminEriksson,AdamDoupé,andAndreiSabelfeld. {Spider-
[23] AbeerAlhuzali,RigelGjomemo,BirhanuEshete,andVNVenkatakrishnan. Scents}:Grey-boxdatabase-awarewebscanningforstored{XSS}. In33rd
NAVEX:PreciseandScalableExploitGenerationforDynamicWebApplica- USENIXSecuritySymposium(USENIXSecurity24),pages6741–6758,2024.
tions.In27thUSENIXSecuritySymposium(USENIXSecurity18),2018. [48] YichengOuyang,KailaiShao,KunqiuChen,RuobingShen,ChaoChen,Mingze
[24] BradArkin,ScottStender,andGaryMcGraw.Softwarepenetrationtesting.IEEE Xu,YuqunZhang,andLingmingZhang. Mirrortaint:Practicalnon-intrusive
Security&Privacy,3(1):84–87,2005. dynamictainttrackingforjvm-basedmicroservicesystems.In2023IEEE/ACM
[25] MichaelBackes,KonradRieck,MalteSkoruppa,BenStock,andFabianYamaguchi. 45thInternationalConferenceonSoftwareEngineering(ICSE),pages2514–2526.
Efficientandflexiblediscoveryofphpapplicationvulnerabilities.In2017IEEE IEEE,2023.
europeansymposiumonsecurityandprivacy(EuroS&P),pages334–349.IEEE, [49] JiadongRen,MingyouWu,BingZhang,KeXu,ShangyangLi,QianWang,Yue
2017. Chang,andTaoCheng.Detac:Approachtodetectaccesscontrolvulnerability
[26] MiaoChen,TengfeiTu,HuaZhang,QiaoyanWen,andWeihangWang.Jasmine: inwebapplicationbasedonsitemapmodelwithglobalinformationrepresenta-
Astaticanalysisframeworkforspringcoretechnologies. InProceedingsof tion.InternationalJournalofSoftwareEngineeringandKnowledgeEngineering,
the37thIEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering, 33(09):1327–1354,2023.
pages1–13,2022. [50] MarcRennhard,MalteKushnir,OlivierFavre,DamianoEsposito,andValentin
[27] JohannesDahseandThorstenHolz. SimulationofBuilt-inPHPFeaturesfor Zahnd.Automatingthedetectionofaccesscontrolvulnerabilitiesinwebappli-
PreciseStaticCodeAnalysis.InNDSS,2014. cations.SNComputerScience,3(5):376,2022.
[28] GDeepa,PSanthiThilagam,AmitPraseed,andAlwynRPais.Detlogic:Ablack- [51] ChristianRossow.jAk:UsingDynamicAnalysistoCrawlandTestModernWeb
boxapproachfordetectinglogicvulnerabilitiesinwebapplications.Journalof Applications.InResearchinAttacks,Intrusions,andDefenses:18thInternational
NetworkandComputerApplications,109:89–109,2018. Symposium,RAID2015,Kyoto,Japan,November2-4,2015.Proceedings,2015.
[29] AdamDoupé,LudovicoCavedon,ChristopherKruegel,andGiovanniVigna. [52] SooelSon,KathrynSMcKinley,andVitalyShmatikov.Rolecast:FindingMissing
Enemyofthestate:A{state-aware}{black-box}webvulnerabilityscanner.In SecurityChecksWhenYouDoNotKnowWhatChecksAre.InProceedingsof
21stUSENIXSecuritySymposium(USENIXSecurity12),pages523–538,2012. the2011ACMinternationalconferenceonObjectorientedprogrammingsystems
[30] AdamDoupé,MarcoCova,andGiovanniVigna.Whyjohnnycan’tpentest:An languagesandapplications,pages1069–1084,2011.
analysisofblack-boxwebvulnerabilityscanners.InInternationalConferenceon [53] SooelSon,KathrynSMcKinley,andVitalyShmatikov. FixMeUp:Repairing
DetectionofIntrusionsandMalware,andVulnerabilityAssessment,pages111–131. Access-ControlBugsinWebApplications.InNDSS.Citeseer,2013.
Springer,2010. [54] FangqiSun,LiangXu,andZhendongSu. StaticDetectionofAccessControl
[31] KostasDrakonakis,SotirisIoannidis,andJasonPolakis.Rescan:Amiddleware VulnerabilitiesinWebApplications.In20thUSENIXSecuritySymposium(USENIX
frameworkforrealisticandrobustblack-boxwebapplicationscanning. In Security11),2011.
NetworkandDistributedSystemSecurity(NDSS)Symposium,2023. [55] LinTan,XiaolanZhang,XiaoMa,WeiweiXiong,andYuanyuanZhou.AutoISES:
[32] BenjaminEriksson,GiancarloPellegrino,andAndreiSabelfeld.Blackwidow: AutomaticallyInferringSecuritySpecificationandDetectingViolations. In
Blackboxdata-drivenwebscanning. In2021IEEESymposiumonSecurityand USENIXSecuritySymposium,2008.
Privacy(SP),pages1125–1142.IEEE,2021. [56] ErikTrickel,FabioPagani,ChangZhu,LukasDresel,GiovanniVigna,Christopher
[33] RoyFieldingandJulianReschke.Hypertexttransferprotocol(http/1.1):Semantics Kruegel,RuoyuWang,TiffanyBao,YanShoshitaishvili,andAdamDoupé.Toss
andcontent.RFC7231,2014. afaulttoyourwitcher:ApplyingGrey-boxCoverage-guidedMutationalFuzzing
[34] EmreGüler,SergejSchumilo,MoritzSchloegel,NilsBars,PhilippGörz,Xinyi toDetectSQLandCommandInjectionVulnerabilities.In2023IEEEsymposium
Xu,CemalKaygusuz,andThorstenHolz. Atropos:Effectivefuzzingofweb onsecurityandprivacy(SP),2023.
applicationsforserver-sidevulnerabilities.InUSENIXSecuritySymposium,2024. [57] FabianYamaguchi,NicoGolde,DanielArp,andKonradRieck. Modelingand
[35] XiangyuGuo,AkshayKawlay,EricLiu,andDavidLie. Evocrawl:Exploring DiscoveringVulnerabilitieswithCodePropertyGraphs.In2014IEEESymposium
webapplicationcodeandstateusingevolutionarysearch.IntheNetworkand onSecurityandPrivacy,2014.
DistributedSystemSecuritySymposium(NDSS).Acceptedforpublication. [58] HuangYongheng,ShiChenghang,LuJie,LiHaofeng,MengHaining,andLiLian.
[36] NenadJovanovic,ChristopherKruegel,andEnginKirda.Pixy:AStaticAnalysis Detectingbrokenobject-levelauthorizationvulnerabilitiesindatabase-backed
ToolforDetectingWebApplicationVulnerabilities.In2006IEEESymposiumon applications.InProceedingsofthe31stACMConferenceonComputerandCom-
SecurityandPrivacy(S&P’06),2006. municationsSecurity(CCS),October2024.
[37] MalteKushnir,OlivierFavre,MarcRennhard,DamianoEsposito,andValentin [59] LiYujianandLiuBo.Anormalizedlevenshteindistancemetric.IEEEtransactions
Zahnd.Automatedblackboxdetectionofhttpgetrequest-basedaccesscontrol onpatternanalysisandmachineintelligence,29(6):1091–1095,2007.
vulnerabilitiesinwebapplications.InICISSP2021,online,11-13February2021, [60] TongZhang,WenboShen,DongyoonLee,ChangheeJung,AhmedMAzab,and
pages204–216.SciTePress,2021. RuowenWang.Pex:APermissionCheckAnalysisFrameworkforLinuxKernel.
[38] PenghuiLiandWeiMeng.Lchecker:DetectingLooseComparisonBugsinPHP. In28thUSENIXSecuritySymposium,2019.
InProceedingsoftheWebConference2021,2021. [61] JunZhu,BillChu,HeatherLipford,andTylerThomas.MitigatingAccessControl
[39] PenghuiLi,WeiMeng,MingxueZhang,ChenlinWang,andChanghuaLuo. VulnerabilitiesthroughInteractiveStaticAnalysis. InProceedingsofthe20th
Holisticconcolicexecutionfordynamicwebapplicationsviasymbolicinterpreter ACMSymposiumonAccessControlModelsandTechnologies,2015.
analysis. InProceedingsofthe45thIEEESymposiumonSecurityandPrivacy [62] ChaoshunZuo,QingchuanZhao,andZhiqiangLin.Authscope:Towardsauto-
(Oakland).SanFrancisco,CA,USA,2024. maticdiscoveryofvulnerableauthorizationsinonlineservices.InProceedings
[40] XiaoweiLi,XujieSi,andYuanXue.AutomatedBlack-boxDetectionofAccess ofthe2017ACMSIGSACConferenceonComputerandCommunicationsSecurity,
ControlVulnerabilitiesinWebApplications. InProceedingsofthe4thACM pages799–813,2017.
ConferenceonDataandApplicationSecurityandPrivacy,2014.
