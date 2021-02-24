#10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

print("Expected output : ")
for m in range(51):
    if m % 3 == 0 and m % 5 == 0:
        print("fizzbuzz")
    elif m % 3 == 0:
        print("fizz")
    elif m % 5 == 0:
        print("buzz")
    else:
        print(m)
