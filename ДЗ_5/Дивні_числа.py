N = int(input("Введіть число:"))

if N % 2 != 0 or N % 2 == 0 and 6 <= N <= 20:
    print("Wierd")

if N % 2 == 0 and 2 <= N <= 5 or N >= 20 and N % 2 != 0:
    print("Not Wierd")
