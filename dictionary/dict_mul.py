# Write a Python program to multiply all the items in a dictionary.

def multi(num, dis):
    mul= 1
    for m, value in dis.items():
        mul = mul * int(value)

    return mul

num = int(input("Input the number : "))
dis = {}
for m in range(97, 97 + num):
    print('%s : '%(chr(m)) , end = '')
    dis[chr(m)] = input()

print("Original dictionary :",dis)
print("Sum of all item in dictionary :",multi(num, dis))
