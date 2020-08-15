#Write a python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print("First list :",list1)
print("Second list :",list2)
print("Third list :",list3)


print('\nCompare list1 and list2 (list2 in lis1) ')
#print(' '.join(map(str, list2)))
#print(' '.join(map(str, list1 * 2)))
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3 (list3 in list1) ')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
