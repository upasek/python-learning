#Write a Python program to print alphabet pattern 'L'.

string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if ( c == 1 or (r == 6 and c != 0 and c != 6)):
            string = string + '*'
        else:
            string = string + ' '
    string = string + '\n'

print(string)
