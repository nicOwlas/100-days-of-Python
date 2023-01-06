import os
from datetime import date, datetime

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"


USER_API_ENDPOINT = "https://pixe.la/v1/users"
CREATE_GRAPH_API_ENDPOINT = f"{USER_API_ENDPOINT}/{USERNAME}/graphs"
PIXEL_API_ENDPOINT = f"{USER_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {"X-USER-TOKEN": TOKEN}


def create_user(token: str, username: str) -> None:
    """Create user"""
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=USER_API_ENDPOINT, json=user_params, timeout=30)
    print(response.text)


def create_graph(**kwargs) -> None:
    """Create Graph"""

    graph_params = {
        "id": kwargs["id"],
        "name": kwargs["name"],
        "unit": kwargs["unit"],
        "type": kwargs["type"],
        "color": kwargs["color"],
    }
    response = requests.post(
        url=CREATE_GRAPH_API_ENDPOINT, json=graph_params, headers=headers, timeout=30
    )
    print(response.text)


def create_pixel(**kwargs) -> None:
    """Create a pixel"""

    pixel_params = {
        "date": kwargs["date"],
        "quantity": kwargs["quantity"],
        "optionalData": kwargs["optionalData"],
    }

    response = requests.post(
        url=PIXEL_API_ENDPOINT, json=pixel_params, headers=headers, timeout=30
    )
    print(response.text)


def update_pixel(**kwargs) -> None:
    """Update a pixel"""
    update_endpoint = f"{PIXEL_API_ENDPOINT}/{kwargs['date']}"

    pixel_params = {
        "quantity": kwargs.get("quantity"),
        "optionalData": kwargs.get("optionalData"),
    }

    response = requests.put(
        url=update_endpoint, json=pixel_params, headers=headers, timeout=30
    )
    print(response.text)


def delete_pixel(**kwargs) -> None:
    """Update a pixel"""
    delete_endpoint = f"{PIXEL_API_ENDPOINT}/{kwargs['date']}"

    response = requests.delete(url=delete_endpoint, headers=headers, timeout=30)
    print(response.text)


if __name__ == "__main__":
    pixel_date = datetime(year=2022, month=11, day=24)

    # create_user(token=TOKEN, username=USERNAME)
    # create_graph(
    #     id=GRAPH_ID,
    #     name="Running Activity",
    #     unit="Kilometers",
    #     type="float",
    #     color="sora",
    # )

    # create_pixel(
    #     date=datetime.strftime(pixel_date, "%Y%m%d"),
    #     quantity="81.14",
    #     optionalData="5.14",
    # )

    # update_pixel(
    #     date=datetime.strftime(pixel_date, "%Y%m%d"),
    #     quantity="8.14",
    #     optionalData="5.14",
    # )

    delete_pixel(date=datetime.strftime(pixel_date, "%Y%m%d"))
