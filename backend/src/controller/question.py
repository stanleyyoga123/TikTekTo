from module.question import QuestionModule

from common.config import CONFIG


class QuestionControlller:
    def __init__(self):
        self._module = QuestionModule()

    def generate_pathway(self, general_idea: str, topics: list[str]) -> dict[str, any]:
        return self._module.retrieve_questions(general_idea, topics)
