import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


def transcribe_exercise(prompt: str) -> dict:
    """Infers the prompt to return a data structure"""
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    exercise_input = {"query": prompt}

    response = requests.post(
        url=exercise_endpoint, json=exercise_input, headers=header, timeout=30
    )
    return response.json()


if __name__ == "__main__":
    answer = input("What exercise have you done today? ")
    # answer = "I've been walking 10km and swimming 2km"
    transcription = transcribe_exercise(answer)
    print(json.dumps(transcription, indent=4))
