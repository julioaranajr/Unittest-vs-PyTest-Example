# Unittest - The TestCase Class

## The TestCase Class

The TestCase class is used to create test cases. A test case is a set of conditions or variables under which a tester will determine whether a system under test satisfies requirements or works correctly.

It provides a set of **assertion methods** that can be used to test the behavior of your code. **The TestCase class** is a subclass of the **unittest.TestCase class.**

## The assert Methods

The `TestCase` class provides a set of assertion methods that can be used to test the behavior of your code. The following table lists some of the most commonly used assertion methods:

| Method | Description | Example |
| --- | --- | --- |
| assertEqual(a, b) | Tests if a and b are equal | self.assertEqual(1, 1) |
| assertNotEqual(a, b) | Tests if a and b are not equal | self.assertNotEqual(1, 2) |
| assertTrue(x) | Tests if x is True | self.assertTrue(True) |
| assertFalse(x) | Tests if x is False | self.assertFalse(False) |
| assertIs(a, b) | Tests if a is b | self.assertIs(1, 1) |
| assertIsNot(a, b) | Tests if a is not b | self.assertIsNot(1, 2) |
| assertIsNone(x) | Tests if x is None | self.assertIsNone(None) |
| assertIsNotNone(x) | Tests if x is not None | self.assertIsNotNone(1) |
| assertIn(a, b) | Tests if a is in b | self.assertIn(1, [1, 2, 3]) |
| assertNotIn(a, b) | Tests if a is not in b | self.assertNotIn(4, [1, 2, 3]) |
| assertIsInstance(a, b) | Tests if a is an instance of b | self.assertIsInstance(1, int) |
| assertNotIsInstance(a, b) | Tests if a is not an instance of b | self.assertNotIsInstance(1, str) |

## The Test Case Method

The test case method is a method that is used to test the behavior of your code. It is a method that is defined in a test case class and is used
to test a specific aspect of your code.

For example, the following code defines a test case method that tests the calculation of the sum of two numbers:

```python
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

In this code, the `test_sum()` method is a test case method that tests the `sum()` function. It uses the `assertEqual()` method to test the behavior of the `sum()` function.

## The setUp() Methods

The `setUp()` method is a method that is called before each test case method is run. It is used to set up any resources that are needed for the test case methods.

For example, the following code defines a test case class that uses the `setUp()` method to set up a list of numbers before each test case method is run:

```python
import unittest

class TestSum(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.numbers), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

In this code, the `setUp()` method is used to set up a list of numbers before each test case method is run. The `test_sum()` method then uses this list of numbers to test the `sum()` function.

## The tearDown() Method

The `tearDown()` method is a method that is called after each test case method is run. It is used to clean up any resources that were set up in the `setUp()` method.

For example, the following code defines a test case class that uses the `tearDown()` method to clean up a list of numbers after each test case method is run:

```python
import unittest

class TestSum(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 2, 3]

    def tearDown(self):
        del self.numbers

    def test_sum(self):
        self.assertEqual(sum(self.numbers), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

In this code, the `tearDown()` method is used to clean up the list of numbers after each test case method is run. The `test_sum()` method then uses this list of numbers to test the `sum()` function.

## Summary

The `TestCase` class is used to create test cases. It provides a set of assertion methods that can be used to test the behavior of your code. The `TestCase` class is a subclass of the `unittest.TestCase` class. The `setUp()` and `tearDown()` methods are used to set up and clean up any resources that are needed for the test case methods.

By using the `TestCase` class and following best practices, you can ensure that your test cases are well-organized and easy to maintain. This will help you to write better tests and improve the quality of your code.

## What's Next?

In the next section, we will learn about the [`TestLoader`](assets/unittest/3_TestLoader_Class.md) class in the `unittest` module. And how it can be used to load test cases from a test module.

## References

- [Python Documentation - unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)
- [Python Testing with unittest](https://realpython.com/python-testing/)
- [Python Assert Statements](https://realpython.com/python-assert-statement/)
