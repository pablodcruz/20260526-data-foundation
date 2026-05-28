# Lab: JSON Profile Manager

## Objectives

By completing this lab, students will be able to:

- Store Python dictionaries and lists in a JSON file
- Use `json.load()` and `json.dump()`
- Read and write files using `with open(...)`
- Handle missing files with `FileNotFoundError`
- Build a menu-driven console application

---

## Scenario

You are building a small profile manager for a class or team. The program should allow a user to add profiles, view saved profiles, search by name, and save the data to a JSON file.

The data should still be available after the program closes.

---

## Requirements

Create a Python file named:

```text
json_profile_manager.py
```

The app should use a JSON file named:

```text
profiles.json
```

Each profile should include:

- Name
- Age
- City
- Goal

Example profile:

```python
{
    "name": "Ada",
    "age": 28,
    "city": "New York",
    "goal": "Become a data engineer"
}
```

---

## Part 1: Load Profiles

Create a function named `load_profiles()` that:

- Opens `profiles.json`
- Loads the JSON data into Python
- Returns a list of profiles
- Returns an empty list if the file does not exist

Hint:

```python
try:
    with open("profiles.json", "r", encoding="utf-8") as file:
        return json.load(file)
except FileNotFoundError:
    return []
```

---

## Part 2: Save Profiles

Create a function named `save_profiles(profiles)` that:

- Opens `profiles.json` in write mode
- Saves the profile list as formatted JSON

Use:

```python
json.dump(profiles, file, indent=2)
```

---

## Part 3: Add a Profile

Create a function named `add_profile(profiles)` that:

- Asks the user for name, age, city, and goal
- Validates that age is a number
- Adds the new profile dictionary to the `profiles` list
- Prints a success message

Example:

```text
Name: Ada
Age: 28
City: New York
Goal: Become a data engineer
Profile added.
```

---

## Part 4: View Profiles

Create a function named `view_profiles(profiles)` that:

- Prints all saved profiles
- Shows a helpful message if no profiles exist

Example:

```text
1. Ada | Age: 28 | City: New York | Goal: Become a data engineer
2. Grace | Age: 31 | City: Chicago | Goal: Learn PostgreSQL
```

---

## Part 5: Search Profiles

Create a function named `search_profiles(profiles)` that:

- Asks the user for a name
- Searches the profile list
- Prints matching profiles
- Handles cases where no match is found

The search should be case-insensitive.

---

## Part 6: Main Menu

Create a `main()` function with this menu:

```text
===== JSON Profile Manager =====
1. Add Profile
2. View Profiles
3. Search Profiles
4. Save Profiles
5. Exit
```

The program should load existing profiles when it starts.

The program should ask the user whether to save before exiting if changes were made.

---

## Starter Code

```python
import json


FILE_NAME = "profiles.json"


def load_profiles():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_profiles(profiles):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(profiles, file, indent=2)


def add_profile(profiles):
    name = input("Name: ").strip()
    city = input("City: ").strip()
    goal = input("Goal: ").strip()

    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Age must be a whole number.")

    profile = {
        "name": name,
        "age": age,
        "city": city,
        "goal": goal
    }

    profiles.append(profile)
    print("Profile added.")


def view_profiles(profiles):
    # TODO: Display all profiles
    pass


def search_profiles(profiles):
    # TODO: Search profiles by name
    pass


def display_menu():
    print("\n===== JSON Profile Manager =====")
    print("1. Add Profile")
    print("2. View Profiles")
    print("3. Search Profiles")
    print("4. Save Profiles")
    print("5. Exit")


def main():
    profiles = load_profiles()
    changed = False

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_profile(profiles)
            changed = True
        elif choice == "2":
            view_profiles(profiles)
        elif choice == "3":
            search_profiles(profiles)
        elif choice == "4":
            save_profiles(profiles)
            changed = False
            print("Profiles saved.")
        elif choice == "5":
            if changed:
                answer = input("Save before exiting? (y/n): ").lower()
                if answer == "y":
                    save_profiles(profiles)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()
```

---

## Test Cases

### Add and Save a Profile

```text
Choose an option (1-5): 1
Name: Ada
City: New York
Goal: Become a data engineer
Age: 28
Profile added.
```

Then choose option `4` and verify that `profiles.json` was created.

### Invalid Age

```text
Age: twenty
Age must be a whole number.
Age: 20
```

### Search by Name

```text
Choose an option (1-5): 3
Search name: ada
Ada | Age: 28 | City: New York | Goal: Become a data engineer
```

### No Profiles

```text
No profiles found.
```

---

## Stretch Goals

- Add an option to delete a profile
- Add an option to update a profile
- Prevent duplicate names
- Sort profiles alphabetically
- Save automatically after every change
- Add a `created_at` field to each profile

---

## Reflection Questions

1. What Python data types are saved into the JSON file?
2. Why do we use `with open(...)` when working with files?
3. What happens if `profiles.json` does not exist?
4. Why is `indent=2` useful when saving JSON?
5. Why should user input be validated before saving it?
