"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction
import math

fract_1 = input('Введите первую дробь формата "a/b": ')
fract_2 = input('Введите вторую дробь формата "a/b": ')


def shorten_fraction(a: int, b: int):  # сокращение дроби
    if a > b:
        tmp = a
    else:
        tmp = b
    while tmp != 1:
        if a % tmp == 0 and b % tmp == 0:
            return str(a // tmp) + str(b // tmp)
        else:
            tmp -= 1
    return str(a) + str(b)

num_1 = fract_1.split("/")
num_2 = fract_2.split("/")

# сумма
lcm_fract = math.lcm(int(num_1[1]), int(num_2[1]))  # НОЗ дроби
numerator_fract_1 = int(lcm_fract / int(num_1[1]) * int(num_1[0]))
numerator_fract_2 = int(lcm_fract / int(num_2[1]) * int(num_2[0]))
summ_result = shorten_fraction(numerator_fract_1 + numerator_fract_2, lcm_fract)
print(f"Сумма дробей равна {summ_result[0]}/{summ_result[1]}")

# произведение
mult_result = shorten_fraction(int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1]))
print(f"Произведение дробей равно {mult_result[0]}/{mult_result[1]}")

# проверка
print(f'Результат сложения (Fraction)- {Fraction(int(num_1[0]), int(num_1[1])) + Fraction(int(num_2[0]), int(num_2[1]))}')
print(f'результат умножения (Fraction) - {Fraction(int(num_1[0]), int(num_1[1])) * Fraction(int(num_2[0]), int(num_2[1]))}')
