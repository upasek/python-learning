# 69. Write a Python program to find the longest common sub-string from two given strings.

from difflib import SequenceMatcher
def char(string1,string2):

    seq_match = SequenceMatcher(None,string1,string2)

    match = seq_match.find_longest_match(0, len(string1), 0, len(string2))

    if ( match.size != 0):
        return (string1[match.a:match.a + match.size])
    else:
        return ("Longest common sub-string not present")

string1 = input("Input first string : ")
string2 = input("Input second string : ")
print(char(string1,string2))
