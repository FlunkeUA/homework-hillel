n = int(input('введіть число = '))
i = 1
sum = 0

while n > i:
    if i % 3 == 0:
        sum = sum + i
        print(i, end = ' ')
    i += 1
print('\nСума =', sum)