def char(string,n):
    if n < 2:
        print("Empty string")

    else:
        str2 = string[:2] + string[-2:]
        print("Output :",str2)

string = input("Iput the string : ")
char(string, len(string))
