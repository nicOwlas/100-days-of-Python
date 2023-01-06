import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
USER_API_ENDPOINT = "https://pixe.la/v1/users"

# 1. Create user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=USER_API_ENDPOINT, json=user_params, timeout=30)
# print(response.text)

# 2. Create Graph
GRAPH_API_ENDPOINT = f"{USER_API_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id": "graph2",
    "name": "Cycling Activity",
    "unit": "Kilometers",
    "type": "float",
    "color": "momiji",
}
headers = {"X-USER-TOKEN": TOKEN}

response = requests.post(
    url=GRAPH_API_ENDPOINT, json=graph_params, headers=headers, timeout=30
)
print(response.text)

# 3. Populate Graph
