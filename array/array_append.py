#Write a Python program to append a new item to the end of the array.

from array import *

list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)

print("Original array :",array)

num = int(input("Input the number for append in array : "))

array.append(num)

print("New array :",array)
