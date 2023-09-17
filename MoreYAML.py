import yaml
import json


class MyClass(object):
    classVar = 10

    def __init__(self, val):
        self.val = val

    def increment(self):
        self.val += 1


x = MyClass(5)
x.increment()
x.increment()

with open('obj.yaml', 'w') as fh:
    yaml.dump(x, fh)




