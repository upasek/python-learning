#Write a Python program to slice a tuple.

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
slice = tuplex[3:5]
print(slice)

slice = tuplex[:6]
print(slice)

slice = tuplex[5:]
print(slice)

slice = tuplex[:]
print(slice)

slice = tuplex[-8:-4]
print(slice)

#nwew tuple
tuplex = tuple("HELLO WORLD")
print(tuplex)

slice = tuplex[2:9:2]
print(slice)

slice = tuplex[::4]
print(slice)

slice = tuplex[9:2:-4]
print(slice)
