"""
Manage the user's interface and application logic.

Imports:
    - Joke: The Joke dataclass.
    - JokeAPI: The JokeAPI client.
    - CATEGORIES: The available categories for jokes.
    - JOKE_TYPES: The available joke types.
    - MAX_JOKES: The maximum number of jokes to return from the API call.
"""

from module_9.joke_model import Joke
import json
from module_9.api_client import JokeAPI, JokeDict
from module_9.constants import CATEGORIES, JOKE_TYPES


class JokeApp:
    """
    The main application class.

    Fields:
        - api_client: The JokeAPI client.
        :type api_client: JokeAPI
    """

    def __init__(self, api_client: JokeAPI) -> None:
        """
        Initialize the JokeApp.

        Parameters:
            - api_client: The JokeAPI client.
            :type api_client: JokeAPI
        """
        self.api_client = api_client

    def _get_validated_input(
        self, prompt: str, choices: list, default: str | None
    ) -> str:
        """
        A private, reusable utility to get a validated choice from the user.

        Parameters:
            - prompt: The prompt to display to the user.
            :type prompt: str

            - choices: Available choices for the user to choose from.
            :type choices: list

            - default: The default choice.
            :type default: str | None
        """
        print(f"\n{prompt} (Choices: {', '.join(choices)})")
        while True:
            user_input = input(f"Enter Choice: (Default: {default}): ").strip().lower()
            if not user_input:
                return default.lower() if default else ""
            if user_input in [choice.lower() for choice in choices]:
                return user_input
            print("Invalid Choice. Please Try Again.")

    def _map_to_jokes(self, jokes_data: list[JokeDict]) -> list[Joke]:
        """
        Map the raw API data to a list of Joke objects.

        Parameters:
            - jokes_data: The raw API data.
            :type jokes_data: list[JokeDict]

        Returns:
            - A list of Joke objects.
            :rtype: list[Joke]
        """
        return [
            Joke(
                category=joke["category"],
                joke_type=joke["type"],
                joke_content=joke.get("joke"),
                setup=joke.get("setup"),
                delivery=joke.get("delivery"),
                raw_json=json.dumps(joke),
            )
            for joke in jokes_data
        ]

    def _display_jokes(self, jokes: list[Joke]) -> None:
        """
        Display the jokes to the user.

        Parameters:
            - jokes: The jokes to display.
            :type jokes: list[Joke]
        """
        if not jokes:
            print("\nNo Jokes Found For The Selected Criteria.")
            return

        print("\n--- Here Are Your Jokes! ---")
        for index, joke in enumerate(jokes, 1):
            print(f"\nJoke #{index} (Category: {joke.category})")

            print("\n--- Raw JSON Response ---")
            joke.print_raw_json()

            print("\n--- Formatted JSON (using json.dumps) ---")
            joke.print_formatted_joke()
        print("\n---------------------------")

    def run(self) -> None:
        """
        Run the main application loop.

        Returns:
            - None
        """
        print("\n--- Welcome To The Joke Factory! ---")

        category = self._get_validated_input(
            prompt="Select a Category: ",
            choices=CATEGORIES,
            default="Programming",
        )
        joke_type = self._get_validated_input(
            prompt="Select a Joke Type: ", choices=JOKE_TYPES, default="single"
        )

        print(f"\nFetching {joke_type} Jokes In The {category} Category...")
        if jokes_data := self.api_client.get_jokes(category, joke_type, amount=5):
            jokes = self._map_to_jokes(jokes_data)
            self._display_jokes(jokes)
