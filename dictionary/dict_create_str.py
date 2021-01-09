# Write a Python program to create a dictionary from a string.
def string(stri):
    dict = {}
    for m in stri:
        if m in dict:
            dict[m] += 1
        else:
            dict[m] = 1

    return dict

stri = input("Input the string : ")
print("Dictionary from a string :",string(stri))
