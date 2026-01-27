# Program to demonstrate string indexing using positive and negative in indices 



# Input string
text = input("Enter a string: ")

# Positive indexing
print("Positive Indexing:")
print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[len(text) - 1])

# Negative indexing
print("\nNegative Indexing:")
print("Last character:", text[-1])
print("Second last character:", text[-2])
print("First character:", text[-len(text)])
