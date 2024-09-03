# Unittest - The TestRunner Class

The TestRunner class is used to run test cases. It provides a set of methods that can be used to run test cases and generate test reports.

The TestRunner class is a subclass of the unittest.TextTestRunner class. It provides a set of methods that can be used to run test cases and generate test reports.

The following table lists some of the most commonly used methods of the TestRunner class:

| Method | Description | Example |
| --- | --- | --- |
| run(test) | Runs the test case | runner.run(suite) |
| run(result) | Runs the test case and generates a test report | runner.run(suite, result) |

For example, the following code runs a test case and generates a test report:

```python
import unittest

from test_sum import TestSum
from test_sub import TestSub

suite = unittest.TestSuite()
suite.addTest(TestSum('test_sum'))
suite.addTest(TestSub('test_sub'))

runner = unittest.TextTestRunner()
result = unittest.TestResult()
runner.run(suite, result)
```

In this code, the `run()` method is used to run the test case and generate a test report. The `run()` method takes the test case and the test result as arguments and generates a test report.

The TestRunner class provides a set of methods that can be used to run test cases and generate test reports. These methods can be used to run test cases and generate test reports.

## Summary

In this chapter, we learned about the TestRunner class and how it can be used to run test cases and generate test reports. We also learned about some of the most commonly used methods of the TestRunner class.

## What's Next?

In the next chapter, we will learn about what is [`Pytest`](assets/pytest/1_Pytest_In_Python.md) and how it can be used to write and run tests for your code.

## Resources

- [Unittest Documentation](http://docs.python.org/library/unittest.html)
- [Unittest - Python Testing](https://realpython.com/python-testing/)
