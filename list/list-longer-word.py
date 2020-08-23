#Write a Python program to find the list of words that are longer than n from a given list of words.
def long(string,n):
    string = string.split(" ")
    list = []
    for item in string:
        if len(item) > n:
            list.append(item)

    return list

string = input("Input the string : ")
n = int(input("Input the size of word : "))
print("List of words that are longer than n from a given list of words :",long(string,n))
