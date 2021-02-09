#Write a Python program to print alphabet pattern 'U'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if ( (c == 1 or c == 5) and r != 6 ) or ( r== 6 and ( c > 1 and c < 5)) :
            string += '*'
        else:
            string += ' '
    string += '\n'

print(string)
