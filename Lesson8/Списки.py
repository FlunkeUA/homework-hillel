# print("Завдання 1: ")
#
# numbers = input("Введіть п'ять чисел, через пробіл: ").split()
# List = list(map(int, numbers))
#
# print(List)
#
# print("Завдання 2: ")
#
# A = [1, 2, 3, 4, 5]
# A.pop()
#
# print(A)
#
# print("Завдання 3: ")
#
# numbers = input("Введіть дес'ять чисел, через пробіл: ").split()
# А = list(map(int, numbers))
#
# N = int(input('Введіть число яке треба порахувати: '))
#
# print(А.count(N))

# print("Завдання 4: ")
#
# N = input('Введіть число: ')
#
# numbers = input("Введіть " + N + " чисел, через пробіл: ").split()
# B = list(map(int, numbers))
# B.reverse()
#
# print(B)

# print("Завдання 5: ")
#
# n = input("Введіть п'ять чисел, через пробіл: ").split()
# B = list(map(int, n))
#
# for i in B:
#     if i > 5:
#         print(i, end=" ")

# print("Завдання 6: ")
# Запросити у користувача число N
# Запросити користувача N цілих чисел і записати їх до списку A
# Знайти в ньому мінімальну та максимальну кількість за допомогою циклу
# (заборонено використовувати функцію min, max, sorted, sort). Вивести ці числа.

# N = input('Введіть число: ')
# numbers = input("Введіть " + N + " чисел, через пробіл: ").split()
# A = list(map(int, numbers))
#
# max_value, min_value = A[0], A[0]
#
# for i in range(len(A)):
#     if A[i]>max_value:
#         max_value=A[i]
#     if A[i]<min_value:
#         min_value=A[i]
#
# print ("Найбільший елемент =", max_value)
# print ("Найменьший елемент =", min_value)

print("Завдання 7: ")
# Користувач вводить текст потрібно вивести кількість цифр у цьому тексті
# Приклад:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Кількість цифр: 7

Text = input('Введіть text: ')
