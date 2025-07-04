"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 8.2 JSON Practice
Purpose: Provide the Student class that will be used in the main module.
"""

from dataclasses import dataclass
from typing import override


@dataclass
class Student:
    """
    Representation of a Student.

    The Student class represents a student with a student ID, first name,
    last name, and their email.

    Fields:
        - _student_id_number: The student's ID.
        :type _student_id_number: int

        - first_name: The student's first name.
        :type first_name: str

        - last_name: The student's last name.
        :type last_name: str

        - email_address: The student's email address.
        :type email_address: str
    """

    _student_id_number: int
    first_name: str
    last_name: str
    email_address: str

    def __init__(
        self, first_name: str, last_name: str, student_id: int, email: str
    ) -> None:
        """
        Initialize a new Student object.

        The student ID is already established, it's not passed as a parameter.
        Because this module would technically be in the "business" layer of an
        application, it doesn't contain any methods to validate the input.

        The student ID is a private field so it can't be accessed directly. It
        is initialized in the constructor and is used to identify the student.

        Parameters:
            - first_name: The student's first name.
            :type first_name: str

            - last_name: The student's last name.
            :type last_name: str

            - student_id_number: The student ID.
            :type student_id_number: int

            - email_address: The student's email address.
            :type email_address: str
        """
        self.student_id_number = student_id or 0
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email

    @property
    def student_id_number(self) -> int:
        """
        Get the student ID.

        This property is used to get the student ID.

        Returns:
            - The student ID.
            :rtype: int
        """
        return self._student_id_number

    @student_id_number.setter
    def student_id_number(self, student_id: int) -> None:
        """
        Set the student ID.

        This property is used to set the student ID.

        Parameters:
            - student_id_number: The student ID.
            :type student_id_number: int
        """
        self.student_id_number = student_id or 0

    @override
    def __str__(self) -> str:
        """
        Return a string representation of the Student object.

        The string representation is in the format:
            Last Name, First Name : ID = #, Email = email

        The dunder method uses the `@override` decorator to indicate that it
        overrides the `__str__` method of the `object` class.

        Returns:
            - A string representation of the Student object.
            :rtype: str
        """
        return (
            f"{self.last_name}, {self.first_name} : "
            f"ID = {self.student_id_number}, "
            f"Email = {self.email_address}"
        )
