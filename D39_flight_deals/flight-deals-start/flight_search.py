"""This class is responsible for talking to the Flight Search API."""
import asyncio
import os
from datetime import datetime
from time import perf_counter

import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self) -> None:
        self.header = {"apikey": os.environ.get("KIWI_API_KEY")}
        self.api_endpoint = "https://api.tequila.kiwi.com"

    async def get_iata_city_code(self, city_name: str) -> str:
        """Returns a city IATA code by its name"""
        location_api_endpoint = f"{self.api_endpoint}/locations/query"
        parameters = {"term": city_name.replace(" ", "-")}

        response = await asyncio.to_thread(
            requests.get,
            url=location_api_endpoint,
            params=parameters,
            headers=self.header,
            timeout=30,
        )
        response.raise_for_status()

        for location in response.json().get("locations"):
            if location.get("type") == "city":
                return location.get("code")

    async def search(
        self,
        *,
        fly_from: str,
        fly_to: str,
        date_from: str,
        date_to: str,
        nights_in_dst_from: int = 2,
        nights_in_dst_to: int = 2,
    ) -> dict:
        """Search KIWI API for given flights"""

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
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "curr": "EUR",
            "sort": "price",
            "asc": -1,  # cheapest first
        }

        response = await asyncio.to_thread(
            requests.get,
            url=f"{self.api_endpoint}/v2/search",
            params=parameters,
            headers=self.header,
            timeout=30,
        )
        response.raise_for_status()

        return response.json().get("data")


if __name__ == "__main__":

    destinations = [{"city": "Miami"}, {"city": "Paris"}]

    async def main():
        """Test the function"""
        flight_search = FlightSearch()

        time_start = perf_counter()

        async with asyncio.TaskGroup() as tg:
            _ = [
                tg.create_task(
                    flight_search.get_iata_city_code(destination.get("city"))
                )
                for destination in destinations
            ]

        print(f"Elapsed time: {perf_counter()-time_start}")

    asyncio.run(main())
