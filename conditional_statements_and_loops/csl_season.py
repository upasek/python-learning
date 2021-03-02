#Write a Python program that reads two integers representing a month and day and prints the season for that month and day

month = input("Input the name of month : ")

if month.lower() in ('june', 'july', 'august', 'september'):
    print("Season is spring.")

elif month.lower() in ('october', 'november', 'december', 'january'):
    print("Season is winter.")

elif month.lower() in ('february', 'march', 'april', 'may'):
    print("Season is summer.")

