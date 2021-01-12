#. Write a Python program to filter a dictionary based on values.

num = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

print("Original dictionary :",num)

dict = {key: value for (key, value) in num.items() if value > 170 }

print("New dictionary :",dict)
