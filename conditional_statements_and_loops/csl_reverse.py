#Write a Python program that accepts a word from the user and reverse it.


word = input("input the word : ")

print("Original word :",word)

list = ''

length = len(word)

for m in range(-1, -(length+1), -1):
    list = list + word[m]

print("New word :",list)
