#20. Write a Python program to print all unique values in a dictionary.


dis =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

print("Original dictionary :",dis)
dis1 = []
for key in dis:
    for value in key.values():
        if value not in dis1:
            dis1.append(value)

print("New dictionary :",set(dis1))
