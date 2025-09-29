from google import genai

from pymilvus import connections, Collection

from common.config import CONFIG
from common.constant import EMBEDDING_MODEL
from common.prompt import QUESTION_PROMPT
from common.utility import parse_response_to_json


class QuestionModule:
    def __init__(self):
        self._client = genai.Client()

        if not connections.has_connection(CONFIG.milvus.db_name):
            connections.connect(
                CONFIG.milvus.db_name,
                host=CONFIG.milvus.host,
                port=CONFIG.milvus.port,
            )

        self._collection = Collection(name=CONFIG.question_module.collection)

    def retrieve_questions(
        self, general_idea: str, topics: list[str], limit: int
    ) -> dict[str, any]:
        query = QUESTION_PROMPT.format(
            general_idea=general_idea,
            topics=" ; ".join(topics),
        )
        response = self._client.models.embed_content(
            model=EMBEDDING_MODEL, contents=query
        )
        vector = response.embeddings[0].values

        return self._collection.search(
            data=[vector],
            anns_field=CONFIG.question_module.anns_field,
            limit=CONFIG.question_module.limit,
            output_fields=CONFIG.question_module.output_fields,
        )
