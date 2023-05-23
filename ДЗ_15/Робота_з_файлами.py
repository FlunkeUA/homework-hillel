import random
from collections import Counter

# Завдання 1
# Даний файл із довільним текстом, необхідно знайти всі числа у файлі
# та записати до списку numbers
# f = open('text.txt')
# text = f.read()
# f.close()
# numbers = []
#
# for _ in text:
#     if _.isdigit():
#         numbers.append(_)
#
# print(numbers)

# Завдання 2
# Запросити у користувача текст та записати його у файл data.txt

# text = input("Введіть текст: ")
# f_w = open('data.txt', 'a')
# f_w.write(text)
# f_w.close()

# print("\nЗавдання 3")
#
# Запросити у користувача число N і запитати N чисел у користувача,
# потім записати їх у файл numbers.txt через пробіл
# N = int(input('Кількість чисел: '))
# numbers = []
#
# for i in range(N):
#     i = input('Введіть число: ')
#     numbers.append(i)
#
# numbers = " ".join(numbers)
#
# f_w = open('numbers.txt', 'a')
# f_w.write(numbers)
# f_w.close()

# Завдання 4
# Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt,
# де один рядок = одне число
# n = []
#
# for i in range(100):
#     n.append(random.randint(1, 100))
#
# n = " \n".join(str(x) for x in n)
#
# f_w = open('random_numbers.txt', 'a')
# f_w.write(n)
# f_w.close()

# Завдання 5
#Даний файл із довільним текстом, потрібно знайти кількість слів у
# файлі та вивести користувачеві

# file = open('text.txt')
#
# words = 0
#
# for line in file:
#     words += len(line.split())
#
# print("Кількість слів:", words)
#
# file.close()

#
# Завдання 6
# Даний файл, у якому записані числа через пробіл,
# необхідно вивести користувачу суму цих чисел
#
# file = open('numbers.txt')
# a = file.read()
# numbers = []
# s = 0
#
# for _ in a:
#     if _.isdigit():
#         numbers.append(_)
#
# numbers = [int(x) for x in numbers]
#
# for x in numbers:
#     s += x
#
# print(s)
# file.close()

# Завдання 7
#
# Даний файл у якому записаний текст, необхідно вивести топ 5 рядків,
# які найчастіше повторюються, приклад:
#
# 'в' - 20 разів
# 'привіт' - 10 разів
# 'як' - 9 разів
# 'у' - 7
# 'world' - 4
# Краще за все використовувати тип даних Counter з модуля collections. Приклад:
# Counter(words).most_common(5)

file = open('test.txt')
a = file.read()

print(a)

b = Counter(a).most_common(5)

print(*b)