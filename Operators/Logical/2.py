def check(x):
    print("Function called for value", x)
    return True if x>6 else false

a = check
b = check
c = check

if a(-10) or b(50) or c(20):
    print("Atleast  one True")
else:
    print("All False")