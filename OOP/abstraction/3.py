# built in data types in python are examples of abstraction. 
# We don't need to know how they are implemented to use them. 
# We just need to know how to use them. For example, we can use 
# the + operator to add two numbers or concatenate two strings without 
# knowing how the + operator is implemented for those data types.


class A:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, other):
        return self.a + other.a

# objects created outside class
obj1 = A(1)
obj2 = A(2)

print(obj1 + obj2)        
print(obj1.__add__(obj2)) 
