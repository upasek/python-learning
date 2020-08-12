#Write a Python function that takes a list of words and returns the length of the longest one.

def char(string):
    length = len(string[0])
    stri = string[0]
    for n in string[1:]:
        if len(n) > length:
            length = len(n)
            stri = n

    return length, stri

string = input("Input the string : ")
string = string.split(" ")
print("The list of words :",string)
length, stri = char(string)
print("The length of the longest one :",length)
print("The longest word is :",stri)
