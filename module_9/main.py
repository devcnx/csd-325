"""
Name: Brittaney Perry-Morgan
Date: Sunday, July 6th, 2025
Assignment: Module 9.2 API

Purpose: Demonstrate the ability to interact with a public API (https://sv443.net/jokeapi/v2/).

This is the main entry point for the application.
"""

from module_9.app import JokeApp
from module_9.api_client import JokeAPI


def main():
    """The main function of the application."""
    api_client = JokeAPI()
    app = JokeApp(api_client=api_client)
    app.run()


if __name__ == "__main__":
    main()
