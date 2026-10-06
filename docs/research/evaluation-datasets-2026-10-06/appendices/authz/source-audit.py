import ast,hashlib,json,subprocess
from pathlib import Path
root=Path(r'C:\Users\andyw\Desktop\AP-EYE\local-materials\evaluation-review-2026-10-06\authz')
out=root/'evidence'
def method(path,cls,func):
    tree=ast.parse(path.read_text('utf-8'));c=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name==cls)
    node=next(x for x in c.body if isinstance(x,ast.FunctionDef) and x.name==func)
    return {'start_line':node.lineno,'end_line':node.end_lineno,'source':ast.unparse(node)}
audit={'scope':'Static source audit, NOT service execution','nutrition':[],'repetition_at_idor_guard_pin':[]}
for cls in ['NutritionPlanViewSet','MealViewSet','MealItemViewSet']:
    audit['nutrition'].append({'class':cls,'before':method(out/'wger-vulnerable-nutrition-views.py',cls,'nutritional_values'),'after':method(out/'wger-fixed-nutrition-views.py',cls,'nutritional_values')})
for cls in ['RepetitionsConfigViewSet','MaxRepetitionsConfigViewSet']:
    audit['repetition_at_idor_guard_pin'].append({'class':cls,'method':method(out/'wger-vulnerable-manager-views.py',cls,'get_queryset')})
(out/'wger-source-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
repos=[]
for name in ['bolaz','IDOR-GUARD','restler-fuzzer']:
    repos.append({'name':name,'commit':subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip(),'remote':subprocess.check_output(['git','-C',str(root/name),'remote','get-url','origin'],text=True).strip()})
papers=['IDORacle_2609.12426','BolaZ_2507.02309','BACFuzz_2507.15984','ICST2020_REST-API-security-rules','AuthScope_CCS17','TrafficAuthzRisk_2607.16754']
base=Path(r'C:\Users\andyw\Desktop\AP-EYE\team_hub\docs\papers')
manifest={'investigation_date':'2026-10-06','repos':repos,'papers':[{'name':name,'sha256':hashlib.sha256((base/(name+'.pdf')).read_bytes()).hexdigest(),'page_count':len(json.loads((out/(name+'-pages.json')).read_text('utf-8')))} for name in papers],'local_outputs':[{'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(out.iterdir()) if p.is_file() and p.suffix in ['.json','.py']]}
(out/'review-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('manifest',len(manifest['papers']),'papers',len(repos),'repos')
print('source audit:',len(audit['nutrition']),'nutrition before/after methods;',len(audit['repetition_at_idor_guard_pin']),'already filtered list methods')
