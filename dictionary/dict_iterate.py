#Write a Python program to iterate over dictionaries using for loops.

d = {'v':40, 'w':50, 'x': 10, 'y': 20, 'z': 30,}
print("Original dictionary :",d)
for key, value in d.items():
    print("%s --> %d"%(key, value))
