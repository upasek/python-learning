#Write a Python program to print alphabet pattern 'Z'.

string = ''
print("Expected output : ")
num = 5
for r in range(7):
    for c in range(7):
        if r == 0 or r == 6 :
            string += '*'
        elif c == num:
            num -= 1
            string += '*'
        else:
            string += ' '
    string += '\n'

print(string)
