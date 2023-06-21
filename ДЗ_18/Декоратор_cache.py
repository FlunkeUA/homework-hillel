def cahce_dec(func):
    cache = {}
    def cache_func(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
            print('Память кэша:', cache)
        return cache[cache_key]
    return cache_func

@cahce_dec
def sum_range(a, b):
    print(f'Вызвана функция sum_range с аргументами {a} и {b}')
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))

@cahce_dec
def numbers_range(a, b):
    print(f'Вызвана функция numbers_range с аргументами {a} и {b}')
    numbers = []
    if a > b:
        b, a = a, b
    for i in range(a, b + 1):
        if i % 2 == 0:
            numbers.append(i)
    return numbers

print("Результат выполнения 1:", sum_range(a=2, b=5))
print("Результат выполнения 2:", sum_range(b=8, a=9))
print("Результат выполнения 3:", numbers_range(2, 16))
print("Результат выполнения 4:", numbers_range(2, 8))
print("Результат выполнения 5:", sum_range(2, 5))
print("Результат выполнения 6:", numbers_range(2, 16))
