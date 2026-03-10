from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK


def hilary_intro():

    return {
        "message": """
Hi — I'm Hilary's AI Career Agent.

Hilary is an Applied AI Engineer specializing in:

• LLM applications  
• Retrieval-Augmented Generation systems  
• Autonomous AI agents  

Would you like to learn more about Hilary's AI systems?
""",
        "actions": [
            {"label": "Learn About Hilary", "message": "yes"},
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Schedule Call", "url": CALENDLY_LINK},
        ],
    }


def hilary_systems():

    return {
        "message": """
Hilary has built several applied AI systems:

• AI Research Agent — autonomous research system using LangGraph

• AI Interview Intelligence — multimodal system analyzing interview recordings

• Knowledge Copilot — Retrieval-Augmented Generation assistant

• AI Automation Agent — recruiter automation system

And of course… me — the AI Career Agent you're speaking with now.

Would you like to explore Hilary's work?
""",
        "actions": [
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Schedule Call", "url": CALENDLY_LINK},
        ],
    }
