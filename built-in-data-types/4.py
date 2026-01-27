# program to perform string slicing in different ways

# Input string
text = input("Enter a string: ")

# Different slicing methods
print("Original string:", text)
print("From index 0 to 4:", text[0:5])
print("From index 2 to end:", text[2:])
print("From start to index 4:", text[:5])
print("Last 3 characters:", text[-3:])
print("From index 1 to 5:", text[1:6])
print("Alternate characters:", text[::2])
print("Reverse string:", text[::-1])
