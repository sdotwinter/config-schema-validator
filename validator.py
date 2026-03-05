from jsonschema import Draft202012Validator

def validate_config(schema: dict, config: dict):
    validator = Draft202012Validator(schema)
    errs = []
    for e in sorted(validator.iter_errors(config), key=lambda x: list(x.path)):
        errs.append({
            'path': '/'.join(str(p) for p in e.path) or '$',
            'message': e.message,
            'validator': e.validator,
        })
    return errs
