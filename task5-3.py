"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


number = int(input('Введите число  '))
print(f"Последовательность из {number} чисел Фибоначчи:\n {list(fib(number))}")
