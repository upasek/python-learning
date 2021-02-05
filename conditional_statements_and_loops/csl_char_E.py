#Write a Python program to print alphabet pattern 'E'.
#if ((c == 1 and ( r != 0 and r != 3 and r != 6)) or ((r == 0 or r == 6) and (c > 0 and c < 6)) or (r== 3) and (c > 0 and c < 5)):
string = ''
print("Expected output : ")

for r in range(7):
    for c in range(7):
        if ((c == 1 and ( r != 0 and r != 3 and r != 6)) or ((r == 0 or r == 6) and (c > 0 and c < 6)) or (r== 3) and (c > 0 and c < 5)):
            string = string + '*'
        else:
            string = string + ' '

    string = string + '\n'

print(string)
