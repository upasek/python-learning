#4. Write a Python program to construct the following pattern, using a nested for loop.


num = int(input("Input the number of rows : "))

print("pattern.....")

for m in range(num+1):
    for n in range(m):
        print("*", end = ' ')
    print("")

for m in range(num-1, 0, -1):
    for n in range(m):
        print("*",end = ' ')
    print("")
