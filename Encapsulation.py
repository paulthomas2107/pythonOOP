class MyClass(object):
    def __init__(self, value: int, age: int):
        self.value = value
        self.age = age

    def set_val(self, val: int):
        self.value = val

    def get_val(self) -> int:
        return self.value

    def set_age(self, age: int):
        try:
            age = int(age)
        except ValueError:
            return
        self.age = age

    def decrement_age(self):
        self.age -= 1

    def get_age(self) -> int:
        return self.age


a = MyClass(10, 20)
b = MyClass(30, 40)

a.decrement_age()
b.decrement_age()

# a.set_age('ssss')
# b.set_age('sss')

print(a.get_val(), a.get_age())
print(b.get_val(), b.get_age())