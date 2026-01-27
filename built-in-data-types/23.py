# program to update a tuple by converting it into a list 

# Original tuple
numbers = (10, 20, 30, 40, 50)
print("Original tuple:", numbers)

# Convert tuple to list
numbers_list = list(numbers)

# Update the list
numbers_list[2] = 300          # change third element
numbers_list.append(60)         # add a new element

# Convert list back to tuple
numbers = tuple(numbers_list)
print("Updated tuple:", numbers)
