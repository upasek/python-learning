# Write a Python program to print alphabet pattern 'P'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if (r == 0 or r == 3) and ( c > 0 and c < 5):
            string = string + '*'

        elif (r == 1 or r == 2) and ( c == 1 or c == 5):
            string = string + '*'

        elif (c == 1) and ( r >= 4):
            string = string + '*'

        else:
            string = string + ' '

    string = string + '\n'

print(string)
