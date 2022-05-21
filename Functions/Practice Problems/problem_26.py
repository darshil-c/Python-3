# Write a Python function to multiply all the numbers in a list.

def multiply(l):
    x = 1

    for n in l:
        x *= n

    return x

# Test case l = [1, 2, 3, 4], expected output = 24

print(multiply([1, 2, 3, 4]))

# Test case l = [-2, -2, 2, -2], expected output = -16

print(multiply([-2, -2, 2, -2]))

# Test case l = [1, 2, 3, 0], expected output = 0

print(multiply([1, 2, 3, 0]))