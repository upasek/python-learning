print("Enter a set of tuple (x, y) : ")
a = [ tuple(map(int, input ("x : " ).split(","))) for x in range(5) ]
print(a)
