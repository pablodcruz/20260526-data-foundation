# Week 1 — Python Fundamentals, Git, and Agile

## Learning Outcomes

By the end of this week you will be able to:

* Explain SDLC & Agile, write clear user stories with acceptance criteria, and run daily stand-ups.
* Use Git professionally: branch, commit, push/pull, open PRs, resolve conflicts, and follow Conventional Commits.
* Set up a Python 3.11+ environment with `venv`, run scripts, use the REPL and Jupyter.
* Write Python that uses variables, expressions, **casting**, control flow, **functions (incl. lambdas)**, core data structures, and **namespaces/scope (LEGB)**.
* Describe and use **data types** including strings, numbers, **range**, lists, tuples, sets, dicts, **binary types** (bytes/bytearray), booleans, and `NoneType`.
* Build simple programs using **iterators** and idiomatic loops.

---

### 💻 Admin & Setup

* **Tooling**

  * Python 3.11+ (verify: `python --version` or `python3 --version`)
  * VS Code + extensions: *Python*, *Pylance*, *Jupyter*
  * Git + a GitHub account

* **Project bootstrap**

  ```bash
  git clone <your-repo-url> data-foundations
  cd data-foundations

  # virtual env
  python -m venv .venv
  # Windows (PowerShell): .\.venv\Scripts\Activate.ps1
  # Windows (Git Bash):   source .venv/Scripts/activate
  # macOS/Linux:
  source .venv/bin/activate

  python -m pip install --upgrade pip
  pip install pandas
  ```

---

## 🐍 Python Orientation

### 🌐 Full-Stack Context

Modern software typically has three layers:

* **Frontend** → user interface (web or mobile).
* **Backend** → APIs, business logic, and databases.
* **Data Layer** → ETL pipelines, analytics, and warehousing.

Python fits across all layers — especially in the **data layer** — as a flexible scripting and integration language.

---

### 💡 Why Python for Data Foundations

* **Fast iteration** and easy to read.
* **Rich ecosystem**: `pandas`, `numpy`, `sqlalchemy`, `airflow`, and more.
* Acts as a **“glue language”** connecting SQL, APIs, and automation tasks.

---

### ⚙️ Interpreter vs. Compiler

* **Interpreter** → executes code **line by line**.
* **Compiler** → translates code into **machine instructions** ahead of time (e.g., C/C++).
* **Python** (via CPython) compiles your code into **bytecode**, then runs it inside its **virtual machine** — giving the flexibility of an interpreted language with decent performance.

---

### ⏩ REPL/Jupyter

* REPL: `python` (or `python -i`) for quick experiments.
* Jupyter: literate notebooks for demos/EDA; keep “production” logic in `.py` modules. Designed for interactive, cell-based learning and data exploration.
* Tools like Jupyter and Replit are great for quick tests, data exploration, and sharing small code snippets.
But to build real applications — where you control dependencies, structure, and deployment —
you should learn to work locally with VS Code and virtual environments.

---

### ⚙️ SDLC (Software Development Life Cycle)

### 🧩 Phases

1. **Requirements** → Gather what the system must do.
2. **Design** → Plan architecture, UI, and database structure.
3. **Implementation** → Write and integrate the code.
4. **Testing** → Verify correctness and quality.
5. **Deployment** → Release the product to users.
6. **Maintenance** → Fix bugs, update features, monitor performance.

💡 Think of SDLC as the *blueprint* for building and maintaining software effectively.

---

### 💧 Waterfall Model

* **Sequential** process (each phase must finish before the next).
* Simple and easy to manage.
* **Best for:** projects with *clear, fixed requirements*.
* ❌ Hard to change once development begins.

---

### 🔁 Agile Model

* **Iterative & adaptive** — work in short cycles called **sprints** (usually 1–2 weeks).
* Focus on **continuous feedback**, **collaboration**, and **working software**.
* **Best for:** evolving projects and team-based development.

---

### 👥 Agile for Developers

#### 💡 Agile Values (from the Agile Manifesto)

1. **Individuals and interactions** over processes and tools.
2. **Working software** over comprehensive documentation.
3. **Customer collaboration** over contract negotiation.
4. **Responding to change** over following a plan.

---

#### 🧭 Scrum Framework (most common Agile approach)

**Roles:**

* **PO (Product Owner):** Defines vision, manages backlog.
* **SM (Scrum Master):** Facilitates process, removes blockers.
* **Dev Team:** Builds and delivers working increments.

**Ceremonies:**

* **Sprint Planning:** define sprint goals and tasks.
* **Daily Stand-up:** ≤15 min sync on progress/blockers.
* **Sprint Review:** demo completed work to stakeholders.
* **Retrospective:** reflect and improve process.

---

#### 🧱 User Story Format

> As a `<role>`, I want `<goal>` so that `<benefit>`.

Include **Acceptance Criteria** (clear conditions for success).

Example:

```
As a user, I want to reset my password
so that I can access my account if I forget it.

Acceptance Criteria:
- Reset link sent to registered email.
- Must expire after 10 minutes.
```

---

#### 🔢 Story Pointing

* Measures **effort/complexity**, not time.
* Uses **relative sizing** (often **Fibonacci sequence**: 1, 2, 3, 5, 8, 13...).
* Helps teams plan sprints realistically.

---

✅ **Summary**

| Model         | Key Traits          | Best For                     |
| ------------- | ------------------- | ---------------------------- |
| **Waterfall** | Linear, fixed steps | Predictable projects         |
| **Agile**     | Iterative, flexible | Dynamic, collaborative teams |

---

## Git Fundamentals

### Source Control Management (SCM)

* **VCS**: track changes & history.
* **CVCS**: centralized (single server).
* **DVCS**: distributed (e.g., **Git**); full history per clone.

### File states & everyday commands

```bash
git init                         # initialize repository
git remote add origin <URL>      # link remote
git status
git add <path>                   # stage changes
git commit -m "feat: initial commit"
git branch                       # list branches
git checkout -b feat/basics      # create & switch
git push -u origin feat/basics   # first push
git pull                         # fetch+merge current branch
git merge <branch>               # merge into current branch
git log --oneline --graph
```

**Conventional Commits**: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:` (e.g., `feat(core): add cli basics`).

**Quick exercises** (Git katas):

* Init a repo, add a file, create a feature branch, open a PR.
* Create a merge conflict with a partner and resolve it.
* Add a `.gitignore` for Python:

  ```
  __pycache__/
  *.pyc
  .venv/
  .env
  .DS_Store
  Thumbs.db
  ```

---

## Python Basics

### 🐍 What is Python? Why Python?

* **High-level, interpreted language** focused on readability and simplicity.
* **Batteries-included**: rich standard library for files, networking, math, data, and more.
* **Cross-domain power**: great for **data science**, **AI/ML**, **web development**, **automation**, and **scripting**.
* **Strong community & ecosystem** — huge package index (PyPI) and active open-source support.

---

### ✍️ Syntax & Style

* **Indentation is semantic** → indentation defines code blocks (no `{}`); standard is **4 spaces**.
* **Naming** → use `snake_case` for variables and functions, `PascalCase` for classes, `UPPER_CASE` for constants.
* **Docstrings** → triple quotes `"""..."""` for documenting functions, classes, or modules.
* **Comments** → start with `#` for single-line comments.
* **Follow PEP 8** → the official Python style guide.

```python
def get_score(name: str) -> int:
    """Return the score for a given player."""
    score = 100  # starting value
    return score
```

---

### Variables and Data Types

#### 🔹 Strongly Typed

* Once a variable has a type, Python **won’t automatically convert** it for you.
* You **can’t mix incompatible types** without explicit casting.

Example:

```python
x = "10"
y = 5
print(x + y)      # ❌ TypeError (string + int not allowed)
print(int(x) + y) # ✅ 15
```

💡 **Meaning:**
Python *remembers* each variable’s type and enforces rules between them.
It won’t silently guess what you meant — that’s what makes it *strongly typed*.

---

#### 🔹 Dynamically Bound (Dynamically Typed)

* You **don’t declare variable types** in advance.
* The type is decided **at runtime** when the value is assigned.
* You can reassign variables to values of different types.

Example:

```python
x = 42         # x is an int
x = "hello"    # now x is a str
```

💡 **Meaning:**
Python *binds* variables to objects dynamically — the **object** has a type, not the **name**.

* Built-ins datatypes: `int`, `float`, `bool`, `str`, `list`, `tuple`, `set`, `dict`, `NoneType`.

### 🔄 Casting

**Type casting** means converting a value from one data type to another.
Python has many built-ins for this — useful when handling user input, files, or APIs.

#### 🔹 Common Conversions

| Function        | Converts To         | Example                | Output            |
| --------------- | ------------------- | ---------------------- | ----------------- |
| `int(x)`        | Integer             | `int("10")`            | `10`              |
| `float(x)`      | Float               | `float("3.14")`        | `3.14`            |
| `str(x)`        | String              | `str(42)`              | `"42"`            |
| `bool(x)`       | Boolean             | `bool(0), bool("hi")`  | `False, True`     |
| `list(x)`       | List                | `list("abc")`          | `['a', 'b', 'c']` |
| `tuple(x)`      | Tuple               | `tuple([1, 2, 3])`     | `(1, 2, 3)`       |
| `set(x)`        | Set (unique values) | `set([1,1,2])`         | `{1, 2}`          |
| `bytes(x, enc)` | Bytes               | `bytes("hi", "utf-8")` | `b'hi'`           |

---

### User Input and Output

```python
name = input("Name: ") # input
print(f"Hello, {name}!") # output
```

---

### 💬 Comments

* **Single-line:** start with `#`
* **Block comments:** use multiple `#` lines for clarity
* **Docstrings:** triple quotes (`""" ... """`) for documenting modules, classes, or functions

```python
# This is a single-line comment
# Explains what the next line does
x = 42  # inline comment

def greet(name):
    """Return a friendly greeting."""  # docstring
    return f"Hello, {name}!"
help(greet)
```

✅ Comments are ignored by Python.
✅ Docstrings can be accessed via `help()` or `__doc__`.

---

### 🌐 Namespaces & Scope (LEGB)

**Namespace** = a mapping of names to objects (like a dictionary).
**Scope** = the region of code where a name is visible.

Python looks up names in this order (the **LEGB rule**):

> **L**ocal → **E**nclosing → **G**lobal → **B**uilt-ins

---

#### 🔹 Example

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()

outer()
```

Lookup order inside `inner()`:

1. **Local** (`x = "local"`)
2. **Enclosing** (`x = "enclosing"`)
3. **Global** (`x = "global"`)
4. **Built-in** (like `len`, `print`, etc.)

---

#### 🔹 Modifying Variables

To modify variables outside the local scope:

```python
def outer():
    count = 0
    def inner():
        nonlocal count  # refers to outer's 'count'
        count += 1
        print(count)
    inner()
```

And for globals:

```python
x = 0
def update():
    global x
    x += 1
    print(x)
```

---

#### **Summary**

* Every function creates a new **local scope**.
* Python resolves names using **LEGB** order.
* Use `global` or `nonlocal` only when truly necessary.

---

## Python Data Types

### ✅ Booleans & NoneType

```python
is_ready = True
nothing = None
```

* `bool`: represents truth values `True` or `False`.
* `None`: special constant for “no value” or “empty result.”
* Common in condition checks:

  ```python
  if is_ready:
      print("Go!")
  if nothing is None:
      print("Nothing here.")
  ```

---

### 🔢 Numbers

* **`int`** → whole numbers (unbounded in size).
* **`float`** → decimal numbers (IEEE 754).
* **`complex`** → optional for real + imaginary parts (`3 + 4j`).
* **`Decimal`** → from `decimal` module for precision-critical work (e.g. finance).

```python
from decimal import Decimal
price = Decimal("19.99")
```

---

### 🧵 Strings

* Immutable sequences of characters.
* Common methods: `.split()`, `.join()`, `.replace()`, `.startswith()`.
* Support **slicing** and **f-strings** for formatting.

```python
s = "hello world"
print(s[0:5])          # 'hello'
print(f"Greeting: {s}") # f-string
```

---

### 🔁 Range

```python
for i in range(3):  # 0, 1, 2
    print(i)
```

* Generates a sequence of numbers without storing all in memory.
* Often used in `for` loops.

---

### 📋 Lists

* **Ordered**, **mutable** (changeable), can hold **mixed types**.
* Best for general-purpose dynamic collections.
* Support **slicing**: `[start:end:step]`.

```python
nums = [10, 20, 30, 40]
nums.append(50)
print(nums[1:3])   # [20, 30]
```

✅ Add/remove items anytime (`append`, `pop`, `remove`)
✅ Great for iteration, sorting, and dynamic data

---

### 🔸 Tuples

* **Ordered**, **immutable** (cannot be changed after creation).
* Use when data should not change or to group related values.

```python
point = (10, 20)
print(point[0])   # 10
```

✅ Safe, lightweight, hashable (can be dict keys)
⚠️ Cannot modify or append after creation

---

### 🔷 Sets

* **Unordered**, **mutable**, stores **unique** items only.
* Useful for deduplication or mathematical set operations.

```python
colors = {"red", "green", "blue"}
colors.add("red")   # duplicate ignored
print(colors)       # {'green', 'blue', 'red'}
```

✅ Fast membership tests (`"red" in colors`)
✅ Supports union/intersection/difference

---

### 🗝️ Dictionaries

* **Unordered key–value mappings** (insertion order preserved since Python 3.7).
* Keys must be unique and immutable.

```python
person = {"name": "Alice", "age": 30}
print(person["name"])  # Alice
person["age"] = 31
```

✅ Fast lookups by key
✅ Great for structured or JSON-like data

---

#### 🧩 Summary

| Type      | Ordered  | Mutable | Unique      | Key–Value | Typical Use       |
| --------- | -------- | ------- | ----------- | --------- | ----------------- |
| **List**  | ✅        | ✅       | ❌           | ❌         | Dynamic sequence  |
| **Tuple** | ✅        | ❌       | ❌           | ❌         | Fixed grouping    |
| **Set**   | ❌        | ✅       | ✅           | ❌         | Unique collection |
| **Dict**  | ✅ (3.7+) | ✅       | Keys unique | ✅         | Mapped data       |

---

### 💾 Binary Types

Python has three main types for working with **binary data** — useful for files, networking, and performance-critical code.

```python
b = b"hello"                # bytes (immutable sequence of bytes)
ba = bytearray(b)           # bytearray (mutable version of bytes)
mv = memoryview(b)          # memoryview (zero-copy view of bytes)
```

---

#### 🔹 `bytes`

* Immutable (cannot be changed after creation)
* Often used for reading/writing binary files or network data

```python
b = b"data"
print(b[0])     # 100  (byte value for 'd')
```

---

#### 🔹 `bytearray`

* Mutable version of `bytes` — you can modify its contents

```python
ba = bytearray(b"abc")
ba[0] = 65
print(ba)       # bytearray(b'Abc')
```

---

#### 🔹 `memoryview`

* Provides a **view** of binary data **without copying it**
* Efficient for slicing or working with large data buffers

```python
mv = memoryview(b"abcdef")
print(mv[2:4].tobytes())   # b'cd'
```

---

#### ✅ Summary

| Type         | Mutable | Purpose                                  |
| ------------ | ------- | ---------------------------------------- |
| `bytes`      | ❌ No    | Fixed binary data (files, I/O)           |
| `bytearray`  | ✅ Yes   | Modify binary data in place              |
| `memoryview` | N/A     | Efficient, zero-copy view for large data |

---

### 📆 Datetime 
* The datetime module supplies classes for manipulating dates and times.
```python
from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)
```

---

### 🔢 Operators in Python

Operators perform actions on values (operands).
They fall into several key categories:

---

#### 🔹 Arithmetic Operators

```python
+, -, *, /, //, %, **
```

| Operator | Meaning             | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `3 + 2`  | `5`    |
| `-`      | Subtraction         | `5 - 1`  | `4`    |
| `*`      | Multiplication      | `2 * 3`  | `6`    |
| `/`      | Division (float)    | `5 / 2`  | `2.5`  |
| `//`     | Floor division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

---

#### 🔹 Comparison Operators

Return a **Boolean** (`True` / `False`).

```python
==, !=, >, <, >=, <=
```

Example:

```python
x, y = 5, 10
x < y   # True
x == y  # False
```

---

#### 🔹 Logical Operators

Combine Boolean expressions.

```python
and, or, not
```

Example:

```python
x = 5
print(x > 0 and x < 10)  # True
```

---

#### 🔹 Assignment Operators

```python
=, +=, -=, *=, /=, //=, %=, **=
```

Example:

```python
x = 5
x += 2   # same as x = x + 2 → 7
```

---

#### 🔹 Membership & Identity

| Type           | Operators      | Example        | Result              |
| -------------- | -------------- | -------------- | ------------------- |
| **Membership** | `in`, `not in` | `'a' in 'cat'` | `True`              |
| **Identity**   | `is`, `is not` | `x is y`       | True if same object |

---

#### 🔹 Bitwise Operators (for integers)

Operate on binary representations.

```python
&, |, ^, ~, <<, >>
```

Example:

```python
a, b = 5, 3  # (101, 011)
a & b  # 1 (bitwise AND)
a | b  # 7 (bitwise OR)
```

---

✅ **Summary**

| Category   | Examples          | Returns       |     |
| ---------- | ----------------- | ------------- | --- |
| Arithmetic | `+ - * / % ** //` | Numbers       |     |
| Comparison | `== != > < >= <=` | Bool          |     |
| Logical    | `and or not`      | Bool          |     |
| Assignment | `+= -= *=`        | Updated value |     |
| Membership | `in`, `not in`    | Bool          |     |
| Identity   | `is`, `is not`    | Bool          |     |
| Bitwise    | `&                | ^ ~ << >>`    | Int |

---

### 🔄 Flow Control Statements

#### 🧠 Overview

**Flow control** lets your program make decisions and repeat actions.
Python provides three main types:

1. **Conditional statements** (`if`, `elif`, `else`)
2. **Loops** (`for`, `while`)
3. **Loop control keywords** (`break`, `continue`, `pass`)

---

#### 🔹 1. **If / Elif / Else**

Used for **decision making** — only one block runs based on a condition.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)  # Output: B
```

✅ Conditions use comparison operators (`>`, `<`, `>=`, `==`, `!=`)
✅ You can nest or chain conditions as needed

---

#### 🔹 2. **While Loop**

Repeats a block **while** a condition is true.

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

✅ Use when you don’t know how many times to loop
⚠️ Make sure the loop condition eventually becomes false (avoid infinite loops)

---

#### 🔹 3. **For Loop**

Iterates over any **iterable** (list, string, range, etc.).

```python
for item in ["a", "b", "c"]:
    print(item)

for i in range(3):
    print(i)  # 0, 1, 2
```

✅ Use `range(start, stop, step)` for numeric loops
✅ Works automatically with lists, tuples, sets, strings, and more

---

#### 🔹 4. **Loop Control Keywords**

| Keyword      | Description                     | Example                   |
| ------------ | ------------------------------- | ------------------------- |
| **break**    | Stop the loop entirely          | `if x == 5: break`        |
| **continue** | Skip the rest of this iteration | `if x % 2 == 0: continue` |
| **pass**     | Placeholder (does nothing)      | Used for empty blocks     |

Example:

```python
for x in range(5):
    if x == 2:
        continue
    if x == 4:
        break
    print(x)
# Output: 0, 1, 3
```

---

#### ✅ Summary

| Concept            | Purpose                     | Example              |
| ------------------ | --------------------------- | -------------------- |
| `if / elif / else` | Conditional branching       | `if x > 0:`          |
| `while`            | Loop while condition true   | `while n > 0:`       |
| `for`              | Loop over iterable          | `for i in range(5):` |
| `break`            | Exit loop early             | `break`              |
| `continue`         | Skip to next iteration      | `continue`           |
| `pass`             | Placeholder for future code | `pass`               |

---

### ⚙️ Functions in Python

#### 🧠 What Is a Function?

A **function** is a reusable block of code that performs a specific task.
It helps make code **modular**, **organized**, and **easier to maintain**.

---

#### 🔹 1. **Defining a Function**

```python
def clean(name: str) -> str:
    """Remove spaces and capitalize each word."""
    return name.strip().title()
```

✅ `def` starts the function definition
✅ Parameters are listed in parentheses
✅ The `return` statement sends a value back
✅ Type hints (`: str -> str`) are optional but good practice

```python
print(clean("  john doe  "))  # Output: "John Doe"
```

---

#### 🔹 2. **Function Parameters**

Functions can take:

* **Positional arguments**
* **Default arguments**
* **Keyword arguments**
* **Variable-length arguments** (`*args`, `**kwargs`)

Example:

```python
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()           # Hello, friend!
greet("Alice")    # Hello, Alice!
```

---

#### 🔹 3. **Lambda Functions (Anonymous)**

A **lambda** is a small, one-line function used for short operations.

```python
title = lambda s: s.strip().title()
print(title("  python programming "))  # Output: "Python Programming"
```

✅ No name (anonymous)
✅ Can only contain one expression
✅ Often used with `map()`, `filter()`, or `sorted()`

Example with `map()`:

```python
names = ["alice", " bob ", "CHARLIE"]
cleaned = list(map(lambda n: n.strip().title(), names))
print(cleaned)  # ['Alice', 'Bob', 'Charlie']
```

---

#### 🔹 4. **Return Values**

Functions can return **any object**, or multiple values as a **tuple**.

```python
def divide(a, b):
    q = a // b
    r = a % b
    return q, r

quotient, remainder = divide(10, 3)
print(quotient, remainder)  # 3 1
```

---

#### ✅ Summary

| Concept           | Example           | Description                 |
| ----------------- | ----------------- | --------------------------- |
| Define a function | `def greet():`    | Create a reusable block     |
| Call a function   | `greet()`         | Execute it                  |
| Parameters        | `(name, age)`     | Input values                |
| Return            | `return result`   | Output from function        |
| Lambda            | `lambda x: x + 1` | One-line anonymous function |

---

### 📦 Arrays in Python

#### 🧠 Overview

Python doesn’t have a built-in “array” type like C or Java — instead, it provides **lists** and optional **array modules** for specialized use.

---

#### 🔹 1. **Lists = Dynamic Arrays**

Use **lists** for most cases — they’re flexible and can hold **mixed types**.

```python
nums = [10, 20, 30]
nums.append(40)
print(nums[1])     # 20
print(len(nums))   # 4
```

✅ Supports slicing, appending, removing, iteration, etc.
⚠️ Slightly more memory overhead because each element can be any object.

---

#### 🔹 2. **Typed Arrays (`array` module)**

For **large numeric data**, use the built-in `array` module for compact storage.

```python
from array import array

nums = array('i', [10, 20, 30])  # 'i' = integer
nums.append(40)
print(nums)  # array('i', [10, 20, 30, 40])
```

✅ Faster and memory-efficient for numeric data
⚠️ All elements must be of the **same type**

---

#### 🔹 3. **NumPy Arrays**

For scientific or vectorized math, use **NumPy**:

```python
import numpy as np
a = np.array([10, 20, 30])
print(a * 2)  # [20 40 60]
```

✅ Powerful operations, broadcasting, linear algebra
⚙️ Requires installing the `numpy` package

---

#### ✅ Summary

| Type              | Description                           | Use Case               |
| ----------------- | ------------------------------------- | ---------------------- |
| **list**          | General-purpose, dynamic, mixed types | Everyday Python work   |
| **array.array**   | Fixed-type, memory-efficient          | Numeric storage        |
| **numpy.ndarray** | High-performance numeric arrays       | Data science, ML, math |

---

### 🔁 Iterators in Python

#### 🧠 What is an Iterator?

An **iterator** is an object that allows you to **loop through a sequence** (like a list, tuple, or string) **one item at a time**.

* Technically, an object is an **iterator** if it implements two special methods:

  * `__iter__()` → returns the iterator object itself
  * `__next__()` → returns the next value in the sequence

When there are **no more items**, `__next__()` raises a `StopIteration` exception — this is how Python knows a loop should stop.

---

#### 🧩 Built-in Example

```python
it = iter([10, 20, 30])  # create an iterator from a list

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it)      # would raise StopIteration
```

Explanation:

* `iter()` creates an iterator object from an iterable (like a list).
* `next()` retrieves items one by one.

---

#### 🔁 Using Iterators in Loops

When you use a `for` loop, Python automatically:

1. Calls `iter()` on the object.
2. Calls `next()` repeatedly until `StopIteration` is raised.

Example:

```python
it = iter([10, 20, 30])
for x in it:
    print(x)  # Output: 10, 20, 30
```

---

#### ⚙️ Iterables vs Iterators

| Term         | Description                                                            | Example              |
| ------------ | ---------------------------------------------------------------------- | -------------------- |
| **Iterable** | Any object you can loop over (list, tuple, string, dict, set)          | `for x in [1,2,3]`   |
| **Iterator** | The object returned by `iter()`, which produces elements one at a time | `it = iter([1,2,3])` |

➡️ All **iterators** are **iterables**, but not all **iterables** are **iterators**.

---

#### 💡 Common Built-ins that Return Iterators

* `iter()`
* `map()`
* `filter()`
* `zip()`
* `enumerate()`
* Generators (`yield`)

Example:

```python
nums = [1, 2, 3]
squares = map(lambda x: x**2, nums)
print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9
```

---

#### ✅ Summary

| Concept         | Function                                            | Description |
| --------------- | --------------------------------------------------- | ----------- |
| `iter(obj)`     | Get an iterator from an iterable                    |             |
| `next(it)`      | Get next item, raises `StopIteration` when done     |             |
| `__iter__()`    | Returns iterator object (usually `self`)            |             |
| `__next__()`    | Returns next value each time                        |             |
| `StopIteration` | Signals end of iteration                            |             |
| `for` loop      | Automatically uses `iter()` and `next()` internally |             |

---

## 🧱 Object-Oriented Programming (OOP) in Python

### 🧠 What Is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into **objects** — reusable pieces that contain both **data** (attributes) and **behavior** (methods).

Instead of writing procedural code with functions and variables floating everywhere, OOP helps you model *real-world things* using **classes**.

---

### 👤 Classes and Objects

A **class** is a blueprint for creating objects.
An **object** is a specific instance of a class.

#### Example:

```python
class Person:
    def __init__(self, id: int, name: str):
        self.id = id          # instance variable
        self.name = name      # instance variable

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"
```

#### Explanation

* `class Person:` defines a new type (a “blueprint”).
* `__init__` is the **constructor** — it runs automatically when you create a new `Person`.
* `self` represents the **current object**.
* `self.id` and `self.name` are **instance variables** (unique per object).
* `greet()` is a **method** (a function that belongs to the class).

#### Example usage:

```python
p1 = Person(1, "Alice")
p2 = Person(2, "Bob")

print(p1.greet())  # Output: Hi, I'm Alice
print(p2.greet())  # Output: Hi, I'm Bob
```

---

### 🧩 Understanding `self`

In Python, every instance method must include `self` as its first parameter.
It refers to the *object itself*.

Example:

```python
p1 = Person(1, "Alice")
print(p1.name)        # accessing instance variable directly
print(p1.greet())     # calling a method that uses self.name
```

---

### 🔐 Encapsulation

Encapsulation means **keeping data safe** inside the object, only exposing what’s necessary.

In Python, we can simulate private variables by prefixing them with an underscore `_` or double underscore `__`.

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # "private" attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

```python
acct = BankAccount("Alice", 1000)
acct.deposit(500)
print(acct.get_balance())  # ✅ 1500
print(acct.__balance)      # ❌ AttributeError (not accessible directly)
```

---

### 🧬 Inheritance

**Inheritance** allows one class to inherit attributes and methods from another.
This promotes **code reuse** and **hierarchies** of related types.

### Example:

```python
class Employee(Person):  # Employee inherits from Person
    def __init__(self, id: int, name: str, role: str):
        super().__init__(id, name)  # call Person's constructor
        self.role = role

    def greet(self) -> str:  # method overriding
        return f"{super().greet()} and I work as {self.role}"
```

#### Explanation:

* `Employee` is a **subclass** (child).
* `Person` is the **superclass** (parent).
* `super().__init__(...)` calls the parent’s constructor.
* We **override** `greet()` to extend its behavior.

#### Example usage:

```python
e1 = Employee(101, "John", "Engineer")
print(e1.greet())  # Output: Hi, I'm John and I work as Engineer
```

---

### 🧱 Polymorthism: Method Overriding

Overriding happens when a **child class** defines a method with the **same name** as one in the **parent class**.

This lets the child **customize or extend** the parent’s behavior.

```python
class Parent:
    def speak(self):
        return "Hello from Parent!"

class Child(Parent):
    def speak(self):
        return "Hello from Child!"

obj = Child()
print(obj.speak())  # Output: Hello from Child!
```

---

### 🧬 Polymorphism

**Polymorphism** means “many forms.”
It allows different classes to respond to the same method name in their own way.

Example:

```python
people = [Person(1, "Alice"), Employee(2, "Bob", "Designer")]

for p in people:
    print(p.greet())
```

Output:

```
Hi, I'm Alice
Hi, I'm Bob and I work as Designer
```

Even though `p.greet()` is called on both, the correct version (from each class) runs — that’s polymorphism.

---

Here’s a compact but complete summary of **abstraction in Python** — ideal for your OOP week notes:

---

### 🧠 Abstraction 

**Abstraction** = hiding *implementation details* and exposing *only what’s necessary*.
It helps simplify complex systems by focusing on **what** an object does, not **how** it does it.

---

#### 🔹 Example Concept

```python
class Car:
    def start(self):
        self._ignite_engine()
        print("Car started")

    def _ignite_engine(self):   # internal (abstracted)
        print("Igniting engine...")
```

✅ The user calls `start()`, not caring how `_ignite_engine()` works.

---

#### 🔹 Abstract Base Classes aka ABCs (advanced, probably not in QC, but important for large codebases)

Use the **`abc`** module to define abstract methods that **must** be implemented by subclasses.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r**2
```

✅ Can’t instantiate `Shape()` directly
✅ Forces subclasses to implement `area()`

---

#### 🔹 Why it matters

* Defines **interfaces** for families of classes.
* Enforces **structure** in large codebases.
* Supports **polymorphism** cleanly.

---

#### ✅ Summary

| Concept                   | Purpose                       | Example                          |
| ------------------------- | ----------------------------- | -------------------------------- |
| **Abstraction**           | Hide details, show essentials | `car.start()` hides engine logic |
| **ABC / @abstractmethod** | Define required methods       | `Shape.area()`                   |
| **Implementation**        | Done by subclasses            | `Circle.area()`                  |


### 🧰 Additional OOP Features in Python

| Concept                | Description                                                                    | Example                     |
| ---------------------- | ------------------------------------------------------------------------------ | --------------------------- |
| **Class Variables**    | Shared across all instances                                                    | `Company.name = "TechCorp"` |
| **Instance Variables** | Unique to each object                                                          | `self.name = "Alice"`       |
| **Static Methods**     | Methods that don’t access `self`; utility functions                            | `@staticmethod`             |
| **Class Methods**      | Operate on the class itself, not an instance                                   | `@classmethod`              |
| **Dunder Methods**     | Special methods that start/end with `__` (like `__str__`, `__len__`, `__eq__`) | `def __str__(self):`        |

Example of a static and class method:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is {cls.__name__} class"
```

---

### 🧩 Real-World Analogy

| Concept          | Example                                             |
| ---------------- | --------------------------------------------------- |
| **Class**        | Blueprint for a car                                 |
| **Object**       | A specific car (VIN #123)                         |
| **Attributes**   | Color, model, year                                  |
| **Methods**      | start(), accelerate(), brake()                      |
| **Inheritance**  | ElectricCar inherits from Car                       |
| **Polymorphism** | Different cars implement `accelerate()` differently |
| **Abstraction**  | We dont know how the engine, brakes, etc works      |
| **Encapsulation**| You must press a button inside the car to access whats under the hood      |

---

### ✅ Summary

| Concept       | Key Idea                         | Python Example             |
| ------------- | -------------------------------- | -------------------------- |
| Class         | Blueprint for creating objects   | `class Person:`            |
| Object        | Instance of a class              | `p = Person(1, "Alice")`   |
| Constructor   | Initializes new objects          | `def __init__(self):`      |
| Encapsulation | Restrict access to internal data | `self.__balance`           |
| Inheritance   | Reuse code from parent class     | `class Employee(Person)`   |
| Polymorphism  | Same method, different behavior  | `p.greet()` vs `e.greet()` |
| Overriding    | Redefine parent method in child  | `def greet()` in Employee  |
| super()       | Call parent’s method             | `super().greet()`          |

---

## 🧩 Practice Exercise

Try creating a small hierarchy:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

vehicles = [Car("Ford"), Boat("Yamaha")]

for v in vehicles:
    print(f"{v.brand}: {v.move()}")
```

Output:

```
Ford: Driving 🚗
Yamaha: Sailing ⛵
```

---

## Extra - Lab Starters

### basics_cli.py

```python
name = input("Name: ").strip()
age = int(input("Age: ").strip())
print(f"Hello {name}! Next year you'll be {age + 1}.")
```

### datatypes_playground.py

```python
s = "data foundations"
assert s[:4] == "data"
nums = [3,1,4]; nums.append(1); assert 1 in nums
coords = (40.7, -74.0)
flags = {"etl", "sql", "python"}
cfg = {"retries": 3, "timeout": 5.0}
b = b"abc"; ba = bytearray(b); ba[0] = 65  # 'A'
r = range(3); assert list(r) == [0,1,2]
```

### flow_funcs.py

```python
from array import array

def grade(score: int) -> str:
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C" return "D"

title = lambda s: s.strip().title() # Example lambda.

scores = array("i", [95, 82, 73, 60]) # Typed int array. "i" for integers.

for score in scores:
    print(score, grade(score))

name = "   pablo de la cruz   "
print(title(name))
```

### oop_basics.py

```python
class Person:
    def __init__(self, pid: int, name: str):
        # Encapsulation: internal data is stored inside the object
        # In Python, _variable means "internal/private by convention"
        self._pid = pid
        self._name = name

    # Abstraction: outside code can call greet() without knowing how the greeting is built internally
    def greet(self) -> str:
        return f"Hi, I'm {self._name}"

# Inheritance: Employee reuses and extends Person
class Employee(Person):
    def __init__(self, pid: int, name: str, role: str):
        super().__init__(pid, name)
        self._role = role

    # Polymorphism: Employee has its own version of greet()
    def greet(self) -> str:
        return f"{super().greet()} and I work as {self._role}"

emps = [
    Employee(1, "Ada", "Engineer"),
    Employee(2, "Alan", "Researcher")
]

for e in emps:
    # Abstraction
    print(e.greet())
```

---

## Stretch Labs (optional)

* **Build a Python CLI Profile App**
  Ask the user for name, age, city, and goal, then print a formatted profile. Practice `input()`, casting, f-strings, and basic validation.

* **Create a Grade Analyzer**
  Store student scores, calculate letter grades, average, highest/lowest score, and pass count. Practice lists, dictionaries, loops, functions, and conditionals.

* **Practice a Git Workflow**
  Create a branch, add a Python file, commit with Conventional Commits, push to GitHub, open a PR, and merge it. Bonus: resolve a merge conflict with a partner.

* **Build a Simple To-Do List**
  Create a terminal app that can add, view, complete, and remove tasks. Practice `while` loops, lists, dictionaries, and functions.

* **Create a Data Types Playground**
  Write examples for `str`, `int`, `float`, `bool`, `None`, `list`, `tuple`, `set`, `dict`, `bytes`, `bytearray`, and `range`. Print each value and its `type()`.

* **Build an Employee Directory with OOP**
  Create `Person`, `Employee`, and `Manager` classes. Use constructors, inheritance, method overriding, and polymorphism.

* **Create a Bank Account Class**
  Add private-style balance data, `deposit()`, `withdraw()`, and `get_balance()`. Prevent negative deposits and overdrafts. Practice encapsulation and validation.

* **Practice Iterators and Built-ins**
  Demonstrate `iter()`, `next()`, `map()`, `filter()`, `enumerate()`, and `zip()` with small examples. Bonus: create a custom iterator.

* **Write Mini Agile Artifacts**
  Choose one Python app and write 3 user stories. Practice Agile planning and writing clear requirements.

* **Refactor a Script into Functions**
  Take a basic script and split it into reusable functions with type hints and docstrings. Practice modular code and cleaner design.