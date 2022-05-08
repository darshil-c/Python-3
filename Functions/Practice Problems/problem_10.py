# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, 
# and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

def myfunc(x):
    output = []
    for i in range(len(x)):
        if i % 2 == 0:
            output.append(x[i].upper())
        else:
            output.append(x[i].lower())
    return ''.join(output)

# Test case x = "Test", expected output = "TeSt"

print(myfunc("Test"))

# Test case x = "Argument", expected output = "ArGuMeNt"

print(myfunc("Argument"))
