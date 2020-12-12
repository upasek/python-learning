#Write a Python program to reverse the order of the items in the array.

from array import *

list = list(map(int, input("Input the integer separated by comma : ").split(",")))

array = array('i', list )

print("Original array :",array)

array.reverse()

print("New array :",array)
