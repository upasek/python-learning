#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def char(string):
    length = len(string)
    if length < 3:
        return string

    elif string[-3:] == 'ing':
        return string + 'ly'

    else :
        return string + 'ing'

string = input("Input the string : ")
print("Expectrd output :",char(string))
