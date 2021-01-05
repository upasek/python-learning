#Write a Python program to check multiple keys exists in a dictionary.

student = {'name': 'Alex','class': 'V','roll_id': '2'}
num1 = {'class', 'name'}
num2 = {'name', 'Alex'}
num3 = {'roll_id', 'name'}

print( num1 <= student.keys() )
print( num2 <= student.keys() )
print( num3 <= student.keys() )
