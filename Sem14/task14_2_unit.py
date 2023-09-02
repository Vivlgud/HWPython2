import unittest
from task14_2_doctest import check_triangle


class TestCaseName(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(check_triangle(3, 3, 3), 'Треугольник существует. Треугольник равносторонний')

        self.assertEqual(check_triangle(7, 3, 7), 'Треугольник существует. Треугольник равнобедренный')

        self.assertEqual(check_triangle(3, 4, 5), 'Треугольник существует. Треугольник разносторонний')

    def test_method_2(self):
        self.assertEqual(check_triangle(40, 10, 11), 'Треугольник не существует')


if __name__ == '__main__':
    unittest.main(verbosity=2)