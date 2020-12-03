import unittest
from modules.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_can_add(self):
        self.assertEqual(10, add(5,5))

    def test_can_subtract(self):
        self.assertEqual(2, subtract(8,6))

    def test_can_multiply(self):
        self.assertEqual(10, multiply(5, 2))

    def test_can_divide(self):
        self.assertEqual(5, divide (10, 2))