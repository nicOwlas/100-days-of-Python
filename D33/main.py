import requests
import json

response = requests.get(url="https://api.kanye.rest/")
print(json.dumps(response.json(), indent=4))