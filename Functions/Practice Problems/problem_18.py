# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(s):
    output = ''
    for c in s:
        output += c*3
    return output

# Test case s = "Hello", expected output = "HHHeeellllllooo"

print(paper_doll("Hello"))

# Test case s = "Test", expected output = "TTTeeesssttt"

print(paper_doll("Test"))