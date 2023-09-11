import abc


class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.value = value
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print('GetSetInt object ({0}) only accepts int values'.format(id(self)))


class GetSetList(GetSetParent):
    def __init__(self, value=0):
        super().__init__(value)
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print('GetSetList obj len {0} stores hist of values set'.format(len(self.vallist)))