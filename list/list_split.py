#Write a Python program to split a list based on first character of word.
def split(list):
    list1 = ""
    list = sorted(list)
    for m in list:
        if m[0] not in list1:
            print("\n"+m[0],end = " : ")
            for item in list:
                if item[0] == m[0]:
                    print(item, end = ' ')
                    list1 = list1 + str(m[0])

                elif item[0] > m[0]:
                    break;
    print("\n")

list = input("Input the words seprated by comma : ").split(",")
print("After spliting :")
split(list)
