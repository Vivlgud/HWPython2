
import unittest
from task14_1_doctest import quad_equation

class TestCaseName(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(quad_equation(2, 3, 4), 'Уравнение не имеет корней')

    def test_method_2(self):
        self.assertEqual(quad_equation(3, 12, 7), 'Уравнение имеет два корня: X1=-0.71,X2=-3.29')

    def test_method_3(self):
        self.assertEqual(quad_equation(0, 6, 5), 'Уравнение имеет один корень X=-0.8333333333333334')


if __name__ == '__main__':
    unittest.main(verbosity=2)
