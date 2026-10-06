> 원본: AuthScope_CCS17.pdf; 변환: markitdown; 2026-10-06

<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
|     | AuthScope:  |     | Towards        |     | Automatic     |           | Discovery |          | of  | Vulnerable  |     |     |     |
| --- | ----------- | --- | -------------- | --- | ------------- | --------- | --------- | -------- | --- | ----------- | --- | --- | --- |
|     |             |     | Authorizations |     |               | in Online |           | Services |     |             |     |     |     |
|     | ChaoshunZuo |     |                |     | QingchuanZhao |           |           |          |     | ZhiqiangLin |     |     |     |
heUniversityofTexasatDallas heUniversityofTexasatDallas heUniversityofTexasatDallas
|     | 800WCampbellRd |     |     |     | 800WCampbellRd |     |     |     |     | 800WCampbellRd |     |     |     |
| --- | -------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | -------------- | --- | --- | --- |
Richardson,Texas75080 Richardson,Texas75080 Richardson,Texas75080
chaoshun.zuo@utdallas.edu qingchuan.zhao@utdallas.edu zhiqiang.lin@utdallas.edu
ABSTRACT Systems [32], where a user irst logs in the system to acquire a
Whenaccessingonlineprivateresources(e.g.,userproiles,photos, userID(UID)viaapassword-basedauthentication,andthenthe
shopping carts) from a client (e.g., a desktop web-browser or a kernelcheckstheUIDwhentheuserrequestsaccesstoaprotected
mobileapp),theserviceprovidersmustimplementproperaccess resource based on the corresponding permissions. Nearly all of
thelatermulti-useroperatingsystems(e.g.,UNIX/Linux)havefol-
| control, | which | typically involvesboth | authentication |     | and autho- |     |     |     |     |     |     |     |     |
| -------- | ----- | ---------------------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
lowedsuchanapproachwhenimplementingtheiraccesscontrol
rization. However,notalloftheserviceprovidersfollowthebest
mechanisms.
| practice,resultinginvariousaccesscontrolvulnerabilities. |     |     |     |     | Toun- |     |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
derstandsuchathreatinalargescale,andidentifythevulnerable Whenmovingtotheonlineservices,designingandimplement-
access control implementations in online services, this paper in- ingasecureaccesscontrolmechanismbecomesachallengingtask
troducesAuthScope,atoolthatisabletoautomaticallyexecutea forseveralreasons. First, anonlineservicecanhaveuptohun-
dredsofmillions(evenbillions)ofusers,andhandlingsuchalarge
mobileappandpinpointthevulnerableaccesscontrolimplemen-
|          |              |                |                 |     |               |     | scale of users | oten needs | to  | use eicient | database | technologies. |     |
| -------- | ------------ | -------------- | --------------- | --- | ------------- | --- | -------------- | ---------- | --- | ----------- | -------- | ------------- | --- |
| tations, | particularly | the vulnerable | authorizations, |     | in the corre- |     |                |            |     |             |          |               |     |
Second,managingtheusercredentialcorrectlyforauthentication
| spondingonlineservice. |     | hekeyideaistousediferentialtraic |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analysis to recognize the protocol ields and then automatically isanotherchallenge(e.g.,manyonlineservicetodaystillmistak-
substitutetheieldsandobservetheserverresponse. Oneofthe enlystoreplaintextpassword[3,12]).hird,theclientside(e.g.,a
keychallengesforalargescalestudyliesinhowtoobtainthepost- browser,amobileapp)canbecompletelycontrolledbyanatacker
|     |     |     |     |     |     |     | andcannotbetrustedatall. |     | hatis,arequestmessagegenerated |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | ------------------------------ | --- | --- | --- | --- |
authenticationrequest-and-responsemessagesforagivenapp.We
|     |     |     |     |     |     |     | by a client | can be untrusted, |     | and the eicient |     | security check | is  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | --- | --------------- | --- | -------------- | --- |
havethusdevelopedatargeteddynamicactivityexplorertoper-
neededattheserverside[47].
| form | an in-context | analysis | and drive the | app execution | to  | au- |     |     |     |     |     |     |     |
| ---- | ------------- | -------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tomatically log in the service. We have tested AuthScope with Whiletheuseofsingle-sign-on(e.g.,withFacebookLogin)[38]
4,838popularmobileappsfromGooglePlay,andidentiied597 hasmadetheauthenticationmanagementmucheasierforonline
0-dayvulnerableauthorizationsthatmapto306apps. services,itdoesnotsolvetheauthorizationproblemautomatically
|     |     |     |     |     |     |     | in that the | online service | provider | (e.g., | shopping | sites such | as  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | -------- | ------ | -------- | ---------- | --- |
CCSCONCEPTS Amazon)stillhastoregulatethattheauthenticateduseronlyviews
andupdatesherownresources(e.g.,heruserproileorshopping
•Securityandprivacy→Accesscontrol;Authorization;Web
|     |     |     |     |     |     |     | cart). Over | the past many | years, | an eicient |     | approach of | using |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------ | ---------- | --- | ----------- | ----- |
applicationsecurity;
|     |     |     |     |     |     |     | securitytokenstohandleauthorizationwasdeveloped[20], |     |     |     |                       |     | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --------------------- | --- | --- |
|     |     |     |     |     |     |     | popularizedespeciallyinwebapplications.              |     |     |     | Inparticular,intradi- |     |     |
KEYWORDS
tionaldesktopwebapplications,abrowsercookieorasessionID
Accesscontrol;authorization;vulnerabilitydiscovery
(theseareotencalledsecuritytokens)isusedfortheauthoriza-
tion.
1 INTRODUCTION
Consequently,thesecurityoftheauthorizationdependsonhow
Foranymulti-usercomputingsystems(e.g.,onlineshoppingand strongthetokenis(andalsowhethertheserverenforcesit). Any
social networking), there is a need to regulate who can view or disclosure, capture, prediction, brute force, or ixation of the se-
usearesource. Aparticular securitymechanismtoachievethis curity tokens will lead to severe atacks such as account hijack-
istouseaccesscontrol,inwhichauserneedstobeirstauthenti- ing, where an atacker is able to fully impersonate a victim to
|     |     |     |     |     |     |     | getallofherpersonaldata. |     |     | Unfortunately, | not | alloftheonline |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | -------------- | --- | -------------- | --- |
cated(i.e.,tellingthesystemwhotheuseris)andthentheaccess
is granted if the authenticated user has the permission to do so. serviceprovidersfollowthebestpracticewhenusingthesecurity
heuseofaccesscontrolcanbedatedbacktoMulticsOperating tokensfortheauthorization.Forinstance,wehaveobservedweak
|     |     |     |     |     |     |     | security tokens | (e.g., just | a very | small | integer) | passing through |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ------ | ----- | -------- | --------------- | --- |
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
mobileapps.Meanwhile,wehavealsoobservedthateventhough
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forproitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation a service provider may have used strong security tokens (e.g., a
ontheirstpage. Copyrightsforcomponentsofthisworkownedbyothersthan 256-bitcryptographichash),theserveractuallydoesnotenforce
| ACMmustbehonored. |     | Abstractingwithcreditispermited. |     | Tocopyotherwise, |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orrepublish, topostonserversortoredistributetolists, requirespriorspeciic whetherthistokenbelongstoaparticularuser(i.e.,thetoken)or
permissionand/orafee.Requestpermissionsfrompermissions@acm.org. itisjustatoken. Giventhefactthatsomanymobileappsused
CCS’17,Oct.30–Nov.3,2017,Dallas,TX,USA.
inourdailylives,itisimperativetosystematicallyidentifythese
| ©2017ACM. | ISBN978-1-4503-4946-8/17/10…$15.00 |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DOI:http://dx.doi.org/10.1145/3133956.3134089
799

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
vulnerableaccesscontrolservers,otherwiseusers’personaldata 1 User Credential
| canbethusleaked. |     |     |     |     |     |     |     | Access Token |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
2
Tothisend, thispaperintroducesAuthScope, atooltoauto- 3 Access Token, Resource
maticallyidentifythevulnerableaccesscontrolservers,especially
|     |     |     |     |     |     |     |     | 4 Response |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
thevulnerableauthorizations,whengivenjustmobileapps.Since
wedonothaveanysourcecodeoftheseversideimplementations,
wecanonlyperformablackboxanalysisoftheremoteserverby Figure1:ASimpliiedAuthenticationandAuthoriza-
generating and analyzing various network request and response tionProtocolinOnlineServices.
| messagesbetweentheclientandtheserver. |     |     |     | Topinpointthevul- |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
nerableaccesscontrolimplementations,ourkeyinsightistouse
onlineserviceisimplementedanditspracticalsecurityissuesin
| diferentialtraicanalysis, |     | awidelyusednetworkprotocolanal- |     |     |     |     |     |     |     |     |
| ------------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
§2.3.
ysistechnique(e.g.,[13,16,17,40,47]),torecognizethenetwork
| protocol | ields and | then automatically | substitute | the ields | of in- |     |                                |     |     |     |
| -------- | --------- | ------------------ | ---------- | --------- | ------ | --- | ------------------------------ | --- | --- | --- |
|          |           |                    |            |           |        | 2.1 | AuthenticationandAuthorization |     |     |     |
terestandobservetheserverresponsetoidentifythevulnerable
services. Oneofthekeychallengesforalargescalestudyliesin When providing private resources to multiple users, it oten re-
quirestwosecurityservices:authenticationandauthorization.
howtoobtainthepost-authenticationrequest-and-responsemes-
sagepairsforagivenapp. Wehavethusdevelopedanadaptive - Authentication. heprocessofverifyingauser’siden-
dynamic app activity explorer to perform an in-context analysis tityiscalledauthentication. Inamulti-usersystem,itis
anddrivetheappexecutiontoautomaticallylogintheservice. crucialtoaccuratelyidentifywhomakestherequest. A
WehaveimplementedAuthScopeandtesteditwith4,838very widelyusedapproachtoperformauthenticationistouse
popularmobileappsfromGooglePlay. Notethattheseappsall apasswordsysteminwhichauser’sidentityisveriiedby
checkingwithahashedpasswordtypedduringthelogin.
containFacebookloginandtheybelongtothetop10%ofthemo-
Also,authenticationtypicallyonlyneedstobeperformed
bileappsintermsoftheaccumulateddownloadsinGooglePlay.
Tooursurprise, AuthScopehasidentiied5970-dayvulnerable once;otherwiseitwillbeannoyingtotheuser.
access control implementations in the server side of 306 mobile - Authorization.heprocessofgrantingtheaccessofspe-
apps (with an upper bound of total install of 61 million). he ciicresourcesbasedonuser’sprivilegesorpermissionsis
rootcauseofthesevulnerabilitiescomesfromthemistakenuseof calledauthorization.Notthatauthenticationprovidesthe
|     |     |     |     |     |     |     | proof of | identity, but it | does not describe | the resources |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | ----------------- | ------------- |
eitherpredictableIDs,oruser’semailaddress,oruser’sFacebook
thatareallowedtobeaccessedbytheauthenticateduser.
IDfortheauthorizationwithout(orenforcing)anysecuritytokens.
Consequently,theseonlineservicescanallbecompletelybroken For instance, a user is authenticated before accessing a
byanadversary,andprivacysensitiveorevensecretdataforupto database,butthisdoesnottellthedatabasesystemwhich
61millionmobileuserscanbeleakedduetothesevulnerabilities. datatheuserisentitledtoaccess. Forthis,itrequiresthe
Inshort,wemakethefollowingcontributionsinthispaper. authorizationservice.
|     | - NovelSystem. | WepresentAuthScope,anoveltoolto |     |     |     |     |                                   |     |     |     |
| --- | -------------- | ------------------------------- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- |
|     |                |                                 |     |     |     | 2.2 | AuthorizationSecurityinUNIX/Linux |     |     |     |
automaticallyidentifythevulnerableaccesscontrolonthe
serverside.Itdoesnotrequireanycodeaccessofserver’s Foramulti-useroperatingsystemsuchasUNIX/Linux,rightater
implementation,otherthanjustthetraicbetweenanau- anauthenticateduserlogsin,thesystemwillautomaticallyassign
aUID(whichisjustaninteger)basedontheproileinthesystem
thenticateduserandtheserver.
- EicientTechniques. Weapplydiferentialtraicanal- (e.g.,/etc/password)andcreateashellprocesstoservetheuser’s
ysis to automatically reverse engineer protocol ields of request. hisshellprocesswillinteractwiththesystemonbehalf
interest,suchassecuritytokens,andalsowedevelopan oftheuserwiththeassignedUIDthatismaintainedbytheprocess
adaptiveappactivityexplorationschemetoexecuteamo- descriptorinthekernel. TochangetheUIDofaprocessorauser,
|     | bile app | in a targeted | way and | apply it to trigger | post- | itmustinvokesystemcalls. |              |           |               |                     |
| --- | -------- | ------------- | ------- | ------------------- | ----- | ------------------------ | ------------ | --------- | ------------- | ------------------- |
|     |          |               |         |                     |       | More                     | speciically, | to ensure | the security, | any access to a re- |
authenticationrequestmessages.
- PracticalResults.WehavetestedAuthScopewith4,838 source needs to invoke system calls, in which access control is
popularAndroidapps. Ourtoolhasidentiied5970-day enforcedbasedontheUIDandpermissions.Anadversarycannot
vulnerableaccesscontrolimplementationsamongthere- forge his or her UID to someone else’s even though the UID is
moteserversof306mobileapps.Wehavemaderesponsi- known, because the kernel remembers the UID and tracks it at
bledisclosuretoallofthevulnerableserviceproviders. thecorrespondingprocessdescriptor. Foranadversarytoreally
changetheUID,heorshemustexploitsotwarevulnerabilitiesin
|     |     |     |     |     |     | thesystemsuchasbuferoverlowsinadaemonprocess. |     |     |     | When |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | ---- |
2 BACKGROUND
Inthissection,wepresentnecessarybackgroundinordertounder- theuserlogsout,theshellprocessalsoterminatesandtheuserhas
tobeauthenticatedagaininordertousethesystem.
standthecommonmistakesandrootcausesofvulnerableaccess
| control                                      | implementations | in online      | services.         | We begin with | the |     |     |     |     |     |
| -------------------------------------------- | --------------- | -------------- | ----------------- | ------------- | --- | --- | --- | --- | --- | --- |
| basic                                        | concepts of     | authentication | and authorization | in §2.1,      | and |     |     |     |     |     |
| thenexaminewhytheauthorizationinUNIX/Linuxis |                 |                |                   | securein      |     |     |     |     |     |     |
§2.2. Finally,wediscusshowatypicalsecureauthorizationinan
800

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
2.3 SecureAuthorizationinOnlineService engineeredmobileappssuferedfromvariousvulnerabilitiesiden-
Asstatedearly,therearemanychallenges(e.g.,alargevolumeof tiiedinthepastfewyearssuchascomponenthijacking[24],in-
users,untrustedclient,etc.) whenimplementingasecureautho- formationleakage[9]),andprivilegeescalation[44]).
rizationinonlineservices.Moreimportantly,onlineservicesoten Morespeciically,therewillbeavarietyofissueswhenimple-
require high scalability and availability. Unlike the UNIX/Linux mentingtheauthorizationsecurityontheserverside.Forinstance,
authenticationandauthorization,whichisstatefulandkernelre- isthesecuritytoken(orRID)suicientlyrandom? Hastheserver
memberswhohasloggedinandout,themajorityoftoday’sonline reallyenforcedthecheckofthesecuritytokens?Eventhoughthe
service uses HTTP/HTTPS protocol, which is stateless. A state- servercheckedthetoken, hasitreallymadesureitisthetoken
lessprotocolcanbeforcedtobehaveasifitwerestatefulifthe binded to a particular user or it is just a token (a token vs. the
serverandtheclientcansendthestatealongwitheveryrequest token)?Doestheuserhavethepermissionstoaccesstheprotected
and response message. A typical way of accomplishing this in resources?Withthesequestionsinmind,wewouldliketoperform
HTTP/HTTPSistousesecuritytokenssuchascookiesorsession a large scale, systematic study of how online service providers
IDs. AsillustratedinFigure1,atahighlevel,theauthentication implementtheiraccesscontrolformobileusers,andidentifythose
andauthorizationprotocolsinon-lineservicescanbeabstracted vulnerableonesifthereisany.
usingthefollowingfoursteps:
3 OVERVIEW
- Step❶:heclientsendsarequesttotheserverwithuser
credentialssuchasapassword. heserverauthenticates hegoalofthisworkistounderstandhowonlineserviceproviders
the identity of the user via the password, social single implementtheiraccesscontrolofuserresources,andidentifythose
signon(e.g.,FacebookConnect),orothermeans. Topre- serversthatarevulnerabletoaccounthijackingandprivateinfor-
ventanyleakageofthecredentials,transportlayersecu- mationleakage, byjustanalyzingthetraicbetweenthemobile
rity(TLS)isotenusedtoensurethecommunicationse- appsandtheserver. Whilethereareavarietyofwaystodoso,
curity. we seek to design an approach that is scalable, automated, and
- Step❷: heservercreatesarandomlygeneratedtoken systematic.Inthissection,weirstusearunningexample(§3.1)to
and binds it with the authenticated user, and the server discussvariouschallenges(§3.2)wehavetosolve,andthengive
thentransmitsthetokenbacktotheclient. anoverviewofoursystem(§3.3).
- Step❸: heclientincludestheserverprovidedtokenon
3.1 ARunningExample
subsequentrequeststotheserverasaproofofidentity,the
serverthengrantsorrejectstheuseraccesstoprotected Toillustratetheproblemclearly,weusearunningexamplefroma
resourcesbasedonherpermissions. popularsocialappnamedW1thatmanagesusers’pets(e.g.,dogs)
- Step❹: heserverrespondstotheuserrequestwiththe andtracktheiractivities. W appisveryinterestinginthatitac-
appropriateinformation. tually contains a vulnerable access control implementation even
Sometimes, thereareevenmoresimpliiedimplementationof thoughitusesstrongsecuritytokensforuserauthorization.
theprotocolandtheclientdoesnotneedtocompletetheirstthree Inparticular,asillustratedinFigure2,rightateralegitimate
stepstoaccessaresourcestoredintheserver,iftheclientknows userlogsintheapp,theW clientwillautomaticallysendarequest
(e.g.,distributedviaanemailirst)theresourceID(RIDinshort) to the server to get all the notiication messages (which are pri-
and this RID is suiciently random. For instance, when using vateresourcesbelongingtothisparticularuser).Foreachspeciic
Overleaf,anonlineCollaborativeWritingandPublishingservice, notiicationmessage, theserverwillassignanRID(e.g., 433222
toshareapaperrepository,theusercouldjustsenttheURLs(e.g., and433227)andsendtheresponsemessagecontainingtheRIDto
https://www.overleaf.com/9357323vdzpzwzmwdmx)generatedby theclient,asshowninFigure2(a)andFigure2(b),therequestand
Overleaf. OnlytherecipientwhohastheURLcanaccessthepa- responsemessagepairsforuserAliceandBobweregisteredwith
per repository because the RID (e.g., 9357323vdzpzwzmwdmx, theservice,respectively.
whichisessentiallyatoken)issuicientlyrandom. Also,inthis WecanobservethattheserverofW doesuseauserspeciicran-
case, the server does not have to remember who holds the RID: domstringasthesecuritytoken(i.e.,asshowninthein_app_token
anyonewhohasitcanaccesstherepository. hatis,thebinding ield). heserveralsoassignstwointegers,namely21690asAl-
ofthetokentoauserisperformedseparately(e.g., managedby
ice’suserID(UIDinshort)and21691asBob’sUID.Unfortunately,
theusernotbytheserver). if we substitute the UID in the post-authentication request mes-
sageofAlicewiththevaluefromBob’s,e.g.,replacing21690with
PracticalIssues. Accordingtotheabovediscussion,wecanno- 21691,wecansuccessfullyreadBob’sprivatenotiicationmessage
ticethatpropergenerationanduseofsecuritytokens(orRIDs)is byusingAlice’stokenasshowninFigure3.
paramounttoensuretheauthorizationsecurity.Intheory,because herefore,ascanbenoticed,theserverofW hasmadeeitherof
thetoken(orRID)isgeneratedatthetimeoflogin(orcreation) thetwofollowingmistakes:
andisrandomandunguessable,itspresencesuicientlyservesas
- Noenforcementofthesecuritytokenwhetherornot
proofthattherequestreallycomesfromtheauthenticateduserto
belongingtoaparticularuser.Iftheserverhaschecked
whom the token (or RID) was assigned. In reality, however, we UID21690withAlice’stokenand21691withBob’stoken,
believenotalldeveloperswouldhavefollowedsuchbestpractice,
thesubstitutionatackwouldnothavesucceeded.
andtherewillbemanypoorlyengineeredservers(asthosepoorly
1Notethatwedonotreporttheconcretenameofthisapp,sincethevulnerability
identiiedintheserverofW hasnotbeenpatchedyetasthetimeofthiswriting.
801

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
GET /api/v1//users/21690/notifications?in_app_token=e67315b35aa3 hegoalofourAuthScopeisexactlydesignedtoidentifythese
8d4ac8cac3cd9c7f88ae7f576d373f HTTP/1.1 vulnerableserversautomaticallyandinalargescale,byperform-
Host: api.*****.com
Connection: close ingtherequestmessageieldinferenceandsubstitutionsystemat-
ically.
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate
Content-Type: application/json 3.2 ChallengesandKeyInsights
ETag: W/"5319d96924bb6d0a761b5f13b248919c"
Server: nginx/1.6.2 From the above running example, we can notice that there will
X-Request-Id: 5775d45e-cc3b-4665-8bc6-c2c7a2c9180d
X-Runtime: 0.027840 beanumberofchallengesinordertoachieveourgoalandthese
Content-Length: 191 include:
Connection: Close
- Howtoobtainthepost-authenticationmessages.Since
[{"id":433222,"sender":null,"dog":null,"notification_type":15,"n
otification_text":"Welcome to *****.","object_id":21690,"is_seen wefocusontheidentiicationofthevulnerableauthoriza-
":true,"is_read":true,"created_at":"2017-01-28T23:54:59.831Z"}] tionimplementations(whichoccuratertheuserauthen-
(a) Alice’s first request and response message after login tication),wemustexecutetheapptoreachthestatethat
generates the post-authentication request messages. In
GET /api/v1//users/21691/notifications?in_app_token=fb153b7d8c0a otherwords,wemusthavearegisteredlegitimateuserof
0c6ac841d7bfbd9446de627c642858 HTTP/1.1 thetestingserviceandobtainalegalpost-authentication
Host: api.*****.com
Connection: close message. Whilewecanuse manualefortsto registera
legaluserineachoftheto-be-testedservice,thiscannot
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate scaletoalargevolumeofapps. hisalsocontradictsour
Content-Type: application/json goal of fully automation. herefore, we have to design
ETag: W/"6ee365b32e7f3e145d5c74778ea243cd"
Server: nginx/1.6.2 techniques to drive the app execution to trigger the le-
X-Request-Id: 4970cafb-9438-4a70-96e0-ca2f789f0d5d
gitimatepost-authenticationmessages(e.g.,theonesillus-
X-Runtime: 0.022889
Content-Length: 192 tratedinFigure2).
Connection: Close
- Howtorecognizetheprotocolieldsofinterest.With
[{"id":433227,"sender":null,"dog":null,"notification_type":15,"n thetracedlegitimaterequestandresponsemessages,we
otification_text":"Welcome to *****.","object_id":21691,"is_seen
":true,"is_read":false,"created_at":"2017-01-28T23:56:40.533Z"}] havetoalsoidentifytheieldsthatareofourinterest.For
instance,asshowninFigure2,wehavetorecognizevari-
(b) Bob’s first request and response message after login
ousieldssuchasin_app_tokeninwhichthereareield-
name associated, and those that do not have any ield-
Figure2: SampleRequestandResponseMessagesof name(e.g.,21690and21691intheURLpaththoughwe
our Running Example. he server name has been suspectitisaUIDield)inthemessages. Notethatun-
anonymizedwith*****. liketraditional HTTP request messagein which wecan
directlyrecognizetheprotocolieldsbyieldnames, we
GET /api/v1//users/21691/notifications?in_app_token=e67315b35aa3 havetosystematicallyrecognizealloftheprotocolields
8d4ac8cac3cd9c7f88ae7f576d373f HTTP/1.1 including ield-name hidden ones used in URLs such as
Host: api.*****.com
Connection: close thoseusingRESTAPIs.
- How to identify the vulnerability. Having obtained
HTTP/1.1 200 OK
thepost-authenticationmessagesandrecognizedthepro-
Cache-Control: max-age=0, private, must-revalidate
Content-Type: application/json tocolields,westillneedtosystematicallysubstitutethe
ETag: W/"6ee365b32e7f3e145d5c74778ea243cd"
Server: nginx/1.6.2 protocolieldsintherequestmessagestoobservehowa
X-Request-Id: 4970cafb-9438-4a70-96e0-ca2f789f0d5d serverwouldrespondtothesubstitutedrequestmessages.
X-Runtime: 0.022889
Content-Length: 192 Howtodecidewhetheraserverisvulnerablebasedonthe
Connection: Close responsemessageisanotherchallenge.
[{"id":433227,"sender":null,"dog":null,"notification_type":15,"n Fortunately,allofthechallengeslistedabovecanbesolvedor
otification_text":"Welcome to *****.","object_id":21691,"is_seen
":true,"is_read":false,"created_at":"2017-01-28T23:56:40.533Z"}] partiallysolvedwiththefollowingkeyinsights.
- Executingtheappwithsingle-sign-on.Itistediousto
Figure3:AliceReadBob’sPrivateMessage. manuallyregisterauseraccountonebyoneforeachof
thetestedmobileapp. Interestingly,wenoticethatmany
ofthemobileappstodaysupportsocialloginsuchasusing
- No randomness of the UID. If the server does not at- Facebooklogin.Withthis,wecanautomaticallyloginan
tempttoenforcetheconsistencycheckbetweentheUID
apptoexercisethepost-authenticationmessagesifweare
andthecorrespondingusertoken,itcanmaketheUIDsuf-
abletodrivetheapptoexecutetheFacebooklogin. he
icientlyrandomandatackercannotmakeapredictable
limitation for this approach is for those that do not use
guess,therebydefeatingthesubstitutionatack.
socialloginwewillnotbeabletotestthemautomatically.
- Recognizingprotocolieldsofinterestwithdiferen-
tialtraicanalysis.Withjustonerequestandresponse
802

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
7 Field-Substituted Alice’s Request Messages (for Bob)
1 Alice’s Request1 1 Alice’s Request1
Post-Authentication 2 Alice’s Request2 Field Recognition 2 Alice’s Request2
Message Generation 3 Bob’s Request and Substitution 3 Bob’s Request
4 Alice’s Response1
Response Message 5 Alice’s Response2
Labeling 6 Bob’s Response
8 Server Response Messages for the Field-Substituted Request
Smartphone Man-in-the-Middle Proxy Cloud
Figure4:AnOverviewofAuthScope.
messagepair,itwillbechallengingtorecognizethepro- 3.3 SystemOverview
tocol ields of our interest. However, if we have two le- An overview of AuthScope is presented in Figure 4. here are
gitimateusersandhavetwosuchmessagepairs,wecan threekeycomponents: (1)Post-AuthenticationMessageGen-
easilyidentifytheieldsofourinterestbyaligningthetwo erationthatdrivestheappexecutionandtriggersthelegitimate
corresponding messages and looking for the diferences, user’s post authentication request messages, (2) Protocol Field
aswhatwehavedoneinourpriorworkAutoForge[47]. RecognitionandSubstitutionthatrecognizestheprotocolields
Forinstance,ifwealignthetworequestmessagesgener- oftherequestmessagesandmutatestheieldofourinterest,and
atedbyAliceandBob,wecaneasilyrecognizetheUID (3) Response Message Labeling that labels the response mes-
ieldandthein_app_tokenieldasshowninFigure2. sagesanddecideswhethertheserverisvulnerabletoaccesscon-
- Substituting the ields having small Euclidean dis- trol violation atacks. All of these components run in the client
tance. We do not have to substitute the cryptographi- side(withoutaccessinganyservercode)eitherinamobiledevice,
callygeneratedtokenieldssinceitwillbesorandomand orinaman-in-the-middlenetworkproxy.
impossibletoguess(e.g.,thethein_app_tokenieldin
our running example), and instead we should substitute ScopeandAssumptions.Wefocusonanalyzingthemobileapps
theieldwhosecorrespondingdifedvaluehasashortdis- thatuseHTTP/HTTPSprotocols,althoughAuthScopecanbeex-
tance(e.g.,theUIDieldwithvalue21690and21691,which tendedtoanalyzenon-textprotocols. Also,wefocusontheapps
hasjustoneEuclideandistance,ifweconventthesetwo thatusetheFacebooklogin;otherwisewewillnotbeabletoauto-
numberstointegers).hisalsomeanswehavetoconvert maticallytriggerthepost-authenticationmessages.Regardingthe
allthenumbersandstringstocomputableformssuchthat typeoftheaccesscontrolvulnerabilities,wefocusonthevulner-
theEuclideandistancecanbemeasuredbetweenthetwo ableauthorizationimplementationsthatarecausedby(i)nosecu-
difed values. Note that there might be some other dis- ritytoken,(ii)norandomnessofwhenreferringresourcesatserver
tancesbuteuclideandistancecanserveourpurposeinour sidewhennotoken,(iii)noaccesscontrolenforcementwhenusing
problemseting. token.Othervulnerabilitiesoftheserveraccesscontrolsuchas(1)
- Labelingserverresponsealsowithdiferentialtraf- ausersecuritytokenisneverchangedinthelifespanoftheuser,
ic analysis. Ater we substituting the ields of our in- (2)howrandomatokenis,(3)thetokenistransmitedinplaintext,
terest(e.g.,theUIDield)asshowninFigure3,wehave or(4)no/weakauthentication,areout-of-scopeofthiswork.
todecidewhetherthesubstitutionindeedprovestheex- WithrespecttotheHTTPStraic,sincewecontrolthesmart-
istenceofthevulnerableauthorizationintheserverside. phone and also the man-in-the-middle proxy, we install a root
Fortunately,wenoticethatwhensubstitutingtheAlice’s certiicateinthephonesignedbyourselves,andthenwecanob-
UIDwithBob’s,iftheserverresponseswithBob’sprivate serve the traic in the proxy in plaintext. Such a method has
message we observed before, then it is indeed vulnera- beenwidelyusedinmanysystemstoobservetheHTTPStraic
ble. More speciically, as demonstrated in our running betweenmobileappsandservers(e.g.,[5,46,47]).
example,theresponsemessageinFigure3isidenticalto
4 DETAILEDDESIGN
theresponsemessageinFigure2(b),whichtrulyconirms
thattheserversideofW appisvulnerable. However,the In this section, we present the detailed design of the three key
responsemaycontainsomemessagespeciicinformation components of AuthScope. Based on their execution order, we
such as the time stamp. Fortunately, diferential traic irst describe how to trigger the post-authentication message of
analysiscanalsoidentifytheseieldsandilterthemout, a mobile app in §4.1, then explain how to perform the protocol
asdemonstratedinAutoForge[47]. reverseengineeringtorecognizeandsubstitutetheprotocolields
ofinterestin§4.2,andinallypresenthowwelabeltheresponse
803

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
message and detect the vulnerable access control of the remote arerecognizedandusedtodrivetheappexecution,wealsodesign
servicesin§4.3. an approach that parses the UI elements in a given activity and
thenleveragesadepth-irst-search(DFS)algorithmtoexplorethe
4.1 Post-AuthenticationMessageGeneration next-layerappactivitiesandtriggertheactivitiesofourinterest
Unlikemanyothermobileappdynamicanalyseswhichonlyneed (suchasFacebookLogin).
torandomlytriggersomeappactivities,weneedananalysisthat InAndroid,anactivityrepresentsasinglescreen(canbeawin-
can allow the app to enter an important state (i.e., the post au- doworaloatingwindowembeddedinanotheractivity)interface
thenticationstate). Atahighlevel,thiswouldmeanthatweneed thatinteractswithusers. Everyactivitydeinedfortheappmust
to irst register a legal user in the remote service when given a be declared in the manifest ile. Within each activity, every UI
mobileapp,andthenexecutetheappwiththeregistereduserand elementsuchasaButon, anImageButon, aCheckBox, anEditBox,
meanwhilesuccessfullylogintheserver.However,theuserregis- etc.,representsaview. Alltheviewsaredeinedinthelayoutile
tration(i.e.,signup)interfaceofamobileappcanactuallybequite ofanactivityordeinedbyprogrammersincode.Eachviewcanbe
sophisticated.Wecannotrunadynamicrandomtestingtoolsuch bindedtoaspeciicaction. Whenauserinteractswithanactivity
asMonkey[7]toperformtheusersignupbecauseofthevarious (e.g.,clickaButon),theactionbindedtothecorrespondingspeciic
constraintsintheinterfacesuchassomeinputmayneedtofollow viewwillbeinvoked,whichmightleadtojumptoanotheractivity.
certainformat(e.g.,username,passwords,emails,zipcode,phone Sincewewouldliketoexploreasmanyactivities(aswellasthe
numbers),someinput(e.g.,passwords,PINs,andemails)mayneed viewsinsideanactivity)aswecan,wehavetouniquelyidentifyeach
toentertwiceforconsistencychecks,andsomeinputmustsatisfy activityandeachviewsuchthatwedonothavetoexploretheactiv-
someconstraints(e.g.,ageneedstobegreaterthan18). ityandtheviewagain(e.g.,clickaButonagain)ifwehaveexplored
Itmightappearweneedtousesymbolicexecutiontocollectthe it before (otherwise our DFS activity exploration may encounter
constraintsandsolvethemtoinishtheserversignupprocessfrom deadloops). Touniquelyidentifyanactivityistrivial,weusethe
a mobile app. However, many of the constraints checking code nameofeachactivityasthesignature,duetotheuniquenessofthe
mayjustexistintheserverside,andsymbolicexecutionofmobile activityname.However,thereisnosuchasingleobviousatribute
appmaynotbeabletocollecttheseconstraints.Meanwhile,many touniquelyidentifyaview. Notethatintuitively,thememoryad-
oftheregistrationprocessesmayalsoneeduserstoclickcertain dressofeachviewobjectshouldbeunique,butthememoryaddress
linkssentviatheemails.Inaddition,theremightbeCAPTCHAsin ofaviewcanbechangedwhenanactivityisrefreshed.
theusersignupinterface.heseallmakeuserregistrationprocess
ViewIdentiication. InAndroid,allactivitiesforataskaremain-
non-trivialforalargescalestudy.
tainedusingastack,andtheyarearrangedintheorderaccording
Fortunately, we also notice that many mobile apps today use
tothetimewheneachactivityisopened.Forexample,thecurrent
sociallogin,inwhichauserjustneedstologintheservicewithher
activityisatthetopofthestack;whenjumpingtoanotheractivity,
socialaccountandtheserverwillautomaticallypullthedatafrom
thestateofcurrentactivityissavedinthetopofthestackandthen
thecorrespondingauthenticationserviceproviders(e.g.,Facebook).
opens the new activity. When the new activity inishes (e.g., the
Withthis,wecanavoidrunningthesignupprocessandinsteaddi-
userclicksabackButon),theolderactivitystoredinthetopofthe
rectlyruntheapptotriggerthesociallogininterface.Also,itwill
stackwillbepoppedup. Suchanactivityexplorationmechanism
beveryraretohavesophisticatedconstraintsinordertotrigger
canmakeeachsingleviewappearonthescreenmultipletimes.But
theFacebooklogin,andmostofthetimethesociallogininterface
forouranalysis,exploringeachviewonlyonceisenough.
canbetriggeredwiththeirstfewactivitiesiftheappdoescontain
Toavoidexplorationredundancyandensureeiciency,weneed
suchaninterface.Wealsodonotneedsymbolicexecutionforour
touniquelyidentifyeachview.InAuthScope,weuseavectorwith
later stage post-authentication analysis, as long as we can have sixatributes<N,C,T,I,A,H>touniquelyidentifyaview,more
one sample request and response message pair (this is based on
speciically:
theobservationthatiftheserverisvulnerabletotheauthorization,
(1) N:theNameoftheactivity,towhichtheviewbelongs.
it is very likely that this vulnerability will exist in many of its
(2) C: theClassnameoftheview(e.g.,theclassnameof But-
requestmessages). Meanwhile,mostmobileappsaredesignedto
tonandroid.widget.Buton).
pulldatafromservers. Anin-depthactivityexploreshallbeable
(3) T: theTextorimagedisplayedontheview. Typically,the
to trigger at least one such message pair. herefore, we decide
textorimageofaviewshouldbediferentwithotherviews
todesignatargetedappactivityexplorer(§4.1.1),whichwillsolve
inthesameactivity.
bothautomaticserviceloginviasocial-basedsinglesignon(§4.1.2),
(4) I: the ID of the view. Developers may assign each view
but also the generation of post-authentication messages for our
withanIDinthelayoutile.Howeverthisvaluecouldbe
laterstageanalysis.
NULLbecausethisisnotamandatoryrulefordevelopers
andnoteveryviewhasanID.
4.1.1 TargetedAppActivityExplorer (5) A:theclassnameoftheActionbindedtotheview.
Again,whilewecouldhavejustrunrandomdynamictestingtool (6) H: theHierarchyoftheviewinthelayoutile. Typically,
such as Monkey to explore the app activities, such an approach each activity has its own layout ile, which contains the
wouldbeveryineicient(cannotmeetourlargescalestudygoal) typeandlocationofeachview.However,noteveryactivity
andcannotprovideanyguaranteesoftriggeringthecodewein- has a layout ile, because Android allows developers to
tended. Inspired by prior works such as AppsPlayground [34], hard-code the arrangement of the layout in the source
SVM-Hunter[35],andGuiRipping[27,31]inwhichUIelements code.
804

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
With <N,C,T,I,A,H>, AuthScope can uniquely distinguish views.OurDFStraversalalgorithmisdeterministic.herefore,the
eachviewfromothers. Wehavetonotethatwearenottheirst exercisedrequestandresponsemessagesequencesareconsistent
to encounter this view identiication problem. In fact, AppsPlay- amongdiferentusers.
|                           |     | <T,H,L> | whereL |                       |     |     |     |     |     |     |     |     |
| ------------------------- | --- | ------- | ------ | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ground[34]hasused         |     |         |        | representsthelocation |     |     |     |     |     |     |     |     |
| oftheviewinanactivityandT |     |         | andH   |                       |     |     |     |     |     |     |     |     |
arethesameasinAuth- 4.2 MessageFieldRecognitionandSubstitution
Scope. While<T,H,L>maybesuicientintheirapplicationsce- With the exercised request and response messages collected by
nario[34],weindwedoneedmoreinformationinourusecase.
ourman-in-the-middleproxy,nextweneedtoinferthemessage
| Forinstance,weobserveH |     |     | canbemissingbecausenotalldevel- |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ieldsandsubstitutetheieldsofinteresttoseewhethertheserver
L
opers use layout iles for view arrangement. Meanwhile, can has vulnerable authorization implementations. To perform this
be changed in some views. For instance, when scrolling up and automatically,weneedtodesignaprincipledapproachto(1)parse
down, the location of the view in an activity can be changed. In themessageields(§4.2.1),(2)identifytheieldsofinterest(§4.2.2),
contrast,AuthScopehasamuchstricterpolicyindeterminingthe and(3)substitutetheieldsthatareenumerable(§4.2.3).
uniquenessofaview,andourN,C,AwillneverbemissingandH
canbeusedtosolvemostofthescrollingproblems.
4.2.1 ParsingMessageFields
ViewExploration. Whenanactivityiscreated,AuthScopewill SinceAuthScopefocusesonHTTP/HTTPSprotocol,wejustneed
automaticallycreatethe<N,C,T,I,A,H>vectorforeachviewwithin
toparsethepost-authenticationrequestandresponsemessagesfor
theactivity.Havinguniquelyidentiiedeachview,wethenexplore
|     |     |     |     |     |     | thiswell-formedtextprotocol. |     |     | AccordingtotheHTTPprotocol |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | -------------------------- | --- | --- | --- |
thecurrentactivityusingaprioritizedDFSalgorithm.Sinceweaim
speciication[2],eachrequestmessageconsistsof(1)arequestline
toexercisethesociallogininterfacebeforeauthenticationandany
|     |     |     |     |     |     | (e.g., GET | /index.html | HTTP/1.1), | (2) | request-header | ields | (e.g., |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | --- | -------------- | ----- | ------ |
explorableinterfaceaterauthentication(togetsamplerequestand
Host:www.sigsac.org),(3)anemptyline,and(4)optionalmessage
response message pair), we classify all views in the same activity body.Similarly,eachresponsemessageconsistsof(1)astatusline
intothreecategoriesandthenprioritizetheDFStraversalinthe
|     |     |     |     |     |     | (e.g., HTTP/1.1 | 200 | OK), (2) | response-header | ields | (e.g., | Accept- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------------- | ----- | ------ | ------- |
followingorder:
Language:en),(3)anemptyline,and(4)anoptionalmessagebody.
- viewcontainssociallogin(e.g.,Facebooklogin). Both Figure 2 and Figure 3 contains more concrete examples of
| - viewhasabindingaction. |     |     |     |     |     | requestandresponsemessages. |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
- viewhasnobindingaction.
|     |     |     |     |     |     | ParsingRequestMessages. |     |     | Eachrequestmessageneedstobe |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------------------------- | --- | --- | --- |
Tosummarize,similartoAppsPlayground[34],whenanactivity
|              |           |            |      |                          |                | responded                                            | by a server | API, | and this | API can be | indexed | by the |
| ------------ | --------- | ---------- | ---- | ------------------------ | -------------- | ---------------------------------------------------- | ----------- | ---- | -------- | ---------- | ------- | ------ |
| is created,  | AuthScope | recognizes |      | each unique UI           | element (i.e., |                                                      |             |      |          |            |         |        |
|              |           |            |      |                          |                | valueofHostandtheresourcesrequestedintherequestline. |             |      |          |            |         | To     |
| view) of the | activity, | traverses  | each | view using a prioritized | DFS            |                                                      |             |      |          |            |         |        |
parseeachrequestline,weneedtoirstparsethepathsegmentby
algorithm.Iftheviewhasbeenvisitedbefore,wewillnottraverse
scanthereservedpathsymbol“/”andthenretrieveeachdirectory
itagain.Weinishtheexplorationofthecurrentactivity,whenwe
name. IfthereisanyURLencodingintherequestline(asinour
traverseallofitsviews.
runningexample),wealsoneedtoparseeachrequestparameter
|     |     |     |     |     |     | name (e.g., | in_app_token) |     | and its value. | Note | that in | URL en- |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | -------------- | ---- | ------- | ------- |
4.1.2 AutomaticSocial-basedServiceLogin
coding,theparameternameanditsvalueisconnectedbysymbol
Havingthecapabilityofexploringtheappactivities,nextweneed “=”,eachpairisconcatenatedby“&”. Itisquitestraightforward
todrivetheapptoexecutesociallogininterface.Weuseasimilar toindextheparameternameanditsvalue,andwestorethemina
pair<name,value>.
| approach of | how a | real user | recognizes | whether a | view contains |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | ---------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Regardingthemessagebody,itcanbejustempty,dataencoded
sociallogin.Inparticular,takeFacebookloginasanexample,real
|     |     |     |     |     |     | withURLs, | JSON(e.g., | asshowninourrunningexample), |     |     |     | XML, |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ---------------------------- | --- | --- | --- | ---- |
usersrecognizethereisaFacebookloginbyreadingthetextover
aButon,suchas“SigninwithFacebook”or“FacebookLogin”. htmlpage,orjustsometext. WeonlyparseURL,JSONorXML
Byscanningthetextofaviewinthelayoutilewhetherornotcon- encodingsofthemessagebody,andtreattherestjustastext. To
tainingFacebooksub-string,weprioritizetheactivityexploration parse URL encoding, we parse it in the same way as in request
line.ForJSONandXML,theybothhaveahierarchytreestructure,
| tosuchaview. | Ifthereisnosuchstring,theremustbeabinding |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichmeansthateachvaluecanbetrackedbythepathfromthe
| action to invoke        | the | Facebook | login,                              | and our DFS | traversal will |             |             |      |             |            |           |      |
| ----------------------- | --- | -------- | ----------------------------------- | ----------- | -------------- | ----------- | ----------- | ---- | ----------- | ---------- | --------- | ---- |
|                         |     |          |                                     |             |                | root of the | tree. Also, | note | that if the | value of a | parameter | is a |
| alsoeventuallyinvokeit. |     |          | Normally,thislogininterfaceexistsin |             |                |             |             |      |             |            |           |      |
theirstfewactivitiesanditisveryunlikelythattherewillbeany JSONarray,wewillnotconsidertheorderoftheelementinthe
constraintsinvolvedtoinvoketheFacebooklogin. array. hatisthearray[a,b]shouldbetreatedasthesamearray
AterAuthScopesuccessfullyclickstheFacebookloginbuton, as array [b,a] when we build the parameter and value pair (i.e.,
theappwillfollowtheexecutionlogicinthelibraryfromtheFace- <name,value>)whenparsingthemessageield.
book, which is a very standard logic. We just pre-register two heresponsemessageissentby
ParsingResponseMessages.
accountsAliceandBobwiththeFacebookservice(thereasonof
theserverateritprocessestherequest(essentiallythereturnvalue
whyweneedtwousersispresentedin§4.2),andthenautomati-
oftheserverAPI).Wewillassociatetheresponsemessageswith
callyloginthecorrespondingserversusingtheFacebookaccount
|                |           |      |     |                  |           | thecorrespondingrequestmessages. |     |     |     | Similartohowweparsethe |     |     |
| -------------- | --------- | ---- | --- | ---------------- | --------- | -------------------------------- | --- | --- | --- | ---------------------- | --- | --- |
| when the login | interface | pops | up. | he app execution | ater this |                                  |     |     |     |                        |     |     |
stagewilltriggerthosepost-authenticationrequestandresponse
messageswhenperformingourDFStraversaloftheactivitiesand
805

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
ED
requestmessages,weusethesamewaytoparsetheresponsemes- Field-ValueofAlicevs.FieldValueofBob
sagesandbuild<name,value>pairsifthereisany. heresponse fb153b7d8c0a0c6ac841d7bfbd9446de627c642858
+∞
messagewillbeprimarilyusedin§4.3. e67315b35aa38d4ac8cac3cd9c7f88ae7f576d373f
21690
| Indexing |     | the request | and | response | messages. |     | Ater parsing |     |     |     |     |     |     |     |
| -------- | --- | ----------- | --- | -------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1.00
| eachrequestandcorrespondingresponsemessagepair,weneed |     |     |     |     |     |     |     |     | 21691 |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
toindexitsuchthatwecaneasilylocateitduringournextstage Table 1: he Euclidean distance of the difed-ields
analysis(§4.2.2).Essentially,thiscanbeconsideredasaninstance betweenAlice’sandBob’srequestmessages.
ofaserverAPIexecution,andwehavecollectedtheserverinter-
face(i.e.,theURLsthatincludetheHostaddressanddatareference
| path), | theparameters, |     | andreturnvalues. |     |     | herefore, | weindexit |     |     |     |     |     |     |     |
| ------ | -------------- | --- | ---------------- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
clearlyweshouldselectandsubstituteield21690withvalue21691
| based | on the | URLs, | the <name,value> |     | pair | we parsed | from the |     |     |     |     |     |     |     |
| ----- | ------ | ----- | ---------------- | --- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
(aswhatwedidinFigure3),insteadofthein_app_tokenield
requestmessage(whichcanbeconsideredasparameters)andthe
becauseatokenisingeneralunguessableandsubstitutingatoken
responsemessage.
doesnotrevealthevulnerabilities(ifasecuritytokenischanged,
|     |     |     |     |     |     |     |     | the | response should | be changed | as well). | As such, | we need | an  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --------- | -------- | ------- | --- |
4.2.2 IdentifyingFieldsofInterest
|     |     |     |     |     |     |     |     | algorithmtoselecttheenumerableields. |     |     |     | Fortunately,wenotice |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | -------------------- | --- | --- |
Clearly,notallieldsareofourinterest. Forinstance,inourrun- thatbyusingtheEuclideandistanceandpredictablevalues,wecan
ningexampleshowninFigure2(a),wearejustinterestedinield automaticallylocatesuchields.
(ED)
withvalue21690andthein_app_tokenieldinAlice’srequest - Euclidean Distance. An Euclidean distance is a
message.Sincetherearemanynon-relatedieldsinarequestmes- metric that measures the ordinary straight-line distance
sage,wemustautomaticallyselecttheieldsofourinterest. he between two points in Euclidean space. he smaller an
keysolutionhereistousemessagealignment andvaluediing,a ED ofaield,themorelikelytobeguessedbyatackers.
commonapproachusedinprotocolreverseengineering,suchas For instance, as shown in Table 1, the ED of 21690 and
ProtocolInformatics[13].hatexplainswhyAuthScoperequires 21691isjustone,whereastheEDbetweenthetwotokens
atleasttworegisteredusers(e.g.,AliceandBob)withtheservice, is 14a225ca31667f1ff7713f22114be2fe324f6f119 (we thus
consideritagiantastronomicalnumber+∞).
andalsooneuserneedstologinandlogouttwicetoexercisetwo Certainly,
setsofthesamerequestmessages(e.g., Alice’sRequest1 andAl- when having a sample message with 21690, an atacker
ice’sRequest2asshowninFigure4). canquicklyprobeotheruser’sinformationinaserviceby
changingtootherclosernumbers,whereasfortokenitis
|         |     |           |     |              |     | In general, | a request |     |     |     |     |     |     |     |
| ------- | --- | --------- | --- | ------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| Message |     | Alignment | and | Value Diing. |     |             |           |     |     |     |     |     |     |     |
hardforatackerstoguessother’s.
| messagecouldcontainuser-speciicields(e.g,. |     |     |     |     |     | in_app_token), |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
henthenextquestionbecomeshowAuthScopecom-
andnonuser-speciicields(e.g.,therequest-headerields,andalso putesEDanddecideswhetheradistanceis+∞(unguess-
| timestampieldifthereisanyintherequestmessage). |     |     |     |     |     |     | Byusing |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
able).Toachievethis,AuthScopeconvertsalldifedvalue
messagealignmentandvaluediing,wecanquicklylocateuser-
(includingstringsandbytesequences)tonumbersusing
speciicields,andnonuser-speciicields.
|     |     |     |     |     |     |     |     |     | theirminimalbase. |     | Forinstance, | wewillconvert21690 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | ------------------ | --- | --- |
- AligningandDiingDiferentUsers’SameRequest. to a decimal value (using base-10), and the token using
|     | By  | aligning | and diing | with | the same | request | messages |     |                             |     |     |                        |     |     |
| --- | --- | -------- | --------- | ---- | -------- | ------- | -------- | --- | --------------------------- | --- | --- | ---------------------- | --- | --- |
|     |     |          |           |      |          |         |          |     | base-36(alphabetic+number). |     |     | Ifastringcontainsother |     |     |
(recallthatwehaveindexedalloftherequestmessages)
printableASCIIsymbols(recallHTTPistext-basedproto-
|     | of  | two diferent | users | (e.g., | Alice’s | Request1 | and Bob’s |     |     |     |     |     |     |     |
| --- | --- | ------------ | ----- | ------ | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
col),wewillusetheworstcasebase-95toconvertit(there
request),wecanquicklyidentifytheuser-speciicieldsby
aremaximum95printableASCIIcharacters).
selectingthevaluedif-edields.Forinstance,byaligning To decide whether an ED is +∞, we set a threshold
anddiingthetwodiferentusersrequestmessagesshow- based on the number of downloads of the app. he in-
|     | ing                               | in Figure | 2, we | can automatically |     | locate | ield 21690  |     |               | ED      |            |          |              |     |
| --- | --------------------------------- | --------- | ----- | ----------------- | --- | ------ | ----------- | --- | ------------- | ------- | ---------- | -------- | ------------ | --- |
|     |                                   |           |       |                   |     |        |             |     | tuition is if | the     | is smaller | than the | total number | of  |
|     | and21691,andtheieldsin_app_token. |           |       |                   |     |        | herestields |     |               |         |            |          |              |     |
|     |                                   |           |       |                   |     |        |             |     | downloads     | showing | in the app | market,  | we consider  | the |
havenodiferencesandarethereforenotofourinterest.
correspondingieldenumerablebecauseanysubstitution
-
Aligning and Diing Same Users’ Same Request at ofthevaluewithanearbyonewilllikelyleadtothedisclo-
Diferent Time. However, some message-speciic ields sureotheruser’sinformationiftheserverisvulnerable.
(e.g.,timestampifthereisany)canalsobevaluediferent. - PredictableValue.UsingEDcanindmostoftheguess-
herefore,wewillfurtheralignanddifthetworequest
ableields.However,thereareafewspecialcasesthatthe
messagesofthesameuser (e.g.,Alice’sRequest1 andAl- EDmightbe+∞,butitisguessable.
Oneexampleisthe
ice’sRequest2)toremovethosemessage-speciicields.
|     |     |     |     |     |     |     |     |     | emailaddress. | Verylikely,theEDoftwoemailaddresses |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------------------------- | --- | --- | --- | --- |
canbe+∞,butanatackercaneasilyguessother’semail
| Selecting |     | the Fields | of Interest. |     | he key | objective | of Auth- |     |     |     |     |     |     |     |
| --------- | --- | ---------- | ------------ | --- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
addressbecauseoftherecenthugedataleakageofuserac-
| Scopeistodiscoverthevulnerable |     |     |     |     | authorizationbyperforming |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
countsinonlineservices,makingtheemailaddressvalue
whatanatackercoulddo—substitutingaguessableieldandob-
servingwhetherotheruser’sinformationcanbeleaked.herefore, predictable. herefore,weusestringmatchingtohandle
|     |     |     |     |     |     |     |     |     | suchields. | Morespeciically, |     | ifanyoftherequestmes- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --- | --------------------- | --- | --- |
weshouldfocusontheieldsthatareguessableorenumerable(can
sagecontainsAlice’semailaddress(usingemailaddress
| be  | performed | by  | a brute-force | atack). | In  | our running | example, |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------- | ------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
806

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
paternmatching),thisguessableemailaddressieldisof vulnerableinterfacesidentiiedareusedtoprovidethepublicre-
ourinterest. sources.Sinceitisapublicresource,nomaterhowwesubstitute
heotherexampleistheFacebookID(FID).Whileit theenumerableields,theserverwillalwaysreturnthesamere-
isagiantinteger(e.g.,17927643151,whichistheACM’s), sponse.Forinstance,anewsappthatprovidesnewstosubscribed
itcanbepubliclycrawled. OtherthanthisID,whenuser users may be lagged as vulnerable if the news is fetched ater
usingFacebooklogintologintoaspeciicapp,Facebook authenticationandthisnewscanalsobeaccessedwithoutlogin
willissueanapp-speciicID[1](e.g.,106611716575863as (apublicresource).
showninthecasestudyinFigure6)totheuserwhichis Tofurtherprunesuchcases,wethenletAuthScopetakeone
uniquetoeachapp,andsuchIDcanalsobeeasilycrawled morerunoftheappwithoutloggintheservice. hatis,whenit
(e.g., within the app). herefore, we also call this app- encounters the Facebook login interface, it directly skips it and
speciicIDFIDandconsideritpublicavailableknowledge. continues exploring the app as deeply as it can. We will align
Similartotheemailcase,ifweobserveAlice’sFIDisused theseaterauthentication-skippedrequestmessageswiththosein
in a request message, we will replace it with Bob’s and Alice’sandBob’s.Ifweobserveapreviouslyidentiiedvulnerable
observehowserverwouldrespondtherequest. interfacecanactuallyservethepublicresource,wewillnotlagit
vulnerable.
4.2.3 SubstitutingEnumerableFields
5 EVALUATION
Now we have identiied all of the guessable ields, next Auth-
WehaveimplementedAuthScopeatopAndroid4.4platformby
Scopewillsubstitutethemtodecidewhetherthereisavulnerable
usingtheXposed[6]frameworktodrivetheappexecutionandper-
authorizationimplementation. hisstepisquitestraightforward:
formtargetedappexploration,andourman-in-the-middleproxyis
for any identiied enumerable ields in Alice’s request message,
implementedwiththeBurpSuite[5].Intotal,AuthScopeconsists
our man-in-the-middle proxy will just replace the value of this
ofover5,000linesofourownJavacodeand300linesofourown
ieldwithBob’s. Iftherearemultipleields,wewillsendmultiple
pythonscripts. Inthissection,wepresentourdetailedevaluation
requestmessages. Onlyoneieldatatimeissubstitutedineach
results.
message, and we will not simultaneously substitute ields at the
sametime(asitisunlikelythatanauthorizationdependsontwo
5.1 ExperimentSetup
ields).
DatasetCollection. Asoftoday,GooglePlayhasover2million
4.3 ResponseMessageLabeling
mobile apps. To have a reasonable coverage of these apps, we
AterwehavesentaieldsubstitutedrequestmessageofAlicewith crawledthetop10%offreemobileappsbasedonthenumberof
thevalueofBob’stotheserver,wethenlabeltheresponsemessage installsinMarch2017.RecallthatAuthScoperequiresautomatic
to determine whether the server is vulnerable. he key idea to loginandcurrentlyweonlyfocusontheappsthatuseFacebook
decide this is if the response message returns the identical ones login,andthuswehavetoselectsuchapps. Tothisend,weirst
withthesameresponsemessagerequestedbyBob,thentheserver analyzedthe200,000appstoilteroutthosethatdonotimport
isvulnerable. anyFacebooklibraries.NotethatifanapphasnotimportedFace-
Morespeciically,welabelaresponsemessagethatisreturned book libraries, deinitely it does not have Facebook login. Ater
by a ield-substituted Alice’s request message is identical to the thisinitialiltering,wehave33,950remainingapps.
correspondingBob’sresponse, iftheuser-speciicdatainthere- However,evenifanapphasimportedFacebooklibrary,thereis
sponsemessageisthesame(byte-by-byteidentical). hatis,we noguaranteethatitwilluseFacebooklogin,wehavetoperforma
willremovethosenon-userspeciicdata(suchasmessage-speciic furtheranalysis.Inparticular,wehaveobservedthattherearetwo
timestamp) using the diferential traic analysis again, i.e., the waystointegrateFacebooklogininanapp:(1)directlyputaFace-
alignmentanddiferingapproachdescribedin§4.2.2whenidenti- bookloginbuton(implementedbyFacebooklibrary)inoneofits
fyingthenon-userspeciicieldintherequestmessages.Without activitylayoutiles,or(2)callFacebookloginfunctionusingpro-
diferentialanalysis, wewill not be able to tell we have success- gramcode. Basedonthesetwoobservations,wedesignanother
fullyretrievedBob’sdatabyjustbyte-by-bytecomparisonofthe screeningprocedure,whichirstcheckswhethertheFacebooklo-
response messages if there is any message-speciic data. Ater ginbutonexistsinoneofitsactivitylayoutileswithinanapp;if
removing these non-user speciic data in the response message, theredoesnotexistsuchabuton,thencontinuestosearchcode
AuthScope outputs that the server is vulnerable if we ind an thatinvokingFacebookloginmethodsfromtheFacebooklibrary.
identical response for the corresponding request interface. We hiscodesearchisimplementedbyusingtheSootframeworkand
will keep substituting and labeling, until all the Alice’s request checkingthefunctioncallpaterns. Iftheilterneitherindsout
messageshavesubstituted. Ifnoneoftheresponsemessagesare the Facebook login buton nor the invoking code, then this app
identical with initial Bob’s, then the server is not vulnerable. A willbediscarded. Withalltheseilteringanalyses,eventuallywe
server may have multiple vulnerable interfaces if multiple of its have4,838appsinourdataset.
serverrequestinterfacesarevulnerable.
TestingEnvironment. AllofourappsweretestedinarealLG
Pruning the Vulnerable Interface that Provides Public Re- Nexus4smartphonewithAndroid4.4system. hisphoneisin-
sources. Certainly, AuthScope can have false positives if the stalledwithourapppost-authenticationmessagegenerationcom-
ponent, and is connected with a Ubuntu 14.04 desktop running
807

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
150
sppAelbarenluVforebmuN
100
50
0
Reference e ss o n ment n ce Drink m es Fitnes s ty le avigation ic a l di o n e s h y oductivity Shopping Social o l s c a l Editors
|     |       |     | in a ti   |       | Fin a | a     | es   | ed  | A u agazi | tograp | T o | L o     |     |     |
| --- | ----- | --- | --------- | ----- | ----- | ----- | ---- | --- | --------- | ------ | --- | ------- | --- | --- |
|     |       |     | Bu s unic | rtain | &     | G     | L if | M   | &         |        |     | & &     |     |     |
|     |       |     | m         | e     | o d   | lth & | N    |     | i c M     | h o r  | v e | l s     |     |     |
|     | Books | &   | m n t     |       | F o   | a     | &    | u s | & P       | P      | r a | lay e r |     |     |
|     |       |     | C o E     |       |       | H e   | ap s | M   | w s       |        | T   |         |     |     |
|     |       |     |           |       |       |       | M    |     | N e       |        | o   | P       |     |     |
d e
V i
Figure5:DistributionoftheVulnerableInterfacesBasedontheAppCategory.
Item Value We mutated in total 57,736 ields, and found 2,976 suspicious
| Σ#Apps |     |     |     |     |     |     | 4,838 |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
serverinterfacesthathavevulnerableauthorizationimplementa-
ΣTimetoperformthetest(hours) 562.4 ourfurtheranalysisrevealedthat2,379are
tion. Amongthem,
| Σ#Requestmessages |     |     |     |     |     |     | 3,220,886 |        |          |                         |     |          |                |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | ----------------------- | --- | -------- | -------------- | --- |
|                   |     |     |     |     |     |     |           | public | resource | interfaces. Eventually, |     | we found | 597 vulnerable |     |
| Σ#HTTPMessages    |     |     |     |     |     |     | 178,539   |        |          |                         |     |          |                |     |
serverinterfacesaterpruningthosethatprovidepublicresources,
| ΣSizeofthemessages(G-bytes) |     |     |     |     |     |     | 59.2 |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
andtheymapto306mobileapps.
ΣTimeofactivityexplorationbeforeauthentication(hours) 169.9 Tounderstandthosepopularvulnerableservices,wepresentthe
| Σ#Exploredactivitiesbeforeauthentication |     |     |     |     |     |     | 15,367 |                                                 |     |     |     |     |           |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ----------------------------------------------- | --- | --- | --- | --- | --------- | --- |
|                                          |     |     |     |     |     |     |        | distributionsofthesevulnerableappserversbasedon |     |     |     |     | thecorre- |     |
Σ#Identiiedviewsbeforeauthentication 503,441 spondingtoplevelappcategory2assignedbyGooglePlay.hisre-
| Σ#Exploredactivitiesaterauthentication |     |     |     |     |     |     | 20,704 |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
sultisshowninFigure5.Interestingly,wefoundtheseappsbelong
| Σ#Identiiedviewsaterauthentication |     |     |     |     |     |     | 1,181,442 |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
to20categories.hetopthreecategoriesincludeLifestyle(which
| Σ#Mutatedields |     |     |     |     |     |     | 57,736 |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
has153vulnerableinterfaces),Game(99),andShopping(72).One
| Σ#Suspiciousinterfaces |     |     |     |     |     |     | 2,976 |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
reasonofwhythesecategoriescontainsomanyvulnerableimple-
| Σ#Publicinterfaces |     |     |     |     |     |     | 2,379 |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Σ#Vulnerableinterfaces 597 mentationisthatwefoundtheappsinthesecategoriestypically
Table2:OverallExperimentalResult. highlyinteractive,theuserdataisotenstored,shared,updatedin
theirservers,whichalsomeanstherearemoreresourcesinthose
|     |     |     |     |     |     |     |     | appsandmorecomplicatedaccesscontrolimplementation. |     |                   |               |                 |     | Also, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | ----------------- | ------------- | --------------- | --- | ----- |
|     |     |     |     |     |     |     |     | surprisingly,                                      |     | we found a number | of vulnerable | implementations |     |       |
atop an Intel i7-6700k Skylake 4.00 GHz CPU with 8G memory. inFinance(3)andBusiness(9)relatedapps. hedataleakagein
| his | desktop | controls | the automatic |     | app execution |     | in the smart- |     |     |     |     |     |     |     |
| --- | ------- | -------- | ------------- | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
theseserverscancauseseriousdamagestotheendusers.Wewill
phonethroughtheADBinterfacebypythonscript,andmeanwhile
discusstheseverityoftheseleakagesin§6.
| intercepts, |     | collects, | and mutates | the | network | messages | between |             |     |                                            |     |     |     |     |
| ----------- | --- | --------- | ----------- | --- | ------- | -------- | ------- | ----------- | --- | ------------------------------------------ | --- | --- | --- | --- |
|             |     |           |             |     |         |          |         | MicroLevel. |     | Aterwehavedescribedtheoverallresult,nextwe |     |     |     |     |
theappsandremoteservers,usingourman-in-the-middleproxy.
showclearlyhowAuthScopeperformsforeachapp.Weselected
Also,weregisteredwithFacebooktwotestaccountsAliceandBob
|      |       |         |                         |     |     |                  |     | the | top downloaded | app in each | vulnerable | server | category | pre- |
| ---- | ----- | ------- | ----------------------- | --- | --- | ---------------- | --- | --- | -------------- | ----------- | ---------- | ------ | -------- | ---- |
| with | email | address | alice4testapp@gmail.com |     |     | and bob4testapp@ |     |     |                |             |            |        |          |      |
gmail.com,respectively. sented in Figure 5 and show the detailed result in Table 3. he
irsttwocolumnsarethecategorynameandpackagename3,re-
5.2 EvaluationResult spectively,followedbythenumbersof activitiesthatweexplored,
|     |     |     |     |     |     |     |     | and | the numbers | of unique | views that | we identiied | during | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | ------------ | ------ | --- |
MacroLevel. Wespent562.4hoursintotaltodynamicallyana- dynamicanalysisoneachapp. heithcolumnisthetimethat
lyzethese4,838apps,andeventuallywediscovered597vulner- oursystemspentonindingFacebooklogin,whichisthetimefrom
ableauthorizationimplementationsinthecorrespondingservers
startingtheapptosuccessfullylogintheapp.hesixthcolumnis
thatmapto306apps.heoverallexperimentalresultispresented
totalnumbersofrequestmessagesthattheapphasgenerated,the
inTable2.Intotal,wegenerated3,220,886requestmessages,and seventhcolumnisthetotalnumberofieldsthatwesubstituted
amongthem,178,539areHTTPprotocols(therestareHTTPS). 2heonlyexceptioniswefurtherclusteralltoplevelgamesub-categoryintoagame
| hetotalsizeofthesemessagesis59.2G-bytes. |     |     |     |     |     | Toexecutethe |     | category. |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
Facebooklogin,ouranalysisspent196.9hours,duringwhichwe 3Fortheappswhoseservershavenotbeenpatchedyetasthetimeofthiswriting,we
explored 15,367 activities, and 503,441 views. Ater we get au- donotrevealtheirfullnameandinsteadanonymizetheirnamewith***.
|              |     |             | 20,704 |             |     | 1,181,442 |        |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ------ | ----------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| thenticated, |     | we explored |        | activities, | and |           | views. |     |     |     |     |     |     |     |
808

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
|     |     |     | # # | Timeto #Request | #Mutated | #Public #Vulnerable |     |
| --- | --- | --- | --- | --------------- | -------- | ------------------- | --- |
Category PackageName Activities Views Login(s) Messages Fields Interfaces Interfaces
| Books&Reference      | com.***.e***                 |     | 3 288    | 45        | 975 16 | 5   | 3   |
| -------------------- | ---------------------------- | --- | -------- | --------- | ------ | --- | --- |
| Business             | com.***.k***                 |     | 8 1,224  | 30        | 927 12 | 2   | 3   |
| Communication        | com.***.w***                 |     | 18 970   | 41        | 727 1  | 0   | 1   |
| Entertainment        | com.***.c***                 |     | 3 184    | 32        | 739 2  | 0   | 1   |
| Finance              | com.***.m***                 |     | 8 549    | 16        | 790 7  | 0   | 2   |
| Food&Drink           | com.***.h***                 |     | 10 924   | 21 1,032  | 8      | 4   | 1   |
| Games                | com.***.c***                 |     | 7 609    | 20 1,050  | 7      | 3   | 1   |
| Health&Fitness       | com.***.u***                 |     | 12 788   | 15        | 966 10 | 2   | 2   |
| Lifestyle            | com.m***                     |     | 17 1,938 | 25 1,229  | 29     | 5   | 5   |
| Maps&Navigation      | com.***.***.c***             |     | 11 667   | 26        | 490 12 | 7   | 1   |
| Medical              | com.***.a***                 |     | 18 1,616 | 23        | 927 9  | 2   | 1   |
| Music&Audio          | com.b***                     |     | 2 456    | 25        | 933 15 | 3   | 1   |
| News&Magazines       | com.***.a***                 |     | 5 462    | 37        | 880 9  | 0   | 2   |
| Photography          | com.***.j***                 |     | 15 909   | 26        | 965 7  | 0   | 1   |
| Productivity         | com.***.d***                 |     | 15 1,347 | 32        | 882 10 | 5   | 1   |
| Shopping             | cl.***.***.i***              |     | 8 795    | 44        | 961 10 | 0   | 5   |
| Social               | in.v***                      |     | 10 645   | 20 1,068  | 20     | 4   | 5   |
| Tools                | com.mediaingea.uptodown.lite |     | 7 1,347  | 112 1,276 | 25     | 6   | 1   |
| Travel&Local         | com.t***                     |     | 5 321    | 35 1,024  | 10     | 0   | 2   |
| VideoPlayers&Editors | cz.***.n***                  |     | 4 218    | 25        | 821 5  | 1   | 1   |
Table3:DetailedExperimentalResultsforTopTestedAppinEachCategory.
| Category |     | DetailedPrivacyType |     |     |     |     |     |
| -------- | --- | ------------------- | --- | --- | --- | --- | --- |
UserE-Proile 01 Email, 02 UserID, 03 RegistrationDate, 04 IPAddress, 05 LastLoginDate, 06 LastUpdateDate
UserPhysical-Proile 07 RealName, 08 Birthday, 09 Geo-location, 10 HomeAddress, 11 PhoneNumber, 12 BodyInformation
| UserSecrets |     | 13 Token, 14 Password, | 15 PassCode |     |     |     |     |
| ----------- | --- | ---------------------- | ----------- | --- | --- | --- | --- |
AppSpeciicPrivateData 16 InAppMessages, 17 ShoppingHistory, 18 BookShelf, 19 FavoritesorSubscription, 20 AccountBalance
|     |     | 21 ContactsInformation, | 22 PaymentInformation, | 23 PrivateActivityInformation |     |     |     |
| --- | --- | ----------------------- | ---------------------- | ----------------------------- | --- | --- | --- |
Table4:UserPrivacy
|     |     |     | Credential User | User | User AppSpeciic |     |     |
| --- | --- | --- | --------------- | ---- | --------------- | --- | --- |
APP Version Type E-Proile Physical-Proile Secrets PrivateData
| com.***.e*** |     | 2.2 | N0101 0102 | 0708011011 |     | 010118 |     |
| ------------ | --- | --- | ---------- | ---------- | --- | ------ | --- |
com.***.k*** 2.0.11 01E 01 010203040106 0701091011 1314 01170119
| com.***.w***  |     | 1.0.5 | 0101F 0102  | 07         | 13  | 160101190121 |     |
| ------------- | --- | ----- | ----------- | ---------- | --- | ------------ | --- |
| com.g***.c*** |     | 2.4.1 | 01E 01 0102 | 0101010111 | 13  | 0117010120   |     |
com.***.m*** 1.6.8 N 0101 0102 0701091011 010115 16010101200122
| com.***.h*** |     | 2.5.6.0 | 01E 01 0102   |              | 13  | 16010119   |     |
| ------------ | --- | ------- | ------------- | ------------ | --- | ---------- | --- |
| com.***.c*** |     | 2.6.1   | 0101F 01      | 07010110     | 13  | 01010119   |     |
| com.***.u*** |     | 2.03    | N 0101 010203 | 070801010112 |     | 16010119   |     |
| com.m***     |     | 7.3.0   | N 0101 0102   | 07080110     |     | 1601011920 |     |
com.***.***.c*** 7.5.5v 0101F 0102 0701091011 13 01010119010122
| com.***.a***                 |     | 3.09    | 0101F 0102        | 07         | 13  | 16010119         |     |
| ---------------------------- | --- | ------- | ----------------- | ---------- | --- | ---------------- | --- |
| com.b***                     |     | 2.0.4   | N 0101            |            |     | 01010119         |     |
| com.***.a***                 |     | 2.3.2   | N 0101 0101030405 | 070809     | 13  | 16010119         |     |
| com.***.j***                 |     | 2.7.4   | 0101F 010203      | 07         | 13  | 16010119         |     |
| com.***.d***                 |     | 2.4.2   | 01E 01 010203     | 070109     | 13  | 0101010101010123 |     |
| cl.***.***.i***              |     | 2.1.0   | N 0101 0102       | 070809     |     | 0101010120       |     |
| in.v***                      |     | 4.4.5.2 | N 0101            | 0708       |     | 160101190121     |     |
| com.mediaingea.uptodown.lite |     | 3.18    | 0101F 0102        |            | 13  | 16010119         |     |
| com.t***                     |     | 1.4.0   | 0101F 0102        | 0101011011 | 13  | 1601010101010123 |     |
| cz.***.n***                  |     | 4.8     | 0101F 0102        | 07         | 13  | 0101010101010123 |     |
Statistics 8 4 8 141605020101 150606070601 130101 1102011304020203
Table5:VulnerabilityDetailsforTopTestedAppinEachCategory,whereNdenotesNumericvalues,EdenotesEmails,
andFdenotesFacebookIDs.
809

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
| forthetestedapp,theeighthcolumnisthenumberofpublicin-    |     |     |     |     |     |     | 00 {    |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
| terfaceidentiied,andthelastcolumnisthenumberofvulnerable |     |     |     |     |     |     | 01  ... |     |     |     |     |     |     |
02  "response":{
03   "user":{
interfacediscoveredforthetestedapp.
04    "idnum":false,
| WecannoticefromTable3thatsomeappshavemanyactivities, |     |     |     |     |     |     | 05    "name":"Bob", |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
06    "lastname":"Ccs",
whichmeansitwouldbereallyhardtouseblinddynamicanalysis 07    "birthday":"1990-04-26",
toolssuchasMonkey[7]toexplorealloftheseactivities. Also,all 08    "gender":"M",
09    "email":"bob4testapp@gmail.com",
appshavehundredsofrequestmessages. hisisactuallybecause 10    "type":"EMAIL",
many of the messages are related to Facebook login. In our ex- 11    "firstlogin":"1",
12    "country":{
13     "id":"10",
periment,wefoundforeachFacebooklogin,Facebooklibrarywill 14     "name":"United States",
| generatehundredsofrequestmessagestostatic.xx.fbcdn.netto |     |     |     |     |     |     | 15     ... |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
16    },
| retrievejsiles. |     |     |     |     |     |     | 17    "post_on_activities":"disabled", |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
18    "bananas_count":0,
| Also, | the last column | shows | that | 9 apps | have more | than one |     |     |     |     |     |     |     |
| ----- | --------------- | ----- | ---- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
19    "id":"673491",
(from2to5)vulnerableauthorizationinterfacesattheserverside, 20    "fbid_number":"106611716575863",
21    "current_latitude":”30.9863214",
| and 13 apps | also | contain | several | (from 1 | to 7) public | interfaces. |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | ------- | ------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
22    "current_longitude":”-86.7501116",
Interestingly,wealsoindiftheatacksurfaceiseitheremailad- 23    "bananas_history":"https:\/\/profile.*******.com\/bananas\
/store\/673491\/?accesstoken=debda35ccd92f4b8e2e06f0bff3b6e49279
a557d&latitude=30.9863214&longitude=-86.7501116&lang=",
dressorFID,thentherewillbejustonevulnerableinterface(and
24    ...
| this interface | is usually | the | one serves | the | irst request | message | 25   } |     |     |     |     |     |     |
| -------------- | ---------- | --- | ---------- | --- | ------------ | ------- | ------ | --- | --- | --- | --- | --- | --- |
26  }
| rightaterauthenticatedwithFacebook). |     |     |     |     | Iftheatacksurfaceis |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
27 }
apredictablenumber,thentherearelikelymorethanonevulner-
| ableinterfaces. | hisisbecauselikelyallotherrequestsalsouse |     |     |     |     |     |        |          |      |               |             |     |     |
| --------------- | ----------------------------------------- | --- | --- | --- | --- | --- | ------ | -------- | ---- | ------------- | ----------- | --- | --- |
|                 |                                           |     |     |     |     |     | Figure | 6: Alice | Read | Bob’s Account | Information |     | in  |
thepredictablenumber,whichmakestheircorrespondingserver
appI.
interfacesallvulnerable.
6 SECURITYANALYSIS privatedatafromthevictimservers. Inourexperimentsetings,
|     |     |     |     |     |     |     | an adversary | can | possibly | get up to 61 | million | mobile | users pri- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------ | ------- | ------ | ---------- |
6.1 SystematizedAnalysis
vaterecordaccordingtothetotalnumberofdownloadsforallthe
Next,wewouldliketounderstandwhatkindofdataleakagethe
vulnerableapps.
vulnerableaccesscontrolimplementationcancauseandhowse-
| vere they | are. To | this end, | we have | manually | examined | the 20 |     |     |     |     |     |     |     |
| --------- | ------- | --------- | ------- | -------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
6.2 CaseStudies
| vulnerableappserversfortheapppresentedin |              |     |               |     | Table3. | Tosys-         |                                          |     |     |     |     |                  |     |
| ---------------------------------------- | ------------ | --- | ------------- | --- | ------- | -------------- | ---------------------------------------- | --- | --- | --- | --- | ---------------- | --- |
|                                          |              |     |               |     |         |                | Asdemonstratedinoursystematizedanalysis, |     |     |     |     | vulnerableautho- |     |
| tematize                                 | the leakage, | we  | irst classify | the | leaked  | data into four |                                          |     |     |     |     |                  |     |
categoriesasshowninTable4(basedonourbestunderstanding) rizationcaneasilyleadtouserprivatedataleakage.Tounderstand
|           |               |          |            |           |             |              | this threat                                  | more    | concretely, | in the following, |       | we would | like to   |
| --------- | ------------- | -------- | ---------- | --------- | ----------- | ------------ | -------------------------------------------- | ------- | ----------- | ----------------- | ----- | -------- | --------- |
| including | user e-proile |          | such as    | her email | address,    | service reg- |                                              |         |             |                   |       |          |           |
|           |               |          |            |           |             |              | perform                                      | further | analysis    | of two mobile     | apps, | namely   | the I app |
| istration | date, IP      | address, | last login | date,     | last update | date; user   |                                              |         |             |                   |       |          |           |
|           |               |          |            |           |             |              | andcom.***.k***(wejustcallitK)appfromTable3, |         |             |                   |       |          | toshow    |
physicalproilesuchasfullname,birthday,geo-location,home
howtheycouldleakuser’sprivacysensitivedataincludinguser’s
address,phonenumber,andbodyinformationsuchasweightand
secrets. hesetwocasestudiesrequiredetailedknowledgeofthe
height; usersecretssuchasaccesstoken,userpassword(either
plaintextorhashed),apppasscode;andappspeciicprivatedata mobileappsandwereconductedmanually.
suchasshoppinghistory,bookshelf,favorites,paymentinforma- Sensitive Data Leakage. We use I app as an example to illus-
tion,accountbalance,etc.Basedontheseclassiication,welooked tratethisatack. I appisaverypopularappinGooglePlaywith
into each of the vulnerable service interface and examined their 100,000to500,000downloads.hisappcanprovidediscountin-
dataleakage.hedetailedresultforthese20vulnerableserversis formationforshopping. Duringourtest,AuthScopeintercepted
presentedinTable5.
|     |     |     |     |     |     |     | the Alice’s | request | which | asks for personal | information, |     | and re- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | ----------------- | ------------ | --- | ------- |
From the 3rd column of Table 5, we notice that 8 out of 20 placedAlice’saccountIDorUID(673436)withBob’sUID(673491)
vulnerableserversjustusepredictablenumberstoaccessauser’s foranewrequest. Figure6showsaportionoftheresponsemes-
privateinformation(e.g.,forappcl.***.***.i***andwewilljust sage. WecanseeclearlythatitleaksalotofBob’ssensitiveinfor-
callitI
app,ouruserAlicehasaUID673436andBobhas673491 mation,includinghisbirthday,gender,email,FacebookID,current
as presented in Figure 6), 4 use email addresses, and 8 use FIDs. locationandbalancehistory.
Also,wecanobservethatvarioususerprivatedatacanbeleaked
|     |     |     |     |     |     |     | For this | app and | so many | other alike | apps, | the atacker | only |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | ----------- | ----- | ----------- | ---- |
fromthevulnerableservers.hetopleakeddataincludesUID(16),
needstogettheUIDofausertoperformtheatack.Moreover,to
emailaddress(14),andsecuritytoken(13).Notethatthesetokens getother’sUIDisrelativelystraightforward. Inthisapp,theUID
actuallybelongtoBob,butcanberetrievedbyAlice. Meanwhile, isgeneratedincrementally,notrandomly. Givensucha6-bitUID
surprisingly, some of the servers even leak user’s password, as anditsinstallnumbers,statically,anatackercaneasilyenumer-
shown in Figure 7. his is astonishing, since a user’s password ate other’s UID. Since this app has close to 500,000 installs, an
shouldneverbeleakedtoaclientregardlessofthequery. adversarycaneasilyretrieve500,000user’sprivateinformation.
Inshort,givensucheasilypredictablenumbersandpotentially
publicavailableemailaddressesandFIDswithoutanyfurtherau-
| thorizationchecks, |     | itmakesanatackertriviallycrawlalluser’s |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
810

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
| 00 { |     |     |     |     |     | 7 DISCUSSIONS |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
01  "pk_i_id": "163126",
02  "dt_reg_date": "2017-04-30 23:21:59",
03  "dt_mod_date": "2017-04-30 23:36:58", Limitations and Future Works. While AuthScope has made
04  "s_name": "Bob Ccs",
airststeptowardsautomaticdiscoveryofauthorizationvulnera-
05  "s_username": "163126",
06  "s_password": "7c4a8d09ca3762af61e59520943dc26494f8941b", bilitiesinonlineservice,itstillhasanumberoflimitations. First,
07  "s_secret": "6stgMaAb",
08  "s_email": "bob4testapp@gmail.com", clearlyAuthScopehasfalsenegatives. Forinstance,weonlyfo-
09  "s_website": "bob.ccs\/index.html",
10  "s_phone_mobile": "4695855213", cusedontheappsthatuseFacebooklogin(essentiallyusingFace-
11  "s_pass_ip": null, booklogintobypasstheauthenticationstep),butnotalltheapps
12  "fk_c_country_code": null,
13  "s_country": "Tanzania", havebeenusingthissociallogin. Inourexperiment,weiltered
| 1 4     "s _ a d | d r e s s " :   " 1 5 | 2 4 6  S n i  Rd. APT 252 Tanzania", |     |     |     |     |     |     |     |     |     |
| ---------------- | --------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
morethan25,000mobileappsthatdonotcontainFacebooklogins.
| 1 5    " f k _ i | _ r e g i o n _ i d " | :  " 1 7 " , |     |     |     |     |     |     |     |     |     |
| ---------------- | --------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
16  "s_region": "Mara", Howtohandleothersocialloginschemes(e.g.,Googlelogin),or
17  "d_coord_lat": null,
18  "d_coord_long": null, ingeneralhowtoautomaticallyloginaremoteserviceisstillan
19  "b_company": "0",
20  "i_items": "1", unsolvedproblem. hismayrequiresolvingthechallengesofau-
21  "i_comments": "0",
tomatedservicesignup,moreintelligentAndroidUIrecognition
22  "dt_access_date": "2017-04-30 23:46:05",
| 23  "s_access_ip": "", |     |     |     |     |     | andtestcasegeneration,etc. |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
24  "b_prefer_phone": "1",
|     |     |     |     |     |     | Second, | AuthScopeonlydiscoverstheauthorizationvulnera- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ---------------------------------------------- | --- | --- | --- | --- |
25  "s_dialing_code": "+255",
26  "fk_i_category_id": "22", bilitythatleadstotheinformationleakageandaccounthijacking
27  "s_facebook_page": "http:\/\/",
28  ... atacks. Basically,theseareatacksthatleadtounauthorizedread.
29 }
|     |     |     |     |     |     | However, there | are also | many | other interesting | atacks such | as  |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | ---- | ----------------- | ----------- | --- |
theunauthorizedwrite.Forinstance,ausershouldnotmodifyany
Figure7:AliceReadBob’sInformationinappK. itemsthatbelongtootherusers.Currently,AuthScopeisnotable
toinfertheunauthorizedwriteautomatically.
|                    |     |                                     |     |     |     | Finally, | the vulnerable | authorization | is a | general problem | in  |
| ------------------ | --- | ----------------------------------- | --- | --- | --- | -------- | -------------- | ------------- | ---- | --------------- | --- |
| SecretDataLeakage. |     | Otherthanuser’sprivatedata,moresen- |     |     |     |          |                |               |      |                 |     |
onlineservicesandisnotjustlimitedtoAndroidapp’sserverside
| sitive secret | data can | also be leaked | from the | vulnerabilities | dis- |                 |                                           |     |     |     |     |
| ------------- | -------- | -------------- | -------- | --------------- | ---- | --------------- | ----------------------------------------- | --- | --- | --- | --- |
|               |          |                |          |                 |      | implementation. | Currently,weonlydevelopedtheprototypethat |     |     |     |     |
K
covered by AuthScope. Considering the app as an example, performsdynamicAndroidappanalysisandprotocolreverseengi-
itisasecond-handgoodstradingapponGooglePlay,whichhas neeringtoinferthevulnerability,andwebelieveourmethodology
between500,000and1,000,000downloads. Withthisapp,any canalsobeappliedtootherplatformssuchasiOSandWindows.
registered user can sell/buy second-hand goods. Unfortunately, Also,AuthScopecurrentlyonlyhandlesthenetworkcommunica-
wefoundtheauthorizationvulnerabilitycanleadtouser’ssecret tionswithHTTP/HTTPSprotocols. Wewillstudyhowtoenable
dataleakage.
AuthScopetoanalyzethevulnerabilitiesforotherplatformsand
Inparticular,aterauthentication,theserverwillpushdetailed otherprotocols,aswellasaddressingtheirsttwolimitationsin
| informationoftheuserbasedonheremailaddress. |     |     |     | Atersubsti- |     | ourfuturework. |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
tutingAlice’semailwithBob’s,AuthScopesuccessfullygotBob’s
|              |                              |     |     |             |     | PracticalityoftheAttackandCountermeasures. |     |     |     | Itisabso- |     |
| ------------ | ---------------------------- | --- | --- | ----------- | --- | ------------------------------------------ | --- | --- | --- | --------- | --- |
| information, | partofwhichisshowninFigure7. |     |     | Aswecansee, |     |                                            |     |     |     |           |     |
lutelyincorrecttousepredictablenumberswithoutfurtherautho-
therearequiteanumberofprivaterecordsintheresponsemessage
suchastheregistrationdate(line2),modiicationdate(line3),user rizationcheckstoallowaccessofauser’sprivateresource. How-
ever,servicedevelopersmayfeelitissecuretojustuseemailad-
name(line4),phonenumber(line10),homeaddress(line14),Geo-
dressorothersophisticatednumberssuchasFacebookIDforthe
location(line17,18whichisnullinourtestcase),lastlogintime
|     |     |     |     |     |     | authorization. | However, | wehavetonotethatrecentlythereare |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | -------------------------------- | --- | --- | --- |
(line22). Amongtheseleakeddata,themostdangerousrecordis
massivedataleakagesandhugevolumeofInternetuser’semailad-
Bob’shashedpassword(whichis7c4a8d09ca3762af61e59520943
|                 |                                        |     |     |     |     | dresseshavebeenleaked. |     | Wehavetoconsiderthatemailaddress |     |     |     |
| --------------- | -------------------------------------- | --- | --- | --- | --- | ---------------------- | --- | -------------------------------- | --- | --- | --- |
| dc26494f8941b). | Undernocircumstanceshouldtheappprovide |     |     |     |     |                        |     |                                  |     |     |     |
user’spasswordtotheuser.Withafurtherinvestigation,wefound is a public information now. Also, Facebook ID can be crawled
|                    |     |           |                 |        |        | and it can                   | also be considered |     | public. herefore,               | the atacks | we  |
| ------------------ | --- | --------- | --------------- | ------ | ------ | ---------------------------- | ------------------ | --- | ------------------------------- | ---------- | --- |
| this hash password | is  | generated | by SHA-1, which | can be | easily |                              |                    |     |                                 |            |     |
|                    |     |           |                 |        |        | discoveredarequitepractical. |                    |     | Toreallyixthesevulnerabilities, |            |     |
crackedbymanyonlineservices(e.g.,https://crackstation.net/which
weurgeservicedeveloperstofollowthebestpractices(aswehave
takeslessthanasecondtoreturntheplaintextofthispassword).
|           |               |               |        |            |       | discussed in | §2.3) such | as using | random token | in each session, |     |
| --------- | ------------- | ------------- | ------ | ---------- | ----- | ------------ | ---------- | -------- | ------------ | ---------------- | --- |
| With this | authorization | vulnerability | in K’s | server, an | atack |              |            |          |              |                  |     |
enforcingthesecuritycheckswiththetokenandparticularuser,
caneasilygetthehashedpassword,andfurthercrackauser’spass-
word when provided with the victim’s email address. Recently, andneverassumingthataclientisalwaystrusted.
therearehugedatabreachesandlikelytheatackercantrivially EthicsandResponsibleDisclosure. WhendevelopingAuth-
inK’s
probe the victim’s email server. However, we also found Scopeforvulnerabilitydiscovery,wedotakeethicsinthehighest
when opening a seller’s page, her email address is embedded in standard.First,weonlytestedtheserviceswiththetwolegitimate
themetadata.herefore,anadversarycanalsocrawlalltheprod- usersweregistered(namelyAliceandBob),andweneverstealany
uctsinthisserviceandgetallseller’semail,andfurthergettheir
|     |     |     |     |     |     | other user’s | private information. |     | Second, we | never sent | a large |
| --- | --- | --- | --- | --- | --- | ------------ | -------------------- | --- | ---------- | ---------- | ------- |
hashedpassword.Consideringthatmostonlineuserstodayreuse
|     |     |     |     |     |     | volume of | traic to a | remote | service (to perform | any denial | of  |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------ | ------------------- | ---------- | --- |
theirpassword,suchanatackcancauseseriousdamagestomany serviceatack),andallthetraicisgeneratedatthespeedashow
onlineusers.
811

Session D2:  Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
anormaluserinteractswiththeremotesystem. Finally,wehave 9 CONCLUSION
maderesponsibledisclosureswhenwediscoveravulnerability.
Wehavepresentedthedesign,implementation,andevaluationof
Inparticular,wehaveimmediatelynotiiedthedevelopersbased AuthScope,atoolthatisabletoautomaticallyexecuteamobile
on the corresponding contact information on Google Play. As app,generatepost-authenticationmessages,andpinpointthevul-
aresult, someappdeveloperscontactedustodiscussthedetails nerableaccesscontrolimplementations,particularlythevulnera-
oftheirservervulnerabilitiesandwehaveworkedtogetherwith
bleauthorizations,ontheserverside.WehavetestedAuthScope
themtopatchthevulnerabilities. Forthoseappswhosevulnera- with4,838popularmobileappsfromGooglePlay,andidentiied
bilitieshavenotbeenixedyetatthetimeofthiswriting,wedo
597vulnerableauthorizationimplementationsin306mobileapps.
notrevealtheirconcreteappnamesandinsteadjustmaskedtheir heseareveryserioussecurityvulnerabilities,veryeasytoatack,
nameswithsymbol‘***’asshowninTable3. Wewillcontinueto andcancauseseveredamagestoenduserssuchaspersonalinfor-
provideourbestefortstohelpixtheirvulnerabilities. mationleakageandaccounthijacking.Wehavemaderesponsible
disclosuretoallofthevulnerableserviceproviders,andmanyof
8 RELATEDWORK
themhaveacknowledgedusandpatched(orstartedtopatch)their
|                                         |     |     |                 |     | vulnerabilities. | Finally,giventhecapabilityofsuchanautomated |     |     |     |
| --------------------------------------- | --- | --- | --------------- | --- | ---------------- | ------------------------------------------- | --- | --- | --- |
| VulnerabilityDiscoveryinOnlineServices. |     |     | Itischallenging |     |                  |                                             |     |     |     |
analysis,wewouldliketoraisetheawarenessofthevulnerableau-
| todevelopvulnerabilityfreesotware, |     | andmanyonlineservices |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
thorizationimplementationissuesinonlineservicesandhopethe
| contain various | vulnerabilities | ranging from | SQL injection | [21], |     |     |     |     |     |
| --------------- | --------------- | ------------ | ------------- | ----- | --- | --- | --- | --- | --- |
restvulnerableserviceproviderscouldpatchtheirservicesshortly.
cross-site-scripting[37],cross-site-forgery[11],tobrokenauthen-
tication [19], and even application logic vulnerabilities (e.g., [33, ACKNOWLEDGMENT
| 39,40,43]). | Correspondingly, | signiicantamountofefortshave |     |     |     |     |     |     |     |
| ----------- | ---------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Wewouldliketothanktheanonymousreviewersfortheirvery
beenfocusingonidentifyingthesevulnerabilitiesthrougheither
|           |                      |          |           |               | helpfulfeedbacks. | hisresearchwassupportedinpartbyAFOSR |     |     |     |
| --------- | -------------------- | -------- | --------- | ------------- | ----------------- | ------------------------------------ | --- | --- | --- |
| white-box | analysis with server | code, or | black-box | analysis with |                   |                                      |     |     |     |
justnetworktraic. under grants FA9550-14-1-0119 and FA9550-14-1-0173, and NSF
here are also eforts to particularly study the access control awards1453011and1516425.Anyopinions,indings,conclusions,
|           |                      |              |         |            | or recommendations | expressed | are those | of the authors | and not |
| --------- | -------------------- | ------------ | ------- | ---------- | ------------------ | --------- | --------- | -------------- | ------- |
| issues in | the online services. | Most of them | focused | on the au- |                    |           |           |                |         |
necessarilyoftheAFOSRandNSF.
thenticationrelatedproblems,suchassecuritywithsingle-signon
| (e.g., [38, | 45]), oauth (e.g., | [15, 36]), authentication |     | vulnerability |     |     |     |     |     |
| ----------- | ------------------ | ------------------------- | --- | ------------- | --- | --- | --- | --- | --- |
REFERENCES
| scanning | (e.g., [10]), and | password brute-force | atacks | with on- |     |     |     |     |     |
| -------- | ----------------- | -------------------- | ------ | -------- | --- | --- | --- | --- | --- |
lineservices(e.g.,[47]). Comparedtotheseworks,AuthScopeis [1] “Facebook app-speciic ids,” https://developers.facebook.com/docs/graph-api/
reference/user/.
amongtheirstfewtolookintothepost-authenticationissuesin
|     |     |     |     |     | [2] Hypertext | transfer protocol. https://www.w3.org/Protocols/rfc2616/rfc2616. |     |     |     |
| --- | --- | --- | --- | --- | ------------- | ---------------------------------------------------------------- | --- | --- | --- |
html.LastaccessedinMay2017.
onlineservicesandisabletoautomaticallydiscoverthevulnerable
[3] “Plaintextofenders,”lastaccessedinMay2017.
authorizationswhengivenmobileappsenabledwithsociallogin.
[4] “Robotium,”https://code.google.com/p/robotium/,lastaccessedinMay2017.
|                              |     |                       |     |     | [5] “Usingburpproxy,” | https://portswigger.net/burp/help/proxy_using.html, |     |     | last |
| ---------------------------- | --- | --------------------- | --- | --- | --------------------- | --------------------------------------------------- | --- | --- | ---- |
| DynamicAnalysisofMobileApps. |     | AuthScopeleveragesdy- |     |     |                       |                                                     |     |     |      |
accessedinMay2017.
namic analysis of Android apps to generate server request mes- [6] “Xposedmodulerepository,”http://repo.xposed.info/.
sages.Inthepastseveralyears,therearealargebodyofresearchin [7] “Ui/application exerciser monkey,” https://developer.android.com/tools/help/
monkey.html,2017.
dynamicanalysisofAndroidapps(e.g,.Monkey[7],Robotium[4],
[8] S.Anand,M.Naik,M.J.Harrold,andH.Yang,“Automatedconcolictesting
AppsPlayground [34], and DynoDroid [26]). Recently, there are ofsmartphoneapps,” inProceedingsoftheACMSIGSOFT20thInternational
|     |     |     |     |     | SymposiumontheFoundationsofSotwareEngineering,ser.FSE’12. |     |     |     | NewYork, |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | -------- |
alsoefortsofusingsymbolicexecution(e.g.,[8,29,42,46]formore
NY,USA:ACM,2012,pp.59:1–59:11.
systematicdynamicanalysisofmobileapps. [9] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein, Y. Le Traon,
Comparedtotheseworks,AuthScopeispartiallyinspiredby D.Octeau,andP.McDaniel,“Flowdroid: Precisecontext,low,ield,object-
sensitiveandlifecycle-awaretaintanalysisforandroidapps,”inProceedings
AppsPlaygroundandwehaveextendedittosupportmoreaccurate
ofthe35thACMSIGPLANConferenceonProgrammingLanguageDesignand
anddeeperUIelementexploration.Whilewecanalsoleveragethe
|     |     |     |     |     | Implementation,ser.PLDI’14. | NewYork,NY,USA:ACM,2014,pp.259–269. |     |     |     |
| --- | --- | --- | --- | --- | --------------------------- | ----------------------------------- | --- | --- | --- |
[10] G.Bai,J.Lei,G.Meng,S.S.Venkatraman,P.Saxena,J.Sun,Y.Liu,andJ.S.
symbolicexecutiontohavebetercoverage,werealizethatwemay
|     |     |     |     |     | Dong,“Authscan: | Automaticextractionofwebauthenticationprotocolsfrom |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --------------------------------------------------- | --- | --- | --- |
notneedsymbolicexecutionasidentifyingvulnerableauthoriza- implementations.”inNDSS,2013.
tion may not need large volume of request messages. Certainly, [11] A.Barth,C.Jackson,andJ.C.Mitchell,“Robustdefensesforcross-siterequest
forgery,”inProceedingsofthe15thACMconferenceonComputerandcommuni-
symbolicexecutionwillhelpthough.
|     |     |     |     |     | cationssecurity. | ACM,2008,pp.75–88. |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | ------------------ | --- | --- | --- |
AuthScope needs to reverse [12] E.Bauman,Y.Lu,andZ.Lin,“Halfacenturyofpractice: Whoisstillstoring
Protocol Reverse Engineering. plaintextpasswords?” inProceedingsofthe11thInternationalConferenceon
engineer the application protocol ields of interest and then per- InformationSecurityPracticeandExperience,Beijing,China,May2015.
|                                                         |     |     |     |      | [13] M. Beddoe, | “he protocol informatics | project,” | 2017, https://github.com/ |     |
| ------------------------------------------------------- | --- | --- | --- | ---- | --------------- | ------------------------ | --------- | ------------------------- | --- |
| formieldssubstitutiontoidentifysecurityvulnerabilities. |     |     |     | Over |                 |                          |           |                           |     |
wolever/Protocol-Informatics.
thepastdecade,therearesigniicantamountofefortsofanalyz- [14] J.CaballeroandD.Song,“Polyglot: Automaticextractionofprotocolformat
ingbothnetworkmessages(e.g.,[13,16,17,25])andinstructions using dynamic binary analysis,” in Proceedings of the 14th ACM Conference
traces (e.g., [14, 18, 22, 23, 28, 41]) to discover protocol formats onComputerandandCommunicationsSecurity(CCS’07),Alexandria,Virginia,
USA,2007,pp.317–329.
andusethemforsecurityapplications.AuthScopeisparticularly
[15] E.Y.Chen,Y.Pei,S.Chen,Y.Tian,R.Kotcher,andP.Tague,“Oauthdemystiied
|     |     |     |     |     | for mobile | application developers,” | in Proceedings | of the 2014 | ACM SIGSAC |
| --- | --- | --- | --- | --- | ---------- | ------------------------ | -------------- | ----------- | ---------- |
inspiredbytheprotocolinformaticsproject[13],andusesacus-
|                                                      |     |     |     |     | ConferenceonComputerandCommunicationsSecurity. |     |     | ACM,2014,pp.892– |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | ---------------- | --- |
| tomizedNeedleman-Wunschalgorithm[30]toalignanddifthe |     |     |     |     | 903.                                           |     |     |                  |     |
protocolmessagesandinferonlytheieldsofourinterest. [16] A.Continella,Y.Fratantonio,M.Lindorfer,A.Pucceti,A.Zand,C.Kruegel,and
G.Vigna,“Obfuscation-resilientprivacyleakdetectionformobileappsthrough
812

Session D2: Vulnerable Mobile Apps CCS’17, October 30-November 3, 2017, Dallas, TX, USA
diferentialanalysis,”inProceedingsoftheISOCNetworkandDistributedSystem pp.1–41,2013.
SecuritySymposium(NDSS),2017,pp.1–16. [32] E.I.Organick,hemulticssystem:anexaminationofitsstructure. MITpress,
[17] W.Cui,J.Kannan,andH.J.Wang,“Discoverer: Automaticprotocolreverse 1972.
engineeringfromnetworktraces,”inProceedingsofthe16thUSENIXSecurity [33] G.PellegrinoandD.Balzaroti,“Towardblack-boxdetectionoflogiclawsin
Symposium(Security’07),Boston,MA,August2007. webapplications.”inNDSS,2014.
[18] W.Cui,M.Peinado,K.Chen,H.J.Wang,andL.Irun-Briz,“Tupni:Automatic [34] V. Rastogi, Y. Chen, and W. Enck, “AppsPlayground: Automatic Security
reverseengineeringofinputformats,”inProceedingsofthe15thACMConference AnalysisofSmartphoneApplications,”inhirdACMConferenceonDataand
onComputerandCommunicationsSecurity(CCS’08),Alexandria,Virginia,USA, ApplicationSecurityandPrivacy,2013.
October2008,pp.391–402. [35] D.Sounthiraraj, J. Sahs, G. Greenwood, Z. Lin, and L. Khan, “Smv-hunter:
[19] M.Dalton,C.Kozyrakis,andN.Zeldovich,“Nemesis: Preventingauthentica- Largescale,automateddetectionofssl/tlsman-in-the-middlevulnerabilitiesin
tion&accesscontrolvulnerabilitiesinwebapplications.”inUSENIXSecurity androidapps,”inProceedingsofthe21stAnnualNetworkandDistributedSystem
Symposium,2009,pp.267–282. SecuritySymposium(NDSS’14),SanDiego,CA,February2014.
[20] J.Franks,P.Hallam-Baker,J.Hostetler,S.Lawrence,P.Leach,A.Luotonen,and [36] S.-T.SunandK.Beznosov,“hedevilisinthe(implementation)details: an
L.Stewart,“Htpauthentication:Basicanddigestaccessauthentication,”Tech. empirical analysis of oauth sso systems,” in Proceedings of the 2012 ACM
Rep.,1999. conferenceonComputerandcommunicationssecurity. ACM,2012,pp.378–390.
[21] W.G.Halfond,J.Viegas,andA.Orso,“Aclassiicationofsql-injectionatacks [37] P.Vogt,F.Nentwich,N.Jovanovic,E.Kirda,C.Kruegel,andG.Vigna,“Crosssite
andcountermeasures,”inProceedingsoftheIEEEInternationalSymposiumon scriptingpreventionwithdynamicdatataintingandstaticanalysis.”inNDSS,
SecureSotwareEngineering,vol.1. IEEE,2006,pp.13–15. vol.2007,2007,p.12.
[22] Z.Lin, X.Jiang, D.Xu, andX.Zhang, “Automaticprotocolformatreverse [38] R.Wang, S.Chen, andX.Wang, “Signingmeontoyouraccountsthrough
engineeringthroughcontext-awaremonitoredexecution,”inProceedingsofthe facebookandgoogle:Atraic-guidedsecuritystudyofcommerciallydeployed
15thAnnualNetworkandDistributedSystemSecuritySymposium(NDSS’08),San single-sign-onwebservices,”inSecurityandPrivacy(SP),2012IEEESymposium
Diego,CA,February2008. on. IEEE,2012,pp.365–379.
[23] Z.LinandX.Zhang,“Derivinginputsyntacticstructurefromexecution,”in [39] R.Wang,S.Chen,X.Wang,andS.Qadeer,“Howtoshopforfreeonline–security
Proceedingsofthe16thACMSIGSOFTInternationalSymposiumonFoundations analysisofcashier-as-a-servicebasedwebstores,”inSecurityandPrivacy(SP),
ofSotwareEngineering(FSE’08),Atlanta,GA,USA,November2008. 2011IEEESymposiumon. IEEE,2011,pp.465–480.
[24] L.Lu,Z.Li,Z.Wu,W.Lee,andG.Jiang,“Chex: staticallyvetingandroid [40] R.Wang,Y.Zhou,S.Chen,S.Qadeer,D.Evans,andY.Gurevich,“Explicating
appsforcomponenthijackingvulnerabilities,”inProceedingsofthe2012ACM sdks:Uncoveringassumptionsunderlyingsecureauthenticationandauthoriza-
conferenceonComputerandcommunicationssecurity. ACM,2012,pp.229–240. tion.”inUSENIXSecurity,vol.13,2013.
[25] J.Ma,K.Levchenko,C.Kreibich,S.Savage,andG.M.Voelker,“Unexpected [41] G.Wondracek,P.Milani,C.Kruegel,andE.Kirda,“Automaticnetworkprotocol
means of protocol inference,” in Proceedings of the 6th ACM SIGCOMM on analysis,” inProceedingsofthe15thAnnualNetworkandDistributedSystem
Internetmeasurement(IMC’06). RiodeJaneriro,Brazil:ACMPress,2006,pp. SecuritySymposium(NDSS’08),SanDiego,CA,February2008.
313–326. [42] M.Y.WongandD.Lie,“Intellidroid:Atargetedinputgeneratorforthedynamic
[26] A.Machiry,R.Tahiliani,andM.Naik,“Dynodroid:Aninputgenerationsystem analysisofandroidmalware,”inProceedingsofthe21stAnnualNetworkand
forandroidapps,”inProceedingsofthe20139thJointMeetingonFoundationsof DistributedSystemSecuritySymposium(NDSS’16), SanDiego, CA,February
SotwareEngineering. ACM,2013,pp.224–234. 2016.
[27] A.Memon,I.Banerjee,andA.Nagarajan,“Guiripping: Reverseengineering [43] L. Xing, Y. Chen, X. Wang, and S. Chen, “Integuard: Toward automatic
ofgraphicaluserinterfacesfor testing,” inProceedings ofthe10thWorking protectionofthird-partywebserviceintegrations.”inNDSS,2013.
ConferenceonReverseEngineering,ser.WCRE’03. Washington,DC,USA:IEEE [44] L.Xing,X.Pan,R.Wang,K.Yuan,andX.Wang,“Upgradingyourandroid,
ComputerSociety,2003,pp.260–. elevatingmymalware: Privilegeescalationthroughmobileosupdating,”in
[28] P. Milani Compareti, G. Wondracek, C. Kruegel, and E. Kirda, “Prospex: Proceedingsofthe2014IEEESymposiumonSecurityandPrivacy,ser.SP’14.
ProtocolSpeciicationExtraction,”inIEEESymposiumonSecurity&Privacy, Washington,DC,USA:IEEEComputerSociety,2014,pp.393–408.
Oakland,CA,2009,pp.110–125. [45] Y.ZhouandD.Evans,“Ssoscan: Automatedtestingofwebapplicationsfor
[29] N.Mirzaei,S.Malek,C.S.Păsăreanu,N.Esfahani,andR.Mahmood,“Testing singlesign-onvulnerabilities.”inUSENIXSecurity,2014,pp.495–510.
androidappsthroughsymbolicexecution,”ACMSIGSOFTSotwareEngineering [46] C.ZuoandZ.Lin,“Exposingserverurlsofmobileappswithselectivesymbolic
Notes,vol.37,no.6,pp.1–5,2012. execution,”inProceedingsofthe26thWorldWideWebConference,Perth,Aus-
[30] S.B.NeedlemanandC.D.Wunsch,“Ageneralmethodapplicabletothesearch tralia,April2017.
forsimilaritiesintheaminoacidsequenceoftwoproteins,”Journalofmolecular [47] C.Zuo,W.Wang,R.Wang,andZ.Lin,“Automaticforgeryofcryptographically
biology,vol.48,no.3,pp.443–453,1970. consistent messages to identify security vulnerabilities in mobile services,”
[31] B.Nguyen,B.Robbins,I.Banerjee,andA.Memon,“Guitar:aninnovativetool in Proceedings of the 21st Annual Network and Distributed System Security
forautomatedtestingofgui-drivensotware,”AutomatedSotwareEngineering, Symposium(NDSS’16),SanDiego,CA,February2016.
813