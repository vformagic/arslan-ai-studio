from fastapi import APIRouter
from backend.app.services.gemini_service import ask_ai

router = APIRouter()


@router.get("/ask")
def ask(topic: str):
    cevap = ask_ai(topic)

    return {
        "topic": topic,
        "answer": cevap
    }