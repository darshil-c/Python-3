# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    return list(set(l))

# Test case l = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3], expected output = [1, 2, 3]

print(unique_list([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))

# Test case l = [1, 1, 1, 1, 1, 1, 1, 1], expected output = [1]

print(unique_list([1, 1, 1, 1, 1, 1, 1, 1]))