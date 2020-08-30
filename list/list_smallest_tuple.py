#60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
def small(list):
    min = list[0][1]; tup = list[0]
    for m in range(len(list)):
        if min > list[m][1]:
            min = list[m][1]; tup = list[m]
    return tup

list = [(4, 1), (1, 2), (6, 0)]
print("Original list of tuple :",list)
print("Smallest second index value from a list of tuples :",small(list))
