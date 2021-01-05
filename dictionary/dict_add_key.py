#Write a Python program to add a key to a dictionary.

d = {0:10, 1:20}
print("Original dictionary :",d)
d.update({2:30})
print("Dictionary after update :",d)
d[3] = 40
print("Dictionary after update :",d)
