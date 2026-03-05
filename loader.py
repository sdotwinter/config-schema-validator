import json
from pathlib import Path
import yaml

def load_doc(path: Path):
    text = path.read_text(encoding='utf-8')
    if path.suffix.lower() in ('.yaml', '.yml'):
        return yaml.safe_load(text)
    return json.loads(text)
