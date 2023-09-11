import abc


class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, input):
        return

    @abc.abstractmethod
    def get_val(self):
        return


class MyClass(GetterSetter):
    def __init__(self):
        self.val = None

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


x = MyClass()
print(x)