import sqlite3

class Person:

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata2.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]                

p1 = Person()
p1.load_person(1)
print(p1.first)
print(p1.last)
print(p1.age)
print(p1.id_number)