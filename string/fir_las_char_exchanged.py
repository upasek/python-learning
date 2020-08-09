#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def char(string):
    length = len(string)
    first = string[0]
    last = string[length - 1]
    return last + string[1:length-1] + first

string = input("Input the string :")
print("New string :",char(string))
