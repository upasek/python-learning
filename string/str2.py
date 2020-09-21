#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def char(string):
    kir = string[0]
    string = string.replace(kir,'$')
    string2 = kir + string[1:]
    return string2

string = input("Input the string : ")
print("Output :",char(string))
