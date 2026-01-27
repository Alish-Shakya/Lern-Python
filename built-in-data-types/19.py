# program to join two liists into a single list  

# Two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

# Method 1: Using + operator
joined_list1 = list1 + list2
print("Joined list using +:", joined_list1)

# Method 2: Using extend() method
list1.extend(list2)
print("Joined list using extend():", list1)
