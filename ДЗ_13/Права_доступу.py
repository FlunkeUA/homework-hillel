files = {}

num_files = int(input('Кількість файлів: '))

for i in range(num_files):
    Files_names, *Files_operation = input("Імя файлу та допустимі опреації через пробіл: ").split()
    files[Files_names] = Files_operation

Operation_options = {'read': 'R', 'write': 'W', 'execute': 'X'}

num_request = int(input('Кількість запитів до файлів: '))

for i in range(num_request):
    Necessary_operation, Files_names = input("Необхідна опреація та імя файлу через пробіл: ").split()
    Necessary_operation = Necessary_operation.upper().lower()
    if Operation_options.get(Necessary_operation) in files.get(Files_names, 'Access denied'):
        print("Ok")
    else:
        print('Access denied')
