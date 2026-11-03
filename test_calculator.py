import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    # Add the following test methods to the TestCalculator class:
    def test_substract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 5), 35)
        self.assertEqual(self.calc.multiply(-9, 5), -45)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 9), 1)
        self.assertEqual(self.calc.divide(10, 3), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(17, 9), 8)
        self.assertEqual(self.calc.modulo(5, 2), 1)


if __name__ == '__main__':
    unittest.main()