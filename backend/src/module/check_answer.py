from google import genai

from common.constant import GENERATOR_MODEL
from common.prompt import CHECK_ANSWER_PROMPT
from common.utility import parse_response_to_json, wrap_prompt


class CheckAnswerModule:
    def __init__(self):
        self._client = genai.Client()

    def check(
        self, question: str, true_answer: str, user_answer: str, is_highlighted: bool
    ) -> dict[str, any]:
        content = CHECK_ANSWER_PROMPT.format(
            question=question, true_answer=true_answer, user_answer=user_answer
        )
        content = wrap_prompt(content, is_highlighted)
        response = self._client.models.generate_content(
            model=GENERATOR_MODEL, contents=content
        )
        out = parse_response_to_json(response.text)
        return out
