
# Вірус пошкодив систему доступу до файлів. Відомо, що над кожним файлом можна робити певні дії:
# запис – W;
# читання – R;
# запуск - X.
#
# На вхід програмі подається:
# число n – кількість файлів;
# n рядків з іменами файлів та допустимими операціями;
# число m – кількість запитів до файлів;
# m запитів виду "операція файл".
#
# Для кожного припустимого запиту програма має повертати OK, для неприпустимого – Access denied.
#
# Приклад введення:
#
# 3
# python.exe X
# book.txt R W
# notebook.exe R W X
# 5
# read python.exe
# read book.txt
# write notebook.exe
# execute notebook.exe
# write book.txt
#
#
# Приклад виводу:
#
# Access denied
# OK
# OK
# OK
# OK

# N = int(input('Введіть число яке треба порахувати: '))
# A = list(input("іменами файлів та допустимими операціями:"))

# file_numbers = N
# file_name = F
# file_operations = O

# files = {
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
#     choice = input('Додати файли та можливі операції? Введіть: Так/Ні - ')
#     if choice == 'Так':
#         file_numbers = input('кількість файлів: ')
#         file_name = input('іменами файлів: ')
#         file_operations = input('допустимими операціями: ')
#         files[name] = {
#             'Full Name': full_name,
#             'Phone number': phone_number,
#             'Mark': mark
#         }
#     elif choice == '2':
#         break

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
#
# k = 0
# d = 0
#
#
# for i in range(int(input('кількість запитів: '))):
#     files_names, files_operations = input('Name: '), input('Operation: ')
#
# for i in range(files):
#     if files_names in files and files_operations[0] in files[files_names]:
#         print("Ok")
#     else:
#         print("Access denied")

# count = int(k+d)
# print(count)
#
# for k in range(count):
#     if k + 1:
#         print("Ok")
#     if d + 1:
#         print("Access denied")


files = {}
for i in range(int(input('number of files: '))):
    name, *operations = input('names and optoins: ').split(' ')
    files[name] = operations
print(files)

for i in range(int(input('number of use: '))):
    operation, name = input('names and optoins: ').split(' ')
    if operation == 'read':
        if 'r' in files[name]:
            print('OK')
        else:
            print('Access denied')
    elif operation == 'write':
        if 'w' in files[name]:
            print('OK')
        else:
            print('Access denied')
    elif operation == 'execute':
        if 'x' in files[name]:
            print('OK')
        else:
            print('Access denied')