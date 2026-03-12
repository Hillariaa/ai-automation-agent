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

Intents:

intro
User wants to know who Hilary is.

systems
User asks about AI systems, projects, or what she has built.

portfolio
User wants to view Hilary's portfolio or see her work.

cv
User asks for Hilary's CV or resume.

schedule
User wants to schedule a meeting or call.

audio
User wants to hear Hilary introduce herself or mentions audio.

tech
User asks about Hilary's tech stack, tools, or technologies she uses.

unknown
Anything else.

Return ONLY the intent name.
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

    intent = classify_intent(message)

    if intent == "intro":
        return hilary_intro()

    if intent == "systems":
        return hilary_systems()

    if intent == "portfolio":
        return {
            "message": "You can explore Hilary's AI portfolio here:",
            "actions": [{"label": "Open Portfolio", "url": PORTFOLIO_LINK}],
        }

    if intent == "cv":
        return {
            "message": "You can download Hilary's CV here:",
            "actions": [{"label": "Download CV", "url": CV_LINK}],
        }

    if intent == "schedule":
        return {
            "message": "You can schedule a call with Hilary here:",
            "actions": [{"label": "Schedule Meeting", "url": CALENDLY_LINK}],
        }

    if intent == "audio":
        return {
            "message": "You can hear Hilary briefly introduce herself and explain the AI systems she builds:",
            "actions": [
                {"label": "▶ Play Introduction", "url": "/audio/hilary_intro.mp3"}
            ],
        }

    if intent == "tech":
        return {
            "message": """
Hilary's AI engineering stack includes:

AI & LLM Systems
• OpenAI APIs
• LangGraph
• Retrieval-Augmented Generation (RAG)
• AI agent architectures
• Whisper speech processing

Backend
• Python
• FastAPI
• API-based AI services

Frontend
• Next.js
• React
• TailwindCSS

Infrastructure
• Vercel deployment
• Render backend services

These technologies power systems like her Research Agent,
Interview Intelligence system, Knowledge Copilot, and
AI Career Assistant.
""",
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    return hilary_intro()
