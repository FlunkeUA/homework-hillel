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

# A = ["FirstItem", "FriendsList", "MyTuple"]
# A = ','.join(A)
# A = A.replace('FirstItem,FriendsList,MyTuple', "first_item friends_list my_tuple")
# A = A.split()
#
# print(A)


# sentence = "The quick brown fox jumps over the lazy dog"
# word_count = sentence.count(" ") + 1
# print("Количество слов в строке:", word_count)

# S = '_Here_are, _My_words, _All_time'
#
# print(S)
# print(S + S)
# print(len(S))
# print(S*2)
# print(S[2::3])
# print(S[::-1])
#
# S = S[0] + 'b' + S[2:]
# print(S)
# print(S.find('my'))
# print(S.rfind('my'))
# #print(s.replace('e', 'Y'[1,2]))
# print(S.replace('e', 'Y'))
# #print(S.split(','))
# print(S.isdigit())
# print(S.isalpha())
# print(S.isalnum())
# print(S.isupper())
# print(S.isspace())
# print(S.istitle())
# for i in S:
#     if i.lstrip():
#         S = S.replace('_','')
#
# print(S)
# names = ['Bob', 'Alice', 'Guido']
# for index, value in enumerate(names, 1):
#     print(f'{index}: {value}')

# a = ["FirstItem", "FriendsList", "MyTuple"]
# a = ','.join(a)
#
# # print(list(enumerate(a)))
# b = ""
#
# for i in a:
#         if i.isupper():
#             b += "_"+i.lower()#add _ then convert to lowercase
#         else:
#             b += i
#
#
# print("Camel case string:", a)
# print("Snake case string:", b)
#
# inputString = 'СтеНА коВер ПОЛ'
#
# letters = ["FirstItem", "FriendsList", "MyTuple"]
# lettersUpd = []
# for i in letters:
#     letter = ''
#     letter += i[0].lower()
#     letter += i[1:]
#     lettersUpd.append(letter)
# print(' '.join(lettersUpd))
# from itertools import chain
# first = {'A': 1, 'B': 2, 'C': 3}
# second = {'С': 4, 'E': 5}
#
# d = dict(chain(first.items(), second.items()))
# print(d)

# camel_case = ["FirstItem", "FriendsList", "MyTuple"]
# snake_case = []
#
# for words in camel_case:
#     new_words = ""
#     for char in words:
#         if char.isupper():
#             new_words += "_"
#         new_words += char.lower()
#     snake_case.append(new_words.lstrip("_"))
#
# print(snake_case)

#snake_case = []

# snake_case = ""
# for i, c in enumerate(camel_case):
#     if i == 0:
#         snake_case += c.lower()
#     elif c.isupper():
#         snake_case += "_" + c.lower()
#     else:
#         snake_case += c


# print(camel_case)
# print(snake_case)


# file = open('test.txt')
# a = file.read()
# a = a.split()
#
# c = Counter(a).most_common(5)
# c = ','.join(map(str, c))
#
# print(c)
# file.close()

# d1 = {'key': 1, 'key2': True}
# d2 = {'key': 'Hello', 'key2': 11, 'key':'World'}

# dict1 = {
#     'Student': 'Butler',
#     'Course': 'Computer Science',
#     'Address': 'Los Angeles'
# }
# dict2 = {
#     'Course': 'Rosy',
#     'Subject': 'Computer Science'
# }
#
# dict3 = dict1.copy()  # Copy the dict1 into the dict3 using copy() method
#
# for key, value in dict2.items():  # use for loop to iterate dict2 into the dict3 dictionary
#     dict3[key] = value
#
# print("After merging of the two Dictionary ")
# print(dict3)  # print the merge dictionary





# def task(d1,d2):
#     k=set(list(d1.keys())+list(d2.keys()))
#     print(k)
#     d={}
#     for a in k:
#         v1=d1.get(a)
#         v2=d2.get(a)
#         if v1==None:
#             v=v2
#         elif v2==None:
#             v=v1
#         elif type(v1)==int and type(v2)==int:
#             v=v1+ "," +v2
#         else:
#             v = (str(v1) + "," + str(v2)).split(",")
#         d[a]=v
#     return d

# print(task(d1,d2))

# lst = ["home", "car", "dog"]
#
# def to_dict(lst):
#     to_dict = {item:item for item in lst}
#     return to_dict
# print(to_dict(lst))

# fruits = ["Apple", "Pear", "Peach", "Banana"]
# fruit_dictionary = dict.fromkeys(fruits)
# print(fruit_dictionary)

def memoize_func(f):
    memo = dict()
    def func(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return func

@memoize_func
def func(a, b):
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')