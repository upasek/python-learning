#Write a Python program to replace dictionary values with their average.

student = [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82}, {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74}, {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86} ]

print("Original dictionary :",student)

for m in student:
    n1 = m.pop('V')
    n2 = m.pop('VI')
    m['V+VI'] = (n1 + n2) / 2

print("New dictionary :",student)
