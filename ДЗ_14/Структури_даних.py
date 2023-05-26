print("Завдання 1:")

june = {'Mark', 'Andy', 'July', 'Kate', 'Billy'} # Червень
july = {'Mark', 'Fred', 'July', 'Inessa', 'Billy'} # Липень

print(*june.intersection(july))
print(*july.difference(june))

print("\nЗавдання 2:")

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = []

for words in camel_case:
    new_words = ""
    for char in words:
        if char.isupper():
            new_words += "_"
        new_words += char.lower()
    snake_case.append(new_words.lstrip("_"))

print(snake_case)
