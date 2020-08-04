#Write a Python program to capitalize first and last letters of each word of a given string.
def char(string):
    string2 = ""
    str1 = string.split(" ")
    for m in str1:
        length = int(len(m) - 1)
        string2 = string2 + m[0].upper() + m[1:length]+m[length].upper() + " "

    return string2


string = input("Input the string : ")
print("New string :",char(string))
