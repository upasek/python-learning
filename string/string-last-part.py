#Write a Python program to get the last part of a string before a specified character.
def char(string,ch):
    length = int(len(string) - 1)
    for n in range(length,-1,-1):
        if string[n] == ch:
            return string[:n]
            break;


string = input("Input the string :")
ch = input("Input the specific character :")
print("New string :",char(string,ch))
