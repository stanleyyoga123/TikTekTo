from pymongo import MongoClient

from module.pathway import UserPathwayModule

from common.config import CONFIG


class UserPathwayControlller:
    def __init__(self):
        self._module = UserPathwayModule()
        mongo = MongoClient(CONFIG.mongo.uri)
        db = mongo[CONFIG.user_controller.db_name]
        self._collection = db[CONFIG.user_controller.collection]

    def generate_pathway(
        self, username: str, role: str, background: str, additional: str, objective: str
    ):
        pathway = self._module.create_pathway(role, background, additional, objective)
        self._collection.insert_one(
            {
                "username": username,
                "role": role,
                "background": background,
                "additional": additional,
                "objective": objective,
                "pathway": pathway,
            }
        )

        return pathway
