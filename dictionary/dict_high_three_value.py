#Write a Python program to find the highest 3 values in a dictionary.

from heapq import nlargest

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

print("Original dictionary :",my_dict)
three_largest = nlargest(3, my_dict, key = my_dict.get)

print("Highest 3 values in a dictionary :",three_largest)
