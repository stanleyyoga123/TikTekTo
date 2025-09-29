from google import genai
from google.genai.types import Part

from common.constant import GENERATOR_MODEL
from common.prompt import USER_PATHWAY_PROMPT, USER_PATHWAY_DOCUMENT_PROMPT
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

    def create_pathway_from_file(self, data: bytes, objective: str) -> dict[str, any]:
        content = USER_PATHWAY_DOCUMENT_PROMPT.format(objective=objective)
        response = self._client.models.generate_content(
            model=GENERATOR_MODEL,
            contents=[content, Part.from_bytes(data=data, mime_type="application/pdf")],
        )
        return parse_response_to_json(response.text)
