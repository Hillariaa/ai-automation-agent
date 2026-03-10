from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK


def automation_agent(message: str):

    message = message.lower()

    if message in ["yes", "learn", "learn more"]:
        return {
            "message": """Hilary has built several applied AI systems:

• AI Research Agent
• AI Interview Intelligence
• Knowledge Copilot
• AI Automation Agent

Would you like to explore Hilary's work?""",
            "actions": [
                {"label": "View Portfolio", "url": PORTFOLIO_LINK},
                {"label": "Download CV", "url": CV_LINK},
                {"label": "Schedule Call", "url": CALENDLY_LINK},
            ],
        }

    if "portfolio" in message:
        return {
            "message": "You can explore Hilary's AI portfolio here:",
            "actions": [{"label": "Open Portfolio", "url": PORTFOLIO_LINK}],
        }

    if "cv" in message:
        return {
            "message": "You can download Hilary's CV here:",
            "actions": [{"label": "Download CV", "url": CV_LINK}],
        }

    if "schedule" in message:
        return {
            "message": "You can schedule a call with Hilary here:",
            "actions": [{"label": "Schedule Meeting", "url": CALENDLY_LINK}],
        }

    return {
        "message": """Hi — I'm Hilary's AI Career Agent.

Hilary is an Applied AI Engineer specializing in:

• LLM applications
• Retrieval-Augmented Generation systems
• Autonomous AI agents

Would you like to learn more about Hilary's AI systems?""",
        "actions": [
            {"label": "Learn About Hilary", "message": "yes"},
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Schedule Call", "url": CALENDLY_LINK},
        ],
    }
