"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 8.2 JSON Practice

Purpose: Implementation of a student management system.

Imports:
    - json: Used to interact with the JSON file.
    - os: Used to get the current working directory.
    - sys: Used to add the project root to the Python path.
    - Path: Used to work with file paths.
    - messagebox: Used to display a message box.
    - tkinter: Used to create a GUI.
"""

import json
import os
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

# Add project root to the Python path to
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

# flake8: noqa: E402

from module_8.student import (  # pylint: disable=wrong-import-position
    Student,
    StudentList,
)

JSON_FILE_PATH = Path(__file__).parent / "data" / "student.json"


def load_students(file_path: Path) -> StudentList:
    """
    Loads students from JSON (PascalCase keys). Removes existing duplicates.

    Parameters:
        - file_path: The path to the JSON file.
        :type file_path: Path

    Returns:
        - A StudentList containing the loaded students.
        :rtype: StudentList
    """
    students_data = []
    if file_path.exists() and file_path.stat().st_size > 0:
        with open(file_path, encoding="utf-8", mode="r") as file:
            try:
                students_data = json.load(file)
            except json.JSONDecodeError:
                print(
                    f"Warning: JSON file at {file_path} is empty or malformed. \n"
                    f"Starting with an empty list."
                )
                students_data = []
    students = [
        Student(
            f_name=item["F_Name"],
            l_name=item["L_Name"],
            student_id=item["Student_ID"],
            email=item["Email"],
        )
        for item in students_data
        if all(k in item for k in ("F_Name", "L_Name", "Student_ID", "Email"))
    ]
    student_list = StudentList(students)  # pylint: disable=redefined-outer-name
    student_list.remove_duplicates()  # Remove any existing duplicates in the file!
    return student_list


# pylint: disable=redefined-outer-name
def save_students(file_path: Path, student_list: StudentList) -> None:
    """
    Save students to JSON with PascalCase keys.

    Parameters:
        - file_path: The path to the JSON file.
        :type file_path: Path

        - student_list: The StudentList to save.
        :type student_list: StudentList
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data_to_save = [
        {
            "F_Name": s.f_name,
            "L_Name": s.l_name,
            "Student_ID": s.student_id,
            "Email": s.email,
        }
        for s in student_list.students
    ]
    try:
        with open(file_path, encoding="utf-8", mode="w") as file:
            json.dump(data_to_save, file, indent=4)
    except (IOError, OSError) as e:
        print(f"Error saving students to {file_path}: {e}")
        raise


def student_notification(user_msg: str) -> str:
    """
    Returns the user message if it's not empty, otherwise returns a default message.

    Parameters:
        - user_msg: The user message to return.
        :type user_msg: str

    Returns:
        - The user message if it's not empty, otherwise returns a default message.
        :rtype: str
    """
    return user_msg or "Invalid input. Please try again..."


def get_relative_path(path: Path) -> str:
    """
    Returns a relative path string from the current working directory to the given path.

    Parameters:
        - path: The path to get the relative path for.
        :type path: Path

    Returns:
        - The relative path string.
        :rtype: str
    """
    try:
        return os.path.relpath(str(path), start=os.getcwd())
    except ValueError as e:
        print(f"Error getting relative path: {e}")
        return str(path)


def show_save_dialog(file_path: Path) -> bool:
    """
    Shows a dialog asking the user if they want to save the changes.

    Parameters:
        - file_path: The path to the file being modified.
        :type file_path: Path

    Returns:
        - True if the user clicks 'Yes', False otherwise.
        :rtype: bool
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    relative_path = get_relative_path(file_path)
    message = f"This file has been modified outside. Do you want to reload it?\n\n{relative_path}"
    return messagebox.askyesno("File Modified", message)


if __name__ == "__main__":
    JSON_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    student_list = load_students(JSON_FILE_PATH)
    print(student_notification(f"\n{'=' * 50}\nOriginal Student List:\n{'=' * 50}\n"))
    student_list.print_students()
    print("\n")

    new_student = Student(
        f_name="Brittaney",
        l_name="Perry-Morgan",
        student_id=12345,
        email="bperrymorgan@me.com",
    )

    if student_list.contains_student(new_student):
        print(
            student_notification(
                f"\n***** DUPLICATE STUDENT DETECTED: ({new_student}) will not be added.*****\n\n"
            )
        )
    else:
        student_list.add_student(new_student)
        print(
            student_notification(
                f"\n***** STUDENT ADDED: ({new_student}) has been added.*****\n\n"
            )
        )
        if show_save_dialog(JSON_FILE_PATH):
            save_students(JSON_FILE_PATH, student_list)
            print(student_notification("Changes saved."))
        else:
            print(student_notification("Changes not saved."))

    print(student_notification(f"\n{'=' * 50}\nUpdated Student List:\n{'=' * 50}\n"))
    student_list.print_students()
    print("\n")

    student_list = load_students(JSON_FILE_PATH)
    print(
        student_notification(
            f"\n{'=' * 50}\nUpdated Student List from JSON:\n{'=' * 50}\n"
        )
    )
    student_list.print_students()
    print("\n")
