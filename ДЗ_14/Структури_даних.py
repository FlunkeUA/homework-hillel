# print("Завдання 1:")
#
# june = {'Mark', 'Andy', 'July', 'Kate', 'Billy'} #Червень
# july = {'Mark', 'Fred', 'July', 'Inessa', 'Billy'} #Липень
#
# print(*june.intersection(july))
# print(*july.difference(june))

print("\nЗавдання 2:")

a = ["FirstItem", "FriendsList", "MyTuple"]
#a = " ".join(a)
print(a)

# a_new = []
# for i in a:
#     letter = ''
#     letter += i[0].lower()
#     letter += i[1:]
#     a_new.append(letter)
#
# b = ''
# for i, item in a:
#     if i.isupper():
#         b = '_' + i.lower()
#     else:
#         b += i

#b = b.split(',')

# print(b)

snake_case = ""
for i, c in enumerate(camel_case):
    if i == 0:
        snake_case += c.lower()
    elif c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c
