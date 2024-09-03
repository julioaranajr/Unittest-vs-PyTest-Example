"""
A class representing a calculator.
Methods:
- add(): Returns the sum of two numbers.
- multiply(): Returns the product of two numbers.
- subtract(): Returns the difference between two numbers.
- divide(): Returns the quotient of two numbers.

Returns:
    int: The sum of two numbers
    int: The product of two numbers
    int: The difference between two numbers
    int: The quotient of two numbers

Args:
    a (int): The first number
    b (int): The second number
    
Instance Attributes:
    a (int): The first number
    b (int): The second number
    
Example:
    >>> calc = Calculator(3, 5)
    >>> calc.add()
    8
"""
class Calculator:
    """
    A class representing a calculator.
    
    Attributes:
        a (int): The first number
        b (int): The second number
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """
        Returns the sum of two numbers.

        Returns:
            int: The sum of two numbers

        Example:
            >>> calc = Calculator(3, 5)
            >>> calc.add()
            8
        """
        return self.a + self.b

    def subtract(self):
        """
        Returns the difference between two numbers.
        
        Returns:
            int: The difference between two numbers
            
        Example:
            >>> calc = Calculator(3, 5)
            >>> calc.subtract()
            -2
        """
        return self.a - self.b

    def multiply(self):
        """_
        Returns the product of two numbers.
        
        Returns:
            int: The product of two numbers
            
        Example:
            >>> calc = Calculator(3, 5)
            >>> calc.multiply()
            15
        """
        return self.a * self.b

    def divide(self):
        """
        Returns the quotient of two numbers.
        
        Returns:
            int: The quotient of two numbers
            
        Example:
            >>> calc = Calculator(3, 5)
            >>> calc.divide()
            0.6
        """
        if self.b == 0:
            raise ZeroDivisionError("You Cannot divide by zero (0)")
        return self.a / self.b
