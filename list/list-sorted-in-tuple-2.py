#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#second method

def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("New list after sorting :",sort_list_last(tuples))
