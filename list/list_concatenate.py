#54. Write a Python program to concatenate elements of a list.
def conc(list,ch):
    list1 = ""
    for m in range(len(list)):
        if m == 0:
            list1 = list1 + list[m]
        else:
            list1 = list1 + ch + list[m]
    return list1

list = input("Input words seprated by comma : ").split(",")
ch = input("Input the symbol for concatenate the list : ")
print("Output after concatenate :",conc(list,ch))
