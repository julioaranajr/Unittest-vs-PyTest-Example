# Outputs

This file contains the outputs of the tests run in the `test_calculator.py` file.

## Test Output without Verbose

```bash
❯ python3 -m unittest
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK

```

## Test Output with Verbose

```bash
❯ python3 -m unittest -v
test_add (test_calculator.TestCalculator) ... ok
test_division (test_calculator.TestCalculator) ... ok
test_multiply (test_calculator.TestCalculator) ... ok
test_my_calc_instance (test_calculator.TestCalculator) ... ok
test_subtract (test_calculator.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK

```

## Test Failure Output

```bash
❯ python3 -m unittest -v
test_add (test_calculator.TestCalculator) ... FAIL
test_division (test_calculator.TestCalculator) ... ok
test_multiply (test_calculator.TestCalculator) ... ok
test_my_calc_instance (test_calculator.TestCalculator) ... ok
test_subtract (test_calculator.TestCalculator) ... ok

======================================================================
FAIL: test_add (test_calculator.TestCalculator)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/username/Projects/testing/unittest/test_calculator.py", line 15, in test_add
    self.assertEqual(self.calc.add(1, 2), 3)
AssertionError: 0 != 3

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)

```
