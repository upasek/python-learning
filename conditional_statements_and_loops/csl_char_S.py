#Write a Python program to print the following patterns 'S'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if ( (r == 0) and (c > 1 and c < 6) ) or ( (r == 6) and ( c > 0 and c < 5 ) ):
            string += '*'
        elif ( (r == 1 or r == 2) and ( c == 1)) or ( (r == 4 or r ==5 ) and ( c == 5)):
            string += '*'
        elif ( r== 3 and ( c > 1 and c < 5)):
            string += '*'
        else:
            string += ' '
    string = string + '\n'
print(string)

row = 15
col = 17
string2 = ''
for r in range(row):
    for c in range(col):
        if (( r >= 0 and r <= 2 ) or ( r>=6 and r<=8 ) or ( r >= 12 and r <= 14) ) and  ( c >= 0 and c <= 16):
            string2 += 'o'
        elif ( (r>=3 and r<=5) and ( c >= 0 and c<=3) or  ( ( r>=9 and r<= 11) and ( c >= 13 and c <= 16) )):
            string2 += 'o'
        else:
            string2 += ' '
    string2 += '\n'

print(string2)
