#Write a Python program to count and display the vowels of a given text

def char(string):
    vowel = 'aeiouAEIOU'
    count = 0
    str1 = ""
    for m in string:
        if m in vowel:
            str1 = str1 + m
            count += 1
    print("Counting of vowel in given string :",count)
    print("list of vowel present in given string :",list(str1))

string = input("Input the string : ")
char(string)
