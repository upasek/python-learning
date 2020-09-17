#. Write a Python program to find smallest and largest word in a given string.
def char(string):
    str1 = string.split(" ")
    max = int(len(str1[0]))
    min = int(len(str1[0]))
    for m in str1:
        length = len(m)
        if length > max:
            max = length
            max_word = m
        if length < min:
            min = length
            min_word = m

    print("Largest word in a given string :",max_word)
    print("Smallest word in a given string :",min_word)


string = input("Input the string : ")
char(string)
