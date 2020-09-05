#Write a Python program to get unique values from a list.

def unique(list):
    list1 = []
    for m in list:
        index = list.index(m)
        if m not in list[index+1:] and m not in list1:
            list1.append(m)

        elif m in list[index+1:] and m not in list1:
            list1.append(m)

    return list1


list = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("Original list :",list)
print("new unique list :",unique(list))
