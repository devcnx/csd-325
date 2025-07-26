"""
Name: Brittaney Perry-Morgan
Date: Sunday, July 6th, 2025
Assignment: Module 9.2 API

Purpose: Complete the API tutorial (https://www.dataquest.io/blog/api-in-python/)

Imports:
    - json: Used to format JSON responses.
    - List: Used to define a list of astronauts.
    - TypedDict: Used to define a dictionary of astronauts.
    - requests: Used to make HTTP requests.
"""

import json
from typing import List, TypedDict

import requests


class AstronautInfo(TypedDict):
    """
    Defines the structure for the 'people' part of the API response.

    Fields:
        - name: The name of the astronaut.
        :type name: str

        - craft: The name of the spacecraft the astronaut is in.
        :type craft: str
    """

    name: str
    craft: str


class AstronautsData(TypedDict):
    """
    Defines the overall structure of the astronauts API response.

    Fields:
        - number: The number of astronauts in space.
        :type number: int

        - people: A list of astronauts in space.
        :type people: List[AstronautInfo]
    """

    number: int
    people: List[AstronautInfo]


def test_open_notify_astronauts_invalid() -> int:
    """
    Test the OpenNotify astronauts API with an invalid endpoint.

    Returns:
        - HTTP status code from the invalid endpoint request.
        :rtype: int

    Raises:
        - requests.exceptions.RequestException: If the request fails completely.
    """
    url = "http://api.open-notify.org/this-api-doesnt-exist"
    try:
        response = requests.get(url, timeout=30)
        return response.status_code
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        raise


def test_open_notify_astronauts() -> None:
    """
    Test the OpenNotify astronauts API endpoint and display astronaut information.

    Makes a GET request to the astronauts API, parses the JSON response,
    and prints detailed information about people currently in space.

    Raises:
        - requests.exceptions.RequestException: If the API request fails.
    """
    url = "http://api.open-notify.org/astros"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raises HTTPError if the request returns unsuccessfully.
        # Cast the JSON response to our defined TypedDict for type safety
        json_data: AstronautsData = response.json()  # Parse JSON once and reuse

        print("\nConnection Successful")
        print(f"\nResponse Status Code: {response.status_code}")
        print(f"\nResponse Headers: {response.headers}")
        print("\nRaw JSON Response:")
        print(f"{response.text}")
        print("\nFormatted JSON Response:")
        print(f"{format_json_response(json_data)}")
        print(f"\nNumber of People in Space: {json_data['number']}")
        print("\nPeople in Space:")
        for person in json_data["people"]:
            print(f"{person['name']} is on the {person['craft']}")

    except requests.exceptions.RequestException as error:
        print(f"\nError Connecting:\n{error}")


def format_json_response(json_obj: AstronautsData) -> str:
    """
    Format a JSON object (aka the API response).

    Parameters:
        - json_obj: The API response in JSON format.
        :type json_obj: AstronautsData

    Returns:
        - A string representation of the JSON response.
        :rtype: str
    """
    return json.dumps(json_obj, indent=4)


if __name__ == "__main__":
    print(
        f"\nThis is an invalid endpoint\nStatus Code: {test_open_notify_astronauts_invalid()}\n"
    )
    test_open_notify_astronauts()
