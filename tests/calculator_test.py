import unittest
from modules import calculator

class TestCalculator(unittest.TestCase):

    def test_can_add(self):
        self.assertEqual(10, calculator.add(5,5))