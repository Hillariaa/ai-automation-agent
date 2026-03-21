from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK


def recruiter_intro():
    return {
        "message": """
Hi — this assistant helps you evaluate Hilary's AI systems and engineering work.

Start here:
""",
        "actions": [
            {"label": "Why hire Hilary", "message": "why hire hilary"},
            {"label": "Key projects", "message": "projects"},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Schedule Call", "url": CALENDLY_LINK},
        ],
    }


def normal_intro():
    return {
        "message": """
Hi — explore Hilary's AI work and projects.

Ask anything or browse below.
""",
        "actions": [
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Schedule Call", "url": CALENDLY_LINK},
        ],
    }
