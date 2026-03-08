import json

def print_report(errors, lint_issues, as_json=False):
    if as_json:
        payload={
            'errors':[{'path':list(e.path),'message':e.message} for e in errors],
            'lint':lint_issues,
            'valid':(len(errors)==0 and len(lint_issues)==0)
        }
        print(json.dumps(payload, indent=2)); return
    if errors:
        print('Schema errors:')
        for e in errors:
            p='.'.join(str(x) for x in e.path) or '<root>'
            print(f'- {p}: {e.message}')
    if lint_issues:
        print('Lint issues:')
        for i in lint_issues:
            print(f'- {i}')
    if not errors and not lint_issues:
        print('Config is valid.')
