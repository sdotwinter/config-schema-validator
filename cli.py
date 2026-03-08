import argparse
from loader import load_doc
from validator import validate_config, lint_config
from reporter import print_report

def run(argv=None):
    p=argparse.ArgumentParser(prog='config-schema-validator')
    sub=p.add_subparsers(dest='cmd', required=True)

    v=sub.add_parser('validate')
    v.add_argument('--config', required=True)
    v.add_argument('--schema', required=True)
    v.add_argument('--json', action='store_true')

    l=sub.add_parser('lint')
    l.add_argument('--config', required=True)

    r=sub.add_parser('report')
    r.add_argument('--config', required=True)
    r.add_argument('--schema', required=True)
    r.add_argument('--json', action='store_true')

    a=p.parse_args(argv)

    if a.cmd=='lint':
        cfg=load_doc(a.config)
        issues=lint_config(cfg)
        print_report([], issues, as_json=False)
        return 1 if issues else 0

    cfg=load_doc(a.config)
    sch=load_doc(a.schema)
    errs=validate_config(cfg, sch)
    issues=lint_config(cfg) if a.cmd=='report' else []
    print_report(errs, issues, as_json=getattr(a,'json',False))
    return 1 if errs or issues else 0
