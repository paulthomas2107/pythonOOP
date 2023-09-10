import random


class Dog(object):

    def __init__(self, breed: str, name: str, price: float):
        self.breed = breed
        self.name = name
        self.price = price
        self.id = random.randint(1, 999999)

    def inc_price(self):
        self.price += .01

    def show_dog(self):
        print(self.breed, self.name, '{:.2f}'.format(self.price))


myDog = Dog('Boxer', 'Woof', 123.45)
myDog.show_dog()
myDog.inc_price()
myDog.show_dog()

myDog2 = Dog('Shitzu', 'Bella', -99.99)
myDog2.show_dog()
myDog2.inc_price()
myDog2.show_dog()
print(myDog2.id)
myDog2.name = 'Dinky'
myDog2.show_dog()
