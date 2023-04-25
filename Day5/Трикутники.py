N = int(input("Enter your number: "))

for x in range(N, 0, -1):
    for y in range(1, x + 1):
        print('*', end=' ')
    print("")

print("")

for x in range(1, N + 1):
    for y in range(1, x + 1):
        print('*', end=' ')
    print("")

print("")

for x in range(1, N + 1):
    for y in range(N, 0, -1):
        if y > x:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print("")

print("")

for x in range(N, -1, -1):
    for y in range(N, 0, -1):
        if y > x:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print("")
