#Write a Python program to find maximum length of consecutive 0’s in a given binary string.

#def max_consecutive_0(input_str):
    #return  max(map(len,input_str.split('1')))

#str1 = '1110000111'
#print(max_consecutive_0(str1))


def char(string):
    sum = 0
    max = 0
    for m in string:
        if m == "0":
            sum += 1
            if sum > max:
                max = sum

        elif m != "0":
            sum = 0

    return max

string = input("Input the string : ")
print("Maximum length of consecutive 0’s in a given binary string :",char(string))
