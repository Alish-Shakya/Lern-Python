class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   

    def show_salary(self):
        print(self.__salary)

    def add_salary(self, amount):
        self.__salary = self.__salary + amount


e = Employee("RAM", 1000)

e.add_salary(2000)   
e.show_salary()      
