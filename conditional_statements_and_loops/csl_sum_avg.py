#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

print("Input some integers to calculate their sum and average. Input 0 to exit.")

sum = 0.0
count = 0
num = 1

while num != 0:
    num = int(input(""))
    sum = sum + num
    count += 1

if count == 0:
    print("Input some numbers .")

else:
    print("Average of the above numbers are : {}".format( sum / (count - 1)))
    print("The sum of above numbers are : {}".format( sum ))
