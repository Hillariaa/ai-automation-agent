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
    # FIRST LOAD (CONTEXT-AWARE)
    # -----------------------------
    if message_lower == "start":
        return recruiter_intro() if user.get("source") == "outreach" else normal_intro()

    # -----------------------------
    # TRACK USER ACTIVITY
    # -----------------------------
    user["progress"].append(message_lower)
    update_intent(user_id)

    # -----------------------------
    # AUDIO
    # -----------------------------
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
• Retrieval-Augmented Generation (RAG)  
• Autonomous AI agents  

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
    # PROJECTS / SYSTEMS
    # -----------------------------
    if "project" in message_lower or "system" in message_lower:
        return {
            "message": """
Hilary has built several applied AI systems:

• AI Research Agent — autonomous multi-step research system  
• AI Interview Intelligence — analyzes interview recordings  
• Knowledge Copilot — Retrieval-Augmented Generation assistant  
• AI Automation Agent — recruiter-facing AI system  

Each system focuses on real-world AI applications, not just prototypes.
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
Hilary builds production-ready AI systems, not just demos.

• Strong experience with LLMs, RAG, and agent architectures  
• Focus on real-world AI applications  
• Full-stack AI engineering (backend + frontend)  
• Builds complete AI products end-to-end  

This assistant itself is an example of that capability.
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
    #  AI FALLBACK (FIXED PROPERLY)
    # -----------------------------
    try:
        context = f"""
You are Hilary's AI Career Assistant.

Hilary is an Applied AI Engineer specializing in:
- LLM applications
- Retrieval-Augmented Generation (RAG)
- Autonomous AI agents

IMPORTANT RULES:
- Always assume the user is asking about Hilary
- Never ask "which Hilary"
- Never act confused
- Speak confidently and clearly
- Answer like you're helping a recruiter evaluate her

User type: {user.get("source")}
Persona: {user.get("persona")}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message},
            ],
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

    except Exception as e:
        print("AI fallback error:", e)
        return normal_intro()
