class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
    

person1 = Person("Mike", 30, 180)
print(person1.name)
print(person1.age)
print(person1.height)

print(person1)