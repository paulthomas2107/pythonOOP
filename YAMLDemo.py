import yaml

myDict = {'a': 1, 'b': 2, 'c': 3}
myList = [1, 2, 3, 4, 5]
myTuple = ('x', 'y', 'z')

loaded_yaml = yaml.dump(myDict, default_flow_style=False)
print(loaded_yaml)
print(yaml.dump(myList, default_flow_style=False))
print(yaml.dump(myTuple, default_flow_style=False))

myObj = (
    [1, 2, 3, 4, 5],
    {'a': 1, 'b': 2, 'c': 3},
    [
        {'x': 98, 'y': 99, 'z': 100},
        3,
        4
    ],
    {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
)

print(yaml.dump(myObj, default_flow_style=False))