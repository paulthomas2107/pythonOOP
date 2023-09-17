import yaml
import json

with open('app.yaml', 'r') as fh:
    struct = yaml.safe_load(fh)

print(json.dumps(struct, indent=4, separators=(',', ': ')))