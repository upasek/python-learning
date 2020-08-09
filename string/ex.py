# return the numbers of factorial x
# factorial.py
def factdata(n):
    result = []
    fact = 1
    while n > 0:
        result.append(n)
        fact = fact * n
        n = n - 1
    print("List of all element :",result)
    return fact

num = int(input("Input the integer : "))
print("The factorial of given integer :",factdata(num))
