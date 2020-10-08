#Write a python program to count repeated characters in a string.

def char(string):
    dict = {}
    for m in string:
        if m in dict and m != " ":
            dict[m] += 1
        elif m != " ":
            dict[m] = 1
    print("\ncounting of repeating character in a string is ....")
    for m in dict:
        if dict[m] > 1:
            print("{}  {}".format(m,dict[m]))


string = input("Input the string : ")
char(string)
