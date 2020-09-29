#Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
def char(string):
    length = len(string)
    if length <= 3:
        return string
    else:
        return string[:3]

string = input("Input the string : ")
print("New string :",char(string))
