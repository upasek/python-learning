#Write a Python program to compute sum of digits of a given string.
#here x.isdidit() function also we can use
def char(string):
    digit = "0123456789"
    sum = 0
    for m in string:
        if m in digit:
            sum = sum + int(m)

    return sum

string = input("Input the string : ")
print("Sum of digits of a given string :",char(string))
