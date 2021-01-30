#Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

row = int(input("Input the number of rows : "))
col = int(input("Input the number of columns : "))

array = [[0 for c in range(col)] for r in range(row) ]

for r in range(row):
    for c in range(col):
        array[r][c] = r * c

print("Expected output :",array)
