#Write a Python program to find the median of three values.

print("Input first number : ", end = '')
x = float(input())
print("Input second number: ", end = '')
y = float(input())
print("Input third number: ",end = '')
z = float(input())

if (x > y and x < z) or ( x < y and x > z):
    print("The median is ",x)
elif (y > x and y < z) or ( y < x and y > z):
    print("The median is ",y)
elif (z > x and z < y) or (z < x and z > y):
    print("The median is ",z)
