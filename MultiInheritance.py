class A(object):

    @staticmethod
    def do_this() -> None:
        print('Doing this in A')


class B(A):
    pass


class C (A):

    @staticmethod
    def do_this() -> None:
        print('Doing this in C')


class D(B, C):
    pass


d_instance = D()
d_instance.do_this()
print(D.mro())  # method resolution order