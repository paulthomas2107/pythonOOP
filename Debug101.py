import pdb


argSum: int = 0


def doubleVal(argSum: int, val: int):
    newVal = argSum + val
    return newVal


values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

mySum: int = 0

for val in values:
    # mySum = mySum + val
    pdb.set_trace()
    mySum = doubleVal(mySum, val)


print(mySum)