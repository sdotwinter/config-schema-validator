from jsonschema import Draft202012Validator

def validate_config(config, schema):
    v=Draft202012Validator(schema)
    errs=sorted(v.iter_errors(config), key=lambda e: e.path)
    return errs

def lint_config(config):
    issues=[]
    if isinstance(config, dict):
        for k,v in config.items():
            if isinstance(k,str) and k.strip()!=k:
                issues.append(f'Key has leading/trailing spaces: {k!r}')
            if isinstance(v,str) and v=='' :
                issues.append(f'Empty string value at key: {k}')
    return issues
