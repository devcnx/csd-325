"""
The data access layer of the application.

This module is responsible for the communication with the JokeAPI.

Imports:
    - dataclass: Used to create dataclasses.
    - Optional: Used to type hint optional parameters.
    - TypedDict: Used to define a dictionary of jokes.
    - cast: Used to cast the response to a dictionary.
    - requests: Used to make HTTP requests.
    - BASE_URL: The base URL of the JokeAPI.
    - MAX_JOKES: The maximum number of jokes to retrieve.
"""

from dataclasses import dataclass
from typing import Optional, TypedDict, cast
import requests
from module_9.constants import BASE_URL, MAX_JOKES


class JokeDict(TypedDict):
    """A dictionary representing a single joke from the API."""

    error: bool
    category: str
    type: str
    joke: Optional[str]
    setup: Optional[str]
    delivery: Optional[str]
    flags: dict[str, bool]
    id: int
    safe: bool
    lang: str


class JokeListResponse(TypedDict):
    """A dictionary representing the response for multiple jokes."""

    error: bool
    amount: int
    jokes: list[JokeDict]


class JokeAPI:
    """
    The client for interacting with the JokeAPI.

    Fields:
        - session: The session used to make HTTP requests.
        :type session: requests.Session
    """

    session: requests.Session

    def __init__(self) -> None:
        """Initialize the client."""
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def get_jokes(
        self, category: str, joke_type: str, amount: int = MAX_JOKES
    ) -> Optional[list[JokeDict]]:
        """
        Get jokes from the JokeAPI.

        Parameters:
            - category: The category of the joke.
            :type category: str

            - joke_type: The type of joke.
            :type joke_type: str

            - amount: The number of jokes to retrieve.
            :type amount: int

        Returns:
            - A list of jokes if successful, None otherwise.
            :rtype: Optional[list[JokeDict]]
        """
        params = {"type": joke_type, "amount": amount}
        url = f"{BASE_URL}{category}"

        try:
            return self._extracted_from_get_jokes_25(url, params, amount)
        except requests.RequestException as error:
            print(f"Network Error: Could Not Fetch Joke Data:\n{error}")
            return None

    def _extracted_from_get_jokes_25(
        self, url: str, params: dict[str, str], amount: int
    ) -> Optional[list[JokeDict]]:
        """
        Make a GET request to the JokeAPI and return the response.

        Parameters:
            - url: The URL to make the request to.
            :type url: str

            - params: The parameters to pass to the request.
            :type params: dict[str, str]

            - amount: The number of jokes to retrieve.
            :type amount: int

        Returns:
            - A list of jokes if successful, None otherwise.
            :rtype: Optional[list[JokeDict]]
        """
        response = self.session.get(url, params=params, timeout=15)
        response.raise_for_status()
        if amount > 1:
            data = cast(JokeListResponse, response.json())
            if data["error"]:
                print("API Error: Could not fetch jokes.")
                return None
            return data["jokes"]

        data = cast(JokeDict, response.json())
        if data["error"]:
            print("API Error: Could not fetch joke.")
            return None
        return [data]
