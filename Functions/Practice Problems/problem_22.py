#Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is 4/3 * PI * r^3

import math


def vol(r):
    return 4/3*math.pi*r**3

# Test case r = 2, expected output = 33.51032

print(vol(2))

# Test case r = 5, expected output = 523.598

print(vol(5))