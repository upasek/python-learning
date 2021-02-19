#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

print("By using continue statement numbers from 0 to 6 except 3 and 6 : ")
print("Expected output : ", end = '')
for m in range(7):
    if m == 3 or m == 6:
        continue;
    else:
        print(m, end = ' ')

print("")
