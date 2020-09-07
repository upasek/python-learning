#Write a Python program to find the maximum occurring character in a given string

def char(string):
    dict = {}
    max = 0
    temp = "none"
    for m in string:
        if m in dict and m != " ":
            dict[m] += 1
            if dict[m] > max:
                max = dict[m]
                temp = m

        elif m != " " and m not in dict:
            dict[m] = 1


    return temp

string = input("Input the string : ")
print("The maximum occuring character in a given string :",char(string))
