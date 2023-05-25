import random
from collections import Counter

print('Завдання: 1')
with open('text.txt') as f:
    text = f.readline()
    numbers = []
    for items in text:
        if items.isdigit():
            numbers.append(items)
    print(numbers)

print('\nЗавдання: 2')

with open('data.txt', 'a') as file:
    text = input("Введіть текст: ")
    file.write(text)

print("\nЗавдання: 3")
with open('numbers.txt', 'a') as file:
    amount_of_numbers = int(input('Кількість чисел: '))
    for num in range(amount_of_numbers):
        numbers = input('Введіть число: ')
        file.write(f"{numbers} ")

print('\nЗавдання: 4')
with open("random_numbers.txt", 'w') as file:
    for _ in range(100):
        numbers = random.randint(1, 100)
        file.write(f"{numbers}\n")

print('\nЗавдання: 5')
with open('text.txt') as file:
    words = 0
    for line in file:
        words += len(line.split())
    print("Кількість слів:", words)

print('\nЗавдання: 6')
with open('numbers.txt', 'r') as file:
    file_numbers = file.readline()
    numbers = []
    summ = 0
    for item in file_numbers:
        if item.isdigit():
            numbers.append(item)
    for num in numbers:
        summ += int(num)
    print(summ)

print('\nЗавдання: 7')
with open('test.txt') as file:
    text = file.read()
    text = text.split()
    most_common_count = Counter(text).most_common(5)
    most_common_count = ','.join(map(str, most_common_count))
    print(most_common_count)
