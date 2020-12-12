#Write a Python program to remove the first occurrence of a specified element from an array.

from array import *

list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)

print("Original array :",array)

num = int(input("Input the element which is to be remove : "))

for i in array:
    if i == num:
        array.pop(array.index(i))
        break;

#array.remove(num)

print("Remove the first occurrence of %d from the said array : "%num)
print("New array :",array)
