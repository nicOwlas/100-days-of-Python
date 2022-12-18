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
temperature_max = data["temp"].max()
print(data[data.temp == temperature_max])
