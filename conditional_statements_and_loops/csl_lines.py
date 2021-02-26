#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in upper case).

lines = []
print("Input the strings : ")
while True:
    l = input()
    if l:
        lines.append(l.upper())

    else:
        break;

print("Expected output : ")
for l in lines:
    print(l)
