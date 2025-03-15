# https://en.wikipedia.org/wiki/International_Space_Station     --ISS
# https://en.wikipedia.org/wiki/API                             --API
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/      --ISS current loc API docs
# https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?pli=1           --JSON viewer
# https://www.webfx.com/web-development/glossary/http-status-codes/                 --HTTPS status code
# https://www.latlong.net/Show-Latitude-Longitude.html          --lat long 
# https://docs.python-requests.org/en/latest/                   --requests module

import requests
from datetime import datetime
import smtplib
import time

my_email="nishankshah16@gmail.com"
my_password=""
MY_LAT = 18.600269
MY_LNG = 73.729455

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    iss_pos = (latitude, longitude)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

#SUNSET SUNRISE API
def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted":0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameter) #if we run without specifying parameter will get 400 BAD REQUEST error!
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="anunita.n@gmail.com",msg=f"Subject: Look Up \n\nThe ISS is above you in the sky.")
