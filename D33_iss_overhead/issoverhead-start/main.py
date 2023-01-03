from datetime import datetime
import time
import smtplib
import os
import pytz
import requests

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_nigth(location):
    """Returns true if its night time"""
    time_now = datetime.now().astimezone(pytz.utc)

    parameters = {
        "lat": location.get("lat"),
        "lng": location.get("long"),
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, timeout=30
    )
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.strptime(data["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
    sunset = datetime.strptime(data["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z")

    if time_now > sunset or time_now < sunrise:
        return True
    else:
        return False


def is_iss_close(location):
    """Returns true if my position is within +5 or -5 degrees of the ISS position."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=30)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_position = {"lat": iss_latitude, "long": iss_longitude}
    if (
        abs(iss_position["lat"] - location["lat"]) <= 5
        and abs(iss_position["long"] - location["long"]) <= 5
    ):
        return True
    else:
        return False


def send_email(email_recipient):
    """Sends an email. The sender email is defined in the .env file"""

    smtp_address = os.environ.get("SMTP_ADDRESS")
    email_sender = os.environ.get("EMAIL_SENDER")
    password_app = os.environ.get("PASSWORD_APP")

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password_app)
        connection.sendmail(
            from_addr=email_sender,
            to_addrs=email_recipient,
            msg="Subject:ISS is close!\n\nLook up, the iss is close !",
        )


my_location = {"lat": MY_LAT, "long": MY_LONG}

while True:
    time.sleep(60)
    if is_nigth(my_location) and is_iss_close(my_location):
        send_email(os.environ.get("EMAIL_RECIPIENT"))
