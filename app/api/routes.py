from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

from app.agents.automation_agent import automation_agent
from app.db.memory import (
    create_user,
    get_user,
    update_user,
    USER_DB,
    add_feedback,
)

router = APIRouter()


# -----------------------------
# MODELS
# -----------------------------
class InitRequest(BaseModel):
    source: str | None = None
    persona: str | None = None
    campaign: str | None = None


class AgentRequest(BaseModel):
    message: str
    user_id: str


class EmailCaptureRequest(BaseModel):
    user_id: str
    email: str


class FeedbackRequest(BaseModel):
    user_id: str
    feedback: str


# -----------------------------
# INIT USER
# -----------------------------
@router.post("/init")
def init_user(req: InitRequest):

    user_id = str(uuid4())

    create_user(
        user_id,
        {
            "source": req.source,
            "persona": req.persona,
            "campaign": req.campaign,
        },
    )

    return {"user_id": user_id}


# -----------------------------
# AGENT
# -----------------------------
@router.post("/automate")
def automate(request: AgentRequest):
    return automation_agent(request.user_id, request.message)


# -----------------------------
# EMAIL
# -----------------------------
@router.post("/capture-email")
def capture_email(req: EmailCaptureRequest):

    user = get_user(req.user_id)

    if not user:
        return {"status": "error"}

    update_user(req.user_id, "email", req.email)

    return {"status": "success"}


# -----------------------------
# FEEDBACK (NEW)
# -----------------------------
@router.post("/feedback")
def feedback(req: FeedbackRequest):

    user = get_user(req.user_id)

    if not user:
        return {"status": "error"}

    add_feedback(req.user_id, req.feedback)

    return {"status": "success"}


# -----------------------------
# DASHBOARD
# -----------------------------
@router.get("/dashboard")
def dashboard():
    return {
        "total_users": len(USER_DB),
        "users": list(USER_DB.values()),
    }
