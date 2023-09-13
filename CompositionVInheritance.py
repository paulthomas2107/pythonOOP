from io import StringIO


class WriteMyStuff(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = 'This is a silly message'
        self.writer.write(write_text)


fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print('File obj', open('test.txt', 'r').read())
print('StringIO obj', sioh.getvalue())