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

    # -----------------------------
    # FIRST LOAD
    # -----------------------------
    if message_lower == "start":
        return recruiter_intro() if user.get("source") == "outreach" else normal_intro()

    # track activity
    user["progress"].append(message_lower)
    update_intent(user_id)

    # -----------------------------
    # AUDIO
    # -----------------------------
    if "audio" in message_lower or "hear" in message_lower:
        return {
            "message": "You can hear Hilary introduce herself:",
            "actions": [
                {"label": "▶ Play Introduction", "url": "/audio/hilary_intro.mp3"}
            ],
        }

    # -----------------------------
    # TECH STACK
    # -----------------------------
    if "tech" in message_lower or "stack" in message_lower:
        return {
            "message": """
Hilary's AI engineering stack:

AI Systems
• OpenAI APIs  
• LangGraph  
• Retrieval-Augmented Generation  
• Autonomous agents  

Backend
• Python  
• FastAPI  

Frontend
• Next.js  
• React  
• TailwindCSS  

Infrastructure
• Vercel  
• Render  
""",
            "actions": [
                {"label": "View Portfolio", "message": "portfolio"},
                {"label": "Download CV", "message": "cv"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    # -----------------------------
    # PROJECTS
    # -----------------------------
    if "projects" in message_lower or "systems" in message_lower:
        return {
            "message": """
Key AI systems:

• AI Research Agent — autonomous research system  
• AI Interview Intelligence — analyzes interview recordings  
• Knowledge Copilot — RAG-based assistant  
• AI Automation Agent — recruiter interaction system  
""",
            "actions": [
                {"label": "View Portfolio", "message": "portfolio"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    # -----------------------------
    # WHY HIRE
    # -----------------------------
    if "why hire" in message_lower or "hire" in message_lower:
        return {
            "message": """
Hilary builds real-world AI systems, not just prototypes.

• Strong experience with LLMs, RAG, and agents  
• Focus on production-ready AI systems  
• Full-stack AI product development  
• Builds systems like this assistant end-to-end  

This assistant itself demonstrates that capability.
""",
            "actions": [
                {"label": "Download CV", "message": "cv"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    # -----------------------------
    # STANDARD ACTIONS
    # -----------------------------
    if "portfolio" in message_lower:
        return portfolio_response()

    if "cv" in message_lower or "resume" in message_lower:
        return cv_response()

    if "schedule" in message_lower or "meeting" in message_lower:
        return calendly_response()

    # -----------------------------
    # 🔥 AI FALLBACK (THIS MAKES IT SMART)
    # -----------------------------
    try:
        prompt = f"""
You are an AI career assistant representing Hilary, an Applied AI Engineer.

Answer the user's question clearly and professionally.

User question:
{message}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        answer = response.choices[0].message.content

        return {
            "message": answer,
            "actions": [
                {"label": "View Portfolio", "message": "portfolio"},
                {"label": "Download CV", "message": "cv"},
                {"label": "Schedule Call", "message": "schedule"},
            ],
        }

    except Exception:
        return normal_intro()
