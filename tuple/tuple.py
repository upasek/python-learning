#Write a Python program to remove an empty tuple(s) from a list of tuples.

l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = []
for m in l:
    if m != ():
        L.append(m)

print(L)
