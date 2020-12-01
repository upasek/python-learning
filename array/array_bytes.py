#Write a Python program to get the length in bytes of one array item in the internal representation.

from array import *
list = list(map(int, input("Input the integer separated by comma : ").split(",")))

array = array('i', list)

print("Orirginal array :",array)

print("Length in bytes of one array item :", (array.itemsize))
