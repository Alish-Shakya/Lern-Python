#program to create a simple calculater

a=int(input("Enter a 1st number:")
b=int(input("Enter a 2nd number:")
choice=input("Enter an operater(+,-,*,/):")
match choice:
    case '+:
        print(f"The sum is:{a+b}")
    case '-':
        print(f"The difference is:{a-b}")
    case '*':                                   
        print(f"The product is:{a*b}")
    case '/':
        print(f"The quotient is:{a/b}")
    case _:
        print("Invalid operater")   

