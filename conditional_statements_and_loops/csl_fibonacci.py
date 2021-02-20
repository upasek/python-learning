#Write a Python program to get the Fibonacci series between 0 to 50.

x, y = 0, 1

print("Fibonacci serirs between 0 to 50 : ", end = '')

while y < 50:
    print(y, end = ' ')
    x, y = y, x+y

print('')
