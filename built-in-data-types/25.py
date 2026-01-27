# program to loop through a tuple and write a program to join two tuple 

# Create a tuple
numbers = (10, 20, 30, 40, 50)

# Loop through the tuple using for loop
print("Looping through the tuple:")
for num in numbers:
    print(num)

# Create another tuple
more_numbers = (60, 70, 80)

# Join two tuples
joined_tuple = numbers + more_numbers
print("\nJoined tuple:", joined_tuple)
