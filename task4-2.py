"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def kwargs_to_dict(**kwargs):
    """Swaps key and value"""
    res = {}
    for key, value in kwargs.items():
        try:
            res[value] = key
        except:
            res[str(value)] = key
    return res


print(kwargs_to_dict(One='Имя', Two='Отчество', Three='Фамилия', Four=1980))
