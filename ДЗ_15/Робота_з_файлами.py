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
# f_w = open('text.txt', 'a')
# f_w.write("\n" + text)
# f_w.close()

# Завдання 3
#
# Запросити у користувача число N і запитати N чисел у користувача,
# потім записати їх у файл numbers.txt через пробіл
# N = input('Кількість чисел: ')
# numbers = input('Введіть ' + N + ' чисел(a): ').split()
# numbers = " ".join(numbers)

# f_w = open('text.txt', 'a')
# f_w.write('\n' + numbers)
# f_w.close()


# Завдання 4
# Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt,
# де один рядок = одне число
# import random
#
# n=[]
#
# for i in range(100):
#    n = n.append(random.randint(1,1000))
#
# print(n)
# type=n

#numbers = " ".join(n)

# f_w = open('random_numbers.txt', 'a')
# f_w.write(n)
# f_w.close()

# Завдання 5
#Даний файл із довільним текстом, потрібно знайти кількість слів у файлі та вивести користувачеві

# f = open('text.txt')
#
# words = 0
#
# for line in f:
#     words += len(line.split())
#
# print("Кількість слів:", words)
#
# f.close()

#
# Завдання 6
# Даний файл, у якому записані числа через пробіл, необхідно вивести користувачу суму цих чисел
# f_w = open('random_numbers.txt')
# a = f_w.read()
# a = list(a)
# s = 0
#
# for _ in a:
#     if _.isdigit():
#         s += _
#
# print(a)

# Завдання 7
#
# Даний файл у якому записаний текст, необхідно вивести топ 5 рядків, які найчастіше повторюються, приклад:
#
# 'в' - 20 разів
#
# 'привіт' - 10 разів
#
# 'як' - 9 разів
#
# 'у' - 7
#
# 'world' - 4
#
# Краще за все використовувати тип даних Counter з модуля collections. Приклад:
#
# Counter(words).most_common(5)

