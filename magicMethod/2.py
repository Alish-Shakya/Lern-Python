# String Representation
class Demo:
    def __str__(self):
        return "This is Demo object"
    
    def __repr__(self):
        return "Demo()"

d = Demo()
print(d)       # calls __str__
print(repr(d)) # calls __repr__



