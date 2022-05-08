# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(list):
    for i in range(len(list)-1):
        if list[i] == 3 and list[i+1] == 3:
            return True
        else:
            pass
    return False

# Test case list = range(10), expected output = False

print(find_33(range(10)))

# Test case list = [1,2,3,4,6,7], expected output = False

print(find_33([1,2,3,4,6,7]))

# Test case list = [3,3,1,4,6,7], expected output = True

print(find_33([3,3,1,4,6,7]))

# Test case list = [1,2,3,3,6,7], expected output = True

print(find_33([1,2,3,3,6,7]))

# Test case list = [1,2,3,4,3,3], expected output = True

print(find_33([1,2,3,4,3,3]))