#Write a Python program to get the key, value and item in a dictionary.

num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Original dictionary :",num)
print("key\tvalue\tcount")
for m in num:
    print(m, end ='\t')
    print(num[m], end = '\t')
    print(m)
