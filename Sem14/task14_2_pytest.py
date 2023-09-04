import pytest
from task14_2_doctest import check_triangle


def test_1():
    assert check_triangle(3, 3, 3) == 'Треугольник существует. Треугольник равносторонний', 'ошибка тест 1'


def test_2():
    assert check_triangle(7, 3, 7) == 'Треугольник существует. Треугольник равнобедренный', 'ошибка тест 2'


def test_3():
    assert check_triangle(3, 4, 5) == 'Треугольник существует. Треугольник разносторонний', 'ошибка тест 3'


def test_4():
    assert check_triangle(40, 10, 11) == 'Треугольник не существует', 'ошибка тест 4'


if __name__ == '__main__':
    pytest.main(['-v'])