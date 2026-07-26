from backend.app.routes.ai import router as ai_router
from fastapi import FastAPI
from backend.app.routes.system import router as system_router
app = FastAPI(
    title="Arslan AI Studio",
    version="0.1.0"
)

app.include_router(system_router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "Arslan AI Studio çalışıyor."
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }