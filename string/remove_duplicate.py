#61. Write a Python program to remove duplicate characters of a given string.
def char(string):
    string2 = ""
    for m in string:
        index = string.index(m)
        if m not in string[index+1:] and m not in string2:
            string2 = string2 + m

        elif m in string[index+1:] and m not in string2:
            string2 = string2 + m

    return string2

string = input("Input the string : ")
print("New string :",char(string))
