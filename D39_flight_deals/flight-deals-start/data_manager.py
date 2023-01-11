"""This class is responsible for talking to the Google Sheet."""
import asyncio
import os

import inflect
import requests
from dotenv import load_dotenv

load_dotenv()

p = inflect.engine()


def to_camel_case(text: str) -> str:
    """Returns a string in camelCase"""
    text_spaced = text.replace("-", " ").replace("_", " ")
    text_split = text_spaced.split()
    if len(text) == 0:
        return text
    return text_split[0].lower() + "".join(
        token.capitalize() for token in text_split[1:]
    )


class DataManager:
    """This class is responsible for talking to the Google Sheet"""

    def __init__(self, file_name: str, tab_name: str) -> None:
        self.username = os.environ.get("SHEETY_USERNAME")
        self.file_name = to_camel_case(file_name)
        self.tab_name = to_camel_case(tab_name)
        self.header = {"Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"}
        self.api_endpoint = (
            f"https://api.sheety.co/{self.username}/{self.file_name}/{self.tab_name}"
        )
        # Return the sheet name if its singular does not exist (prices -> price)
        self.tab_name_singular = (
            tab_name if not p.singular_noun(tab_name) else p.singular_noun(tab_name)
        )

    async def get_tab_data(self) -> dict:
        """Read and return values stored in tab_name"""
        response = await asyncio.to_thread(
            requests.get,
            url=self.api_endpoint,
            headers=self.header,
            timeout=30,
        )
        response.raise_for_status()
        return response.json().get(self.tab_name)

    async def update_row(self, row_data: dict) -> None:
        """Update a given row. dictionnary with key/value.
        Keys : camelCase of the column titles / Values: data to be updated
        An 'id' key takes an int for value. It's the row index (starts at 1) to be updated
        """
        row_id = row_data.get("id")
        update_row_endpoint = f"{self.api_endpoint}/{row_id}"

        payload = {self.tab_name_singular: row_data}
        response = await asyncio.to_thread(
            requests.put,
            url=update_row_endpoint,
            json=payload,
            headers=self.header,
            timeout=30,
        )
        return response.status_code


if __name__ == "__main__":

    async def main():
        file_name = "Flight Deals"
        tab_name = "prices"
        row = {"city": "Miami", "iataCode": "hello", "lowestPrice": 540, "id": 2}
        data_manager = DataManager(file_name=file_name, tab_name=tab_name)
        tab_data = await data_manager.get_tab_data()
        print(tab_data)
        update_status = await data_manager.update_row(row_data=row)
        print(update_status)

    asyncio.run(main())
