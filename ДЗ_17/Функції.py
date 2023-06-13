# Завдання 1
lst = ["home", "car", "dog", "cat", "roof"]

def change(lst):
    first_item = lst[0]
    last_item = lst[-1]
    lst[-1], lst[0] = first_item, last_item
    return lst

# Завдання 2
lst = ["home", "car", "dog"]
def to_dict(lst):
    to_dict = {item:item for item in lst}
    return to_dict

# Завдання 3
start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))
