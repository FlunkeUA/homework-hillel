print("Завдання 1:")

A = {'Mark', 'Andy', 'July', 'Kate', 'Billy'} #Червень
B = {'Mark', 'Fred', 'July', 'Inessa', 'Billy'} #Липень

print(*A.intersection(B))
print(*B.difference(A))

print("\nЗавдання 2:")

A = ["FirstItem", "FriendsList", "MyTuple"]
print(A)

A_new = []
for i in A:
    letter = ''
    letter += i[0].lower()
    letter += i[1:]
    A_new.append(letter)

A = ','.join(A_new)

B = ''
for i in A:
    if (i.isupper()):
        B += '_' + i.lower()
    else:
        B += i

B = B.split(',')

print(B)
