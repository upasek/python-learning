#Write a Python program that prints each item and its corresponding type from the following list.


datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

print("Original list :",datalist,"\n")
for m in datalist:
    print("Type of {} is {} ".format(m, type(m)))
