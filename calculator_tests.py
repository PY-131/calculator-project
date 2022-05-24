import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):

        self.assertEqual(self.calc.add(3,3), 6, "answer should be 6")

    def test_sub(self):

        self.assertEqual(self.calc.sub(3,3), 0, "answer should be zero")

    def test_multi(self):

        self.assertEqual(self.calc.multi(3,3), 9, "answer should be nine")


if __name__ == '__main__':
    unittest.main()
