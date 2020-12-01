#Write a Python program to convert an array to an ordinary list with the same items.

from array import *

array = array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("Original array :",array)

num_list = array.tolist()

print("Convert the said array to an ordinary list with the same items :",num_list)
