import sys

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = input('Please input a key ')

try:
    arg = sys.argv[1]
    num = int(arg)
    print('Value for {0} is {1}'.format(key, myDict[key]))
except IndexError:
    print('The key {0} is not found'.format(key))


