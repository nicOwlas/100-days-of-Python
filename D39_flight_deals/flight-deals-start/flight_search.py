# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     pass
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

kiwi_api_key = os.environ.get("KIWI_API_KEY")
header = {"apikey": kiwi_api_key}


def get_iata_city_code(name: str) -> str:
    """Returns a city IATA code by its name"""
    api_endpoint = "https://api.tequila.kiwi.com/locations/query"
    parameters = {"term": name}

    response = requests.get(
        url=api_endpoint, params=parameters, headers=header, timeout=30
    )
    print(response.json())
    for location in response.json():

        if location.get("type") == "city":
            return location.get("code")


def flight_search(*, fly_from: str, fly_to: str, date_from: str, date_to: str) -> dict:
    """Search on KIWI API for given flights"""

    # Convert dates to KIWI API input format
    date_from_fr_format = datetime.strptime(date_from, "%Y-%m-%d").strftime("%d/%m/%Y")
    date_to_fr_format = datetime.strptime(date_to, "%Y-%m-%d").strftime("%d/%m/%Y")

    parameters = {
        "fly_from": fly_from,
        "fly_to": fly_to,
        "date_from": date_from_fr_format,
        "date_to": date_to_fr_format,
    }

    response = requests.get(
        url="https://api.tequila.kiwi.com/v2/search",
        params=parameters,
        headers=header,
        timeout=30,
    )

    return response.json()


if __name__ == "__main__":

    flight_search(
        fly_from="LGA", fly_to="MIA", date_from="2023-02-23", date_to="2023-02-24"
    )
