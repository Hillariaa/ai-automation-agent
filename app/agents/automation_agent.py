from openai import OpenAI
import os
from dotenv import load_dotenv

from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK
from app.tools.hilary_knowledge import hilary_intro
from app.tools.github_projects import explain_projects

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_specific_project(message_lower: str):

    if "research" in message_lower:
        return """
AI Research Agent

An autonomous research system built using LangGraph and OpenAI APIs.
It performs multi-step reasoning to gather information from sources,
analyze documents, and generate structured research outputs.

Technologies
Python
LangGraph
OpenAI APIs
Retrieval pipelines
"""

    if "interview" in message_lower:
        return """
AI Interview Intelligence

A multimodal AI system that analyzes interview recordings using
speech-to-text models and large language models.

The system extracts insights about candidate responses,
communication clarity, and key interview themes.

Technologies
Python
OpenAI APIs
Speech-to-text models
Natural language processing
"""

    if "knowledge" in message_lower:
        return """
AI Knowledge Copilot

A retrieval-augmented generation assistant that allows users
to query knowledge bases and receive grounded responses.

The system combines vector search with large language models
to synthesize accurate answers from documents.

Technologies
Python
Vector databases
OpenAI APIs
RAG architecture
"""

    if "automation" in message_lower:
        return """
AI Automation Agent

An AI assistant designed to automate recruiter interactions.
It explains Hilary's AI systems, shares portfolio links,
provides CV downloads, and allows scheduling meetings.

Technologies
FastAPI
Next.js
OpenAI APIs
Automation workflows
"""

    if "career" in message_lower or "ui" in message_lower:
        return """
AI Career Agent UI

A conversational interface that allows recruiters to interact
with Hilary's AI assistant and explore her AI engineering work.

The interface connects to a FastAPI backend that handles
AI reasoning, automation, and GitHub project explanations.

Technologies
Next.js
React
TailwindCSS
FastAPI
"""

    return None


def automation_agent(message: str):

    message_lower = message.lower().strip()

    # -----------------------------
    # AUDIO
    # -----------------------------

    if "audio" in message_lower or "hear" in message_lower:
        return {
            "message": "You can hear Hilary briefly introduce herself:",
            "actions": [
                {"label": "▶ Play Introduction", "url": "/audio/hilary_intro.mp3"}
            ],
        }

    # -----------------------------
    # PORTFOLIO
    # -----------------------------

    if "portfolio" in message_lower:
        return {
            "message": "You can explore Hilary's AI portfolio here:",
            "actions": [{"label": "Open Portfolio", "url": PORTFOLIO_LINK}],
        }

    # -----------------------------
    # CV
    # -----------------------------

    if "cv" in message_lower or "resume" in message_lower:
        return {
            "message": "You can download Hilary's CV here:",
            "actions": [{"label": "Download CV", "url": CV_LINK}],
        }

    # -----------------------------
    # SCHEDULE
    # -----------------------------

    if "schedule" in message_lower or "meeting" in message_lower:
        return {
            "message": "You can schedule a call with Hilary here:",
            "actions": [{"label": "Schedule Meeting", "url": CALENDLY_LINK}],
        }

    # -----------------------------
    # TECH STACK
    # -----------------------------

    if (
        "stack" in message_lower
        or "tech" in message_lower
        or "technology" in message_lower
    ):
        return {
            "message": """
Hilary's AI engineering stack includes

AI Systems
OpenAI APIs
LangGraph
Retrieval-Augmented Generation
Autonomous AI agents

Backend
Python
FastAPI

Frontend
Next.js
React
TailwindCSS

Infrastructure
Vercel
Render
""",
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    # -----------------------------
    # GENERAL PROJECT QUESTIONS
    # -----------------------------

    if (
        "projects" in message_lower
        or "systems" in message_lower
        or "github" in message_lower
    ):
        explanation = explain_projects()

        return {
            "message": explanation,
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    # -----------------------------
    # SPECIFIC PROJECT QUESTIONS
    # -----------------------------

    project_explanation = explain_specific_project(message_lower)

    if project_explanation:
        return {
            "message": project_explanation.strip(),
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
            ],
        }

    # -----------------------------
    # DEFAULT
    # -----------------------------

    return hilary_intro()
