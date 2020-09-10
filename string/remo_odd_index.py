#Write a Python program to remove the characters which have odd index values of a given string.

def char(string):
    string2 = ''
    for n in string:
        if string.index(n) % 2 == 0:
            string2 = string2 + n

    return string2

string = input("Input the string :")
print("new string :",char(string))
