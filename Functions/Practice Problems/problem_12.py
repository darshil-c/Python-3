# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(x):
    if len(x.split(" ")) != 2:
        return False
    l = x.split(" ")
    if l[0][0] == l[1][0]:
        return True
    else:
        return False

# Test case x = "test test", expected output = True

print(animal_crackers("test test"))

# Test case x = "test", expected output = False

print(animal_crackers("test"))

# Test case x = "test failed", expected output = False

print(animal_crackers("test failed"))