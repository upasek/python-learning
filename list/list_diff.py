#19. Write a Python program to get the difference between the two lists.
def diff(list1,list2):
    diff_list1_list2 = list(set(list1) - set(list2))
    diff_list2_list1 = list(set(list2) - set(list1))
    total_diff = diff_list1_list2 + diff_list2_list1
    return total_diff



list1 = list(map(int,input("Input the integers seprated by comma : ").split(",")))
list2 = list(map(int,input("Input the integers seprated by comma : ").split(",")))
print("New list :",diff(list1,list2))
