import json,subprocess,base64
from pathlib import Path
out=Path(r'C:\Users\andyw\Desktop\AP-EYE\local-materials\evaluation-review-2026-10-06\authz\evidence')
for ref,label in [('a912c313b8fec21469ff47e6f51a1040d03c92e8','wger-vulnerable'),('29876a1954fe959e4b58ef070170e81703dab60e','wger-fixed')]:
    for path,short in [('wger/nutrition/api/views.py','nutrition-views'),('wger/manager/api/views.py','manager-views')]:
        data=json.loads(subprocess.check_output(['gh','api',f'repos/wger-project/wger/contents/{path}?ref={ref}'],text=True,encoding='utf-8'))
        text=base64.b64decode(data['content']).decode('utf-8')
        (out/f'{label}-{short}.py').write_text(text,encoding='utf-8')
        print(label,short,len(text))
