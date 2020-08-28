#Write a Python program to shuffle and print a specified list.
from random import shuffle
def shuff(list):
    shuffle(list)
    return list

list = input("Input list seprated by comma : ").split(",")
print("Original list :",list)
print("List after shuffle :",shuff(list))
