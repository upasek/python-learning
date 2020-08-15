#Write a Python program to clone or copy a list.
def clone(list):
    list2 = []
    for m in list:
        list2.append(m)
    return list2

list = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("Original list :",list)
print("New list :",clone(list))
