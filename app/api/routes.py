from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.automation_agent import automation_agent

router = APIRouter()


class AgentRequest(BaseModel):
    message: str


@router.post("/automate")
def automate(request: AgentRequest):

    result = automation_agent(request.message)

    return result
