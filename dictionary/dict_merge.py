#Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'x': 400, 'y': 500, 'z':600}
d = d1.copy()
d.update(d2)
print("First dictionary :",d1)
print("Second dictionary :",d2)
print("New dictionary :",d)
