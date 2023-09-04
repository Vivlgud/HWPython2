"""
- Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import json
import csv
import pickle
import os


def directory_scan(dir_path):
    res = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            res.append({"Parent dir": root,
                        "file": True,
                        "name": name,
                        "size": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            res.append({"Parent dir": root,
                        "file": False,
                        "name": name,
                        "size": get_size_file(full_path)})

    with open("output.json", "w", encoding='utf-8') as json_file:
        json.dump(res, json_file, indent=4)

    with open("output.csv", "w", encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=res[0].keys())
        writer.writeheader()
        writer.writerows(res)

    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(res, pickle_file)


def get_size_file(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total


directory_scan('C:\\Users\\Home\\Desktop\\Files')
