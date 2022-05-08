# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(x, y):
    if sum((x, y)) == 20 or (x == 20 or y == 20):
        return True
    else:
        return False

# Test case x = 15, y = 5, expected output = True

print(makes_twenty(15, 5))

# Test case x = 1, y = 2, expected output = False

print(makes_twenty(1, 2))

# Test case x = 20, y = 15, expected output = True

print(makes_twenty(20, 15))

# Test case x = 1, y = 20, expected output = True

print(makes_twenty(1, 20))