#Write a Python program to find the most common elements and their counts of a specified text.

from collections import Counter

str = input("Input the string : ")

print("Original string : "+str)

print("Most common three characters of the said string :",Counter(str).most_common(3) )
