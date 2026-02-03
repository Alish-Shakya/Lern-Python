class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def role(self):
        print(self.name, "is an employee")

class Manager(Employee):
    def department(self, dept):
        print(self.name, "is in", dept, "department")

m = Manager("Alish")
m.role()
m.department("IT")