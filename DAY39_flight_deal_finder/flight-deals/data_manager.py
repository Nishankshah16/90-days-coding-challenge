import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

# shetty sheet details
username = os.environ["SHETTY_USERNAME"]
project = "flightDeals"
sheetname = "prices"
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{username}/{project}/{sheetname}"
class DataManager:
    def __init__(self):
        self._USERNAME = os.environ["USERNAME"]
        self._PASSWORD = os.environ["PASSWORD"]
        self._auth = (self._USERNAME,self._PASSWORD)    
        self.dest_data = []
        

    def get_dest_data(self):
        response=requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._auth)
        # print(response.raise_for_status)
        self.dest_data= response.json()["prices"]
        return self.dest_data
    
    def update_dest_code(self):
        for data in self.dest_data:
            sheet_input={
                "price": {
                    "iataCode": data["iataCode"]
                }
            }
            
            response=requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{data['id']}",json=sheet_input, auth=self._auth)
            # print(response.text)
