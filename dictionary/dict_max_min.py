#Write a Python program to get the maximum and minimum value in a dictionary.

num = {'v':1000, 'w':2000, 'x':500, 'y':5874, 'z': 560}
print("Original dictionary :",num)
max = num['v']
min = num['v']
for m in num:
    if max < int(num[str(m)]):
        max = num[str(m)]

    if min > int(num[str(m)]):
        min = num[str(m)]

print("Maximum value :",max)
print("Minimum value :",min)
