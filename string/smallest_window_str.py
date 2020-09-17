#75. Write a Python program to find smallest window that contains all characters of a given string.
#not perfectly work
def char(string):
    dict = {}
    string2 = ""
    for m in string:
        index = string.index(m)
        if m not in string[index+1:]:
            string2 = string2 + m
        elif m in string[index+1:] and m not in dict:
            dict[m] = 1
            string2 = string2 + m
    return string2

string = input("Input the string : ")
print(char(string))
