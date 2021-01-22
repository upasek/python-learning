#Write a Python program to print a dictionary in table format.

dis = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for m in dis:
    print(m, end = ' ')

print("\n")
val = 0

for m in dis:
    for values in dis.values():
        print(values[val], end = '  ')
    print("\n")
    val += 1
