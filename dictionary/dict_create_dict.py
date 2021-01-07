#Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

from pprint import pprint

dict1 = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))

pprint(dict1)

for value in dict1.values():
    print(value[4])

for key, value in dict1.items():
    print(key, "has value", value)
