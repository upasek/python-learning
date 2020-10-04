#.Write a Python program to find the first repeated word in a given string.
def char(string):
    str1 = string.split(" ")
    for m in str1:
        index = str1.index(m)
        if m in str1[index+1:]:
            return m
            break;

string = input("Input the string : ")
print("First repeated word in a given string :",char(string))
