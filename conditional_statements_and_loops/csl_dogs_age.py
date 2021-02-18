#Write a Python program to calculate a dog's age in dog's years.
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.


h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)
