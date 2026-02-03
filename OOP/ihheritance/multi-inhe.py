


class Animal:
    def __init__(self, name):
        self.name = name

class Species:
    def __init__(self, species):
        self.species = species


class Cat(Animal, Species):
    def __init__(self, name,  species):
        Animal.__init__(self, name)
        Species.__init__(self, species)

    def info(self):
        print(self.name, "meow and is of species", self.species)

c = Cat("Cat", "Domestic")
c.info()