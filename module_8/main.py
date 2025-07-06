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
import os
import re
from typing import Callable

ID_LENGTH = 5
MIN_ID = 10000
MAX_ID = 99999
MAX_POSSIBLE_IDS = MAX_ID - MIN_ID
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def load_students(filepath: str) -> list[dict[str, str | int]]:
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def is_existing_student(students: list[dict[str, str | int]], student_id: int) -> bool:
    return any(student["Student_ID"] == student_id for student in students)


def student_notification(user_msg: str = "") -> None:
    print(user_msg)


def display_students(students: list[dict[str, str | int]]) -> None:
    for student in students:
        print(
            f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, "
            f"Email = {student['Email']}"
        )


def add_student(
    students: list[dict[str, str | int]], new_student: dict[str, str | int]
) -> list[dict[str, str | int]]:
    students.append(new_student)
    return students


def save_students(filepath: str, students: list[dict[str, str | int]]) -> None:
    with open(filepath, encoding="utf-8", mode="w") as file:
        json.dump(students, file, indent=4)


def display_save_cancel_dialog() -> bool:
    print("\n" + "=" * 50)
    print("SAVE CHANGES DIALOG")
    print("=" * 50)
    while True:
        choice = (
            input("Do you want to save your changes to the student list? (y/n): ")
            .lower()
            .strip()
        )
        if choice in ["y", "yes"]:
            return True
        if choice in ["n", "no"]:
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def get_valid_input(
    prompt: str, validation_fn: Callable[[str], bool], err_msg: str
) -> str:
    while True:
        value = input(prompt).strip()
        if validation_fn(value):
            return value
        print(err_msg)


def get_student_from_user(existing_ids: set[int]) -> dict[str, str | int] | None:
    try:
        f_name = get_valid_input(
            "Enter student's first name: ",
            lambda x: x.isalpha(),
            "First name must be alphabetic.",
        )
        l_name = get_valid_input(
            "Enter student's last name: ",
            lambda x: x.isalpha(),
            "Last name must be alphabetic.",
        )
        student_id_str = get_valid_input(
            f"Enter student's ID ({ID_LENGTH} digits, unique, between {MIN_ID}-{MAX_ID}): ",
            lambda x, existing_ids=existing_ids: valid_id(existing_ids, x),
            f"Student ID must be a unique {ID_LENGTH}-digit number between {MIN_ID} and\
                {MAX_ID} not already in use.",
        )
        if not student_id_str:
            return None
        student_id = int(student_id_str)
        email = get_valid_input(
            "Enter student's email: ", valid_email, "Email must be valid."
        )
        return {
            "F_Name": f_name,
            "L_Name": l_name,
            "Student_ID": student_id,
            "Email": email,
        }
    except ValueError:
        return None


def valid_id(existing_ids: set[int], x: str) -> bool:
    try:
        student_id = int(x)
        return MIN_ID <= student_id <= MAX_ID and student_id not in existing_ids
    except ValueError:
        return False


def valid_email(x: str) -> bool:
    return re.match(EMAIL_REGEX, x) is not None


if __name__ == "__main__":
    FILEPATH = "module_8/data/student.json"
    orig_students_list = load_students(FILEPATH)
    current_students = [dict(student) for student in orig_students_list]

    student_notification(user_msg=f'\n{"-" * 5} Original Student List {"-" * 5}')
    display_students(current_students)

    print("\nAdd a new student to the list:")
    existing_ids_set = {int(s["Student_ID"]) for s in current_students}
    MAX_POSSIBLE_IDS = MAX_ID - MIN_ID + 1
    if len(existing_ids_set) >= MAX_POSSIBLE_IDS:
        student_notification(
            f"\nAll possible {ID_LENGTH}-digit IDs are in use. Cannot add more students."
        )
    else:
        new_student_data = get_student_from_user(existing_ids_set)
        if new_student_data is None:
            student_notification("\nInvalid input. No student added.")
            exit(1)

        if any(
            s["Student_ID"] == new_student_data["Student_ID"] for s in current_students
        ):
            student_notification(
                f"\nStudent with ID {new_student_data['Student_ID']} already exists. \
                    No student added."
            )
        else:
            add_student(current_students, new_student_data)
            student_notification(user_msg=f'\n{"-" * 5} Updated Student List {"-" * 5}')
            display_students(current_students)

            if current_students == orig_students_list:
                student_notification("No Changes Were Made to the File.")
            elif display_save_cancel_dialog():
                save_students(FILEPATH, current_students)
                student_notification("The student.json File Was Updated.")
            else:
                student_notification("Changes Were Not Saved.")
