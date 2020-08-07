# Write a Python program to count the occurrences of each word in a given sentence.
def char(string):
    dict = {}
    for n in string:
        if n in dict.keys():
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

string = input("Input the string :")
string = string.split(" ")
print("Occurrences of each word in a given sentence :",char(string))
