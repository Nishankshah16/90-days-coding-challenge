# nutition_api= https://www.nutritionix.com/business/api
# nutition_api docs = https://docx.syndigo.com/developers
# sheety API = https://sheety.co/
# sheety docs = https://sheety.co/docs/requests
# make copy = https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?gid=0#gid=0
 
import requests
import datetime as dt

#  Nutritionix  api key and id
api_key=""
api_id=""
# GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 173
AGE = 27

API_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
input_exercise=input("Please tell what you did today: ")

headers={
    "x-app-id": api_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

parameters={
    "query": input_exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# shetty username and password of authentication(Basic)
YOUR_USERNAME=""
YOUR_PASSWORD=""
response=requests.post(url=API_ENDPOINT, json= parameters,headers=headers)
data=response.json()
print(data)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

# API -> get username from get url
username=""
project="myWorkoutsRegister"
sheetname="workouts"
sheet_endpoint=f"https://api.sheety.co/{username}/{project}/{sheetname}"

for exercise in data["exercises"]:
    sheet_input={
        "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }
    response=requests.post(url=sheet_endpoint,json=sheet_input, auth=(YOUR_USERNAME,YOUR_PASSWORD))
    print(response.text)


