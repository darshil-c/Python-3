# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    cs = s.replace(' ', '')
    cs = cs.lower()
    if cs == cs[::-1]:
        return True
    else:
        return False

# Test case s = race car, expected output = True

print(palindrome("race car"))

# Test case s = Hello, expected output = False

print(palindrome("Hello"))

# Test case s = Helleh, expected output = True

print(palindrome("Helleh"))