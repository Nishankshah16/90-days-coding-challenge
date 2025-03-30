from data_manager import DataManager
from flight_search import FlightSearch


sheet_data= DataManager.get_data()

if sheet_data[0]["iataCode"]== "":
    for i in sheet_data:
        city=i["city"]
        response=FlightSearch.get_code(city)
        data = sheet_data
        DataManager.update()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.