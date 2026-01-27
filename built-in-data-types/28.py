# program to add and remove element from a set 

# Create a set
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Add elements
fruits.add("mango")          # add single element
fruits.update(["orange", "grapes"])  # add multiple elements
print("After adding elements:", fruits)

# Remove elements
fruits.remove("banana")       # removes element; raises error if not found
fruits.discard("pineapple")   # removes element if exists; no error if not found
print("After removing elements:", fruits)
