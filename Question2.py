import os
import csv
import math

DATA_FOLDER = "temperatures"

SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}


def is_valid(value):
    """Check if temperature value is valid (not empty or NaN)."""
    return value not in ("", "NaN")


def read_all_temperatures():
    """
    Reads all CSV files and collects:
    - seasonal temperatures
    - station temperature lists
    """
    seasonal_data = {season: [] for season in SEASONS}
    station_data = {}

    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".csv"):
            with open(os.path.join(DATA_FOLDER, file), newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    station = row["STATION_NAME"]

                    if station not in station_data:
                        station_data[station] = []

                    for season, months in SEASONS.items():
                        for month in months:
                            if is_valid(row[month]):
                                temp = float(row[month])
                                seasonal_data[season].append(temp)
                                station_data[station].append(temp)

    return seasonal_data, station_data


def calculate_seasonal_averages(seasonal_data):
    with open("average_temp.txt", "w", encoding="utf-8") as file:
        for season, temps in seasonal_data.items():
            avg = sum(temps) / len(temps)
            file.write(f"{season}: {avg:.2f}°C\n")


def main():
    seasonal_data, station_data = read_all_temperatures()
    calculate_seasonal_averages(seasonal_data)
    print("Question 2 analysis completed successfully.")


if __name__ == "__main__":
    main()

