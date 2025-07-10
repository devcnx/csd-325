"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 8.2 JSON Practice
Purpose: Demonstrate ability to work with JavaScript Object Notation (JSON).

The purpose of this program is to use an existing JSON file to create a list
of students, add a new student to the list, and then write the updated list
back to the JSON file.

Imports:
    - json : Used to read and write JSON files.
    - os : Used to check the existence of a file.
    - re : Used to validate email addresses using regular expressions.
    - sys : Used to exit the program.
    - typing : Used to type hint functions.

Constants:
    - ID_LENGTH : The length of the student ID.
    - MIN_ID : The minimum possible student ID.
    - MAX_ID : The maximum possible student ID.
    - MAX_POSSIBLE_IDS : The maximum possible number of student IDs.
    - EMAIL_REGEX : The regular expression used to validate email addresses.
"""

# Imports
import json
import os
import re
import sys
from typing import Dict, Union

# Constants
ID_LENGTH = 5
MIN_ID = 10000
MAX_ID = 99999
MAX_POSSIBLE_IDS = MAX_ID - MIN_ID + 1
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Type alias for a student record
Student = Dict[str, Union[str, int]]


def load_student(file_path: str):
    print("Hello, World")


def load_students(file_path: str):
    print("Hello, World")


def is_existing_student():
    print("Hello, World")


def student_notification(user_msg: str):
    print(user_msg)


def add_student():
    print("Hello, World")


def display_students():
    print("Hello, World")
