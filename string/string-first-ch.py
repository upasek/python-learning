#Write a Python program to find the first non-repeating character in given string.
def char(string):

    for m in string:
        lim = int(string.index(m))
        if m not in string[lim+1:] and m != " ":
            return m
            break;

string = input("Input the string : ")
print("first non-repeating character in given string :",char(string))
