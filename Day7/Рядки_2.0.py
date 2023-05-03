print("Перевірка на поліндром/не поліндром")
word = input("Введіть текст: ").lower()
re_word = word[::-1].lower()
print("+" if re_word == word else "-")

print("\nЗнайти слово в тексті")
text = input("Введіть текст: ").lower()
word = input("Введіть слово: ").lower()
print("yes" if word in text else "no")

print("\nЗаміна та додавання тексту")
text = input("Введіть текст: ").lower()
print(text[:3].replace('abc', 'www')+text[3:] if "abc" in text[:3] else text+"qqq")

print("\nВидалення цифр")
text = input("Введіть текст: ").lower()
print(''.join([x for x in text if not x.isdigit()]))

print("\nПеревірка пошти")
email = input("Введіть email: ").lower()
print("No" if "." not in email or "@" not in email else "Yes")
