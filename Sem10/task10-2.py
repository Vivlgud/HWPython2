"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), 
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
Задания должны решаться через вызов методов экземпляра.

"""

import json
import csv
import os


class ScanDir():
    def directory_scan(self, dir_path):
        self.dir_path = dir_path
        self.res = []
        for root, dirs, files in os.walk(dir_path):
            for name in files:
                full_path = os.path.join(root, name)
                self.res.append({"Parent dir": root,
                                 "file": True,
                                 "name": name,
                                 "size": os.path.getsize(full_path)})

            for name in dirs:
                full_path = os.path.join(root, name)
                self.res.append({"Parent dir": root,
                                 "file": False,
                                 "name": name, })
                # "size": get_size_file(full_path)})

        with open("output.json", "w", encoding='utf-8') as json_file:
            json.dump(self.res, json_file, indent=4)

        with open("output.csv", "w", encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.res[0].keys())
            writer.writeheader()
            writer.writerows(self.res)

    def get_size_file(self, path):
        self.total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                self.total += os.path.getsize(fp)
        return self.total


dir1 = ScanDir()
dir1.directory_scan('C:\Work\Book')
