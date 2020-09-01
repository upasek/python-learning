#Write a Python program to convert a pair of values into a sorted unique array.

def convert(list):
    list1 = []
    for m in list:
        for n in m:
            if n not in list1:
                list1.append(n)

    return list1

list = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
print("Original list :",list)
print("New list :",convert(list))
