"""Rebuild the standalone, offline viewer from the curated family dataset."""
from pathlib import Path
import json
p=Path(__file__).parent
data=json.loads((p/'master_family.json').read_text(encoding='utf8'))
template=(p/'viewer_template.html').read_text(encoding='utf8')
assert template.count('__FAMILY_DATA__')==1
output=template.replace('__FAMILY_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
(p/'family_tree.html').write_text(output,encoding='utf8')
