from pydantic import BaseModel
from module.check_answer import CheckAnswerModule


class CheckAnswerRequest(BaseModel):
    question: str
    true_answer: str
    user_answer: str
    is_highlighted: bool


class CheckAnswerControlller:
    def __init__(self):
        self._module = CheckAnswerModule()

    def check(self, body: CheckAnswerRequest) -> dict:
        return {
            "status": 200,
            "data": self._module.check(
                body.question,
                body.true_answer,
                body.user_answer,
                body.is_highlighted,
            ),
        }
