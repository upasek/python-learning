#Write a Python program to count number of items in a dictionary value that is a list.

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2', 'subj3']}
print("Original dictionary :",dict)
count = 0
for values in dict.values():
    count += len(values)

print("Number of items in a dictionary value that is a list is :",count)
