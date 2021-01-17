#Write a Python program to remove a key from a dictionary.

myDict = {'a':1,'b':2,'c':3,'d':4,'e':5}
print("Original dictionary :",myDict)
stri = input("InPut the key which is remove from dictionary : ")
if stri in myDict:
    del myDict[stri]

print("New dictionary :",myDict)
