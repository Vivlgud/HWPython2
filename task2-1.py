"""
Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

print("Решение квадратного уравнения типа a*x^2+b*x+c=0")
a = int(input("Введите а ="))
b = int(input("Введите b ="))
c = int(input("Введите c ="))

if a != 0:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x1 = (-b + complex(discriminant) ** 0.5) / (2 * a)
        x2 = (-b - complex(discriminant) ** 0.5) / (2 * a)
        print("Уравнение имеет два комплексных корня:")
        print(f'X1={x1}')
        print(f'X2={x2}')
    elif discriminant == 0:
        x = round(-b / (2 * a), 2)
        print(f'Уравнение имеет один корень X={x}')
    elif discriminant > 0:
        x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
        x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
        print("Уравнение имеет два корня:")
        print(f'X1={x1}')
        print(f'X2={x2}')
else:
    x = -c / b
    print(f'Уравнение имеет один корень X={x}')
