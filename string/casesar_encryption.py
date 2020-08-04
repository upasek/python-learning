# Write a Python program to create a Caesar encryption.
def char(string,intr):
    string2 = []
    for m in string:
        if ord(m) >= 65 and ord(m) <= 90:
            temp = int(ord(m) + intr)
            string2.append(chr(temp))
        elif ord(m) >= 97 and ord(m) <= 122:
            temp = int(ord(m) + intr)
            string2.append(chr(temp))

    return string2

string = input("Input the string :")
intr = int(input("Input the step :"))
string = list(string)
print("Output :",char(string,intr))
