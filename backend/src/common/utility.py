import json

from common.prompt import HIGHLIGHT_ADDITIONAL_PROMPT


def parse_response_to_json(response: str):
    return json.loads(response.strip("```").strip("json"))


def wrap_prompt(prompt: str, is_highlighted: bool):
    return prompt + HIGHLIGHT_ADDITIONAL_PROMPT if is_highlighted else prompt
