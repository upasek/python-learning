# Write a Python program to print the index of the character in a string.

string = input("Input the string : ")
for m in string:
    if m != " ":
        print("Current character {} possition at {} ".format(m,string.index(m)))
