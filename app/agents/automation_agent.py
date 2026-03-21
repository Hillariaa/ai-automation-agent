from datetime import datetime
import os
from openai import OpenAI

from app.db.memory import get_user, update_user, update_intent
from app.tools.outreach_tools import (
    portfolio_response,
    cv_response,
    calendly_response,
)
from app.tools.hilary_knowledge import recruiter_intro, normal_intro

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def automation_agent(user_id: str, message: str):

    user = get_user(user_id)

    if not user:
        return {"message": "User not found.", "actions": []}

    update_user(user_id, "last_active", datetime.utcnow())

    message_lower = message.lower().strip()

    # FIRST LOAD
    if message_lower == "start":
        return recruiter_intro() if user.get("source") == "outreach" else normal_intro()

    user["progress"].append(message_lower)
    update_intent(user_id)

    #  AUDIO
    if "audio" in message_lower or "hear" in message_lower or "intro" in message_lower:
        return {
            "message": "You can hear Hilary introduce herself:",
            "actions": [
                {
                    "label": "▶ Play Introduction",
                    "url": "https://ai-career-agent-ui.vercel.app/audio/hilary_intro.mp3",
                }
            ],
        }

    # TECH STACK
    if "tech" in message_lower or "stack" in message_lower:
        return {
            "message": """
Hilary's AI engineering stack:

AI Systems
• OpenAI APIs  
• LangGraph  
• RAG systems  
• Autonomous agents  

Backend
• Python  
• FastAPI  

Frontend
• Next.js  
• React  
• TailwindCSS  
""",
            "actions": [
                {"label": "Portfolio", "message": "portfolio"},
                {"label": "Download CV", "message": "cv"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    if "portfolio" in message_lower:
        return portfolio_response()

    if "cv" in message_lower:
        return cv_response()

    if "schedule" in message_lower:
        return calendly_response()

    # AI fallback
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Answer professionally: {message}"}],
        )

        return {
            "message": response.choices[0].message.content,
            "actions": [
                {"label": "Portfolio", "message": "portfolio"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    except Exception:
        return normal_intro()
