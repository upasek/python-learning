#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
def char(string1, string2):
    a = string2[:2] + string1[2:]
    b = string1[:2] + string2[2:]

    return a + ' ' + b

string1 = input("Input the string :")
string2 = input("Input the string :")
print("The given strings are :{},{}".format(string1,string2))
print(char(string1, string2))
