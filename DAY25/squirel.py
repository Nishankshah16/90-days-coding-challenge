import pandas as pd

data=pd.read_csv("./DAY25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)

finaldata= data["Primary Fur Color"]
# print(finaldata)


unique=finaldata.unique()
# print(unique)

agg_data=finaldata.groupby(level="Primary Fur Color").sum()
print(agg_data)