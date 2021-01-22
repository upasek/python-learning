#10. Write a Python program to sum all the items in a dictionary.

def sum(num, dis):
    sum = 0
    for m, value in dis.items():
        sum = sum + int(value)

    return sum

num = int(input("Input the number : "))
dis = {}
for m in range(97, 97 + num):
    print('%s : '%(chr(m)) , end = '')
    dis[chr(m)] = input()

print("Original dictionary :",dis)
print("Sum of all item in dictionary :",sum(num, dis))
