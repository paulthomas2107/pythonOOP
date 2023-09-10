import random


class MyClass(object):

    rand_num: int

    def doThis(self):
        x: int = random.randint(1, 10)
        self.rand_num = x


myInst = MyClass()
myInst.doThis()
print(myInst.rand_num)