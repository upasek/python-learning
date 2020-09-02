#21. Write a Python program to convert a list of characters into a string.
def stri(list):
    string = ""
    for m in list:
        string = string + str(m)
    return string

list = list(map(str,input("Input the character seprated by comma : ").split(",")))
print("String by character in string :",stri(list))
