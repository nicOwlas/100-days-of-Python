import os
from datetime import date, datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def transcribe_exercise(prompt: str) -> dict:
    """Infers the prompt with Nutritionix to return a data structure"""
    app_id = os.environ.get("NUTRITIONIX_APP_ID")
    api_key = os.environ.get("NUTRITIONIX_API_KEY")
    header = {
        "x-app-id": app_id,
        "x-app-key": api_key,
    }
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    exercise_input = {"query": prompt}

    response = requests.post(
        url=exercise_endpoint, json=exercise_input, headers=header, timeout=30
    )
    return response.json()


def add_row(workout: dict, project_name: str, sheet_name: str) -> None:
    """Fill in a google sheet with Sheety with the exercises infered by Nutritionix"""
    username = os.environ.get("SHEETY_USERNAME")
    token = os.environ.get("SHEETY_TOKEN")
    sheety_api_endpoint = (
        f"https://api.sheety.co/{username}/{project_name}/{sheet_name}"
    )
    # Header
    header = {"Authorization": f"Bearer {token}"}
    date_today = date.today().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    payload = {
        f"{sheet_name}": {
            "date": date_today,
            "time": time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }
    requests.post(url=sheety_api_endpoint, json=payload, headers=header, timeout=30)


if __name__ == "__main__":
    PROJECT_NAME = "d38MyWorkouts"
    SHEET_NAME = "log"
    answer = input("What exercise have you done today? ")
    # answer = "I've been walking 10km and swimming 2km"
    transcription = transcribe_exercise(answer)

    for exercise in transcription.get("exercises"):
        add_row(
            workout=exercise,
            project_name=PROJECT_NAME,
            sheet_name=SHEET_NAME,
        )
