#Write a Python script that takes input from the user and displays that input back in upper cases without using an upper() function.
def char(string):
    string1 = ""
    for str1 in string:
        for n in str1:
            ch = chr(ord(n) - 32)
            string1 = string1 + ch

        string1 = string1 + " "

    return string1


string = input("Input the string in lower case :")
string = string.split(" ")
print("The string in upper case :",char(string))
