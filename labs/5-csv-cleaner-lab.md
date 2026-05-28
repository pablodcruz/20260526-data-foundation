# Lab: CSV Cleaner

## Objectives

By completing this lab, students will be able to:

- Read data from a CSV file
- Clean and standardize string values
- Validate numeric data
- Skip or track invalid rows
- Write cleaned data to a new CSV file

---

## Scenario

You received a messy student grades file. Some names have extra spaces, some names use inconsistent capitalization, and some grades are invalid.

Your job is to create a script that reads the messy file, cleans the valid records, and writes the clean records to a new file.

---

## Requirements

Create a Python file named:

```text
csv_cleaner.py
```

Create an input file named:

```text
messy_grades.csv
```

The script should create an output file named:

```text
clean_grades.csv
```

---

## Sample Input File

Create `messy_grades.csv` with this content:

```csv
name,grade
 alice,85
BOB, ninety
carol,92
,70
david,-5
eva,101
 frank ,88
grace,95
```

---

## Cleaning Rules

A row is valid only if:

- The name is not empty
- The grade is a number
- The grade is between 0 and 100

Clean valid rows by:

- Stripping extra spaces from names
- Converting names to title case
- Converting grades to integers

Example:

```text
 frank ,88
```

Should become:

```text
Frank,88
```

---

## Part 1: Read the CSV File

Create a function named `read_rows(file_name)` that:

- Opens the CSV file
- Reads each row into a dictionary
- Returns a list of rows

Use the built-in `csv` module:

```python
import csv
```

Hint:

```python
with open(file_name, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
```

---

## Part 2: Validate and Clean One Row

Create a function named `clean_row(row)` that:

- Accepts one row dictionary
- Returns a cleaned row dictionary if the row is valid
- Returns `None` if the row is invalid

Example return value:

```python
{
    "name": "Alice",
    "grade": 85
}
```

Use `try` and `except` to handle invalid grade values.

---

## Part 3: Clean All Rows

Create a function named `clean_rows(rows)` that:

- Loops through all rows
- Calls `clean_row(row)` for each row
- Stores valid cleaned rows in one list
- Stores invalid rows in another list
- Returns both lists

Example:

```python
cleaned_rows, rejected_rows = clean_rows(rows)
```

---

## Part 4: Write the Clean CSV File

Create a function named `write_clean_rows(file_name, cleaned_rows)` that:

- Writes the cleaned rows to `clean_grades.csv`
- Includes the header row

Expected output:

```csv
name,grade
Alice,85
Carol,92
Frank,88
Grace,95
```

---

## Part 5: Print a Summary

After the script runs, print:

- Total rows read
- Number of valid rows
- Number of rejected rows
- Output file name

Example:

```text
Rows read: 8
Valid rows: 4
Rejected rows: 4
Clean file written to clean_grades.csv
```

---

## Starter Code

```python
import csv


INPUT_FILE = "messy_grades.csv"
OUTPUT_FILE = "clean_grades.csv"


def read_rows(file_name):
    with open(file_name, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_row(row):
    name = row["name"].strip().title()
    grade_text = row["grade"].strip()

    if name == "":
        return None

    try:
        grade = int(grade_text)
    except ValueError:
        return None

    if grade < 0 or grade > 100:
        return None

    return {
        "name": name,
        "grade": grade
    }


def clean_rows(rows):
    cleaned_rows = []
    rejected_rows = []

    # TODO: Loop through rows and sort each row into one of the lists

    return cleaned_rows, rejected_rows


def write_clean_rows(file_name, cleaned_rows):
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)


def main():
    rows = read_rows(INPUT_FILE)
    cleaned_rows, rejected_rows = clean_rows(rows)
    write_clean_rows(OUTPUT_FILE, cleaned_rows)

    # TODO: Print summary


if __name__ == "__main__":
    main()
```

---

## Test Cases

### Valid Rows

These rows should appear in `clean_grades.csv`:

```csv
Alice,85
Carol,92
Frank,88
Grace,95
```

### Invalid Rows

These rows should be rejected:

```text
BOB, ninety
,70
david,-5
eva,101
```

### Summary Output

```text
Rows read: 8
Valid rows: 4
Rejected rows: 4
Clean file written to clean_grades.csv
```

---

## Stretch Goals

- Write rejected rows to `rejected_grades.csv`
- Add a rejection reason for each bad row
- Calculate the average grade from valid rows
- Sort clean rows by grade from highest to lowest
- Accept the input file name from the user
- Handle `FileNotFoundError` if the input file is missing

---

## Reflection Questions

1. Why is CSV data often messy in real projects?
2. Why should invalid rows be rejected instead of silently changed?
3. What does `csv.DictReader` do?
4. Why do we use `newline=""` when opening CSV files?
5. How is this lab similar to an ETL pipeline?
