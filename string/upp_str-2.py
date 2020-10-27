#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters without using upper function.
def char(string):
    k = 0
    for n in string[:4]:
        if ord(n) >= 65 and ord(n) <= 90:
            k += 1

    if k >= 2:
        string2 = ""
        for m in string:
            if ord(m) > 90:
                string2 = string2 + chr(ord(m) - 32)
            else:
                string2 = string2 + m
        return string2
    else:
        return string


string = input("Input the word :")
print("new string :",char(string))
