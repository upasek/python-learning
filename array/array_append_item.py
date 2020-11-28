#Write a Python program to append items from a specified list.

from array import *

list = list(map(int, input("Input the integer separated by comma : ").split(",")))

print("Items in the list :",list)

array = array('i', [] )

array.fromlist(list)

print("Append items from the list : ")
print("Items in the array :",array)
