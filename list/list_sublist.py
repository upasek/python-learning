#Write a Python program to check whether a list contains a sublist.

def sublist(list,sub_list):
    length1 = len(list) ; length2 = len(sub_list)
    q = 0
    for m in range(length1 - length2 + 1):
        var = 0;a = 0
        for n in range(m, length2+m):
            if list[n] == sub_list[a]:
                var += 1
                a += 1

        if var == length2:
            q = 1
            print("Sublist are present in given list.")
            break;

    if q == 0:
        print("Sublist are not present in given list.")


list = input("Input the element seprated by comma : ").split(",")
#print(list)
sub_list = input("Input the sublist : ").split(",")
sublist(list,sub_list)
