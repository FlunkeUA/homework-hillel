password = input("Введіть пароль: ")
mark = 0

# Перевірка довжини
if len(password) >= 8:
    mark = mark + 1
else:
    print("Довжина паролю менше 8 символів")

# Перевірка на цифри
if any(char.isdigit() for char in password):
    mark = mark + 1
else:
    print("Пароль не містить цифр")

# Перевірка на великі літери
if any(char.isupper() for char in password):
    mark = mark + 1
else:
    print("Пароль не містить великих літер")

# Перевірка на маленькі літери
if any(char.islower() for char in password):
    mark = mark + 1
else:
    print("Пароль не містить маленьких літер")

# Перевірка на спецсимволи
if any(not char.isalnum() for char in password):
    mark = mark + 1
else:
    print("Пароль не містить спецсимволів")

print("\nСкладніть паролю =", mark, "/ 5")
