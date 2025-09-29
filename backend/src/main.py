from fastapi import FastAPI

from controller.flashcard import FlashcardControlller
from controller.pathway import UserPathwayControlller
from controller.question import QuestionControlller


app = FastAPI()

flashcard_controller = FlashcardControlller()
pathway_controller = UserPathwayControlller()
question_controller = QuestionControlller()


app.add_api_route(
    "/api/flashcard/generate",
    flashcard_controller.create_flashcard,
    methods=["POST"],
)
app.add_api_route(
    "/api/user/pathway/create",
    pathway_controller.generate_pathway,
    methods=["POST"],
)
app.add_api_route(
    "/api/questions/retrieve",
    question_controller.retrieve_questions,
    methods=["POST"],
)
app.add_api_route(
    "/api/user/pathway/{username}",
    pathway_controller.get_user_pathway,
    methods=["GET"],
)
