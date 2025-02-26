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
# print(data)
# print(data["temp"])

data_dict= data.to_dict()
print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)

# Average=sum(temp_list)/len(temp_list)
# print(Average)

# print(data["temp"].mean())

# print(data["temp"].max())

# #get data in column
# print(data["day"]=="Monday")

# print(data[data["temp"]==data["temp"].max()])

monday=data[data["day"]=="Monday"]
# print(monday)
# print(monday["condition"])
print(monday["temp"][0])
monday_temp=monday["temp"][0]
monday_temp_f=monday_temp * 9/5 +32
