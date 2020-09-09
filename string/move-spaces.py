# Write a Python program to move spaces to the front of a given string.
def char(string):
    count = 0
    str1 = ""
    for n in string:
        if n != " ":
            str1 = str1 + n

    for m in string:
        if m == " ":
            count += 1
    result = " " * count
    print("New string :",result+str1)

string = input("Input the string : ")
char(string)
