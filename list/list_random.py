#Write a Python program to select an item randomly from a list.

import random
color_list = input("Input list seprated by comma : ").split(",")
print("Original list :",color_list)
print(random.choice(color_list))
