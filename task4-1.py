"""
Напишите функцию для транспонирования матрицы
"""


def matrix_print(matrix):
    """printing matrix"""
    for i in matrix:
        print(i)


def matrix_transp(matrix):
    """matrix transposition"""
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print("исходная матрица")
matrix_print(matrix)

print("транспонированная матрица")
matrix_print(matrix_transp(matrix))


