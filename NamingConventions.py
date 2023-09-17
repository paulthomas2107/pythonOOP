class GetSet(object):

    instance_count = 0

    __mangled_name = 'no privacy !'

    def __init__(self, value):
        self._attrval = value
        GetSet.instance_count += 1

    @property
    def var(self):
        print('Getting the var attr')
        return self._attrval

    @var.setter
    def var(self, value):
        print('Setting the var attr')
        self._attrval = value

    @var.deleter
    def var(self):
        print('Deleting the var attr')
        self._attrval = None


cc = GetSet(5)
cc.var = 10
print(cc._attrval)
print(cc._GetSet__mangled_name)
