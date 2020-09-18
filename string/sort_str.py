#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

string = input("Input the comma separated sequence of word :")
string = string.split(",")
print("The unique words in sorted form : " + ",".join(sorted(list(set(string)))))


#word = [word for word in string.split(",")]
#print(",".join(sorted(list(set(word)))))
