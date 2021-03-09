# Write a Python program to check a triangle is equilateral, isosceles or scalene.


print("Input lengths of the triangle sides : ")
x = int(input())
y = int(input())
z = int(input())

if x == y == z:
    print("Equilateral triangle")

elif x != y != z:
    print("Scalene triangle")

elif x == y or y == z or x == z:
    print("Isosceles triangle")
