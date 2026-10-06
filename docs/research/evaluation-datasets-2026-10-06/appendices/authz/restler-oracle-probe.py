import ast,json,hashlib
from pathlib import Path
from types import SimpleNamespace
root=Path(r'C:\Users\andyw\Desktop\AP-EYE\local-materials\evaluation-review-2026-10-06\authz')
repo=root/'restler-fuzzer'
methods=[]
for f,c,m in [('restler/checkers/checker_base.py','CheckerBase','_rule_violation'),('restler/checkers/namespace_rule_checker.py','NameSpaceRuleChecker','_false_alarm')]:
    source=(repo/f).read_text('utf-8'); tree=ast.parse(source)
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==c)
    node=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==m)
    methods.append(node)
module=ast.fix_missing_locations(ast.Module(body=[ast.ClassDef(name='PinnedOriginalMethods',bases=[],keywords=[],body=methods,decorator_list=[])],type_ignores=[]))
namespace={};exec(compile(module,'<unmodified-upstream-methods>','exec'),namespace)
checker=namespace['PinnedOriginalMethods']()
class Response:
    def __init__(self,status,body):self.status=status;self.body=body
    def has_valid_code(self):return 200<=self.status<300
    def has_bug_code(self):return 500<=self.status<600
seq=SimpleNamespace(last_request=SimpleNamespace(method='GET'))
cases=[('bare_empty',200,'[]','NORMAL'),('spaced_empty',200,'[ ]','NORMAL'),('newline_empty',200,'[\n]','NORMAL'),('wrapped_empty',200,'{"results": [], "count": 0}','NORMAL'),('own_only_list',200,'{"items":[{"id":"own_1"}]}','NORMAL'),('public_list',200,'{"items":[{"id":"public_1"}]}','NORMAL'),('foreign_private_list',200,'{"items":[{"id":"foreign_private_1"}]}','BOLA'),('forbidden',403,'{"error":"forbidden"}','NORMAL'),('missing',404,'{}','NORMAL'),('server_error',500,'{}','INDETERMINATE')]
results=[{'case_id':n,'status':s,'response_body':b,'fixture_truth':t,'upstream_rule_reports_violation':checker._rule_violation(seq,Response(s,b))} for n,s,b,t in cases]
out={'scope':'Component probe of two unmodified source methods; synthetic responses; NOT end-to-end RESTler execution and NOT a dataset accuracy estimate','commit':'6d984deedbc54aad957fa3da0c7e9e5df23a2aee','cases':results}
(root/'evidence/restler-oracle-component-probe.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
