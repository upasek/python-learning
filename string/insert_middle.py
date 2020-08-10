#Write a Python function to insert a string in the middle of a string.
def char(string,stri):
    length = int(len(string) / 2)
    string2 = ""
    for n in string:
        if string.index(n) == length:
            string2 = string2 +" "+stri +" "+n
        else:
            string2 = string2 +" "+n

    return string2


string = input("Input the string :")
string = string.split(" ")
stri = input("Input another string to insert :")
print("new string :",char(string,stri))
