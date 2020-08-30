# Write a Python program to get the smallest number from a list
def small_int(list):
    smallest = int(list[0])
    for m in list:
        if int(m) < int(smallest):
            smallest = m

    return smallest


list = input("Input the element seprated by comma : ")
list = list.split(",")
print("Smallest number in list :",small_int(list))
