# program to add emelents to a list using append(), insert(), and extend()


# Create a list
numbers = [10, 20, 30]

print("Original list:", numbers)

# append() – adds element at the end
numbers.append(40)
print("After append():", numbers)

# insert() – adds element at a specific index
numbers.insert(1, 15)
print("After insert():", numbers)

# extend() – adds multiple elements
numbers.extend([50, 60, 70])
print("After extend():", numbers)
