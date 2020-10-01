#Write a Python program to find the first repeated character in a given string.


def char(string):

    for m in string:
        lim = int(string.index(m))
        if m in string[lim+1:] and m != " ":
            return m
            break;

string = input("Input the string : ")
print("first repeating character in given string :",char(string))
