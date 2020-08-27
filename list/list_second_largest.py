#28. Write a Python program to find the second largest number in a list.

def swap(list, i, index):
    list[i], list[index] = list[index], list[i]
    return list

def large(list):
    if (len(list) < 2):
        return
    if (len(list) == 2) and (list[0] == list[1]):
        return

    i = 0
    while i < 2:
        max = list[i]
        for n in list[i+1:]:
            if max < n:
                max = n
                index = list.index(n)
                swap(list,i, index)

        i += 1

    return list[1]

list =list(map(int,input("Input the integer seprated by comma : ").split(",")))
print("Second largest number in a list :",large(list));
