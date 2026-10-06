> 원본: BolaZ_2507.02309.pdf; 변환: markitdown; 2026-10-06

<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrust
Principle
ANBINWUandZHIYONGFENG,
TheCollegeofIntelligenceandComputing,TianjinUniversity,CHINA
RUITAOFENG∗,
SouthernCrossUniversity,Australia
ZHENCHANGXING,
CSIRO’sData61,Australia
YANGLIU,
SchoolofComputerScienceandEngineering,NanyangTechnologicalUniversity,Singapore
RESTfulAPIsfacilitatedataexchangebetweenapplications,buttheyalsoexposesensitiveresourcestopotentialexploitation.Broken
ObjectLevelAuthorization(BOLA)isthetopvulnerabilityintheOWASPAPISecurityTop10,exemplifiesacriticalaccesscontrolflaw
whereattackersmanipulateAPIparameterstogainunauthorizedaccess.Toaddressthis,weproposeBolaZ,adefenseframework
groundedinzerotrustprinciples.BolaZanalyzesthedataflowofresourceIDs,pinpointingBOLAattackinjectionpointsand
determiningtheassociatedauthorizationintervalstopreventhorizontalprivilegeescalation.Ourapproachleveragesstatictaint
trackingtocategorizeAPIsintoproducersandconsumersbasedonhowtheyhandleresourceIDs.Bymappingthepropagationpaths
ofresourceIDs,BolaZcapturesthecontextinwhichtheseIDsareproducedandconsumed,allowingforpreciseidentificationof
authorizationboundaries.Unlikedefensemethodsbasedoncommonauthorizationmodels,BolaZisthefirstauthorization-guided
methodthatadaptsdefenserulesbasedonthesystem’sbest-practiceauthorizationlogic.WevalidateBolaZthroughempirical
researchon10GitHubprojects.TheresultsdemonstrateBolaZ’seffectivenessindefendingagainstvulnerabilitiescollectedfromCVE
anddiscovering35newBOLAvulnerabilitiesinthewild,demonstratingitspracticalityinreal-worlddeployments.
CCSConcepts:•Securityandprivacy→Webapplicationsecurity.
AdditionalKeyWordsandPhrases:APIsecurity,BOLAattack,RESTfulAPIs,Accesscontrol.
ACMReferenceFormat:
AnbinWu,ZhiyongFeng,RuitaoFeng,ZhenchangXing,andYangLiu.2025.RethinkingBrokenObjectLevelAuthorizationAttacks
UnderZeroTrustPrinciple.InProceedingsofACMTransactionsonSoftwareEngineeringandMethodology.ACM,NewYork,NY,USA,
27pages.https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
RESTfulAPIshavebecomethestandardforaccessingweb-orientedresources,enablinguserstoinitiateoperational
requeststhroughHTTPmethods,paths,andparameters.However,theparametersofRESTfulAPIsareuser-controlled,
hence,inherentlyuntrusted.AttackerscanexploitthisbytamperingwiththeresourceIDparametertoaccesssensitive
dataofotheruserswithoutauthorization,leadingtoaBrokenObjectLevelAuthorization(BOLA)attack[19].
ResourceIDistheuniqueidentifierofresourcesinRESTAPIthatareusedtooperate(INSERT,DELETE,UPDATE,READ)
∗Correspondingauthor
Authors’ContactInformation:AnbinWu,wuanbin@tju.edu.cn;ZhiyongFeng,zyfeng@tju.edu.cn,TheCollegeofIntelligenceandComputing,Tianjin
University,CHINA;RuitaoFeng,SouthernCrossUniversity,Australia,ruitao.feng@scu.edu.au;ZhenchangXing,CSIRO’sData61,Australia,zhenchang.
xing@anu.edu.au;YangLiu,SchoolofComputerScienceandEngineering,NanyangTechnologicalUniversity,Singapore,yangliu@ntu.edu.sg.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesarenot
madeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitationonthefirstpage.Copyrightsforcomponents
ofthisworkownedbyothersthantheauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,toposton
serversortoredistributetolists,requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ManuscriptsubmittedtoACM
ManuscriptsubmittedtoACM 1
5202
luJ
51
]RC.sc[
2v90320.7052:viXra

2 AnbinWuetal.
resources,thatis,BOLAattackinjectionpoint.Thevulnerabilityarisesfromover-relianceontheuser-supplied
resourceID,withoutenforcingproperaccesscontrolmechanisms.
TheBOLAvulnerabilityisanaccesscontrolvulnerability,anddevelopersneedtoperformsomesecuritychecks
beforeusersoperatesensitiveinformationtodefendagainstthevulnerability.BOLAvulnerabilitiesarederivedfromthe
lackofobject-levelauthorizationchecking[18].ToaccuratelydetectBOLAvulnerabilities,itisnecessarytounderstand
theaccesscontrolpolicyofresources.Throughthestudyoftheexistingwork,therearetwomainwaystoobtainaccess
controlpolicies.1).Manuallyprovideauthorizationpoliciesrules[14],[31],[5].Thismethodreliesonmanuallylabeling
authorizationrulesforeachresourceoperation,whichistediousandpronetoerrors[17].2).Deducetheauthorization
modelofresourcesthroughsourcecode[37],[29],[18],[32].Thistypeofmethodfirstartificiallysummarizesthe
application’sresourceauthorizationmodel,andinferswhichauthorizationmodeltheresourcebelongstobyanalyzing
thesourcecode.However,thistypeofmethodisbasedontheauthorizationmodelofhumansummary.Whenthe
systemauthorizationmodelisinconsistentwiththeauthorizationmodelofhumansummary,itwillleadtofalse
positives.Theauthorizationmodel’sstaticnatureandtheunknownsystemlogic’sdynamicnaturearecontradictory.
Fig.1. BOLARAYauthorizationmodel
BOLARAY(CCS’24,Oct)[18]isthestate-of-the-art(SOTA)methodfordetectingBOLAattacks.Byanalyzingreal-
worldBOLAvulnerabilitiesinopen-sourceapplications,BOLARAYidentifiesfourcommonobject-levelauthorization
models.However,thesemodels,beingmanuallysummarized,lackadaptabilitytothediverseandevolvingnatureof
modernwebapplications.AsillustratedinFig.1,BOLARAYclassifiestheArticletableundertheownershipmodel,
whereanarticlecanonlybeupdatedordeletedbyitsowner.ThismodelfailstosupportSELECToperations.For
instance,API5inFig.1involvesanUPDATEstatementthatallowsuserstoaddlikestoarticles.However,BOLARAY
incorrectlyassumesthatarticlescanonlybeupdatedbytheirowners.Thisrigidinterpretationoverlookstheactual
propagationpatternsofresourceidentifiersinwebapplications[1],leadingtosemanticmismatches.Asaresult,such
out-of-contextauthorizationlogiclimitsBOLARAY’sabilitytocomprehensivelydetectBOLAvulnerabilities.
WerevisittheessenceofBOLAattacks—horizontalprivilegeescalationandreconceptualizetheirdefenseasa
problemofminimallyscopedauthorization.Specifically,defendingagainstBOLAattacksinvolvesisolatingtheinjection
point(i.e.,theresourceID)withinthenarrowestpermissionboundarythatalignswiththeapplication’slogic.The
resourceIDparameterfunctionsduallyasanattacksurfacevulnerabletohorizontalprivilegeescalation[36],andasa
protectionsurfaceresponsibleforenforcingleastprivilegeaccesscontrol[7].Effectivemitigationrequiresaccurately
determiningtheauthorizationintervalforeachresourceID,ensuringuserscanonlyaccessormanipulateresources
withintheirminimumnecessarypermissions[20].
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 3
ZeroTrust,groundedintheprincipleof“nevertrust,alwaysverify"[35],emphasizesfine-grained,identity-based
accesscontroltomitigaterisksassociatedwithunauthorizedlateralmovement.Micro-segmentation(MSG),acrucial
componentofzerotrust,createsasecurityclosed-loopbyconsideringmultiplefactors—suchasuserroles,processes,
andaccesscontexts—todefinetheminimalsecurityboundaryforresourceIDsbasedonAPIcontextdataflow.Thisnot
onlyalignswiththeAPI’sauthorizationlogicbutalsoenforcestheprincipleofminimumpermissions,makingMSGan
effectivestrategyfordefendingagainstBOLAattacks.
ThispaperintroducesBolaZ1,anovelframeworkdesignedtodefendagainstBOLAattacksfromtwoperspectives:
attacksurfacediscoveryandprotectionsurfaceauthorization.BolaZleveragesanattacker’sviewpointtoanalyzeBOLA
attackdataflows,accuratelyidentifyingtheBOLAattackinjectionpoints.BolaZtakesadvantageofthecontext
relationshipbetweenAPIparametersandresourceIDtocompensatefortheshortcomingsofidentifyinginjection
pointsbasedonfixedauthorizationmodels.Additionally,BolaZdividesresourcesintosmallerlogicalintervalsbased
onresourceIDworkflows,isolatingtheprotectionsurfacetotheminimalauthorizationintervalsdefinedbythe
system’sauthorizationlogic.Thisapproachenableseffectiveresourceisolationacrossdifferentusersandbusiness
processes,overcomingthelimitationsofstaticauthorizationmodels.
Throughempiricalresearchon10GitHubprojectsverifiedtocontainRESTfulAPIusage,wefirstquantitatively
evaluateBolaZ’seffectivenessbyassessingtheprecisionandrecallofattackinjectionpointidentification,authorization
intervaldetermination,andperformanceoverhead.Ourexperimentalselectioncriteria—GitHubstars,applicationtype,
andlogiccontroltype(detailedinSection3.4.2)—ensureacomprehensivecoverageofvariousapplicationscenarios.
Next,wecollectrelevantvulnerabilitiesfromtheCommonVulnerabilitiesandExposures(CVE)DBbasedonthree
BOLAattackmodes(detailedinSection3.1)todemonstrateBolaZ’scapabilityindetectingthesevulnerabilities.Finally,
weapplyBolaZtoscanforpotentialBOLAvulnerabilitiesin10projects,evaluatingitinreal-worldscenariosto
confirmitspracticality.
Tothebestofourknowledge,thisisthefirstworktoapplyMicro-segmentation(MSG),whichisderivedfrom
zerotrustprinciples,tothediscoveryofattacksurfacesandtherefinementofdata-levelpermissionsinRESTfulAPIs.
Amongthe94RESTfulAPIsanalyzedintheselectedGitHubprojects,BolaZachievedrecallratesof97%forattack
injectionpointsand87%forauthorizationintervals,withonlyonefalsepositive.Theexperimentalresultsarepromising;
BolaZsuccessfullydefendedagainstknownBOLAvulnerabilitiesinourbenchmarkandidentified35newBOLA
vulnerabilitiesin10real-worldprojects.
Thispapermakesthefollowingcontributions:
• WeproposeanovelapproachforidentifyingBOLAattackinjectionpointsbytrackingthedataflowof
resourceIDs.ThismethodenhancesdetectionbyanalyzinghowresourceIDsareusedthroughoutthesystem.
• Ourworkisthefirsttoapplystatictainttrackingtechnologytoinferauthorizationintervals(MSGintervals)
forBOLAattackinjectionpoints.Thistechniqueimprovesthegranularityofaccesscontrolbydefiningminimum
securityboundariesbasedondataflow.
• Weintroduceamethodtoisolateattackinjectionpointstothesystem’sminimumsecurityboundary,
leveragingtheresourceIDpropagationmode.BolaZisthefirstauthorization-guidedmethodthatadapts
defenserulesbasedonthesystem’sbest-practiceauthorizationlogic.
Therestofthispaperisorganizedasfollows.Section2introducesbackgroundknowledgeonRESTfulAPIs,BOLA
attacksandMicro-Segmentation(MSG).Section3demonstrateshowtheproblemofBOLAvulnerabilitydetection
1Codeavailability:https://anonymous.4open.science/r/bolaz-96AC
ManuscriptsubmittedtoACM

4 AnbinWuetal.
isformulatedatthemethodologicallevel.InSection4,thetechnicaldetailsoftheproposednovelapproach,BolaZ,
aredescribed.Section5showsthedetailsoftheimplementation.Section6describestheexperimentsanddiscusses
theresults.Section7providesdiscussionandfuturework.RelevantliteratureissummarizedinSection8.Section9
concludesthiswork.
2 Background
2.1 RESTfulAPIs
RESTfulAPIsareAPIsthatfollowthestyleofRESTarchitecture[16].RESTfulAPIsprovideaunifiedinterfacefor
creating(C),reading(R),updating(U),anddeleting(D)resources[10].RESTfulAPIsarearesource-orientedarchitecture.
UserscanidentifyresourcesthroughtheURIandcorrespondtotheCRUDoperationoftheresourcethroughPOST,
GET,UPDATE,DELETEandPATCH.
2.2 BOLAAttack
BOLAisthenumberonevulnerabilityinOWASPAPISecurity[34].Let’stakeaconcreteexampletoexplainwhat
theBOLAattackis.AsshowninFig.2a,usersusingorderdetailsAPI(GET/api/order/{orderid})canonlyreadorder
resourcesthattheyhavecreated.Normalusers(userA,userB)accesstheorderresourceusingtheirowncreatedorderid
(733,845).Still,theattackerinitiatesaccesstouserB’sorderresourcesbymodifyingtheorderid(resourceID)parameter,
whichistheinjectionpointoftheBOLAattack.IfthedeveloperdoesnotperformaneffectiveresourceIDpermission
checkontheAPI,attackerscangainunauthorizedaccesstootherusers’sensitiveresources.TheBOLAvulnerability
opensthedoorforattackerstodirectlyaccessresources,allowingthemtobypassintendedapplicationworkflows
andgainunauthorizedaccesstosensitivedata.
2.3 Micro-Segmentation(MSG)
MSG[23]followsthecoreprinciplesofzerotrust-minimumpermissions,allusersareuntrusted,anduseraccesstoany
resourceneedstobeauthenticated.MSGdividesresourcesintoseveralsmallresourceintervalsbasedonservicelogicin
asoftware-definedway,logicallyseparatingresourcesandrestrictingthemovementofuserswithinresources,enabling
themostfine-grainedaccesscontrolofresources.AsshowninFig.2b,accordingtothesystemlogic,MSGdividesthe
entireorderresourceintosmallpartitionsaccordingtouseridentity.MSGpoliciesallowuserstoaccessonlytheorderid
createdbythemselves,andpreventstheattacker’shorizontalunauthorizedaccesstootherusers’orderresources.
(a)BOLAAttack (b)MSG
Fig.2. ABOLAattackonanorderdetailsAPIanditspreventionbyMicro-Segmentation(MSG)
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 5
3 ProblemFormulation
3.1 ThreatModel
3.1.1 Attacker’sCapability. ToeffectivelyexecuteaBrokenObjectLevelAuthorization(BOLA)attack,attackersmust
obtainresourceIDstheyarenotauthorizedtoaccess.TheseIDscanbeexposedthroughseveralAPIvulnerabilities,as
showninFig.3.TheprimaryvulnerabilitiesleadingtoBOLAattacksareBrokenObjectPropertyLevelAuthorization
(BOPLA),UnrestrictedAccesstoSensitiveBusinessFlows(UASBF),andBrokenFunctionLevelAuthorization(BFLA)
[34].
Fig.3. System,user,andattackerworkflows
3.1.2 VulnerabilityTechniques.
- BOPLA,ranked3rdintheOWASPAPISecurityTop10,occurswhenAPIsunintentionallyexposesensitiveresource
IDsintheirresponses.AttackersexploitthisexposurebyextractingtheseIDsfromtheAPIresponsesandusingthem
togainunauthorizedaccesstoresources.
- UASBF,ranked4th,allowsattackerstobypassrestrictionsandaccessAPIswithoutproperauthentication.When
resourceIDsarepredictableorsequential,attackerscanuseautomatedscriptstoenumeratetheseIDs,leadingto
potentialBOLAattacksastheygainunauthorizedaccesstovariousresources.
- BFLA,listed5th,allowsattackerstoaccessAPIswithelevatedpermissionswithoutproperauthorizationchecks.If
anAPIfailstoenforceauthorizationcontrols,attackersmayexploitthistoretrievesensitiveresourceIDsbelonging
tootherusers.
3.2 Terminology
WeclassifyAPIsaccordingtotheproductionandconsumptionofresourceIDs,asshowninFig.4.
- ProducerAPI(P-API).P-APIscanreturntheresourceID.
- ConsumerAPI(C-API).C-APIsconsumetheresourceIDthroughparameters.
- FalseProducerAPI(FP-API).FP-APIsconsumeandreturnthesameresourceID,whichisessentiallyC-API.
- ProducerandconsumerAPI(PC-API).PC-APIsconsumesomeresourceIDsandproduceothertypesofresource
IDs.
ManuscriptsubmittedtoACM

6 AnbinWuetal.
- Non-producerandnon-consumerAPI(NPC-API).NPC-APIsneitherproducenorconsumeresourceIDs.
Fig.4. ClassificationofAPIsbasedonridproductionandconsumption
3.3 ProblemDefinition
DefendingagainstBOLAattacksfundamentallyinvolvesconfiningtheresourceIDaccessedbyattackerswithinthe
smallestnecessarypermissionscope.AsillustratedinFig.3,theresourceID(attackinjectionpoint)isnotarbitrarily
providedbytheuser;itisgeneratedupstreaminthesystemworkflowandthenpropagateddownstream.Thenthe
resourceIDgeneratedupstreamofthedatastreamistheaccessibleintervaloftheresourceIDofthedownstream
consumerAPI.Consequently,fromtheperspectiveoftheresourceID’sdataflow,theproblemofdefendingagainst
BOLAattackscanbedecomposedintothreesub-problems.
Problem1:P-APIidentificationanddiscoveryofresourceIDgenerationrules.TheP-APIislocatedupstream
intheresourceIDdatastream,whichgeneratesasetofresourceIDsaccordingtothesystem’slogicalconstraints.
Therefore,thefirstsub-problemistoidentifytheP-APIandextracttherulesgoverningresourceIDgeneration.
Formulation:GivenanAPI𝑃,determinewhetheritproducestheresourceID𝑟𝑖𝑑andthelogicrules𝑅ofcreatingthe
resourceID.
𝑃 ∈𝐴𝑃𝐼,𝑅𝑢𝑙𝑒 ={𝑅 1 ,...,𝑅 𝑛},𝑅 𝑖 ={𝑟𝑖𝑑 1 ,...𝑟𝑖𝑑 𝑛} (1)
Problem2:C-APIidentificationanddiscoveryofBOLAattackinjectionpoints.TheC-APIisdownstreaminthe
resourceIDdatastream,utilizingtheresourceIDpropagatedbytheP-APItoperformresourceoperations.Therefore,
thesecondsub-problemistoidentifytheC-APIandfindtheBOLAattackinjectionpointsintheC-API.
Formulation:GivenanAPI𝐶,determinewhetheritconsumestheresourceID𝑟𝑖𝑑andwhichparameters𝑝𝑎𝑟𝑚are
associatedwiththeresourceID.
𝐶 ∈𝐴𝑃𝐼,𝑝𝑎𝑟𝑚 𝑖 ∈𝐶,𝐶 𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛 ={(𝑝𝑎𝑟𝑚 𝑖 ,𝑟𝑖𝑑 𝑖)} (2)
Problem3:DataflowassociationbetweenP-APIandC-API.P-APIandC-APIserveastheresourceIDdata
flow’sstartingandendingnodes.AnalyzingthedataflowrelationshipbetweenP-APIandC-APIcandeterminethe
authorizationintervaloftheBOLAattackinjectionpoints.
Formulation:GivenaP-API,P,andaC-API,C,determinewhetherthereisadataflowcontextbetweenPandC.
𝑃 ∈𝑃−𝐴𝑃𝐼,𝐶 ∈𝐶−𝐴𝑃𝐼,𝐴𝑃𝐼 𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛 =(𝑃,𝐶) (3)
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 7
3.4 ProblemScope
TherearemanywaystostoreandextractresourcesinRESTfulAPIs.Wedefinetheproblemscopetoreducethe
divergenceoftheresearchprocessandproposeanextensiblemethodbasedonthis.
3.4.1 ResourceStorageBasedonDatabase. TherearemanyformsofresourcestorageinRESTfulAPIs,suchasdatabases,
Hadoop,andSpark.Thedatabaseisthemaincarrierforresourcestorage.Therefore,BolaZconsidersthedatabaseasa
resourcestoragecarrierforBOLAattackdetection,thesameasBOLARAY[18].
3.4.2 MSG Intervals = SELECT Statements. BolaZ uses the database as the resource storage carrier, so SELECT
statementsarethecorewayforP-APItoobtainresourceIDs,andSELECTstatementssupportmostofthedatafiltering
functions.Server-sidecodesrarelyfilterresourceIDsreceivedbySELECTstatements.Therefore,BolaZusesSELECT
statementsofP-APIsasMSGintervalsofresourceIDs.TheprimaryandforeignkeysobtainedbySELECTstatements
areresourceIDs.
MSGintervalsarenotonlydeterminedbySELECTstatementsbecausetherearetwowaysforuserstodeleteand
updateresources:1).Serverlogiccontrol.P-APIsgenerateresourcesthatusershavepermissiontodeleteandmodify,
anduserscandeleteandmodifyallresourcesreturnedbyP-APIsontheclient.2).Clientlogiccontrol.P-APIsreturn
allresourcestoclients,andfront-endcodesdeterminewhethercurrentusershavepermissiontousetheresourceIDto
deleteormodifytheresource.
3.4.3 PropagationinvarianceofresourceIDs. Byanalyzingnearlyahundredopensourceprojects,wefindthatthe
resourceID,astheuniqueidentifieroftheresource,hasassignmentandreplicationoperationsduringthepropagation
process,andtherearefewmodificationanddeletionoperations(onlyonecaseisfoundinnearly1,000APIs).Resource
IDsremaininvariantovertheentiredatastreamofproduction,propagationandconsumption.Moreover,inAPI
automatedtesting,theresourceIDisalsoregardedasimmutable,e.g.,RestTestGenandRESTler.
4 Approach
Inthissection,wegiveanoverviewoftheBolaZframeworkandproposethreemodulestosolveourthreesub-problems
asdescribedinFig.5.
4.1 Overview
(a)P-APIidentificationandMSGintervalgeneration.○1 BolaZanalyzeswhichSELECTstatementsgenerate
resourceIDs(primaryandforeignkeys)fromserver-sidesourcecode.○2 ResourceIDsgeneratedbySELECTstatements
arepropagatedintheMapperlayer(databaseprocessinglayer)andtheServicelayer(applicationlogicprocessing
layer).○3 ResourceIDsarepropagatedtothereturnvalueoftheAPI.BolaZdeterminesiftheAPIisP-API.○4 BolaZ
analyzesthedependenciesbetweenP-APIparametersandSELECTstatements,explorestheparent-childrelationship
betweenSELECTstatements,andgeneratesMSGintervalsofresourceID.
(b)C-APIidentificationandBOLAattackinjectionpointdiscovery.○1 BolaZtracksthedataflowofAPIparameters
intheserversourcecode.○2 APIparametersarepropagatedattheServiceandMapperlayers.○3 BolaZonlyretainsthe
APIparameterdataflowpropagatingtotheSQLstatement’sprimaryorforeignkey(resourceID).○4 BolaZusesthe
mappingrelationshipbetweenAPIparametersandprimaryandforeignkeystoidentifyC-APIandfindstheinjection
pointoftheBOLAattack.
ManuscriptsubmittedtoACM

8 AnbinWuetal.
Fig.5. TheoverviewofBolaZ
(c)P-APIandC-APIdataflowassociation.○1 BolaZexploresdataflowsofresourceIDsinfront-endcodefrom
P-APItoC-APIandinnovativelyobtainstherelationshipbetweenP-APIandC-API.○2 MSGintervalsofmultipleP-APIs
provideMSGintervalsforattackinjectionpointsofC-APIsandgeneratetheMSGintervalset.○3 BolaZimprovesthe
performanceofresourceIDauthorizationcheckingbyoptimizingtheMSGintervalset.
4.2 P-APIIdentificationandMSGIntervalGeneration
TheP-APIistheupstreamoftheresourceIDpropagationandgeneratestheresourceID’sMSGinterval.Therefore,
BolaZ’sfirststepistoidentifytheP-APIandgettheMSGintervaloftheresourceID.
BolaZarguesthatSELECTstatementsrepresentMSGintervals.AsshowninFig.6,thethreeSELECTstatements
produceMSGintervalsfortheresourceID(blog_id)ofblog,respectively.TheMSGintervalacontainstheblog_idcreated
byuserAhimself.TheMSGintervalbcontainstheblog_idcreatedbyuserbhimself.TheMSGintervalccontainsall
blog_id.ThefalseMSGintervalonlyreadstheamountofdataintheblogtableanddoesnotgenerateresourceID.
4.2.1 P-APIIdentification. Usually,theGETtypeAPIreturnstheresourceID[48].BolaZtakestheGETtypeAPIas
thestartingpointandusesthetainttrackingtechnologytoobtainSELECTstatementsassociatedwiththereturnvalue
intheAPI.
AsshowninFig.8a,BOLAZtracksthepropagationoftokensintheAPIlayerandSQLlayer,andobtainstheSELECT
statementsassociatedwiththeAPIreturnvalue.ByanalyzingtheAbstractsyntaxtree(AST)oftheSELECTstatement,
BolaZdeterminesthattheSELECTstatementobtainstheprimarykeyidoftheblogtable.Onlywhentheassociated
SELECTstatementobtainstheresourceIDcolumnsofthetable,BolaZdeterminestheAPIasP-API.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 9
Fig.6. MSGintervals
Fig.7. FP-APIIdentification.SQL-(a)producesthesameblogIDastheAPIparameter,notcreatinganewblogID.BolaZconsiders
theAPIforcreatingandconsumingthesameresourceIDasaP-API,notanFP-API.
4.2.2 MSGIntervalGeneration. OncetheP-APIisidentified,theSELECTstatementsassociatedwiththeP-APIreturn
valuearetheMSGintervals.MSGintervalsmustmaintainintegritytoisolateresourceIDstothemaximumauthorization
range.Additionally,sinceMSGintervalsgeneratedbyP-APIsmayhavedependencyconditions,BolaZextractsthese
dependenciestoensuretheaccuracyoftheauthorizationrange.
Listing1ReductionofMSGintervals
1: Select a_id,addr from address where user_id="uid" and detail="userinput"
limit start,stop
2: Select a_id,addr from address where user_id="uid"
IntegrityoftheMSGinterval.SELECTstatementsrepresentMSGintervals.Still,theremaybesomeconditionsin
SELECTstatementstoreducetherangeofMSGintervals.AsshowninListing1(1),theSQLstatementobtainstheuser’s
address.“Detail"conditioncorrespondstothekeywordsearchfunctionoftheaddress,andtheusercanmakethedetail
conditioncovertheentiretablewithoutenteringthekeyword.“Limit"correspondstotheaddresspagingfunction,and
userscanalsoobtainalldatathroughthepageturningfunction.ConditionsofthistypewillreduceMSGintervals.
User_idistheforeignkeyoftheaddr table,whichisanecessaryconditiontodetermineMSGintervals.Therefore,
BolaZpreservesonlytheforeignkeyandnon-userinputconditionsinSELECTstatements,asshowninListing1(2).
DependenceoftheMSGinterval.ThecompleteMSGintervalpreservestheconditionsofforeignkeys,butthese
conditionsarenotnecessarilyindependent.BolaZobtainsthedependencyconditionsofforeignkeysfromexternal
inputs(APIparametersandtokens)andinternalassociations(parentresourceIDs)ofAPI.
ManuscriptsubmittedtoACM

10 AnbinWuetal.
(a)P-APIidentification (b)C-APIidentification (c)P-APIandC-APIdataflowassociation
Fig.8. ResourceIDproduction,propagationandconsumption
First,BolaZanalyzestheAPIparameters.TheparametersoftheP-APIarepropagatedtotheforeignkeyinthe
MSGinterval,indicatingthattheP-APIfirstconsumesaspecifictypeofresourceIDandthenproducesanotherkindof
resourceID.AsshowninFig.9,thecommentID’sMSGintervaldependsontheblogID’sMSGinterval.BolaZtracks
thepropagationdataflowofparameterstofindthemappingrelationshipbetweenparametersandforeignkeys.
Fig.9. PC-APIidentification.theAPIgeneratescommentIDswhileconsumingtheblogID,whichisbothaC-APIandaP-API.
Second,theAPItokenrepresentstheencryptedinformationoftheuser’sownidentity.Underthepremisethatthe
tokenisnotleaked,theattackerisnotcapableoflaunchinganattackbymodifyingthetoken.Therefore,tokensarenot
consideredthepotentialinjectionpointsofBOLAattacks.However,afterpropagation,thetokenwillbeconvertedto
theuserID,whichmaybepassedtotheconditionsofSELECTstatementsinP-API.Itisalsoadependencyconditionfor
generatingMSGintervals.BolaZtracksthetokenpropagationtodiscoverwhethertokensareassociatedwithuserId.
Third,theremaybeaparent-childdependencybetweenresourceIDsinP-APIs.ObtainingtheMSGintervalofthe
parentresourceIDisthepremiseofcalculatingtheMSGintervalofthesub-resourceID.AsshowninFig.10,theAPI
usesSQL-(a)andSQL-(b)toproduceMSGintervalsofblogIDanddiscussID,respectively.SQL-(a)forSQL-(b),and
SQL-(b)dependsonSQL-(a).BolaZtracksthedependencyofresourceIDswithinP-APIbetweenSQLstatements.
Finally,BolaZidentifiestheP-APIbyanalyzingtheSELECTstatementthatreturnstheresourceIDintheAPIand
extractsMSGintervals.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 11
Fig.10. DependencyonresourceID
4.3 C-APIIdentificationandBOLAAttackInjectionPointDiscovery
C-APIisdownstreamfromthepropagationdataflowofresourceID.TheBOLAattacktakestheresourceIDparameter
oftheC-APIastheinjectionpoint,soBolaZneedstoidentifytheC-APIanddeterminewhichparametershavea
mappingrelationshipwiththeresourceID.
BOLAattackinjectionpointsexistinuser-controlledresourceIDparameters,whicheventuallypropagatetotheSQL
statement’sprimaryorforeignkey.SincetheresourceIDparameterdoesnotchangeintheC-APIpropagationprocess
(detailedin3.4.3),BolaZalsousestainttrackingtechnology[24]toanalyzewhichAPIparametersarepropagatedto
SQLstatements,anddetermineswhichresourceIDisassociatedwithAPIparametersbyanalyzingtheASTofSQL
statements.
AsshowninFig.8b,BolaZusesAPIparameters(blogId)astaintsourcesandSQLstatementsastaintpropagation
endpoints.BolaZfoundthatblogIdeventuallyspreadtotheidconditionofDeletestatementtodeleteblog.BolaZ
determinesthatthedeleteBlog{blogId}isC-API,andtheblogIdparameterconsumestheprimarykeyidoftheblogtable.
BolaZdetermineswhethertheAPIparametersconsumetheresourceIDfromthecontextcorrelationbetweenAPI
parametersandprimaryorforeignkeysinthefouroperationtypesofSQLstatements,asshowninTable1.
Table1. C-APIidentification
Type Mapping
Select ThereisamappingrelationshipbetweenAPIparametersandthewherecondition’sprimarykeyor
foreignkeyintheSQLstatement.
Delete ThereisamappingrelationshipbetweenAPIparametersandthewherecondition’sprimarykeyor
foreignkeyintheSQLstatement.
Insert APIparametersaremappedwiththeprimaryorforeignkeyoftheinsertedvalueintheSQLstatement.
𝑈𝑝𝑑𝑎𝑡𝑒 1 ThereisamappingrelationshipbetweenAPIparametersandupdatevaluesinSQLstatements.
𝑈𝑝𝑑𝑎𝑡𝑒 2 ThereisamappingrelationshipbetweenAPIparametersandthewherecondition’sprimarykeyor
foreignkeyintheSQLstatement.
4.4 P-APIandC-APIDataFlowAssociation
EffectivedefenseagainstBOLAattackshingesoncapturingAPIcontexts[42].Insystemdevelopment,developersretain
thecontextrelationshipbetweenP-APIsandC-APIswhenwritingfront-endcode.Therefore,BolaZcanalsoanalyze
thepropagationrelationshipofresourceIDsbetweenP-APIsandC-APIsinfront-endcodethroughtainttracking
technology.
ManuscriptsubmittedtoACM

12 AnbinWuetal.
AsshowninFig.8c.Whenthepageisloaded,theJavascriptcodecallstheP-API(/getUserBlog)togettheblogcreated
bytheuserhimself.TheHTMLcoderenderstheblogresourcesreturnedbytheP-APIandprovidesaclickeventsothat
theusercancallthedeleteBlogfunction.Whentheuserinitiatesaclickeventinthepage,theJavascriptcodecallsthe
C-API(/deleteBlog/{blogId})todeletethecorrespondingblogresource.BolaZtakesP-APIasthestartingpointoftaint
trackingandC-APIastheendpointoftainttrackingdetermineswhichP-APIprovidesresourceIDsfortheC-API.
4.4.1 IdentifyTheDataFlowofP-APIsAndC-APIs. BolaZcapturesthepropagationofresourceIDwithinandbetween
HTMLpages.First,weanalyzethepropagationofresourceIDwithintheHTMLpage.AsshowninFig.11,BolaZ
dividestheinternalpropagationofthepageintofourdataflowpatterns,withP-APIasthestartingpointofdataflow
propagation.C-APIwillterminatethedataflowafterconsumingtheresourceID.Therouterisusedtorealizethe
functionofjumpingfromonepagetoanother,andtheparameterscanbecarriedoutduringthejumpingprocess.
Fig.11. DataflowbetweenP-APIandC-API
• P-APItoC-API:P-APIpropagatesresourceIDsdirectlytoC-API
• P-APItoEventtoC-API:P-APIpropagatesresourceIDstoC-APIthroughHTMLevents.
• P-APItoRouter:P-APIpropagatesresourceIDstoRouter.
• P-APItoEventtoRouter:P-APIpropagatesresourceIDstoRouterthroughHTMLevents.
Secondly,thepropagationofresourceIDbetweenHTMLpagescancomplementthedataflowofP-APIandC-API
betweenmultipleHTMLpages.AsshowninFig.11,BolaZusestwodataflowpatternstoreceivetheresourceID
passedfromtheparentHTMLpage.
• RoutertoPC-API:RouterreceivesresourceIDsofparentpagesandpropagatesthemtoPC-API.
• RoutertoC-API:RouterreceivestheresourceIDofparentpagesandpropagatesthemtoC-API.
Throughtheabovesixdataflowpatterns,BolaZtrackingAPIworkflowstoobtainthelogicalrelationshipbetween
attackinjectionpointsandMSGintervals,andensuringthattheauthorizationpolicyofinjectionpointsconstantly
changeswithAPIworkflows.
4.4.2 GenerationofMSGIntervalSet. TheMSGintervaloftheresourceIDproducedbytheP-APIistheauthorization
intervaloftheassociatedC-APIattackinjectionpoint.However,thethreecharacteristicsofMSGintervalsgenerated
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 13
byP-APIsleadtothelimitationsoftheauthorizationintervalofattackinjectionpointsinC-APIs:thediversityof
resourceIDs,thedependencebetweenresourceIDs,andtheincompletenessofforeignkeyresourceIDs.Therefore,
BolaZperformsthefollowingthreeoperationsonMSGintervals.
Matching.P-APImaycreateMSGintervalsformultipleresourceIDs.Therefore,BolaZmustmatchtheresourceID
consumedbyC-APIwiththeresourceIDcreatedbyP-API.
DependenceResolving.WhenthereisanydependencybetweenresourceIDs,BolaZwillanalyzetheMSGinterval
oftheparentresourceID.IftheMSGintervaloftheparentresourceIDcoversallthedatainthedatabasetable,the
childresourceIDwilldiscardthelimitationoftheparentresourceID.Otherwise,BolaZwillupdatetheconditionof
theparentresourceIDtotheMSGintervaloftheparentresourceID.
Backtracking.TheprimaryorforeignkeyobtainedbyP-APImaybecometheresourceIDthatC-APIrequires.The
MSGintervaloftheprimarykeyiscomplete,whichcanprovidetheC-APIwithafullrangeofpermissionsforthe
availableresourceID.Theforeignkeyonlyhasapartialmappingrelationshipwiththeprimarykeyofotherresources,
andthegeneratedMSGintervalisincomplete.
TheforeignkeyisinsertedintothedatabasebytheC-APIoftheresourcecreationtype(POST),sotheMSGrangeof
theforeignkeyiscreatedbytheP-APIthatprovidestheresourceIDforthePOSTC-API.AsshowninFig.12,indata
stream1,theP-APIofResourceBpassestheresourceIDoftheprimarykeytothePOSTC-APIofResourceA,andthe
C-APIstorestheprimarykeyofResourceBastheforeignkeyofResourceA.Indatastream2,theP-APIpropagates
theresourceIDoftheforeignkeytotheC-API.TheMSGintervaloftheforeignkeyresourceIDindatastream2comes
fromtheP-APIindatastream1.Therefore,BolaZconvertstheMSGintervaloftheforeignkeyintotheMSGinterval
oftheprimarykeyoftheP-APIassociatedwiththePOSTC-APIthroughdatastreambacktracking,asshownindata
stream3.
Fig.12. Dataflowbacktracking
C-APImayhavemultipleassociatedP-APIs,whichmeansitisrelatedtonumerousMSGintervals,thusforminga
setofMSGintervals.
4.4.3 Optimization of MSG Interval Set. There may be subset or intersection relationships between the internal
elementsoftheMSGintervalset,andperformingrepeatedintervalquerieswillresultinconsiderableperformance
costs.Therefore,BolaZdefinesthemergingrulesofSELECTstatementstoreduceitsnumberunderthepremiseof
ManuscriptsubmittedtoACM

14 AnbinWuetal.
ensuringthattheMSGintervaldoesnotchange,thusreducingthenumberofSELECTstatementsandthequeryof
repeatedintervals.
First,wedefinetheidentifiersinthemergingrules,asshowninTable2.Then,wediscussthemergingrulesofSQL
statementsfromtheperspectiveofthecoincidencerelationshipbetweenMSGintervals,AsshowninFig.13.
|     |     |     | Fig.13. MSGintervaloptimization |     |
| --- | --- | --- | ------------------------------- | --- |
Table2. Mergeruleidentifier
Type Meaning
𝑆 𝑞 Singletablequery.
𝑀 Multitablequery.
𝑞
𝑀
𝑡 Themaintableinmulti-tablequery.
𝑆 𝑖 TheithMSGinterval(SQLstatement)associatedwiththeC-API.
|     | 𝑇 𝑖 | 𝑇 𝑖 isthetablecorrespondingtoresourceIDproducedin𝑆 |     | 𝑖.     |
| --- | --- | -------------------------------------------------- | --- | ------ |
|     | 𝑊   | 𝑊 isthesetofwhereconditionsrelatedto𝑇              |     | in𝑆 𝑖. |
|     | 𝑖   | 𝑖                                                  |     | 𝑖      |
Rule#1:Subsetrule.WhenthereisasubsetrelationshipbetweenthetwoSQLstatements,theBolaZmergesthe
twoSQLstatementsintoaparentSQLstatement.
Precondition:
| 𝑆 ∈𝑆       | ,𝑆 ∈𝑆 ,𝑇       | =𝑇        |          |     |
| ---------- | -------------- | --------- | -------- | --- |
| • 𝑖 𝑞      | 𝑗 𝑞 𝑖          | 𝑗         |          |     |
| • 𝑆 ∈𝑀     | ,𝑆 ∈𝑀 ,𝑇       | ∈𝑀 ,𝑇     | ∈𝑀 ,𝑇 =𝑇 |     |
| 𝑖          | 𝑞 𝑗 𝑞          | 𝑖 𝑡 𝑗     | 𝑡 𝑖 𝑗    |     |
| • 𝑆 𝑖 ∈𝑆 𝑞 | ,𝑆 𝑗 ∈𝑀 𝑞 ,𝑇 𝑗 | ∈𝑀 𝑡 ,𝑇 𝑖 | =𝑇 𝑗     |     |
if:
| 𝑊 𝑖 =∅or𝑊 | 𝑖 ⊆𝑊 𝑗 |     |     |     |
| --------- | ------ | --- | --- | --- |
then:
𝑆 ∪𝑆 =𝑆
| 𝑖   | 𝑗 𝑖 |     |     |     |
| --- | --- | --- | --- | --- |
Rule#2:Intersectionandunionrule.WhentwoSQLstatementshaveanintersectionorunionrelationship,the
BolaZmergesthewhereconditionsofthetwoSQLstatements.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 15
Precondition:𝑆
𝑖
∈𝑆
𝑞
,𝑆
𝑗
∈𝑆
𝑞
,𝑇
𝑖
=𝑇
𝑗
if:
𝑊
𝑖
∩𝑊
𝑗
=∅or𝑊
𝑖
∩𝑊
𝑗
≠∅,𝑊
𝑖
⊈𝑊
𝑗
then:
𝑆
𝑖
∪𝑆
𝑗
=𝑊
𝑖
∪𝑊
𝑗
BolaZusestheoptimizedMSGintervaltoperformaresourceIDauthorizationcheckontheBOLAattackinjection
pointoftheC-API.SupposetheoptimizedMSGintervalcancoverallthedatabasetabledata.Inthatcase,itshows
thattheresourceIDconsumedintheC-APIisunlimited,andtheBolaZdoesnotperformauthorizationchecksonthe
C-API.
5 Implementation
Inthissection,wedetailtheimplementationof BolaZ,atoolfordetectingBOLAvulnerabilitiesinSpringBoot-based
webapplications.AsshowninFig.14,BolaZincludesofflineanalysisandruntimeauthorization.
Fig.14. ImplementationoftheBolaZ
5.1 OfflineAnalysis
BolaZutilizesCodeQL’stainttrackingtool[8]totracethedataflowofresourceIDs.BolaZfocusesondetermining
MSGintervalsforAPIsthatoperateunderordinaryuserpermissions.Ifanattackergainsadministratorprivileges,he
haspermissiontooperateonallresourcesanddoesnotneedtolaunchBOLAattacks.Notperformingauthorization
checksonadministratorrightsAPIsalsoreducestheperformanceoverheadof BolaZ.
The first step is identifying P-APIs. BolaZ uses global taint tracking [9], treating API parameters or function
expressionsasthesourceandAPIreturnsasthesink.Duringthedatapropagationprocess,BolaZanalyzestheabstract
syntaxtree(AST)ofSQLstatementstoextractresourceIDsanddeterminetheMSGintervalsproducedbytheAPI.
ThegeneratedMSGintervalsarestoredintheMSGengine.BolaZalsotrackstokenpropagation.WhileRESTfulAPIs
typicallyusetoken-basedauthenticationmethodssuchasJWT[22]orOAuth[15],thespecificimplementationvaries
acrossapplications,makingitchallengingtoextracttokenflagsfromsourcecode.Therefore,BolaZrequiresdevelopers
toprovidetherelevanttokencodeflags.
ManuscriptsubmittedtoACM

16 AnbinWuetal.
ThesecondstepisC-APIidentification.BolaZusesAPIparametersasthesourceandSQLstatementsasthesinkto
maptherelationshipbetweenparametersandresourceIDs,identifyingbothBOLAattackinjectionpointsandC-APIs.
Finally,toestablishthedataflowassociationsbetweenP-APIsandC-APIs,BolaZanalyzesthepropagationpaths
ofresourceIDsinthefront-endcode.Byleveragingsixdataflowpatterns,itidentifiesdirectorindirectresourceID
propagationthroughoutthesystem.
5.2 RuntimeAuthorization
BolaZcheckstheauthorizationofresourceIDaccordingtoMSGintervalsgeneratedbyofflineanalysiswhenthe
systemisrunning.ResourceIDsusedbyusersmustexistinMSGintervals,otherwise,theC-APIcallwillbeblocked.
Weconsiderthatwhenthedatabasedatasizeislarge,ifdatabasequeriesareperformedateachC-APIauthorization
check,itwillleadtohighlatency.C-APIswillbecalledinashorttimeafteruserscallP-APIs.Hence,theMSGengine
cachesresourceIDsproducedbyP-APIs.Ifthecacheisnothit,adatabasequeryisperformed.Acacheordatabasehit
meanstheC-APIhasaccesstotheresourceID.
6 Evaluation
6.1 ResearchQuestions
RQ1:HowistheeffectivenessofBolaZidentifyingAPItypesandassociations?
First,BolaZtransformsthedefenseofBOLAattacksintothreesub-problemsintheresourceIDworkflow(see3.3).
Hence,ourexperimentsfirstevaluatetheeffectivenessofBolaZbyverifyingthetechnicalconsistencyofeach‘module’
(see4.1)throughdataflowanalysis.
RQ2:HowmuchextraperformanceoverheaddoesBolaZcost?
Second,BolaZperformsauthorizationcheckingonresourceIDsbycachingordatabasequeries,whichresultsinextra
performanceoverhead.WeevaluatetheperformanceoverheadofBolaZbycomparingtheoriginalsystemandthe
BolaZ-addedsysteminthreeaspects:P-APIstoragecache,C-APIcachequeryanddatabasequery.
RQ3:HoweffectiveisBolaZ’sdefenseagainstreal-worldBOLAattacks?
BolaZshouldbeabletodefendagainstBOLAattacksintherealworld.WefirstusetheCVEvulnerabilitytoevaluatethe
effectivenessof BolaZ’sdefenseagainstexistingvulnerabilities.Second,weverifyBolaZ’sabilitytodetectunknown
vulnerabilitiesbyscanningtheBOLAvulnerabilityofopen-sourceprojects.
RQ4:HowdoesBolaZcomparewiththeSOTAapproach?
BOLARAYisthemostcloselyrelevantworktoBolaZandistheSOTAmethodfordetectingBOLAvulnerabilities.
Therefore,wecomparedthevulnerabilitydetectioneffectofBOLARAYandBolaZinreal-worldprojects.
6.2 Dataset
6.2.1 Howtocollectprojects. Astheimplementationof BolaZisontheSpringBootframeworkinJavalanguage,we
searchedforrepositoriesthatdependonSpringBootonGitHub[39],SourceCodeExamples[38]andLibHunt[25]and
filteredthembyapplicationtypes,authenticationmodes,andlogiccontrolmodes.
Theselected10projectscovervariousapplicationtypes,twoauthenticationmodes,andtwologiccontrolmodes.1).
Applicationtype.Therearesimilaritiesinthebusinesstypesofopen-sourceprojects.Theprojectweselectedcontains
Blog,Bookstore,E-commerce,ContentManagementSystem,OnlineExaminationSystem,PeopleInformationSystem,
etc.WescreensystemswithdifferentbusinesslogicsothatBolaZcancoveravarietyofbusinessscenarios.2).User
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 17
Table3. Statisticsonevaluationprojects
| Project                | Stars Files | LLOC APIs | Description         |
| ---------------------- | ----------- | --------- | ------------------- |
| Blog-master[30]        | 616 106     | 42,366    | 57 BlogSystem       |
| BookStore-master[40]   | 314 168     | 29,944    | 71 BookstoreProject |
| Mall-master[27]        | 78.8k 121   | 15,467    | 65 E-commerceSystem |
| NewbellMall-master[33] | 1.4k 140    | 16,546    | 62 MallSystem       |
IceCms-master[44] 1.7k 241 80,308 109 ContentManagementSystem
| MusicwWbsite-master[46] | 5.7k 133 | 42,906 | 63 MusicWebsite |
| ----------------------- | -------- | ------ | --------------- |
OnlineExam-master[47] 2k 106 8,116 46 OnlineExaminationSystem
UniversityForum-master[11] 196 64 13,279 16 UniversityCampusForum
InformationSystem-master[6] 2k 20 2,344 4 PeopleInformationSystem
| OnlineMall-master[41] | 32 118  | 10,640      | 33 OnlineMall |
| --------------------- | ------- | ----------- | ------------- |
| Total                 | - 1,217 | 261,916 526 | -             |
authenticationmode.Userauthenticationmodesincludetokensandcookies,sothesystemwehavechosencoversboth
userauthenticationmodes.3).Logicalcontrolmodes(detailedin3.4.2),asshowninTable3.Basedonthesethree,the
selectedprojectsaresufficientandcaneffectivelycoverourscopeofproblems.WefocusontheAPIdataflow,which
requiresagoodcoverageofbusinesstypes.Itisoflittlesignificancetoinvolvemoreprojects.
6.2.2 RQ1&RQ2. ThereisnotooltoachievetheclassificationandassociationofAPI.Toconstructthedataset’s
groundtruth,weneedtodeployprojectslocallyandmanuallycountandidentifyP-API,C-APIandtherelationship.
Thewholeprocessiscomplexandtime-consuming.SoweselectedfivesystemsfromTable3basedonapplication
types,logicalcontrolmode,anduserauthenticationmodestocontributeabenchmarktoverifytheeffectivenessof
| BolaZ,asshowninTable4.Sufficienttoverifytheeffectivenessof |     | BolaZ. |     |
| ---------------------------------------------------------- | --- | ------ | --- |
WemanuallyanalyzedtheAPIcategoriesandrelationshipstobuildthegroundtruthdata.First,wedeployedand
rantheprojectlocally,logginginasaregularusertoaccessallfunctionalities.Simultaneously,weusedFiddler[43]to
capturetheAPIlist.Next,weexaminedtheAPIserver’ssourcecode.Giventhatthecurrentarchitecturefollowsa
three-tiermodel,wewereabletoquicklycategorizetheAPIs.Wethenanalyzedthefront-endsourcecodetotracethe
propagationpathsofresourceIDsbothwithinandacrosspages.Ourteamwasdividedintotwogroups,analyzingthe
project’ssourcecodeindependently,followedbycross-validationoftheresults.Acrossthefiveprojects,weidentifieda
totalof40P-APIsand54C-APIs.
6.2.3 RQ3-1. WesearchedtheCVEvulnerabilitydatabaseforBOLA(a.k.a.,IDOR)vulnerabilities.Theresultsindicate
thatonlyafewarefromJavaprojects(e.g.,SpringBoot).Finally,wescreenedoutthreevulnerabilitiescorrespondingto
thethreemodesofBOLAattackfromtheCVE-2023-36100[13]andCVE-2023-32310[12].
6.2.4 RQ3-2. Thesurveyofexistingwork[18],[5],[37],[29]foundnocurrentlarge-scalebenchmarks.Wedetect
unpublishedBOLAvulnerabilitiesinthese10projectstoevaluatetheeffectivenessof BolaZintherealworld.
6.2.5 RQ4. BOLARAY is used to detect BOLA vulnerabilities in PHP. We adapted BOLARAY to the SpringBoot
frameworkandcompareditwithBolaZbydetectingBOLAvulnerabilitiesinthecollected10projects.
ManuscriptsubmittedtoACM

18 AnbinWuetal.
Table4. BenchmarkofIdentifyingAPITypesandAssociations,RdenoteRelation,LCMdenoteLogiccontrolmode,UAMdenote
Userauthenticationmode.
| Project           |     | P-API C-API |     | API-R | LCM UAM       |     |
| ----------------- | --- | ----------- | --- | ----- | ------------- | --- |
| NewbellMall       |     | 9           | 14  | 17    | Server Token  |     |
| OnlineExam        |     | 11          | 20  | 20    | Server UserId |     |
| Blog              |     | 10          | 14  | 49    | Client Token  |     |
| UniversityForum   |     | 9           | 4   | 10    | Server UserId |     |
| InformationSystem |     | 1           | 2   | 2     | Server Token  |     |
| Total             |     | 40          | 54  | 98    | - -           |     |
6.3 Metrics
Inourexperiment,weevaluatedthefollowingindicators.WeusePrecisionandRecalltomeasuretheeffectiveness
ofAPIclassificationandAPIassociation.TruePositive(TP)representsthenumberofcorrectlyclassifiedAPIs;The
numberofAPIpairsthatarecorrectlyassociated.FalsePositive(FP)representsthenumberofAPIsclassifiedasP-API
(C-API)butnotP-API(C-API);ThenumberofAPIpairsthatarejudgedtobeassociatedwithP-APIsandC-APIsbutdo
notexist.FalseNegative(FN)representsthenumberofAPIsclassifiedasnotP-API(C-API)butP-API(C-API);The
numberofP-APIandC-APIpairsthatarejudgednottobeassociatedbutareassociated.TheformulasforPrecision(Pr)
andRecall(Re)areasfollows.
|     |      | 𝑇𝑃    | 𝑇𝑃    |     |     |     |
| --- | ---- | ----- | ----- | --- | --- | --- |
|     | 𝑃𝑟 = | ,𝑅𝑒   | =     |     |     | (4) |
|     |      | 𝑇𝑃+𝐹𝑃 | 𝑇𝑃+𝐹𝑁 |     |     |     |
6.4 RQ1:HowistheEffectivenessofBolaZIdentifyingAPITypesandAssociations?
6.4.1 Setup. Theexperimentwascompletedintwosteps.First,weuseBolaZtoclassifytheAPIsintheproject.
SupposethereisanerrorintheAPIclassification.Inthatcase,wewillmodifytheAPItothecorrecttypebecause
thepremiseofaccuratelyassociatingtheAPIistoobtaintheaccurateAPItype.Inthesecondstep,weuseBolaZto
associateP-APIwithC-API.
Table5. EffectivenessofAPIClassificationandAssociation,PdenotesP-API,CdenotesC-API,RdenotesRelation.
| Project           | P-Pr  | P-Re    | C-Pr  | C-Re  | R-Pr R-Re   |     |
| ----------------- | ----- | ------- | ----- | ----- | ----------- | --- |
| NewbeeMall        |       | 8/8 8/9 | 14/14 | 14/14 | 17/17 17/17 |     |
| OnlineExam        | 11/11 | 11/11   | 20/20 | 20/20 | 20/21 18/20 |     |
| Blog              | 10/10 | 10/10   | 13/13 | 13/14 | 42/42 42/49 |     |
| UniversityForum   |       | 9/9 9/9 | 4/4   | 4/4   | 7/7 7/10    |     |
| InformationSystem |       | 1/1 1/1 | 2/2   | 2/2   | 2/2 2/2     |     |
6.4.2 Results. Theexperimentalresultsof BolaZarereportedinTable5.BolaZachievedrecallratesof97%forAPI
classificationand87%forAPIassociation,withonefalsepositive.TheprecisionofAPIclassificationandassociation
ishighbecausetheresourceID,astheuniqueidentificationoftheresource,israrelymodifiedintheprocessofdata
flowpropagation.BolaZcancategorizeandassociateAPIsveryaccuratelywithoutinterruptingthetainttracking.We
alsoanalyzethereasonsforthefailureofAPIclassification.Byexaminingthelog,wefoundthatCodeQLgenerated
dataflowinterruptionattheArrays.asListmethodduringthetainttrackingprocess,failingP-APIidentificationofthe
Newbellmallproject.TheBlogprojectalsofailedC-APIrecognitionduetodataflowinterruption.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 19
WeobservedthattheOnline-Exam,UniversityForumandBlogprojectshavelowAPIassociationrecallrates.First,
weanalyzeOnline-ExamandUniversityForumprojects.TheC-APIsofassociationfailureareallattackinjectionpoints
ofuserId,suchasGET/api/score/{current}/{size}/{studentId}.Byanalyzingthesourcecode,wefoundthatnoP-API
providesstudentIdforC-APIsthatfailtocorrelate,andthesestudentIdarederivedfromtheclient’slocalcookie.The
Online-ExamProjectsavesthestudentIDtotheclient’scookieafterthestudentuserlogsinandprovidesittothe
C-API.RESTAPIstypicallyuseencryption,suchasJWT,forauthentication,andtheOnlineExamproject’smethodof
usingtheuserIDisnotsecure.Atpresent,theuserIDwillexistinmoreAPIreturndata,anditiseasyforattackersto
usetheuserIDtolaunchBOLAattacks.AlthoughBolaZcansolvethisproblembyextendingthedataflowfromclient
datastorage(cookie,localstorage)toC-API,thisAPIauthenticationmodeisnotsecure.
BolaZgeneratedtheonlyfalsepositiveinanalyzingAPIrelationshipsintheonline-examproject.Afteranalyzing
thesourcecode,wefoundthatthereasonwasthattheclientcodemodifiedtheresourceIDgeneratedbyP-APIand
passedittothedownstreamC-API,resultinginBolaZincorrectlyassociatingthecontextofP-APIandC-API.BOLAZ
needstoanalyzethesourcecodetoobtainthemodificationlogicoftheresourceIDtosolvethistypeoffalsepositive.
Theproblemistransformedintoextractingoperationalsemanticsfromthesourcecode.
Secondly,weanalyzethattheBlogprojectisduetotheexistenceofclientlogiccontrolinthesystem,whichleadsto
thefailureoftheAPIassociation.Forexample,v-if=getStoreName()==name||getStoreRoles().indexOf("ADMIN")>-1.
Thisconditionmeansthattheuser’snamestoredbytheclientisequaltotheusernameoftheresource,orthestored
permissionstringcontainsADMINsothattheusercanseethebuttontodeletetheblogandhavetherighttocall
theAPItodeletetheblog.However,BolaZcannotaccuratelydeterminethemeaningofthiscondition,failingthe
associationbetweenthedeletionAPIofblogresourcesandthelistAPI.
Insight#1:Staticanalysiscombinedwithdynamicanalysisisaworthtryingdirection,whichhasthepotentialto
refinepropagationlogicofresourceID.
AnswertoRQ1:BolaZachievedrecallratesof97%forAPIclassificationand87%forAPIassociation,withfew
falsepositives.
6.5 RQ2:HowMuchExtraPerformanceOverheaddoesBolaZCost?
6.5.1 Setup. ToevaluatetheperformanceoverheadcausedbyBolaZ,weselecttheNewbeemallprojectasthetest
systemofperformanceoverheadfromtheGitHubstars,thenumberofAPIs,andtherecallofidentifyingandassociating
APIs,andselectP-APIsandC-APIs,asshowninTable6.
Weconductedaround-triplatency(RTT)comparisontestbetweentheoriginalapplicationsystemandtheBolaZ-
addedsystemtoevaluatetheextraperformanceoverheadof BolaZ,whichmainlyincludesthreeaspects:theextra
RTTbroughtbyP-APIscacheresourceID;theextraRTTbroughtbyC-APIsquerycache;theextraRTTbroughtby
C-APIsquerydatabase.
6.5.2 Results. Firstly,wetesttheperformancecostoftheP-APIcacheresourceID.Torestoretherealapplication
scenario,weuseApacheJMeter[21]tosimulate100usersaccessingmultipleP-APIsconcurrentlyatdifferentdata
levelsandaveragetheRTT.ThetestresultsareshowninFig.15.Astheamountofdatainthedatabaseincreases,the
performancecostof BolaZincreases.Whentheoriginalsystemhas6secondsRTT,BolaZonlyincreasesthedelayby
hundredsofmilliseconds,whichuserscanaccept.
ManuscriptsubmittedtoACM

20 AnbinWuetal.
Table6. TestAPI
Type API AssociatedP-API
P-API GET/address -
P-API GET/shop-cart/page -
P-API GET/order -
C-API GET/order/{orderNo} GET/order
C-API DELETE/shop-cart/{cartItemId} GET/shop-cart/page
C-API DELETE/address/{addressId} GET/address
Fig.15. PerformanceoverheadofP-API
Second,wetesttheperformanceoverheadcausedbyBolaZ’sMSGintervalcheckingofC-API.Wefirsttestedthe
averageRTTofC-APIatdifferentdatalevelsunder1,000userconcurrencyintheoriginalsystem.Then,wetestedthe
averageRTTofsystemcachehitsandmissesunderBolaZprotection.ThetestresultsareshowninFig.16.Through
experiments,wefoundthat1)ThedelaycausedbyBolaZtotheoriginalsystemremainswithin1secondwhetheritis
acachehitornot.2)Thecachehitqueryspeedisfasterthanthedirectquerydatabase,butthegapisnotverybig.The
gapissmallbecauseBolaZaddstheprimarykeyresourceIDasaqueryconditiontotheSQLstatement.Aftertesting
inMysql8,thequeryspeedofSQLstatementswithprimarykeyconditionscanbemaintainedatthemillisecondlevel
atthe700wdatalevel.
TheperformanceoverheadofBOLAZisduetothequerycacheordatabase,independentoforiginalsystems.The
overheadisentirelyrelatedtothespeedofcacheordatabasequeries.
AnswertoRQ2:RegardlessofP-APIscacheresourceIDsorC-APIsqueryresourceIDsfromthecacheanddatabase,
theperformancecostof BolaZremainsatthemillisecondlevel.
6.6 RQ3:HowEffectiveisBolaZ’sDefenseAgainstReal-worldBOLAAttacks?
6.6.1 Results. Theresultsoftheevaluationonreal-worldBOLAvulnerabilitiesareshowninTable7.
BFLA(CVE-2023-36100).TheattackerobtainstheuseridsofallusersbyaccessingAPI1(GET/squareComment/getAll-
Square)verticallyunauthorizedlyandthentamperingwiththeuserIdinjectionpointofC-API1(POST/api/User/ChangeUser
Body:User,userId)tomodifytheinformationofotherusers.Byanalyzingthedataflow,BolaZfoundthatP-API1(GET
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 21
|                       | Fig.16. PerformanceoverheadofBolaZ      |                                               |
| --------------------- | --------------------------------------- | --------------------------------------------- |
|                       | Table7. EvaluationonBOLAvulnerabilities |                                               |
| Type                  | APIType                                 | API                                           |
| BFLA                  | VerticalPrivilege                       | GET/squareComment/getAllSquare/{page}/{limit} |
| CVE-2023-36100(C-API) |                                         | POST/api/User/ChangeUser/{jwt}Body:userId     |
|                       | P-API                                   | GET/User/GetUserInfoByid/{user_self_id}       |
| ExcessiveDataExposure |                                         | GET/api/share/treeList                        |
BOPLA
| CVE-2023-32310(C-API) |       | POST/api/share/removePanelShares/{panelId} |
| --------------------- | ----- | ------------------------------------------ |
|                       | P-API | POST/api/share/shareOut                    |
| CVE-2023-32310(C-API) |       | POST/api/sys_msg/batchDeleteBody:msgId     |
UASBF
|     | P-API | POST/api/sys_msg/list/{goPage}/{pageSize} |
| --- | ----- | ----------------------------------------- |
/User/GetUserInfoByid/{user_self_id})providedtheuserIdforC-API1.P-API1returnstheuser’sownuserId,soC-API1
canonlyusetheuser’sownuserId.
BOPLA(CVE-2023-32310).theattackeruseAPI2(GET/api/share/treeList)canviewthepanelIdofthepanelsshared
byotherusersandmodifythepanelIdparameterofC-API2(POST/share/removePanelShares/{panelId})toremovethe
panelssharedbyotherusers.However,undertheprotectionofBolaZ,attackersdonothavepermissiontousepanelids
sharedbyotherusersinC-API2.PanelIdauthorizationfailsbecausethereisnodataflowinthesystemforAPI2to
propagatepanelIdtoC-API2.P-API2(POST/share/shareOut)isassociatedwithC-API2,andP-API2isolatesthepanelId
ofC-API2intothepaneIdofthepanelthattheusershares.
UASBF(CVE-2023-32310).ThemsgIdinjectionpointofC-API3(POST/sys_msg/batchDeleteBody:msgId)isanumeric
type,andtheattackerconstantlyguessesmsgIdofotherusers.BolaZlearnsfromthedatastreamthatP-API3provides
msgIdsforC-API3.P-API3(POST/sys_msg/list)generatesthesystemmessagesusersreceive,soC-API3canonlydelete
messagesusingthemsgIdofthemessagesitreceives.
Detectioninthewild.WeuseBolaZtoscanprojectsinTable3toobtaintheMSGintervaloftheC-APIresource
ID.BypassingtheresourceIDoutsidethepermissionintotheC-APIparameter,wedeterminewhetherthereisa
vulnerabilityaccordingtotheresponseresult.BolaZreportsatotalof36vulnerabilities,ofwhich35vulnerabilitieshave
beenmanuallyconfirmedasrealvulnerabilities,asshowninTable8.Thefalsepositiveiscausedbythemodificationof
theresourceIDduringthepropagationprocess.WehavesubmittedvulnerabilityinformationtotheCVEvulnerability
database.Duetoethicalconsiderations,wewilldisclosethevulnerabilityafternotifyingthemanufacturertorepairit.
Thedetailsof BolaZreportvulnerabilitiesareshowninTable9.
ManuscriptsubmittedtoACM

22 AnbinWuetal.
Wealsofoundanimplementation-defectiveAPI(API1:findartbyuserid/{userId})whosefunctionistoobtainaself-
publishedarticle.TheuserIdparameterinAPI1istheuser’sownuserId,butthecallercanobtainthearticlepublishedby
otherusersbymodifyingtheuserId.API1doesnotperformaccesscontrolchecksonuserId.Althoughthereisanother
APIinthesystemthatcanviewalluser-publishedarticles,developersstillneedtoaddaccesscontrolcheckstoAPI1
duringimplementation.
Table8. BOLAvulnerabilitiesreportedbyBolaZ
|     | SELECT | INSERT UPDATE | DELETE | Total |
| --- | ------ | ------------- | ------ | ----- |
Project
|                   | TP FP | TP FP TP FP | TP FP | TP FP |
| ----------------- | ----- | ----------- | ----- | ----- |
| Blog              | 0 0   | 0 0 0 0     | 0 0   | 0 0   |
| BookStore         | 2 0   | 3 0 3 0     | 3 0   | 11 0  |
| Mall              | 1 0   | 0 0 1 0     | 0 0   | 2 0   |
| NewbellMall       | 0 0   | 0 0 0 0     | 0 0   | 0 0   |
| IceCms            | 1 0   | 3 0 0 0     | 0 0   | 4 0   |
| MusicwWbsite      | 3 0   | 4 0 3 0     | 3 0   | 13 0  |
| OnlineExam        | 1 0   | 1 1 1 0     | 0 0   | 3 1   |
| UniversityForum   | 0 0   | 2 0 0 0     | 0 0   | 2 0   |
| InformationSystem | 0 0   | 0 0 0 0     | 0 0   | 0 0   |
| OnlineMall        | 0 0   | 0 0 0 0     | 0 0   | 0 0   |
| Total             | 8 0   | 13 1 8 0    | 6 0   | 35 1  |
AnswertoRQ3:BolaZcandefendagainstBOLAattacksinthreeattackmodesandsupportsthedetectionof
BOLAvulnerabilitiesinreal-worldprojects.
6.7 RQ4:HowdoesBolaZComparewiththeSOTAApproach?
6.7.1 Setup. BOLARAYfirstanalyzesthesourcecodetoinfertheauthorizationmodeofresources,andthenverifies
whetherthesemodelscorrectlyimplementaccesscontrolchecks.BOLARAYdeterminestheaccesscontrolmodeof
theresourcebasedontheartificiallysummarizedauthorizationmode.BolaZdoesnotneedtoclassifyresourcesinto
specificauthorizationmodels.Therefore,wefocusonthedifferencebetweentheauthorizationmodelofBOLARAY
andtheaccesscontrolmodelofBOLAZbasedonsystemlogic.Inordertoeliminatethedeviationcausedbythe
authorizationmodeofBOLARAYinferenceresources,wefirstlabeltheresourceauthorizationmodelandusetheAPI
testmethodtoverifytheBOLAvulnerability.
BOLARAYneedstoanalyzeadmincolumntodetermineadministratorpermissions,butPHPandSpringBoothave
differentmethodsfordeterminingadministratorpermissions.InsomeSpringBootAPIs,thereisnoadministratorper-
missionflag.BolaZalsodetectedAPIswithnon-administratorpermissions.Therefore,inthecomparativeexperiment,
weremovetheAPIsofadministratorpermissions,registrationandlogin,andreducedthefalsepositivescausedby
BOLARAYduetoadmincolumn.
6.7.2 Results. TheresultsofthiscomparisonaresummarizedinTable10.BOLARAYcorrectlyidentified27trueBOLA
vulnerabilities,allofwhichwerealsodisclosedbyBolaZ.However,BOLARAYmissed8vulnerabilitiesreportedby
BolaZbecauseitcannotidentifyBOLAvulnerabilitiesfromSELECTstatements.Incontrast,BolaZcananalyzeBOLA
vulnerabilitieswithalltypesofSQLstatements.BOLARAYreported3falsevulnerabilities,buttheyaredifferentfrom
thosereportedbyBolaZ,asshowninTable11.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 23
Table9. Identifiedunpublishedvulnerabilitiesinprojects
Project Type Description
Mall SELECT AttackersgetorderinformationsofotherusersbymodifyingtheorderId.
Mall UPDATE AttackersupdateorderinformationsofotherusersbymodifyingtheorderId.
Musicwebsite UPDATE AttackersupdateinfoofotherusersbymodifyingtheuserId.
Musicwebsite UPDATE AttackersupdatepasswordofotherusersbymodifyingtheuserId.
Musicwebsite UPDATE AttackersupdateavatarofotherusersbymodifyingtheuserId.
Musicwebsite SELECT Attackersgetcollection’sdetailofotherusersbymodifyingtheuserId.
Musicwebsite INSERT Attackersaddcollection’sofotherusersbymodifyingtheuserId.
Musicwebsite DELETE Attackersdeletecollection’sofotherusersbymodifyingtheuserId.
Musicwebsite SELECT Attackersgetcollection’sstatusofotherusersbymodifyingtheuserId.
Musicwebsite SELECT AttackersgetrankofotherusersbymodifyingtheuserId.
Musicwebsite INSERT AttackersaddrankofotherusersbymodifyingtheuserId.
Musicwebsite INSERT AttackersaddcommentsofotherusersbymodifyingtheuserId.
Musicwebsite DELETE AttackersdeletecommentsofotherusersbymodifyingthecommentId.
Musicwebsite INSERT AttackersaddsupportofotherusersbymodifyingthecommentIdanduserId.
Musicwebsite DELETE AttackersdeletesupportofotherusersbymodifyingthecommentIdanduserId.
IceCMS SELECT AttackersgetotherusersinformationsbymodifyingtheuserId.
IceCMS INSERT AttackersinsertotherusersarticlecommentbymodifyingtheuserId.
IceCMS INSERT AttackersinsertotheruserssquarecommentbymodifyingtheuserId.
IceCMS INSERT AttackersinsertotherusersresourcecommentbymodifyingtheuserId.
BookStore DELETE AttackersdeleteaddressesofotherusersbymodifyingtheaddressId.
BookStore UPDATE AttackersupdateaddressesofotherusersbymodifyingtheaddressId.
BookStore INSERT Attackersaddcartofotherusersbymodifyingtheaccount.
BookStore DELETE Attackersdeletecartofotherusersbymodifyingtheaccount.
BookStore DELETE Attackersbatchdeletecartofotherusersbymodifyingtheaccount.
BookStore UPDATE Attackersupdatecartofotherusersbymodifyingtheaccount.
BookStore SELECT Attackersgetcartofotherusersbymodifyingtheaccount.
BookStore INSERT Attackersinitorderofotherusersbymodifyingtheaccount.
BookStore INSERT Attackersaddorderofotherusersbymodifyingtheaccount.
BookStore SELECT Attackersgetorderofotherusersbymodifyingtheaccount.
BookStore UPDATE AttackersupdateorderstatusofotherusersbymodifyingtheorderId.
OnlineExam UPDATE AttackersupdatepasswordofotherusersbymodifyingthestudentId.
OnlineExam INSERT AttackersaddscoreofotherusersbymodifyingthestudentId.
OnlineExam SELECT AttackersgetscoreofotherusersbymodifyingthestudentId.
UniversityForum INSERT AttackersaddpostofotherusersbymodifyingtheuserId.
UniversityForum INSERT AttackersaddcommentofotherusersbymodifyingtheuserId.
6.7.3 Casestudyoffalsepositives. Throughanin-depthinvestigation,wehavesummarizedthecausesofthesefalse
positivesasfollows.
Case1:Application-levelAuthorization[18].BOLARAYsimplifiedtheapplication-layeraccesscontrolpolicy
withtheadministratorrole,andthissimplificationresultedin2falsepositives.Intheonlineexamproject,theteacher
hasthepermissiontomodify,anddeletealluserdata,butBOLARAYbelievesthatnon-administratoruserscanonly
operateontheirownuserdata,resultinginfalsepositives.
Case2:Column-levelAuthorization[18].Someapplicationsrequiretheauthorizationmodeltobemoregranular
andlimitedtospecificcolumns,leadingtoafalsepositive.Inthemusicwebsiteproject,thecommenttableisdefined
by BOLARAY as the ownership model, and a comment can only be updated/deleted by its owner. However, the
comment-likeAPI(/comment/like)modifiesthecomment’slike_countcolumn,whichcanbemodifiedbyallusers.
ManuscriptsubmittedtoACM

24 AnbinWuetal.
Table10. BOLAvulnerabilitiesreportedbyBOLARAY
|     | SELECT |     | INSERT UPDATE | DELETE | Total |
| --- | ------ | --- | ------------- | ------ | ----- |
Project
|                   | TP  | FP  | TP FP TP | FP TP FP | TP FP |
| ----------------- | --- | --- | -------- | -------- | ----- |
| Blog              | 0   | 0   | 0 0 0    | 0 0 0    | 0 0   |
| BookStore         | 0   | 0   | 3 0 3    | 0 3 0    | 9 0   |
| Mall              | 0   | 0   | 0 0 1    | 0 0 0    | 1 0   |
| NewbellMall       | 0   | 0   | 0 0 0    | 0 0 0    | 0 0   |
| IceCms            | 0   | 0   | 3 0 0    | 0 0 0    | 3 0   |
| MusicwWbsite      | 0   | 0   | 4 0 3    | 1 3 0    | 10 1  |
| OnlineExam        | 0   | 0   | 1 0 1    | 1 0 1    | 2 2   |
| UniversityForum   | 0   | 0   | 2 0 0    | 0 0 0    | 2 0   |
| InformationSystem | 0   | 0   | 0 0 0    | 0 0 0    | 0 0   |
| OnlineMall        | 0   | 0   | 0 0 0    | 0 0 0    | 0 0   |
| Total             | 0   | 0   | 13 0 8   | 2 6 1    | 27 3  |
BOLARAYreported2morefalsevulnerabilitiesthanBolaZ.ThisisbecauseBOLARAYperformsauthorization
checkingbasedontheartificiallysummarizedauthorizationmodel,whichwillleadtofailureinsomeapplication
scenarios.Itsauthorizationmodeldoesnotfittheworkflowofthesystem,andwronglydeterminesthecontextbetween
APIs.However,BolaZdefenserulesbasedonthesystem’sbest-practiceauthorizationlogicsolvethesedefects.
Table11. FalsepositivesreportedbyBOLARAY
| Project |             | API |                                 | Description |     |
| ------- | ----------- | --- | ------------------------------- | ----------- | --- |
|         | PUT/student |     | Application-levelAuthorization. |             |     |
OnlineExam
DELETE/student
Application-levelAuthorization.
/studentId
| MusicWebsite | POST/comment/like |     | Column-levelAuthorization. |     |     |
| ------------ | ----------------- | --- | -------------------------- | --- | --- |
Insight#2:CombinedwithBOLARAY’sauthorizationmodels,BolaZcanalleviatefalsenegativescausedby“client
logiccontrol(detailedin3.4.2)".
AnswertoRQ4:ComparedwithBOLARAY,BOLAZnotonlysupportsBOLAvulnerabilitydetectionforalltypes
ofSQLstatements,butalsobreaksthelimitationsoftheartificiallysummarizedauthorizationmodelandhasa
lowerfalsepositiverate.
7 DiscussionandFutureWork
7.1 ThreattoValidity.
Throughourexperiments,weidentifiedcertainlimitationsinBolaZ’sdataflowanalysiswhenthescenariosare
relativelyspecific.First,assystemsgrowmorecomplexinfunctionalityandlogic,itbecomeschallengingtointerpret
client-sidecontrolconditionsusingstaticcodeanalysis.BolaZsometimeswasunabletodeterminewhichresource
IDsproducedbyP-APIsarepassedtoC-APIssolelybyanalyzingconditioncode,particularlyinscenariosinvolving
client-controlleddeletionandmodificationoperations.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 25
Second,duetovaryinglevelsofdeveloperexpertiseandcodingpractices,thesamelogiccanbeimplementedin
numerousways.CodeQLcannotaccommodateallcodingpatterns,leadingtointerruptionsinsomedataflowanalysis
processes.Asaresult,APIidentificationandassociationmayfail,leavingsomeBOLAvulnerabilitiesunaddressed.In
thesecases,BolaZwillnotrestrictsuchAPIs,andthevulnerabilitiesmaypersist.
Third,BolaZiscurrentlyimplementedontheSpringBootframework.Afactisthatthepropagationlogicand
behaviorofresourceIDsremainsconsistentinvariedlanguagesorframeworks.Hence,BolaZisagenericapproachat
themethodologicallevel.
7.2 FutureWork.
First,BolaZcurrentlyonlysupportsdatabases.Inthefuture,weplantoinvestigatethepotentialoftheMSGconcept
inothertypesofstoragesystems.Second,improvementsareneededinBolaZ’sfront-endcodeanalysis.Weaimto
integratedynamicapplicationsecuritytestingtobettercapturethelogicalrelationshipsbetweenP-APIsandC-APIs.
Additionally,toaddressdataflowinterruptionsintainttracking,wewillofferopenprogramminginterfaces,allowing
userstoadaptBolaZtotheirsystem’scodingpatternsthroughcustomizedrules.
8 RelatedWork
8.1 APIAutomatedTesting
MostautomatedtestsforRESTfulAPIsfocusonfunctionaltestsandarenotusedtodetectBOLAvulnerabilities.
However,wecandrawideasfromAPIautomatedtestingmethods.
RestTestGen[45]analyzedtheproducersandconsumersofresourcesintheAPIbasedonOAS.RESTler[3]deduces
producer-consumerdependenciesofresourcesandresourceIDsbasedonOAS.EvoMaster[2]generatestestcasesfor
RESTfulAPIsbyanalyzingthesourcecode.However,EvoMasterbelievesthatuserscanonlyoperateontheresources
theycreate,whichdoesnotapplytoallapplicationscenarios.Atlidakisetal.[4]usedautomatedAPItestingtoverify
whethertheAPIviolatedtheuser-namespacerule.TheruleholdsthattheresourcesproducedbyuserAcannotbe
accessedbyuserB,anddoesnotapplytoallresourcerelationships.Corradinietal.[10]DetectMassAssignment
VulnerabilitiesinRESTfulAPIsusingautomatedblack-boxtesting.Themethodusingcommonnamingpracticesto
identifytheResourceIDisinaccurate.RESTest[28]isanautomatedblack-boxtestingtoolforRESTfulAPIs,which
supportsinferenceofdependenciesbetweenparameters.
8.2 StaticAnlaysis-basedBOLAVulnerabilityDetection
Applicationsourcecodecontainsresourceaccesspatterns,somanytoolsusestaticanalysistechniquestoinferresource’s
authorizationrulesfromthesourcecode.
SPACE[32]requiresdeveloperstoprovideamappingofapplicationresourcestothebasictypesthatoccurinSPACE
catalog.SPACEusessymbolicexecutiontoextractthedataexposuresfromsourcecode.ThenSPACEcheckswhether
eachdataexposureisallowed.Cancheck[5]alsorequiresdeveloperstoprovideauthorizationrulesforresources.
RoleCast[37]commonsoftwareengineeringpatternstodetermineresourceauthorizationpatterns,butRoleCast’s
patternsdonotapplytoallwebapplications.MACE[29]analyzesINSERTstatementstodeterminerelationshipsbetween
usersandresources,butMACEonlysupportstheownershipmodel[18]andcannotdetecttheBOLAvulnerabilityof
SELECTstatements.BOLARAY[18]combinesSQLandstaticanalysistoautomaticallyidentifyBOLAvulnerabilitiesin
database-backedapplications.However,BOLARAYalsorequiresdeveloperstomarkDALspecifications,anddoesnot
ManuscriptsubmittedtoACM

26 AnbinWuetal.
supportthedetectionofBOLAvulnerabilitiesinSELECTstatements.TheprincipleofMOCGuard[26]andBOLARAY
todetectBOLAvulnerabilitiesishighlysimilar.Theyarebasedonhuman-summarizedauthorizationmodelsanduse
therelationshipbetweenthedatabasetablescorrespondingtotheresourcestoinferwhethertheuserhaspermissionto
accessthecorrespondingresources.ThefourauthorizationmodelssummarizedbyBOLARAYaremorecomprehensive
thanMOCGuardandcovermorescenarios.Similarly,MOCGuardalsocannothandlethedynamicauthorizationlogic
ofunknownsystemsduetothestaticnatureoftheartificiallysummarizedauthorizationmodel.
8.3 RuntimeMonitoring
Therearealsosomeworkstoenforceaccesscontrolatsystemruntime.Nemesis[14]ensuresthatonlyauthenticated
userscanaccessresourcesunderthemanualauthorizationpolicy.FlowWatcher[31]foundthattheaccesscontrol
patternofresourcesinmostwebapplicationsissimilar.Therefore,FlowWatcherrequiresdeveloperstoprovidean
accesspolicytodetectwhetherthepolicyisviolatedduringsystemruntime.
9 Conclusions
ThispaperproposesadefenseframeworkforBOLAattacks,BolaZ,basedonzerotrust.Theframeworkusesstatic
tainttrackingtechnologytoobtainpropagationdataflowsofresourceIDsanddeterminesAPIs’roleaccordingtothe
productionandconsumptionofresourceIDs.TocapturethecontextsemanticrelationshipbetweenP-APIsandC-APIs,
BolaZalsotracksthepropagationpathofresourceIDsbetweenAPIs.ExperimentsshowthatBolaZcaneffectively
identifyandcorrelateAPIs,low-performanceoverhead,andhighsecurityinmulti-APIvulnerabilityscenarios.
Acknowledgments
ThisworkissupportedbytheNationalNaturalScienceFoundationofChinaunderGrant62372323.
References
[1] akamai.2024.owasps-top-10-api-security-risks.akamai(2024). https://www.akamai.com/site/zh/documents/white-paper/2023/owasps-top-10-api-
security-risks.pdf
[2] AndreaArcuri.2019.RESTfulAPIautomatedtestcasegenerationwithEvoMaster.ACMTransactionsonSoftwareEngineeringandMethodology
(TOSEM)28,1(2019),1–37. Publisher:ACMNewYork,NY,USA.
[3] VaggelisAtlidakis,PatriceGodefroid,andMarinaPolishchuk.2019.Restler:Statefulrestapifuzzing.In2019IEEE/ACM41stInternationalConference
onSoftwareEngineering(ICSE).IEEE,748–758.
[4] VaggelisAtlidakis,PatriceGodefroid,andMarinaPolishchuk.2020.CheckingsecuritypropertiesofcloudserviceRESTAPIs.In2020IEEE13th
InternationalConferenceonSoftwareTesting,ValidationandVerification(ICST).IEEE,387–397.
[5] IvanBocicandTevfikBultan.2016.FindingaccesscontrolbugsinwebapplicationswithCanCheck.201631stIEEE/ACMInternationalConferenceon
AutomatedSoftwareEngineering(ASE)(2016),155–166. https://api.semanticscholar.org/CorpusID:2890296
[6] boylegu.2023.InformationSystem. https://github.com/boylegu/SpringBoot-vue
[7] MarkCampbell.2020.Beyondzerotrust:Trustisavulnerability.Computer53,10(2020),110–113. Publisher:IEEE.
[8] CodeQL.2024.CodeQL. https://github.com/github/codeql
[9] CodeQL.2024.globaltainttracking. https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-java/
[10] DavideCorradini,MichelePasqua,andMarianoCeccato.2023.Automatedblack-boxtestingofmassassignmentvulnerabilitiesinRESTfulAPIs.In
2023IEEE/ACM45thInternationalConferenceonSoftwareEngineering(ICSE).IEEE,2553–2564.
[11] cp3geek.2022.universityforum. https://github.com/cp3geek/universityforum
[12] CVE.2023.CVE-2023-32310.TechnicalReport. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32310
[13] CVE.2023.CVE-2023-36100.TechnicalReport. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36100
[14] MichaelDalton,ChristosKozyrakis,andNickolaiZeldovich.2009.Nemesis:PreventingAuthentication&AccessControlVulnerabilitiesinWeb
Applications.InUSENIXSecuritySymposium. https://api.semanticscholar.org/CorpusID:15907882
[15] DickHardt.2012.TheOAuth2.0AuthorizationFramework. https://tools.ietf.org/html/rfc6749
[16] RoyThomasFielding.2000.Architecturalstylesandthedesignofnetwork-basedsoftwarearchitectures.UniversityofCalifornia,Irvine.
ManuscriptsubmittedtoACM

RethinkingBrokenObjectLevelAuthorizationAttacksUnderZeroTrustPrinciple 27
[17] MahmoudGhorbanzadehandHamidRezaShahriari.2020.ANOVUL:Detectionoflogicvulnerabilitiesinannotatedprogramsviadataandcontrol
flowanalysis.IETInformationSecurity14,3(2020),352–364. Publisher:WileyOnlineLibrary.
[18] YonghengHuang,ChenghangShi,JieLu,HaofengLi,HainingMeng,andLianLi.2024.DetectingBrokenObject-LevelAuthorizationVulnerabilities
inDatabase-BackedApplications.InProceedingsofthe2024onACMSIGSACConferenceonComputerandCommunicationsSecurity.2934–2948.
[19] MuhammadIdris,IwanSyarif,andIdrisWinarno.2021.DevelopmentofvulnerablewebapplicationbasedonOWASPAPIsecurityrisks.In2021
InternationalElectronicsSymposium(IES).IEEE,190–194.
[20] SamuelJero,JulianaFurgala,RunyuPan,PhaniKishoreGadepalli,AlexandraClifford,BiteYe,RogerKhazan,BryanCWard,GabrielParmer,and
RichardSkowyra.2021.Practicalprincipleofleastprivilegeforsecureembeddedsystems.In2021IEEE27thReal-TimeandEmbeddedTechnology
andApplicationsSymposium(RTAS).IEEE,1–13.
[21] Jmeter.2024.Jmeter. https://jmeter.apache.org/
[22] JWT.2015.JSONWebToken. http://www.rfc-editor.org/rfc/rfc7519
[23] SreejithKeeriyattilandSreejithKeeriyattil.2019.Microsegmentationandzerotrust:Introduction.ZeroTrustNetworkswithVMwareNSX:Build
HighlySecureNetworkArchitecturesforYourDataCenters(2019),17–31. Publisher:Springer.
[24] JunhyoungKim,TaeGuenKim,andEulGyuIm.2014. Surveyofdynamictaintanalysis.In20144thIEEEInternationalConferenceonNetwork
InfrastructureandDigitalContent.269–272.doi:10.1109/ICNIDC.2014.7000307
[25] libhunt.2025.Open-sourceprojectscategorizedasspring-boot. https://www.libhunt.com/topic/spring-boot
[26] FengyuLiu,YoukunShi,YuanZhang,GuangliangYang,EnhaoLi,andMinYang.2025.MOCGuard:AutomaticallyDetectingMissing-Owner-Check
VulnerabilitiesinJavaWebApplications.In2025IEEESymposiumonSecurityandPrivacy(SP).903–919.doi:10.1109/SP61157.2025.00010
[27] macrozheng.2024.mall. https://github.com/macrozheng/mall
[28] AlbertoMartin-Lopez,SergioSegura,andAntonioRuiz-Cortés.2020. RESTest:Black-boxconstraint-basedtestingofRESTfulwebAPIs.In
Service-OrientedComputing:18thInternationalConference,ICSOC2020,Dubai,UnitedArabEmirates,December14–17,2020,Proceedings18.Springer,
459–475.
[29] MalihehMonshizadeh,PrasadNaldurg,andVNVenkatakrishnan.2014.Mace:Detectingprivilegeescalationvulnerabilitiesinwebapplications.In
Proceedingsofthe2014ACMSIGSACConferenceonComputerandCommunicationsSecurity.690–701.
[30] MQPearth.2024.Blog. https://github.com/MQPearth/Blog
[31] DivyaMuthukumaran,DanO’Keeffe,ChristianPriebe,DavidEyers,BrianShand,andPeterPietzuch.2015. FlowWatcher:Defendingagainst
datadisclosurevulnerabilitiesinwebapplications.InProceedingsofthe22ndACMSIGSACConferenceonComputerandCommunicationsSecurity.
603–615.
[32] JosephPNearandDanielJackson.2016.Findingsecuritybugsinwebapplicationsusingacatalogofaccesscontrolpatterns.InProceedingsofthe
38thInternationalConferenceonSoftwareEngineering.947–958.
[33] newbee-ltd/.2024.newbee-mall. https://github.com/newbee-ltd/newbee-mall-api
[34] OWASPAPISecurity.2023.OWASPAPISecurityProject. https://owasp.org/www-project-api-security/
[35] MayraSamaniegoandRalphDeters.2018.Zero-trusthierarchicalmanagementinIoT.In2018IEEEinternationalcongressonInternetofThings
(ICIOT).IEEE,88–95.
[36] SailikSengupta,AnkurChowdhary,AbdulhakimSabur,AdelAlshamrani,DijiangHuang,andSubbaraoKambhampati.2020.Asurveyofmoving
targetdefensesfornetworksecurity.IEEECommunicationsSurveys&Tutorials22,3(2020),1909–1941. Publisher:IEEE.
[37] SooelSon,KathrynMcKinley,andVitalyShmatikov.2011.RoleCast:FindingMissingSecurityChecksWhenYouDoNotKnowWhatChecksAre.
InSigplanNotices-SIGPLAN,Vol.46.1069–1084.doi:10.1145/2076021.2048146
[38] sourcecodeexamples.2025.sourcecodeexamples. https://www.sourcecodeexamples.net/
[39] spring-projects.2025.spring-bootdependencygraph. https://github.com/spring-projects/spring-boot/network/dependents
[40] StuHaiBin.2020.BookStore. https://github.com/StuHaiBin/bookStore-Springboot-Vue
[41] tablu666.2020.onlinemall. https://github.com/tablu666/springboot-vue-online-mall
[42] GonçaloAndréCarneiroTeixeira.2023.SecurityTestingofWebAPIs.(2023).
[43] telerik.2024.Fiddler. https://www.telerik.com/fiddler-b
[44] Thecosy.2024.IceCMS. https://github.com/Thecosy/IceCMS
[45] EmanueleViglianisi,MichaelDallago,andMarianoCeccato.2020. Resttestgen:automatedblack-boxtestingofrestfulapis.In2020IEEE13th
InternationalConferenceonSoftwareTesting,ValidationandVerification(ICST).IEEE,142–152.
[46] Yin-Hongwei.2024.music-website. https://github.com/Yin-Hongwei/music-website
[47] YXJ2018.2024.SpringBoot-Vue-OnlineExam. https://github.com/YXJ2018/SpringBoot-Vue-OnlineExam
[48] ManZhang,BogdanMarculescu,andAndreaArcuri.2021.ResourceanddependencybasedtestcasegenerationforRESTfulWebservices.Empirical
SoftwareEngineering26,4(2021),76. Publisher:Springer.
ManuscriptsubmittedtoACM