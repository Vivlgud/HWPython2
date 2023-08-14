'''
Задание
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.

'''

import csv
import datetime
import json
import math
import os.path
from random import randint
from typing import Callable


def deco_csv(function: Callable):
    number_generators_csv()

    def wrapper():
        with open('number_for_equation.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    function(*coef)

    return wrapper


def json_result(func: Callable):
    result = {}
    if os.path.exists('solutions.json'):
        with open('solutions.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)
    else:
        with open('solutions.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        res_key = f'{datetime.datetime.now()}'[:-7]
        result[res_key] = result.get(res_key) + [solve_dict] if result.get(res_key) else [solve_dict]
        with open('solutions.json', 'w', encoding='UTF-8', ) as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        return roots

    return wrapper


def number_generators_csv():
    with open('number_for_equation.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(randint(100, 1000)):
            writer.writerow([randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)])


@deco_csv
@json_result
def solve_of_equation(*args):
    a, b, c = args
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discr == 0:
        x = -b / (2 * a)
        return round(x, 2)


solve_of_equation()
