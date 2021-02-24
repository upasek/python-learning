#Write a Python program to check a string represent an integer or not

import re

string = input("Input the string : ")

if re.search('[a-z]', string):
    print("The string is not an integer.")
elif re.search('[A-Z]', string):
    print("The string is not an integer.")
else:
    print("The string is an integer.")
