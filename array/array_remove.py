#Write a Python program to remove a specified item using the index from an array.

from array import *

list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)

print("Original array :",array)

num = int(input("input the index of element which can be remove : "))

array.pop(num)

print("New array :",array)
