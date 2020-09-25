#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#myself
def char(string):
    kir = string[0]
    string2 = ''
    for n in string:
        if n == kir:
            string2 = string2 + '$'
        else:
            string2 = string2 + n

    string = kir + string2[1:]
    return string

string = input("Input the string : ")
print(char(string))
