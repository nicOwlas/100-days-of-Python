import csv
import pandas

# with open("./weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temperatures)

data = pandas.read_csv("./weather_data.csv")
print(data)
monday = data[data.day == "Monday"]
monday_temperature_fahrenheit = int(monday.temp) * 9 / 5 + 32
# data.loc[data.day == "Monday", ["temp"]] = monday.temp * 1.8 + 32
print(monday_temperature_fahrenheit)
