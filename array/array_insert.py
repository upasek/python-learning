#Write a Python program to insert a new item before the second element in an existing array.


from array import *

list = list(map(int, input("Input the integers separated by comma : ").split(",")))

array = array('i', list)

print("Original array :",array)

num = int(input("Input the new element to insert : "))

array.insert(1, num)

print("Insert new value %d before %d :"%(num, array[2]))

print("New array :",array)
