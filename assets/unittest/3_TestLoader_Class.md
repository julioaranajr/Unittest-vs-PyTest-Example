# Unittest - The TestLoader Class

## The TestLoader Class

The TestLoader class is used to load test cases from a test module. It provides a set of methods that can be used to load test cases from a test module.

The TestLoader class is a subclass of the unittest.TestLoader class. It provides a set of methods that can be used to load test cases from a test module.

The following table lists some of the most commonly used methods of the TestLoader class:

| Method | Description | Example |
| --- | --- | --- |
| loadTestsFromModule(module) | Loads test cases from a test module | loader.loadTestsFromModule(test_module) |
| loadTestsFromTestCase(test_case) | Loads test cases from a test case class | loader.loadTestsFromTestCase(TestSum) |
| loadTestsFromName(name) | Loads test cases from a test case method | loader.loadTestsFromName('TestSum.test_sum') |
| loadTestsFromNames(names) | Loads test cases from a list of test case methods | loader.loadTestsFromNames(['TestSum.test_sum', 'TestSum.test_sub']) |

For example, the following code loads test cases from a test module:

```python
import unittest

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_module)
```

In this code, the `loadTestsFromModule()` method is used to load test cases from a test module. The `loadTestsFromModule()` method takes the test module as an argument and returns a test suite that contains the test cases from the test module.

The TestLoader class provides a set of methods that can be used to load test cases from a test module. These methods can be used to create a test suite that contains the test cases from the test module.

## Summary

In this chapter, we learned about the TestLoader class and how it can be used to load test cases from a test module. We also learned about some of the most commonly used methods of the TestLoader class.

## What's Next?

In the next chapter, we will learn about the [`TestSuite class`](assets/unittest/4_TestSuite_Class.md) and how it can be used to create a test suite. And how it can be used to run test cases.

## Resources

- [Unittest Documentation](http://docs.python.org/library/unittest.html)
- [Unittest - Python Testing](https://realpython.com/python-testing/)
