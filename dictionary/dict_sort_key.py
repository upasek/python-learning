#Write a Python program to sort a dictionary by key.

color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
print("Original dictionary :",color_dict)
dict = {}
for key in sorted(color_dict):
    dict[key] = color_dict[key]

print("After sorting by key:",dict)
