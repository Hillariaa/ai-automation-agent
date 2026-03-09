from app.tools.hilary_knowledge import hilary_intro, hilary_projects
from app.tools.outreach_tools import portfolio_link, cv_link, calendly_link


def automation_agent(message: str, state: str):

    msg = message.lower()

    # Start conversation
    if msg == "start":
        return {"state": "intro", "message": hilary_intro}

    # Recruiter wants to learn more
    if msg in ["yes", "sure", "ok"]:
        return {"state": "knowledge", "message": hilary_projects}

    # Portfolio
    if "portfolio" in msg:
        return {
            "state": "portfolio",
            "message": f"View Hilary's portfolio here:\n\n{portfolio_link}",
        }

    # CV
    if "cv" in msg:
        return {
            "state": "cv",
            "message": f"You can download Hilary's CV here:\n\n{cv_link}",
        }

    # Schedule
    if "schedule" in msg or "book" in msg:
        return {
            "state": "schedule",
            "message": f"Great! Schedule a call with Hilary here:\n\n{calendly_link}",
        }

    return {
        "state": "end",
        "message": "Thank you for exploring Hilary's work. You're welcome back anytime.",
    }
