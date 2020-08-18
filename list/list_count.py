#Write a Python program to count the number of elements in a list within a specified range.

def count(list,low,high):
    count = 0
    for m in list:
        if low <= m <= high:
            count += 1
    return count


list = list(map(int, input("Input the integers seprated by comma : ").split(",")))
low = int(input("Input the lowest range : "))
high = int(input("Input the highest range : "))
print("Number of elements in a list within a specified range is :",count(list,low,high))
