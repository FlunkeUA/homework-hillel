# Завдання 1
print("Завдання 1:")

lst = ["home", "car", "dog", "cat", "roof"]
print(lst)

def change(lst):
    for item in lst:
        first_item = lst[0]
        last_item = lst[-1]
        lst[-1], lst[0] = first_item, last_item
    return print(lst)

change(lst)

# Завдання 2
print("Завдання 2:")

lst = ["home", "car", "dog"]
def to_dict(lst):
    to_dict = {}
    for item in lst:
        if item not in to_dict:
            to_dict[item] = item
        else:
            to_dict += to_dict[item]
    return print(to_dict)

to_dict(lst)

# Завдання 3
print("Завдання 3:")

start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

def sum_range(start, end):
    sum_numbers = 0
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        sum_numbers += i
    return print("Сума чисел:", sum_numbers)

sum_range(start, end)
