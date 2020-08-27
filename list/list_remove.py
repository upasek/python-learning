# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def remove(list):
    list1 = []
    for m in list:
        index = int(list.index(m))
        if index != 0 and index != 4 and index != 5:
            list1.append(m)
    return list1


list = input("input the minimum six word seprated by comma : ").split(",")
print("Original list :",list)
print("New list :",remove(list))
