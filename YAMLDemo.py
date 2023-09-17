import yaml

myDict = {'a': 1, 'b': 2, 'c': 3}
myList = [1, 2, 3, 4, 5]
myTuple = ('x', 'y', 'z')

loaded_yaml = yaml.dump(myDict, default_flow_style=False)
print(loaded_yaml)
print(yaml.dump(myList, default_flow_style=False))
print(yaml.dump(myTuple, default_flow_style=False))
