#Write a Python program to check whether a list contains a sublist with different methode.

def sublist(list,sub_list):
    length1 = len(list); length2 = len(sub_list)
    q = 0
    for m in range(length1 - length2 + 1 ):
        if list[m:length2+m] == sub_list:
            print("Sublist are present in given list.")
            q += 1
            break;

    if q == 0:
        print("Sublist are not present in given list.")


list = input("Input the element seprated by comma : ").split(",")
#print(list)
sub_list = input("Input the sublist : ").split(",")
sublist(list,sub_list)
