from datetime import datetime
import requests
import pytz

parameters = {"lat": 16.330707, "lng": -61.343031, "formatted": 0}
response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters, timeout=30
)
response.raise_for_status()
data = response.json()
sunrise = datetime.strptime(data["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
sunset = datetime.strptime(data["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z")
print(sunrise)
print(sunset)


time_now = datetime.now().astimezone(pytz.utc)
print(time_now)
print(sunrise < time_now)
