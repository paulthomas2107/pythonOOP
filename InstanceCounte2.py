class InstanceCounter(object):
    count: int = 0

    def __init__(self, val: int):
        self.val = self.filterInt(val)
        InstanceCounter.count += 1

    def set_val(self, newVal: int):
        self.val = newVal

    def get_val(self) -> int:
        return self.val

    @classmethod
    def get_count(cls) -> int:
        return cls.count

    @staticmethod
    def filterInt(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)


for obj in (a, b, c):
    print("Val of obj: {0}".format(obj.get_val()))
    print("Count: {0}".format(obj.get_count()))
    print(obj.val)

print(InstanceCounter.get_count())