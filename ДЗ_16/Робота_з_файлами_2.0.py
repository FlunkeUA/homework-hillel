import pickle
import json
from collections import defaultdict

# Завдання: 1

cars = {
        'license plate': "2222",
        'model': 'Jeep',
        'color': 'Red',
        'year of manufacture': '2010'
    }, {
        'license plate': "5689",
        'model': 'Volvo',
        'color': 'Black',
        'year of manufacture': '2016'
    }, {
        'license plate': "4563",
        'model': 'BMW',
        'color': 'Yellow',
        'year of manufacture': '2005'
    }

with open('cars.bin', 'wb') as f:
    pickle.dump(cars, f)

# Завдання: 2

car1 = {
        'license plate': 2222,
        'model': 'Jeep',
        'color': 'Red',
        'year of manufacture': 2010
    }
car2 = {
        'license plate': 5689,
        'model': 'Volvo',
        'color': 'Black',
        'year of manufacture': 2016
    }
car3 = {
        'license plate': 4563,
        'model': 'BMW',
        'engine capacity': 3.0,
        'year of manufacture': 2005
    }

all_cars = car1|car2|car3

merged_dict = defaultdict(list)
for key in all_cars:
    if key in car1:
        merged_dict[key].append(car1[key])
    if key in car2:
        merged_dict[key].append(car2[key])
    if key in car3:
        merged_dict[key].append(car3[key])

with open('merged_dict.json', 'w') as f:
    f.write(json.dumps(merged_dict))
