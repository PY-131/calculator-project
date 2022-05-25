import unittest
from calculator import Calculator


# the class is the "test suite"
class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):

        self.assertEqual(self.calc.add(3,3), 6, "tests addition of two arguments on integers")
        self.assertEqual(self.calc.add(3,3,3), 9, "tests addition of three arguments on integers")
        self.assertEqual(self.calc.add(3.2,3.2), 6.4, "tests addition on floats")
        self.assertEqual(self.calc.add(-3, -3), -6, "tests adding negatives")
        #self.assertEqual(self.calc.add("ab", "cd"),  "tests adding negatives")
        # with self.assertRaises(TypeError):
        # 	pass

    def test_sub(self):

        self.assertEqual(self.calc.sub(3,3), 0, "answer should be zero")
        self.assertEqual(self.calc.sub(-5,3), -8, "answer should be -8")
    @unittest.skip('Skipped multiply tests')
    def test_multi(self):

        self.assertEqual(self.calc.multi(3,3), 9, "answer should be nine")

    def test_division(self):
    	self.assertEqual(self.calc.division(3,3), 1, "answer should be 1")
    	self.assertIsNone(self.calc.division(3,0), "Division by zero impossible") 

    def test_is_even(self):
    	self.assertTrue(self.calc.is_even(0))
    	self.assertFalse(self.calc.is_even(3))
    	self.assertTrue(self.calc.is_even(4))


    def test_divisors(self):
    	self.assertIn(3, self.calc.divisors(9))
    	self.assertIn(9, self.calc.divisors(9))

if __name__ == '__main__':
    unittest.main()
