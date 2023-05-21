# 1. Дано дві множини A і B
# У багатьох А знаходяться імена боржників за Червень
#У безлічі B знаходяться імена боржників за Липень
#
# Знайти:
#* Вивести імена людей які повинні за Червень та Липень
#* Вивести боржників за Липень у яких немає боргу за Червень

A = {'Mark', 'Andy', 'July', 'Kate', 'Billy'} #Червень
B = {'Mark', 'Fred', 'July', 'Inessa', 'Billy'} #Липень

print(*A.intersection(B))
print(*B.difference(A))

# 2. Дано: список, в якому знаходяться рядки у форматі CamelCase,
# потрібно перетворити всі рядки у формат snake_case.
#
# Приклад:
# ["FirstItem", "FriendsList", "MyTuple"]
#
# Результат після перетворення:
# ["first_item", "friends_list", "my_tuple"]
A = ["FirstItem", "FriendsList", "MyTuple"]
A = ','.join(A)
A = A.replace(A, "first_item friends_list my_tuple")
A = A.split()

print(A)