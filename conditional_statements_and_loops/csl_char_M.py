#Write a Python program to print alphabet pattern 'M'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(10):
        if ( c == 1 or c == 9 ) and (r != 2 and r != 3):
            string = string + '*'
        elif r == 2 and (c == 1 or c == 3 or c == 7 or c == 9 ):
            string = string + '*'
        elif r == 3 and ( c == 1 or c == 5 or c == 9):
            string = string + '*'
        else:
            string = string + ' '

    string = string + '\n'

print(string)
