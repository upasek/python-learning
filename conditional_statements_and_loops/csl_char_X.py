#Write a Python program to print alphabet pattern 'X'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if (  ( c == 1 or c == 5)  and ( r < 2 or r > 4 ) ):
            string += '*'
        elif ( r == 2 or r == 4) and ( c == 2 or c == 4):
            string += '*'
        elif r == 3 and c == 3:
            string += '*'
        else:
            string += ' '
    string += '\n'

print(string)
