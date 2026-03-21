from app.tools.outreach_tools import PORTFOLIO_LINK, CV_LINK, CALENDLY_LINK


def hilary_intro():

    return {
        "message": """
Hi — explore Hilary’s AI work and projects.

This assistant lets you understand how she designs and builds real AI systems.

Ask anything or start below:
""",
        "actions": [
            {"label": "Key Projects", "message": "projects"},
            {"label": "Why hire Hilary", "message": "why hire"},
            {"label": "View Portfolio", "url": PORTFOLIO_LINK},
            {"label": "Download CV", "url": CV_LINK},
            {"label": "Discuss role fit (15 min)", "url": CALENDLY_LINK},
        ],
    }
