def char(str1):
    dict = {}
    for n in str1:
        num = dict.keys()
        #print(num)
        if n in num:
            dict[n] += 1
        else:
            dict[n] = 1

    return dict

string = input("Input the string : ")
print("Length of string = ",len(string))
print(char(string))
