# Write a Python program to convert month name to a number of days.


month = input("Input the name of month : ")

list1 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
list2 = ['april', 'june', 'september', 'november']

if month.lower() in list1:
    print("No. of days : 31 days")
elif month.lower() in list2:
    print("No. of days : 30 days")
elif month.lower() == 'february':
    print("No. of days : 28/29 days")
