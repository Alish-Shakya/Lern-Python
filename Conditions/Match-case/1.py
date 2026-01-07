# display the name of the week

day = int(input("Enter a number:"))

match day:
    case 1:
        print("Sunday:")
    case 2: 
        print("Moday:")
    case 3:
        print("Tuesday:")
    case 4:
        print("wednesday:")
    case 5: 
        print("Thrusday:")
    case 6:
        print("Friday:")
    case 7:
        print("Saturday:")
    case _:
        print("Invalid")