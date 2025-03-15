# https://home.openweathermap.org/          -- weather data
# https://openweathermap.org/current        --oppenweathermap current weather
# https://www.latlong.net/                  -- find lat long
# https://openweathermap.org/forecast5      --5day/3hr forecast
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2     -- condition codes
# https://www.ventusky.com/                 -- find place where its raining
# https://console.twilio.com/               -- twilio- used for making calls or sms
# https://www.twilio.com/docs/messaging/quickstart/python                     -- twilio docs\
# https://jsonviewer.stack.hu/              --JSON viewer
# https://www.pythonanywhere.com/           --deploy code on cloud
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/                 -- get twilio work on pythonanywhere
# https://en.wikipedia.org/wiki/Environment_variable                          --env var
# https://apilist.fun/                      --other API to explore

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = ""#OPENWEATHER_API_KEY
account_sid = ""#TWILIO_ACC_SID
auth_token = ""#TWILIO_AUTH_TOKEN
parameters ={
    "lat":22.733124,
    "lon":113.908977,
    "appid" : api_key,
    "cnt" : 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    #Send SMS to mobile
    # uncomment this when deployed to pythonAnywhere and comment the client line
    # '''     
    # proxy_client =TwilioHttpClient()
    # proxy_client.session.proxies = {'https' : os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    # '''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Its going to rain today, bring an umbrella!.", 
    from_= "",#TWILIO_NUMBER     # from_="whatsapp:TWILIO_WHATSAPP_NUMBER",   -- for whatspp msg
    to= "",#VERIFIED_NUMBER
    )

    print(message.status)