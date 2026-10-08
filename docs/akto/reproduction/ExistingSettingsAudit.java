import com.akto.DaoInit;
import com.akto.dao.*;
import com.akto.dao.context.Context;
import com.akto.dto.*;
import com.akto.dto.data_types.*;
import com.akto.dto.type.*;
import com.akto.dto.test_editor.*;
import com.akto.test_editor.filter.Filter;
import com.akto.dao.test_editor.filter.ConfigParser;
import com.mongodb.*;
import com.mongodb.client.model.Filters;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import java.util.*;
import java.nio.file.*;

public class ExistingSettingsAudit {
 static ObjectMapper mapper=new ObjectMapper();
 static void check(boolean condition,String message){if(!condition)throw new AssertionError(message);}
 static Conditions regex(String expression){return new Conditions(Arrays.<Predicate>asList(new RegexPredicate(expression)),Conditions.Operator.AND);}
 static CustomDataType type(String name,String key,String value){
  return new CustomDataType(name,true,new ArrayList<SingleTypeInfo.Position>(),1,true,regex(key),regex(value),Conditions.Operator.AND,new IgnoreData(new HashMap<>(),new HashSet<>()),false,false);
 }
 static RawApi api(String body){
  return new RawApi(new OriginalHttpRequest("https://audit.invalid/items","","GET","{}",new HashMap<String,List<String>>(),"HTTP/1.1"),new OriginalHttpResponse(body,new HashMap<String,List<String>>(),200),"");
 }
 static boolean validate(Object config,RawApi original,RawApi current){
  ConfigParserResult parsed=new ConfigParser().parse(config);
  check(parsed.getNode()!=null,"Parser node missing");
  return new Filter().isEndpointValid(parsed.getNode(),original,current,new ApiInfo.ApiInfoKey(99105,"https://audit.invalid/items",URLMethods.Method.GET),null,null,false,"validate",new HashMap<String,Object>(),"audit",false).getResult();
 }
 public static void main(String[] args){
  try{run(args);System.exit(0);}catch(Throwable t){t.printStackTrace();System.exit(1);}
 }
 static void run(String[] args)throws Exception{
  DaoInit.init(new ConnectionString("mongodb://127.0.0.1:27105"),ReadPreference.primary(),WriteConcern.ACKNOWLEDGED);Context.accountId.set(20261005);
  CustomDataTypeDao.instance.deleteAll(Filters.in("name",Arrays.asList("AUDIT_KR_RRN_FORMAT","AUDIT_KR_PHONE")));
  SingleTypeInfo.fetchCustomDataTypes(20261005);
  String[][] inputs={
   {"rrn_hyphen","주민등록번호","000000-0000000","AUDIT_KR_RRN_FORMAT"},
   {"rrn_digits","rrn","0000000000000","AUDIT_KR_RRN_FORMAT"},
   {"order_digits","order_id","0000000000000",""},
   {"masked_rrn","주민등록번호","[REDACTED]",""},
   {"domestic_phone","휴대전화","010-1234-5678","AUDIT_KR_PHONE"},
   {"digits_phone","phone","01012345678","AUDIT_KR_PHONE"},
   {"order_phone","order_id","01012345678",""},
   {"international_phone","phone","+821012345678",""},
   {"short_phone","phone","010-123-4567",""},
   {"rrn_in_sentence","주민등록번호","번호는 000000-0000000입니다.",""}
  };
  Map<String,String> before=new HashMap<>();
  for(String[] p:inputs){before.put(p[0],KeyTypes.findSubType(p[2],p[1],null,true).getName());}
  CustomDataTypeDao.instance.insertOne(type("AUDIT_KR_RRN_FORMAT","^(?:주민등록번호|resident_registration_number|rrn)$","^[0-9]{6}-?[0-9]{7}$"));
  CustomDataTypeDao.instance.insertOne(type("AUDIT_KR_PHONE","^(?:휴대전화|전화번호|phone|mobile)$","^010-?[0-9]{4}-?[0-9]{4}$"));
  SingleTypeInfo.fetchCustomDataTypes(20261005);
  List<Map<String,Object>> privacy=new ArrayList<>();
  for(String[] p:inputs){
   String after=KeyTypes.findSubType(p[2],p[1],null,true).getName();
   check(p[3].isEmpty()?!after.startsWith("AUDIT_KR_"):after.equals(p[3]),p[0]);
   Map<String,Object> row=new LinkedHashMap<>();row.put("case",p[0]);row.put("key",p[1]);row.put("synthetic_value",p[2]);row.put("before",before.get(p[0]));row.put("after",after);privacy.add(row);
  }
  for(int length:new int[]{2,8193}){
   KeyTypes kt=new KeyTypes(new HashMap<SingleTypeInfo.SubType,SingleTypeInfo>(),false);
   String raw=length==2?"{}":"{\"padding\":\""+new String(new char[length-14]).replace('\0','x')+"\"}";
   check(raw.length()==length,"sample length");mapper.readTree(raw);
   kt.process("https://audit.invalid/items","GET",200,false,"휴대전화","010-1234-5678","user-a",99105,raw,new HashMap<SensitiveParamInfo,Boolean>(),false,1);
   String found=kt.getAllTypeInfo().get(0).getSubType().getName();
   check(found.equals(length==2?"AUDIT_KR_PHONE":"GENERIC"),"raw message length");
   Map<String,Object> row=new LinkedHashMap<>();row.put("case","raw_message_length");row.put("length",length);row.put("runtime_type",found);privacy.add(row);
  }
  Path out=Paths.get(args[1]);Files.createDirectories(out);
  mapper.writerWithDefaultPrettyPrinter().writeValue(out.resolve("2026-10-05-korean-settings.json").toFile(),privacy);
  Map<?,?> template=new ObjectMapper(new YAMLFactory()).readValue(Paths.get(args[0]).toFile(),Map.class);
  Object normal=template.get("validate");
  Map<String,Object> markerConfig=new LinkedHashMap<>();
  markerConfig.put("response_code",new BasicDBObject("gte",200).append("lt",300));
  markerConfig.put("response_payload",new BasicDBObject("contains_all",Arrays.asList("protected-marker")));
  String[][] responses={
   {"empty_array","[]","[]"},
   {"empty_object","{}","{}"},
   {"empty_wrapper","{\"data\":[]}","{\"data\":[]}"},
   {"shared","[{\"id\":\"shared-a\",\"text\":\"allowed\"}]","[{\"id\":\"shared-a\",\"text\":\"allowed\"}]"},
   {"forbidden","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]"},
   {"filtered","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[]"},
   {"different_allowed","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"public-b\",\"text\":\"allowed\"}]"},
   {"mixed","[{\"id\":\"private-a\",\"text\":\"protected-marker\"}]","[{\"id\":\"public-b\",\"text\":\"allowed\"},{\"id\":\"private-a\",\"text\":\"protected-marker\"}]"},
   {"association_swapped","[{\"id\":\"a\",\"text\":\"x\"},{\"id\":\"b\",\"text\":\"y\"}]","[{\"id\":\"a\",\"text\":\"y\"},{\"id\":\"b\",\"text\":\"x\"}]"}
  };
  List<Map<String,Object>> results=new ArrayList<>();
  for(String[] p:responses){
   boolean baseline=validate(normal,api(p[1]),api(p[2]));
   boolean marker=validate(markerConfig,api(p[1]),api(p[2]));
   check(marker==(p[0].equals("forbidden")||p[0].equals("mixed")),"marker "+p[0]);
   Map<String,Object> r=new LinkedHashMap<>();r.put("case",p[0]);r.put("original",p[1]);r.put("current",p[2]);r.put("template_validate",baseline);r.put("existing_contains_all_setting",marker);results.add(r);
  }
  mapper.writerWithDefaultPrettyPrinter().writeValue(out.resolve("2026-10-05-list-validation-settings.json").toFile(),results);
  mapper.writerWithDefaultPrettyPrinter().writeValue(out.resolve("2026-10-05-marker-validate-config.json").toFile(),markerConfig);
  CustomDataTypeDao.instance.deleteAll(Filters.in("name",Arrays.asList("AUDIT_KR_RRN_FORMAT","AUDIT_KR_PHONE")));MCollection.clients[0].close();
  System.out.println("Korean settings: 12 inputs; list validation: 9 inputs. Assertions passed.");
 }
}
