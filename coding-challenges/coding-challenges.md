# Coding Challenges Practice Set 1

---

## How to Practice

1. Open `coding_challenge_checks.py`.
2. Find the starter function for the challenge you want to solve.
3. Replace the `pass` statement with your code.
4. Print the final answer from the function, like an iMocha-style coding prompt.
5. Run the matching checker function.

The checker prints each input, the expected output, and your printed output.

---

# Problem 1: FizzBuzz

## Problem Statement

Write a function named `fizz_buzz(n)` that prints the values from `1` to `n`.

Replace:

- Multiples of `3` with `"Fizz"`
- Multiples of `5` with `"Buzz"`
- Multiples of both `3` and `5` with `"FizzBuzz"`
- All other values with the number itself

## Function Signature

```python
def fizz_buzz(n):
    pass
```

## Input

- `n`: an integer
- `1 <= n <= 10_000`

## Output

Print the values separated by spaces.

## Practice Cases

Try your function with these inputs:

```text
15
5
4
3
20
9
```

---

# Problem 2: Digit Multiplication and Modulo

## Problem Statement

Maria has an integer `n`. She must perform the following operation exactly `k`
times:

1. Multiply the digits of `n` to form a new number.
2. Replace `n` with that new number modulo `m`.
3. After all operations, print the sum of the digits of the final value.

Write a function named `digit_multiply_mod_sum(n, k, m)`.

## Function Signature

```python
def digit_multiply_mod_sum(n, k, m):
    pass
```

## Input

- `n`: starting integer
- `k`: number of operations
- `m`: modulo constant

## Output

Print one integer: the digit sum of the final value.

## Practice Cases

Try your function with these inputs:

```text
38, 2, 5
123, 3, 50
57, 1, 10
99, 2, 100
86, 3, 7
2222, 4, 9
```
