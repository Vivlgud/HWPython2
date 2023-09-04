import pytest
from task14_1_doctest import quad_equation


def test_1():
    assert quad_equation(2, 3, 4 , msg='Уравнение не имеет корней')


def test_2():
    assert quad_equation(3, 12, 7) == 'Уравнение имеет два корня: X1=-0.71,X2=-3.29'


def test_3():
    assert quad_equation(0, 6, 5) == 'Уравнение имеет один корень X=-0.8333333333333334'


if __name__ == '__main__':
    pytest.main(['-v'])
