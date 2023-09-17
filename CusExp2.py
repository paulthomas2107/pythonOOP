class MyError(Exception):
    def __init__(self, *args):
        print("init")
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('str')
        if self.message:
            return 'MyError exc {0}'.format(self.message)
        else:
            return 'MyError exc !'


# raise MyError

raise MyError('Houston...')