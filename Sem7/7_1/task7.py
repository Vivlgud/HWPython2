"""
Задача 7 (из семинара):
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
from pathlib import Path


def sort_of_filetype(dir):
    extensions = {
        'video': ['avi', 'mp4', 'mov', 'mkv', 'mpg', 'mpeg', 'vob'],
        'image': ['bmp', 'cdr', 'ai', 'psd', 'jpg', 'tif'],
        'text': ['txt', 'doc', 'docx', 'pdf', ],
        'audio': ['mp3', 'wav', 'ogg', 'flac', 'midi']
    }
    res = [file.split('.') for dirs, folders, files in os.walk(dir) for file in files]

    for (name, ext) in res:
        for i, j in extensions.items():
            if ext in j:
                new_dir = Path().cwd() / dir / i
                if new_dir.is_dir():
                    old_dir = Path(dir) / f'{name}.{ext}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{ext}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(dir) / f'{name}.{ext}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{ext}')

# для проверки в папке Files лежат файлы с разными расширениями
sort_of_filetype('Files')
