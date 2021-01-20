#Write a Python program to sort Counter by value.

num = {'Math':81, 'Physics':83, 'Chemistry':87}
print("Original dictionary :",num)
list = []
for key, value in sorted(num.items()):
    list.append(tuple([key, value]))

print("sorted list Counter by value :",list)
