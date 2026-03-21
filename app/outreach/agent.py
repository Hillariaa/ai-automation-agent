# app/outreach/agent.py

from app.outreach.leads import get_leads
from app.outreach.sender import send_email

BASE_URL = "https://ai-career-agent-ui.vercel.app"


def generate_link(persona: str):
    return f"{BASE_URL}?source=outreach&persona={persona}&campaign=linkedin"


def generate_initial_message(lead: dict, link: str):
    """
    Message A (your chosen best message)
    """

    name = lead.get("name", "there")

    return f"""
Hi {name} — I built something a bit different.

It’s an interactive AI assistant that walks through my projects and systems as an AI Engineer.

Thought this might be a faster way to evaluate my work:
{link}
"""


def generate_followup_message(lead: dict):
    """
    Follow-up message
    """

    name = lead.get("name", "there")

    return f"""
Hi {name} — just wanted to follow up.

Curious if you had a chance to try the assistant.
Happy to walk through anything if helpful.
"""


def run_outreach():
    leads = get_leads()

    for lead in leads:
        link = generate_link(lead["role"])
        message = generate_initial_message(lead, link)

        send_email(lead["email"], message)


def run_followups():
    leads = get_leads()

    for lead in leads:
        message = generate_followup_message(lead)

        send_email(lead["email"], message)
