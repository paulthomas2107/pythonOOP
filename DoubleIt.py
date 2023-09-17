import sys


def doubleIt(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var


def doubleLines(filename):
    with open(filename) as fh:
        newList = [str(doubleIt(int(val)) for val in fh)]
    with open(filename, 'w') as fh:
        fh.write('\n'.join(newList))


def tripleIt(x):
    var = x * 3
    return var


if __name__ == '__main__':
    inputVal = sys.argv[1]
    doubledVal = doubleIt(inputVal)
    print('Value of {0} is {1}'.format(inputVal, doubledVal))