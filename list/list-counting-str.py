#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def count_str(list):
    count = 0
    for str in list:
        if len(str) > 1 and str[0] == str[-1]:
            count += 1
    return count


list = input("Input the string seprated by comma : ")
list = list.split(",")
print("Number of string :",count_str(list))
