import json

def print_errors(errors, as_json=False):
    if as_json:
        print(json.dumps({'valid': not errors, 'errors': errors}, indent=2)); return
    if not errors:
        print('✅ Config valid'); return
    print(f"❌ {len(errors)} validation error(s)")
    for e in errors:
        print(f"- {e['path']}: {e['message']} ({e['validator']})")
