"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 7.2 Test Cases
Purpose: Provides the city_country function that will be used in the test cases.
"""

import random
from module_7.constants import CITY_COUNTRIES, LANGUAGES, DEFAULT_LANGUAGE


def city_country_str(
    city: str, country: str, population: int = 0, language: str = ""
) -> str:
    """
    Displays a string in the format City, Country - Population # (if provided),
    Language.

    This function takes a city, a country, and a population as input and returns a
    string in the format City, Country - Population #. The population is optional and
    defaults to 0 if not provided.

    The function uses the title() method to capitalize the first letter of each word in
    the city and country names.

    Parameters:

        - city: The name of the city.
        :type city: str

        - country: The name of the country.
        :type country: str

        - population: The population of the city.
        :type population: int

        - language: The language of the city.
        :type language: str

    Returns:
        - A string in the format City, Country - Population #, Language.
        :rtype: str
    """
    if population > 0 and language:
        return f"{city.title()}, {country.title()} - Population {population:,}, {language.title()}"
    if language:
        return f"{city.title()}, {country.title()} - {language.title()}"
    if population > 0:
        return f"{city.title()}, {country.title()} - Population {population:,}"
    return f"{city.title()}, {country.title()}"


if __name__ == "__main__":
    city_and_country = random.choices(CITY_COUNTRIES, weights=None, k=1)
    is_language = random.choice([True, False])
    print(
        city_country_str(
            city=city_and_country[0]["city"],
            country=city_and_country[0]["country"],
            population=random.randint(0, 5),
        )
        if is_language
        else city_country_str(
            city=city_and_country[0]["city"],
            country=city_and_country[0]["country"],
            population=random.randint(0, 5),
            language=random.choice(LANGUAGES),
        )
    )
