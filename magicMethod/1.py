# construction and deconstruction 


class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called: {self.name}")
    
    def __del__(self):
        print(f"Destructor called: {self.name}")

obj = Demo("Ram")
del obj
