package com.akto.test_editor.filter;
import com.akto.DaoInit;
import com.akto.dao.MCollection;
import com.akto.dao.SingleTypeInfoDao;
import com.akto.dao.context.Context;
import com.akto.dto.ApiInfo;
import com.akto.dto.OriginalHttpRequest;
import com.akto.dto.type.SingleTypeInfo;
import com.akto.dto.type.URLMethods;
import com.akto.types.CappedSet;
import com.mongodb.*;
import com.mongodb.client.model.Filters;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
import java.nio.file.*;

public class UrlPrivateContextAuditTest {
  @Test public void auditDatabaseUrlBranch() throws Exception {
    String uri=System.getProperty("audit.mongo","mongodb://127.0.0.1:27105");
    if(!uri.equals("mongodb://127.0.0.1:27105")) throw new IllegalArgumentException("Isolated audit DB only");
    DaoInit.init(new ConnectionString(uri), ReadPreference.primary(), WriteConcern.ACKNOWLEDGED);
    Context.accountId.set(20261005);
    String variant=System.getProperty("audit.variant","baseline");
    List<Map<String,Object>> rows=new ArrayList<>();
    String[] cases={"public_values","private_values","private_empty","private_null_values","zero_observations","missing","two_variables","static_url"};
    for(String id:cases){
      String url=id.equals("two_variables")?"https://audit.invalid/items/STRING/sub/STRING":id.equals("static_url")?"https://audit.invalid/items/fixed":"https://audit.invalid/items/STRING";
      ApiInfo.ApiInfoKey key=new ApiInfo.ApiInfoKey(99105,url,URLMethods.Method.GET);
      SingleTypeInfoDao.instance.deleteAll(Filters.eq("apiCollectionId",99105));
      if(!id.equals("missing")&&!id.equals("static_url")){
        SingleTypeInfo sti=new SingleTypeInfo();
        sti.setApiCollectionId(99105);sti.setUrl(url);sti.setMethod("GET");sti.setResponseCode(-1);sti.setParam("4");sti.setIsUrlParam(true);sti.setSubType(SingleTypeInfo.GENERIC);
        sti.uniqueCount=id.equals("zero_observations")?0:10;
        sti.publicCount=(id.equals("public_values")||id.equals("two_variables"))?10:0;
        sti.setValues(id.equals("private_null_values")?null:id.equals("private_empty")||id.equals("zero_observations")?new CappedSet<String>():CappedSet.create("observed-value"));
        SingleTypeInfoDao.instance.insertOne(sti);
        if(id.equals("two_variables")){
          SingleTypeInfo second=new SingleTypeInfo();second.setApiCollectionId(99105);second.setUrl(url);second.setMethod("GET");second.setResponseCode(-1);second.setParam("6");second.setIsUrlParam(true);second.setSubType(SingleTypeInfo.GENERIC);second.uniqueCount=10;second.publicCount=0;second.setValues(CappedSet.create("second-observed"));
          SingleTypeInfoDao.instance.insertOne(second);
        }
      }
      SingleTypeInfo read=FilterAction.querySti("4",true,key,false,-1);
      String requestUrl=url.replaceFirst("STRING","request-value").replace("STRING","second-request");
      OriginalHttpRequest req=new OriginalHttpRequest(requestUrl,"","GET","{}",new HashMap<String,List<String>>(),"HTTP/1.1");
      BasicDBObject result=new FilterAction().getPrivateResourceCount(req,key);
      Map<String,Object> row=new LinkedHashMap<>();
      row.put("case",id);row.put("sti_found",read!=null);row.put("observed_private",read==null?null:read.getIsPrivate());row.put("result",result);
      int expected;
      if(id.equals("static_url")) expected=0;
      else if(variant.equals("baseline")) expected=id.equals("two_variables")?4:2;
      else if(variant.equals("remove_overwrite_only")) expected=id.equals("private_empty")||id.equals("private_null_values")||id.equals("zero_observations")?2:id.equals("two_variables")?2:1;
      else expected=id.equals("public_values")?0:1;
      assertEquals(expected,((Number)result.get("privateCount")).intValue(),id);
      List<?> values=(List<?>)result.get("values");
      if(id.equals("public_values")&&variant.equals("candidate")) assertTrue(values.isEmpty());
      if(id.equals("private_values")&&!variant.equals("baseline")) assertEquals("observed-value",((BasicDBObject)values.get(0)).get("value"));
      if(id.equals("private_values")&&variant.equals("baseline")) assertEquals("request-value",((BasicDBObject)values.get(0)).get("value"));
      rows.add(row);
    }
    Map<String,Object> output=new LinkedHashMap<>();output.put("variant",variant);output.put("scope","real FilterAction, querySti, DAO and MongoDB; not dashboard or complete YAML test");output.put("cases",rows);
    Path target=Paths.get(System.getProperty("audit.output"));Files.createDirectories(target.getParent());new ObjectMapper().writerWithDefaultPrettyPrinter().writeValue(target.toFile(),output);
    SingleTypeInfoDao.instance.deleteAll(Filters.eq("apiCollectionId",99105));MCollection.clients[0].close();
  }
}
