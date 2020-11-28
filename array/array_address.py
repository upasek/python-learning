#Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array’s contents and also find the size of the memory buffer in bytes.

from array import *
list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)
print("Original array :",array)

print("Current memory address and the length in elements of the buffer : ",array.buffer_info())

print("The size of the memory buffer in bytes : ",array.buffer_info()[1]*array.itemsize )
