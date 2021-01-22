#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

num = int(input("Input the range : "))
dict = {}
for m in range(1, num+1):
    dict[m] = m*m

print("Expected output :",dict)
