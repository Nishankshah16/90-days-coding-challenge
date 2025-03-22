# nutition_api= https://www.nutritionix.com/business/api

import requests
import datetime as dt

api_key="9eb5cbfc27e07c3fb75f6f45794de819"
api_id="372eece0"
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

YOUR_USERNAME="nishankshah16"
YOUR_PASSWORD="Nishu16@"
response=requests.post(url=API_ENDPOINT, json= parameters,headers=headers)
data=response.json()
print(data)



today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")


username="3550a86d20c174db2e94b4b24276862b"
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


