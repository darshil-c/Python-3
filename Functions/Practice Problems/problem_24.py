# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    uppers = 0
    lowers = 0
    for l in s:
        if l.isupper():
            uppers += 1
        elif l.islower():
            lowers += 1
    print(f"The original string: {s}")
    print(f"# of upper case characters: {uppers}")
    print(f"# of lower case characters: {lowers}")

# Test case s = "TeST", expected output = uppers = 3 lowers = 1

up_low("TeST")

# Test case s = "test", expected output = uppers = 0 lowers = 4

up_low("test")

# Test case s = "TEST", expected output = uppers = 4 lowers = 0

up_low("TEST")