# program to show that tuple are immutable

# Create a tuple
numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

# Try to change an element
try:
    numbers[2] = 300   # This will raise an error
except TypeError as e:
    print("Error:", e)

# Tuple remains unchanged
print("Tuple after trying to modify:", numbers)
