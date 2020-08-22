#3. Write a Python program to get the largest number from a list.
def largest_num(list):
    largest = int(list[0])
    for m in list:
        if int(m) > int(largest):
            largest = m

    return largest


list = input("Input the element separated by comma : ")
list = list.split(",")
print("Largest number in list :",largest_num(list))
