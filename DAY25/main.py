with open("./DAY25/weather_data.csv") as file:
    weather_data=file.readlines()
    print(weather_data)


import csv

with open("./DAY25/weather_data.csv") as file:
    data=csv.reader(weather_data)
    temprature=[]
    for row in data:
        if row[1] != "temp":
            temprature.append(int(row[1]))
    print(temprature)


import pandas as pd

data= pd.read_csv("./DAY25/weather_data.csv")
print(data)
print(data["temp"])