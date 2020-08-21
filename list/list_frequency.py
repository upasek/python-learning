#30. Write a Python program to get the frequency of the elements in a list.

def frequency(list):
    dict = {}
    for m in list:
        if m in dict:
            dict[m] += 1
        elif m not in dict:
            dict[m] = 1

    for m in dict:
        print("{} : {}".format(m,dict[m]))


list = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("Frequency of all element :")
frequency(list)
