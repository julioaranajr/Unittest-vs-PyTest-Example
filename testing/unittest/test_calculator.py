import unittest
from calculator_app import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        #will run every test
        self.my_calc = Calculator(8,2)

    # @classmethod 
    # def setUpClass(cls):
    #     #will run once at the beginning of the test
    #     cls.my_calc = Calculator(8,2)
    def test_my_calc_instance(self):
        self.assertIsInstance(self.my_calc,Calculator,'message: check the instance of the object')

    def test_add(self):
        self.assertEqual(self.my_calc.add(),10,'message: check the add method')

    def test_multiply(self):
        self.assertEqual(self.my_calc.multiply(),16,'message: check the multiply method')
        self.assertTrue(self.my_calc.multiply() > 8)

    def test_subtract(self):
        self.assertEqual(self.my_calc.subtract(),6, 'message: check the subtract method')
        self.assertNotEqual(self.my_calc.subtract(),8)#x != y

    def test_division(self):
        calc = Calculator(8,0)
        with self.assertRaises(ZeroDivisionError) as error:
            result = calc.divide()

        self.assertEqual(str(error.exception), "You Cannot divide by zero (0)")


if __name__ == '__main__':
    unittest.main()
