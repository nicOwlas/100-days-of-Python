import csv
import pandas

# with open("./weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temperatures)

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = ["Gray", "Cinnamon", "Black"]
data_dict = {}
data_dict["Fur Color"] = ["Gray", "Red", "Black"]
data_dict["Count"] = [len(data[data["Primary Fur Color"] == color]) for color in colors]
dataframe_fur_count = pandas.DataFrame(data_dict)
dataframe_fur_count.to_csv("count_fur_color.csv")
