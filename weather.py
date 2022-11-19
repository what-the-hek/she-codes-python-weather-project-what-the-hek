import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    day = date.strftime("%A %d %B %Y")
    return day

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

def convert_f_to_c(temp_in_farenheit):
    temp_in_c = round(((float(temp_in_farenheit)) - 32) * 5/9, 1)
    return temp_in_c

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

def calculate_mean(weather_data):
    new_list = []
    for number in weather_data:
        number = float(number)
        new_list.append(number)
    mean = (sum(new_list)) / (len(new_list))
    return mean

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

def load_data_from_csv(csv_file):
    weather_data = []
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if not line:
                continue
            line[1] = int(line[1])
            line[2] = int(line[2])
            weather_data.append(line)
    return weather_data

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

def find_min(weather_data):
    temp_list = []
    for temp in weather_data:
        temp = float(temp)
        temp_list.append(temp)
    if not (temp_list):
        return ()
    min_temp = min(temp_list)
    # min_index = temp_list.index(min_temp) - there is a way to get this working with one character extra, google later ----------------
    for index in range(0, len(temp_list)):
        if temp_list[index] == min_temp:
            min_index = index
    return min_temp, min_index

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass

def find_max(weather_data):
    temp_list = []
    for temp in weather_data:
        temp = float(temp)
        temp_list.append(temp)
    if not (temp_list):
        return ()
    max_temp = max(temp_list)
    for index in range(0, len(temp_list)):
        if temp_list[index] == max_temp:
            max_index = index
    return max_temp, max_index

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass

def generate_summary(weather_data):
    day_list = []
    min_list = []
    max_list = []
    for row in weather_data:
        day = len(weather_data)
        day_list.append(row[0])
        min_list.append(row[1])
        max_list.append(row[2])

    min_temp_f = find_min(min_list)
    max_temp_f = find_max(max_list)
    min_temp_c = format_temperature(convert_f_to_c(min_temp_f[0]))
    max_temp_c = format_temperature(convert_f_to_c(max_temp_f[0]))
    min_day = convert_date(day_list[min_temp_f[1]])
    max_day = convert_date(day_list[max_temp_f[1]])

    average_low = format_temperature(convert_f_to_c(calculate_mean(min_list)))
    average_high = format_temperature(convert_f_to_c(calculate_mean(max_list)))

    summary = (f"{day} Day Overview\n  The lowest temperature will be {min_temp_c}, and will occur on {min_day}.\n  The highest temperature will be {max_temp_c}, and will occur on {max_day}.\n  The average low this week is {average_low}.\n  The average high this week is {average_high}.\n")
    return summary

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

def generate_daily_summary(weather_data):
    full_summary = ''
    for row in weather_data:
        day = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))
        daily_summary = (f"---- {day} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n")
        full_summary += daily_summary
    return full_summary

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
