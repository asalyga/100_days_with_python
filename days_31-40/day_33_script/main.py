import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.407446  # Your latitude
MY_LONG = 16.932706  # Your longitude
my_email = "ur email here"
password = "ur password here"


def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 > iss_latitude > MY_LONG - 5 and MY_LONG + 5 > iss_longitude > MY_LONG - 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if sunrise >= time_now.hour or sunset <= time_now.hour:
        return True


def main_func():
    if is_iss_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="where to send",
                                msg=f"Subject:ISS IS IN UR AREA \n\n Look Up!")
            connection.close()


while True:
    main_func()
    time.sleep(60)
