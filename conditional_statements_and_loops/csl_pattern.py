#Write a Python program to construct the following pattern, using a nested loop number.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

print("Expected output : ")
num = 1
for r in range(1, 10):
    for c in range(1, 10):
        if c <= r:
            print(num, end = '')
    num += 1
    print("")

