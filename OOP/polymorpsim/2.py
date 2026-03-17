# Overridding

class Animal:
    def sound(self):
        print("Some Sound")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Dog(Animal):
    def sound(self):
        print("Bark")


animals = [Dog(), Cat(), Animal()]

for i in animals:
   print(i.sound())
