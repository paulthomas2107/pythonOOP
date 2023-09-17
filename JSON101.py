import json

with open('jsonconfig.json', 'rb') as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))

conf['new_key'] = 5.00005
with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ': '))

