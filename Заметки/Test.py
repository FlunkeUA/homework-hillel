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

entered_list = input("Введите список чисел, разделенных пробелом: ").split()
entered_list.extend('10')
A = list(map(int, entered_list))

print("Введенный список:", A)