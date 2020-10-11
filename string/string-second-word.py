#Write a Python program to find the second most repeated word in a given string.

def char(string):
    str1 = string.split(" ")
    count = 1
    for m in str1:
        index = str1.index(m)
        if m in str1[index+1:]:
            temp = m
            count += 1

        if count == 2:
            return temp
            break;

string = input("Input the string : ")
print("Second most repeated word in a given string :",char(string))
