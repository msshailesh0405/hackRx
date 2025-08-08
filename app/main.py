# trigger redeploy
from fastapi import FastAPI, Header
from app.config import settings
from app.models import HackRxRequest, HackRxResponse
from app.utils import validate_token
from app.services import process_questions

app = FastAPI(title="HackRx Webhook")

# ✅ Health check route
@app.get("/")
def home():
    return {"message": "Hello Render!"}

# ✅ Webhook route
@app.post("/api/v1/hackrx/run", response_model=HackRxResponse)
async def hackrx_run(payload: HackRxRequest, authorization: str = Header(...)):
    # 1 Validate token
    validate_token(authorization, settings.TEAM_TOKEN)

    # 2 Process questions
    answers = process_questions(payload.documents, payload.questions)

    # 3 Return structured response
    return HackRxResponse(answers=answers)