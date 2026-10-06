import java.util.*;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.node.*;
public class BolaProbe {
static ObjectMapper mapper=new ObjectMapper(); static JsonFactory factory=mapper.getFactory();
public static void extractAllValuesFromPayload(String payload, Map<String,Set<String>> payloadMap) throws Exception{
        JsonParser jp = factory.createParser(payload);
        JsonNode node = mapper.readTree(jp);
        extractAllValuesFromPayload(node,new ArrayList<>(),payloadMap);
    }
public static void extractAllValuesFromPayload(JsonNode node, List<String> params, Map<String, Set<String>> values) {
        // TODO: null values remove
        if (node == null) return;
        if (node.isValueNode()) {
            String textValue = node.asText();
            if (textValue != null) {
                String param = String.join("",params);
                if (param.startsWith("#")) {
                    param = param.substring(1);
                }
                if (!values.containsKey(param)) {
                    values.put(param, new HashSet<>());
                }
                values.get(param).add(textValue);
            }
        } else if (node.isArray()) {
            ArrayNode arrayNode = (ArrayNode) node;
            for(int i = 0; i < arrayNode.size(); i++) {
                JsonNode arrayElement = arrayNode.get(i);
                params.add("#$");
                extractAllValuesFromPayload(arrayElement, params, values);
                params.remove(params.size()-1);
            }
        } else {
            Iterator<String> fieldNames = node.fieldNames();
            while(fieldNames.hasNext()) {
                String fieldName = fieldNames.next();
                params.add("#"+fieldName);
                JsonNode fieldValue = node.get(fieldName);
                extractAllValuesFromPayload(fieldValue, params,values);
                params.remove(params.size()-1);
            }
        }

    }
public static double compareWithOriginalResponse(String originalPayload, String currentPayload, Map<String, Boolean> comparisonExcludedKeys) {
        if (originalPayload == null && currentPayload == null) return 100;
        if (originalPayload == null || currentPayload == null) return 0;

        String trimmedOriginalPayload = originalPayload.trim();
        String trimmedCurrentPayload = currentPayload.trim();
        if (trimmedCurrentPayload.equals(trimmedOriginalPayload)) return 100;

        Map<String, Set<String>> originalResponseParamMap = new HashMap<>();
        Map<String, Set<String>> currentResponseParamMap = new HashMap<>();
        try {
            extractAllValuesFromPayload(originalPayload, originalResponseParamMap);
            extractAllValuesFromPayload(currentPayload, currentResponseParamMap);
        } catch (Exception e) {
            return 0.0;
        }

        if (originalResponseParamMap.keySet().size() == 0 && currentResponseParamMap.keySet().size() == 0) {
            return 100.0;
        }

        Set<String> visited = new HashSet<>();
        int matched = 0;
        for (String k1: originalResponseParamMap.keySet()) {
            if (visited.contains(k1) || comparisonExcludedKeys.containsKey(k1)) continue;
            visited.add(k1);
            Set<String> v1 = originalResponseParamMap.get(k1);
            Set<String> v2 = currentResponseParamMap.get(k1);
            if (Objects.equals(v1, v2)) matched +=1;
        }

        for (String k1: currentResponseParamMap.keySet()) {
            if (visited.contains(k1) || comparisonExcludedKeys.containsKey(k1)) continue;
            visited.add(k1);
            Set<String> v1 = originalResponseParamMap.get(k1);
            Set<String> v2 = currentResponseParamMap.get(k1);
            if (Objects.equals(v1, v2)) matched +=1;
        }

        int visitedSize = visited.size();
        if (visitedSize == 0) return 0.0;

        double result = (100.0*matched)/visitedSize;

        if (Double.isFinite(result)) {
            return result;
        } else {
            return 0.0;
        }

    }
public static void main(String[] args) {
System.out.println("same_object\t"+compareWithOriginalResponse("{\"id\":1,\"label\":\"alpha\"}","{\"id\":1,\"label\":\"alpha\"}",new HashMap<>()));
System.out.println("different_private_value\t"+compareWithOriginalResponse("{\"id\":1,\"label\":\"alpha\"}","{\"id\":2,\"label\":\"alpha\"}",new HashMap<>()));
System.out.println("array_association_lost\t"+compareWithOriginalResponse("[{\"id\":1,\"label\":\"alpha\"},{\"id\":2,\"label\":\"beta\"}]","[{\"id\":1,\"label\":\"beta\"},{\"id\":2,\"label\":\"alpha\"}]",new HashMap<>()));
System.out.println("extra_object_preserves_original_leak\t"+compareWithOriginalResponse("[{\"id\":1,\"label\":\"alpha\"}]","[{\"id\":1,\"label\":\"alpha\"},{\"id\":2,\"label\":\"beta\"}]",new HashMap<>()));
System.out.println("number_vs_string\t"+compareWithOriginalResponse("{\"id\":1}","{\"id\":\"1\"}",new HashMap<>()));
System.out.println("90pct_common_metadata\t"+compareWithOriginalResponse("{\"id\":1,\"m0\":\"shared\",\"m1\":\"shared\",\"m2\":\"shared\",\"m3\":\"shared\",\"m4\":\"shared\",\"m5\":\"shared\",\"m6\":\"shared\",\"m7\":\"shared\",\"m8\":\"shared\"}","{\"id\":2,\"m0\":\"shared\",\"m1\":\"shared\",\"m2\":\"shared\",\"m3\":\"shared\",\"m4\":\"shared\",\"m5\":\"shared\",\"m6\":\"shared\",\"m7\":\"shared\",\"m8\":\"shared\"}",new HashMap<>()));
}}