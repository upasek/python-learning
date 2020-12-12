tuple = tuple(map(int,input("Input the integer : ").split(",") ))
print(tuple)
tuple = tuple + (3,)
print(tuple)
string = ""
for m in tuple:
    string = string + str(m)
print(string)
