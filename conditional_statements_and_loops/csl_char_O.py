#Write a Python program to print alphabet pattern 'O'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if (c == 1 or c == 5) and ( r != 0 and r != 6):
            string = string + '*'

        elif (r == 0 or r == 6) and ( c < 5 and c > 1):
            string = string + '*'

        else:
            string = string + ' '

    string = string + '\n'

print(string)
