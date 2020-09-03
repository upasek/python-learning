#sum of all item in a list
def sum_int(list):
    sum = 0
    for m in list:
        sum = sum + int(m)

    return sum
list = input("Input the integers separated by comma : ")
list = list.split(",")
print("Sum of all item in list :",sum_int(list))
