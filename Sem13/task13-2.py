"""
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
"""

from Myexept import ValueDigitError
def check(num):
    if not isinstance(num, (int)):
        raise ValueDigitError()
    else:
        return num

a=check(12)
b=check("15")
c=check(10)

print("Решение квадратного уравнения типа a*x^2+b*x+c=0")

if a != 0:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("Уравнение не имеет корней")
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

