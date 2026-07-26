from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/info")
def info():
    return {
        "project": "Arslan AI Studio",
        "developer": "Emre",
        "version": "0.1.0",
        "time": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    }