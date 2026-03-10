from app.tools.hilary_knowledge import hilary_intro, hilary_systems
from app.tools.outreach_tools import (
    portfolio_response,
    cv_response,
    calendly_response,
)


def automation_agent(message: str):

    message = message.lower()

    # recruiter wants systems

    if message in ["yes", "learn", "learn more"]:
        return hilary_systems()

    # recruiter wants portfolio

    if "portfolio" in message:
        return portfolio_response()

    # recruiter wants cv

    if "cv" in message:
        return cv_response()

    # recruiter wants meeting

    if "schedule" in message or "call" in message or "meeting" in message:
        return calendly_response()

    # default intro

    return hilary_intro()
