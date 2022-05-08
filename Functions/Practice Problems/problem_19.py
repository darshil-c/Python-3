# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(x, y, z):
    if sum((x,y,z)) <= 21:
        return sum((x,y,z))
    elif sum((x,y,z)) > 21 and 11 in (x,y,z):
        if sum((x,y,z)) - 10 <= 21:
            return sum((x,y,z)) - 10
        else:
            return 'BUST'
    elif sum((x,y,z)) > 21:
        return 'BUST'

# Test case x = 5, y = 6, z = 7, expected output = 18

print(blackjack(5,6,7))

# Test case x = 10, y = 9, z = 8, expected output = "BUST"

print(blackjack(10, 9, 8))

# Test case x = 11, y = 10, z = 1, expected output = 12

print(blackjack(11, 10, 1))

# Test case x = 11, y = 10, z = 11, expected output = "BUST"

print(blackjack(11, 10, 11))