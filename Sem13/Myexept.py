class ValMatrixSizeError(Exception):
    def __init__(self, operation):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        else:
            return f"Error: Невозможно сравнить. Матрицы разных размеров"


class ValueDigitError(Exception):
    def __str__(self):
        return f"Ошибка. Введено не число"

