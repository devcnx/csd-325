"""
Starting file for Module 3.2 High/Low Temperatures.

This module is a simple example of reading a CSV file and plotting data
from it. The flow of the program will be as follows:

    1. Open the file.
    2. Read the data from the file.
    3. Capture the data from the header row.
    4. Create empty lists to hold the `dates` and `highs`.
    5. Loop through the data and fill the lists with data extracted from the file.
    6. Plot the high temperatures.
    7. Format the plot.
    8. Show the plot.
"""


import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = "module_4/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
