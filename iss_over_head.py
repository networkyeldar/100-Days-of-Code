import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "eltaiuly1205@gmail.com"
PASSWORD = "ewf"

MY_LAT = 51.160522
MY_LONG = 71.470360

def is_iss_over_head():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latiude = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= iss_latiude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters ={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(90) # will run code every 1.5 minute
    if is_iss_over_head() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,msg="Subject: Look up\n\n The ISS is aboveyou in the sky")




