#Write a Python program to create a dictionary from two lists without losing duplicate values.

from collections import defaultdict

list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
print("First list :",list)

num = [1, 2, 2, 3]
print("Second list :",num)

dict = defaultdict(set)

for c, i in zip(list, num):
    dict[c].add(i)

print(dict)
