import pathlib,json,importlib.util,os
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=pathlib.Path(os.environ.get('AP_EYE_KPII_SOURCE',ROOT/'sources'/'k-pii-bench'))/'src'/'k_pii_bench'/'evaluation'/'metrics'/'span_metrics.py'
spec=importlib.util.spec_from_file_location('audited_span_metrics',SOURCE)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
gold=[[{'type':'PERSON','surface':'홍길동','start':0,'end':3},{'type':'PERSON','surface':'홍길동','start':10,'end':13}]]
pred=[[{'type':'PERSON','text':'홍길동','start':10,'end':13}]]
out={'case':'one_of_two_occurrences_detected','source_module':str(SOURCE),'helper_result':module.compute_span_metrics(gold,pred,['홍길동']),'actual_character_exact_expected':{'tp':1,'fp':0,'fn':1,'precision':1.0,'recall':0.5,'f1':2/3},'scope':'This helper is not the official seqeval CLI; do not attribute helper behavior to all scorers.'}
(ROOT/'evidence'/'kpii-scorer-probe.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
