import requests
import datetime as dt

pixel_endpoint="https://pixe.la/v1/users"
user_name="nishank16"
token= "NISHANKSHAH"
graph_id="nishank1"
users_parms={
    "token":token,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    
}


# response= requests.post(url= pixel_endpoint, json=users_parms)
# print(response.text)

graph_endpoint= f"{pixel_endpoint}/{user_name}/graphs"

graph_config={
    "id": graph_id,
    "name": "nishank_graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":token
}

# response= requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today_date=dt.datetime(year=2025, month=3, day=22)
print(today_date)

pixel_endpoint= f"{pixel_endpoint}/{user_name}/graphs/{graph_id}"

pixel_data={
    "date" : today_date.strftime('%Y%m%d'),
    "quantity" : "11.74",
}

# response= requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}/{today_date}"
pixel_update_data={
    "quantity" : "11.74",
}

response=requests.put(url = pixel_update, json = pixel_update_data, headers=headers)
print(response.text)

# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>