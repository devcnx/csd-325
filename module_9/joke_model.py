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

    Attributes:
        category: The category of the joke
        joke_type: The type of joke (single or twopart)
        joke_content: The complete joke text for single-type jokes
        setup: The setup line for two-part jokes
        delivery: The punchline for two-part jokes
        raw_json: The original JSON response from the API
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
        """
        if self.joke_type == "single":
            print(self.joke_content or "No joke content available")
        else:
            print(self.setup or "No setup available")
            print(self.delivery or "No delivery available")

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
