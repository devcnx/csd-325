"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 8.2 JSON Practice
Purpose: Demonstrate ability to work with JavaScript Object Notation (JSON).

The purpose of this program is to use an existing JSON file to create a list
of students, add a new student to the list, and then write the updated list
back to the JSON file.
"""

import json
import sys
from module_8.student import Student


def load_students(json_path: str) -> list[Student]:
    """
    Load a list of students from a JSON file.

    The function takes a JSON file path as input and returns a list of student
    objects loaded from the JSON file.

    Parameters:
        - json_path: The path to the JSON file, including the filename.
        :type json_path: str

    Returns:
        - A list of student objects loaded from the JSON file.
        :rtype: list[Student]
    """
    try:
        with open(json_path, encoding="utf-8", mode="r") as file:
            students = json.load(file)
            return [Student(**student) for student in students]

    except FileNotFoundError as e:
        print(f"***** Unable to find the specified file: {e}")
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"***** Invalid JSON format in {json_path}: {e}")
        sys.exit(1)
