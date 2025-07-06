"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 15th, 2025
Assignment: Module 3.2 Brownfield + Flowchart
Purpose: Modify the original `sitka_highs.py` module as defined below:
    - Open the program with instructions on how to use the menu: Highs, Lows, or Exit.
    - When the program starts, allow the user to select whether they want to see the high
    temperatures or the low temperatures, or to exit.
    - When the user selects `lows`, they should see a graph, in blue, that reflects the lows for those dates.
    - Allow the program to loop until the user selects exit.
    - When the user exits, provide an exit message.
    - Use what elements you can from previous programs, perhaps including sys to help the exit process.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys


def get_weather_data(filename):
    """Reads weather data from a CSV file and returns dates, highs, and lows."""
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {row[2]}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows


def plot_temperatures(dates, temperatures, color, title):
    """Plots the given temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()


def print_instructions():
    print("\nWelcome to the Sitka Weather 2018 Temperature Viewer!")
    print("You can view daily high or low temperatures as a graph.")
    print("How to use the menu:")
    print("  1 - View High Temperatures (red graph)")
    print("  2 - View Low Temperatures (blue graph)")
    print("  3 - Exit the program")
    print("Select the desired option by entering its number and pressing Enter.\n")


def main():
    filename = "sitka_weather_2018_simple.csv"
    dates, highs, lows = get_weather_data(filename)

    print_instructions()

    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            plot_temperatures(dates, highs, "red", "Daily High Temperatures - 2018")
        elif choice == "2":
            plot_temperatures(dates, lows, "blue", "Daily Low Temperatures - 2018")
        elif choice == "3":
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
