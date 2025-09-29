from module.flashcard import FlashcardModule

from common.config import CONFIG


class FlashcardControlller:
    def __init__(self):
        self._module = FlashcardModule()

    def generate_pathway(
        self, num_flashcards: int, general_idea: str, topics: list[str]
    ) -> dict[str, any]:
        return self._module.create_flashcard(num_flashcards, general_idea, topics)
