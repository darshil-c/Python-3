# Define a function called is_greater that takes in two arguments,
# and returns True if the first value is greater than the second, False if it is less than or equal to the second

def is_greater(x, y):
    if x > y:
        return True
    else:
        return False

# Test case where x > y, expected output = True

print(is_greater(10, 0))

# Test case where x = y, expected output = False

print(is_greater(5, 5))

# Test case where x < y, expected output = False

print(is_greater(0, 10))