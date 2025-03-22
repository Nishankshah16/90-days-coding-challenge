# https://pixe.la/              --pixela
# https://docs.pixe.la/         --pixela API docs
# https://requests.readthedocs.io/en/latest/api/            --request module docs

import requests
from datetime import datetime

USERNAME = "nishank16"
TOKEN = "NISHANKSHAH"
GRAPH_ID = "graph1"

pixel_endpoint="https://pixe.la/v1/users"

# register 
users_parms={
    "token": TOKEN,   # give token of your choice [-~]{8,128}
    "username": USERNAME,     # [a-z][a-z0-9-]{1,32}
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    
}

# response= requests.post(url= pixel_endpoint, json=users_parms)
# print(response.text)

#Create graph
graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,     #^[a-z][a-z0-9-]{1,16}
    "name": "Cyclic graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

header = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers=header)
# print(response.text)      #https://pixe.la/v1/users/USERNAME/graphs/graph1.html

# Post a pixel in graph
pixel_create_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2025,month=3,day=21)#.now()
date = today.strftime("%Y%m%d")
pixel_config = {
    "date" : date,    #yyyyMMdd
    "quantity" : "15",     #int^-?[0-9]+ float^-?[0-9]+.[0-9]+
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_config, headers=header)
# print(response.text)

#Update a pixel
pixel_update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_data = {
    "quantity" : "12"
}
response = requests.put(url=pixel_update_endpoint, json=update_data, headers=header)
print(response.text)

#Delete a pixel
pixel_update = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

response=requests.delete(url=pixel_update, headers=header)
print(response.text)
