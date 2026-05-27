"""
Student Grade Manager
A console application using only lists and dictionaries.
No imports allowed - pure Python fundamentals!
"""

def calculate_average(grades):
    """
    Calculate average of a list of grades.
    Returns 0 if list is empty.
    """
    # TODO: Implement this function
    pass

def add_student(students):
    """
    Add a new student to the dictionary.
    students format: {"Name": [grade1, grade2, ...]}
    """
    # TODO: Get name from user, add to dictionary with empty list
    pass

def view_students(students):
    """
    Display all students and their average grades.
    """
    # TODO: Loop through dictionary, print each student's average
    pass

def add_grade(students):
    """
    Add a grade to an existing student's grade list.
    Grade should be between 0-100.
    """
    # TODO: Find student, validate grade, append to their list
    pass

def class_average(students):
    """
    Calculate and display the average of ALL grades in the class.
    """
    # TODO: Loop through all students and all grades, calculate overall average
    pass

def top_student(students):
    """
    Find and display the student with the highest average grade.
    """
    # TODO: Calculate average for each student, find the maximum
    pass

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("     STUDENT GRADE MANAGER")
    print("="*40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Add Grade to Student")
    print("4. View Class Average")
    print("5. Find Top Student")
    print("6. Exit")
    print("="*40)

def main():
    """Main program loop"""
    # Dictionary to store students and their grades
    # Format: {"Student Name": [85, 92, 78]}
    students = {}
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        # TODO: Implement menu logic with if/elif/else
        # Call the appropriate function based on user input
        pass

# Program entry point