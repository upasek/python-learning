#Write a Python program to convert a list into a nested dictionary of keys.

num = [1, 2, 3, 4]
print("Original list :",num)
current = dict = {}
for m in num:
    dict[m] = {}
    dict = dict[m]

print("New dictionary :",current)
