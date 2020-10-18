#Write a Python program to count occurrences of a substring in a string without using count() function.
#string = "str str is a normal"
#print(string.count("str")) = 2

def char(string,sub_str):
    length = len(sub_str)
    length2 = len(string)
    count = 0
    for m in range(0,length2):
        if string[m:m+length] == sub_str:
            count += 1

    return count

string = input("Input the string :")
sub_str = input("Input the substring :")
print("occurrences of a substring in a string is :",char(string,sub_str))
