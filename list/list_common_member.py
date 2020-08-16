#11. Write a Python function that takes two lists and returns True if they have at least one common member.

def common(list1,list2):
    for m in list1:
        if m in list2:
            return True


list1 = list(map(int,input("Input the integers seprated by comma : ").split(",")))
list2 = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("Result :",common(list1,list2))
