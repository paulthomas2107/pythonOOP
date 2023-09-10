class Dog(object):
    def __init__(self, breed: str, name: str, price: float):
        self.breed = breed
        self.name = name
        self.price = price


myDog = Dog('Boxer', 'Woof', 123.45)
print(myDog.breed, myDog.name, myDog.price)
