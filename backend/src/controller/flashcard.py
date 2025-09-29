from pydantic import BaseModel
from pydantic.functional_validators import field_validator

from module.flashcard import FlashcardModule

from common.config import CONFIG


class FlashcardRequest(BaseModel):
    num_flashcards: int
    general_idea: str
    topics: list[str]
    is_highlighted: bool


class FlashcardControlller:
    def __init__(self):
        self._module = FlashcardModule()

    def create_flashcard(self, body: FlashcardRequest) -> dict:
        return {
            "status": 200,
            "data": self._module.create_flashcard(
                body.num_flashcards,
                body.general_idea,
                body.topics,
                body.is_highlighted,
            ),
        }
