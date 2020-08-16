#Write a Python program to find common items from two lists.
def common(list1,list2):
    list = []
    for m in list1:
        if m in list2:
            list.append(m)

    return list

list1 = input("Input the words in first list seprated by comma : ").split(",")
list2 = input("Input the word in second list seprated by comma : ").split(",")
print("Common items from two lists :",common(list1,list2))
