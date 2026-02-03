class Cat:
    
    def __init__(self, name, age):  # __init__ is a constructor, runs automatically
        self.name = name  # initialize attribute
        self.age = age


c = Cat("abc", 5)  # creating object of the class
print(c.name)
print(c.age)
