import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

def display_menu():
    """Displays the menu for the user to choose between highs, lows, or exit."""
    print("\nChoose an option:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

while True:
    choice = display_menu()

    if choice == '1':
        # Plot high temperatures
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '2':
        # Plot low temperatures
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")