#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

item = []
print("Input the binary number separated by comma : ", end = '')
num = [ x for x in input().split(",")]

print("The ogirinal list of binary number : " + ','.join(num))

for p in num:
    x = int(p, 2)
    if x % 5 == 0: #if not x%5:
        item.append(p)

print("The numbers that are divisible by 5 : " + ",".join(item))
