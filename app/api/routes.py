from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

from app.agents.automation_agent import automation_agent
from app.db.memory import create_user, USER_DB

router = APIRouter()


class InitRequest(BaseModel):
    source: str | None = None
    persona: str | None = None
    campaign: str | None = None


class AgentRequest(BaseModel):
    message: str
    user_id: str


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


@router.post("/automate")
def automate(request: AgentRequest):
    return automation_agent(request.user_id, request.message)


#  NEW: DASHBOARD ENDPOINT
@router.get("/dashboard")
def dashboard():
    return {"total_users": len(USER_DB), "users": list(USER_DB.values())}
