from datetime import datetime

from app.db.memory import get_user, update_user, update_intent
from app.tools.outreach_tools import (
    portfolio_response,
    cv_response,
    calendly_response,
)
from app.tools.hilary_knowledge import recruiter_intro, normal_intro


def automation_agent(user_id: str, message: str):

    user = get_user(user_id)

    if not user:
        return {"message": "User not found.", "actions": []}

    update_user(user_id, "last_active", datetime.utcnow())

    message_lower = message.lower().strip()

    # FIRST LOAD
    if message_lower == "start":
        return recruiter_intro() if user.get("source") == "outreach" else normal_intro()

    # track activity
    user["progress"].append(message_lower)
    update_intent(user_id)

    # recruiter actions
    if "why hire" in message_lower:
        return {
            "message": """
Hilary builds real-world AI systems, not just prototypes.

• LLM systems, RAG, agents  
• Production-focused engineering  
• Full-stack AI products  
""",
            "actions": [
                {"label": "Download CV", "url": cv_response()["actions"][0]["url"]},
                {
                    "label": "Schedule Call",
                    "url": calendly_response()["actions"][0]["url"],
                },
            ],
        }

    if "projects" in message_lower:
        return {
            "message": """
Key systems:

• AI Research Agent  
• AI Interview Intelligence  
• Knowledge Copilot  
• AI Automation Agent  
""",
            "actions": [
                {
                    "label": "View Portfolio",
                    "url": portfolio_response()["actions"][0]["url"],
                },
            ],
        }

    if "portfolio" in message_lower:
        return portfolio_response()

    if "cv" in message_lower:
        return cv_response()

    if "schedule" in message_lower:
        return calendly_response()

    return normal_intro()
