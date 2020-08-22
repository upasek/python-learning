#Write a Python program to insert a given string at the beginning of all items in a list.

def insert(list,string):
    for m in range(len(list)):
        list[m] = str(string)+ str(list[m])

    return list

list = list(map(int, input("Input the integers seprated by comma : ").split(",")))
string = input("Input the string : ")
print("\nOriginal list :",list)
print("String :",string)
print("List after inserting string :",insert(list,string))
