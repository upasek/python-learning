#Write a Python program to sort a tuple by its float element.

def swap(m, n, list):
    list[m], list[n] = list[n], list[m]
    return list

def sort(list):
    length = len(list)
    for m in list[:length]:
        index = list.index(m)
        for n in list[index+1:]:
            if m[-1] < n[-1]:
                swap(list.index(m), list.index(n), list)

    return list

list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item4', '30.45'), ('item', '17.65')]
print("Original list :",list)
print("\nNew list :",sort(list))
