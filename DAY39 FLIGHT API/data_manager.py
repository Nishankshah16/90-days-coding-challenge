import requests


api_sheety="https://api.sheety.co/3550a86d20c174db2e94b4b24276862b/myFlightDeals/prices"
class DataManager:
    def __init__(self):
        self.api_key = ""
        self.data = {}
    

    def get_data(self):
        response=requests.get(url=api_sheety)
        return response.json()["prices"]
    
    def update(self):
        response=requests.put(url=f"{api_sheety}/{self.data["city"]}")
        return response.json()["prices"]
    




    #This class is responsible for talking to the Google Sheet.
    pass