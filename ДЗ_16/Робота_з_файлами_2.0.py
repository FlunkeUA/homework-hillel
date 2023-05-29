import pickle
import json

# Завдання: 1
# Дано: довільний список словників.
# Необхідно записати їх у файл за допомогою модуля pickle.
# У кожному словнику однаковий набір ключів, а всі значення представлені у вигляді рядків.

# cars = [
#     {
#         'license plate': 2222,
#         'model': 'Jeep',
#         'color': 'Red',
#         'year of manufacture': '2010'
#     },
#     {
#         'license plate': 5689,
#         'model': 'Volvo',
#         'color': 'Black',
#         'year of manufacture': '2016'
#     },
#     {
#         'license plate': 4563,
#         'model': 'BMW',
#         'color': 'Yellow',
#         'year of manufacture': '2005'
#     },
# ]
#
# with open('cars.bin', 'wb') as f:
#     pickle.dump(cars, f)

f = open('cars.bin', 'rb')
pickle.load(f)
print(type(f))
print(f)

#
# Завдання: 2
# Дано два словники
# A = {'key': 1}
# B = {'key1: 2}
# Необхідно написати код який їх об'єднуватиме
#
# C = {'key': 1, 'key1': 2}
# Але потрібно також враховувати колізії,
# наприклад ситуація коли у нас два однакові ключі
# і щоб не втратити значення потрібно записати в один
# ключ список в якому будуть значення
#
# Наприклад:
# A = {'key': 1, 'key2': True}
# B = {'key': 'Hello'}
# C = {'key': [1, 'Hello'], 'key2': True}
# Записати результат у файл result.json у форматі JSON.