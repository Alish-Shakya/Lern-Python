# program to check whether a given number is even or odd using Boolean logic 


# Input number
num = int(input("Enter a number: "))

# Boolean logic
is_even = (num % 2 == 0)

# Check and display result
if is_even:
    print("The number is Even")
else:
    print("The number is Odd")
