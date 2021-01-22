#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

dict = {}
for m in range(1, 16): dict[m] = m*m
print("New dictionary :",dict)
