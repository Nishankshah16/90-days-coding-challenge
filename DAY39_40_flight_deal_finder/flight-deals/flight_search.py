import requests
from dotenv import load_dotenv
import os

load_dotenv()

AMANDEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()
    
    def get_code(self, cityname):
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        parameter = {
            "keyword" : cityname,
            "max" : 2,
            "include" : "AIRPORTS"
        }
        response=requests.get(url=IATA_ENDPOINT,headers=header, params=parameter)
        # print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {cityname}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {cityname}.")
            return "Not Found"

        return code
    
    def _get_new_token(self):
        header = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response=requests.post(url=AMANDEUS_TOKEN_ENDPOINT,headers=header, data=body)

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        header ={
            "Authorization" : f"Bearer {self._token}"
        }
        parameter = {
            "originLocationCode" : origin_city_code,
            "destinationLocationCode" : destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate" : to_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop" : "true" if is_direct else "false",
            "currencyCode" : "GBP",
            "max" : 10
        }

        response=requests.get(url=FLIGHT_ENDPOINT,headers=header, params=parameter)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n")
            print("Response body:", response.text)
            return None
        return response.json()