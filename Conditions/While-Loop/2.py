#program to find the factorial of a given number

num=int(input("enter a factorial number:"))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    i=i+1
print(f"The factorial of {num} is {factorial}")


