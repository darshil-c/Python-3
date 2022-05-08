# Define a function called myfunc that takes in an arbitrary number of arguments,
# and returns a list containing only arguments that are even

def myfunc(*args):
    even_list = []
    for x in args:
        if x % 2 == 0:
            even_list.append(x)
        else:
            pass
    return even_list

# Test case with 1, 2, 3, and 4, expected output = [2, 4]

print(myfunc(1, 2, 3, 4))

# Test case with only odd numbers, expected output = []

print(myfunc(1, 3, 5, 7))


