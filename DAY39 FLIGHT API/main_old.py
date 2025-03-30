import requests
from pprint import pprint

api_sheety="https://api.sheety.co/3550a86d20c174db2e94b4b24276862b/myFlightDeals/prices"

response=requests.get(url=api_sheety)
pprint(response.json()["prices"])