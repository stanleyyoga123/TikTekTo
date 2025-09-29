from pydantic import BaseModel
from module.question import QuestionModule


class QuestionRequest(BaseModel):
    general_idea: str
    topics: list[str]


class QuestionControlller:
    def __init__(self):
        self._module = QuestionModule()

    def retrieve_questions(self, body: QuestionRequest) -> dict:
        return {
            "status": 200,
            "data": self._module.retrieve_questions(
                body.general_idea,
                body.topics,
            ),
        }
