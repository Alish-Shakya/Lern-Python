class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b

        for num in args:
            result *=num

        return result
c = Calculator()
print(c.multiply(2,3))

print(c.multiply(2,3,4,5,6))