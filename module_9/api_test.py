"""
Name: Brittaney Perry-Morgan
Date: Sunday, July 6th, 2025
Assignment: Module 9.2 API

Purpose: Complete the API tutorial (https://www.dataquest.io/blog/api-in-python/)

Imports:
    - json: Used to format JSON responses.
    - requests: Used to make HTTP requests.
"""

import json
import requests


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
        json_data = response.json()  # Parse JSON once and reuse

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


def format_json_response(json_obj: dict) -> str:
    """
    Format a JSON object (aka the API response).

    Parameters:
        - json_obj: The API response in JSON format.
        :type json_obj: dict

    Returns:
        - A string representation of the JSON response.
        :rtype: str
    """
    return json.dumps(json_obj, indent=4)


if __name__ == "__main__":
    print(
        f"This is an invalid endpoint\nStatus Code: {test_open_notify_astronauts_invalid()}\n"
    )
    test_open_notify_astronauts()
