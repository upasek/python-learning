#Write a Python program to find missing and additional values in two lists.

def missing(list1,list2):
    missing1 = []; additional1 = []
    missing2 = []; additional2 = []
    for m in list1:
        if m not in list2:
            missing2.append(m)
        if m not in list2:
            additional1.append(m)

    for m in list2:
        if m not in list1:
            additional2.append(m)
        if m not in list1:
            missing1.append(m)

    print("\nMissing value in first list :",missing1)
    print("additional value in first list :",additional1)
    print("Missing values in second list :",missing2)
    print("Additional values in second list :",additional2)


list1 = input("Input character in first list seprated by comma : ").split(",")
list2 = input("Input character in second list seprated by comma : ").split(",")
missing(list1,list2)
