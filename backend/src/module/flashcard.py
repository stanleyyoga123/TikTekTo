from google import genai

from common.constant import GENERATOR_MODEL
from common.prompt import FLASHCARD_CREATION_PROMPT
from common.utility import parse_response_to_json


class FlashcardModule:
    def __init__(self):
        self._client = genai.Client()

    def create_flashcard(
        self, num_flashcards: int, general_idea: str, topics: list[str]
    ) -> dict[str, any]:
        content = FLASHCARD_CREATION_PROMPT.format(
            num_flashcards=num_flashcards,
            general_idea=general_idea,
            topics=" ; ".join(topics),
        )
        response = self._client.models.generate_content(
            model=GENERATOR_MODEL, contents=content
        )
        out = parse_response_to_json(response.text)
        return out
