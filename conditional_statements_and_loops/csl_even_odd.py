#Write a Python program to count the number of even and odd numbers from a series of numbers.

num = tuple(map(int, input("Input the integers separated by comma : ").split(',')))
even = []; count1 = 0
odd = []; count2 = 0
print("\nOriginal list of all integers :",num)

for m in num:
    if m % 2 == 0:
        even.append(m)
        count1 += 1
    elif m % 2 != 0:
        odd.append(m)
        count2 += 1

print("Number of even numbers :",count1)
print("List of all even element :",tuple(even))
print("Numbers of odd numbers :",count2)
print("List of all odd element :",tuple(odd))
