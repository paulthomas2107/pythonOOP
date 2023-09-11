import random


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food) -> None:
        print("{0} is eating {1}.".format(self.name, food))


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing) -> None:
        print("{0} goes after {1}!".format(self.name, thing))

    def show_affection(self) -> None:
        print("{0} wags tail".format(self.name))


class Cat(Animal):
    def swatstring(self) -> None:
        print("{0} shreds the string!".format(self.name))

    def show_affection(self) -> None:
        print("{0} purrs".format(self.name))


for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()

d = Dog('dogname')

print(d.name)
print(d.breed)