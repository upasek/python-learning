#Write a Python program to unzip a list of tuples into individual lists.

#create a tuple
l = [(1,2), (3,4), (8,9)]
print(l)
print (list(zip(*l)))
