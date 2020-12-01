#Write a Python program to get the number of occurrences of a specified element in an array.

from array import *

array = array('i', [1, 3, 5, 3, 7, 9, 3])
num = int(input("Input the integer : "))
count = 0
for i in array:
    if i == num:
        count += 1

print("Original array :",array)
print("Number of occurrences of the number %d in the said array: %d"%(num, count))

#print("Number of occurrences of the number 3 in the said array: "+str(array.count(num)))
