import requests

pixel_endpoint="https://pixe.la/v1/users"

users_parms={
    "token":"NISHANKSHAH",
    "username":"nishank16",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    
}


# response= requests.post(url= pixel_endpoint, json=users_parms)
# print(response.text)