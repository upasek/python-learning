#Write a Python program to create the multiplication table (from 1 to 10) of a number.

number = int(input("Input the number : "))
num = 1
while num <= 10:
    print( "{} x {} = {}".format( number, num, number*num) )
    num += 1
