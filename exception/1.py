try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
