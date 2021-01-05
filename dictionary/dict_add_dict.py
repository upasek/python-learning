# Write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for m, value in d1.items():
    if m in d2:
        d2[m] = d2[m] + d1[m]
    elif m not in d2:
        d2[m] = value

print(d2)
