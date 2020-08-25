# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove(list):
    list2 = []
    for m in list:
        if m % 2 != 0:
            list2.append(m)

    return list2

list = list(map(int,input("Input the element seprated by comma : ").split(",")))
print("Original list :",list)
print("New list :",remove(list))
