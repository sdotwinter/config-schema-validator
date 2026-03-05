# Config Schema Validator

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

CLI for validating YAML/JSON config files against JSON Schema.

## Usage
```bash
python3 main.py lint --schema examples/schema.json
python3 main.py explain --schema examples/schema.json
python3 main.py validate --schema examples/schema.json --config examples/config-valid.yaml
python3 main.py validate --schema examples/schema.json --config examples/config-invalid.yaml --json
```

## Sponsorware
Personal evaluation is free. Commercial/team usage and advanced rule packs require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
