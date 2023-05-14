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

print("Я - УКРАЇНЕЦЬ!")
print("Отже, я люблю БОРЩ!")
print("БОРЩ "+50)
print("Хочу ще...")

# A = [1,2,3]
# i = [4,5,6]
# B = A.insert(i,0)
# print(B)
