#Write a Python program to convert temperatures to and from celsius, fahrenheit.

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")

degree = int(temp[:-1])
char = temp[-1]

if char.upper() == 'C':
    result = int(round((9 * degree) / 5 + 32))
    con = "Fahrenheit"
elif char.upper() == 'F':
    result = int(round((degree - 32) * 5 / 9))
    con = "Celsius"
else:
    print("Input proper convertion")

print("The temperature in {} is {} ".format(con, result))
