# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            return x
        else:
            return y
    else:
        if x > y:
            return x
        else:
            return y

# Test case x = 2, y = 16, expected output = 2

print(lesser_of_two_evens(2, 16))

# Test case x = 2, y = 19, expected output = 19

print(lesser_of_two_evens(2, 19))

# Test case x = 7, y = 5, expected output = 7

print(lesser_of_two_evens(7, 5))