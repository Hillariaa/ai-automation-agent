from openai import OpenAI
import os
from dotenv import load_dotenv

from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK
from app.tools.hilary_knowledge import hilary_intro, hilary_systems

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def classify_intent(message: str) -> str:

    prompt = f"""
You are the intent router for Hilary's AI Career Assistant.

Classify the user's message into ONE of the following intents.

Message:
{message}

Valid intents:

intro
systems
portfolio
cv
schedule
audio
tech
unknown

Return ONLY the intent word.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You classify user intent."},
            {"role": "user", "content": prompt},
        ],
    )

    content = response.choices[0].message.content or ""
    return content.strip().lower()


def automation_agent(message: str):

    message_lower = message.lower().strip()

    # deterministic routing (fast + reliable)

    if "audio" in message_lower or "hear" in message_lower:
        return {
            "message": "You can hear Hilary briefly introduce herself:",
            "actions": [
                {"label": "▶ Play Introduction", "url": "/audio/hilary_intro.mp3"}
            ],
        }

    if "portfolio" in message_lower:
        return {
            "message": "You can explore Hilary's AI portfolio here:",
            "actions": [{"label": "Open Portfolio", "url": PORTFOLIO_LINK}],
        }

    if "cv" in message_lower or "resume" in message_lower:
        return {
            "message": "You can download Hilary's CV here:",
            "actions": [{"label": "Download CV", "url": CV_LINK}],
        }

    if "schedule" in message_lower or "meeting" in message_lower:
        return {
            "message": "You can schedule a call with Hilary here:",
            "actions": [{"label": "Schedule Meeting", "url": CALENDLY_LINK}],
        }

    if (
        "stack" in message_lower
        or "tech" in message_lower
        or "technology" in message_lower
    ):
        return {
            "message": """
Hilary's AI engineering stack includes:

AI Systems
• OpenAI APIs
• LangGraph
• Retrieval-Augmented Generation (RAG)
• AI agents

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
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    # LLM classifier fallback

    intent = classify_intent(message)

    if intent == "intro":
        return hilary_intro()

    if intent == "systems":
        return hilary_systems()

    if intent == "tech":
        return {
            "message": """
Hilary builds applied AI systems using:

• Python
• FastAPI
• OpenAI APIs
• LangGraph
• Retrieval-Augmented Generation (RAG)
• Next.js
• TailwindCSS

Her work focuses on AI agents, automation systems,
and intelligent developer tools.
""",
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    return hilary_intro()
