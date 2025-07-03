"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 7.2 Test Cases
Purpose: Provides the city_country function that will be used in the test cases.
"""

from module_7.constants import CITY_COUNTRIES


def city_country_str(city: str, country: str) -> str:
    """
    Displays a string in the format City, Country.

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
    for city_country in CITY_COUNTRIES:
        print(
            city_country_str(city=city_country["city"], country=city_country["country"])
        )
