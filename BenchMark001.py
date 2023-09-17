import timeit

print('By index', timeit.timeit(stmt="myDict['c']", setup="myDict = {'a': 5, 'b': 6, 'c': 7}", number=1000000))
print('By get  ', timeit.timeit(stmt="myDict.get('c')", setup="myDict = {'a': 5, 'b': 6, 'c': 7}", number=1000000))


