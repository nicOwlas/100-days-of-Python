# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass
import os

import inflect
import requests
from dotenv import load_dotenv

p = inflect.engine()

load_dotenv()

username = os.environ.get("SHEETY_USERNAME")
token = os.environ.get("SHEETY_TOKEN")
header = {"Authorization": f"Bearer {token}"}


def convert_to_camel_case(text: str) -> str:
    """Returns a string in camelCase"""
    text_spaced = text.replace("-", " ").replace("_", " ")
    text_split = text_spaced.split()
    if len(text) == 0:
        return text
    return text_split[0].lower() + "".join(
        token.capitalize() for token in text_split[1:]
    )


def get_sheet_data(file_name: str, sheet_name: str) -> dict:
    """Read google sheet values and return its values"""
    file_name_formatted = convert_to_camel_case(file_name)
    sheet_name_formatted = convert_to_camel_case(sheet_name)
    api_endpoint = (
        f"https://api.sheety.co/{username}/{file_name_formatted}/{sheet_name_formatted}"
    )
    response = requests.get(url=api_endpoint, headers=header, timeout=30)
    print(response.json())
    return response.json().get(sheet_name)


def update_row(file_name: str, sheet_name: str, row_value: dict) -> None:
    """Update a given row. dictionnary with key/value.
    Keys : camelCase of the column titles / Values: data to be updated
    An 'id' key takes an int for value. It's the row index (starts at 1) to be updated
    """
    file_name_formatted = convert_to_camel_case(file_name)
    sheet_name_formatted = convert_to_camel_case(sheet_name)
    row_id = row_value.get("id")
    api_endpoint = f"https://api.sheety.co/{username}/{file_name_formatted}/{sheet_name_formatted}/{row_id}"

    # SHEETY requires the row_data to be in a dict having as a key the singular of the sheet_name...
    payload = {p.singular_noun(sheet_name): row_value}
    requests.put(url=api_endpoint, json=payload, headers=header, timeout=30)


if __name__ == "__main__":
    google_sheet_name = "Flight Deals"
    tab_name = "prices"
    row_value = {"city": "Paris", "iataCode": "", "lowestPrice": 54, "id": 2}
    get_sheet_data(google_sheet_name, tab_name)
    update_row(google_sheet_name, tab_name, row_value)
