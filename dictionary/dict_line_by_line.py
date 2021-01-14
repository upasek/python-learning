#Write a Python program to print a dictionary line by line.

students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for m in students:
    print(m)
    for key, value in students[m].items():
        print( str(key) + ' : ' + str(value) )
