files = {}
result = []

for i in range(int(input('Кількість файлів: '))):
    files_name, *files_operations = input("Імя файлу та допустимі опреації через пробіл: ").split()
    files[files_name] = files_operations

operation_options = {'read':'R','write':'W','execute':'X'}

for i in range(int(input('Кількість запитів до файлів: '))):
    files_operations, files_name = input("Необхідна опреація та імя файлу  через пробіл: ").split()
    result.append('OK') if operation_options[files_operations] in files[files_name] else result.append('Access denied')

print('\n'.join(result))
