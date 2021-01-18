#Write a Python program to remove spaces from dictionary keys.

list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary :",list)
list1 = {}
for m in list:
    li = ''
    for n in m:
        if n != ' ':
            li += n
    list1[li] = list[m]

print("New dictionary :",list1)
