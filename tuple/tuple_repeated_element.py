#Write a Python program to find the repeated items of a tuple.

def repeat(tuple,num):
    count = 0
    for m in tuple:
        if num == m:
            count += 1
    return count

tuple = tuple(map(int, input("Input the integer seprated by comma : ").split(",")))
num = int(input("Input the element : "))
print("Repeated items of a tuple :",repeat(tuple,num))
