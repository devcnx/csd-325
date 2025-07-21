"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 1st, 2025
Assignment: Module 8.2 JSON

Purpose: Holds the Student and StudentList dataclasses.

Imports:
    - dataclass: Used to create dataclasses.
    - field: Used to create default factory for the students list.
    - List: Used to type hint the students list.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    """
    Representation of a Student.

    Fields:
        - f_name: The first name of the student.
        :type f_name: str

        - l_name: The last name of the student.
        :type l_name: str

        - student_id: The student's unique ID.
        :type student_id: int

        - email: The student's email address.
        :type email: str
    """

    f_name: str
    l_name: str
    student_id: int
    email: str

    def __str__(self) -> str:
        """String representation of a student."""
        return f"{self.l_name}, {self.f_name} : ID = {self.student_id}, Email = {self.email}"


@dataclass
class StudentList:
    """
    Representation of a list of students.

    Fields:
        - students: The list of students.
        :type students: List[Student]
    """

    students: List[Student] = field(default_factory=list)

    def __iter__(self):
        """Iterator for the StudentList."""
        return iter(self.students)

    def print_students(self) -> None:
        """Print all students in the list."""
        for student in self.students:
            print(student)

    def add_student(self, student: Student) -> None:
        """
        Add a student to the list.

        Parameters:
            - student: The Student to add to the list.
            :type student: Student
        """
        self.students.append(student)

    def contains_student(self, student: "Student") -> bool:
        """
        Check for duplicate by student_id OR email.

        Parameters:
            - student: The student to check for duplicates.
            :type student: Student

        Returns:
            - True if the student is a duplicate, False otherwise.
            :rtype: bool
        """
        return any(
            s.student_id == student.student_id or s.email == student.email
            for s in self.students
        )

    def remove_duplicates(self) -> None:
        """
        Removes duplicate students by student_id or email, keeping the first occurrence.
        """
        seen_ids = set()
        seen_emails = set()
        unique_students = []
        for s in self.students:
            if s.student_id not in seen_ids and s.email not in seen_emails:
                unique_students.append(s)
                seen_ids.add(s.student_id)
                seen_emails.add(s.email)
        self.students = unique_students
