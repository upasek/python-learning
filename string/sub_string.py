# Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'.
def char(string,sub_str):
    length = len(string)
    length2 = len(sub_str)
    for m in range(0,length):
        if string[m:m+length2] == sub_str:
            return m
            break;

string = input("Input the string : ")
sub_str = input("Input the string : ")
print("Index of a given string at which a given substring starts :",char(string,sub_str))
