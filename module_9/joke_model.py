"""
Representation of a joke.

This module holds the Joke dataclass that's used to represent a joke from the API. The dataclass
defines the data structure for a joke.

Imports:
    - json: Used to parse the JSON.
    - dataclasses: Used to create dataclasses.
    - asdict: Used to convert the dataclass to a dictionary.
    - Optional: Used to type hint optional parameters.
"""

import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Joke:
    """
    Representation of a single joke.

    Fields:
        - category: The category of the joke.
        :type category: str

        - joke_type: The type of joke.
        :type joke_type: str

        - joke_content: The joke. Default is None.
        :type joke_content: str

        - setup: The setup of the joke. Default is None.
        :type setup: str

        - delivery: The delivery of the joke. Default is None.
        :type delivery: str
    """

    category: str
    joke_type: str
    joke_content: Optional[str] = None
    setup: Optional[str] = None
    delivery: Optional[str] = None
    raw_json: Optional[str] = None

    def __str__(self) -> str:
        """
        Return a string representation of the joke.

        Returns:
            - A string representation of the joke.
            :rtype: str
        """
        return f"{self.category}: {self.joke_content}"

    def print_no_formatting(self) -> None:
        """
        Print the joke in its raw, unformatted form.

        Returns:
            - None
        """
        if self.joke_type == "single":
            print(self.joke_content)
        else:
            print(self.setup)
            print(self.delivery)

    def print_formatted_joke(self) -> None:
        """
        Print the joke in a formatted JSON style.

        Returns:
            - None
        """
        # Create a dictionary from the dataclass, excluding the raw_json field
        joke_dict = asdict(self)
        joke_dict.pop("raw_json", None)
        print(json.dumps(joke_dict, indent=4, sort_keys=True))

    def print_raw_json(self) -> None:
        """
        Print the raw JSON response for the joke.

        Returns:
            - None
        """
        print(self.raw_json)
