import random
from collections import Counter

print('Завдання: 1')
f = open('text.txt')
text = f.read()

numbers = []

for _ in text:
    if _.isdigit():
        numbers.append(_)

print(numbers)

f.close()

print('\nЗавдання: 2')

text = input("Введіть текст: ")
f_w = open('data.txt', 'a')
f_w.write(text)
f_w.close()

print("\nЗавдання: 3")
N = int(input('Кількість чисел: '))
numbers = []

for _ in range(N):
    i = input('Введіть число: ')
    numbers.append(i)

numbers = " ".join(numbers)

f_w = open('numbers.txt', 'a')
f_w.write(numbers)
f_w.close()

print('\nЗавдання: 4')
n = []

for i in range(100):
    n.append(random.randint(1, 100))

n = " \n".join(str(x) for x in n)

f_w = open('random_numbers.txt', 'a')
f_w.write(n)
f_w.close()

print('\nЗавдання: 5')
file = open('text.txt')
words = 0

for line in file:
    words += len(line.split())

print("Кількість слів:", words)

file.close()

print('\nЗавдання: 6')

file = open('numbers.txt')
a = file.read()
numbers = []
s = 0

for _ in a:
    if _.isdigit():
        numbers.append(_)

numbers = [int(x) for x in numbers]

for x in numbers:
    s += x

print(s)
file.close()

print('\nЗавдання: 7')

file = open('test.txt')
a = file.read()
a = a.split()

c = Counter(a).most_common(5)
c = ','.join(map(str, c))

print(c)
file.close()
