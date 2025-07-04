"""Tests for the module_7.city_functions module."""

import unittest
from module_7.city_functions import city_country_str
from module_7.constants import CITY_COUNTRIES


class TestCityCountry(unittest.TestCase):
    """
    Test class for city_country_str function.

    Fields:
        - None
    """

    def test_city_country(self) -> None:
        """Test that city_country_str returns the correct string, including formatting."""
        result = city_country_str(
            city=CITY_COUNTRIES[0]["city"],
            country=CITY_COUNTRIES[0]["country"],
            population=0,
        )
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main(verbosity=2)
