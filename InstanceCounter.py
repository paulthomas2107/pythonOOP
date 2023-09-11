class InstanceCounter(object):
    count: int = 0

    def __init__(self, val: int):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newVal: int):
        self.val = newVal

    def get_val(self) -> int:
        return self.val

    @staticmethod
    def get_count() -> int:
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter(21)

for obj in (a, b, c, d):
    print("Val of obj: %s" % (obj.get_val()))
    print("Count: %s" % (obj.get_count()))
    print("Count (from instance): %s" % obj.count)

print(InstanceCounter)