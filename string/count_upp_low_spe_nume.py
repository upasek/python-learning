#73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.

def char(string):
    count_upp = 0;count_low = 0;count_num = 0;count_spe = 0
    for item in string:
        if item.isupper():
            count_upp += 1
        elif item.islower():
            count_low += 1
        elif item.isdigit():
            count_num += 1
        else:
            count_spe += 1

    return count_upp, count_low, count_num, count_spe


string = input("Input the string : ")
print("\nOriginal string :",string)
u, l, n, s = char(string)

print("\nUpper case characters :",u)
print("Lower case characters :",l)
print("Number case :",n)
print("Special case character :",s)
