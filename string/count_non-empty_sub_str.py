#Write a Python program to count number of non-empty substrings of a given string.

def number_of_substrings(str):
    str_len = len(str)
    #print((str_len + 1) / 2)
    return int(str_len * (str_len + 1) / 2);

str1 = input("Input a string: ")
print("Number of substrings:",number_of_substrings(str1))
