# SUMMER OF '69: Return the sum of the numbers in the list, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True
    for i in arr:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total

# Test case arr = [1, 2, 3], expected output = 6

print(summer_69([1, 2, 3]))

# Test case arr = [6, 9], expected output = 0

print(summer_69([6, 9]))

# Test case arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], expected output = 15

print(summer_69([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Test case arr = [6, 1, 2, 3, 9, 4, 5], expected output = 9

print(summer_69([6, 1, 2, 3, 9, 4, 5]))

# Test cass arr = [1, 2, 3, 6, 4, 5, 9, 7, 8], expected output = 21

print(summer_69([1, 2, 3, 6, 4, 5, 9, 7, 8]))