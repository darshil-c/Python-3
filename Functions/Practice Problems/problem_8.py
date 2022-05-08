# Define a function called myfunc that takes in an arbitrary number of arguments,
# and returns the sum of those arguments

def myfunc(*args):
    return sum(args)

# Test case with 2 arguments 1 and 2, expected output = 3

print(myfunc(1, 2))

# Test case with 5 arguments 1, 2, 3, 4, and 5, expected output = 15

print(myfunc(1, 2, 3, 4, 5))