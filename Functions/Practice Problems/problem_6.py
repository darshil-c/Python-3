# Define a function called is_even that takes in one argument,
# and returns True if the passed-in value is even, False if it is not

def is_even(x):
    # Check if given number is divisible by 2 using modulo
    if x % 2 == 0:
        return True
    else:
        return False

# Test case where x = 20, expected output = True

print(is_even(20))

# Test case where x = 7, expected output = False

print(is_even(7))