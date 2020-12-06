# Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.

from array import *

def duplicate(array):
    print("Original array :",array)
    val = 0
    for i in array:
        index = array.index(i)
        if i in array[index+1:]:
            print("First duplicate element in a given array is :",i)
            val += 1
            break;
    if val == 0:
        print("There is no any duplicate element.")



list = list(map(int, input("Input the integer separated by comma : ").split(",")))
array = array('i', list)
duplicate(array)
