"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

Создайте класс Матрица. Добавьте методы для: -
вывода на печать,сравнения,сложения,
"""
import logging


logging.basicConfig(filename='Sem15/Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:

    def __init__(self, matrx):
        self._matrx = matrx

    def get_matrix(self):
        return self._matrx

    def __add__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            logger.error(f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self._matrx)}][{len(self._matrx[0])}] !=  [{len(other._matrx)}][{len(other._matrx[0])}] ')
        else:
            new_matrx = Matrix([[self._matrx[i][j] + other._matrx[i][j] for j in range(len(self._matrx[0]))] for i in
                               range(len(self._matrx))])
            logger.info(f' СЛОЖЕНИЕ:  {self._matrx} + {other._matrx} = {new_matrx}  ')
            return new_matrx

    def __eq__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            return logger.error(f'Невозможно сравнить, матрицы разных размеров')
        else:
            for i in range(len(self._matrx)):
                for j in range(len(self._matrx[0])):
                    if self._matrx[i][j] != other._matrx[i][j]:
                        return logger.info(f' РАВЕНСТВО:  {self._matrx} = {other._matrx} ')
            return True

    def __repr__(self):
        s = ''
        for i in range(len(self._matrx)):
            s += str(self._matrx[i]) + '\n'
        return s


m1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
m2 = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]
m3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

matrx1 = Matrix(m1)
matrx2 = Matrix(m2)
matrx3 = Matrix(m3)

matrx_sum = matrx1 + matrx2
print(f'Сумма матриц\n {matrx_sum}')
matrx_sum = matrx1 + matrx3
print(f'Сумма матриц\n {matrx_sum}\n')

print("Cравнение матриц:")
print(matrx1 == matrx1)
print(matrx2 == matrx3)