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


def calculate_largest_range(station_data):
    ranges = {}
    for station, temps in station_data.items():
        ranges[station] = max(temps) - min(temps)
 
    max_range = max(ranges.values())
 
    with open("largest_temp_range_station.txt", "w", encoding="utf-8") as file:
        for station, r in ranges.items():
            if math.isclose(r, max_range):
                file.write(
                    f"{station}: Range {r:.2f}°C "
                    f"(Max: {max(station_data[station]):.2f}°C, "
                    f"Min: {min(station_data[station]):.2f}°C)\n"
                )
 
 
def standard_deviation(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
 
 
def calculate_temperature_stability(station_data):
    std_devs = {station: standard_deviation(temps)
                for station, temps in station_data.items()}
 
    min_std = min(std_devs.values())
    max_std = max(std_devs.values())
 
    with open("temperature_stability_stations.txt", "w", encoding="utf-8") as file:
        for station, std in std_devs.items():
            if math.isclose(std, min_std):
                file.write(f"Most Stable: {station}: StdDev {std:.2f}°C\n")
 
        for station, std in std_devs.items():
            if math.isclose(std, max_std):
                file.write(f"Most Variable: {station}: StdDev {std:.2f}°C\n")
 
 
def main():
    seasonal_data, station_data = read_all_temperatures()
    calculate_seasonal_averages(seasonal_data)
    calculate_largest_range(station_data)
    calculate_temperature_stability(station_data)
    print("Question 2 analysis completed successfully.")
 
 
if __name__ == "__main__":
    main()
 
