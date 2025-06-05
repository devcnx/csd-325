"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 1st, 2025
Assignment: Module 2.2 Documented Debugging and Flowchart(s)

Purpose: Demonstrate proficiency in documented debugging and flowchart(s).

This program is used to "sing" the "Bottles of Beer on the Wall" song. It has been refactored
into smaller, well-defined functions for improved readability, maintainability, and for
demonstrating debugging techniques.

Referenced Debugging Guide: https://cse232-msu.github.io/CSE232/debugging_guide.html
"""


def get_valid_bottles_input(prompt: str) -> int:
    """
    Prompts the user for the number of bottles and validates the input.

    This ensure that the users centers a positive integer.

    Parameters:
        - prompt: The prompt to display to the user.
        :type prompt: str

    Returns:
        - A valid, positive integer.
        :rtype: int
    """
    while True:
        try:
            user_input = input(prompt)
            starting_bottles = int(user_input)
            if starting_bottles <= 0:
                print(
                    f"{" " * 2}*** Invalid input. Please enter a positive integer. ***"
                )
                continue
            break
        except ValueError:
            print(f"{" " * 2}*** Invalid input. Please enter a whole number. ***")
    return starting_bottles


def __get_verse_lyrics(current_bottles: int) -> str:
    """
    Returns the lyrics for a single verse of the song.

    Parameters:
        - current_bottles: The number of bottles in the current verse.
        :type current_bottles: int

    Returns:
        - The lyrics for the current verse.
        :rtype: str
    """
    if current_bottles > 1:
        return (
            f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer."
            + f"Take one down and pass it around, {current_bottles - 1} bottles of beer on the wall."
        )
    elif current_bottles == 1:
        return (
            "1 bottle of beer on the wall, 1 bottle of beer."
            + "Take one down and pass it around, no more bottles of beer on the wall."
        )
    else:
        return "No more bottles of beer on the wall, no more bottles of beer."


def sing_bottles_song(starting_bottles: int) -> None:
    """
    Prints the lyrics for the "Bottles of Beer on the Wall" song.

    Parameters:
        - starting_bottles: The number of bottles to start with.
        :type starting_bottles: int
    """
    while starting_bottles > 0:
        print(__get_verse_lyrics(starting_bottles))
        starting_bottles -= 1
    print("No more bottles of beer on the wall, no more bottles of beer.")
    return None


def main():
    while True:
        try:
            user_input = input("How many bottles of beer are on the wall? ")
            starting_bottles = int(user_input)
            if starting_bottles <= 0:
                print(f"{' ' * 2}*** Please enter a positive integer. ***")
                continue
            break
        except ValueError:
            print(f"{' ' * 2}*** Invalid input. Please enter a positive integer. ***")
    sing_bottles_song(starting_bottles)


if __name__ == "__main__":
    main()
