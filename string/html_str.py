#Write a Python function to create the HTML string with tags around the word(s).
def char(string,ch):

    return "<%s>%s</%s>"%(ch,string,ch)

string = input("Input the string :")
ch = input("Input the character :")
print("HTML string with tags around the word :",char(string,ch))
