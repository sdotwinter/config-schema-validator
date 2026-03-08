import json, yaml
from pathlib import Path

def load_doc(path):
    p=Path(path)
    txt=p.read_text(encoding='utf-8')
    if p.suffix.lower() in ('.yaml','.yml'):
        return yaml.safe_load(txt)
    return json.loads(txt)
