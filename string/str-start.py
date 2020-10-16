#Write a Python program to check whether a string starts with specified characters.
def char(string,start):
    length = len(start)
    return string[:length] == start

string = input("Input the string :")
start = input("String start with :")
print(char(string,start))
