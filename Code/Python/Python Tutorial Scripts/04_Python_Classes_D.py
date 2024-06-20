class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def helloWorld(self):
        print("Hello Drug Discovery World!")

person1 = Person("Mike", 30, 180)
print(person1.name)
print(person1.age)
print(person1.height)

person1.name = "Henry"
print(person1.name)
person1.helloWorld()