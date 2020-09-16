#Write a Python function to reverses a string
def char(string):
    string2 = ""
    length = int(len(string) - 1)
    for n in range(length,-1,-1):
        string2 = string2 + string[n]

    return string2


string = input("Input the string :")
print("New string :",char(string))
