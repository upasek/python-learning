#Write a Python program access the index of a list.
def index(list):
    for m in list:
        print("{}\t{}".format(list.index(m),m))

list = list(map(int,input("Input the integers seprated by comma : ").split(",")))

print("given list :",list)
print("\nIndex\tValue")
index(list)
