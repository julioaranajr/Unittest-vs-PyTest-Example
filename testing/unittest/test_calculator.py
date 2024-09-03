"""
This module tests the calculator_app module

Example:
    $ python test_calculator.py or python -m unittest test_calculator.py
    
Attributes:
    my_calc (Calculator): An instance of the Calculator class

Methods:
    setUp(self): Will run every test
    test_my_calc_instance(self): Check the instance of the object
    test_add(self): Check the add method
    test_multiply(self): Check the multiply method
    test_subtract(self): Check the subtract method
    test_division(self): Check the division method
    
Todo:
    * Add more test cases
    
"""
import unittest
from calculator_app import Calculator


class TestCalculator(unittest.TestCase):
    """
    The TestCalculator class tests the Calculator class

    Args:
        unittest (module): The unittest module
        
    Attributes:
        my_calc (Calculator): An instance of the Calculator class
    """
    def setUp(self):
        """
        Will run every test in the class TestCalculator
        """
        self.my_calc = Calculator(8,2)

    # @classmethod
    # def setUpClass(cls):
    #     #will run once at the beginning of the test
    #     cls.my_calc = Calculator(8,2)
    def test_my_calc_instance(self):
        """
        Check the instance of the object, if it is an instance of the Calculator class
        """
        self.assertIsInstance(self.my_calc,Calculator,'message: check the instance of the object')

    def test_add(self):
        """
        Check the add method, if it returns the correct value (10)
        """
        self.assertEqual(self.my_calc.add(),10,'message: check the add method')

    def test_multiply(self):
        """
        Check the multiply method, if it returns the correct value (16) and if it is greater than 8
        """
        self.assertEqual(self.my_calc.multiply(),16,'message: check the multiply method')
        self.assertTrue(self.my_calc.multiply() > 8)

    def test_subtract(self):
        """
        Check the subtract method, if it returns the correct value (6) and if it is not equal to 8
        """
        self.assertEqual(self.my_calc.subtract(),6, 'message: check the subtract method')
        self.assertNotEqual(self.my_calc.subtract(),8)

    def test_division(self):
        """
        Check the division method, if it returns the correct value (4) and if it is not equal to 8
        
        Raises:
            ZeroDivisionError: If the denominator is zero
        """
        calc = Calculator(8,0)
        with self.assertRaises(ZeroDivisionError) as error:
            calc.divide()

        self.assertEqual(str(error.exception), "You Cannot divide by zero (0)")


if __name__ == '__main__':
    unittest.main()

# ❯ pylint test_calculator.py
#
# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 6.82/10, +3.18)
