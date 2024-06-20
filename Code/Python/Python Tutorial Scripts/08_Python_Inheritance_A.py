class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
    
    def get_older(years):
        self.age += years
    
class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12
    
worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary())