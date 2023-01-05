import requests


def get_question_set(set_size):
    """Return a set of questions from the trivia API"""
    parameters = {"amount": set_size, "type": "boolean"}
    response = requests.get(
        url="https://opentdb.com/api.php", params=parameters, timeout=30
    )
    return response.json()["results"]


question_data = get_question_set(10)
