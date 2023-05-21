files = {}

num_files = int(input('Кількість файлів: '))

for i in range(num_files):
    files_names, *files_operation = input("Імя файлу та допустимі опреації через пробіл: ").split()
    files_names = files_names.lower()
    files[files_names] = [op.upper() for op in files_operation]

operation_options = {'read': 'R', 'write': 'W', 'execute': 'X'}

num_request = int(input('Кількість запитів до файлів: '))

for i in range(num_request):
    necessary_operation, files_names = input("Необхідна опреація та імя файлу через пробіл: ").split()
    necessary_operation = necessary_operation.lower()
    files_names = files_names.lower()
    if operation_options.get(necessary_operation) in files.get(files_names, []):
        print("Ok")
    else:
        print('Access denied')
