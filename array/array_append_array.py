#Write a Python program to append items from inerrable to the end of the array.

from array import *

list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)

print("Original array :",array)

array.extend(array)

print("New array :",array)
