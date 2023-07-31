"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

import os


def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)


string = "C:\Vitaliy\Home\Desktop\Study projects\Python2\Sem5\Task5-1.py"
print(f'Исходная строка: {string} \nКортеж из пути: {parse_path(string)}')
