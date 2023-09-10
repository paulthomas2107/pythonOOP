class MyClass(object):
    age: int = 91


this_obj = MyClass()
print(this_obj)
print(this_obj.age)

this_obj2 = MyClass()
this_obj.age = 99
print(this_obj.age)