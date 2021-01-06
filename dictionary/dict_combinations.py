#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

import itertools
d = {'1':['a','b'], '2':['c','d']}
print("Original dictionary :",d)
print("Expected Output : ")
for combo in itertools.product(*[d[k] for k in sorted(d.keys()) ] ):
    print(''.join(combo))
