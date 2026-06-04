# Lab: Data Analysis with Pandas, NumPy, and Matplotlib

## Objectives

By completing this lab you will be able to:

- Load and inspect tabular data using `pandas`.
- Use `numpy` for numeric arrays and vectorized operations.
- Clean and transform data with `pandas` and `numpy`.
- Produce basic visualizations with `matplotlib`.
- Save cleaned data and charts to disk.

---

## Prerequisites

- Python 3.8+
- Install dependencies:

```bash
pip install pandas numpy matplotlib
```

Files you'll create and/or use in this lab:

- `data/school_grades.csv` (sample dataset)
- `analysis.py` (starter script using pandas/numpy/matplotlib)

---

## Sample Dataset

Create `data/school_grades.csv` with the following content:

```csv
student_id,name,math_score,english_score,science_score,grade_level
1,Alice,88,92,85,10
2,Bob,76,81,79,10
3,Carol,95,89,94,11
4,David,65,70,60,10
5,Eva,58,62,55,9
6,Frank,84,78,82,11
7,Grace,91,95,93,12
8,Hector,72,68,75,11
9,Ivy,99,98,100,12
10,Jack,45,52,40,9
```

---

## Part 1 — Load & Inspect (Pandas)

1. Load the CSV into a DataFrame.
2. Show the first 5 rows, data types, and basic summary statistics.
3. Report the number of students per `grade_level`.

Starter code (`analysis.py`):

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = "data/school_grades.csv"

def load_data(path):
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_data(INPUT)
    print(df.head())
    print(df.dtypes)
    print(df.describe())
    print(df['grade_level'].value_counts())
```

---

## Part 2 — Clean & Transform (Pandas + NumPy)

Tasks:

1. Ensure score columns (`math_score`, `english_score`, `science_score`) are numeric.
2. Compute an `average_score` column using `numpy` vectorized arithmetic.
3. Create a `pass` boolean column where `average_score >= 60`.
4. Replace any missing names with `Unknown` and strip whitespace from names.

Hints:
- Use `pd.to_numeric(..., errors='coerce')` to coerce invalid scores to `NaN`.
- Use `np.nanmean` or `df.mean(axis=1)` to compute averages.

Example code snippet:

```python
score_cols = ['math_score', 'english_score', 'science_score']
for c in score_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# average ignoring NaNs
df['average_score'] = df[score_cols].mean(axis=1)

# pass boolean
df['pass'] = df['average_score'] >= 60

# clean names
df['name'] = df['name'].fillna('Unknown').str.strip().str.title()
```

---

## Part 3 — Analysis & Aggregation

1. Compute average scores by `grade_level`.
2. Find the top 3 students by `average_score`.
3. Compute the pass rate (percentage) per `grade_level`.

Expected approach:

```python
by_grade = df.groupby('grade_level')['average_score'].mean()
top3 = df.nlargest(3, 'average_score')
pass_rate = df.groupby('grade_level')['pass'].mean() * 100
```

---

## Part 4 — Visualizations (Matplotlib)

Create the following plots and save them as PNG files in `output/`:

1. Histogram of `average_score` (`output/avg_histogram.png`).
2. Bar chart of average score by grade level (`output/avg_by_grade.png`).
3. Scatter plot of `math_score` vs `science_score` colored by `grade_level` (`output/math_vs_science.png`).

Example code for histogram:

```python
plt.figure(figsize=(6,4))
plt.hist(df['average_score'].dropna(), bins=8, color='skyblue', edgecolor='black')
plt.xlabel('Average Score')
plt.ylabel('Count')
plt.title('Distribution of Average Scores')
plt.savefig('output/avg_histogram.png', dpi=150)
```

For scatter, use a colormap with the `grade_level` values.

---

## Part 5 — Save Clean Data

Write the cleaned DataFrame to `output/clean_school_grades.csv` with these columns:

- `student_id`, `name`, `grade_level`, `math_score`, `english_score`, `science_score`, `average_score`, `pass`

Example:

```python
df.to_csv('output/clean_school_grades.csv', index=False)
```

---

## Part 6 — Starter Script (complete example)

Add this to `analysis.py` and run the script to complete lab steps.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = 'data/school_grades.csv'
OUTPUT_DIR = 'output'

def load_data(path):
    return pd.read_csv(path)

def clean_and_transform(df):
    score_cols = ['math_score', 'english_score', 'science_score']
    for c in score_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['average_score'] = df[score_cols].mean(axis=1)
    df['pass'] = df['average_score'] >= 60
    df['name'] = df['name'].fillna('Unknown').str.strip().str.title()
    return df

def plots(df):
    plt.figure(figsize=(6,4))
    plt.hist(df['average_score'].dropna(), bins=8, color='skyblue', edgecolor='black')
    plt.xlabel('Average Score')
    plt.ylabel('Count')
    plt.title('Distribution of Average Scores')
    plt.savefig(f'{OUTPUT_DIR}/avg_histogram.png', dpi=150)

    by_grade = df.groupby('grade_level')['average_score'].mean()
    plt.figure(figsize=(6,4))
    by_grade.plot(kind='bar', color='coral')
    plt.title('Average Score by Grade Level')
    plt.savefig(f'{OUTPUT_DIR}/avg_by_grade.png', dpi=150)

    plt.figure(figsize=(6,4))
    sc = plt.scatter(df['math_score'], df['science_score'], c=df['grade_level'], cmap='viridis')
    plt.colorbar(sc, label='Grade Level')
    plt.xlabel('Math Score')
    plt.ylabel('Science Score')
    plt.title('Math vs Science')
    plt.savefig(f'{OUTPUT_DIR}/math_vs_science.png', dpi=150)

if __name__ == '__main__':
    df = load_data(INPUT)
    df = clean_and_transform(df)
    df.to_csv(f'{OUTPUT_DIR}/clean_school_grades.csv', index=False)
    plots(df)
    print('Done. Outputs in output/')
```

---

## Part 7 — Test Cases

- Confirm `output/clean_school_grades.csv` exists and has the same number of rows as input.
- Confirm `average_score` is numeric and between 0 and 100.
- Confirm three PNG files exist in `output/`.

Example quick checks (run in Python):

```python
import os
import pandas as pd
assert os.path.exists('output/clean_school_grades.csv')
df = pd.read_csv('output/clean_school_grades.csv')
assert 'average_score' in df.columns
assert df['average_score'].between(0,100).all()
for f in ['avg_histogram.png','avg_by_grade.png','math_vs_science.png']:
    assert os.path.exists(f'output/{f}')
```

---

## Stretch Goals

- Add `rejected` logging for rows with invalid scores.
- Create summary statistics (median, std-dev) per `grade_level`.
- Use `seaborn` for enhanced visualizations.
- Add CLI flags for input/output paths.

---

## Reflection Questions

1. When is vectorized NumPy computation preferable to row-wise operations?
2. Why is it important to handle missing numeric values before aggregations?
3. What visualization best shows distribution vs. relationship between two variables?

---