"""
Создайте модуль и напишите в нём функцию,
которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует
Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from sys import argv
from datetime import datetime


def check_data(date_str):
    *_, year = list(date_str.split("."))
    try:
        print(date_str)
        datetime.strptime(date_str, "%d.%m.%Y").date()
        leap_year(int(year))
        return True
    except ValueError:
        print("Такой даты нет")
        return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")


if __name__ == '__main__':
    print("Запуск через консоль (ДД.ММ.ГГ)")
    print(check_data(*(argv[1:])))
