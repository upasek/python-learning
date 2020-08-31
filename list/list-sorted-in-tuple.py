#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#first methode

def swap_list(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def sort(list):
    length = len(list)
    for m in list[:length]:
        index = list.index(m)
        for n in list[index + 1:]:
            if n[-1] < m[-1]:
                swap_list(list, list.index(m), list.index(n))

    return list

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("New list after sorting :",sort(list))
