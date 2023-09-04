"""
Создайте класс Матрица.
Добавьте методы для: -
вывода на печать,
сравнения,
сложения,
*умножения матриц
"""


class Matrix:

    def __init__(self, matrx):
        self._matrx = matrx

    def get_matrix(self):
        return self._matrx

    def __add__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            return f'Невозможно сложить, матрицы разных размеров'
        else:
            return Matrix([[self._matrx[i][j] + other._matrx[i][j] for j in range(len(self._matrx[0]))] for i in
                           range(len(self._matrx))])

    def __eq__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            return f'Невозможно сравнить, матрицы разных размеров'
        else:
            for i in range(len(self._matrx)):
                for j in range(len(self._matrx[0])):
                    if self._matrx[i][j] != other._matrx[i][j]:
                        return False
            return True

    def __str__(self):
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
