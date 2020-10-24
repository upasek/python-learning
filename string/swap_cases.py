#Write a Python program to swap cases of a given string.
def char(string):
    string2 = ""
    for item in string:
        if ord(item) >= 65 and ord(item) <= 90:
            string2 = string2 + chr(ord(item) + 32)
        elif ord(item) >= 97 and ord(item) <= 122:
            string2 = string2 + chr(ord(item) - 32)
        else:
            string2 = string2 + " "

    return string2


string = input("Input the string : ")
print("New string :",char(string))
