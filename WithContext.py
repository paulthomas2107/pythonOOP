class MyClass(object):
    def __enter__(self):
        print('Entered with')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving with')
        print('Type {0}'.format(exc_type))
        print('Value {0}'.format(exc_val))
        print('Trace {0}'.format(exc_tb))

    def sayHi(self):
        print('Hi, instance %s' % (id(self)))


with MyClass() as cc:
    cc.sayHi()
    5/0

print('After the with')
