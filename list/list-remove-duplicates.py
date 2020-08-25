#7. Write a Python program to remove duplicates from a list.
def remove(list):
    list2 = []
    for m in list:
        index = list.index(m)
        if m in list[index+1:] and m not in list2:
            list2.append(m)

        elif m not in list[index+1:]:
            list2.append(m)

    return list2

list = list(map(int,input("Input the element seprated by comma : ").split(",")))
print("Given list :",list)
print("New list after remove duplicates :",remove(list))
