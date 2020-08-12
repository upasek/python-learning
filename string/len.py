def substring_copy(str, n):
    flen = 2
    result = ''

    if flen > len(str):
        flen = len(str)

    substr = str[:flen]
    for i in range(n):
        result = result + substr

    return result

str = input("Input the string : ")
n = int(input("Input the repetation of new substring : "))
print("New string :",substring_copy(str, n))
