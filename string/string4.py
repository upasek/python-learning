#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def char(string):
    return string[-2:]*4

string = input("Input the word :")
print("new string :",char(string))
