


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name is: ", self.name)

class Cat(Animal):
    def sound(self):
        print(self.name, "meow")

c = Cat("DDD")
c.info()
c.sound()