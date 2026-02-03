


class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def role(self):
        print(self.name, "is a employee")

class Intern(Person):
    def role(self):
        print(self.name, "is a intern")

e = Employee("Ram")
e.role()

i = Intern("Shyam")
i.role()