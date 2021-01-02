#Write a Python program to convert a tuple to a dictionary.

#create a tuple
tuplex = (("w", 2),("r", 3), ("x", 3), ("y", 1), ("z", 1))
print(dict((y, x) for y, x in tuplex))
