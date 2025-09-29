import json


def parse_response_to_json(response: str):
    return json.loads(response.strip("```").strip("json"))
