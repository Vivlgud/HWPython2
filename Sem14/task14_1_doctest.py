"""
Решите квадратное уравнение 5x2-10x-400=0.
"""
import doctest


def quad_equation(a, b, c):
    """решение квадратных уравнений
    >>> quad_equation(2, 3, 4)
    'Уравнение не имеет корней'
    >>> quad_equation(3, 12, 7)
    'Уравнение имеет два корня: X1=-0.71,X2=-3.29'
    >>> quad_equation(0, 6, 5)
    'Уравнение имеет один корень X=-0.8333333333333334'
    """
    if a != 0:
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return ("Уравнение не имеет корней")
        elif discriminant == 0:
            x = round(-b / (2 * a), 2)
            return (f'Уравнение имеет один корень X={x}')
        elif discriminant > 0:
            x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
            x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
            return (f'Уравнение имеет два корня: X1={x1},X2={x2}')
    else:
        x = -c / b
        return (f'Уравнение имеет один корень X={x}')


if __name__ == '__main__':
    #print(quad_equation(0, 6, 5))
    doctest.testmod(verbose=True)