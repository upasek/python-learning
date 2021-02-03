#Write a Python program to print alphabet pattern 'D'.

string = ''
print("Expected output : ")
for r in range(0, 7):
    for c in range(0, 6):
        if ((( c==1 or c== 5) and  ( r != 0 and r != 6 )) or (( r == 0 or r == 6) and ( c > 0 and c < 5))):
            string = string + '*'
        else:
            string = string + ' '

    string = string + '\n'

print(string)
