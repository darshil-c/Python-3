# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

import string

# this is the longer way, after learning about set comparisons there isn't a need for converting back and forth between data types
# just convert both to sets and do a simple comparison check.
def ispangram(str, alphabet=string.ascii_lowercase):
    # empty string used to join later
    s = ""
    # get the string without any spaces and all lowercase
    str = str.replace(' ', '')
    str = str.lower()
    # convert the string to a set followed by a list to get all the unique values
    str = list(set(str))
    # sort the list in lexicographical order a -> z
    str.sort()
    # put the string back together
    str = s.join(str)
    # if the string is the same as the alphabet then it is a valid pangram
    if alphabet == str:
        return True
    else:
        return False

# Test case str = "The quick brown fox jumps over the lazy dog", expected output = True

print(ispangram("The quick brown fox jumps over the lazy dog"))

# Test case str = "Test", expected output = False

print(ispangram("Test"))