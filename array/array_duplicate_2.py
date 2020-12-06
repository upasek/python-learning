#Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.


from array import *

def duplicates(array):
    print("Original array :",array)
    val = 0
    for i in array:
        index = array.index(i)
        if i in array[index + 1 : ]:
            val += 1
            print("The given array contain duplicate element.")
            break;
    if val == 0:
        print("The given array not contain duplicate element.")



list = list(map(int, input("Input the integers separated by comma : ").split(",")))
array = array('i', list)
duplicates(array)
