#Write a Python program that accepts a string and calculate the number of digits and letters.


string = input("Input the string : ")
count1 = 0
count2 = 0
for m in string:
    if (m >= 'a' and m <= 'z') or ( m >= 'A' and m <= 'Z' ):
        count1 += 1

    elif m >= '0' and m  <= '9':
        count2 += 1

print("Letters :",count1)
print("Digits :",count2)
