from unittest import TestCase
from src.ex_factorial import *


class TestFactorial(TestCase):

    def test_recursive(self):
        self.assertTrue(factorial(9), 362880)
        self.assertTrue(factorial(-102902), 1)
        self.assertTrue(factorial(20), 2432902008176640000)
