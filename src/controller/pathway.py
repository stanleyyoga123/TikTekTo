from pydantic import BaseModel
from pymongo import MongoClient

from fastapi import UploadFile, File, Form

from module.pathway import UserPathwayModule

from common.config import CONFIG


class GeneratePathwayRequest(BaseModel):
    username: str
    role: str
    background: str
    additional: str
    objective: str


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

    def generate_pathway_from_file(
        self,
        username: str = Form(...),
        role: str = Form(...),
        objective: str = Form(...),
        document: UploadFile = File(..., description="PDF document"),
    ) -> dict:
        file = document.file.read()
        pathway = self._module.create_pathway_from_file(file, objective)
        data = {
            "username": username,
            "role": None,
            "background": None,
            "additional": None,
            "objective": objective,
            "pathway": pathway,
        }
        self._collection.insert_one(data)

        return {
            "status": 200,
            "data": pathway,
        }

    def get_user_pathway(self, username: str) -> dict:
        query = {"username": username}
        data = self._collection.find_one(query)
        return {"status": 200, "data": data["pathway"]}
