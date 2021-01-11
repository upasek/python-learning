#Write a Python program to drop empty Items from a given Dictionary.

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None, 'c4' :None}

print("Original dictionary :",dict1)

dict1 = {key: value for (key, value) in dict1.items() if value is not None }

print("New dictionary :",dict1)
