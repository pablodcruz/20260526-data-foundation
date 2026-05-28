# Lab: Unit Testing With Pytest

## Objectives

By completing this lab, students will be able to:

- Explain what a unit test is
- Write tests using `pytest`
- Use `assert` to verify expected behavior
- Test normal cases and edge cases
- Separate application logic from test code

---

## Scenario

You are given a small utility module for cleaning and validating student data. Your job is to write unit tests that prove the functions work correctly.

Testing helps catch bugs early and gives developers confidence when changing code.

---

## Requirements

Create two files:

```text
student_utils.py
test_student_utils.py
```

The first file will contain the functions.

The second file will contain your tests.

---

## Part 1: Create the Utility Module

Create `student_utils.py` with these functions:

```python
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def clean_name(name):
    return name.strip().title()


def is_passing(grade):
    return grade >= 70


def is_valid_grade(grade):
    return 0 <= grade <= 100
```

---

## Part 2: Install Pytest

If `pytest` is not installed, install it:

```bash
pip install pytest
```

Run tests with:

```bash
pytest
```

Or:

```bash
pytest -v
```

---

## Part 3: Write Your First Test

Create `test_student_utils.py`.

Import the function you want to test:

```python
from student_utils import calculate_average
```

Write a test:

```python
def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90
```

Run:

```bash
pytest -v
```

---

## Part 4: Test Average Edge Cases

Add tests for:

- Empty grade list
- One grade
- Decimal result

Example:

```python
def test_calculate_average_empty_list():
    assert calculate_average([]) == 0
```

---

## Part 5: Test Name Cleaning

Write tests for `clean_name(name)`.

Examples:

```python
clean_name(" ada ")      # "Ada"
clean_name("ALAN TURING") # "Alan Turing"
```

Test at least three different name inputs.

---

## Part 6: Test Passing Logic

Write tests for `is_passing(grade)`.

Rules:

- 70 or higher is passing
- Below 70 is not passing

Make sure to test the boundary value `70`.

---

## Part 7: Test Grade Validation

Write tests for `is_valid_grade(grade)`.

Rules:

- Valid grades are from 0 to 100
- Negative grades are invalid
- Grades above 100 are invalid

Make sure to test boundary values:

- `0`
- `100`
- `-1`
- `101`

---

## Starter Test Code

```python
from student_utils import (
    calculate_average,
    clean_name,
    is_passing,
    is_valid_grade,
)


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_calculate_average_empty_list():
    assert calculate_average([]) == 0


def test_clean_name_removes_spaces_and_formats_case():
    assert clean_name(" ada ") == "Ada"


def test_is_passing_true_for_70():
    assert is_passing(70) is True


def test_is_passing_false_below_70():
    assert is_passing(69) is False


def test_is_valid_grade_accepts_boundaries():
    assert is_valid_grade(0) is True
    assert is_valid_grade(100) is True


def test_is_valid_grade_rejects_out_of_range_values():
    assert is_valid_grade(-1) is False
    assert is_valid_grade(101) is False
```

---

## Expected Output

When all tests pass, you should see output similar to:

```text
7 passed
```

If a test fails, read the failure message carefully. Pytest will show:

- Which test failed
- What value was expected
- What value was actually returned

---

## Part 8: Introduce a Bug

Change this function temporarily:

```python
def is_passing(grade):
    return grade > 70
```

Run the tests again.

One test should fail because `70` should count as passing.

After observing the failure, fix the function.

---

## Stretch Goals

- Add a function named `letter_grade(grade)`
- Write tests for A, B, C, D, and F grades
- Add tests for invalid grade values
- Use `pytest.mark.parametrize`
- Add a function that raises `ValueError` for invalid grades
- Test the error with `pytest.raises`

---

## Reflection Questions

1. What is a unit test?
2. Why should test function names be descriptive?
3. What is an edge case?
4. Why is `70` an important test case for `is_passing()`?
5. How can tests help when you refactor code?
