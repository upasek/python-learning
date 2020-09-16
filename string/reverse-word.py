#Write a Python program to reverse words in a string.
def char(string):
    string2 = ""
    length = len(string) - 1
    for m in range(length,-1,-1):
        string2 = string2 + string[m] + " "

    return string2

string = input("Input the string : ")
string = string.split(" ")
print("New string after reverse word in string :",char(string))
