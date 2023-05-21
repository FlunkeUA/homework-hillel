# n = int(input('введіть кількість цифр = '))
# i = 1
# sum = 0
#
# while n > i:
#     if i % 3 == 0:
#         sum = sum + i
#         print(i, end = ' ')
#     i += 1
# print('\nСума =', sum)

# while n > i:
#     print(i, end=' ')
#     i += 1
#     sum = sum + i
# print(sum)

# print("Перевірка на поліндром/не поліндром")
# word = input("Введіть текст: ").lower()
# re_word = word[::-1].lower()
# print("палиндром" if re_word == word else "не палиндром")
#
# print("\nЗнайти слово в тексті")
# text = input("Введіть текст: ").lower()
# word = input("Введіть слово: ").lower()
# print("yes" if word in text else "no")
#
# print("\nЗаміна та додавання тексту")
# text = input("Введіть текст: ").lower()
# print(text[:3].replace('abc', 'www')+text[3:] if "abc" in text[:3] else text+"qqq")
#
# print("\nВидалення цифр")
# text = input("Введіть текст: ").lower()
# print(''.join([x for x in text if not x.isdigit()]))
#
# print("\nПеревірка пошти")
# email = input("Введіть email: ").lower()
# print("No" if "." not in email or "@" not in email else "Yes")

# N = input("Введіть п'ять чисел, через пробіл: ").split()
# A = list(map(int, N))
# C = []
#
# for i in A:
#     if i > 5:
#         C.append(i)
#
# print("Всі числа:",*A, "\nЧисла білше п`яти:",*C)

# print("Я - УКРАЇНЕЦЬ!")
# print("Отже, я люблю БОРЩ!")
# print("БОРЩ "+50)
# print("Хочу ще...")

# A = [1,2,3]
# i = [4,5,6]
# B = A.insert(i,0)
# print(B)



# students = {
#     'John': {
#         'Full Name': 'John John',
#         'Phone number': '+3806669555555',
#         'Mark': 99
#     },
#     'Bob': {
#         'Full Name': 'asdasd',
#         'Phone number': '+112312412512',
#         'Mark': 79
#     },
# }
#
# while True:
#     choice = input('> ')
#     if choice == '1':
#         name = input('Enter your name: ')
#         full_name = input('Enter your full name: ')
#         phone_number = input('Enter your full name: ')
#         mark = int(input('Enter your mark: '))
#         students[name] = {
#             'Full Name': full_name,
#             'Phone number': phone_number,
#             'Mark': mark
#         }
#     elif choice == '2':
#         break
#
# print(*students)

# arr = {}
#
# for i in range(int(input())):
#     k, v = input().split(' ', 1)
#     arr[k] = v
#
# print(arr)

# files = {}
#
# for i in range(int(input('кількість файлів: '))):
#     files_names, files_operations = input('Name: '), input('Operation: ').split(' ')
#     files[files_names] = files_operations
#     files: {
#         files_names: [files_operations]
#     }
#
# print(files)
#
# new_files = files
# r = read
#
#
# for i in range(int(input('кількість запитів: '))):
#     files_names, files_operations = input('Name: '), input('Operation: ')
#     if files_names in new_files and files_operations in new_files[files_names]:
#         print("Ok")
#     else:
#         print("Access denied")

# files = {}
# k = 0
# d = 0
# count = 0
#
# for i in range(int(input('number of files: '))):
#     name, *operations = input('names and optoins: ').split(' ')
#     files[name] = operations
# print(files)
#
# for i in range(int(input('number of use: '))):
#     operation, name = input('names and optoins: ').split(' ')
#     if operation == 'read':
#         if 'r' in files[name]:
#             k += 1
#         if 'r' not in files[name]:
#             d += 1
#     elif operation == 'write':
#         if 'w' in files[name]:
#             k += 1
#         if 'w' not in files[name]:
#             d += 1
#     elif operation == 'execute':
#         if 'x' in files[name]:
#             True
#         if 'x' not in files[name]:
#             d += 1
#
#
# # print(count)
#
# for k in range(1):
#     if k + 1:
#         print('OK')
#     if d + 1:
#         print('Access denied')
#
# files = {}
# result = []
#
# # Files_names = F_n = Імя файлу
# # Files_operation = F_o = допустимі опреації
# # Operation_options = O_o = словарь где ключ это слово, а значение его буквенный вариант
# # necessary_operation = N_o = Необхідна опреація
#
# for i in range(int(input('Кількість файлів: '))):
#     F_n, *F_o = input("Імя файлу та допустимі опреації через пробіл: ").split()
#     files[F_n] = F_o
#
# O_o = {'read':'R','write':'W','execute':'X'}
#
# for i in range(int(input('Кількість запитів до файлів: '))):
#     F_o, F_n = input("Необхідна опреація та імя файлу через пробіл: ").split()
#     F_o = F_o.upper().lower()
#     result.append('OK') if O_o.get(F_o, 'Access denied') in files.get(F_n, 'Access denied') else result.append('Access denied')
#
# print('\n'.join(result))


# lst =input().split()
# l = []
# for i in lst:
#     if lst.count(i)!=1 and i not in l :
#         l.append(i)
# print(' '.join(l))
#
import re

# A = ["FirstItem", "FriendsList", "MyTuple"]
# B = ",".join(A)
#
# print(B)
# def change_case(B):
#     res=""
#     for i in B:
#         if i.isupper():
#             B.add("_")
#         else:
#             res+=i
#     return res[:]
#
# print(*change_case(B))

# d = {'Read': 'r', 'wriTe': 'W', 'execute': 'X'}
# d = dict([[k.upper().lower(), v.upper()] for k, v in d.items()])
# print(d)

# b = str(input())
# b = b.upper().lower()
# for i in d:
#     if b in d:
#        print(b)

# messages = "Это Тестовое Сообщение"
# print(messages.upper().lower())
#
# a = "a"
# print(a.isupper())

A = ["FirstItem", "FriendsList", "MyTuple"]
A = ','.join(A)
A = A.replace('FirstItem,FriendsList,MyTuple', "first_item friends_list my_tuple")
A = A.split()

print(A)

