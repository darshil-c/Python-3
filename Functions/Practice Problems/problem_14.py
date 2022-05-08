# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(x):
    output = []
    for i in range(len(x)):
        if i == 0 or i == 3:
            output.append(x[i].upper())
        else:
            output.append(x[i])
    return ''.join(output)

# Test case x = "macdonald", expected output = "MacDonald"

print(old_macdonald("macdonald"))

# Test case x = "test", expected output = "TesT"

print(old_macdonald("test"))