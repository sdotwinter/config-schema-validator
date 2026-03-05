import argparse
from pathlib import Path
from loader import load_doc
from validator import validate_config
from reporter import print_errors

def run(argv=None):
    p=argparse.ArgumentParser(prog='config-schema-validator', description='Validate config files with JSON Schema.')
    sub=p.add_subparsers(dest='cmd', required=True)

    v=sub.add_parser('validate')
    v.add_argument('--schema', required=True)
    v.add_argument('--config', required=True)
    v.add_argument('--json', action='store_true')

    l=sub.add_parser('lint')
    l.add_argument('--schema', required=True)

    e=sub.add_parser('explain')
    e.add_argument('--schema', required=True)

    args=p.parse_args(argv)

    if args.cmd == 'lint':
        schema = load_doc(Path(args.schema))
        print('Schema loaded OK with top-level keys:', ', '.join(schema.keys()))
        return 0

    if args.cmd == 'explain':
        schema = load_doc(Path(args.schema))
        req = schema.get('required', [])
        props = list(schema.get('properties', {}).keys())
        print('Required:', ', '.join(req) if req else '(none)')
        print('Properties:', ', '.join(props) if props else '(none)')
        return 0

    schema = load_doc(Path(args.schema))
    config = load_doc(Path(args.config))
    errors = validate_config(schema, config)
    print_errors(errors, as_json=args.json)
    return 0 if not errors else 2
