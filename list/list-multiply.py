# Write a Python program to multiplies all the items in a list
def mul_int(list):
    mul = 1
    for m in list:
        mul = mul * int(m)

    return mul

list = input("Input the integers separeted by comma : ")
list = list.split(",")
print("multplication of all item in list :",mul_int(list))
