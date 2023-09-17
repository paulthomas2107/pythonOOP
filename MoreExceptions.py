class MyClass(object):

    @staticmethod
    def make_error():
        print('in make_error')
        5/0
        print('out make_error')

    def do_something(self):
        print('in do_something')
        self.make_error()
        print('out do_something')


def some_util_func():
    print('in some_util_func')
    cc = MyClass()
    cc.do_something()
    print('out some_util_func')


def some_major_func():
    print('in some_major_func')
    some_util_func()
    print('out some_major_func')


def main():
    print('in main')
    some_major_func()
    print('out main')


main()