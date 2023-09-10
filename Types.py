myInt: int = 5
myStr: str = 'AAAA'
myBool: bool = True
myList = ['a', 'b', 'c']
myNone = None


def myFunc(years):
    return years + 1


print(type(myStr))
print(type(myInt))
print(type(myBool))
print(type(myList))
print(type(myFunc(1999)))
print(type(myNone))

this_type = type(myList)
print(this_type)

int2: int = 5
print(dir(int2))
print(int2.numerator)
print(int2.real)
print(int2.bit_length())
print(int2.bit_count())