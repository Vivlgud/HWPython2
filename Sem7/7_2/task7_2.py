'''
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
import os
from pathlib import Path


def group_rename(new_name: str, lenght_serial_number: int, old_extensions: str,
                 new_expansions: str, range_name: list[int, int], directory=Path().cwd()):
    count = 1
    start_range, end_range = range_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(old_extensions):
                old_name = Path(dirs) / file
                old_name.rename(
                    f'{dirs}/{file[start_range:end_range]}{new_name}{str(count).zfill(lenght_serial_number)}.{new_expansions}')
                count += 1


group_rename('-task7_2-', 2, 'txt', 'docx', [1, 3], 'Testdir')

"""
исходные файлы:             Результат:
aaaaaaaa.txt                aa-task7_2-01.docx
bb.txt                      b.-task7_2-02.docx
cccccc.txt                  cc-task7_2-03.docx
sdfadgad.txt                df-task7_2-04.docx
sdfgjk;lk.txt               df-task7_2-05.docx
sssssssss.txt               ss-task7_2-06.docx
text2.doc                   text2.doc

В папке лежат исходные файлы для проверки
"""
