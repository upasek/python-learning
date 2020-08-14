#Write a Python program to change the position of every n-th value with the (n+1)th in a list.
def swap(list,m,n):
    list[m], list[n] = list[n],list[m]
    return list

def change(list):
    length = len(list) - 1
    for m in range(0,length,2):
        swap(list,m,m+1)

    return list

list = list(map(int,input("Input the integers sepreted by comma : ").split(",")))
print("New list after changes position :",change(list))
