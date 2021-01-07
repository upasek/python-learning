#Write a Python program to count the values associated with key in a dictionary.

student = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
print("Original dictionary :",student)
sum = 0
for m in student:
    if m['success'] == True:
        sum += 1

print("\nCounting of values associated with key in a dictionary is :",sum)
