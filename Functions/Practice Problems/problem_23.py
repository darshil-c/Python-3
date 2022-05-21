# Write a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(n, l, h):

    if n in range(l, h+1):
        print(f"{n} is in range of {l} and {h}")
    else:
        print(f"{n} is not in range of {l} and {h}")

# Test case n = 1, l = 1, h = 10, expected output = 1 is in range of 1 and 10

range_check(1, 1, 10)

# Test case n = 10, l = 1, h = 10, expected output = 10 is in range of 1 and 10

range_check(10, 1, 10)

# Test case n = 5, l = 1, h = 10, expected output = 5 is in range of 1 and 10

range_check(5, 1, 10)

# Test case n = 11, l = 1, h = 10, expected output = 11 is not in range of 1 and 10

range_check(11, 1, 10)

# another solution where only a boolean is returned

def range_bool(n, l, h):

    if n in range(l, h+1):
        return True
    else:
        return False

# Test case n = 1, l = 1, h = 10, expected output = True

print(range_bool(1, 1, 10))

# Test case n = 10, l = 1, h = 10, expected output = True

print(range_bool(10, 1, 10))

# Test case n = 5, l = 1, h = 10, expected output = True

print(range_bool(5, 1, 10))

# Test case n = 11, l = 1, h = 10, expected output = False

print(range_bool(11, 1, 10))