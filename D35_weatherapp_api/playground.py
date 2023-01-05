import os

import requests
from dotenv import load_dotenv

# from weatherData import weather_data

load_dotenv()

API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")

parameters = {
    "lat": -10.443,  # 16.331141,
    "lon": -73.380,  # -61.344570,
    "appid": API_KEY,
    "units": "metric",
    "exclude": "current,minutely,daily",
}

response = requests.get(
    url="https://api.openweathermap.org/data/3.0/onecall",
    params=parameters,
    timeout=30,
)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

weather_codes = []
for hour in weather_data["hourly"][:12]:
    for weather in hour["weather"]:
        weather_codes.append(weather["id"])

if min(weather_codes) < 700:
    print(f"Bring an umbrella\n{weather_codes}")
