# 68. write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.
def char(string):
    s1 = "";s2 = ""
    for m in string:
        index = string.index(m)
        if m not in string[index+1:] and m not in s2:#2nd condition for duplicates
            s1 = s1 + m
        elif m in string[index+1:] and m not in s2:
            s2 = s2 + m

    return s1, s2


string = input("Input the string : ")
s1, s2 = char(string)

print("First string using those character which occurs only once :",s1)
print("second string which consists of multi-time occurring :",s2)
