from math import sqrt

# a = Сторона А
# b = Сторона Б
# c = Сторона В
# p = Сумма сторон треугольника
# s = Площадь треугольника

a = float(input("Сторона А = "))
b = float(input("Сторона Б = "))
c = float(input("Сторона В = "))

p = ((a+b+c)/2)

s = sqrt(p*((p-a)*(p-b)*(p-c)))

print("Площадь треугольника = ", round(s, 2))

