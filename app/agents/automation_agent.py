from openai import OpenAI
import os
from dotenv import load_dotenv

from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK
from app.tools.hilary_knowledge import hilary_intro
from app.tools.github_projects import explain_projects

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_specific_project(project: str):

    explanations = {
        "research": """
AI Research Agent

An autonomous research system built using LangGraph and OpenAI APIs.
The agent performs multi-step reasoning, retrieves information from external
sources, and generates structured research outputs automatically.

Technologies: Python, LangGraph, OpenAI APIs, Retrieval systems.
""",
        "interview": """
AI Interview Intelligence

A multimodal AI system that analyzes interview recordings using speech-to-text
and large language models. It generates structured insights about candidate
responses, communication clarity, and key themes discussed in interviews.

Technologies: Python, OpenAI APIs, speech-to-text models, NLP analysis.
""",
        "knowledge": """
AI Knowledge Copilot

A retrieval-augmented generation assistant that allows users to query
knowledge bases and receive grounded answers. It combines vector search
with large language models to synthesize accurate responses.

Technologies: Python, vector databases, OpenAI APIs, RAG architecture.
""",
        "automation": """
AI Automation Agent

An AI assistant designed to automate recruiter interactions.
It explains Hilary’s AI systems, shares her portfolio, provides her CV,
and allows recruiters to schedule calls through an intelligent interface.

Technologies: FastAPI, Next.js, OpenAI APIs, automation workflows.
""",
        "career": """
AI Career Agent UI

A modern conversational interface built with Next.js that allows recruiters
to interact with Hilary’s AI assistant. The UI connects to a FastAPI backend
that powers the AI reasoning and automation logic.

Technologies: Next.js, React, TailwindCSS, FastAPI.
""",
    }

    for key in explanations:
        if key in project:
            return explanations[key]

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
    # SPECIFIC PROJECT EXPLANATION
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
    # PROJECT OVERVIEW
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
    # DEFAULT
    # -----------------------------
    return hilary_intro()
