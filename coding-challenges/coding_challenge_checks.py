"""
Practice checkers for the root coding challenges.

Student instructions:

1. Read the challenge descriptions in:
   - coding-challenges.md
   - coding-challenges-2.md
2. Complete only the four student functions in the "Student Work Area" below.
3. Each function should print the answer. Do not return the answer.
4. Run one checker at a time to compare your printed output with the expected output.

"""

from contextlib import redirect_stdout
from io import StringIO


# ---------------------------------------------------------------------------
# Student Work Area
# ---------------------------------------------------------------------------
# Complete the four functions below.
# Replace each pass statement with your own code.
# Do not change the function names or parameters because the checkers call them.
# Print your final answer from each function.


def fizz_buzz(n):
    """
    Print the answer for the FizzBuzz challenge.

    For each number from 1 through n:
    - Use "FizzBuzz" for multiples of both 3 and 5.
    - Use "Fizz" for multiples of 3.
    - Use "Buzz" for multiples of 5.
    - Use the number itself for all other values.

    Print the values separated by spaces.
    """
    pass


def digit_multiply_mod_sum(n, k, m):
    """
    Print the final digit sum for the digit multiplication challenge.

    Repeat k times:
    - Multiply the digits of n together.
    - Replace n with that product modulo m.

    After the loop, print the sum of the digits of the final n.
    """
    pass


def same_start_end_count(paragraph):
    """
    Print the count of words that start and end with the same letter.

    Rules:
    - Ignore uppercase/lowercase differences.
    - Ignore punctuation.
    - Single-letter words count.
    """
    pass


def flexible_peak_count(arr):
    """
    Print the count of flexible peaks.

    Check only positions that have both a left and right neighbor.
    A value is a flexible peak when either:
    - It is greater than both neighbors.
    - Its difference from the left neighbor equals its difference from the right.
    """
    pass


# ---------------------------------------------------------------------------
# Checker Code
# ---------------------------------------------------------------------------
# Do not edit anything below this line while practicing.
# The checker functions call your student functions above and compare your
# printed output against hard-coded expected values.


def _check_function(function_name, test_cases):
    function = globals()[function_name]

    if function.__code__.co_code == (lambda: None).__code__.co_code:
        print(f"{function_name}: not started yet.")
        return False

    passed = 0
    total = len(test_cases)

    for index, (test_case, expected) in enumerate(test_cases, start=1):
        args = test_case if isinstance(test_case, tuple) else (test_case,)
        try:
            output = StringIO()
            with redirect_stdout(output):
                function(*args)
            actual = output.getvalue().strip()
        except Exception as exc:
            print(f"\nCase {index}: ERROR")
            print(f"Input: {test_case}")
            print(f"Raised: {type(exc).__name__}: {exc}")
            continue

        expected_output = str(expected)
        status = "PASS" if actual == expected_output else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"\nCase {index}: {status}")
        print(f"Input: {test_case}")
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual}")

    print(f"\n{function_name}: passed {passed} of {total} cases.")
    return passed == total


# Do not edit: checker for Problem 1 in coding-challenges.md.
def check_fizz_buzz():
    test_cases = [
        (
            15,
            "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz",
        ),
        (5, "1 2 Fizz 4 Buzz"),
        (4, "1 2 Fizz 4"),
        (3, "1 2 Fizz"),
        (
            20,
            "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz",
        ),
        (9, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz"),
        (1, "1"),
        (
            30,
            "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz",
        ),
    ]
    return _check_function("fizz_buzz", test_cases)


# Do not edit: checker for Problem 2 in coding-challenges.md.
def check_digit_multiply_mod_sum():
    test_cases = [
        ((38, 2, 5), 4),
        ((123, 3, 50), 6),
        ((57, 1, 10), 5),
        ((99, 2, 100), 8),
        ((86, 3, 7), 6),
        ((2222, 4, 9), 7),
        ((0, 3, 11), 0),
    ]
    return _check_function("digit_multiply_mod_sum", test_cases)


# Do not edit: checker for Problem 1 in coding-challenges-2.md.
def check_same_start_end_count():
    test_cases = [
        ("Bob baked a big banana bread.", 2),
        ("Anna went to vote in the civic center.", 2),
        ("Hello world! No matching words here.", 0),
        ("A I U E O", 5),
        ("Did dad see Eve and Otto today?", 4),
        ("Wow! Hannah and Anna went kayaking at noon.", 4),
        ("Level, radar, and civic!", 3),
    ]
    return _check_function("same_start_end_count", test_cases)


# Do not edit: checker for Problem 2 in coding-challenges-2.md.
def check_flexible_peak_count():
    test_cases = [
        ([3, 2, 3, 1, 3], 3),
        ([1, 4, 2, 6, 3, 5, 4], 3),
        ([3, 7, 3, 8, 3], 2),
        ([5, 5, 5, 5, 5, 5], 4),
        ([10, 1, 10, 9], 2),
        ([2, 5, 2, 5, 2, 5, 2, 5], 6),
        ([1, 2], 0),
    ]
    return _check_function("flexible_peak_count", test_cases)


# Do not edit: runs every checker in this file.
def check_all():
    results = [
        check_fizz_buzz(),
        check_digit_multiply_mod_sum(),
        check_same_start_end_count(),
        check_flexible_peak_count(),
    ]
    if all(results):
        print("\nAll challenge checks passed.")
    else:
        print("\nSome challenge checks still need work.")
    return all(results)

# Check Any
# check_same_start_end_count()
# check_fizz_buzz()
# check_digit_multiply_mod_sum()
# check_flexible_peak_count()
# check_all()