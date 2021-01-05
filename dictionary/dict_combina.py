#Write a Python program to combine values in python list of dictionaries.


num = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

print("Original list :",num)
num2 = {}
for m in num:
    if m['item'] in num2:
        num2[m['item']] += m['amount']
    else:
        num2[m['item']] = m['amount']

print("\nNew dictionary :",num2)
