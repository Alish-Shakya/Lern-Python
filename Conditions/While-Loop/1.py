while True:
    num = int(input("Enter a number to reverse (0 to exit): "))

    if num == 0:
        break

    reverse = 0
    temp = num

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print(f"The reverse of the number is: {reverse}")
