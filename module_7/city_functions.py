"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 7.2 Test Cases
Purpose: Provides the city_country function that will be used in the test cases.
"""

import random
from module_7.constants import CITY_COUNTRIES


def city_country_str(city: str, country: str) -> str:
    """
    Displays a string in the format City, Country.

    This function takes a city and a country as input and returns a string in the format
    City, Country.

    The function uses the title() method to capitalize the first letter of each word in
    the city and country names.

    Parameters:
        - city: The name of the city.
        :type city: str

        - country: The name of the country.
        :type country: str

    Returns:
        - A string in the format City, Country.
        :rtype: str
    """
    return f"{city.title()}, {country.title()}"


if __name__ == "__main__":
    num_samples = 1
    city_and_country = random.choices(CITY_COUNTRIES, weights=None, k=num_samples)
    print(city_country_str(city_and_country[0]["city"], city_and_country[0]["country"]))
