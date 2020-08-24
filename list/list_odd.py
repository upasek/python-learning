#Write a Python program to select the odd items of a list.

def odd(list):
    list1 = []
    for m in list:
        if m % 2 != 0:
            list1.append(m)

    return list1

list = list(map(int,input("Input the integer seprated by comma : ").split(",")))
print("Odd items of a list :",odd(list))
