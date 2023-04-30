N = int(input("Enter your number: "))

for N in range(1, N+1, 1):
    if N % 3 == 0:
        print(N, end=" ")

summ = 0

for N in range(1, N+1):
    if N % 3 == 0:
        summ += N
print("\n", summ)

while N > 0:
    if N % 3 == 0:
        print(N, end=" ")
    N -= 1

while N > 0:
    if N % 3 == 0:
        summ += N
print("\n", summ)

