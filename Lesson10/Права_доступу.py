
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

files = {}
# file_names = files.keys()
# files_operations = files.values()

for i in range(int(input('Введіть кількість файлів: '))):
    files_names, *files_operations = input('Введіть імя файлу:'), input('Введіть потрібні операції через пробіл:')
    files[files_names] = files_operations

print(files)

new_files = files

for i in range(int(input('Введіть кількість запитів: '))):
    files_names, files_operations = input('Введіть імя файлу:'), input('Введіть потрібні операції через пробіл:')
    new_files[files_names] = files_operations
    if files_names in new_files and files_operations in new_files.files_names(files_operations):
        print("Ok")
    else:
        print("Access denied")
