7.1 Python is awesome ------------------------------------------------------#
for i in range(10):
    print('Python is awesome!')

# 7.1 Повторяй за мной 1 -----------------------------------------------------#
string, times = input(), int(input())
for i in range(times):
    print(string)

# 7.1 Последовательность символов --------------------------------------------#
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

# 7.1 Звездный прямоугольник -------------------------------------------------#
times = int(input())
for i in range(times):
    print('*******************')

# 7.1 Повторяй за мной 2 -----------------------------------------------------#
string = input()
for i in range(10):
    print(i, string)

# 7.1 Квадрат числа  ---------------------------------------------------------#
num = int(input())

for i in range(num + 1):
    print('Квадрат числа', i, 'равен', i ** 2)

# 7.1 Звездный треугольник  --------------------------------------------------#
n = int(input())

for i in range(n):
    print('*' * (n - i))

# 7.1 Популяция  -------------------------------------------------------------#
m, p, n = float(input()), float(input()), int(input())

multiplier = p / 100

for i in range(n):
    print(i + 1, m)
    m = m + (m * multiplier)

# 7.2 Последовательность чисел 1  --------------------------------------------#
m, n = int(input()), int(input())

for i in range(m, n + 1):
    print(m)
    m += 1

# 7.2 Последовательность чисел 2  --------------------------------------------#
m, n = int(input()), int(input())

if m < n:
    for i in range(m, n + 1):
        print(m)
        m += 1
else:
    for i in range(n, m + 1):
        print(m)
        m -= 1

# 7.2 Последовательность чисел 3  --------------------------------------------#
m, n = int(input()), int(input())

if m % 2 == 0:
    m -= 1
for i in range(n - 1, m, 2):
    print(m)
    m -= 2

# 7.2 Последовательность чисел 4  --------------------------------------------#
m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)

# 7.2 Таблица умножения  -----------------------------------------------------#
n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)

# 7.3 Количество чисел  ------------------------------------------------------#
a, b = int(input()), int(input())

count = 0

for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)

# 7.3 Сумма чисел  -----------------------------------------------------------#
n = int(input())

result = 0

for _ in range(n):
    result += int(input())
print(result)

# 7.3 Асимптотическое приближение  -------------------------------------------#
from math import log

j = 1
n = int(input())

for i in range(n + 1):
    if i > 1:
        j += (1 / i)
print(j - log(n))

# 7.3 Сумма чисел  -----------------------------------------------------------#
n = int(input())

result = 0

for i in range(1, n + 1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        result += i
print(result)

# 7.3 Факториал  -------------------------------------------------------------#
n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
print(result)

# 7.3 Без нулей  -------------------------------------------------------------#
result = 1

for _ in range(10):
    n = int(input())
    if n != 0:
        result *= n
print(result)

# 7.3 Сумма делителей  -------------------------------------------------------#
n = int(input())

result = 0

for i in range(1, n + 1):
    if n % i == 0:
        result += i
print(result)

# 7.3 Знакочередующаяся сумма  -----------------------------------------------#
n = int(input())

result = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        result -= i
    else:
        result += i
print(result)

# 7.3 Наибольшие числа  ------------------------------------------------------#
n = int(input())

first = 0
second = 0

for _ in range(n):
    inpt = int(input())
    if inpt > first:
        second = first
        first = inpt
    elif second < inpt < first:
        second = inpt

print(first)
print(second)

# 7.3 Only even numbers  -----------------------------------------------------#
all = 1

for _ in range(10):
    n = int(input())
    if n % 2 == 1:
        all = 0
if all == 1:
    print('YES')
else:
    print('NO')

# 7.3 Последовательность Фибоначчи  ------------------------------------------#
n = int(input())

a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

# 7.4 До КОНЦА 1  ------------------------------------------------------------#
string = input()

while string != 'КОНЕЦ':
    print(string)
    string = input()

# 7.4 До КОНЦА 2  ------------------------------------------------------------#
string = input()

while string != 'КОНЕЦ' and string != 'конец':
    print(string)
    string = input()

# 7.4 Количество членов  -----------------------------------------------------#
string = input()

i = 0

while string != 'хватит' and string != 'стоп' and string != 'достаточно':
    i += 1
    string = input()
print(i)

# 7.4 Пока делимся  ----------------------------------------------------------#
num = int(input())

while num % 7 == 0:
    print(num)
    num = int(input())

# 7.4 Сумма чисел  -----------------------------------------------------------#
result = 0

num = int(input())

while num >= 0:
    result += num
    num = int(input())
print(result)

# 7.4 Количество пятерок  ----------------------------------------------------#
score = int(input())

count = 0

while 0 < score < 6:
    if score == 5:
        count += 1
    score = int(input())
print(count)

# 7.4 Ведьмаку заплатите чеканной монетой  -----------------------------------#
price = int(input())

count = 0

count += price // 25
price = price % 25
count += price // 10
price = price % 10
count += price // 5
price = price % 5
count += price

print(count)

# 7.5 Обратный порядок 1  ----------------------------------------------------#
num = int(input())

while num:
    print(num % 10)
    num //= 10

# 7.5 Обратный порядок 2  ----------------------------------------------------#
num = int(input())

while num:
    print(num % 10, end='')
    num //= 10

# 7.5 max и min  -------------------------------------------------------------#
num = int(input())

min_digit = num % 10
max_digit = num % 10

while num:
    if min_digit > num % 10:
        min_digit = num % 10
    if max_digit < num % 10:
        max_digit = num % 10
    num //= 10

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)

# 7.5 Все вместе  ------------------------------------------------------------#
num = int(input())

summ = 0
count = 0
multiple = 1
first = 0
last = num % 10

while num:
    first = num % 10
    summ += first
    multiple *= first
    num //= 10
    count += 1

print(summ, count, multiple, summ / count, first, first + last, sep='\n')

# 7.5 Вторая цифра  ----------------------------------------------------------#
num = int(input())

second = 0
while num:
    if num // 10 > 0:
        second = num % 10
    num //= 10

print(second)

# 7.5 Одинаковые цифры  ------------------------------------------------------#
num = int(input())

result = 'YES'
last = num % 10

while num:
    if last != num % 10:
        result = 'NO'
    num //= 10
print(result)

# 7.5 Упорядоченные цифры  ---------------------------------------------------#
num = int(input())

last = num % 10
result = 'YES'

while num:
    if last > num % 10:
        result = 'NO'
    last = num % 10
    num //= 10

print(result)

# 7.6 Наименьший делитель  ---------------------------------------------------#
divider = num = int(input())

for i in range(2, num + 1):
    if num % i == 0:
        divider = i
        break

print(divider)

# 7.6 Следуй правилам  -------------------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)

# 7.7 Ревью кода-1  ----------------------------------------------------------#
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

# 7.7 Ревью кода-2  ----------------------------------------------------------#
mx = 0
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s += x
        if x > mx or mx == 0:
            mx = x
if mx < 0:
    print(s)
    print(mx)
else:
    print('NO')

# 7.7 Ревью кода-3  ----------------------------------------------------------#
s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)

# 7.7 Ревью кода-4  ----------------------------------------------------------#
n = int(input())
max_digit = -1
while n > 9:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit % 3 != 0:
    print('NO')
else:
    print(max_digit)

# 7.7 Ревью кода-5  ----------------------------------------------------------#
n = int(input())
while n > 9:
    n //= 10
print(n)

# 7.7 Ревью кода-6  ----------------------------------------------------------#
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)

# 7.8 Таблица-1  -------------------------------------------------------------#
num = int(input())

for _ in range(num):
    print(num, num, num)

# 7.8 Таблица-2  -------------------------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    print(i, i, i, i, i)

# 7.8 Таблица-3  -------------------------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    else:
        print()

# 7.8 Звездный треугольник  --------------------------------------------------#
num = int(input())

top = (num // 2) + 1
bottom = (num // 2)

for i in range(1, top + 1):
    for j in range(1, i + 1):
        print('*', end='')
    else:
        print()
for i in range(bottom, 0, -1):
    for j in range(1, i + 1):
        print('*', end='')
    else:
        print()

# 7.8 Численный треугольник 1  -----------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(i, end='')
    else:
        print()

# 7.9 Численный треугольник 3  -----------------------------------------------#
num = int(input())

count = 0

for i in range(1, num + 1):
    for j in range(1, i + 1):
        count += 1
        print(count, end=' ')
    else:
        print()

# 7.9 Численный треугольник 4  -----------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    tmp = 1
    to_lower = 0
    for j in range(1, i * 2):
        if tmp < i and to_lower == 0:
            print(tmp, end='')
            tmp += 1
        elif i >= tmp > 0:
            to_lower = 1
            print(tmp, end='')
            tmp -= 1
    else:
        print()

# 7.9 Делители-1  ------------------------------------------------------------#
a, b = int(input()), int(input())

total_max = 0
digit = 0

for i in range(a, b + 1):
    curr_max = 0
    for j in range(1, i + 1):
        if i % j == 0:
            curr_max += j
        if curr_max >= total_max:
            total_max = curr_max
            digit = j

print(digit, total_max)

# 7.9 Делители-2  ------------------------------------------------------------#
num = int(input())

for i in range(1, num + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    else:
        print()

# 7.9 Цифровой корень  -------------------------------------------------------#
num = int(input())

while num > 9:
    tmp = num % 10
    num //= 10
    num += tmp
print(num)

# 7.9 Цифровой корень  -------------------------------------------------------#
from math import factorial

num = int(input())
summ = 0

for i in range(1, num + 1):
    summ += factorial(i)
print(summ)

# 7.9 Простые числа  -------------------------------------------------------#
a, b = int(input()), int(input())

for i in range(a, b + 1):
    is_simple = 1
    for j in range(2, i):
        if i % j == 0:
            is_simple = 0
    if is_simple == 1 and i != 1:
        print(i)
