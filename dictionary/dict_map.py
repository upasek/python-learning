#Write a Python program to map two lists into a dictionary.

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
mix = dict(zip(keys, values))
print("First list :",keys)
print("Second list :",values)
print("New dictionary :",mix)
