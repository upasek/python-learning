#Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

from array import *
list = list(map(int, input("Input the integer separated by comma : ").split(",")))
array = array('i', list)
print("Display all item in array...")
for i in array:
    print(i)

print("Access first three items individually...")
print(array[0])
print(array[1])
print(array[2])
