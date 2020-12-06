#Write a Python program to convert an array to an array of machine values and return the bytes representation.

from array import *

list = list(map(int, input("Input the bytes separated by comma : ").split(",")))

print("Bytes to string : ")

x = array('b', list)

s = x.tobytes()

print(s)
