from openai import OpenAI
import os
from dotenv import load_dotenv

from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK
from app.tools.hilary_knowledge import hilary_intro
from app.tools.github_projects import explain_projects
from app.db.memory import get_user

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------
# WHY HILARY (UPGRADED 🔥)
# -----------------------------
def why_hilary():

    return {
        "message": """
Why hire Hilary?

• Builds end-to-end AI systems — not just prototypes  
• Strong understanding of LLM applications, RAG, and agent design  
• Focuses on real-world usability, not just theory  
• Thinks in terms of systems, architecture, and outcomes  

She has built applied AI tools that simulate real workflows — including this assistant you're interacting with now.

This reflects how she would approach building AI systems in a real company environment.
""",
        "actions": [
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
        ],
    }


# -----------------------------
# RECRUITER INTRO (UPGRADED 🔥)
# -----------------------------
def recruiter_intro():

    return {
        "message": """
Hi — this assistant helps you quickly evaluate Hilary’s AI systems and engineering work.

You can explore real projects, understand system architecture, and assess how she builds production-style AI systems.

Start here:
""",
        "actions": [
            {"label": "Key Projects", "message": "projects"},
            {"label": "Why hire Hilary", "message": "why hire"},
            {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
        ],
    }


# -----------------------------
# SPECIFIC PROJECT EXPLANATION (UPGRADED)
# -----------------------------
def explain_specific_project(message_lower: str):

    if "research" in message_lower:
        return """
AI Research Agent

Problem:
Automates multi-step research workflows.

Architecture:
- LangGraph-based agent loop
- Retrieval pipelines for sourcing data
- LLM reasoning for synthesis

How it works:
The system gathers data, processes it step-by-step, and produces structured insights.

Why it matters:
Reduces manual research time and improves output consistency.
"""

    if "interview" in message_lower:
        return """
AI Interview Intelligence

Problem:
Manual interview analysis is slow and inconsistent.

Architecture:
- Speech-to-text pipeline
- LLM-based analysis

How it works:
Processes interviews, extracts insights, and evaluates communication.

Why it matters:
Enables scalable and consistent evaluation of candidates.
"""

    if "knowledge" in message_lower:
        return """
AI Knowledge Copilot

Problem:
Difficulty accessing and querying internal knowledge.

Architecture:
- Vector database
- Retrieval-Augmented Generation (RAG)

How it works:
Retrieves relevant documents and generates grounded responses.

Why it matters:
Improves accuracy and reduces hallucination risk.
"""

    if "automation" in message_lower:
        return """
AI Automation Agent

Problem:
Recruiter interactions are repetitive and manual.

Architecture:
- FastAPI backend
- AI routing logic
- UI integration

How it works:
Handles recruiter queries, provides information, and drives toward conversion.

Why it matters:
Turns static portfolios into interactive systems.
"""

    if "career" in message_lower or "ui" in message_lower:
        return """
AI Career Agent UI

Problem:
Traditional portfolios don’t demonstrate real system thinking.

Architecture:
- Next.js frontend
- FastAPI backend
- AI-driven interaction layer

How it works:
Allows recruiters to interact with an AI that explains Hilary’s work.

Why it matters:
Shows both engineering depth and product thinking.
"""

    return None


# -----------------------------
# MAIN AGENT
# -----------------------------
def automation_agent(user_id: str, message: str):

    user = get_user(user_id)
    message_lower = message.lower().strip()

    # -----------------------------
    # ENTRY
    # -----------------------------
    if message_lower in ["start", "hi", "hello"]:
        if user and user.get("source") == "outreach":
            return recruiter_intro()

        return hilary_intro()

    # -----------------------------
    # WHY HIRE
    # -----------------------------
    if "why hire" in message_lower:
        return why_hilary()

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
    # PORTFOLIO
    # -----------------------------
    if "portfolio" in message_lower:
        return {
            "message": "Explore Hilary's AI portfolio:",
            "actions": [{"label": "Open Portfolio", "url": PORTFOLIO_LINK}],
        }

    # -----------------------------
    # CV
    # -----------------------------
    if "cv" in message_lower or "resume" in message_lower:
        return {
            "message": "Download Hilary's CV:",
            "actions": [{"label": "Download CV", "url": CV_LINK}],
        }

    # -----------------------------
    # SCHEDULE
    # -----------------------------
    if "schedule" in message_lower or "meeting" in message_lower:
        return {
            "message": "Schedule time to discuss role fit:",
            "actions": [{"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK}],
        }

    # -----------------------------
    # PROJECTS
    # -----------------------------
    if "projects" in message_lower or "systems" in message_lower:
        explanation = explain_projects()

        return {
            "message": explanation,
            "actions": [
                {"label": "Why hire Hilary", "message": "why hire"},
                {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
            ],
        }

    # -----------------------------
    # SPECIFIC PROJECT
    # -----------------------------
    project = explain_specific_project(message_lower)

    if project:
        return {
            "message": project,
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
            ],
        }

    # -----------------------------
    # FALLBACK (AI)
    # -----------------------------
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are Hilary's AI career assistant. Be clear, confident, and focused on real-world AI system building.",
            },
            {"role": "user", "content": message},
        ],
    )

    return {
        "message": response.choices[0].message.content,
        "actions": [
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
        ],
    }
