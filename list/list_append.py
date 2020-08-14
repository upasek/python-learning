#Write a Python program to append a list to the second list.
def append(list1,list2):
    for m in list2:
        list1.append(m)

    return list1

list1 = input("Input first list seprated by comma : ").split(",")
list2 = input("Input second list seprated by comma : ").split(",")
print("New list :",append(list1,list2))
