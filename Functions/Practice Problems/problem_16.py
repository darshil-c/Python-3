# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(x):
    if abs(100-x) <= 10 or abs(200-x) <= 10:
        return True
    else:
        return False

# Test case x = 95, expected output = True

print(almost_there(95))

# Test case x = 50, expected output = False

print(almost_there(50))

# Test case x = 210, expected output = True

print(almost_there(210))

# Test case x = 211, expected output = False

print(almost_there(211))