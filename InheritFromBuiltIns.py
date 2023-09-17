class MyDict(dict):
    def __setitem__(self, key, val):
        print('Setting a key and value !')
        # self[key] = val  # recursive
        dict.__setitem__(self, key, val)


class MyList(list):
    def __getitem__(self, index):       
        if index == 0:
            raise IndexError
        if index > 0:
            index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index - 1
        list.__setitem__(self, index, value)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))

print("-" * 100)

x = MyList(['a', 'b', 'c'])
print(x)
x.append('spam')
print(x[1])
print(x[4])
