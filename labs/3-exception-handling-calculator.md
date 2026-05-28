# Lab: Exception Handling Calculator

## Objectives

By completing this lab, students will be able to:

- Use `try`, `except`, `else`, and `finally`
- Handle invalid user input without crashing the program
- Catch specific exceptions such as `ValueError` and `ZeroDivisionError`
- Use loops to keep a console program running
- Write clean functions for calculator operations

---

## Scenario

You are building a simple console calculator. Users should be able to enter two numbers and choose an operation.

The calculator must handle common errors gracefully. If the user enters invalid input, the program should show a helpful message and continue running instead of crashing.

---

## Requirements

Create a Python file named:

```text
exception_calculator.py
```

The calculator app should support:

- Addition
- Subtraction
- Multiplication
- Division
- Exit option

---

## Part 1: Display a Menu

Create a function named `display_menu()` that prints the available options.

Example:

```text
===== Exception Handling Calculator =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

---

## Part 2: Get Valid Numbers

Create a function named `get_number(prompt)` that:

- Asks the user for input
- Converts the input to a `float`
- Handles invalid numeric input using `try` and `except`
- Keeps asking until the user enters a valid number

Example behavior:

```text
Enter first number: hello
Invalid number. Please try again.
Enter first number: 10
```

Hint:

```python
try:
    value = float(input(prompt))
except ValueError:
    print("Invalid number. Please try again.")
```

---

## Part 3: Calculator Functions

Create one function for each operation:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

The `divide()` function should not handle the error itself yet. Let the main program catch the division error.

---

## Part 4: Main Program Loop

Create a `main()` function that:

- Displays the menu
- Gets the user's menu choice
- Gets two numbers when needed
- Calls the correct calculator function
- Prints the result
- Repeats until the user chooses Exit

Use `if`, `elif`, and `else` to handle the user's menu choice.

---

## Part 5: Handle Division by Zero

When the user chooses division, handle this error:

```python
ZeroDivisionError
```

Example behavior:

```text
Enter first number: 10
Enter second number: 0
Cannot divide by zero.
```

The program should continue after showing the error.

---

## Part 6: Add `else` and `finally`

Use an `else` block to print the result only when no exception occurs.

Use a `finally` block to print:

```text
Operation complete.
```

This message should appear after every attempted calculation, even if an error happened.

---

## Starter Code

```python
def display_menu():
    print("\n===== Exception Handling Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose 1-5.")
            continue

        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(first_number, second_number)
            elif choice == "2":
                result = subtract(first_number, second_number)
            elif choice == "3":
                result = multiply(first_number, second_number)
            elif choice == "4":
                result = divide(first_number, second_number)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {result}")
        finally:
            print("Operation complete.")


if __name__ == "__main__":
    main()
```

---

## Test Cases

Run your program and test the following:

### Valid Addition

```text
Choose an option (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
Operation complete.
```

### Invalid Number Input

```text
Choose an option (1-5): 2
Enter first number: abc
Invalid number. Please try again.
Enter first number: 10
Enter second number: 3
Result: 7.0
Operation complete.
```

### Division by Zero

```text
Choose an option (1-5): 4
Enter first number: 10
Enter second number: 0
Cannot divide by zero.
Operation complete.
```

### Invalid Menu Choice

```text
Choose an option (1-5): 9
Invalid choice. Please choose 1-5.
```

### Exit

```text
Choose an option (1-5): 5
Goodbye!
```

---

## Stretch Goals

Try one or more of the following:

- Add exponent support using `**`
- Add floor division using `//`
- Add modulo using `%`
- Round results to two decimal places
- Keep a history of calculations in a list
- Save calculation history to a text file
- Add unit tests for the calculator functions

---

## Reflection Questions

Answer these after completing the lab:

1. What exception happens when a user enters text instead of a number?
2. What exception happens when a number is divided by zero?
3. Why is it better to catch specific exceptions instead of using a broad `except`?
4. What is the difference between `else` and `finally` in exception handling?
5. Why should the program keep running after a user makes a mistake?
