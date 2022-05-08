# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(x):
    l = x.split(" ")
    l.reverse()
    return " ".join(l)

# Test case x = "this is a test", expected output = "test a is this"

print(master_yoda("this is a test"))

# Test case x = "test", expected output = "test" no change

print(master_yoda("test"))