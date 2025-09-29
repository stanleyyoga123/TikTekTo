from google import genai

from common.constant import GENERATOR_MODEL
from common.prompt import USER_PATHWAY_PROMPT
from common.utility import parse_response_to_json


class UserPathwayModule:
    def __init__(self):
        self._client = genai.Client()

    def create_pathway(
        self, role: str, background: str, additional: str, objective: str
    ) -> dict[str, any]:
        content = USER_PATHWAY_PROMPT.format(
            role=role,
            background=background,
            additional=additional,
            objective=objective,
        )
        response = self._client.models.generate_content(
            model=GENERATOR_MODEL, contents=content
        )
        return parse_response_to_json(response.text)
