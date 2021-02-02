#Write a Python program to print alphabet pattern 'A'.

string = ''
print("Expected output : ")
for r in range(7):
    for c in range(6):
        if (((c== 1 or c== 5) and r != 0) or ((r == 0 or r == 3) and (c > 1 and c < 5))):
            string = string + '*'
        else:
            string = string + ' '

    string = string + '\n'

print(string)
