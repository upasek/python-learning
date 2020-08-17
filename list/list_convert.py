#. Write a Python program to convert a list of multiple integers into a single integer.
def convert(list):
    value = ""
    for m in list:
        value = value + str(m)

    return value

list = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("Original list :",list)
print("single integer :",convert(list))
