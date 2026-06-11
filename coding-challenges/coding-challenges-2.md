# Coding Challenges Practice Set 2

---

## How to Practice

1. Open `coding_challenge_checks.py`.
2. Find the starter function for the challenge you want to solve.
3. Replace the `pass` statement with your code.
4. Print the final answer from the function, like an iMocha-style coding prompt.
5. Run the matching checker function.

The checker prints each input, the expected output, and your printed output.

---

# Problem 1: Same Starting and Ending Letter

## Problem Statement

Write a function named `same_start_end_count(paragraph)` that prints how many
words in a paragraph start and end with the same letter.

Words should be checked:

- Case-insensitively
- Ignoring punctuation
- Single-letter words count

## Function Signature

```python
def same_start_end_count(paragraph):
    pass
```

## Input

- `paragraph`: a string
- `1 <= len(paragraph) <= 1000`

## Output

Print one integer: the number of matching words.

## Practice Cases

Try your function with these inputs:

```text
"Bob baked a big banana bread."
"Anna went to vote in the civic center."
"Hello world! No matching words here."
"A I U E O"
"Did dad see Eve and Otto today?"
"Wow! Hannah and Anna went kayaking at noon."
```

---

# Problem 2: Flexible Peaks

## Problem Statement

Write a function named `flexible_peak_count(arr)` that prints how many flexible
peaks exist in a list of integers.

A position `i` is a flexible peak if `1 <= i <= len(arr) - 2` and at least one
of these is true:

1. `arr[i]` is strictly greater than both neighbors.
2. The difference between `arr[i]` and each neighbor is equal.

## Function Signature

```python
def flexible_peak_count(arr):
    pass
```

## Input

- `arr`: a list of integers

## Output

Print one integer: the number of flexible peaks.

## Practice Cases

Try your function with these inputs:

```text
[3, 2, 3, 1, 3]
[1, 4, 2, 6, 3, 5, 4]
[3, 7, 3, 8, 3]
[5, 5, 5, 5, 5, 5]
[10, 1, 10, 9]
[2, 5, 2, 5, 2, 5, 2, 5]
```