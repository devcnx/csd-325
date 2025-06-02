"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 1st, 2025
Assignment: Module 1.3 On the Wall + Flowchart
Purpose: A program that prompts the user for the number of bottles on the wall and then prints the "Bottles of Beer" song lyrics counting down to 0.
"""


def sing_bottles_song(starting_bottles: int) -> None:
    """
    Sing the song.

    Parameters:
        - starting_bottles: The number of bottles to count down from.
        :type starting_bottles: int

    Returns:
        None
    """

    for bottles in range(starting_bottles, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottles = bottles - 1
            bottle_word = "bottle" if next_bottles == 1 else "bottles"
            print(
                f"Take one down and pass it around, {next_bottles} {bottle_word} of beer on the wall.\n"
            )
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print(
                "Take one down and pass it around, no more bottles of beer on the wall.\n"
            )
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(
        f"Go to the store and buy some more, {starting_bottles} bottles of beer on the wall."
    )


def main() -> None:
    """
    Main function.
    """
    while True:
        try:
            user_input = input("How many bottles of beer are on the wall? ")
            starting_bottles = int(user_input)
            if starting_bottles <= 0:
                print("Please enter a positive integer.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.\n")
    sing_bottles_song(starting_bottles)


if __name__ == "__main__":
    main()
