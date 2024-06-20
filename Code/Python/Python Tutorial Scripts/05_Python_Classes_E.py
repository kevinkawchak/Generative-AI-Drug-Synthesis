class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __del__(self):
        print("Object deleted!")

person1 = Person("Mike", 30, 180)
print(person1.name)
print(person1.age)
print(person1.height)

person1.name = "Henry"
print(person1.name)

del person1