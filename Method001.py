class Joe(object):
    greeting = 'Hi, Joe'

    def call_me(self):
        print('Calling callme')
        print(self)

    def showGreeting(self) -> str:
        return self.greeting


thisJoe = Joe()
print(thisJoe.greeting)
thisJoe.call_me()
print(thisJoe)
print(thisJoe.showGreeting())
