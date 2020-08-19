#Write a Python program to flatten a shallow list.
def flatten(list):
    list1 = []
    for m in list:
        index1 = list.index(m)
        for n in m:
            index2 = m.index(n)
            list1.append(list[index1][index2])

    return list1

list = [[2,4,3],[1,5,6], [9], [7,9,0]]
print("Original list :",list)
print("New list :",flatten(list))
