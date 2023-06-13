def cahce_dec(f):
    cache = dict()
    def cache_func(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return cache_func

@cahce_dec
def sum_range(a, b):
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))

@cahce_dec
def numbers_range(start, end):
    print(f'Вызвана функция numbers_range с аргументами {start} и {end}')
    numbers = []
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        if i % 2 == 0:
            numbers.append(i)
    return numbers

print("Результат выполнения:", sum_range(2, 5))
print("Результат выполнения:", sum_range(8, 9))
print("Результат выполнения:", numbers_range(2, 16))
print("Результат выполнения:", numbers_range(2, 8))
print("Результат выполнения:", sum_range(2, 5))
print("Результат выполнения:", numbers_range(2, 16))
