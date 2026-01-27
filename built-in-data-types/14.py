# program to remove element from a list using for loop and while loop 

numbers1 = [10, 20, 30, 40, 50]
remove_value = 30

for i in numbers1[:]:      # iterate over a copy
    if i == remove_value:
        numbers1.remove(i)

print("List after removing using for loop:", numbers1)


# Using while loop
numbers2 = [10, 20, 30, 40, 50]
i = 0

while i < len(numbers2):
    if numbers2[i] == remove_value:
        numbers2.pop(i)
    else:
        i += 1

print("List after removing using while loop:", numbers2)
