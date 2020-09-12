# 67. Write a Python program to remove all consecutive duplicates of a given string.
def char(string):
    str1 = ""
    length = len(string)
    for m in range(0,length):
        if m == 0 :
            str1 = str1 + string[m]

        elif string[m] != string[m-1]:
            str1 = str1 + string[m]
    return str1

string = input("Input the string : ")
print("New string :",char(string))
