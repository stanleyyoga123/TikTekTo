from pydantic import BaseModel
from pymongo import MongoClient

from module.pathway import UserPathwayModule

from common.config import CONFIG


class GeneratePathwayRequest(BaseModel):
    username: str
    role: str
    background: str
    additional: str
    objective: str


class GetUserPathwayRequest(BaseModel):
    username: str


class UserPathwayControlller:
    def __init__(self):
        self._module = UserPathwayModule()
        mongo = MongoClient(CONFIG.mongo.uri)
        db = mongo[CONFIG.user_controller.db_name]
        self._collection = db[CONFIG.user_controller.collection]

    def generate_pathway(self, body: GeneratePathwayRequest) -> dict:
        pathway = self._module.create_pathway(
            body.role, body.background, body.additional, body.objective
        )
        data = {
            "username": body.username,
            "role": body.role,
            "background": body.background,
            "additional": body.additional,
            "objective": body.objective,
            "pathway": pathway,
        }
        self._collection.insert_one(data)

        return {
            "status": 200,
            "data": pathway,
        }

    def get_user_pathway(self, body: GetUserPathwayRequest) -> dict:
        data = self._collection.find_one({"username": body.username})
        return data["pathway"]
