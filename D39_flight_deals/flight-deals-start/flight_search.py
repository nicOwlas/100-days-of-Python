"""This class is responsible for talking to the Flight Search API."""
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self) -> None:
        self.header = {"apikey": os.environ.get("KIWI_API_KEY")}
        self.api_endpoint = "https://api.tequila.kiwi.com"

    def get_iata_city_code(self, name: str) -> str:
        """Returns a city IATA code by its name"""
        location_api_endpoint = f"{self.api_endpoint}/locations/query"
        parameters = {"term": name}

        response = requests.get(
            url=location_api_endpoint,
            params=parameters,
            headers=self.header,
            timeout=30,
        )

        for location in response.json().get("locations"):
            if location.get("type") == "city":
                return location.get("code")

    def search(
        self, *, fly_from: str, fly_to: str, date_from: str, date_to: str
    ) -> dict:
        """Search on KIWI API for given flights"""

        # Convert dates to KIWI API input format
        date_from_fr_format = datetime.strptime(date_from, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        date_to_fr_format = datetime.strptime(date_to, "%Y-%m-%d").strftime("%d/%m/%Y")

        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from_fr_format,
            "date_to": date_to_fr_format,
        }

        response = requests.get(
            url=f"{self.api_endpoint}/v2/search",
            params=parameters,
            headers=self.header,
            timeout=30,
        )

        return response.json()


if __name__ == "__main__":
    import json

    flight_search = FlightSearch()

    flights = flight_search.search(
        fly_from="LGA", fly_to="MIA", date_from="2023-02-23", date_to="2023-02-24"
    )
    print(json.dumps(flights, indent=2))
