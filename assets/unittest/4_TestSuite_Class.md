# Unittest - The TestSuite Class

## The TestSuite Class

The TestSuite class is used to create a test suite. A test suite is a collection of test cases that can be run together. The TestSuite class provides a set of methods that can be used to add test cases to the test suite.

The TestSuite class is a subclass of the unittest.TestSuite class. It provides a set of methods that can be used to create a test suite.

The following table lists some of the most commonly used methods of the TestSuite class:

| Method | Description | Example |
| --- | --- | --- |
| addTest(test) | Adds a test case to the test suite | suite.addTest(TestSum('test_sum')) |
| addTests(tests) | Adds a list of test cases to the test suite | suite.addTests([TestSum('test_sum'), TestSum('test_sub')]) |
| addTestSuite(test_suite) | Adds a test suite to the test suite | suite.addTestSuite(TestSum) |
| run(result) | Runs the test suite | suite.run(result) |

For example, the following code creates a test suite and adds test cases to it:

```python

import unittest

from test_sum import TestSum
from test_sub import TestSub

suite = unittest.TestSuite()
suite.addTest(TestSum('test_sum'))
suite.addTest(TestSub('test_sub'))

result = unittest.TestResult()
suite.run(result)

```

## How to Use the TestSuite Class

To use the TestSuite class, you need to create a test suite and add test cases to it using the `addTest()`, `addTests()`, and `addTestSuite()` methods. You can then run the test suite using the `run()` method.

## Summary

In this chapter, we learned about the TestSuite class and how it can be used to create a test suite. We learned about the importance of test suites and how they can be used to run test cases together.

## What's Next?

In the next chapter, we will learn about the [`TestRunner class`](assets/unittest/5_TestRunner_Class.md) and how it can be used to run test suites and generate test reports.

## Resources

- [Unittest Documentation](http://docs.python.org/library/unittest.html)
- [Unittest - Python Testing](https://realpython.com/python-testing/)
- [Unittest - TestSuite Class](https://docs.python.org/3/library/unittest.html#unittest.TestSuite)
