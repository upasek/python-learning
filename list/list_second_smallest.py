#Write a Python program to find the second smallest number in a list

def swap(list, i, index):
    list[i], list[index] = list[index], list[i]
    return list

def small(list):
    if (len(list) < 2):
        return
    if (len(list) == 2) and (list[0] == list[1]):
        return

    i = 0
    while i < 2:
        min = list[i]
        for n in list[i+1:]:
            if min > n:
                min = n
                index = list.index(n)
                swap(list,i, index)

        i += 1

    return list[1]



list = list(map(int,input("Input the integer seprated by comma : ").split(",")))
print("Second smallest number in list :",small(list))
