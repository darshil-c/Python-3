# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(n):
    # create a list of prime numbers starting with 2
    primes = [2]
    # start x from 3 as that is the next prime number
    x = 3
    # if the length of the given n is less than 2 there a no prime numbers
    if n < 2:
        return 0
    while x <= n:
        # check for every number in our current primes list
        for y in primes:
            # if our current number can be divided by any number in the primes list it is not a prime number 
            if x % y == 0:
                # increment by 2 as all even numbers aren't prime numbers 
                x += 2
                break
        # else the number is a prime number and we add it to our primes list
        else:
            primes.append(x)
            x += 2
    # we only need to return the length and not the actual prime numbers
    # if you wanted to see the numbers a simple print statement would suffice
    # print(primes)
    return len(primes)

# Test case up to 100, expected output = 25

print(count_primes(100))

# Test case up to 50, expected output = 15

print(count_primes(50))