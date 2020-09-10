#Write a Python program to remove the nth index character from a nonempty string
def char(string,index):
    if index >= len(string):
        return "Invalid index"
    else:
        return string[:index] + string[index+1:]

string = input("Input the string :")
index = int(input("Input the index :"))
print("Expected output :",char(string,index))
