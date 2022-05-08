# Define a function called myfunc that takes three arguments, x, y, and z
# If z is True, return x. If z is False, return y

def myfunc(x,y,z):
    if z:
        return x
    else:
        return y

# Test case when z is True

print(myfunc("z is True", "z is False", True))

# Test case when z is False

print(myfunc("z is True", "z is False", False))